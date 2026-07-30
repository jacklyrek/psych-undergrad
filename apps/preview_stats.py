#!/usr/bin/env python3
"""Render the app's Stats tab to a standalone HTML file, using the real study history.

Why this is needed: the Stats page can't be inspected by just opening the app locally. Its data
lives in Supabase and localStorage, so a fresh browser shows an empty tab — the one page that most
needs looking at is the one you can't see. This runs the actual view function from docs/app.js
against review_log.csv and review_state.json and writes a file you can open.

It exists because charts have to be looked at. Validating the palette proves the colours are
distinguishable; it says nothing about whether a label collides, a bar overflows, or a chart is
degenerate on the data you actually have. (It earned its place immediately: it's what showed that
"Coming due" was a single tall column beside fourteen empty ones, and that the hero was calling 541
never-reviewed items "overdue".)

    python apps/preview_stats.py            # writes docs/.preview/stats.html and opens it
    python apps/preview_stats.py --no-open  # just write it

The output is gitignored. The JavaScript runs under JavaScriptCore via osascript, same as the tests.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
OUT_DIR = DOCS / ".preview"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import test_web_logic as harness  # noqa: E402  — reuse its JXA runner and DOM stub

# Order matters once the module syntax is stripped: each file's names must already be defined.
MODULE_ORDER = ("config.js", "sm2.js", "session.js", "analytics.js", "supabase.js", "store.js")


def build(today: str) -> tuple[str, int]:
    items = json.loads((ROOT / "items" / "build" / "items.json").read_text(encoding="utf-8"))
    slim = [{k: it.get(k) for k in ("id", "unit", "bloom_level", "type", "cluster", "source_page")}
            for it in items]
    state_path = ROOT / "review_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    log = harness.load_log()

    # store.js reads both the log and the scheduler state out of localStorage when the module loads,
    # so they have to be seeded before it runs — otherwise ensureState initialises every item as new
    # and the page reports a backlog that isn't real.
    stub = (harness.DOM_STUB
            + "\nglobalThis.localStorage.setItem('psych.log.v1', "
            + json.dumps(json.dumps(log)) + ");\n"
            + "globalThis.localStorage.setItem('psych.state.v1', "
            + json.dumps(json.dumps(state)) + ");\n")

    sources = [stub] + [(DOCS / n).read_text(encoding="utf-8") for n in MODULE_ORDER]
    sources.append(harness.BOOT_CALL.sub("", (DOCS / "app.js").read_text(encoding="utf-8")))

    driver = """
content.items = PAYLOAD.items;
content.itemsById = new Map(PAYLOAD.items.map(i => [i.id, i]));
content.version = 'preview';
content.pages = []; content.pagesBySlug = new Map(); content.readingsLoaded = true;
ensureState(content.items, getState(), PAYLOAD.today);
__emit({ html: viewStats(), rows: getLog().length });
"""
    got = harness.run_js(sources, driver, {"items": slim, "today": today})
    if got.get("__error"):
        sys.exit("Couldn't render the view:\n" + got["__error"])
    return got["html"], got["rows"]


PAGE = """<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Stats preview — {rows} attempts</title>
<style>{css}
/* Preview chrome only — none of this ships. */
.pv-bar {{ position: sticky; top: 0; z-index: 50; display: flex; gap: .6rem; align-items: center;
  padding: .6rem 1rem; background: var(--surface); border-bottom: 1px solid var(--border); }}
.pv-bar b {{ flex: 1; font-size: .8125rem; }}
.pv-page {{ max-width: 393px; margin: 0 auto; }}   /* iPhone 15 logical width */
</style></head>
<body>
<div class="pv-bar">
  <b>Stats preview · {rows} real attempts · {today}</b>
  <button class="btn btn-sm btn-ghost" id="w">Widen</button>
</div>
<main class="view pv-page" id="p">{html}</main>
<script>
  document.getElementById('w').addEventListener('click', () => {{
    document.getElementById('p').classList.toggle('pv-page');
  }});
</script>
</body></html>
"""


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--no-open", action="store_true", help="write the file without opening it")
    ap.add_argument("--date", default=None, help="render as if it were this date (YYYY-MM-DD)")
    args = ap.parse_args()

    from datetime import date
    today = args.date or date.today().isoformat()

    html, rows = build(today)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out = OUT_DIR / "stats.html"
    out.write_text(PAGE.format(css=(DOCS / "style.css").read_text(encoding="utf-8"),
                               html=html, rows=rows, today=today), encoding="utf-8")
    print(f"Wrote {out.relative_to(ROOT)} — {rows} attempts, {len(html) / 1024:.0f} KB of view HTML.")
    if not args.no_open:
        subprocess.run(["open", str(out)], check=False)


if __name__ == "__main__":
    main()
