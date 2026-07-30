#!/usr/bin/env python3
"""Check the web app's JavaScript: every module parses, and the pure-logic ones compute correctly.

There is no node and no browser on this machine, so this does what can honestly be done from here:

  1. parse      every docs/*.js is fed to the JavaScriptCore parser. Catches the failure mode
                hand-written 700-line files actually have — an unbalanced brace or a broken template
                literal — which would otherwise show up as a blank white screen on the phone.
  2. logic      session.js and analytics.js are run against the real item bank and the real
                review_log.csv, and their answers are compared with the same quantities computed
                independently in Python here. These are the off-by-one-prone parts: date windows,
                confidence bucketing, streak counting.

What this cannot cover is DOM behaviour and layout — those need the app open in Safari. See the
"Verifying on the phone" checklist in docs/README.md.

Run:  python apps/test_web_logic.py
"""
from __future__ import annotations

import csv
import json
import re
import subprocess
import sys
import tempfile
from collections import defaultdict
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
ITEMS_JSON = ROOT / "items" / "build" / "items.json"
REVIEW_LOG = ROOT / "review_log.csv"
STATE_JSON = ROOT / "review_state.json"

MODULES = ["sm2.js", "session.js", "analytics.js", "store.js", "supabase.js", "config.js",
           "app.js", "sw.js"]

IMPORT_LINE = re.compile(r"^\s*import\s.*?;\s*$", re.MULTILINE)


def strip_module_syntax(src: str) -> str:
    """ES-module source -> something JavaScriptCore will parse and run as a plain script.

    Substitutions, all inert with respect to what's being tested:
      - drop the import statements (every module ends up in one shared scope instead)
      - turn each export into a `var` or a function declaration, so it lands as a property of the
        global object. That is what lets a namespace import like `store.grade` keep working: the
        harness points `store` at the global object itself (see DOM_STUB).
      - replace `import.meta.url`, which is a hard syntax error outside a module, with a stand-in.
    """
    src = IMPORT_LINE.sub("", src)
    src = re.sub(r"^export\s+(?:const|let)\s+", "var ", src, flags=re.MULTILINE)
    src = re.sub(r"^export\s+function\s+", "function ", src, flags=re.MULTILINE)
    src = re.sub(r"^export\s+class\s+(\w+)", r"var \1 = class", src, flags=re.MULTILINE)
    src = re.sub(r"^export\s+", "", src, flags=re.MULTILINE)
    src = src.replace("import.meta.url", "'file:///app/'")
    return src


