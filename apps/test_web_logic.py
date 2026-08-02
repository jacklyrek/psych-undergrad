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
    # "Overdue" means a review that slipped — never-reviewed items carry a due date of the day they
    # entered the bank, so counting them as overdue would report an untouched bank as a missed
    # schedule. They're `fresh` instead.
    overdue = 0
    fresh = 0
    for it in items:
        st = state.get(it["id"])
        if not st:
            continue
        if st["due"] <= today:
            py_forecast[today] += 1
            if st.get("reps", 0) == 0:
                fresh += 1
            elif st["due"] < today:
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
    if got["forecast"][0]["fresh"] != fresh:
        fails.append(f"fresh: js {got['forecast'][0]['fresh']} != py {fresh}")
    if got["forecast"][0]["fresh"] + got["forecast"][0]["overdue"] > got["forecast"][0]["count"]:
        fails.append("forecast: fresh + overdue exceeds today's total")

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
    _h: {},
    addEventListener(type, fn) { (this._h[type] = this._h[type] || []).push(fn); },
    removeEventListener() {},
    querySelector() { return null; }, querySelectorAll() { return []; },
    closest() { return null; }, focus() {}, setSelectionRange() {},
  };
  return __els[id];
}
// Tap a bottom-bar tab: builds just enough of a click event for the delegating handler, which
// reaches the anchor through ev.target.closest('.tab') and reads its data-tab.
globalThis.__tap = (tab) => {
  const link = { dataset: { tab }, closest: (sel) => (sel === '.tab' ? link : null) };
  const ev = { target: link, preventDefault() {} };
  (__el('tabbar')._h.click || []).forEach((fn) => fn(ev));
};
// Drag a finger across the view: touchstart at (x0,y0), touchend at (x1,y1). `target` stands in for
// whatever the finger landed on, since the gesture defers to sideways-scrolling elements.
globalThis.__swipe = (o) => {
  const v = __el('view');
  const target = o.target || { closest: () => null };
  (v._h.touchstart || []).forEach((fn) => fn({ touches: [{ clientX: o.x0, clientY: o.y0 }], target }));
  (v._h.touchend || []).forEach((fn) => fn({
    changedTouches: [{ clientX: o.x1, clientY: o.y1 }], target,
  }));
};
// The header's ‹ button — the other half of "go back", and the half that is always available.
globalThis.__back = () => (__el('backBtn')._h.click || []).forEach((fn) => fn({}));
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
// Enough of the history stack for the router: a real list of entries, since going back is now
// tab-aware and traverses to a chosen entry rather than always popping the last one. Assigning a
// hash pushes a *new* entry, so its state starts out null — which is how the router tells a fresh
// entry from one it has already stamped with its depth. Traversals are counted so the swipe tests
// can see them fire.
globalThis.__backs = 0;
globalThis.__hist = { entries: [{ hash: '#/study', state: null }], at: 0 };
globalThis.location = {
  get hash() { return __hist.entries[__hist.at].hash; },
  set hash(v) {
    if (v === this.hash) return;             // browsers ignore an assignment that changes nothing
    __hist.entries.length = __hist.at + 1;   // navigating away drops whatever was ahead
    __hist.entries.push({ hash: v, state: null });
    __hist.at++;
  },
  reload() {},
};
globalThis.history = {
  get state() { return __hist.entries[__hist.at].state; },
  replaceState(s) { __hist.entries[__hist.at].state = s; },
  back() { globalThis.history.go(-1); },
  go(delta) {
    const to = Math.max(0, Math.min(__hist.entries.length - 1, __hist.at + delta));
    if (to === __hist.at) return;
    globalThis.__backs += Math.abs(to - __hist.at);
    __hist.at = to;
    (globalThis.__fire || (() => {}))('popstate');
  },
};
// Handlers are kept so the scroll test can fire popstate; scrollTo calls are recorded so it can
// assert what the router did with the scroll position.
globalThis.__handlers = {};
globalThis.__scrolls = [];
globalThis.__fire = (type) => (__handlers[type] || []).forEach((fn) => fn({ type }));
globalThis.window = {
  addEventListener(type, fn) { (__handlers[type] = __handlers[type] || []).push(fn); },
  matchMedia: () => ({ matches: false }),
  navigator: globalThis.navigator,
  scrollY: 0,
  scrollTo(x, y) { globalThis.window.scrollY = y; __scrolls.push(y); },
};
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

