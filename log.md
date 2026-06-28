# Log

Append-only, chronological, greppable. Prefix: `## [YYYY-MM-DD] <op> | Unit N <name> | <counts>`.

## [2026-06-27] scaffold | — | Initialized Psych Learning Wiki
- Read `counseling-syllabus.md` (12 units, 3 tiers) and `learning-science-for-self-study.md`.
- Created schema (`CLAUDE.md`), course map (`course-map.md`), `index.md`, `coverage.md`, `log.md`.
- Created directories: `research/`, `wiki/`, `items/`, `items/build/`, `apps/`.
- Storage decision locked: **hybrid** (markdown source → compiled `items/build/items.json`).
- `create chapter` default locked: **readings + items in one run**.
- Scheduler plan: Leitner first, SM-2 later. Apps not yet built.
- Next: `create chapter 1` (Helping Skills & the Therapeutic Relationship).

## [2026-06-27] create-chapter | Unit 1 Helping Skills | 9 sources, 5 readings, 17 items
- Emphasis (per user): skills-in-the-room + stance shift. Depth: concise.
- Research: triangulated across StatPearls/NCBI [S1], Flückiger 2018 alliance meta-analysis [S2],
  Wampold 2015 common factors [S3], PMC alliance review [S4], Penn State microskills [S5], +others.
  Wampold full text was paywalled (402) — claims corroborated via abstracts/secondary, flagged.
