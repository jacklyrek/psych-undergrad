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

## [2026-07-17] create-chapter | Unit 5 Human Development Across the Lifespan | 11 sources, 7 readings, 45 items
- Depth: **in-depth** (matches Units 2–4; course-map entry was rich, so no outline-confirmation pause).
  Tier 2 clinical foundation. CACREP: Human Growth & Development. Emphasis (per syllabus/course-map):
  **attachment as the centerpiece** ("the single most clinically useful developmental idea"),
  typical-vs-clinical discrimination, and the **attachment ↔ alliance** thread (Unit 5 ↔ Unit 1).
- Research: triangulated across peer-reviewed clinical refs + primaries — StatPearls Erikson [S1] and
  Cognitive Development/Piaget [S2]; *Development and Psychopathology* attachment review PMC4085672
  [S3] (secure base/script, transmission gap, risk-not-destiny, therapist-as-attachment-figure);
  NCBI Bookshelf *Biopsychosocial Model 40 Years On* [S4] + Engel 1977 Science [S5]; van IJzendoorn &
  Kroonenberg 1988 cross-cultural meta-analysis [S6]; Main & Solomon disorganized + disorganized-risk
  meta-analyses [S7]; adult attachment — Hazan & Shaver / Bartholomew & Horowitz / AAI [S8];
  orientation-tier Simply Psychology (Ainsworth Strange Situation, caregiving correlates, sensitivity
  critiques) [S9] and Bowlby phases/monotropy [S10]; AAP developmental surveillance [S11]. Engel full
  text and the 1992-primaries were corroborated via secondary/open sources, flagged.