// The index collapsed, then with one unit opened — the two states of the unit accordion.
const firstUnit = PAYLOAD.pages.find(p => p.collection === 'wiki' && p.unit);
out.openUnit = firstUnit ? firstUnit.unit : null;
openUnit = out.openUnit;
capture('readIndexOpen', () => viewReadIndex());
openUnit = null;

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

    # The index opens collapsed — one header per unit and no reading rows — which is what keeps the
    # later units a tap away instead of sixty rows down. Opening one reveals exactly that unit.
    collapsed = got["views"].get("readIndex", "")
    heads = collapsed.count('data-action="toggleunit"')
    expected_heads = len({p["unit"] for p in pages if p["collection"] == "wiki" and p["unit"]})
    if heads != expected_heads:
        fails.append(f"viewReadIndex: expected {expected_heads} unit headers, found {heads}")
    if 'href="#/read/' in collapsed:
        fails.append("viewReadIndex: collapsed sections should list no readings until one is opened")
    opened = got["views"].get("readIndexOpen", "")
    revealed = [p["slug"] for p in pages
                if p["collection"] == "wiki" and p["unit"] == got.get("openUnit")]
    absent = [s for s in revealed if f'href="#/read/{s}"' not in opened]
    if absent:
        fails.append(f"viewReadIndex: opening a unit did not list {absent}")
    if opened.count('href="#/read/') != len(revealed):
        fails.append("viewReadIndex: only the open unit's readings should be listed")

    # The quiz offer sits both above and below the reading, so finishing a long page doesn't mean
    # scrolling back to the top to act on it.
    first = pages[0]["slug"]
    if any(re.sub(r"\.md$", "", Path(it["source_page"]).name) == first for it in items):
        offers = got["views"].get("page", "").count('data-action="quizpage"')
        if offers != 2:
            fails.append(f"viewPage: expected the quiz button above and below the reading, found {offers}")

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


# ---------------------------------------------------------------- 6. scroll position