- Readings: unit01-helping-skills (hub), theory-common-factors, concept-core-conditions,
  concept-microskills-hierarchy, concept-therapeutic-alliance. All cited [S#], interlinked.
- Tensions flagged in readings: necessary-vs-sufficient (Rogers); alliance correlation≠causation;
  "relationship beats technique" overshoot.
- Items: 17 across 4 clusters; Bloom spread R=4/U=4/Ap=4/An=2/E=3. Compiled to items/build/items.json
  via apps/build_items.py (stdlib-only compiler written this pass).
- Schema change: item source format set to fenced ```json blocks (no PyYAML dependency).
- Bookkeeping: index.md + coverage.md updated. Known hole: compare-type items thin outside
  microskill-types cluster.
- NOT done: Streamlit quiz runner (apps) — still pending; build next to start studying.

## [2026-06-27] build-app | — | Quiz runner + Leitner scheduler
- apps/scheduler.py: Leitner engine (boxes 1–5, intervals 1/3/7/16/35d), stdlib only. Owns
  review_state.json, appends review_log.csv, captures predicted_confidence. CLI prints due summary.
- apps/quiz_runner.py: Streamlit study loop — predict-confidence → answer → reveal + inline source
  reading → self/auto-grade → schedule update. Interleaves due set; sidebar filters (cluster/Bloom/
  type), session length, cram toggle; end screen flags overconfident misses (fluency-illusion check).
- Auto-grade for cloze/mcq (normalized match) with self-grade override; self-grade for open items.
- Added requirements.txt (streamlit) + .gitignore (pycache, personal review_log/state). Installed
  streamlit 1.58.0. All apps byte-compile clean; scheduler CLI verified (17 items, all box 1, due).
- Run: `python -m streamlit run apps/quiz_runner.py`.
- Next options: build calibration dashboard, workbook mode, or `create chapter 2`.

## [2026-06-27] fix | apps | Cloze rendering bug + build guard
- Bug: quiz_runner printed `item['prompt']` raw, so cloze items showed the `{{answer}}` in the question instead of a blank. Source items were correctly formatted; the fault was in rendering.
- Fix: `display_prompt()` in quiz_runner.py replaces `{{...}}` with a blank for cloze items.
- Future-proofing: build_items.py now fails the build if a `cloze` prompt lacks a `{{...}}` blank, or if a non-cloze prompt contains one (mis-tagged cloze).

## [2026-06-27] fix | Unit 1 Helping Skills | sourcing gap (empathy/sympathy)
- Issue (user spot-check): item `u1-empathy-analyze-01` asks to distinguish empathy/sympathy/interpretation, but `concept-core-conditions.md` only mentioned sympathy in an uncited parenthetical — the item outran its evidence base.
- Research: added [S10] *A Comparison of Empathy and Sympathy…*, The Professional Counselor (NBCC, peer-reviewed) for the empathy/sympathy distinction (Eisenberg et al. 2010; Clark 2010).
- Reading: added a cited "Empathy vs. sympathy vs. interpretation" section to `concept-core-conditions.md` ([S1][S7][S10]); updated the page Sources footer. Item now grounded; no item edit needed.

## [2026-06-27] create-chapter | Unit 2 Counseling Theories | 17 sources, 7 readings, 36 items
- Depth: **in-depth** (per user "create chapter two in depth"; Unit 1 was concise). Scope from
  course-map: six theory families + hub. Emphasis: the syllabus practice rep ("stuck because ___,
  better by ___"), telling the families apart, and the CS fix-it/identity stance caution.
- Research: triangulated across StatPearls/NCBI psychodynamic [S1], defense mechanisms [S2],
  person-centered [S3], CBT [S4]; OpenStax Psychology 2e §16.2 [S5]; Yalom 1980 four givens [S6]
  (via reputable secondary — flagged, verify verbatim against book); LibreTexts Frankl/logotherapy
  [S7]; PMC existential isolation [S8] and CBT history [S9]; EBSCO family systems [S10], ScienceDirect
  differentiation review [S11], Brown 2024 Bowen critique [S12]; Tarragona 2008 postmodern [S13];
  SAGE SFBT [S14]; orientation-tier [S15–S17]. Anchor text Corey (offline) used as backbone.
- Readings: unit02-theories (hub w/ comparison table on stuck/better + time-focus + stance), plus
  theory-psychodynamic, theory-person-centered, theory-existential, theory-cbt, theory-family-systems,
  theory-postmodern. All cited [S#], interlinked; cluster `theory-families` on each.
- Cross-unit: added bidirectional link from Unit 1 `concept-core-conditions` → `theory-person-centered`
  (page already carried source_units [1,2]).
- Tensions flagged: psychodynamic falsifiability/evidence; person-centered necessary-not-sufficient;
  Bowen differentiation measurement + cultural/gender critique; postmodern "no single truth" vs EBP;
  Yalom givens as framework not measured fact; integrative prevalence figures hedged.
- Items: 36, all in `theory-families` cluster (topic tags per school + confusable pairs). Bloom spread
  R=6/U=6/Ap=12/An=8/E=4 — heavy apply/analyze per generate rules. Includes 6 dedicated compare items,
  5 differential mcq vignettes, per-family "stuck/better" items, and 2 stance/integrative evaluate items.
- Build: items/build/items.json rebuilt — 53 items total (17+36), validated clean by build_items.py.
- Bookkeeping: index.md, coverage.md, course-map.md (status ☐→☑) updated.
- Deferred (noted in coverage.md): separate person-* pages (figures covered inline); theory-cbt links
  forward to pending unit09-modalities — fix that target when Unit 9 is built.

## [2026-06-27] scheduler-upgrade | apps/scheduler.py | Leitner → SM-2
- Replaced the box-based Leitner engine with SM-2 (per-item easiness factor + adaptive interval),
  per learning-science-for-self-study.md "Option B". Public scheduler interface unchanged
  (load/ensure/due/update/autograde/log_attempt), so quiz_runner needed only its log-dict updated.
- Self-grades → SM-2 quality q: missed→2 (relearn from interval 1), shaky→3 (requeue at ½ interval,
  no rep advance), correct→5 (interval ×ease). Ease floored at 1.3, starts 2.5.
- Migration: ensure_state() converts legacy {box,…} records to {ease,interval,reps,…} on load
  (box cadence → interval, ease=2.5); review_state.json (53 items) migrated, verified no box keys.
- Log schema: box_before/box_after → interval_before/interval_after + ease + reps. A pre-upgrade
  review_log.csv is rotated to review_log.leitner.csv on first SM-2 write (one-time, automatic).
- Verified: `python apps/scheduler.py` summary, update() transitions, and log rotation all pass.
