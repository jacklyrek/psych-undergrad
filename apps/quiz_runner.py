#!/usr/bin/env python3
"""Quiz runner — the study loop. Streamlit UI over the Leitner scheduler.

Per CLAUDE.md: reads items/build/items.json, writes attempts to review_log.csv, and NEVER modifies
readings or item source. The loop, per the learning-science doc:
    due item  ->  predict confidence (BEFORE seeing answer)  ->  answer  ->  reveal + feedback
    (with a link to the source reading)  ->  self/auto grade  ->  scheduler update.

Run:  streamlit run apps/quiz_runner.py
Requires: pip install streamlit   (the scheduler/build steps are stdlib-only; only this UI needs it.)
"""
from __future__ import annotations

import re
import time
from datetime import date, datetime
from pathlib import Path

import streamlit as st

import scheduler as sch  # same directory

st.set_page_config(page_title="Psych Wiki — Quiz Runner", page_icon="🧠", layout="centered")
ROOT = sch.ROOT

CLOZE_BLANK = re.compile(r"\{\{.*?\}\}")


def display_prompt(item: dict) -> str:
    """Prompt as shown to the studier. For cloze items, the {{...}} deletion is hidden
    behind a blank so the answer isn't given away in the question."""
    if item.get("type") == "cloze":
        return CLOZE_BLANK.sub("\\_\\_\\_\\_\\_", item["prompt"])
    return item["prompt"]


# ---------- data ----------

@st.cache_data
def _load_items(_mtime: float):
    # _mtime is part of the cache key: rebuilding items.json bumps its mtime, which invalidates
    # the cache so the app picks up new items/fields (e.g. unit) without a manual restart.
    return sch.load_items()


def _items_mtime() -> float:
    p = sch.ITEMS_JSON
    return p.stat().st_mtime if p.exists() else 0.0


def read_reading(rel_path: str) -> str | None:
    p = ROOT / rel_path
    return p.read_text(encoding="utf-8") if p.exists() else None


# ---------- session bootstrap ----------

def matches_filters(it, filters):
    if filters["units"] and it.get("unit") not in filters["units"]:
        return False
    if filters["blooms"] and it.get("bloom_level") not in filters["blooms"]:
        return False
    if filters["types"] and it.get("type") not in filters["types"]:
        return False
    return True


def new_session(items, filters, length, cram):
    state = sch.ensure_state(items, sch.load_state())
    sch.save_state(state)
    pool = sch.due_items(items, state, shuffle=True) if not cram else _shuffled(items)
    pool = [it for it in pool if matches_filters(it, filters)][:length]
    st.session_state.queue = [it["id"] for it in pool]
    st.session_state.idx = 0
    st.session_state.stage = "prompt"
    st.session_state.results = []
    st.session_state.started = time.time()
    st.session_state.item_start = time.time()


def _shuffled(items):
    import random
    xs = list(items)
    random.shuffle(xs)
    return xs


def current_item(items):
    iid = st.session_state.queue[st.session_state.idx]
    return next(it for it in items if it["id"] == iid)


# ---------- sidebar: session setup ----------

items = _load_items(_items_mtime())
def _unit_sort_key(u: str):
    """Numeric units in numeric order (1, 2, ... 10), then elective modules alphabetically."""
    return (0, int(u), "") if u.isdigit() else (1, 0, u)


all_units = sorted({it.get("unit") for it in items if it.get("unit")}, key=_unit_sort_key)
all_blooms = ["remember", "understand", "apply", "analyze", "evaluate"]
all_types = sorted({it["type"] for it in items})


def unit_label(u: str) -> str:
    """Friendly label for a unit value: numeric units -> 'Unit N', elective modules kept as-is."""
    return f"Unit {u}" if u.isdigit() else u

# Reconcile with Supabase once per Streamlit session, before any due count is computed — otherwise
# the sidebar would show yesterday's queue when the phone has already worked through part of it.
# Guarded by session_state because Streamlit re-runs this whole file on every interaction.
if "synced" not in st.session_state:
    st.session_state.synced = sch.sync_down(items)

state_now = sch.ensure_state(items, sch.load_state())
due_now = sch.due_items(items, state_now, shuffle=False)

DEFAULT_LENGTH = min(15, max(5, len(items)))
NO_FILTERS = {"units": [], "blooms": [], "types": []}

