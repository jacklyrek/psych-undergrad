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

## [2026-06-28] create-module | aux-psychological-first-aid (PFA & Acute Grief) | 15 sources, 4 readings, 23 items
- **New schema feature (per user):** off-syllabus topics now built as **elective modules** in the
  `aux-` namespace, documented in a new "Ad-hoc / elective modules" section of CLAUDE.md. Reuses all
  unit machinery (citations, Bloom-spanning, clusters, build/scheduler) but lives outside the 12-unit
  spine and cross-links into it. Decisions confirmed with user: aux- prefix (not unit13/high-numbers/
  subfolder), broad PFA framing (child-death grief as the anchor case), codify the convention now.
- Frontmatter convention for electives: `track: elective`, `module: <slug>`, `spine: false`,
  `related_units: [N]`. Item id prefix `ax-<slug>-`. Bookkeeping under a separate "Elective / ad-hoc
  modules" heading in index.md + coverage.md (kept out of the numbered-unit build table).
- **Build change:** `apps/build_items.py` glob widened `unit*.md` → `*.md` (minus README.md) so
  `aux-*.md` item files compile automatically. Verified clean.
- Research (heavy/clinical topic — kept precise): triangulated WHO PFA Guide for Field Workers [S1],
  NCTSN/NCPTSD Field Operations Guide [S2], VA National Center for PTSD [S3]; Cochrane debriefing
  review [S4] + NICE [S5] (debriefing ineffective/possibly harmful — the key negative); grief models
  PMC5033290 [S6], Stroebe & Schut dual process [S7], Worden tasks [S8], Kübler-Ross critical
  appraisal PMC8675126 [S9]; PGD validation Prigerson/World Psychiatry [S10], predictors PMC9131400
  [S11] (child loss = top risk), DSM-5-TR thresholds [S12]; practical support Ring Theory [S13],
  Nationwide Children's [S14], Children's Hospital Colorado [S15].
