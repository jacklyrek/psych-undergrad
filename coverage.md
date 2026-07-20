# Coverage map

What's built vs. pending, and where the readings and practice have holes. Updated by `lint` and
`create chapter`. The Bloom/item columns fill in as units are created.

## Build status

| Unit | Tier | Readings | Items | Bloom spread | Clusters w/ compare items |
|---|---|---|---|---|---|
| 1 Helping Skills | 1 | ☑ (10) | ☑ (38) | all 5 levels | 4/4 ✓ (5 compares) |
| 2 Theories | 1 | ☑ (7) | ☑ (36) | all 5 levels | theory-families ✓ (6 compares) |
| 3 Ethics & Law | 1 | ☑ (9) | ☑ (51) | all 5 levels | 5/5 ✓ (9 compares) |
| 4 Multicultural | 1 | ☑ (7) | ☑ (48) | all 5 levels | 5/5 ✓ (6 compares) |
| 5 Development | 2 | ☑ (7) | ☑ (45) | all 5 levels | 4/4 ✓ (5 compares) |
| 6 Psychopathology | 2 | ☑ (12) | ☑ (75) | all 5 levels | 7/7 ✓ (8 compares) |
| 7 Assessment | 2 | ☑ (7) | ☑ (51) | all 5 levels | 4/4 ✓ (`mse-domains`, `screening-tools`, `reliability-vs-validity`, `formulation-ps` — 5 compares) |
| 8 Crisis & Trauma | 2 | ☑ (9) | ☑ (67) | all 5 levels | 5/5 ✓ (8 compares) |
| 9 Modalities | 3 | ☑ (9) | ☑ (57) | all 5 levels | 6/6 ✓ (7 compares) |
| 10 Group | 3 | ☑ (7) | ☑ (57) | all 5 levels | 6/6 ✓ (7 compares) |
| 11 Neuroscience | 3 | ☐ | ☐ | — | — |
| 12 Research | 3 | ☐ | ☐ | — | — |

☐ pending · ◐ partial · ☑ complete

## Elective / ad-hoc modules (off-spine)

Built in the `aux-` namespace; not part of the 12-unit count. Same coverage rules apply.

| Module | Borders | Readings | Items | Bloom spread | Clusters w/ compare items |
|---|---|---|---|---|---|
| PFA & Acute Grief Support (`aux-psychological-first-aid`) | Unit 8 | ☑ (5) | ☑ (32) | all 5 levels | 3/3 ✓ (`pfa-frameworks`, `grief-models`, `bereavement-support` each have a compare) |
| Understanding & Changing Addictive Behavior (`aux-addiction`) | Units 6, 9 | ☑ (6) | ☑ (35) | all 5 levels | 4/4 ✓ (`addiction-models`, `change-stages`, `relapse-concepts`, `addiction-treatments` each have a compare) |

## Coverage rules the lint pass enforces
- Every major concept has at least one **Apply** or **Analyze** item, not only "define"-level.
- Every confusable `cluster` (see course-map) has at least one **compare** item.
- Every item's `source_page` still exists and hasn't materially changed since the item was written.
- No orphan readings (a page nothing links to) and no missing concept pages the course-map promised.

## Known holes
- **Unit 1 upgraded concise → in-depth (2026-07-19):** the only spine unit built concise (2026-06-27)
  was brought to the Units 2–8 standard. **5 → 10 readings, 19 → 38 items, ~9 → 17 sources.** Both
  concise-build shortcuts are now **RESOLVED**:
  - ~~Per-condition pages (separate UPR/empathy/congruence) were folded into `concept-core-conditions`
    for the concise build; split later if item volume grows.~~ **Split done:** built
    `concept-unconditional-positive-regard`, `concept-empathy` (adds Carkhuff's five levels), and
    `concept-congruence` (adds immediacy + self-disclosure), each with real depth.
    `concept-core-conditions` is **retained as an overview/synthesis hub** (holds the six-condition
    model + necessary-vs-sufficient debate + how the three relate) so no inbound wikilink broke.
  - ~~`person-carl-rogers` page deferred (concise build) — folded into `concept-core-conditions`.~~
    **Built:** `person-carl-rogers` (self-theory, actualizing tendency, conditions of worth, the
    Wisconsin project, Gloria films, peace work, critiques).
  - **Added beyond the course-map's eight:** `concept-attending-and-listening` (SOLER, the three Vs,
    use of silence, observation, and the cultural non-universality of attending) — split out per
    one-concept-per-page. Course-map entry updated to match.
- **Unit 1 compare-coverage now 4/4 (2026-07-19):** every cluster has ≥1 dedicated `compare` (5 total)
  — `rogers-conditions` 2 (empathy-vs-sympathy-vs-interpretation; UPR-vs-approval/agreement/liking),
  `microskill-types` 1 (paraphrase-vs-reflection-vs-summarizing), `alliance-components` 1
  (bond/goal/task → rupture patterns), `common-factors` 1 (contextual vs. specific-ingredients model).
  (Corrects an earlier note that miscredited the `microskill-types` compare.)
