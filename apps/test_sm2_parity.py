#!/usr/bin/env python3
"""Prove docs/sm2.js and apps/scheduler.py schedule identically.

Why this exists: the phone and the laptop write to the same review_state rows. If the two SM-2
implementations disagree by even a day, an item's schedule silently depends on which device you
happened to grade it on, and nothing would ever surface the drift. So rather than trusting a careful
transliteration, this replays the same transitions through both and diffs them.

Four checks, cheapest and most dangerous first:
  1. rounding      — Python's round() is half-to-even, JavaScript's Math.round() is half-up. A
                     'shaky' grade computes round(interval / 2), so interval 5 gives 2 in Python and
                     3 under Math.round. Exhaustive over the values the scheduler can actually hit.
  2. transitions   — 45k full SM-2 steps from seeded random walks: ease, interval, reps, due, last.
  3. normalize     — the auto-grader's text comparison, over every real item answer plus mutations.
                     Python strips ASCII punctuation only, leaving the corpus's typographic
                     apostrophes and em dashes in place; a Unicode-aware regex in JS would not.
  4. migration     — legacy Leitner box records and the due-date boundary.

There is no node on this machine, so the JS runs under JavaScriptCore via `osascript -l JavaScript`.
docs/sm2.js is an ES module; the harness strips the `export` keywords to evaluate it as a script.

Run:  python apps/test_sm2_parity.py
"""
from __future__ import annotations

import json
import random
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import scheduler as sch  # noqa: E402

ROOT = Path(__file__).resolve().parent.parent
SM2_JS = ROOT / "docs" / "sm2.js"
ITEMS_JSON = ROOT / "items" / "build" / "items.json"
TODAY = date(2026, 7, 29)
OUTCOMES = ["missed", "shaky", "correct"]


# ---------------------------------------------------------------- JS harness

def run_js(driver: str, payload: dict) -> dict:
    """Evaluate docs/sm2.js plus a driver under JavaScriptCore and return the driver's JSON result.

    The result comes back through a temp file rather than stdout: osascript writes console.log to
    stderr and is not something to trust with megabytes of JSON."""
    module = SM2_JS.read_text(encoding="utf-8")
    # ES module -> plain script. Only the `export` keyword needs removing; sm2.js has no imports.
    script_body = re.sub(r"^export\s+", "", module, flags=re.MULTILINE)

    with tempfile.TemporaryDirectory() as tmp:
        out_path = Path(tmp) / "out.json"
        script = f"""
ObjC.import('Foundation');
{script_body}
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
            sys.exit("JS harness produced no output.\n"
                     f"stdout: {proc.stdout.strip()}\nstderr: {proc.stderr.strip()}")
        return json.loads(out_path.read_text(encoding="utf-8"))


# ---------------------------------------------------------------- shared fixtures

def reachable_eases(cap: float = 4.0) -> list[float]:
    """Every ease value the scheduler can actually reach from the 2.5 start, by closure over the
    three grade deltas. Testing arbitrary floats would be testing values that can never occur."""
    seen = {sch.DEFAULT_EASE}
    frontier = [sch.DEFAULT_EASE]
    while frontier:
        e = frontier.pop()
        for q in (2, 3, 5):
            nxt = round(max(sch.MIN_EASE, e + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02))), 3)
            if nxt <= cap and nxt not in seen:
                seen.add(nxt)
                frontier.append(nxt)
    return sorted(seen)


# ---------------------------------------------------------------- 1. rounding

def check_rounding(eases: list[float]) -> list[str]:
    values: list[float] = []
    for n in range(0, 2001):
        values.append(n * 0.5)                       # the 'shaky' halving path
    for interval in range(0, 121):                   # the 'correct' expansion path
        for e in eases:
            values.append(interval * e)
    values = sorted(set(values))

    expected = [round(v) for v in values]
    got = run_js("__emit(PAYLOAD.values.map(roundHalfEven));", {"values": values})

    fails = [f"roundHalfEven({v!r}) -> js {g}, python {e}"
             for v, g, e in zip(values, got, expected) if g != e]
    print(f"  1. rounding      {len(values):>6} values   {'ok' if not fails else f'{len(fails)} MISMATCH'}")
    return fails[:10]


# ---------------------------------------------------------------- 2. transitions

def check_transitions(eases: list[float], walks: int = 3000, steps: int = 15) -> list[str]:
    """Seeded random walks through the state machine. Each walk starts from a fresh item and applies
    a random grade sequence, so the trajectories look like real study histories."""
    rng = random.Random(20260729)
    cases: list[list] = []          # [ease, interval, reps, outcome_index]
    expected: list[list] = []       # [ease, interval, reps, due, last, before, after]

    for _ in range(walks):
        st = {"ease": rng.choice(eases), "interval": rng.choice([0, 1, 2, 3, 5, 6, 9, 15, 16, 35, 45]),
              "reps": rng.randrange(0, 6), "due": TODAY.isoformat(), "last": None}
        for _ in range(steps):
            outcome = OUTCOMES[rng.randrange(3)]
            cases.append([st["ease"], st["interval"], st["reps"], OUTCOMES.index(outcome)])
            state = {"x": dict(st)}
            before, after = sch.update(state, "x", outcome, TODAY)
            st = state["x"]
            expected.append([st["ease"], st["interval"], st["reps"], st["due"], st["last"],
                             before, after])

    driver = """
