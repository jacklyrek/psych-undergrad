#!/usr/bin/env python3
"""Compile the wiki + research readings and the item bank into the web app's content bundle.

The mobile app (`docs/`) is a static PWA with no build toolchain — no npm, no bundler. So this
script does the one job that genuinely needs doing ahead of time: turning 125 markdown files into
ready-to-inject HTML, with wikilinks resolved to in-app routes and `[S3]`-style citations wired to
the source note they point at. Rendering markdown here rather than in the browser means the phone
ships zero parser, the wikilink graph is validated at build time (a broken `[[link]]` is a visible
bug, not a dead tap), and backlinks can be computed across the whole corpus.

Outputs (all under docs/content/, all read-only to the app):
    readings.json   every wiki/ + research/ page: frontmatter, rendered HTML, plain text for
                    search, outbound links, backlinks, and the page's own source notes
    items.json      a copy of items/build/items.json (the app never reads outside docs/)
    version.json    content hash + timestamp; the service worker uses it to bust its cache

Stdlib only, like the rest of the pipeline. Run after build_items.py:
    python apps/build_items.py && python apps/build_web.py
"""
from __future__ import annotations

import hashlib
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_DIR = ROOT / "wiki"
RESEARCH_DIR = ROOT / "research"
ITEMS_JSON = ROOT / "items" / "build" / "items.json"
DOCS_DIR = ROOT / "docs"
OUT_DIR = DOCS_DIR / "content"

# Bumped when the renderer changes so the content hash (and thus the app's cache) turns over even
# if no markdown edited. Keep in step with meaningful changes to the rendering below.
RENDERER_VERSION = "1"


# ---------------------------------------------------------------- frontmatter

FRONTMATTER = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n?", re.DOTALL)


def parse_frontmatter(text: str) -> tuple[dict, str]:
    """Split YAML frontmatter off a page. Deliberately a minimal parser — the pages only ever use
    `key: scalar` and `key: [a, b, c]`, and the rest of this repo is stdlib-only (no PyYAML)."""
    m = FRONTMATTER.match(text)
    if not m:
        return {}, text
    meta: dict = {}
    for line in m.group(1).splitlines():
        line = line.strip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, raw = line.partition(":")
        meta[key.strip()] = _scalar(raw.strip())
    return meta, text[m.end():]


def _scalar(raw: str):
    if raw.startswith("[") and raw.endswith("]"):
        inner = raw[1:-1].strip()
        return [_scalar(p.strip()) for p in inner.split(",") if p.strip()] if inner else []
    if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in "\"'":
        return raw[1:-1]
    if raw.lower() in ("true", "false"):
        return raw.lower() == "true"
    if re.fullmatch(r"-?\d+", raw):
        return int(raw)
    return raw


# ---------------------------------------------------------------- inline markdown

CODE_SPAN = re.compile(r"`([^`]+)`")
WIKILINK = re.compile(r"\[\[([^\]|#]*?)(?:#([^\]|]+?))?(?:\s*\|\s*(.+?))?\]\]")
# A whole wikilink, used to mask them while splitting table rows on "|".
WIKI_SPAN = re.compile(r"\[\[[^\]]*\]\]")
MD_LINK = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BOLD = re.compile(r"\*\*(.+?)\*\*", re.DOTALL)
ITALIC = re.compile(r"(?<![\w*])\*([^*\n]+?)\*(?![\w*])")
# The research files emphasise with underscores. The word-character guards keep snake_case names
# like `source_page` and `review_log.csv` from being mistaken for emphasis.
ITALIC_ = re.compile(r"(?<![\w_])_([^_\n]+?)_(?![\w_])")
# Citations are the wiki's own convention: [S3] into the unit's sources file, plus a handful of
# older pages using bare [3]. Matched after link processing so [text](url) is never eaten.
CITATION = re.compile(r"\[(S?\d+)\]")
SLUG_STRIP = re.compile(r"[^a-z0-9]+")


def slugify(text: str) -> str:
    return SLUG_STRIP.sub("-", strip_inline(text).lower()).strip("-")


def strip_inline(text: str) -> str:
    """Markdown source -> bare words, for heading ids and search text."""
    text = WIKILINK.sub(lambda m: (m.group(3) or m.group(1)), text)
    text = MD_LINK.sub(r"\1", text)
    text = CODE_SPAN.sub(r"\1", text)
    return text.replace("**", "").replace("*", "").strip()


