#!/usr/bin/env python3
"""SM-2 spaced-repetition scheduler + review logging. Stdlib only.

This is the engine the quiz runner uses; it is deliberately separate from the Streamlit UI so it can
be tested and reasoned about on its own (`python apps/scheduler.py` prints a due-queue summary).

Design (per CLAUDE.md): the item *content/metadata* lives in items/build/items.json (read-only here);
the *scheduling state* is owned by the app and lives in review_state.json; every attempt is appended
to review_log.csv.

History: this started as Leitner (numbered boxes, fixed cadence) to get the loop running. It has been
upgraded to **SM-2** — the per-item adaptive rule early Anki used (see
learning-science-for-self-study.md, "Option B"). Each item now carries its own easiness factor and
interval instead of a box number; easy items drift to long intervals, items you keep missing stay
frequent. Old box-based state is migrated transparently on load (see `ensure_state`).

The three self-grades the UI offers map onto SM-2's 0–5 recall-quality scale `q`:
    missed  -> q=2  (failed; relearn from interval 1, ease takes a real hit)
    shaky   -> q=3  (a pass, but bring it back soon and grow ease slowly)
    correct -> q=5  (clean recall; interval expands by the easiness factor)
'shaky' additionally short-circuits the interval so it re-queues sooner than a clean pass — the same
intent the old Leitner 'hold the box, requeue early' branch had.
"""
from __future__ import annotations

import csv
import json
import random
import re
import string
from datetime import date, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEMS_JSON = ROOT / "items" / "build" / "items.json"
STATE_JSON = ROOT / "review_state.json"
REVIEW_LOG = ROOT / "review_log.csv"

# ---- SM-2 constants ----
DEFAULT_EASE = 2.5      # starting easiness factor
MIN_EASE = 1.3          # floor; SM-2 never lets a card get easier-rated than this
FIRST_INTERVAL = 1      # days, after the first successful recall
SECOND_INTERVAL = 6     # days, after the second

# self-grade -> SM-2 recall quality (0..5)
QUALITY = {"missed": 2, "shaky": 3, "correct": 5}

# Old Leitner box -> interval in days, used ONLY to migrate pre-upgrade state files.
_LEGACY_BOX_DAYS = {1: 1, 2: 3, 3: 7, 4: 16, 5: 35}

LOG_FIELDS = [
    "timestamp", "item_id", "type", "bloom_level", "cluster",
    "predicted_confidence", "outcome", "interval_before", "interval_after",
    "ease", "reps", "time_taken_s",
]


# ---------- item + state IO ----------

def load_items() -> list[dict]:
    if not ITEMS_JSON.exists():
        raise FileNotFoundError(
            f"{ITEMS_JSON} not found — run `python apps/build_items.py` first.")
    return json.loads(ITEMS_JSON.read_text(encoding="utf-8"))


def load_state() -> dict:
    if STATE_JSON.exists():
        return json.loads(STATE_JSON.read_text(encoding="utf-8"))
    return {}


def save_state(state: dict) -> None:
    STATE_JSON.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def _new_state(today: date) -> dict:
    return {"ease": DEFAULT_EASE, "interval": 0, "reps": 0,
            "due": today.isoformat(), "last": None}


def _migrate_box_state(st: dict, today: date) -> None:
    """Convert a legacy Leitner record ({box, due, reps, last}) to SM-2 in place. The box's cadence
    becomes the SM-2 interval and everyone starts at the default ease; due/last/reps are preserved."""
    box = st.pop("box", 1)
    st["ease"] = DEFAULT_EASE
    st["interval"] = _LEGACY_BOX_DAYS.get(box, FIRST_INTERVAL)
    st.setdefault("reps", 0)
    st.setdefault("due", today.isoformat())
    st.setdefault("last", None)


def ensure_state(items: list[dict], state: dict, today: date | None = None) -> dict:
    """Initialise any new item (box-1-equivalent: due today, never reviewed), migrate any legacy
    box-based records to SM-2, and drop state for items that no longer exist. Returns mutated state."""
    today = today or date.today()
    known = {it["id"] for it in items}
    for it in items:
        st = state.get(it["id"])
        if st is None:
            state[it["id"]] = _new_state(today)
        elif "ease" not in st:          # pre-upgrade Leitner record
            _migrate_box_state(st, today)
    for stale in [k for k in state if k not in known]:
        del state[stale]
    return state