def check_scroll(items: list[dict], pages: list[dict]) -> list[str]:
    """The router's scroll handling.

    #view has no overflow of its own, so the document is what scrolls — which made the obvious
    `view.scrollTop = 0` a silent no-op and left every new page inheriting the last one's scroll
    position. The fix can't be an unconditional scrollTo(0, 0) either, since render() also runs for
    in-place re-renders. This pins down both halves, plus back/forward restoring where you were."""
    sources = [DOM_STUB] + [(DOCS / n).read_text(encoding="utf-8")
                            for n in ("config.js", "sm2.js", "session.js", "analytics.js",
                                      "supabase.js", "store.js")]
    sources.append(BOOT_CALL.sub("", (DOCS / "app.js").read_text(encoding="utf-8")))

    driver = """
content.items = PAYLOAD.items;
content.itemsById = new Map(PAYLOAD.items.map(i => [i.id, i]));
content.version = 'testbundle';
content.pages = PAYLOAD.pages;
content.pagesBySlug = new Map(PAYLOAD.pages.map(p => [p.slug, p]));
content.readingsLoaded = true;
ensureState(content.items, getState(), PAYLOAD.today);

const steps = {};
function go(hash, scrolledTo) {
  if (scrolledTo !== undefined) globalThis.window.scrollY = scrolledTo;
  location.hash = hash;
  __scrolls.length = 0;
  render();
  return __scrolls.slice();
}

const slugA = PAYLOAD.pages[0].slug, slugB = PAYLOAD.pages[1].slug;

steps.firstRender   = go('#/read');
steps.sameViewAgain = (globalThis.window.scrollY = 900, __scrolls.length = 0, render(), __scrolls.slice());
steps.toPage        = go(`#/read/${slugA}`, 900);        // leaving the index at y=900
steps.toOtherPage   = go(`#/read/${slugB}`, 640);
steps.toStats       = go('#/stats', 300);

// Back to the index: popstate marks it a traversal, so the remembered 900 should come back.
location.hash = '#/read';
__scrolls.length = 0;
__fire('popstate');
render();
steps.backToIndex = __scrolls.slice();

// A fresh (non-traversal) visit to the same view must NOT restore.
steps.forwardToIndex = go('#/stats', 120).concat(go('#/read', 120));

// Search: the switch from the full index to a result list is new content and should go to the top,
// but every keystroke after that is the same list being narrowed and must hold position.
searchQuery = 'em';
globalThis.window.scrollY = 450; __scrolls.length = 0; render();
steps.searchStart = __scrolls.slice();
searchQuery = 'empathy';
globalThis.window.scrollY = 300; __scrolls.length = 0; render();
steps.searchTyping = __scrolls.slice();
searchQuery = '';

// Grading advances to a new item — new content, so back to the top.
const three = PAYLOAD.items.slice(0, 3).map(i => i.id);
saveSession({ queue: three, idx: 0, stage: 'reveal', results: [], startedAt: Date.now(),
              itemStartAt: Date.now(), draft: { confidence: 70, response: 'x' } });
location.hash = '#/study/run';
render();
globalThis.window.scrollY = 700;
__scrolls.length = 0;
submitGrade('correct');
steps.afterGrade = __scrolls.slice();

__emit({ steps, memoryKeys: [...scrollMemory.keys()] });
"""
    got = run_js(sources, driver, {"items": items, "pages": pages, "today": "2026-07-29"})
    if got.get("__error"):
        return [f"scroll harness error — {got['__error']}"]

    s = got["steps"]
    fails: list[str] = []

    def expect(name, want, why):
        if s.get(name) != want:
            fails.append(f"{name}: expected scrollTo {want}, got {s.get(name)} — {why}")

    expect("firstRender", [0], "arriving at a view should start at the top")
    expect("sameViewAgain", [], "re-rendering the same view must not move the scroll")
    expect("toPage", [0], "opening a reading should start at its top, not inherit the index's scroll")
    expect("toOtherPage", [0], "each new reading starts at the top")
    expect("toStats", [0], "switching tabs starts at the top")
    expect("backToIndex", [900], "back should restore where you left the index")
    expect("searchStart", [0], "switching from the index to search results is a new list")
    expect("searchTyping", [], "narrowing an existing search must not scroll the results away")
    expect("afterGrade", [0], "the next item is new content and should start at the top")

    # The forward (non-traversal) visit is the second half of that concatenation.
    if s.get("forwardToIndex", [])[-1:] != [0]:
        fails.append(f"forwardToIndex: a fresh visit must not restore an old position, "
                     f"got {s.get('forwardToIndex')}")

    print(f"  6. scroll        {len(s):>4} routes  {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- 7. navigation gestures

def check_nav(items: list[dict], pages: list[dict]) -> list[str]:
    """The bottom bar's two rules, and the swipe-back gesture.

    Plain <a href="#/read"> links make the tab bar forget: every tap dumps you at the top of the
    section, and there is no way to pop back out of a reading without the header's back button. The
    handler gives the bar phone-app behaviour instead — a tab you are not on resumes where you left
    it, a tab you are on pops to its home, and a second tap at home goes to the top.

    The swipe is the same "go back" the ‹ button runs, and the risk is all in false positives: a
    gesture that fires while you meant to scroll, or inside a table that scrolls itself, hijacks the
    page. Most of what follows is the gestures that must *not* navigate."""
    sources = [DOM_STUB] + [(DOCS / n).read_text(encoding="utf-8")
                            for n in ("config.js", "sm2.js", "session.js", "analytics.js",
                                      "supabase.js", "store.js")]
    sources.append(BOOT_CALL.sub("", (DOCS / "app.js").read_text(encoding="utf-8")))

    driver = """
content.items = PAYLOAD.items;
content.itemsById = new Map(PAYLOAD.items.map(i => [i.id, i]));
content.version = 'testbundle';
content.pages = PAYLOAD.pages;
content.pagesBySlug = new Map(PAYLOAD.pages.map(p => [p.slug, p]));
content.readingsLoaded = true;
ensureState(content.items, getState(), PAYLOAD.today);

const steps = {};
function go(hash, scrolledTo) {
  if (scrolledTo !== undefined) globalThis.window.scrollY = scrolledTo;
  location.hash = hash;
  render();
}
// The stub's location doesn't fire hashchange, so each tap is followed by the render the browser
// would have done for it.
function tap(tab, scrolledTo) {
  if (scrolledTo !== undefined) globalThis.window.scrollY = scrolledTo;
  __scrolls.length = 0;
  __tap(tab);
  render();
  return { hash: location.hash, scrolls: __scrolls.slice() };
}

// A swipe, reported as what it did: how many history entries it traversed, and where it left us.
function swipe(o) {
  const backs = __backs;
  __swipe(o);
  const out = { backs: __backs - backs, hash: location.hash };
  render();
  return out;
}
// The ‹ button, reported the same way, so both routes into goBack() are held to the same answer.
function back() {
  const backs = __backs;
  __back();
  const out = { backs: __backs - backs, hash: location.hash };
  render();
  return out;
}
const across = { x0: 120, y0: 400, x1: 300, y1: 410 };   // a clean rightward drag

const slugA = PAYLOAD.pages[0].slug, slugB = PAYLOAD.pages[1].slug;

// The very first render is the entry the app opened on — a reading here, standing in for a deep
// link or a relaunch that restored the URL. There is nothing behind it to pop.
go(`#/read/${slugA}`);
steps.swipeAtRoot = swipe(across);

go('#/read');
steps.swipeOnIndex = swipe(across);      // no back button showing: not a back gesture
go(`#/read/${slugA}`, 0);
steps.swipeBack    = swipe(across);      // reached by navigation: pops
go(`#/read/${slugA}`, 0);                // back onto a reading for the false-positive cases
steps.swipeDown    = swipe({ x0: 120, y0: 200, x1: 150, y1: 560 });   // a scroll, not a swipe
steps.swipeShort   = swipe({ x0: 120, y0: 400, x1: 160, y1: 400 });   // under the distance floor
steps.swipeDiagonal = swipe({ x0: 120, y0: 400, x1: 190, y1: 440 });  // far enough, but not horizontal
steps.swipeLeft    = swipe({ x0: 300, y0: 400, x1: 120, y1: 400 });   // leftward is not "back"
steps.swipeFromEdge = swipe({ ...across, x0: 8, x1: 220 });           // iOS's own gesture zone
steps.swipeInTable = swipe({ ...across,
  target: { closest: () => ({ scrollWidth: 900, clientWidth: 320 }) } });

steps.awayToStats = tap('stats', 520);   // leaving the reading part-way down
steps.backToRead  = tap('read', 40);     // -> the reading again, at 520
steps.popToHome   = tap('read', 300);    // same tab -> the readings index
steps.tapAtHome   = tap('read', 700);    // already home -> the top
steps.freshTab    = tap('you');          // never visited: its home

// Back means back *within the tab*. The browser keeps one stack with every tab's pages interleaved,
// so stepping off a reading to check Stats and tapping Read again leaves Stats sitting directly
// behind you — and a plain history.back() there drops you out of the tab you are reading in.
go('#/read');
go(`#/read/${slugA}`);
go(`#/read/${slugB}`);
tap('stats');
tap('read');                             // resumes slugB, with #/stats now behind it
steps.backAfterTabHop = back();          // -> slugA: the last page in *this* tab
steps.backToIndex     = back();          // -> the readings index
steps.backAtHome      = back();          // nothing behind a tab's home

// A session left mid-run: the tab still pops to the setup screen, but the session has to be
// reachable from there or popping the tab would silently strand it.
const three = PAYLOAD.items.slice(0, 3).map(i => i.id);
saveSession({ queue: three, idx: 1, stage: 'prompt', results: [], startedAt: Date.now(),
              itemStartAt: Date.now(), draft: { confidence: null, response: '' } });
go('#/study/run');
steps.leaveRun    = tap('read');         // step off mid-session
steps.resumeRun   = tap('study');        // -> back into the running session
steps.runToHome   = tap('study', 200);   // same tab -> the setup screen
steps.setupResume = viewStudySetup().includes('data-action="resume"');
clearSession();
steps.setupNoResume = !viewStudySetup().includes('data-action="resume"');

__emit({ steps, slugA, slugB });
"""
    got = run_js(sources, driver, {"items": items, "pages": pages, "today": "2026-07-29"})
    if got.get("__error"):
        return [f"tabs harness error — {got['__error']}"]

    s = got["steps"]
    fails: list[str] = []

    def expect(name, hash_, scrolls, why):
        step = s.get(name, {})
        if step.get("hash") != hash_ or step.get("scrolls") != scrolls:
            fails.append(f"{name}: expected {hash_} / scrollTo {scrolls}, "
                         f"got {step.get('hash')} / {step.get('scrolls')} — {why}")

    expect("awayToStats", "#/stats", [0], "a different tab opens at its own home")
    expect("backToRead", f"#/read/{got['slugA']}", [520],
           "returning to a tab resumes the page it was left on, where it was left")
    expect("popToHome", "#/read", [0], "tapping the tab you are on pops to that tab's home")
    expect("tapAtHome", "#/read", [0], "tapping again at home scrolls to the top")
    expect("freshTab", "#/you", [0], "a tab with no history opens at its home")
    expect("leaveRun", "#/read", [0], "stepping off mid-session leaves the session running")
    expect("resumeRun", "#/study/run", [0], "returning to Study resumes the running session")
    expect("runToHome", "#/study", [0], "tapping Study during a session pops to the setup screen")

    if not s.get("setupResume"):
        fails.append("study setup offers no way back into a session in progress — popping the tab "
                     "would strand it")
    if not s.get("setupNoResume"):
        fails.append("study setup offers 'resume' with no session saved")

    # Going back, from either the ‹ button or the swipe, walks *this tab's* history. Traversing
    # (backs > 0) rather than pushing the old route again is what keeps the browser's own
    # back/forward and the scroll restoration honest.
    for name, want, why in [
        ("backAfterTabHop", {"backs": 3, "hash": f"#/read/{got['slugA']}"},
         "back should return to the last reading in this tab, not to the tab visited in between"),
        ("backToIndex", {"backs": 1, "hash": "#/read"},
         "and should keep walking that tab back to its index"),
        ("backAtHome", {"backs": 0, "hash": "#/read"},
         "a tab's home has nothing behind it — back must not walk out of the app"),
    ]:
        if s.get(name) != want:
            fails.append(f"{name}: expected {want}, got {s.get(name)} — {why}")

    # The swipe. One gesture must go back; the rest must leave the page exactly where it was.
    if s.get("swipeBack", {}).get("backs") != 1:
        fails.append(f"swipeBack: a rightward swipe on a reading should pop one history entry, "
                     f"got {s.get('swipeBack')}")
    if s.get("swipeAtRoot") != {"backs": 0, "hash": "#/read"}:
        fails.append(f"swipeAtRoot: swiping on the first page the app drew must fall back to the "
                     f"section home, not walk out of the app — got {s.get('swipeAtRoot')}")
    reading, index = f"#/read/{got['slugA']}", "#/read"
    for name, stays_on, why in [
        ("swipeOnIndex", index, "a tab's home has no back to go to"),
        ("swipeDown", reading, "a vertical drag is a scroll"),
        ("swipeShort", reading, "a short drag is under the distance floor"),
        ("swipeDiagonal", reading, "a drag that is only half horizontal is ambiguous, so it waits"),
        ("swipeLeft", reading, "leftward is not back"),
        ("swipeFromEdge", reading, "the left edge belongs to iOS's own gesture — two pops otherwise"),
        ("swipeInTable", reading, "a sideways-scrolling table owns the gesture"),
    ]:
        if s.get(name) != {"backs": 0, "hash": stays_on}:
            fails.append(f"{name}: expected no navigation ({why}), got {s.get(name)}")

    print(f"  7. nav           {len(s):>4} gestures {'ok' if not fails else f'{len(fails)} FAILED'}")
    return fails


# ---------------------------------------------------------------- 8. version / update path

def check_version() -> list[str]:
    """A deployed app must be able to tell it is out of date.

    This is the check that would have caught the deploys-go-unnoticed bug. version.json originally
    carried only a *content* hash, so a code-only release — a restyled chart, a bug fix — left it
    byte-identical and every device reported "already current" while running last week's JavaScript.
    `build` has to cover the shell too, and the app has to compare against `build`."""
    fails: list[str] = []
    sys.path.insert(0, str(ROOT / "apps"))
    import build_web  # noqa: E402

    path = DOCS / "content" / "version.json"
    if not path.exists():
        return ["docs/content/version.json missing — run `python apps/build_web.py`"]
    payload = json.loads(path.read_text(encoding="utf-8"))

    for field in ("version", "build"):
        if not payload.get(field):
            fails.append(f"version.json has no '{field}'")
    if fails:
        return fails

    # The published build id must match what the current tree hashes to — i.e. the bundle was
    # rebuilt after the last edit. A stale one here means a deploy would ship mismatched files.
    expected = build_web.build_hash(payload["version"])
    if expected != payload["build"]:
        fails.append(f"version.json build is {payload['build']} but the tree hashes to {expected} "
                     f"— run `python apps/build_web.py` before committing")

    # Every shell file must actually be in the hash, or changing it wouldn't bump the build.
    for name in ("app.js", "style.css", "sw.js", "index.html", "analytics.js", "store.js"):
        if name not in build_web.SHELL_FILES:
            fails.append(f"build_hash ignores {name} — a change to it would deploy unnoticed")

    # Changing a shell file has to change the id. Verified by hashing a mutated copy rather than by
    # reading the code, so the check survives a refactor of how the hash is computed.
    original = (DOCS / "app.js").read_bytes()
    try:
        (DOCS / "app.js").write_bytes(original + b"\n// version-check probe\n")
        mutated = build_web.build_hash(payload["version"])
    finally:
        (DOCS / "app.js").write_bytes(original)
    if mutated == payload["build"]:
        fails.append("editing app.js does not change the build id — updates would go unnoticed")

    # The app must compare the build, not the content hash.
    app_src = (DOCS / "app.js").read_text(encoding="utf-8")
    if ".build" not in app_src:
        fails.append("app.js never reads version.json's `build` field")
    if "adoptNewBuild" not in app_src or "adoptNewBuild()" not in app_src:
        fails.append("app.js does not check for a new build on boot")

    # The worker must not revalidate through the HTTP cache, or GitHub Pages' max-age=600 lets it
    # refresh its cache with the same stale bytes it already had.
    sw_src = (DOCS / "sw.js").read_text(encoding="utf-8")
    if "no-cache" not in sw_src:
        fails.append("sw.js fetches without cache:'no-cache' — it can revalidate against stale bytes")
    if re.search(r"(?<!fetchFresh\()\bfetch\(request\)", sw_src):
        fails.append("sw.js has a plain fetch(request) that goes through the HTTP cache")

    print(f"  8. version     build {payload['build']}  {'ok' if not fails else f'{len(fails)} FAILED'}")
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
        fails += check_scroll(items, sample)
        fails += check_nav(items, sample)
    else:
        fails.append("docs/content/readings.json missing — run `python apps/build_web.py`")
    fails += check_version()

    if fails:
        print("\nFAILED:")
        for f in fails:
            print(f"  - {f}")
        sys.exit(1)
    print("\nAll web logic checks passed.")


if __name__ == "__main__":
    main()