class Ctx:
    """Per-corpus rendering context: which slugs exist (so a bad wikilink can be flagged rather
    than silently producing a dead link), plus a per-page collector for outbound links."""

    def __init__(self, known_slugs: set[str]):
        self.known = known_slugs
        self.outbound: set[str] = set()
        self.broken: list[str] = []
        self.slug = ""


def inline(text: str, ctx: Ctx) -> str:
    """Render inline markdown to HTML. Order matters: escape first so nothing user-authored can
    inject markup, then lift code spans out into placeholders so their contents are left alone by
    every later pass, then links (before citations, so bracket syntax isn't ambiguous)."""
    text = html.escape(text, quote=False)

    stash: list[str] = []

    def keep(markup: str) -> str:
        stash.append(markup)
        return f"\x00{len(stash) - 1}\x00"

    text = CODE_SPAN.sub(lambda m: keep(f"<code>{m.group(1)}</code>"), text)
    text = WIKILINK.sub(lambda m: keep(_wikilink(m, ctx)), text)
    text = MD_LINK.sub(lambda m: keep(_mdlink(m, ctx)), text)
    text = BOLD.sub(r"<strong>\1</strong>", text)
    text = ITALIC.sub(r"<em>\1</em>", text)
    text = ITALIC_.sub(r"<em>\1</em>", text)
    # A tap target, not an anchor: the app uses hash routing, so a real href="#..." would be
    # swallowed by the router. JS reads data-cite and shows the source note inline.
    text = CITATION.sub(
        lambda m: keep(f'<button class="cite" data-cite="{m.group(1)}">{m.group(1)}</button>'), text)

    # Placeholders nest — a link whose label is a code span stashes markup that still contains the
    # code span's own placeholder, and re.sub does not rescan what it substituted in. Every wiki
    # page's Sources line is exactly that shape, so restore until the text comes back clean.
    for _ in range(6):
        if "\x00" not in text:
            break
        text = re.sub(r"\x00(\d+)\x00", lambda m: stash[int(m.group(1))], text)
    return text


def _wikilink(m: re.Match, ctx: Ctx) -> str:
    target, anchor, label = m.group(1).strip(), m.group(2), m.group(3)
    label = (label or target or anchor or "").strip()
    # [[#Some Heading | label]] — an anchor with no target is a jump within the current page.
    if not target and anchor:
        return f'<a class="wl" href="#/read/{ctx.slug}?h={slugify(anchor)}">{html.escape(label)}</a>'
    if target not in ctx.known:
        ctx.broken.append(target)
        return f'<span class="wl-broken" title="no page named {target}">{html.escape(label)}</span>'
    ctx.outbound.add(target)
    frag = f"?h={slugify(anchor)}" if anchor else ""
    return f'<a class="wl" href="#/read/{target}{frag}">{html.escape(label)}</a>'


def _mdlink(m: re.Match, ctx: Ctx) -> str:
    label, href = m.group(1), m.group(2).strip()
    if href.startswith(("http://", "https://")):
        return (f'<a class="ext" href="{html.escape(href, quote=True)}" '
                f'target="_blank" rel="noopener noreferrer">{label}</a>')
    # Relative repo links: ../research/unit01-...-sources.md and friends. Route them in-app when
    # the target made it into the bundle; otherwise keep the words and drop the dead link.
    slug = re.sub(r"\.md$", "", Path(href.split("#")[0]).name)
    if slug in ctx.known:
        ctx.outbound.add(slug)
        return f'<a class="wl" href="#/read/{slug}">{label}</a>'
    return label


# ---------------------------------------------------------------- block markdown

HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
HRULE = re.compile(r"^\s*([-*_])\1{2,}\s*$")
ULI = re.compile(r"^(\s*)[-*]\s+(.*)$")
OLI = re.compile(r"^(\s*)(\d+)\.\s+(.*)$")
TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$")