# ---------- scheduling ----------

def due_items(items: list[dict], state: dict, today: date | None = None,
              shuffle: bool = True) -> list[dict]:
    """Items whose due date is today or earlier. Shuffled to interleave (per learning-science doc:
    pull the due set and shuffle rather than serving topic-by-topic)."""
    today = today or date.today()
    due = [it for it in items
           if date.fromisoformat(state[it["id"]]["due"]) <= today]
    if shuffle:
        random.shuffle(due)
    return due


def update(state: dict, item_id: str, outcome: str, today: date | None = None) -> tuple[int, int]:
    """Apply an SM-2 transition. outcome in {'correct','shaky','missed'}.
    Returns (interval_before, interval_after) in days; the new ease/reps land in state[item_id]."""
    today = today or date.today()
    st = state[item_id]
    interval_before = st.get("interval", 0)
    ease = st.get("ease", DEFAULT_EASE)
    reps = st.get("reps", 0)
    q = QUALITY[outcome]

    if outcome == "missed":             # q<3: failed; relearn from scratch
        reps = 0
        interval = FIRST_INTERVAL
    elif outcome == "shaky":            # a pass, but requeue soon — don't advance the rep count
        interval = max(FIRST_INTERVAL, round(interval_before * 0.5)) if interval_before else FIRST_INTERVAL
    else:                               # correct: standard SM-2 expansion
        if reps == 0:
            interval = FIRST_INTERVAL
        elif reps == 1:
            interval = SECOND_INTERVAL
        else:
            interval = max(FIRST_INTERVAL, round(interval_before * ease))
        reps += 1

    # SM-2 easiness update — applied on every review, including lapses.
    ease = max(MIN_EASE, ease + (0.1 - (5 - q) * (0.08 + (5 - q) * 0.02)))

    st["ease"] = round(ease, 3)
    st["reps"] = reps
    st["interval"] = interval
    st["due"] = (today + timedelta(days=interval)).isoformat()
    st["last"] = today.isoformat()
    return interval_before, interval


# ---------- auto-grading (cloze / mcq) ----------

_PUNCT = str.maketrans("", "", string.punctuation)


def normalize(text: str) -> str:
    text = text.lower().strip().translate(_PUNCT)
    return re.sub(r"\s+", " ", text)


def autograde(item: dict, response: str) -> bool | None:
    """Return True/False for auto-gradable types, or None if the item needs self-grading."""
    if item["type"] == "cloze":
        return normalize(response) == normalize(item["answer"])
    if item["type"] == "mcq":
        return normalize(response) == normalize(item["answer"])
    return None


# ---------- review log ----------

def log_attempt(row: dict) -> None:
    """Append one attempt to review_log.csv. If a pre-upgrade (Leitner-schema) log exists, it's
    rotated aside to review_log.leitner.csv so the new SM-2 columns start a clean, consistent file."""
    needs_header = True
    if REVIEW_LOG.exists():
        first_line = REVIEW_LOG.read_text(encoding="utf-8").splitlines()[:1]
        if first_line and first_line[0].split(",") == LOG_FIELDS:
            needs_header = False
        else:
            backup = REVIEW_LOG.with_name("review_log.leitner.csv")
            i = 1
            while backup.exists():
                backup = REVIEW_LOG.with_name(f"review_log.leitner.{i}.csv")
                i += 1
            REVIEW_LOG.rename(backup)
    with REVIEW_LOG.open("a", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=LOG_FIELDS)
        if needs_header:
            w.writeheader()
        w.writerow({k: row.get(k, "") for k in LOG_FIELDS})


# ---------- CLI sanity check ----------

if __name__ == "__main__":
    items = load_items()
    state = ensure_state(items, load_state())
    save_state(state)
    due = due_items(items, state)
    intervals = sorted(state[it["id"]]["interval"] for it in items)
    eases = [state[it["id"]]["ease"] for it in items]
    new = sum(1 for it in items if state[it["id"]]["reps"] == 0)
    print(f"{len(items)} items total | {len(due)} due today ({date.today().isoformat()})")
    print(f"  {new} never-reviewed (new) | {len(items) - new} in rotation")
    if eases:
        print(f"  ease: min={min(eases):.2f} mean={sum(eases) / len(eases):.2f} max={max(eases):.2f}")
        print(f"  interval (days): min={intervals[0]} median={intervals[len(intervals) // 2]} max={intervals[-1]}")
