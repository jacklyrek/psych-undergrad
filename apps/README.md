# apps/ — Streamlit front-ends + build/scheduler

Python that consumes the learning layer. **Reads** `../items/build/items.json`, **writes** attempts
to `../review_log.csv`, and **never** modifies readings or item source.

Build order — value-first:
1. ✅ `build_items.py` — compile `items/*.md` (fenced json blocks) → `items/build/items.json`. Stdlib only. Validates ids/vocab/source_page. `python apps/build_items.py`
2. ✅ `scheduler.py` — **SM-2** (per-item easiness + adaptive interval; early-Anki rule). Self-grades map to recall quality `q`: missed→2, shaky→3, correct→5; 'shaky' requeues sooner. Stdlib only; owns `review_state.json` + appends `review_log.csv` (now logs `interval_before/after`, `ease`, `reps`). Captures `predicted_confidence` for calibration. `python apps/scheduler.py` prints a due-queue summary. (Upgraded from the original Leitner engine: old box-state is migrated on load; a pre-upgrade `review_log.csv` is rotated to `review_log.leitner.csv` on first write.)
3. ✅ `quiz_runner.py` — the study loop: due item → predict confidence → answer → reveal + feedback (with the source reading inline) → self/auto grade → schedule update. Interleaves (shuffles the due set). Sidebar filters (cluster/Bloom/type), session length, cram toggle. End screen surfaces overconfident misses.
4. ⬜ `workbook.py` — open-ended exercises / self-explanation, reveal model answer to self-grade.
5. ⬜ `calibration.py` — dashboard of predicted-confidence vs. actual; surfaces most-overconfident items (reads `review_log.csv`).

**Run the quiz runner:** `python -m streamlit run apps/quiz_runner.py` (needs `pip install -r requirements.txt`; build steps don't).