def render_blocks(lines: list[str], ctx: Ctx) -> tuple[str, list[dict]]:
    """Walk the page line by line, emitting HTML. Returns (html, headings) — headings drive the
    in-page contents menu. Paragraphs join their lines with a space, which is what makes the
    hard-wrapped older pages render as continuous prose."""
    out: list[str] = []
    headings: list[dict] = []
    para: list[str] = []
    i = 0

    def flush() -> None:
        if para:
            out.append(f"<p>{inline(' '.join(para), ctx)}</p>")
            para.clear()

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            flush()
            i += 1
            continue

        m = HEADING.match(line)
        if m:
            flush()
            level, raw = len(m.group(1)), m.group(2).strip()
            hid = slugify(raw) or f"h{len(headings)}"
            headings.append({"level": level, "text": strip_inline(raw), "id": hid})
            out.append(f'<h{level} id="{hid}">{inline(raw, ctx)}</h{level}>')
            i += 1
            continue

        if HRULE.match(line):
            flush()
            out.append("<hr>")
            i += 1
            continue

        if line.lstrip().startswith(">"):
            flush()
            block, i = _take_while(lines, i, lambda ln: ln.lstrip().startswith(">"))
            inner = [re.sub(r"^\s*>\s?", "", ln) for ln in block]
            body, _ = render_blocks(inner, ctx)
            out.append(f"<blockquote>{body}</blockquote>")
            continue

        if line.lstrip().startswith("|"):
            flush()
            block, i = _take_while(lines, i, lambda ln: ln.lstrip().startswith("|"))
            out.append(_table(block, ctx))
            continue

        if ULI.match(line) or OLI.match(line):
            flush()
            block, i = _take_while(
                lines, i,
                lambda ln: bool(ULI.match(ln) or OLI.match(ln) or (ln.startswith((" ", "\t")) and ln.strip())))
            out.append(_list(block, ctx))
            continue

        para.append(line.strip())
        i += 1

    flush()
    return "".join(out), headings


def _take_while(lines: list[str], start: int, pred) -> tuple[list[str], int]:
    i = start
    while i < len(lines) and pred(lines[i]):
        i += 1
    return lines[start:i], i


def _split_row(row: str) -> list[str]:
    """Split one table row into cells. A piped wikilink — `[[slug | label]]` — is common inside
    these tables, and its `|` is not a cell boundary, so mask whole wikilinks while splitting."""
    stash: list[str] = []

    def mask(m: re.Match) -> str:
        stash.append(m.group(0))
        return f"\x01{len(stash) - 1}\x01"

    masked = WIKI_SPAN.sub(mask, row)
    cells = [c.strip() for c in masked.split("|")]
    return [re.sub(r"\x01(\d+)\x01", lambda m: stash[int(m.group(1))], c) for c in cells]


def _table(block: list[str], ctx: Ctx) -> str:
    """Render a GFM pipe table. The separator row supplies per-column alignment."""
    rows = [r.strip().strip("|") for r in block]
    cells = [_split_row(r) for r in rows]
    aligns: list[str] = []
    header = cells[0]
    body = cells[1:]
    if len(block) > 1 and TABLE_SEP.match(block[1]):
        for spec in cells[1]:
            left, right = spec.startswith(":"), spec.endswith(":")
            aligns.append("center" if left and right else "right" if right else "left")
        body = cells[2:]

    def td(tag: str, row: list[str]) -> str:
        out = []
        for n, c in enumerate(row):
            a = aligns[n] if n < len(aligns) and aligns[n] != "left" else ""
            style = f' style="text-align:{a}"' if a else ""
            out.append(f"<{tag}{style}>{inline(c, ctx)}</{tag}>")
        return "<tr>" + "".join(out) + "</tr>"

    head = f"<thead>{td('th', header)}</thead>"
    rows_html = "".join(td("td", r) for r in body)
    # Wrapped so a wide table scrolls inside itself instead of forcing the page sideways on a phone.
    return f'<div class="table-wrap"><table>{head}<tbody>{rows_html}</tbody></table></div>'


def _list(block: list[str], ctx: Ctx) -> str:
    """Render a list, supporting one level of nesting (all this corpus uses). Continuation lines
    indented under an item are folded into that item's text."""
    entries: list[dict] = []
    for line in block:
        m_ul, m_ol = ULI.match(line), OLI.match(line)
        m = m_ul or m_ol
        if m:
            indent = len(m.group(1).expandtabs(4))
            text = m.group(2) if m_ul else m.group(3)
            entries.append({"indent": indent, "ordered": bool(m_ol), "parts": [text.strip()]})
        elif entries:
            entries[-1]["parts"].append(line.strip())

    if not entries:
        return ""

    base = min(e["indent"] for e in entries)
    tag = "ol" if entries[0]["ordered"] else "ul"
    out = [f"<{tag}>"]
    open_nested = False
    for e in entries:
        body = inline(" ".join(e["parts"]), ctx)
        if e["indent"] > base:
            if not open_nested:
                nested_tag = "ol" if e["ordered"] else "ul"
                out.append(f"<{nested_tag}>")
                open_nested = nested_tag
            out.append(f"<li>{body}</li>")
        else:
            if open_nested:
                out.append(f"</{open_nested}>")
                open_nested = False
            out.append(f"<li>{body}</li>")
    if open_nested:
        out.append(f"</{open_nested}>")
    out.append(f"</{tag}>")
    return "".join(out)