with st.sidebar:
    st.header("⚙️ Customize session")
    # The filter widgets render below this caption, but their values persist in session_state
    # across Streamlit's rerun-on-interaction, so the due count reflects the current selection.
    sel = {"units": st.session_state.get("f_units", []),
           "blooms": st.session_state.get("f_blooms", []),
           "types": st.session_state.get("f_types", [])}
    if any(sel.values()):
        due_sel = [it for it in due_now if matches_filters(it, sel)]
        st.caption(f"{len(items)} items in bank · **{len(due_sel)} due today in your selection** "
                   f"({len(due_now)} due overall)")
    else:
        st.caption(f"{len(items)} items in bank · **{len(due_now)} due today**")

    mode = st.radio(
        "Mode",
        ["Spaced — only what's due", "Cram — ignore due dates"],
        captions=[
            "The default, healthiest loop. Serves what the scheduler says you're due to review.",
            "Useful right before an exam, but it's massing — don't make it the habit.",
        ],
    )
    cram = mode.startswith("Cram")

    max_len = max(5, len(items))
    length = st.slider("How many items this session?", 5, max_len, min(DEFAULT_LENGTH, max_len))

    with st.expander("🎯 Focus on specific material (optional)"):
        st.caption("Leave empty to draw from everything.")
        f_units = st.multiselect("Units", all_units, default=[], format_func=unit_label, key="f_units",
                                 help="Focus on one or more syllabus units (or an elective module).")
        f_blooms = st.multiselect("Bloom levels", all_blooms, default=[], key="f_blooms",
                                  help="remember → understand → apply → analyze → evaluate. Apply/analyze is where exams concentrate.")
        f_types = st.multiselect("Item types", all_types, default=[], key="f_types")
    filters = {"units": f_units, "blooms": f_blooms, "types": f_types}

    st.divider()
    if st.button("Start with these settings", type="primary", use_container_width=True):
        new_session(items, filters, length, cram)
        st.rerun()

    st.divider()
    # The phone (docs/) writes to the same Supabase tables, so say plainly whether this instance is
    # seeing that shared state or working from the local files alone.
    sync = st.session_state.synced
    st.caption(f"**Sync:** {sch.remote_report()}")
    if sync.get("error"):
        st.warning(f"Supabase said: {sync['error']}")
    elif sync.get("online") and sync.get("changed"):
        st.caption(f"Pulled {sync['pulled']} items from Supabase — "
                   f"{sync['changed']} had newer progress (studied on the phone).")
    if st.button("Sync now", use_container_width=True):
        st.session_state.synced = sch.sync_down(items)
        st.rerun()

st.title("🧠 Quiz Runner")

if "queue" not in st.session_state:
    # one-click path: sensible defaults, no settings needed
    if due_now:
        n = min(DEFAULT_LENGTH, len(due_now))
        label = f"▶  Start studying — {n} item{'s' if n != 1 else ''} due today"
        quick_cram = False
    else:
        n = min(DEFAULT_LENGTH, len(items))
        label = f"▶  Start studying — {n} items (nothing due, so cramming)"
        quick_cram = True

    if st.button(label, type="primary", use_container_width=True):
        new_session(items, NO_FILTERS, DEFAULT_LENGTH, quick_cram)
        st.rerun()
    st.caption("One click, sensible defaults — spaced mode, a balanced mix, no filters. "
               "To set length, mode, or focus on a unit, open **Customize session** in the sidebar.")
    st.stop()

queue = st.session_state.queue
if not queue:
    st.warning("Nothing matches those filters / nothing due. Loosen the filters or try cram mode.")
    st.stop()


# ---------- end-of-session summary ----------

def show_summary():
    res = st.session_state.results
    n = len(res)
    correct = sum(1 for r in res if r["outcome"] == "correct")
    shaky = sum(1 for r in res if r["outcome"] == "shaky")
    missed = sum(1 for r in res if r["outcome"] == "missed")
    st.success(f"Session done — {n} items in "
               f"{int(time.time() - st.session_state.started)}s")
    c1, c2, c3 = st.columns(3)
    c1.metric("Got it", correct)
    c2.metric("Shaky", shaky)
    c3.metric("Missed", missed)

    # lightweight calibration surfacing (the fluency-illusion check)
    overconf = [r for r in res if r["predicted_confidence"] >= 70 and r["outcome"] == "missed"]
    if overconf:
        st.error("**Overconfident misses** — you felt sure and got these wrong. "
                 "These are exactly what the fluency illusion hides; they jump the queue next time.")
        for r in overconf:
            st.write(f"- `{r['item_id']}` (confidence {r['predicted_confidence']}%)")
    st.caption("Full attempt history is in review_log.csv — the calibration dashboard (built later) "
               "reads it.")
    if st.button("New session"):
        for k in ("queue", "idx", "stage", "results"):
            st.session_state.pop(k, None)
        st.rerun()