- Readings (7): unit05-development (hub — four frameworks, why attachment leads, risk-not-destiny w/
  equifinality/multifinality, typical-vs-clinical, practice rep), theory-attachment (Bowlby system +
  Ainsworth Strange Situation + adult attachment + the therapy-room handoff), concept-attachment-
  styles (four styles side-by-side, deactivation/hyperactivation, disorganized-as-risk),
  theory-eriksons-stages (8 stages/virtues, the two confusable pairs, clinical use), theory-piaget
  (4 stages, schema/assim/accom, critiques incl. Vygotsky), concept-biopsychosocial-model (Engel,
  systems theory, the "slogan" critique), person-bowlby-ainsworth (Bowlby + Ainsworth + Main). All
  cited [S#], interlinked.
- **Page consolidation (noted in coverage.md + course-map):** course-map promised 10 pages incl. four
  per-style pages + a lone person page; built as **7** — four attachment styles folded into one
  `concept-attachment-styles` (confusable set taught side-by-side, à la Unit 1 core-conditions), and
  Bowlby/Ainsworth/**Main** on one person page. Per-style topic tags preserve discrimination.
- **Cluster added beyond course-map:** `piaget-stages` (noted in course-map + coverage). Attachment
  theory/mechanism items (7), biopsychosocial (3), and typical-vs-clinical/rep (4) intentionally
  unclustered.
- Cross-unit: wired the **Unit 5 ↔ Unit 1** back-link — `concept-therapeutic-alliance` now
  forward-links to `theory-attachment`/`concept-attachment-styles` (source_units → [1,3,5,7]).
- Tensions flagged (per rules): maternal-sensitivity r≈.24 + transmission gap (temperament rival);
  Strange Situation as possible imposed etic (cross-cultural); Erikson/Piaget as heuristics not laws
  (ages approximate, culturally situated; Vygotsky critique); biopsychosocial "vague slogan" critique;
  disorganized attachment = transdiagnostic **risk, not destiny** (kept clinical/non-deterministic).
- Items: 45 across 4 clusters (`attachment-styles` 12, `erikson-stages` 9, `piaget-stages` 7,
  `developmental-theorists` 3; 14 unclustered). Bloom R=7/U=9/Ap=12/An=9/E=8; types: 12 explain,
  10 mcq (which-style/stage/theorist vignettes), 9 recall, 5 compare (≥1 per cluster), 5 vignette,
  4 cloze. Stance probes: don't-type-the-client, over-pathologizing normal development, secure-base
  moves with preoccupied/dismissing clients; + the syllabus practice rep (own attachment history +
  Erikson stage) as a production item.
- Build: items/build/items.json rebuilt — 263 items total (17+36+51+48+45+31+35 aux), validated clean.
- Bookkeeping: index.md, coverage.md (row + 7 hole/consolidation notes), course-map.md (☐→☑,
  cluster + pages + built line), log.md updated.
- Deferred: Unit 6/7/11 forward-references are by name (pending units) — wire to wikilinks at those
  builds. Tier 2 now 1 of 4 built (Unit 5 ☑).

## [2026-07-16] create-module | aux-addiction (Understanding & Changing Addictive Behavior) | 16 sources, 6 readings, 35 items
- Second elective module (after PFA). Off-spine `aux-` namespace; borders **Unit 6** (SUD as a
  diagnostic category) and **Unit 9** (MI/CBT modalities). Built on request: *addictions and how to
  break them.* Frontmatter: `track: elective`, `module: addiction`, `spine: false`,
  `related_units: [6, 9]`. Item id prefix `ax-add-`.
- Research (heavy/clinical + partly contested — kept precise): NIDA *Drug Misuse and Addiction* [S1],
  *Treatment and Recovery* [S2, 40–60% relapse ≈ chronic disease], DrugFacts [S3]; Koob & Volkow
  *Lancet Psychiatry* three-stage cycle [S4]; DSM-5-TR SUD 11 criteria/4 groups/severity via SAMHSA-
  NCBI [S5]; Prochaska & DiClemente TTM [S6]; Marlatt/NIAAA relapse-prevention overview [S7];
  SAMHSA TIP 35 MI [S8]; NIDA MOUD (methadone/bup reduce mortality, not naltrexone) [S9]; Kelly 2020
  Cochrane AA/TSF [S10]; contingency management gold-standard for stimulants + harm-reduction tension
  [S11]; gambling as sole behavioral addiction / Potenza [S12]; brain-disease-vs-learning debate
  (Lewis; "neither brain disease nor moral failing") [S13]; SMART Recovery [S14]; Surgeon General
  *Facing Addiction* [S15]; APA SUD/IGD [S16].
- Readings: aux-addiction (hub), concept-addiction-models (SUD dx + tolerance/withdrawal/craving +
  gambling + 3 models), concept-neuroscience-of-addiction (dopamine, cue reactivity, 3-stage cycle,
  pos→neg reinforcement), concept-stages-of-change (TTM, spiral, stage-matching), concept-relapse-
  prevention (Marlatt, HRS, lapse vs relapse, AVE, urge surfing), concept-treatment-and-recovery
  (MI/CBT/CM/MOUD/mutual-help/harm-reduction). All cited [S#], interlinked, forward-linked to pending
  Units 6/8/9.
- Tensions flagged (per rules): brain-disease model is contested (learning/choice alternatives);
  harm reduction vs. abstinence held as integrated not opposed; only gambling is a DSM behavioral
  addiction (IGD = Section III); MOUD ≠ "swapping addictions"; physical dependence ≠ addiction
  (prescribed-medication carve-out).
- Items: 35 across 4 clusters (`addiction-models` 8, `change-stages` 8, `relapse-concepts` 9,
  `addiction-treatments` 10); Bloom R=6/U=9/Ap=7/An=9/E=4. 5 compare items (one per major confusable:
  models, stage-matching, lapse-vs-relapse, harm-reduction, AA-vs-SMART), 4 discrimination mcqs
  (behavioral addiction, precontemplation move, stimulant tx, which MOUD reduce mortality), and
  several stance drills (righting reflex, relapse≠failure, MOUD stigma).
- Bookkeeping: index.md + coverage.md updated (elective sections); log appended; items.json rebuilt
  (218 items total). Handoff hole logged: forward-links to Units 6/8/9 are by name (pending units) —
  rewire to real wikilinks and reconcile SUD-criteria / MI-CBT overlap when those units are built.

## [2026-07-17] create-chapter | Unit 6 Psychopathology & the DSM-5-TR | 23 sources, 12 readings, 75 items
- Depth: **in-depth** (the syllabus's biggest unit — 2 weeks at suggested pace; course-map entry was
  rich, no outline-confirmation pause). Tier 2. CACREP: ties into Assessment & Diagnosis. Emphasis
  (per syllabus/course-map): **diagnosis as shorthand, not verdict**; heavy **differential-vignette**
  discrimination; the criteria-cold practice rep (MDD/GAD/PTSD in 2 minutes) as the
  over-pathologizing antidote.
- Research: anchored on peer-reviewed clinical references — StatPearls for every category (MDD
  NBK559078 [S5], Bipolar [S6], GAD [S7], Panic [S8], PTSD [S9], Schizophrenia [S10], Personality
  [S11], OCD [S12], Anorexia [S13], ADHD [S14], ASD [S15]) + First et al. 2022 *World Psychiatry*
  DSM-5-TR overview by the manual's editors [S2]; triangulated with OpenStax §15.2 [S1], Kress/TPC
  multiaxial-removal counselor implications [S3], NCBI DSM-IV→5 overview [S4], SAMHSA SUD table
  (shared with aux-addiction) [S16], Kessler NCS-R comorbidity [S17], HiTOP consortium [S18], Caspi
  & Moffitt p factor [S19], NIMH RDoC [S20], Frances diagnostic inflation [S21], Pies bereavement
  exclusion [S22], SAMHSA TIP 59 cultural formulation [S23]. psychiatry.org 403'd — TR facts cited
  via First et al.; criteria-are-paraphrases caveat flagged in sources file + hub.
- Readings (12): unit06-psychopathology (hub — what "disorder" is, impairment clause, comorbidity
  norm, person-first, insurance reality, practice rep), concept-dsm-structure (history, lifespan
  order, multiaxial removal, other-specified/unspecified, ICD/billing, CFI + cultural concepts),
  concept-mood-disorders, concept-anxiety-disorders, concept-trauma-stressor-disorders (incl. PGD),
  concept-ocd, concept-psychotic-disorders, concept-personality-disorders,
  concept-substance-use-disorders (concise, defers to aux-addiction),
  concept-neurodevelopmental-disorders, concept-eating-disorders,
  concept-categorical-vs-dimensional (absorbs comorbidity). All cited [S#], interlinked.
- **Page plan deviations (noted in coverage + course-map):** concept-comorbidity folded into
  concept-categorical-vs-dimensional; concept-neurodevelopmental-disorders +
  concept-eating-disorders added beyond the course-map list (syllabus categories it had skipped).
- **Clusters added beyond course-map:** `psychotic-spectrum`, `eating-disorders` (alongside
  mood/anxiety/trauma/personality/differential-vignettes). 25 items intentionally unclustered
  (manual, OCD, SUD, neurodevelopmental, categorical-dimensional topics).
- Cross-unit wiring done: aux-addiction hub + concept-addiction-models "Unit 6 (planned)" → real
  wikilinks (SUD overlap reconciled: module keeps the criteria deep-dive);
  unit05-development (both mentions) → [[unit06-psychopathology]]; concept-acculturation →
  concept-dsm-structure (CFI); PFA concept-grief-models PGD → concept-trauma-stressor-disorders.
- Tensions flagged (per rules): categorical system's four cracks (field-trial reliability,
  comorbidity 45%, heterogeneity, continuity) vs. its clinical utility; HiTOP/p-factor/RDoC as
  serious-but-not-clinic-ready (RDoC explicitly not diagnostic); Frances inflation vs.
  early-intervention defense; bereavement exclusion + PGD as the medicalizing-grief emblem;
  Criterion A as drawn line; neurodiversity vs. deficit framing; prevalence figures as
  order-of-magnitude.
- Items: 75 across 7 clusters (differential-vignettes 10 — the cross-category interleaving target,
  mood 8, trauma 8, anxiety 7, psychotic 6, personality 6, eating 5; 25 unclustered). Bloom
  R=20/U=10/Ap=18/An=19/E=8; types: 20 mcq (discrimination vignettes — deliberately high per the
  "heavy vignette unit" note), 18 explain, 15 recall, 11 cloze, 8 compare (≥1 per cluster), 3
  vignette. Stance probes: over-pathologizing grief, reassurance traps (anxiety + OCD),
  person-first, delusion don't-argue-don't-collude, PD stigma discipline, disclosure-pushing,
  eating-disorder screening, diagnostic inflation. The three 2-minute production reps included.
- Build: items/build/items.json rebuilt — **338 items** total (17+36+51+48+45+75 spine + 31+35 aux),
  validated clean by build_items.py.
- Bookkeeping: index.md (full Unit 6 entry), coverage.md (row + 8 new notes), course-map.md (☐→☑,
  clusters + pages + built line), log.md updated.
- Deferred: Unit 7/8/9/11 forward-references by name (pending units) — wire at those builds; Unit 8
  build should reconcile PTSD-criteria/trauma-informed-care split + suicidal-behavior codes. Tier 2
  now 2 of 4 built (Units 5–6 ☑).

## [2026-07-17] create-chapter | Unit 7 Assessment, Diagnosis & Case Conceptualization | 14 sources, 7 readings, 51 items
- Depth: **in-depth** (matching Units 2–6). Tier 2. CACREP: Assessment & Testing. Emphasis (per
  syllabus/course-map): the arc **intake → MSE/screens → formulation → plan**; the load-bearing
  stance **a screen is not a diagnosis**; diagnosis (*what*) vs. case conceptualization (*how/why*)
  as the unit's spine; the syllabus production rep (a one-page conceptualization of a character).
- Research: anchored on peer-reviewed clinical references — StatPearls MSE [S1] + diagnostic-accuracy
  (sensitivity/specificity/PPV) [S9]; the IOM/National Academies psychological-testing report for
  reliability/validity/standardization [S5]; the instrument-validation primaries Kroenke 2001 PHQ-9
  [S2] and Spitzer 2006 GAD-7 [S3] (+ Rutter & Brown 2017 psychometric replication [S10]); the anchor
  author Sommers-Flanagan on the clinical interview [S7]; the peer-reviewed counseling journal (TPC)
  Five Ps framework [S4]; PsychDB 4Ps×BPS grid [S8]; Fortney 2017 measurement-based care [S12]; APA
  PHQ page [S6]; Doran 1981 SMART origin [S13]; OER psychometrics [S11]; golden-thread practitioner
  refs [S14]. Two sources 403'd to automated fetch (Psychiatric Services MBC PDF [S12], OER
  reliability chapter [S11]) — cited via abstract/search-indexed summaries **plus a corroborating
  source**, flagged in the sources file.
- Readings (7): unit07-assessment (hub), concept-intake-interview, concept-mental-status-exam
  (cluster mse-domains), concept-screening-tools (cluster screening-tools — PHQ-9 + GAD-7 together),
  concept-reliability-validity (cluster reliability-vs-validity), concept-case-conceptualization
  (cluster formulation-ps), concept-treatment-planning. All cited [S#], interlinked, each with a
  ## Sources section.
- **Page plan deviation (noted in coverage + course-map):** the course-map's separate
  `concept-phq9` + `concept-gad7` consolidated into one `concept-screening-tools` (confusable set
  taught side-by-side, same rationale as Unit 5 attachment-styles / Unit 6 consolidations) → **7
  pages, not 8**.
- **Cluster added beyond course-map:** `formulation-ps` (the Five Ps), alongside the promised
  `mse-domains`, `screening-tools`, `reliability-vs-validity`. Intake (6) + treatment-planning (6)
  items intentionally unclustered.
- Cross-unit wiring done (earlier by-name handoffs made live): concept-dsm-structure,
  unit06-psychopathology (both mentions + related-pages bullet), concept-categorical-vs-dimensional,
  concept-substance-use-disorders → Unit 7 pages (Unit 6); concept-biopsychosocial-model (body +
  "Connects to") → concept-intake-interview/unit07-assessment (Unit 5); unit04-multicultural +
  concept-acculturation → concept-reliability-validity/screening-tools (Unit 4); unit02-theories
  (theory→formulation) → concept-case-conceptualization (Unit 2); concept-therapeutic-alliance
  forward link made live (Unit 1 — source_units [1,3,5,7] verified).
- Tensions flagged (per rules): a screen is not a diagnosis and cut-points are population-dependent
  (≥8 vs. ≥10) [S2][S3][S9][S10]; reliability ≠ validity and neither licenses use outside the norming
  population (the culture-fair worry from Unit 4) [S5][S11]; diagnosis-vs-formulation as the unit's
  spine [S4][S8]; the MSE is a subjective snapshot that only supports (never makes) a diagnosis [S1];
  "measurable" can crowd out "meaningful" (SMART/MBC serve the work, not the reverse) [S12][S13][S14];
  golden thread labeled a documentation/compliance convention, not a scientific finding.
- Items: 51 across 4 clusters (mse-domains 10, screening-tools 9, reliability-vs-validity 10,
  formulation-ps 10) + unclustered intake (6) and treatment-planning (6). Bloom
  R=15/U=12/Ap=10/An=7/E=7 (apply/analyze/evaluate = 24); types: 12 explain, 10 recall, 9 mcq
  (confusable-pair discriminations: mood/affect, process/content, insight/judgment, which-anxiety,
  classify-the-P, SMART-objective), 9 cloze, 7 compare (5 clustered — ≥1 per cluster — + 2
  unclustered), 4 vignette. Stance probes: interrogation-drift, I-need-all-the-data,
  describe-don't-interpret, screen-is-not-a-diagnosis, formulate-with-not-about, measurable≠meaningful.
  Syllabus production rep included (u7-formulation-rep-01, a recall-type item).
- Build: items/build/items.json rebuilt — **389 items** total (17+36+51+48+45+75+51 spine + 31+35
  aux), validated clean by build_items.py.
- Bookkeeping: index.md (full Unit 7 entry), coverage.md (row 7 ☐→☑ + 6 new notes + 3 resolved-
  handoff updates), course-map.md (☐→☑, clusters + pages + built line), log.md updated.
- Deferred: Unit 8 (item-9 → suicide-risk protocol, C-SSRS, PC-PTSD-5) and Unit 12 (MBC as outcome
  monitoring / program evaluation; concept-reliability-validity carries source_units [7,12])
  forward-referenced by name — wire at those builds. Tier 2 now **3 of 4 built (Units 5–7 ☑)**;
  only Unit 8 remains in Tier 2.

## [2026-07-18] create-chapter | Unit 8 Crisis, Risk Assessment & Trauma-Informed Care | 21 sources, 9 readings, 67 items
- Depth: **in-depth** (course-map entry was rich → no outline-confirmation pause). Tier 2, and one of
  the syllabus's "if only a month, do Units 1, 3, 8." CACREP: Helping Relationships & crisis
  competencies. **Heavy/high-stakes topic — kept clinical and precise, no sensationalism** (per
  CLAUDE.md). Emphasis (per syllabus/course-map): the two opposite reflexes the unit corrects —
  **lean in on danger** (ask about suicide directly; freezing is not an option) and **hold back on
  trauma** (don't dig / don't re-traumatize) — with **safety as the continuous through-line**.
- Research: anchored where possible on **primary instruments/validations and government/professional
  bodies** — Columbia C-SSRS + Posner 2011 [S1]; Shea CASE approach [S2]; VA Suicide Risk Assessment
  Guide (IS PATH WARM, acute/chronic, stratification) [S3]; Dazzi 2014 (asking doesn't plant the idea)
  [S4]; Klonsky & May 3ST + Joiner IPTS (ideation-to-action) [S5]; Stanley & Brown SPI [S6] + Stanley
  2018 JAMA Psychiatry (~45% reduction) & Rudd no-suicide-contract critique [S7]; Harvard Means Matter
  [S8]; James & Gilliland six-step [S9] + Roberts seven-stage [S10]; Richmond 2012 Project BETA
  de-escalation (PMC3298202) [S11]; SAMHSA 2014 trauma-informed framework — 3 Es/4 Rs/6 principles [S12];
  APA + VA/DoD PTSD guidelines (PE/CPT/TF-CBT/EMDR) [S13]; HPA-axis review PMC9120425 [S14, **read in
  full via pypdf**]; Simply Psychology neurobiology (orientation) [S15]; Siegel window of tolerance [S16];
  van der Kolk *Body Keeps the Score* (popular-press, flagged) [S17]; McCann & Pearlman 1990 (VT/CSDT)
  [S18]; Trippany/Kress/Wilcoxon 2004 *JCD* [S19, **read in full via pypdf**]; Figley/Stamm ProQOL [S20];
  ACA Code C.2.g [S21]. Two anchor books (James & Gilliland; Herman) offline → reputable secondary; SAMHSA
  wording confirmed across two secondaries + the primary publication record.
- Readings (9, full course-map list — no consolidation): unit08-crisis-trauma (hub), concept-suicide-
  risk-assessment, concept-safety-planning, concept-means-reduction, concept-de-escalation,
  concept-neurobiology-of-trauma (`source_units: [8, 11]`), concept-trauma-informed-care,
  concept-vicarious-trauma, concept-counselor-self-care. All cited [S#], interlinked, each with a
  ## Sources section.
- **Clusters added beyond course-map (noted in course-map + coverage):** the course-map named
  `crisis-response-models` + `trauma-informed-vs-treatment`; added `suicide-risk-concepts`,
  `trauma-brain`, and `counselor-distress-types` (the last a prime interleaving set:
  VT/STS/compassion-fatigue/burnout/countertransference).
- **Cross-unit wiring done — all by-name "Unit 8" refs → live wikilinks (40 replacements, 22 files):**
  Unit 3 (concept-duty-to-warn, concept-confidentiality-limits, study-tarasoff, concept-scope-of-
  practice, concept-mandated-reporting, hub); Unit 6 (concept-trauma-stressor-disorders [neurobiology/
  treatment/don't-retraumatize + suicidal-behavior codes reconciled], concept-dsm-structure,
  concept-mood-disorders, concept-psychotic-disorders, concept-ocd, hub); Unit 7 (unit07-assessment,
  concept-screening-tools [item-9 trip-wire, PC-PTSD-5, C-SSRS], concept-intake-interview); PFA elective
  (hub, concept-grief-models, concept-supporting-the-bereaved, concept-death-notification); addiction
  elective (hub, concept-treatment-and-recovery); theory-postmodern. No unit08-* by-name refs remain.
- Tensions flagged (per rules, quizzed at evaluate level): individual suicide is **not predictable**
  (the Tarasoff prediction critique — assess to MANAGE, not prophesy); **no-suicide contracts not
  evidence-based**; means-restriction works despite the substitution objection; trauma **cortisol
  findings inconsistent** (no clean biomarker); window of tolerance + polyvagal theory are **heuristics**;
  **van der Kolk popular-press** (mechanisms corroborated vs. S14/S15; memory-as-storage & recovered-
  memory claims flagged); trauma-**informed** (avoid harm, no disclosure required) ≠ trauma **treatment**;
  the counselor-cost terms overlap; self-care is an **ethical duty (C.2.g)** and prevention is
  **organizational**, not only personal.
- Items: 67 across 5 clusters (crisis-response-models 20, suicide-risk-concepts 15, counselor-distress-
  types 13, trauma-brain 10, trauma-informed-vs-treatment 9). Bloom R=16/U=11/Ap=17/An=13/E=10 (apply/
  analyze/evaluate = 40); types: 16 explain, 14 mcq, 12 recall, 10 cloze, 8 compare (≥1 per cluster),
  7 vignette. Includes the syllabus practice rep (memorized ideation-asking structure, u8-sra-rep-01)
  and stance probes throughout (ask-directly, assess-to-manage-not-predict, safety-plan-not-contract,
  don't-dig, freeze-is-not-a-choice, martyr-reflex).
- Build: items/build/items.json rebuilt — **456 items** total (17+36+51+48+45+75+51+67 spine + 31+35
  aux), validated clean by build_items.py.
- Bookkeeping: index.md (full Unit 8 entry), coverage.md (row 8 ☐→☑ + 6 new notes + 2 resolved-handoff
  markers), course-map.md (☐→☑, clusters + pages + built line), log.md updated.
- **Tier 2 now COMPLETE (Units 5–8 ☑); Tier 1 + Tier 2 done (Units 1–8).** Remaining: Tier 3
  (Units 9–12). Note: van der Kolk / Herman anchor books were offline — neurobiology corroborated
  against peer-reviewed sources as required.

## [2026-07-19] lint | fill known compare-coverage holes | +3 items (Unit 1 ×2, PFA elective ×1)
- Filled the three actionable "Known holes" from coverage.md — each a cluster that had analyze/
  evaluate items but no dedicated `compare`-type item (all flagged "add on a later lint/generate pass").
- **Unit 1:** `u1-alliance-compare-01` (`alliance-components`, analyze) — Bordin bond/goal/task paired
  with the distinct rupture each signals + why "more rapport" is the wrong fix for goal/task ruptures;
  `u1-commonfactors-compare-01` (`common-factors`, analyze) — common-factors/contextual (Wampold) vs.
  specific-ingredients/medical model, evidence each leans on, interdependence synthesis. Unit 1 now
  17→**19 items**, 3/4 clusters with a dedicated compare (rogers-conditions covered by the empathy
  analyze item).
- **PFA elective:** `ax-pfa-frameworks-compare-01` (`pfa-frameworks`, analyze) — WHO Look/Listen/Link
  vs. NCTSN 8 Core Actions (audience, the 1–3 / 4 / 5–8 mapping, two-slicings-of-one-logic). Module
  31→**32 items**, all 3 clusters now have a compare.
- Sourced from existing readings only (no new research): concept-therapeutic-alliance, theory-common-
  factors, concept-pfa-core-actions. Build clean — **459 items** total; Bloom analyze 93→96.
- **Bookkeeping-only resolutions (no content change):** marked the **Unit 3 → Unit 8 handoff** hole
  RESOLVED — verified every Unit-8 ref in the Unit 3 pages is already a live wikilink (wired in the
  2026-07-18 Unit 8 build), so the stale "pending Unit 8" bullet was struck through.
- Remaining "Known holes" are all either deliberate design decisions (page/cluster consolidations,
  contested-material load), permanent sourcing caveats, or forward-handoffs to **unbuilt** Units 9/11/12
  — none fillable until those units exist.