# ---------------------------------------------------------------- source notes

def extract_sources(body: str) -> dict[str, str]:
    """Pull `[S1] StatPearls, ... [S5] Penn State, ...` out of a page's `## Sources` section so the
    app can show the note when a citation badge is tapped, instead of just scrolling there."""
    m = re.search(r"^##+\s*Sources\s*$(.*?)(?=^##\s|\Z)", body, re.MULTILINE | re.DOTALL)
    if not m:
        return {}
    section = m.group(1)
    hits = list(CITATION.finditer(section))
    notes: dict[str, str] = {}
    for n, hit in enumerate(hits):
        end = hits[n + 1].start() if n + 1 < len(hits) else len(section)
        note = strip_inline(section[hit.end():end]).strip(" .;\n")
        if note:
            notes[hit.group(1)] = re.sub(r"\s+", " ", note)
    return notes


TAG_STRIP = re.compile(r"<[^>]+>")


def plain_text(rendered: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(TAG_STRIP.sub(" ", rendered))).strip()


# ---------------------------------------------------------------- page assembly

def collect_sources() -> list[tuple[str, Path]]:
    """(collection, path) for every page that goes in the bundle. README files are scaffolding."""
    pages = [("wiki", p) for p in sorted(WIKI_DIR.glob("*.md")) if p.name != "README.md"]
    pages += [("research", p) for p in sorted(RESEARCH_DIR.glob("*.md")) if p.name != "README.md"]
    return pages


UNIT_FROM_SLUG = re.compile(r"^unit0*(\d+)")
AUX_FROM_SLUG = re.compile(r"^(aux-[a-z0-9-]+?)(?:-sources)?$")


def infer_unit(slug: str, meta: dict) -> str:
    """Unit label for grouping in the reader. Frontmatter wins; otherwise read it off the filename,
    matching the convention build_items.py already uses (unitNN -> "NN", aux-<slug> kept whole)."""
    if meta.get("unit") not in (None, ""):
        return str(meta["unit"])
    # Elective concept pages carry `module:` instead of `unit:` (CLAUDE.md's aux- namespace). Without
    # this they group under no unit at all, which in the reader means they are not listed anywhere.
    if meta.get("module"):
        return f"aux-{meta['module']}"
    m = UNIT_FROM_SLUG.match(slug)
    if m:
        return str(int(m.group(1)))
    m = AUX_FROM_SLUG.match(slug)
    if m:
        return m.group(1)
    return ""


def build_pages() -> list[dict]:
    sources = collect_sources()
    known = {p.stem for _, p in sources}
    ctx = Ctx(known)
    pages: list[dict] = []
    broken: list[tuple[str, str]] = []

    for collection, path in sources:
        raw = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(raw)
        ctx.outbound, ctx.broken, ctx.slug = set(), [], path.stem

        rendered, headings = render_blocks(body.splitlines(), ctx)
        broken += [(path.stem, t) for t in ctx.broken]

        title = meta.get("title") or next(
            (h["text"] for h in headings if h["level"] == 1), path.stem)
        pages.append({
            "slug": path.stem,
            "collection": collection,
            "title": title,
            "type": meta.get("type") or ("sources" if collection == "research" else "concept"),
            "unit": infer_unit(path.stem, meta),
            "tags": meta.get("tags") or [],
            "cluster": meta.get("cluster") or "",
            "source_units": [str(u) for u in (meta.get("source_units") or [])],
            "track": meta.get("track") or "",
            "html": rendered,
            "text": plain_text(rendered),
            "headings": [h for h in headings if h["level"] in (2, 3)],
            "sources": extract_sources(body),
            "outbound": sorted(ctx.outbound),
        })

    # Backlinks: the reverse edge of the wikilink graph. Cheap here, impossible on the phone
    # without shipping the whole corpus to every page view.
    inbound: dict[str, set[str]] = {p["slug"]: set() for p in pages}
    for p in pages:
        for target in p["outbound"]:
            if target != p["slug"]:
                inbound[target].add(p["slug"])
    for p in pages:
        p["backlinks"] = sorted(inbound[p["slug"]])

    if broken:
        print(f"  ⚠ {len(broken)} broken wikilink(s) — rendered as plain text, worth a `lint`:")
        for src, target in broken[:15]:
            print(f"      {src} -> [[{target}]]")
        if len(broken) > 15:
            print(f"      … and {len(broken) - 15} more")
    return pages