if st.session_state.idx >= len(queue):
    show_summary()
    st.stop()


# ---------- the item loop ----------

item = current_item(items)
st.progress(st.session_state.idx / len(queue),
            text=f"Item {st.session_state.idx + 1} of {len(queue)}")
st.caption(f"`{item['type']}` · {item['bloom_level']} · {unit_label(item.get('unit', '—'))}")

st.markdown(f"### {display_prompt(item)}")

# --- STAGE 1: predict confidence + answer, BEFORE revealing ---
if st.session_state.stage == "prompt":
    conf = st.slider("Before you answer — how confident are you? (%)", 0, 100, 50, step=5,
                     key=f"conf_{item['id']}")
    if item["type"] == "mcq" and item.get("options"):
        st.radio("Your answer", item["options"], key=f"resp_{item['id']}")
    elif item["type"] == "cloze":
        st.text_input("Fill the blank", key=f"resp_{item['id']}")
    else:
        st.text_area("Answer in your own words (then grade yourself against the model answer)",
                     key=f"resp_{item['id']}", height=120)

    if st.button("Reveal answer", type="primary"):
        st.session_state.pending = {
            "confidence": conf,
            "response": st.session_state.get(f"resp_{item['id']}", ""),
            "time_taken": round(time.time() - st.session_state.item_start, 1),
        }
        st.session_state.stage = "reveal"
        st.rerun()

# --- STAGE 2: reveal answer + feedback + grade ---
elif st.session_state.stage == "reveal":
    pending = st.session_state.pending
    auto = sch.autograde(item, pending["response"])
    if auto is True:
        st.success("Auto-graded: **correct** ✓")
    elif auto is False:
        st.error("Auto-graded: **not a match.**")

    # show what you wrote next to the model answer so you can compare directly
    a1, a2 = st.columns(2)
    with a1:
        st.markdown("**Your answer**")
        st.warning(pending["response"] or "_(blank)_")
    with a2:
        st.markdown("**Model answer**")
        if item["type"] == "mcq":
            # Show the graded-against option so it lines up with the auto-grade banner;
            # the prose in `answer` is the explanation, surfaced below.
            st.info(item.get("correct") or item["answer"])
            if item.get("answer") and item["answer"] != item.get("correct"):
                st.caption(item["answer"])
        else:
            st.info(item["answer"])

    # feedback one click from the explanation
    with st.expander(f"📖 Source reading — {item['source_page']}"):
        txt = read_reading(item["source_page"])
        st.markdown(txt if txt else f"(reading not found at {item['source_page']})")

    st.divider()
    st.write("**Grade your recall** (self-grade for open items; you can override the auto-grade):")
    # For auto-gradeable types (mcq/cloze) highlight the button matching the auto result so
    # recording the verdict is one click; the other buttons remain available as an override.
    auto_outcome = {True: "correct", False: "missed"}.get(auto)
    g1, g2, g3 = st.columns(3)
    chosen = None
    if g1.button("❌ Missed", use_container_width=True,
                 type="primary" if auto_outcome == "missed" else "secondary"):
        chosen = "missed"
    if g2.button("🟡 Shaky", use_container_width=True):
        chosen = "shaky"
    if g3.button("✅ Got it", use_container_width=True,
                 type="primary" if auto_outcome == "correct" else "secondary"):
        chosen = "correct"

    if chosen:
        state = sch.ensure_state(items, sch.load_state())
        before, after = sch.update(state, item["id"], chosen)
        sch.save_state(state)
        st_item = state[item["id"]]
        log_row = {
            "timestamp": datetime.now().isoformat(timespec="seconds"),
            "item_id": item["id"],
            "type": item["type"],
            "bloom_level": item["bloom_level"],
            "cluster": item.get("cluster", ""),
            "predicted_confidence": pending["confidence"],
            "outcome": chosen,
            "interval_before": before,
            "interval_after": after,
            "ease": st_item["ease"],
            "reps": st_item["reps"],
            "time_taken_s": pending["time_taken"],
        }
        sch.log_attempt(log_row)
        # Same event, sent to Supabase so the phone sees it. Queues locally if offline; never raises.
        sch.push_attempt(sch.attempt_from_log_row(log_row, st_item))
        st.session_state.results.append({
            "item_id": item["id"], "outcome": chosen,
            "predicted_confidence": pending["confidence"],
        })
        st.session_state.idx += 1
        st.session_state.stage = "prompt"
        st.session_state.item_start = time.time()
        st.session_state.pop("pending", None)
        st.rerun()