- Readings: aux-psychological-first-aid (hub), concept-pfa-core-actions, concept-grief-models,
  concept-supporting-the-bereaved. All cited [S#], interlinked, forward-linked to pending Unit 8.
- Tensions flagged: stages-of-grief retired as a clinical map; PFA evidence-INFORMED not -proven;
  normal acute grief must not be pathologized vs. the real PGD time/impairment threshold.
- Items: 23 across 3 clusters; Bloom spread R=5/U=4/Ap=5/An=5/E=4. Includes 1 compare + a PGD-risk
  differential mcq + several stance/restraint drills ("don't probe," "don't fix," "say the name").
- Bookkeeping: index.md + coverage.md (new elective sections + handoff holes) updated; items.json
  rebuilt. Handoff hole logged: rewire forward-links to real wikilinks when Unit 8 is built.

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

## [2026-07-06] create-chapter | Unit 3 Ethics, Law & Professional Identity | 12 sources, 9 readings, 51 items
- Depth: in-depth (high-stakes unit; syllabus: "a mistake can end a career"). Scope from course-map
  (entry was rich — no outline-confirmation pause needed). CACREP: Professional Orientation & Ethics.
- Research: **anchored on the primary document** — fetched the official 2014 ACA Code of Ethics PDF
  (counseling.org), extracted full text via pypdf (installed this pass), quoted standards verbatim
  [S1]. Triangulated with *Jaffee v. Redmond* opinion text (Cornell LII) [S2], StatPearls Duty to
  Warn NBK542236 [S3], Darby & Weinstock 2018 PMC [S4], APA Services mandatory-reporting [S5] +
  prescribing-psychologists [S8] (dated — CO/UT additions flagged), Child Welfare Info Gateway [S6],
  APA professions page [S7], UMN open textbook [S9], Northwestern .edu [S10], SAP Div-29 boundaries
  [S11], Zur Institute (orientation) [S12].
- Readings: unit03-ethics-law (hub: nine sections, 5 values + 6 principles, legal-vs-ethical),
  concept-informed-consent, concept-confidentiality-limits (incl. the **confidentiality-speech
  worked model** — the syllabus practice rep), concept-duty-to-warn, study-tarasoff,
  concept-mandated-reporting, concept-dual-relationships, concept-scope-of-practice,
  concept-helping-professions-compared. All cited [S#], interlinked; worked dialogue contrasts on
  consent, threat response, reporting-while-preserving-alliance, and small-town boundaries (per
  standing user preference for dialogue examples).
- Tensions flagged: duty-to-warn is a 50-state patchwork (mandatory/permissive/silent);
  Tarasoff assumes violence prediction the science lacks; how-much-consent-up-front debate
  (retention research); RxP state count moving target; ACA 5-yr vs APA 2-yr post-termination rule.
- Items: 51 across 5 clusters (`confidentiality-exceptions` 16 — main interleaving target,
  `duty-concepts` 10, `ethics-principles` 5, `boundary-concepts` 5, `the-helping-professions` 5,
  10 unclustered consent/competence). Bloom R=16/U=7/Ap=14/An=11/E=3; types: 11 vignette, 11 recall,
  9 compare, 7 cloze, 7 explain, 6 mcq. Stance probes: threat minimizing, report-vs-alliance,
  values-referral, impairment-as-selfishness framing.
- Clusters added beyond course-map (noted there + coverage.md): `ethics-principles`,
  `boundary-concepts`.
- Build: items/build/items.json rebuilt — 127 items total (17+36+51+23 aux), validated clean.
- Bookkeeping: index.md, coverage.md (row + 4 new hole notes incl. Unit 8 handoff), course-map.md
  (☐→☑, cluster + pages lines) updated.
- Deferred: Unit 8 forward-references are by name (no unit08 page yet) — wire to wikilinks at Unit 8
  build, together with the PFA-module handoff.

## [2026-07-06] create-chapter | Unit 4 Multicultural & Social-Justice Competence | 16 sources, 7 readings, 48 items
- Emphasis: the three-framework arc (tripartite 1992 → cultural humility 1998 → MSJCC 2015) as a
  conversation, stance-heavy (this unit's content IS stance), contested material surfaced rather
  than smoothed. Depth: in-depth.
- Research: anchored on the profession's framework documents — MSJCC official PDF + the authors'
  Counseling Today companion [S1][S2], Sue/Arredondo/McDavis 1992 [S3] — triangulated with the
  primary concept articles (Tervalon & Murray-García [S4], McIntosh [S5], Sue 2007 microaggressions
  [S6], Berry 1997 [S7], Day-Vines broaching [S10]), outcome research (Hook 2013 [S8], Tao 2015
  meta-analysis [S9]), critiques (Lilienfeld 2017 [S12], SAP MCC-measurement review [S11]), and
  disparities data (NIMHD/PMC [S15]). Paywalled primaries (Wiley: S3, S7) corroborated via
  abstracts + multiple secondaries, flagged in sources file.
- Readings: unit04-multicultural (hub), theory-tripartite-model, concept-msjcc,
  concept-cultural-humility, concept-acculturation (incl. worldview + help-seeking norms),
  concept-privilege-power (incl. broaching), concept-microaggressions (split out beyond course-map's
  six pages — one concept per page). All cited [S#], interlinked; worked dialogue contrasts on
  one-client-three-failures (tripartite), knowledge-as-hypothesis vs stereotype-with-good-intentions
  (humility), help-seeking "resistance" reframe, congruent broaching, and microaggression repair
  (per standing user preference for dialogue examples).
- Tensions flagged: competence-vs-humility framing debate; self-report MCC invalid after social-
  desirability control (Constantine & Ladany) while client-perception predicts (Tao r≈.29, Hook);
  Lilienfeld-vs-Sue microaggression dispute (Sue conceded points; Williams 2019 replied); Berry's
  boxes static/choice-constrained; MSJCC advocacy-scope boundary questions.
- Items: 48 across 5 clusters (`mc-frameworks` 8, `microaggression-types` 8, `acculturation-
  strategies` 8, `broaching-styles` 6, `mc-competence-dimensions` 6, 12 unclustered privilege/
  help-seeking/mcc-evidence). Bloom R=13/U=8/Ap=11/An=8/E=8; types: 13 recall, 9 mcq
  (discrimination tasks), 8 explain, 6 vignette, 6 compare, 6 cloze, incl. 2 production reps
  (congruent broach; cultural-autobiography slice — the syllabus practice rep). Stance probes:
  privilege-confession-
  at-client, resistance-reframe, misgendering repair, defensive-apology-as-microinvalidation.
- Clusters added beyond course-map (noted there + coverage.md): `mc-frameworks`,
  `acculturation-strategies`, `microaggression-types`, `broaching-styles`.
- Back-links wired: unit03-ethics-law + concept-scope-of-practice "Unit 4" mentions → real
  [[unit04-multicultural]] wikilinks.
- Build: items/build/items.json rebuilt — 175 items total (17+36+51+48+23 aux), validated clean.
- Bookkeeping: index.md, coverage.md (row + 3 new hole notes), course-map.md (☐→☑, clusters +
  pages + built line) updated.
- Deferred: Unit 6/Unit 7 forward-references by name (culture-bound presentations; culture-fair
  assessment) — wire to wikilinks at those builds. Tier 1 now complete (Units 1–4 ☑).

## [2026-07-08] extend-module | psychological-first-aid | +1 reading, +8 items
- Trigger: user Q&A on PFA stabilization → "what if their kid is dead and they ask where they are?"
  → gap identified: the module started *after* the parent knows. Built the missing page on request.
- New reading: wiki/concept-death-notification.md — the five MADD/DOJ principles (in person, in
  time, in pairs, in plain language, with compassion), GRIEV_ING protocol (Hobgood/ACEP), plain
  "D-words" over euphemisms, the three "where is she?" scenarios (confirmed / unknown / re-asking)
  with worked scripts + instinct-vs-practice table, viewing-the-body evidence (Chapple & Ziebland
  BMJ 2010: offered prepared choice, don't assume harm).
- Sources: S16–S20 added to research/aux-psychological-first-aid-sources.md (Hobgood 2005 AEM, ACEP
  trainer manual, MADD/DOJ curriculum, Chapple & Ziebland BMJ, McCarroll 2024 review
  [orientation only — paywalled]); S2 (NCTSN guide) noted for its notification/missing-person/
  body-identification sections.
- Items: 8 new (ax-pfa-notify-*) in cluster `bereavement-support`, remember→evaluate, incl. a
  three-scenario compare and an unconfirmed-missing mcq. Module now 31 items.
- Cross-links: hub map (+entry #3), concept-pfa-core-actions (Core Action 2 line),
  concept-supporting-the-bereaved ("starts after the parent knows" pointer).
- Bookkeeping: index.md + coverage.md updated (bereavement-support now has a compare;
  pfa-frameworks still the only cluster without one). items.json rebuilt.

## [2026-07-13] maintenance | all units | removed CS-background framing from CLAUDE.md, course-map, learning-science doc, 8 wiki pages, and 2 item files (per human request: not a typical CS profile); rebuilt items.json (183 items)