def content_hash(pages: list[dict], items: list[dict]) -> str:
    h = hashlib.sha1(RENDERER_VERSION.encode())
    for p in pages:
        h.update(p["slug"].encode())
        h.update(p["html"].encode())
    h.update(json.dumps(items, sort_keys=True).encode())
    return h.hexdigest()[:12]


# The app shell — everything a browser has to re-download for a code change to take effect.
SHELL_FILES = ("index.html", "style.css", "app.js", "sm2.js", "session.js", "analytics.js",
               "store.js", "supabase.js", "config.js", "sw.js", "manifest.webmanifest")


def build_hash(content_version: str) -> str:
    """A version covering the *code* as well as the content.

    Without this there is no way for a deployed app to notice that it is out of date after a
    code-only change: the content hash stays byte-identical, so an update check against it says
    "already current" while the phone keeps running last week's JavaScript. Hashing the shell too
    means any deploy — new readings, new items, or just a restyled chart — produces a new id, which
    is what the app compares against on boot."""
    h = hashlib.sha1(content_version.encode())
    for name in SHELL_FILES:
        path = DOCS_DIR / name
        h.update(name.encode())
        h.update(path.read_bytes() if path.exists() else b"")
    return h.hexdigest()[:12]


def main() -> None:
    if not ITEMS_JSON.exists():
        sys.exit(f"{ITEMS_JSON.relative_to(ROOT)} not found — run `python apps/build_items.py` first.")
    items = json.loads(ITEMS_JSON.read_text(encoding="utf-8"))

    pages = build_pages()
    if not pages:
        sys.exit("No readings found in wiki/ or research/.")

    # Every item's source_page must be a page the app can actually open, or "📖 Source reading"
    # is a dead end on the phone. build_items.py already checked the file exists on disk; this
    # checks it made it into the bundle.
    slugs = {p["slug"] for p in pages}
    orphans = sorted({it["source_page"] for it in items
                      if re.sub(r"\.md$", "", Path(it["source_page"]).name) not in slugs})
    if orphans:
        print(f"  ⚠ {len(orphans)} item source_page(s) are not in the bundle:")
        for o in orphans:
            print(f"      {o}")

    version = content_hash(pages, items)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    def write(name: str, payload) -> int:
        path = OUT_DIR / name
        # Compact separators: this ships over a phone connection, and nobody hand-edits it.
        path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")),
                        encoding="utf-8")
        return path.stat().st_size

    generated = date.today().isoformat()
    n_read = write("readings.json", {"version": version, "generated": generated, "pages": pages})
    n_item = write("items.json", {"version": version, "generated": generated, "items": items})
    # `build` covers the shell as well, so a code-only deploy still produces a new id and the
    # app can tell it is stale. Written last, after the content files exist.
    write("version.json", {"version": version, "build": build_hash(version), "generated": generated,
                           "pages": len(pages), "items": len(items)})

    by_collection: dict[str, int] = {}
    for p in pages:
        by_collection[p["collection"]] = by_collection.get(p["collection"], 0) + 1
    print(f"Built docs/content/ — content {version} · build {build_hash(version)}")
    print(f"  readings.json: {len(pages)} pages ({', '.join(f'{k}={v}' for k, v in by_collection.items())}) "
          f"— {n_read / 1024:.0f} KB")
    print(f"  items.json:    {len(items)} items — {n_item / 1024:.0f} KB")
    linked = sum(len(p["backlinks"]) for p in pages)
    print(f"  wikilink graph: {linked} edges · "
          f"{sum(1 for p in pages if not p['backlinks'] and p['collection'] == 'wiki')} orphan wiki page(s)")


if __name__ == "__main__":
    main()