const OUT = [];
for (const c of PAYLOAD.cases) {
  const state = { x: { ease: c[0], interval: c[1], reps: c[2], due: PAYLOAD.today, last: null } };
  const r = update(state, 'x', PAYLOAD.outcomes[c[3]], PAYLOAD.today);
  const s = state.x;
  OUT.push([s.ease, s.interval, s.reps, s.due, s.last, r.before, r.after]);
}
__emit(OUT);
"""
    got = run_js(driver, {"cases": cases, "outcomes": OUTCOMES, "today": TODAY.isoformat()})

    fails = []
    for c, g, e in zip(cases, got, expected):
        if g != e:
            fails.append(f"ease={c[0]} interval={c[1]} reps={c[2]} {OUTCOMES[c[3]]}: js {g} != py {e}")
    print(f"  2. transitions   {len(cases):>6} steps    {'ok' if not fails else f'{len(fails)} MISMATCH'}")
    return fails[:10]


# ---------------------------------------------------------------- 3. normalize / autograde

def mutate(text: str, rng: random.Random) -> list[str]:
    """Responses a person might actually type: different case, dropped punctuation, sloppy spacing,
    a truncation. These are the inputs the two normalizers have to agree on."""
    return [
        text,
        text.upper(),
        text.lower(),
        f"  {text}  ",
        text.replace(",", "").replace(".", ""),
        re.sub(r"\s+", "  ", text),
        text[: max(1, len(text) // 2)],
        text + " — and also this",
    ]


def check_normalize() -> list[str]:
    items = json.loads(ITEMS_JSON.read_text(encoding="utf-8"))
    rng = random.Random(7)
    strings: list[str] = []
    for it in items:
        strings += mutate(it["answer"], rng)
        for opt in (it.get("options") or [])[:2]:
            strings.append(opt)
    strings.append("")
    # Every ASCII punctuation mark, plus the typographic characters the corpus is full of and that
    # must survive normalization on both sides.
    strings.append("!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~")
    strings.append("Rogers’ “core” conditions — the client’s frame · naïve · café")
    strings = list(dict.fromkeys(strings))

    expected = [sch.normalize(s) for s in strings]
    got = run_js("__emit(PAYLOAD.strings.map(normalize));", {"strings": strings})
    fails = [f"normalize({s!r}) -> js {g!r}, python {e!r}"
             for s, g, e in zip(strings, got, expected) if g != e]

    # autograde over the auto-gradable items, using both the right answer and a wrong one
    auto = [it for it in items if it["type"] in ("cloze", "mcq")]
    cases = []
    for it in auto:
        right = it.get("correct") or it["answer"]
        cases.append({"item": it, "response": right, "expect": sch.autograde(it, right)})
        wrong = "definitely not the answer"
        cases.append({"item": it, "response": wrong, "expect": sch.autograde(it, wrong)})
    open_item = next(it for it in items if it["type"] not in ("cloze", "mcq"))
    cases.append({"item": open_item, "response": "anything", "expect": sch.autograde(open_item, "anything")})

    got_auto = run_js("__emit(PAYLOAD.cases.map(c => autograde(c.item, c.response)));",
                      {"cases": [{"item": c["item"], "response": c["response"]} for c in cases]})
    for c, g in zip(cases, got_auto):
        if g != c["expect"]:
            fails.append(f"autograde({c['item']['id']}, {c['response'][:30]!r}) -> js {g}, python {c['expect']}")

    print(f"  3. normalize     {len(strings):>6} strings  "
          f"{len(cases)} autogrades   {'ok' if not fails else f'{len(fails)} MISMATCH'}")
    return fails[:10]


# ---------------------------------------------------------------- 4. migration + due boundary

def check_state_handling() -> list[str]:
    items = [{"id": "a"}, {"id": "b"}, {"id": "c"}]
    seed = {
        "a": {"box": 4, "due": "2026-07-01", "reps": 3, "last": "2026-06-15"},   # legacy Leitner
        "b": {"ease": 2.36, "interval": 6, "reps": 2, "due": "2026-07-29", "last": "2026-07-23"},
        "zz-deleted": {"ease": 2.5, "interval": 1, "reps": 0, "due": "2026-01-01", "last": None},
    }

    py_state = sch.ensure_state([dict(i) for i in items], json.loads(json.dumps(seed)), TODAY)
    py_due = sorted(it["id"] for it in sch.due_items(items, py_state, TODAY, shuffle=False))

    driver = """
