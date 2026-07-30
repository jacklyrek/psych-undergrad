# apps/ — Streamlit front-ends + build/scheduler

Python that consumes the learning layer. **Reads** `../items/build/items.json`, **writes** attempts
to `../review_log.csv`, and **never** modifies readings or item source.

Build order — value-first:
1. ✅ `build_items.py` — compile `items/*.md` (fenced json blocks) → `items/build/items.json`. Stdlib only. Validates ids/vocab/source_page. `python apps/build_items.py`
2. ✅ `scheduler.py` — **SM-2** (per-item easiness + adaptive interval; early-Anki rule). Self-grades map to recall quality `q`: missed→2, shaky→3, correct→5; 'shaky' requeues sooner. Stdlib only; owns `review_state.json` + appends `review_log.csv` (now logs `interval_before/after`, `ease`, `reps`). Captures `predicted_confidence` for calibration. `python apps/scheduler.py` prints a due-queue summary. (Upgraded from the original Leitner engine: old box-state is migrated on load; a pre-upgrade `review_log.csv` is rotated to `review_log.leitner.csv` on first write.)
3. ✅ `quiz_runner.py` — the study loop: due item → predict confidence → answer → reveal + feedback (with the source reading inline) → self/auto grade → schedule update. Interleaves (shuffles the due set). Sidebar filters (cluster/Bloom/type), session length, cram toggle. End screen surfaces overconfident misses.
4. ✅ `build_web.py` — compile `wiki/` + `research/` + the item bank → `docs/content/*.json` for the phone app. Renders markdown to HTML ahead of time, resolves `[[wikilinks]]` to in-app routes, wires `[S3]` citations to their source notes, computes backlinks, and reports broken links / items whose `source_page` isn't in the bundle. Stdlib only. `python apps/build_web.py`
5. ✅ `supa.py` — Supabase client over `urllib` (stdlib). Auth, state/log pull+push, the `record_attempt` RPC, and the offline outbox. Credentials from a gitignored `.env`; signs in as the ordinary user so RLS applies here exactly as on the phone — no `service_role` key anywhere.
6. ✅ `sync_supabase.py` — `status` / `push` / `pull` / `flush`. Seeds Supabase from the local files (idempotent), or pulls a fresh snapshot back into git. `python apps/sync_supabase.py status`
7. ✅ `make_icons.py` — generates the PWA home-screen icons. Pure-stdlib PNG writer (zlib + struct), so no Pillow dependency for four icons.
8. ⬜ `workbook.py` — open-ended exercises / self-explanation, reveal model answer to self-grade.
9. ✅ `calibration.py` — **superseded**: the Stats tab of the phone app ([`docs/`](../docs/)) is the calibration dashboard, reading the same synced log. `analytics.js` has the maths (buckets, Brier score, weakest clusters).

**Run the quiz runner:** `python -m streamlit run apps/quiz_runner.py` (needs `pip install -r requirements.txt`; build steps don't).

**Run the tests:** `python apps/test_sm2_parity.py` and `python apps/test_web_logic.py`. Both run the app's JavaScript under JavaScriptCore (`osascript -l JavaScript`) — there is no node on this machine. The parity test is the important one: it replays ~45k SM-2 transitions through `scheduler.py` and `docs/sm2.js` and diffs them, because both write the same `review_state` rows and a silent disagreement would make an item's schedule depend on which device graded it.

## Shared state with the phone

`scheduler.py` now has an optional Supabase layer so the laptop and the phone share one queue:

- `sync_down(items)` — flush the outbox, pull remote state, merge into `review_state.json`. `quiz_runner.py` calls it once per Streamlit session.
- `push_attempt(attempt)` — send one graded attempt; queues to `.supabase-outbox.jsonl` if offline. Never raises: a sync problem must not lose a review.
- `remote_report()` — the one-line status in the sidebar.

All of it no-ops without a `.env`, and the scheduler stays stdlib-only and fully local — same behaviour as before. Setup steps are in [`docs/README.md`](../docs/README.md).