- **Unit 1 Bloom spread:** R=7/U=8/Ap=9/An=9/E=5 across 38 items — heavy on apply/analyze/evaluate (23)
  per generate rules. Types: 11 explain, 9 vignette, 6 recall, 5 cloze, 5 compare, 2 mcq (reserved for
  the two discrimination tasks: Carkhuff-level and rupture-type). Three items' `source_page` was
  repointed from `concept-core-conditions` to the new split pages (UPR ×2, empathy ×1).
- **Unit 1 contested-material load raised deliberately** and surfaced as items at evaluate level:
  necessary-vs-sufficient (the Wisconsin project as the reason "sufficient" was tempered); the
  "organismic trusting" / Western-individualism critiques of Rogers; Lambert's percentages as a
  heuristic, **not** a measured variance partition; SOLER's cultural non-universality; congruence↔UPR
  tension. Two anchor **books** (Carkhuff 1969; Egan 1975) are offline — corroborated via ≥2 secondary
  sources + the primary publication record, flagged inline.
- **Unit 2 cluster design:** all 36 items share one cluster (`theory-families`) by design — it *is*
  the confusable set the unit is built to interleave; the `topic` tag carries the specific school and
  the confusable pairs (ellis-vs-beck, bowen-vs-minuchin, sfbt-vs-narrative, etc.). Compare coverage
  is strong (6 dedicated `compare` items + differential mcqs).
- **Unit 2 person pages deferred** (in-depth build kept theory pages as the unit of organization):
  no separate `person-freud` / `person-yalom` / `person-beck` pages — figures are covered inline on
  each theory page. Split out if a later unit needs to link a person directly.
- **Unit 2 → Unit 9 handoff (RESOLVED 2026-07-19):** ~~`theory-cbt` links forward to a pending
  `unit09-modalities` page.~~ Wired in the Unit 9 build — `theory-cbt` now points to live
  `[[theory-cbt-practice]]` / `[[concept-cognitive-triangle]]` / `[[concept-behavioral-activation]]`
  (fixing a self-link bug where it pointed at itself), and `theory-postmodern` gained a forward link to
  `[[theory-solution-focused]]`. Theory (Unit 2) and practice (Unit 9) are paired, not duplicated.
- **Elective `aux-psychological-first-aid` → Unit 8 handoff:** all three concept pages link forward
  to the *pending* Unit 8 (crisis/risk/trauma-informed care) by name, not by wikilink (no
  `unit08-*` page exists yet). ~~When Unit 8 is built, wire these into real wikilinks and reconcile the
  PGD / vicarious-trauma overlap so the module and Unit 8 don't duplicate or contradict.~~ **RESOLVED
  2026-07-18:** forward-links wired to real wikilinks; overlap reconciled — PGD depth stays in Unit 6
  (`concept-trauma-stressor-disorders`), and the module's helper-load note now points to Unit 8's full
  `concept-vicarious-trauma` / `concept-counselor-self-care`.
- **Unit 3 cluster additions:** the unit introduced two clusters beyond the course-map's three —
  `ethics-principles` (the six principles are a genuinely confusable set: fidelity vs. veracity) and
  `boundary-concepts` (crossing vs. violation). Course-map entry updated to match. 10 items
  (informed-consent + competence topics) are intentionally unclustered — no confusable sibling.
- **Unit 3 Bloom balance:** evaluate=3 of 51 (decision-model, Tarasoff critique, report-while-
  preserving-alliance) — proportionally light; acceptable for a rules-heavy unit, revisit on `lint`.
- **Unit 3 → Unit 8 handoff (RESOLVED 2026-07-18):** ~~`concept-duty-to-warn`,
  `concept-confidentiality-limits`, `study-tarasoff`, `concept-scope-of-practice` (impairment), and
  the hub all forward-reference the *pending* Unit 8 by name.~~ Wired in the Unit 8 build — all Unit 3
  Unit-8 references are now live wikilinks (`[[unit08-crisis-trauma]]`, `[[concept-means-reduction]]`,
  `[[concept-suicide-risk-assessment]]`, `[[concept-counselor-self-care]]`; also
  `concept-mandated-reporting`). No by-name Unit-8 refs remain in the Unit 3 pages. See the "Unit 8
  forward handoffs WIRED" note below.
- **Unit 3 state-law caveat baked in:** duty-to-protect state counts cite a 2012-era compilation
  (StatPearls) and the RxP state list is a moving target (~7 as of 2024–25) — both flagged inline;
  re-verify numbers if this material is ever used for anything beyond orientation.