const state = PAYLOAD.seed;
ensureState(PAYLOAD.items, state, PAYLOAD.today);
const due = dueItems(PAYLOAD.items, state, PAYLOAD.today, false).map(i => i.id).sort();
__emit({ state: state, due: due });
"""
    got = run_js(driver, {"items": items, "seed": seed, "today": TODAY.isoformat()})

    fails = []
    # Python leaves `last: None` where JS produces `last: null` — same value through JSON.
    if json.loads(json.dumps(py_state)) != got["state"]:
        fails.append(f"ensureState diverged:\n    js {got['state']}\n    py {py_state}")
    if py_due != got["due"]:
        fails.append(f"dueItems: js {got['due']} != py {py_due}")
    print(f"  4. migration     {'':>6}          {'ok' if not fails else f'{len(fails)} MISMATCH'}")
    return fails


# ---------------------------------------------------------------- main

def main() -> None:
    if not SM2_JS.exists():
        sys.exit(f"{SM2_JS.relative_to(ROOT)} not found.")
    if not ITEMS_JSON.exists():
        sys.exit("items/build/items.json not found — run `python apps/build_items.py` first.")

    eases = reachable_eases()
    print(f"SM-2 parity: apps/scheduler.py vs docs/sm2.js "
          f"({len(eases)} reachable ease values, JS via JavaScriptCore)")

    fails: list[str] = []
    fails += check_rounding(eases)
    fails += check_transitions(eases)
    fails += check_normalize()
    fails += check_state_handling()

    if fails:
        print("\nFAILED — the two schedulers disagree:")
        for f in fails:
            print(f"  - {f}")
        sys.exit(1)
    print("\nAll parity checks passed — the phone and the laptop will schedule identically.")


if __name__ == "__main__":
    main()