def run_js(sources: list[str], driver: str, payload: dict) -> dict:
    """Concatenate module sources plus a driver, run under JavaScriptCore, return the JSON it emits."""
    with tempfile.TemporaryDirectory() as tmp:
        out_path = Path(tmp) / "out.json"
        body = "\n".join(strip_module_syntax(s) for s in sources)
        script = f"""
ObjC.import('Foundation');
{body}
const PAYLOAD = {json.dumps(payload)};
function __emit(obj) {{
  const s = $.NSString.alloc.initWithUTF8String(JSON.stringify(obj));
  s.writeToFileAtomicallyEncodingError('{out_path}', true, $.NSUTF8StringEncoding, $());
}}
{driver}
"""
        script_path = Path(tmp) / "driver.js"
        script_path.write_text(script, encoding="utf-8")
        proc = subprocess.run(["osascript", "-l", "JavaScript", str(script_path)],
                              capture_output=True, text=True)
        if not out_path.exists():
            return {"__error": (proc.stderr or proc.stdout).strip()[:600]}
        return json.loads(out_path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- 1. parse

def check_parses() -> list[str]:
    fails = []
    for name in MODULES:
        path = DOCS / name
        if not path.exists():
            fails.append(f"{name}: missing")
            continue
        src = strip_module_syntax(path.read_text(encoding="utf-8"))
        # new Function() parses without executing, so browser-only globals inside are fine.
        payload = {"src": src}
        got = run_js([], "try { new Function(PAYLOAD.src); __emit({ok:true}); }"
                         " catch (e) { __emit({ok:false, err:String(e)}); }", payload)
        if got.get("__error"):
            fails.append(f"{name}: harness error — {got['__error']}")
        elif not got.get("ok"):
            fails.append(f"{name}: {got.get('err')}")
    print(f"  1. parse       {len(MODULES)} modules   {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- fixtures

def load_log() -> list[dict]:
    if not REVIEW_LOG.exists():
        return []
    with REVIEW_LOG.open(encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    # The web app receives Supabase rows, where the timestamp column is `ts`.
    for r in rows:
        r["ts"] = r.pop("timestamp", "")
    rows.sort(key=lambda r: r["ts"], reverse=True)
    return rows


# ---------------------------------------------------------------- 2. session.js

def check_session(items: list[dict], state: dict) -> list[str]:
    today = "2026-07-29"
    fails: list[str] = []

    due_ids = sorted(i["id"] for i in items if state.get(i["id"], {}).get("due", today) <= today)
    by_unit = defaultdict(int)
    for i in items:
        if i["id"] in set(due_ids):
            by_unit[i["unit"]] += 1

    driver = """
const state = PAYLOAD.state;
const items = PAYLOAD.items;
const counts = dueCounts(items, state, NO_FILTERS, PAYLOAD.today);
const unit1 = dueCounts(items, state, {units:['1'],blooms:[],types:[]}, PAYLOAD.today);
const q = buildQueue(items, state, {length: 10, today: PAYLOAD.today, shuffle: false});
const qFiltered = buildQueue(items, state, {
  filters: {units:[], blooms:['apply'], types:[]}, length: 500, today: PAYLOAD.today, shuffle: false});
const cram = buildQueue(items, state, {cram: true, length: 999999, today: PAYLOAD.today, shuffle: false});
__emit({
  counts, unit1, queueLen: q.length, queue: q,
  applyIds: qFiltered, cramLen: cram.length,
  units: facets(items).units, blooms: facets(items).blooms,
  labels: [unitLabel('3'), unitLabel('aux-addiction'), unitLabel('')],
});
"""
    got = run_js([(DOCS / "sm2.js").read_text(), (DOCS / "session.js").read_text()], driver,
                 {"items": items, "state": state, "today": today})
    if got.get("__error"):
        return [f"session.js harness error — {got['__error']}"]

    if got["counts"]["due"] != len(due_ids):
        fails.append(f"dueCounts.due: js {got['counts']['due']} != py {len(due_ids)}")
    if got["counts"]["total"] != len(items):
        fails.append(f"dueCounts.total: js {got['counts']['total']} != py {len(items)}")
    if got["unit1"]["inFilter"] != by_unit["1"]:
        fails.append(f"unit-1 filter: js {got['unit1']['inFilter']} != py {by_unit['1']}")
    if got["queueLen"] != min(10, len(due_ids)):
        fails.append(f"buildQueue length cap: js {got['queueLen']} != {min(10, len(due_ids))}")
    if sorted(got["queue"]) != sorted(due_ids)[:len(got["queue"])] and len(due_ids) > 10:
        pass  # order is unconstrained with shuffle off; membership is what matters
    if not set(got["queue"]).issubset(set(due_ids)):
        fails.append("buildQueue returned items that are not due")

    py_apply = sorted(i["id"] for i in items
                      if i["id"] in set(due_ids) and i["bloom_level"] == "apply")
    if sorted(got["applyIds"]) != py_apply:
        fails.append(f"bloom filter: js {len(got['applyIds'])} items != py {len(py_apply)}")
    if got["cramLen"] != len(items):
        fails.append(f"cram should ignore due dates: js {got['cramLen']} != {len(items)}")

    py_units = sorted({i["unit"] for i in items if i.get("unit")},
                      key=lambda u: (0, int(u), "") if u.isdigit() else (1, 0, u))
    if got["units"] != py_units:
        fails.append(f"facets unit order: js {got['units'][:6]} != py {py_units[:6]}")
    if got["labels"] != ["Unit 3", "addiction", "—"]:
        fails.append(f"unitLabel: {got['labels']}")

    print(f"  2. session.js  {len(due_ids):>4} due      {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- 3. analytics.js

def check_analytics(items: list[dict], state: dict, log: list[dict]) -> list[str]:
    today = "2026-07-29"
    fails: list[str] = []

    n = len(log)
    correct = sum(1 for a in log if a["outcome"] == "correct")

    # calibration, computed independently
    buckets = [{"lo": lo, "n": 0, "correct": 0} for lo in range(0, 100, 20)]
    for a in log:
        try:
            c = float(a["predicted_confidence"])
        except (TypeError, ValueError):
            continue
        idx = min(4, int(c // 20))
        buckets[idx]["n"] += 1
        if a["outcome"] == "correct":
            buckets[idx]["correct"] += 1

    # streak, computed independently
    active = {a["ts"][:10] for a in log}
    t = date.fromisoformat(today)
    cursor = t if today in active else t - timedelta(days=1)
    py_streak = 0
    while cursor.isoformat() in active:
        py_streak += 1
        cursor -= timedelta(days=1)

    # pipeline, computed independently
    py_pipe = {"new": 0, "learning": 0, "young": 0, "mature": 0}
    for it in items:
        st = state.get(it["id"])
        if not st or st.get("reps", 0) == 0:
            py_pipe["new"] += 1
        elif st["interval"] < 7:
            py_pipe["learning"] += 1
        elif st["interval"] < 30:
            py_pipe["young"] += 1
        else:
            py_pipe["mature"] += 1

    # 14-day forecast, computed independently
    py_forecast = {}
    for d in range(0, 15):
        py_forecast[(t + timedelta(days=d)).isoformat()] = 0
    overdue = 0
    for it in items:
        st = state.get(it["id"])
        if not st:
            continue
        if st["due"] <= today:
            py_forecast[today] += 1
            if st["due"] < today:
                overdue += 1
        elif st["due"] in py_forecast:
            py_forecast[st["due"]] += 1

    driver = """
const log = PAYLOAD.log, items = PAYLOAD.items, state = PAYLOAD.state, today = PAYLOAD.today;
__emit({
  sum: summarize(log),
  cal: calibration(log).map(b => ({lo: b.lo, n: b.n, correct: b.correct})),
  brier: brierScore(log),
  streak: streak(log, today),
  pipe: pipeline(items, state),
  forecast: dueForecast(items, state, today, 14),
  blooms: byBloom(log, BLOOM_ORDER),
  weak: weakestClusters(log),
  over: overconfidentMisses(log).length,
  act: activity(log, today, 30),
  stale: daysSinceLast(log, today),
});
"""
    got = run_js([(DOCS / "sm2.js").read_text(), (DOCS / "session.js").read_text(),
                  (DOCS / "analytics.js").read_text()], driver,
                 {"log": log, "items": items, "state": state, "today": today})
    if got.get("__error"):
        return [f"analytics.js harness error — {got['__error']}"]

    if got["sum"]["attempts"] != n:
        fails.append(f"summarize.attempts: js {got['sum']['attempts']} != py {n}")
    if got["sum"]["correct"] != correct:
        fails.append(f"summarize.correct: js {got['sum']['correct']} != py {correct}")
    if abs(got["sum"]["accuracy"] - (correct / n if n else 0)) > 1e-9:
        fails.append(f"summarize.accuracy: js {got['sum']['accuracy']} != py {correct / n}")

    for js_b, py_b in zip(got["cal"], buckets):
        if js_b["n"] != py_b["n"] or js_b["correct"] != py_b["correct"]:
            fails.append(f"calibration bucket {py_b['lo']}: js {js_b} != py {py_b}")
    if sum(b["n"] for b in got["cal"]) != sum(b["n"] for b in buckets):
        fails.append("calibration dropped attempts")

    if got["streak"]["current"] != py_streak:
        fails.append(f"streak: js {got['streak']['current']} != py {py_streak}")
    if got["streak"]["activeDays"] != len(active):
        fails.append(f"activeDays: js {got['streak']['activeDays']} != py {len(active)}")
    if got["pipe"] != py_pipe:
        fails.append(f"pipeline: js {got['pipe']} != py {py_pipe}")

    if len(got["forecast"]) != 15:
        fails.append(f"forecast length {len(got['forecast'])} != 15")
    for row in got["forecast"]:
        if py_forecast.get(row["date"]) != row["count"]:
            fails.append(f"forecast {row['date']}: js {row['count']} != py {py_forecast.get(row['date'])}")
    if got["forecast"][0]["overdue"] != overdue:
        fails.append(f"overdue: js {got['forecast'][0]['overdue']} != py {overdue}")

    # Bloom rows must cover every attempt and be ordered remember -> evaluate.
    if sum(r["n"] for r in got["blooms"]) != n:
        fails.append("byBloom dropped attempts")
    order = ["remember", "understand", "apply", "analyze", "evaluate"]
    present = [r["bloom"] for r in got["blooms"] if r["bloom"] in order]
    if present != [b for b in order if b in present]:
        fails.append(f"byBloom order: {present}")

    if len(got["act"]) != 30:
        fails.append(f"activity window {len(got['act'])} != 30")
    if sum(a["count"] for a in got["act"]) > n:
        fails.append("activity counted more attempts than exist")
    if any(w["n"] < 4 for w in got["weak"]):
        fails.append("weakestClusters ignored its minimum-attempts guard")

    print(f"  3. analytics   {n:>4} attempts {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- 4. assets

HTML_REF = re.compile(r'(?:href|src)="([^"#:]+)"')
JS_IMPORT = re.compile(r"""from\s+['"]\./([^'"]+)['"]""")
JS_URL = re.compile(r"""new URL\(\s*['"]([^'"]+)['"]""")
SW_LIST = re.compile(r"const SHELL = \[(.*?)\];", re.DOTALL)


def check_assets() -> list[str]:
    """Every path the app references must exist on disk.

    GitHub Pages serves this from a subdirectory, so an absolute path or a typo'd filename that
    happens to work when opened from the filesystem 404s once deployed — a blank screen with the
    reason buried in a console this app has no way to show. Cheap to catch here instead."""
    fails: list[str] = []

    def must_exist(ref: str, where: str) -> None:
        if ref.startswith(("http://", "https://", "data:", "//")):
            return
        if ref.startswith("/"):
            fails.append(f"{where}: absolute path '{ref}' breaks on a Pages subdirectory")
            return
        target = (DOCS / ref.split("?")[0]).resolve()
        if not target.exists() and ref not in ("./",):
            fails.append(f"{where}: references missing '{ref}'")

    for ref in HTML_REF.findall((DOCS / "index.html").read_text(encoding="utf-8")):
        must_exist(ref, "index.html")

    for name in MODULES:
        src = (DOCS / name).read_text(encoding="utf-8")
        for ref in JS_IMPORT.findall(src):
            must_exist(ref, name)
        for ref in JS_URL.findall(src):
            if not ref.startswith("http"):
                must_exist(ref, name)

    # The service worker's precache list is a plain array of paths — every one has to resolve, or
    # offline support quietly comes up short.
    listed = re.findall(r"'([^']+)'", SW_LIST.search((DOCS / "sw.js").read_text()).group(1))
    for ref in listed:
        must_exist(ref, "sw.js SHELL")
    for name in MODULES:
        if name not in listed and name != "sw.js":
            fails.append(f"sw.js SHELL is missing {name} — it wouldn't be available offline")

    try:
        manifest = json.loads((DOCS / "manifest.webmanifest").read_text(encoding="utf-8"))
        for icon in manifest["icons"]:
            must_exist(icon["src"], "manifest")
        for key in ("start_url", "scope"):
            if manifest[key].startswith("/"):
                fails.append(f"manifest {key} is absolute — breaks on a Pages subdirectory")
    except (json.JSONDecodeError, KeyError) as err:
        fails.append(f"manifest.webmanifest: {err}")

    if not (DOCS / "content" / "items.json").exists():
        fails.append("content/items.json missing — run `python apps/build_web.py`")

    print(f"  4. assets      {len(listed)} precached {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- 5. views + the loop

# Enough of a browser for app.js to load and its view functions to run. Not a DOM implementation —
# the views are string builders, so what's needed is for the module-level wiring not to throw.
DOM_STUB = r"""
const __els = {};
function __el(id) {
  if (!__els[id]) __els[id] = {
    id, innerHTML: '', textContent: '', hidden: false, dataset: {}, value: '', scrollTop: 0,
    addEventListener() {}, removeEventListener() {},
    querySelector() { return null; }, querySelectorAll() { return []; },
    closest() { return null; }, focus() {}, setSelectionRange() {},
  };
  return __els[id];
}
globalThis.document = {
  getElementById: __el, addEventListener() {}, activeElement: null,
  querySelector() { return null; }, querySelectorAll() { return []; },
};
globalThis.localStorage = (() => {
  const m = new Map();
  return {
    getItem: (k) => (m.has(k) ? m.get(k) : null),
    setItem: (k, v) => m.set(k, String(v)),
    removeItem: (k) => m.delete(k),
    clear: () => m.clear(),
  };
})();
globalThis.navigator = { onLine: true };
globalThis.location = { hash: '#/study', reload() {} };
globalThis.history = { back() {} };
globalThis.window = { addEventListener() {}, matchMedia: () => ({ matches: false }),
                      navigator: globalThis.navigator };
globalThis.CSS = { escape: (s) => s };
globalThis.setTimeout = (fn) => 0;
globalThis.clearTimeout = () => {};
globalThis.confirm = () => false;
globalThis.fetch = () => { throw new Error('the view tests must not touch the network'); };

// URL and URLSearchParams are web APIs, not ECMAScript, so JavaScriptCore has neither. The router
// needs enough of URLSearchParams to read ?h=<heading>; module paths only need href concatenation.
if (typeof URLSearchParams === 'undefined') {
  globalThis.URLSearchParams = class {
    constructor(q) {
      this._m = new Map();
      for (const pair of String(q || '').split('&')) {
        if (!pair) continue;
        const [k, ...rest] = pair.split('=');
        this._m.set(decodeURIComponent(k), decodeURIComponent(rest.join('=')));
      }
    }
    get(k) { return this._m.has(k) ? this._m.get(k) : null; }
  };
}
if (typeof URL === 'undefined') {
  globalThis.URL = class {
    constructor(rel, base) { this.href = String(base || '') + String(rel); }
  };
}

// strip_module_syntax turns every export into a global, so `store.grade` and friends resolve as
// long as the namespace name points at the global object.
for (const ns of ['store', 'sm2', 'api', 'sess', 'stats']) globalThis[ns] = globalThis;
"""

# app.js kicks itself off with boot(), which is async and network-bound. Stripped for these tests;
# what's under test is the views and the grading loop, not the bootstrap.
BOOT_CALL = re.compile(r"^boot\(\);\s*$", re.MULTILINE)


def check_views(items: list[dict], pages: list[dict]) -> list[str]:
    # Dependency order matters once the imports are stripped: each module's names have to already be
    # defined as globals by the time the next one runs. config.js first, since supabase.js reads it.
    sources = [DOM_STUB] + [(DOCS / n).read_text(encoding="utf-8")
                            for n in ("config.js", "sm2.js", "session.js", "analytics.js",
                                      "supabase.js", "store.js")]
    app = BOOT_CALL.sub("", (DOCS / "app.js").read_text(encoding="utf-8"))
    sources.append(app)

    driver = """
// Populate content directly rather than fetching, keeping the whole test synchronous.
content.items = PAYLOAD.items;
content.itemsById = new Map(PAYLOAD.items.map(i => [i.id, i]));
content.version = 'testbundle';
content.pages = PAYLOAD.pages;
content.pagesBySlug = new Map(PAYLOAD.pages.map(p => [p.slug, p]));
content.readingsLoaded = true;
ensureState(content.items, getState(), PAYLOAD.today);

const out = { views: {}, errors: [], loop: null };

function capture(name, fn) {
  try {
    out.views[name] = String(fn());
  } catch (e) {
    out.errors.push(`${name}: ${e}`);
    out.views[name] = '';
  }
}

capture('studySetup', () => viewStudySetup());
capture('readIndex', () => viewReadIndex());
capture('page', () => viewPage(PAYLOAD.pages[0].slug));
capture('pageMissing', () => viewPage('no-such-page'));
capture('stats', () => viewStats());
capture('you', () => viewYou());

// One prompt view and one reveal view per item type, so every input branch is exercised.
for (const type of PAYLOAD.types) {
  const item = PAYLOAD.items.find(i => i.type === type);
  if (!item) continue;
  const mk = (stage, draft) => ({
    queue: [item.id], idx: 0, stage, results: [], startedAt: Date.now(),
    itemStartAt: Date.now(), draft,
  });
  saveSession(mk('prompt', { confidence: null, response: '' }));
  capture(`prompt.${type}`, () => viewRun(loadSession()));
  saveSession(mk('prompt', { confidence: 70, response: item.correct || item.answer }));
  capture(`prompt.${type}.answered`, () => viewRun(loadSession()));
  saveSession(mk('reveal', { confidence: 70, response: item.correct || item.answer }));
  capture(`reveal.${type}`, () => viewRun(loadSession()));
  saveSession(mk('reveal', { confidence: 90, response: '' }));
  capture(`reveal.${type}.blank`, () => viewRun(loadSession()));
}

capture('summary', () => viewSummary({
  queue: ['a', 'b'], idx: 2, stage: 'summary', startedAt: Date.now() - 90000,
  results: [
    { item_id: PAYLOAD.items[0].id, outcome: 'correct', confidence: 90 },
    { item_id: PAYLOAD.items[1].id, outcome: 'missed', confidence: 90 },
  ],
}));

// The actual loop: grade three items and check the scheduler and log moved as they should.
const three = PAYLOAD.items.slice(0, 3).map(i => i.id);
saveSession({ queue: three, idx: 0, stage: 'reveal', results: [], startedAt: Date.now(),
              itemStartAt: Date.now(), draft: { confidence: 70, response: 'something' } });
const beforeState = JSON.parse(JSON.stringify(getState()[three[0]]));
submitGrade('correct');
const afterFirst = JSON.parse(JSON.stringify(getState()[three[0]]));
const sessionAfterFirst = loadSession();
sessionAfterFirst.stage = 'reveal';
saveSession(sessionAfterFirst);
submitGrade('missed');
const s2 = loadSession(); s2.stage = 'reveal'; saveSession(s2);
submitGrade('shaky');
const done = loadSession();

out.loop = {
  beforeState, afterFirst,
  idx: done.idx,
  stage: done.stage,
  results: done.results,
  logLen: getLog().length,
  logHead: getLog().slice(0, 3),
  queued: status.queued,
  secondItemReps: getState()[three[1]].reps,
};
__emit(out);
"""
    got = run_js(sources, driver, {
        "items": items, "pages": pages, "today": "2026-07-29",
        "types": ["cloze", "mcq", "recall", "vignette", "compare", "explain"],
    })
    if got.get("__error"):
        return [f"views harness error — {got['__error']}"]

    fails: list[str] = [f"threw — {e}" for e in got["errors"]]

    # Placeholder leakage is the failure mode of building HTML with template literals: a renamed or
    # absent field shows up on the phone as the literal word "undefined" rather than as an error.
    for name, html in got["views"].items():
        if not html.strip():
            fails.append(f"{name}: rendered empty")
            continue
        for bad in ("undefined", "NaN", "[object Object]", "null%", "Infinity"):
            if bad in html:
                at = html.index(bad)
                fails.append(f"{name}: contains '{bad}' — …{html[max(0, at - 60):at + 40]}…")
        for tag in ("div", "span", "button", "p", "a", "article", "details", "summary", "table"):
            opens = len(re.findall(rf"<{tag}\b", html))
            closes = len(re.findall(rf"</{tag}>", html))
            if opens != closes:
                fails.append(f"{name}: {opens} <{tag}> vs {closes} </{tag}>")

    # A cloze prompt must hide its deletion, or the answer sits in the question.
    cloze = got["views"].get("prompt.cloze", "")
    if 'class="blank"' not in cloze:
        fails.append("prompt.cloze: the {{deletion}} was not replaced with a blank")
    if "{{" in cloze:
        fails.append("prompt.cloze: raw {{...}} braces reached the page")

    # The prompt stage must never render the answer. Checking for shared *words* would be wrong —
    # a vignette's scenario and its answer legitimately discuss the same clinical material — so the
    # invariant is that the answer text itself, and the label that introduces it, are absent.
    for type_ in ("cloze", "mcq", "recall", "vignette", "compare", "explain"):
        item = next((i for i in items if i["type"] == type_), None)
        html = got["views"].get(f"prompt.{type_}", "")
        if not (item and html):
            continue
        if "Model answer" in html:
            fails.append(f"prompt.{type_}: the reveal-stage answer box rendered before the reveal")
        distinctive = item["answer"][:60].strip()
        if len(distinctive) > 25 and distinctive in html:
            fails.append(f"prompt.{type_}: model answer text visible before reveal")
        if item["type"] == "mcq" and item.get("correct") and 'data-suggested' in html:
            fails.append(f"prompt.{type_}: grade hinting leaked into the prompt stage")

    # Reveal must show the answer and offer all three grades.
    for type_ in ("cloze", "mcq", "recall"):
        html = got["views"].get(f"reveal.{type_}", "")
        if html and html.count('data-action="grade"') != 3:
            fails.append(f"reveal.{type_}: expected 3 grade buttons")
        if html and "Model answer" not in html:
            fails.append(f"reveal.{type_}: no model answer shown")
    if 'data-suggested="1"' not in got["views"].get("reveal.mcq", ""):
        fails.append("reveal.mcq: a correct response should pre-highlight the 'Got it' grade")
    if 'data-suggested="1"' not in got["views"].get("reveal.cloze", ""):
        fails.append("reveal.cloze: a matching response should pre-highlight 'Got it'")

    if "No reading called" not in got["views"].get("pageMissing", ""):
        fails.append("viewPage: a missing slug should say so, not render blank")

    # The loop itself
    loop = got["loop"]
    if loop["idx"] != 3 or loop["stage"] != "summary":
        fails.append(f"loop: after 3 grades expected idx 3 / summary, got {loop['idx']} / {loop['stage']}")
    if [r["outcome"] for r in loop["results"]] != ["correct", "missed", "shaky"]:
        fails.append(f"loop: results {[r['outcome'] for r in loop['results']]}")
    if loop["logLen"] != 3:
        fails.append(f"loop: expected 3 log entries, got {loop['logLen']}")
    if loop["queued"] != 3:
        fails.append(f"loop: expected 3 attempts queued for upload, got {loop['queued']}")
    if loop["afterFirst"]["reps"] != loop["beforeState"]["reps"] + 1:
        fails.append(f"loop: a correct grade should raise reps ({loop['beforeState']['reps']} "
                     f"-> {loop['afterFirst']['reps']})")
    if loop["afterFirst"]["due"] <= "2026-07-29":
        fails.append(f"loop: a correct grade should push the due date out, got {loop['afterFirst']['due']}")
    if loop["secondItemReps"] != 0:
        fails.append(f"loop: a missed grade should reset reps to 0, got {loop['secondItemReps']}")
    for row in loop["logHead"]:
        missing = [k for k in ("item_id", "outcome", "ts", "predicted_confidence", "ease", "reps",
                               "interval_before", "interval_after", "due", "client") if k not in row]
        if missing:
            fails.append(f"loop: log row missing {missing}")

    print(f"  5. views       {len(got['views']):>4} renders {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- main

def main() -> None:
    if not ITEMS_JSON.exists():
        sys.exit("items/build/items.json not found — run `python apps/build_items.py` first.")
    items = json.loads(ITEMS_JSON.read_text(encoding="utf-8"))
    # Only the fields the web app actually uses, to keep the payload to JavaScriptCore small.
    slim = [{k: it.get(k) for k in ("id", "unit", "bloom_level", "type", "cluster", "source_page")}
            for it in items]
    state = json.loads(STATE_JSON.read_text(encoding="utf-8")) if STATE_JSON.exists() else {}
    log = load_log()

    print(f"Web logic: {len(MODULES)} modules, {len(items)} items, {len(log)} logged attempts")
    fails: list[str] = []
    fails += check_parses()
    fails += check_session(slim, state)
    fails += check_analytics(slim, state, log)
    fails += check_assets()

    readings = DOCS / "content" / "readings.json"
    if readings.exists():
        pages = json.loads(readings.read_text(encoding="utf-8"))["pages"]
        # A handful of pages is enough to exercise the reader, and keeps the payload small.
        sample = [p for p in pages if p["type"] == "concept"][:3] + [p for p in pages if p["type"] == "unit"][:1]
        fails += check_views(items, sample)
    else:
        fails.append("docs/content/readings.json missing — run `python apps/build_web.py`")

    if fails:
        print("\nFAILED:")
        for f in fails:
            print(f"  - {f}")
        sys.exit(1)
    print("\nAll web logic checks passed.")


if __name__ == "__main__":
    main()