- **Unit 4 cluster additions:** the unit introduced four clusters beyond the course-map's one —
  `mc-frameworks` (tripartite vs. MSJCC vs. cultural humility), `acculturation-strategies` (Berry's
  2×2), `microaggression-types` (Sue's taxonomy), and `broaching-styles` (Day-Vines continuum) — and
  one page beyond the promised six (`concept-microaggressions`, split out per one-concept-per-page).
  Course-map entry updated to match. 12 items (privilege, help-seeking, mcc-evidence topics) are
  intentionally unclustered — no confusable sibling.
- **Unit 4 forward handoffs (resolved 2026-07-17):** the Unit 6 handoff (culture-bound presentations
  / misreading acculturative stress as disorder → `concept-dsm-structure`/CFI) and the Unit 7 handoff
  (culture-fair assessment) are now **live wikilinks**: the hub's "Connects forward" and
  `concept-acculturation`'s "Connects to" point to `unit07-assessment` / `concept-reliability-validity`
  / `concept-screening-tools`. No remaining Unit 6/7 by-name refs on the Unit 4 pages.
- **Unit 4 contested-material load is deliberately high** (humility-vs-competence, MCC measurement
  validity, Lilienfeld-vs-Sue): items quiz the debates themselves at evaluate level — if study
  sessions surface confusion between "what the framework says" and "what the critique says," that's
  the intended discrimination, not a bug.
- **Elective cluster design (RESOLVED 2026-07-19):** ~~`pfa-frameworks` has analyze/evaluate items but
  no dedicated `compare`-type item.~~ Added `ax-pfa-frameworks-compare-01` (WHO Look/Listen/Link vs.
  NCTSN 8 Core Actions — who each is for, the mapping, and that they're two slicings of one logic),
  `compare`/analyze. All three module clusters now have a dedicated compare: `pfa-frameworks`,
  `grief-models` (Kübler-Ross vs. dual process), `bereavement-support` (the three "where is she?"
  notification scenarios).
- **Death-notification addition (2026-07-08):** `concept-death-notification` added to the PFA
  elective (Core Action 2 territory: notification, missing loved ones, viewing the body) with an
  8-item set inside `bereavement-support`. Viewing-the-body evidence is qualitative (Chapple &
  Ziebland, n=80) — the practice standard is an *offered, prepared choice*; don't overstate it as
  proof viewing helps. When Unit 8 is built, add notification-after-suicide specifics and wire the
  forward wikilink (same handoff pass as the rest of the module).
- **Elective `aux-addiction` (2026-07-16):** 6 readings, 35 items, 16 sources; 4 clusters, each with
  a compare item, all 5 Bloom levels (R=6/U=9/Ap=7/An=9/E=4). Deliberately high contested-material
  load: the **brain-disease-vs-learning/choice** debate and **harm-reduction-vs-abstinence** are
  quizzed at evaluate level as debates, not settled facts — if study sessions surface confusion
  between "what the disease model says" and "what its critics say," that's the intended
  discrimination. `topic` tags carry the fine-grained confusables (tolerance/withdrawal/craving;
  MOUD-which-reduces-mortality; stage-matching).
- **Elective `aux-addiction` → Units 6/8/9 handoff:** the hub and concept pages forward-reference the
  *pending* Unit 6 (SUD as a DSM category), Unit 8 (overdose/naloxone/crisis), and Unit 9 (MI/CBT as
  general modalities) by name, not wikilink (no `unit06/08/09-*` pages exist yet). When those units
  are built, wire real wikilinks and reconcile overlap so the module and units don't duplicate or
  contradict: **SUD criteria** (module vs. Unit 6), **MI/CBT** (module vs. Unit 9). MI's OARS also
  traces to `unit01-helping-skills` (live wikilink already). **Unit 8 portion RESOLVED 2026-07-18:**
  the hub's overdose/naloxone/crisis forward-link is now a live wikilink to `unit08-crisis-trauma`
  (`concept-means-reduction`). **Unit 9 portion RESOLVED 2026-07-19:** the hub, `concept-stages-of-change`,
  and `concept-treatment-and-recovery` now point to live `[[unit09-modalities]]` /
  `[[theory-motivational-interviewing]]` / `[[theory-cbt-practice]]` / `[[concept-oars]]` — MI/CBT are
  the *general* tools there, applied to addiction here (no duplication). All aux-addiction forward
  handoffs (Units 6, 8, 9) are now wired.
- **Elective `aux-addiction` moving-target caveats:** MOUD/pharmacotherapy specifics and CM's
  "gold-standard for stimulants" reflect 2024–25 evidence; the AA/TSF Cochrane finding (Kelly 2020)
  reversed prior "no evidence" claims — re-verify if used beyond orientation. SMART Recovery's
  evidence base is thinner than AA's (noted inline).
- **Unit 5 page consolidation (deliberate):** the course-map promised 10 pages including four
  separate per-style pages (`concept-secure/anxious/avoidant/disorganized-attachment`) and a separate
  `person-bowlby-ainsworth`. Built as **7 pages**: the four styles are folded into one
  `concept-attachment-styles.md` (the confusable set is best taught side-by-side — compare/contrast
  baked into one page, same rationale as Unit 1's `concept-core-conditions`), and Bowlby/Ainsworth
  **plus Main** share one `person-bowlby-ainsworth.md`. Per-style topic tags (`secure-attachment`,
  `avoidant-attachment`, `anxious-attachment`, `disorganized-attachment`) carry the fine-grained
  discrimination inside the `attachment-styles` cluster. Split later if item volume grows.
- **Unit 5 cluster addition beyond course-map:** added `piaget-stages` (the four cognitive stages are
  a genuinely confusable set) alongside the course-map's `attachment-styles`, `erikson-stages`, and
  `developmental-theorists`. Course-map entry updated to match. Attachment *theory/mechanism* items
  (secure base, IWM, phases, Strange Situation, sensitivity/transmission-gap, AAI) are intentionally
  **unclustered** (7 items) — they're not the styles confusable set; topic tags carry them. The 3
  biopsychosocial items and 4 typical-vs-clinical/risk-not-destiny/rep items are also unclustered.
- **Unit 5 Bloom spread:** R=7/U=9/Ap=12/An=9/E=8 across 45 items — heavy on apply/analyze/evaluate
  per generate rules; every cluster has ≥1 compare (`attachment-styles` 1, `erikson-stages` 2,
  `piaget-stages` 1, `developmental-theorists` 1 = 5 compares). Types: 12 explain, 10 mcq
  (discrimination vignettes), 9 recall, 5 compare, 5 vignette, 4 cloze.
- **Unit 5 → Unit 1 back-link wired:** `concept-therapeutic-alliance` (Unit 1) now forward-links to
  `theory-attachment` / `concept-attachment-styles` (attachment as the developmental theory of the
  bond; source_units updated to [1,3,5,7]) — the course-map's Unit 5 ↔ Unit 1 thread, made live.
- **Unit 5 forward handoffs (Unit 6/7 resolved 2026-07-17):** the Unit 7 handoff on
  `concept-biopsychosocial-model` (the intake biopsychosocial history) is now a **live wikilink** to
  `unit07-assessment` / `concept-intake-interview` (both the body and the "Connects to" bullet); the
  Unit 6 handoff was wired in the Unit 6 pass. Only **Unit 11** (biological domain) remains a by-name
  forward-reference — wire when Unit 11 is built. Note the aging/grief end of the lifespan is handled
  by cross-link to the existing PFA elective (`concept-grief-models`), not duplicated here.
- **Unit 5 contested-material load is deliberately high** (maternal-sensitivity r≈.24 + transmission
  gap; Strange Situation as possible imposed etic; Erikson/Piaget as heuristics not laws;
  biopsychosocial "slogan" critique; disorganized-attachment risk-not-destiny): items quiz these as
  live debates at evaluate level. If study sessions surface confusion between "what the framework
  says" and "what its critique says," that's the intended discrimination. Disorganized-attachment
  material is kept clinical and non-deterministic per the heavy-topic handling in CLAUDE.md.
- **Unit 6 page plan deviations (deliberate, 2026-07-17):** built **12** pages vs. the course-map's
  promised 11 — `concept-comorbidity` was **folded into `concept-categorical-vs-dimensional`**
  (comorbidity is that debate's core evidence; one coherent argument, one page), and two pages were
  **added** beyond the promise: `concept-neurodevelopmental-disorders` and
  `concept-eating-disorders` (both syllabus core-concept categories the course-map page list had
  skipped). `concept-substance-use-disorders` is deliberately concise: the DSM-structural view only,
  deferring depth to the `aux-addiction` elective (overlap reconciled — see below). Course-map entry
  updated to match.
- **Unit 6 cluster additions beyond course-map:** `psychotic-spectrum` (the duration ladder is a
  genuinely confusable set) and `eating-disorders` (AN/BN/BED hinges), alongside the promised
  `mood-disorders`, `anxiety-disorders`, `trauma-disorders`, `personality-disorders`, and
  `differential-vignettes`. OCD items (4), manual/structure items (7), SUD items (2),
  neurodevelopmental items (4), and categorical-vs-dimensional items (8) are intentionally
  **unclustered** (25 total) — topic tags carry them; their discriminations live as
  `differential-vignettes` entries (OCD-vs-GAD, ASD-vs-social-anxiety, mania-vs-ADHD,
  substance-induced, medical rule-out).
- **Unit 6 Bloom spread:** R=20/U=10/Ap=18/An=19/E=8 across 75 items; every cluster has ≥1 compare
  (8 total: grief-vs-MDD, mania-vs-hypomania, anxiety fear-map, trauma stressor×clock, psychotic
  duration ladder, OCD-vs-OCPD, eating hinges, flashback-vs-hallucination). Types: 20 mcq
  (discrimination vignettes — deliberately high for this unit per the course-map's "heavy vignette
  unit" note), 18 explain, 15 recall, 11 cloze, 8 compare, 3 vignette. Includes the syllabus
  practice rep as three production items (explain MDD/GAD/PTSD to a layperson in 2 minutes).
- **Unit 6 ↔ aux-addiction reconciliation (done):** `concept-substance-use-disorders` carries the
  DSM-structural view and wikilinks into the module; module hub + `concept-addiction-models`
  "Unit 6 (planned)" references rewired to real wikilinks. No criteria duplication: the 11-criteria
  deep-dive stays in the module.
- **Unit 6 back-links wired:** `unit05-development` (both Unit 6 mentions), `concept-acculturation`
  (culture-bound presentations → `concept-dsm-structure`/CFI), and the PFA elective's
  `concept-grief-models` (PGD → `concept-trauma-stressor-disorders` + `concept-mood-disorders`).
- **Unit 6 forward handoffs (Unit 7 resolved 2026-07-17):** the Unit 7 refs (case conceptualization,
  MSE, intake) are now **live wikilinks** — the hub, `concept-dsm-structure`,
  `concept-substance-use-disorders`, and `concept-categorical-vs-dimensional` point to
  `unit07-assessment` / `concept-case-conceptualization` / `concept-intake-interview` /
  `concept-treatment-planning`. Still by-name (pending): Unit 8 (risk assessment, suicidal-behavior
  codes, trauma-informed care — `concept-trauma-stressor-disorders` explicitly defers neurobiology/
  treatment there), Unit 9 (CBT/ERP/DBT/behavioral activation as modalities), and Unit 11 (medication,
  dopamine hypothesis depth). The Unit 8 build should also reconcile PTSD/ASD criteria (here) vs.
  trauma-informed care (there), and the new DSM-5-TR suicidal-behavior symptom codes.
  **Unit 8 portion RESOLVED 2026-07-18** (see the "Unit 8 forward handoffs WIRED" note). **Unit 9
  portion RESOLVED 2026-07-19:** `concept-mood-disorders` (behavioral activation → `[[concept-behavioral-activation]]`),
  `concept-anxiety-disorders` + `concept-ocd` (CBT/exposure/ERP → `[[theory-cbt-practice]]`), and
  `concept-personality-disorders` (DBT → `[[concept-dbt-skills]]`) now use live wikilinks. Only **Unit 11**
  (medication / dopamine depth) remains by-name.
- **Unit 6 criteria-are-paraphrases caveat baked in:** all criteria summarized from peer-reviewed
  secondary references (StatPearls et al.), not the paywalled DSM-5-TR text — flagged in the
  sources file and the hub ("quote the manual before relying on a criterion clinically").
  Prevalence figures are survey-era-dependent (NCS-R is DSM-IV-based); treat as order-of-magnitude.
- **Unit 6 contested-material load is deliberately high** (categorical-vs-dimensional as a live
  fight; diagnostic inflation vs. early intervention; bereavement exclusion / PGD; Criterion A as a
  drawn line; neurodiversity vs. deficit framing): items quiz the debates themselves at evaluate
  level — confusion between "what the DSM says" and "what its critics say" that surfaces in study
  sessions is the intended discrimination, not a bug.
- **Unit 7 page plan deviation (deliberate, 2026-07-17):** built **7** pages vs. the course-map's
  promised 8 — the separate `concept-phq9` and `concept-gad7` pages were **consolidated into one
  `concept-screening-tools.md`** (the two instruments are a confusable set best taught side-by-side,
  same rationale as Unit 5's `concept-attachment-styles` and Unit 6's consolidations). Per-instrument
  `topic` tags (`phq-9`, `gad-7`, `phq9-vs-gad7`) carry the fine-grained discrimination inside the
  `screening-tools` cluster. Course-map entry updated to match.
- **Unit 7 cluster addition beyond course-map:** added `formulation-ps` (the Five Ps are a genuinely
  confusable set — predisposing/precipitating/perpetuating/protective) alongside the course-map's
  `mse-domains`, `screening-tools`, and `reliability-vs-validity`. Intake (6) and treatment-planning
  (6) items are intentionally **unclustered** — no confusable sibling set; topic tags carry them.
- **Unit 7 Bloom spread:** R=15/U=12/Ap=10/An=7/E=7 across 51 items — heavy on apply/analyze/evaluate
  (24) per generate rules. Types: 12 explain, 10 recall, 9 mcq (the confusable-pair discriminations),
  9 cloze, 7 compare, 4 vignette. Every cluster has ≥1 compare — `mse-domains` 2, `screening-tools` 1,
  `reliability-vs-validity` 1, `formulation-ps` 1 (5 clustered) + 2 unclustered (intake structure,
  goal-vs-objective) = 7 compare items total. Includes the syllabus production rep as a one-page case
  conceptualization of a novel/show character (`u7-formulation-rep-01`, a `recall`-type item).
- **Unit 7 back-links wired (resolved earlier by-name handoffs):** `concept-dsm-structure`,
  `unit06-psychopathology`, `concept-categorical-vs-dimensional`, `concept-substance-use-disorders`
  (Unit 6); `concept-biopsychosocial-model` (Unit 5); `unit04-multicultural`, `concept-acculturation`
  (Unit 4); `unit02-theories` (theory→formulation thread); `concept-therapeutic-alliance` (Unit 1 —
  `source_units: [1,3,5,7]` verified, now forward-links case-conceptualization/treatment-planning).
- **Unit 7 forward handoffs (by name, not wikilink):** the screening/MSE/intake pages forward-reference
  the *pending* Unit 8 (item-9 → suicide-risk protocol, C-SSRS, PC-PTSD-5) and Unit 12 (outcome
  monitoring / MBC as program evaluation; `concept-reliability-validity` carries `source_units: [7,12]`)
  by name. Wire to real wikilinks when Units 8 and 12 are built.
- **Unit 7 sourcing caveats baked in:** two sources 403'd to automated fetch — the Psychiatric Services
  MBC full text (S12) and the OER reliability chapter (S11) — and are cited via abstracts/search-indexed
  summaries **plus a corroborating source** (S5 IOM for psychometrics; the journal abstract for MBC),
  flagged inline in the sources file. The "golden thread" (S14) is a documentation/compliance
  convention, not a scientific finding — labeled orientation-tier. Screening cut-points are flagged as
  population-dependent, not universal (S10's ≥8 vs. the standard ≥10).
- **Unit 8 page plan (as promised, 2026-07-18):** built the full **9** pages the course-map listed
  (hub + suicide-risk-assessment, safety-planning, means-reduction, de-escalation, trauma-informed-care,
  neurobiology-of-trauma, vicarious-trauma, counselor-self-care) — no consolidation this time; each is
  a genuinely distinct topic. `concept-neurobiology-of-trauma` carries `source_units: [8, 11]` (a
  working-level preview of the Unit 11 stress-response material).
- **Unit 8 clusters added beyond course-map (noted in course-map):** the course-map named
  `crisis-response-models` and `trauma-informed-vs-treatment`; the build added three more genuinely
  confusable sets — `suicide-risk-concepts` (warning-sign/risk-factor/protective; acute/chronic;
  ideation/plan/intent/means; ideation-to-action), `trauma-brain` (amygdala/hippocampus/PFC; window of
  tolerance hyper/hypo; explicit/implicit memory), and `counselor-distress-types` (VT vs. STS vs.
  compassion fatigue vs. burnout vs. countertransference — the prime interleaving target). Note
  `crisis-response-models` deliberately spans three pages (safety-planning, means-reduction,
  de-escalation) — it *is* the "what do I do in a crisis" confusable set.
- **Unit 8 Bloom spread:** R=16/U=11/Ap=17/An=13/E=10 across 67 items — heavy on apply/analyze/evaluate
  (40) per generate rules. Types: 16 explain, 14 mcq (discrimination vignettes), 12 recall, 10 cloze,
  8 compare (≥1 per cluster: suicide-risk-concepts 2, crisis-response-models 2, trauma-brain 2,
  trauma-informed-vs-treatment 1, counselor-distress-types 1), 7 vignette. Includes the syllabus
  practice rep (a memorized structure for asking about suicidal ideation, `u8-sra-rep-01`). Stance
  probes throughout: ask-directly/don't-freeze, assess-to-manage-not-predict, safety-plan-not-contract,
  don't-dig, freeze-is-not-a-choice, self-care-as-ethics/martyr-reflex.
- **Unit 8 forward handoffs WIRED (resolved 2026-07-18):** all previously by-name "Unit 8" references
  are now live wikilinks (40 replacements across 22 files) — **Unit 3** (`concept-duty-to-warn`,
  `concept-confidentiality-limits`, `study-tarasoff`, `concept-scope-of-practice`, `concept-mandated-
  reporting`, hub), **Unit 6** (`concept-trauma-stressor-disorders` [neurobiology/treatment/don't-
  retraumatize + suicidal-behavior codes reconciled], `concept-dsm-structure`, `concept-mood-disorders`,
  `concept-psychotic-disorders`, `concept-ocd`, hub), **Unit 7** (`unit07-assessment`,
  `concept-screening-tools` [item-9 trip-wire, PC-PTSD-5, C-SSRS], `concept-intake-interview`), the
  **PFA elective** (hub, `concept-grief-models`, `concept-supporting-the-bereaved`,
  `concept-death-notification`), the **addiction elective** (hub, `concept-treatment-and-recovery`),
  and `theory-postmodern`. No `unit08-*` by-name refs remain in the wiki.
- **Unit 8 contested-material load is deliberately high** and surfaced as items at evaluate level:
  individual suicide is **not predictable** (the Tarasoff prediction critique in a new setting — assess
  to manage, not prophesy); **no-suicide contracts are not evidence-based**; trauma **cortisol findings
  are inconsistent** (no clean biomarker); the **window of tolerance** and **polyvagal theory** are
  heuristics, not validated brain states; **van der Kolk's *Body Keeps the Score* is popular-press**
  (mechanisms corroborated against peer-reviewed S14/S15; the memory-as-storage and recovered-memory
  claims flagged). Per CLAUDE.md's heavy-topic rule the material is kept clinical and precise, no
  sensationalism.
- **Unit 8 sourcing caveats baked in:** the two anchor **books** (James & Gilliland; Herman) are offline
  and cited via reputable secondary summaries; SAMHSA's exact 4Rs/6-principles/3Es wording was confirmed
  across two secondary summaries + the primary publication record; the HPA-axis review (S14) and the
  Trippany/Kress *Journal of Counseling & Development* vicarious-trauma article (S19) were **read in full
  via pypdf**. Firearm case-fatality (~85–90%) and crisis-duration (minutes–hour) figures are
  order-of-magnitude public-health estimates (Means Matter), not precise constants.
- **Unit 9 page plan deviation (deliberate, 2026-07-19):** built **9** pages vs. the course-map's
  promised 8 — the single `concept-act-dbt-skills` page was **split** into `concept-act` and
  `concept-dbt-skills` (ACT and DBT are distinct third-wave therapies; one-concept-per-page, same
  rationale as prior splits). `theory-cbt-practice` and `theory-solution-focused` are the **practice**
  counterparts to Unit 2's `theory-cbt` / `theory-postmodern` (theory there, hands-on toolkit here) —
  paired via bidirectional wikilinks, not duplicated. Course-map entry updated to match.
- **Unit 9 cluster additions beyond course-map:** the course-map named `ebt-modalities` and
  `oars-skills`; the build added four genuinely confusable sets — `cbt-techniques` (cognitive
  restructuring vs. behavioral activation vs. exposure), `mi-processes` (spirit/PACE, four processes,
  change vs. sustain talk, righting reflex), `sfbt-techniques` (miracle vs. exception vs. scaling vs.
  coping), and `third-wave-skills` (ACT hexaflex vs. DBT modules; acceptance vs. change). Note
  `ebt-modalities` is the **big cross-modality "which tool fits this client?" differential** — the
  unit's prime interleaving target, carried by the four modality-fit discrimination mcqs.
- **Unit 9 Bloom spread:** R=13/U=7/Ap=17/An=13/E=7 across 57 items — heavy on apply/analyze/evaluate
  (37) per generate rules. Types: 21 explain, 9 recall, 7 compare, 7 mcq (the modality-fit
  discriminations), 7 vignette, 6 cloze. Every cluster has ≥1 compare (6/6, 7 total: `third-wave-skills`
  has 2 — ACT-vs-DBT and defusion-vs-restructuring). Includes the syllabus practice rep (run a thought
  record on a recent frustration, `u9-thought-record-rep-01`).
- **Unit 9 stance thread is the spine:** these are the "fixing" tools, and the unit leans into the
  paradox that two of them make *not* fixing the central move — MI's **righting reflex** (hold it) and
  the third wave's **acceptance** (ACT/DBT). Stance probes throughout: hold-the-righting-reflex,
  act-not-feel (BA outside-in), acceptance-is-not-resignation, affirmation-vs-contingent-approval,
  reflect-more-than-you-ask, prescribe-BA-collaboratively-not-at-the-client, borrow-DBT-skills-vs-
  claim-to-do-DBT (scope).
- **Unit 9 contested-material load is deliberately high** and quizzed at evaluate level: (1) the
  **common-factors / dodo-bird** caveat — "evidence-based modality" ≠ "best"; the alliance carries much
  of the outcome and between-therapy technique differences are typically small (`ebt-modalities`
  frames every "which tool?" item under this); (2) the **CBT dismantling** finding — BA alone matched
  full CBT (Jacobson 1996) and beat cognitive therapy / matched meds for severe depression (Dimidjian
  2006; COBRA non-inferiority), genuinely complicating "you must fix the thoughts"; (3) **third-wave ≠
  proven-superior** to standard CBT; (4) **allegiance/publication bias** inflates SFBT's largest
  reported effect sizes (proponent g≈3.02 flagged; the peer-reviewed g≈1.17 preferred). If study
  sessions surface confusion between "what the modality claims" and "what the evidence shows," that's
  the intended discrimination.
- **Unit 9 sourcing caveats baked in:** four anchor **books** (J. Beck; Miller & Rollnick; Hayes et al.;
  Linehan) are offline and cited via reputable secondary sources + the primary publication record,
  flagged. MI is anchored on **SAMHSA TIP 35** (government consensus, NCBI); ACT on the **ACBS**
  in-tradition society; BA on **primary trials** (Jacobson 1996, Dimidjian 2006, COBRA/Richards 2016).
  The SFBT institute page (S12) is a **proponent source** — used for technique descriptions/study
  tallies, with its largest effect sizes explicitly down-weighted in favor of the peer-reviewed
  Franklin 2024 meta-analysis (S13).
- **Unit 9 forward handoffs (by name, not wikilink):** `theory-cbt-practice`/`concept-cognitive-triangle`
  reference **Unit 11** (neuroscience) only implicitly; the unit's own outward links (Units 1/2/6/7/8 +
  both electives) are all **live wikilinks**. No `unit09-*` by-name refs remain in the wiki (verified:
  0 broken links across 89 wiki pages; all 9 new pages have inbound links, no orphans).
- **Unit 10 page plan expansion (deliberate, 2026-07-19):** built **7** pages vs. the course-map's
  promised 4 — added `concept-group-types` (ASGW's four specializations), `concept-difficult-group-members`
  (the syllabus's named "managing difficult members" core concept, given its own page), and
  `concept-group-ethics-and-formation` (screening/preparation/consent + the group-specific confidentiality
  limit). All three are core CACREP **Group Counseling & Group Work** content the 4-page list skipped.
  Person page for Yalom **deferred** (covered inline on `theory-yalom-factors` + the hub), consistent
  with the Unit 2 person-page deferral. Course-map entry updated to match.
- **Unit 10 clusters added beyond course-map:** the course-map named `yalom-factors` + `group-stages`;
  the build added four genuinely confusable sets — `leadership-functions` (the four Lieberman/Yalom/Miles
  functions + the linear/curvilinear discrimination + Lewin's three styles), `group-types` (ASGW's
  task/psychoeducational/counseling/psychotherapy), `difficult-members` (Yalom's monopolist/silent/
  help-rejecting-complainer/scapegoat prototypes), and `group-formation` (screening/consent/confidentiality).
  4 items are intentionally **unclustered** — the "why groups heal differently" throughline (why-group,
  group-vs-individual efficacy, the audience trap, the cohesion-efficacy caveat) has no confusable sibling
  set; topic tags carry them.
- **Unit 10 Bloom spread:** R=10/U=5/Ap=17/An=12/E=13 across 57 items — heavy on apply/analyze/evaluate
  (42) per generate rules. Types: 25 explain, 9 mcq (the which-factor/stage/type/member discriminations),
  7 compare (≥1 per cluster — `leadership-functions` has 2: linear-vs-curvilinear and process-vs-content),
  6 vignette, 5 recall, 5 cloze. **Understand is proportionally light (5)** — acceptable for a unit whose
  payoff is discrimination and stance, but a candidate for a few added understand-level items on a later
  `lint`/generate pass. No syllabus practice rep exists for this unit (the Unit 10 syllabus entry lists
  none), so none was forced.
- **Unit 10 stance thread is the spine:** the "resist the urge to fix" caution becomes **decenter
  yourself and trust the group** — the beginner trap is running individual therapy in front of an
  audience (serial dyads), which starves the group's distinctive engines (universality, altruism,
  interpersonal learning). Stance probes throughout: decenter/turn-the-work-back-to-the-group,
  storming-is-on-schedule, difficult-member-as-opportunity, decline-the-help-rejecting-complainer's-bait,
  a-"resistant"-group-may-be-a-leadership-signal, can't-guarantee-group-confidentiality.
- **Unit 10 contested-material load (quizzed at evaluate):** the therapeutic factors are **clinically
  derived, not a validated factor structure** (rankings vary by group/member/study; lists count 11–14);
  **cohesion's clinical centrality outruns its efficacy evidence** (interpersonal feedback and the
  alliance have firmer support); groups can **harm** (the Lieberman/Yalom/Miles casualty finding →
  aggressive stimulators); and "group is the cheaper/worse option" is **wrong** (Burlingame's 46-RCT
  equivalence). Members and clinicians rank the factors differently — the intended humility check.
- **Unit 10 sourcing caveats baked in:** three anchor **books** (Yalom & Leszcz; Corey; Lieberman/Yalom/
  Miles *Encounter Groups: First Facts*) are offline and cited via reputable secondary sources +
  the primary publication record (StatPearls, APA/Burlingame, ASGW/ACA, IAHIP), flagged in the sources
  file. Two educational secondaries (psychology.town, S3/S9/S12) are **orientation-tier**, used for
  definitions and cross-checked against StatPearls [S1] and the primaries. ACA **B.4.a** quoted verbatim.
- **Unit 10 cross-unit wiring done:** the marquee **Unit 1 ↔ Unit 10** thread is live — `concept-therapeutic-alliance`
  now forward-links `[[theory-yalom-factors]]`/`[[unit10-group]]` (cohesion = the alliance's client-client
  analog; `source_units` → [1,3,5,7,10]), and `concept-dbt-skills` now points to `[[concept-group-types]]`
  (a DBT skills group *is* a psychoeducational group). No earlier page carried a by-name "pending Unit 10"
  handoff (Unit 10 is a leaf that depends on Unit 1, not one earlier units forward-referenced). All Unit 10
  outward links (Units 1/2/3/5/6/9) are live wikilinks. Verified clean build; every new page has inbound
  links (no orphans).
