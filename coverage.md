# Coverage map

What's built vs. pending, and where the readings and practice have holes. Updated by `lint` and
`create chapter`. The Bloom/item columns fill in as units are created.

## Build status

| Unit | Tier | Readings | Items | Bloom spread | Clusters w/ compare items |
|---|---|---|---|---|---|
| 1 Helping Skills | 1 | ☑ (5) | ☑ (17) | all 5 levels | 1/4 (microskill-types*) |
| 2 Theories | 1 | ☑ (7) | ☑ (36) | all 5 levels | theory-families ✓ (6 compares) |
| 3 Ethics & Law | 1 | ☑ (9) | ☑ (51) | all 5 levels | 5/5 ✓ (9 compares) |
| 4 Multicultural | 1 | ☑ (7) | ☑ (48) | all 5 levels | 5/5 ✓ (6 compares) |
| 5 Development | 2 | ☐ | ☐ | — | — |
| 6 Psychopathology | 2 | ☐ | ☐ | — | — |
| 7 Assessment | 2 | ☐ | ☐ | — | — |
| 8 Crisis & Trauma | 2 | ☐ | ☐ | — | — |
| 9 Modalities | 3 | ☐ | ☐ | — | — |
| 10 Group | 3 | ☐ | ☐ | — | — |
| 11 Neuroscience | 3 | ☐ | ☐ | — | — |
| 12 Research | 3 | ☐ | ☐ | — | — |

☐ pending · ◐ partial · ☑ complete

## Elective / ad-hoc modules (off-spine)

Built in the `aux-` namespace; not part of the 12-unit count. Same coverage rules apply.

| Module | Borders | Readings | Items | Bloom spread | Clusters w/ compare items |
|---|---|---|---|---|---|
| PFA & Acute Grief Support (`aux-psychological-first-aid`) | Unit 8 | ☑ (5) | ☑ (31) | all 5 levels | `grief-models` ✓ · `bereavement-support` ✓ (notification-scenarios compare) |

## Coverage rules the lint pass enforces
- Every major concept has at least one **Apply** or **Analyze** item, not only "define"-level.
- Every confusable `cluster` (see course-map) has at least one **compare** item.
- Every item's `source_page` still exists and hasn't materially changed since the item was written.
- No orphan readings (a page nothing links to) and no missing concept pages the course-map promised.

## Known holes
- **Unit 1 compare-coverage:** only the `microskill-types` cluster has an explicit compare item
  (`u1-empathy-analyze-01` also serves `rogers-conditions`). `alliance-components` and
  `common-factors` have analyze/evaluate items but no dedicated `compare`-type item. Add on next
  `lint` or `generate items 1` pass if desired.
- Per-condition pages (separate UPR/empathy/congruence) were folded into `concept-core-conditions`
  for the concise build; split later if item volume grows.
- `person-carl-rogers` page deferred (concise build) — folded into `concept-core-conditions`.
- **Unit 2 cluster design:** all 36 items share one cluster (`theory-families`) by design — it *is*
  the confusable set the unit is built to interleave; the `topic` tag carries the specific school and
  the confusable pairs (ellis-vs-beck, bowen-vs-minuchin, sfbt-vs-narrative, etc.). Compare coverage
  is strong (6 dedicated `compare` items + differential mcqs).
- **Unit 2 person pages deferred** (in-depth build kept theory pages as the unit of organization):
  no separate `person-freud` / `person-yalom` / `person-beck` pages — figures are covered inline on
  each theory page. Split out if a later unit needs to link a person directly.
- **Unit 2 → Unit 9 handoff:** `theory-cbt` links forward to a pending `unit09-modalities` page
  (CBT/MI as practical toolkit). Fix that wikilink target when Unit 9 is built.
- **Elective `aux-psychological-first-aid` → Unit 8 handoff:** all three concept pages link forward
  to the *pending* Unit 8 (crisis/risk/trauma-informed care) by name, not by wikilink (no
  `unit08-*` page exists yet). When Unit 8 is built, wire these into real wikilinks and reconcile the
  PGD / vicarious-trauma overlap so the module and Unit 8 don't duplicate or contradict.
- **Unit 3 cluster additions:** the unit introduced two clusters beyond the course-map's three —
  `ethics-principles` (the six principles are a genuinely confusable set: fidelity vs. veracity) and
  `boundary-concepts` (crossing vs. violation). Course-map entry updated to match. 10 items
  (informed-consent + competence topics) are intentionally unclustered — no confusable sibling.
- **Unit 3 Bloom balance:** evaluate=3 of 51 (decision-model, Tarasoff critique, report-while-
  preserving-alliance) — proportionally light; acceptable for a rules-heavy unit, revisit on `lint`.
- **Unit 3 → Unit 8 handoff:** `concept-duty-to-warn`, `concept-confidentiality-limits`,
  `study-tarasoff`, `concept-scope-of-practice` (impairment), and the hub all forward-reference the
  *pending* Unit 8 by name (danger-to-self operationalization, means restriction, self-care as
  ethical competency). Wire to real `unit08-*` wikilinks when Unit 8 is built — same reconciliation
  pass as the PFA-module handoff below.
- **Unit 3 state-law caveat baked in:** duty-to-protect state counts cite a 2012-era compilation
  (StatPearls) and the RxP state list is a moving target (~7 as of 2024–25) — both flagged inline;
  re-verify numbers if this material is ever used for anything beyond orientation.
- **Unit 4 cluster additions:** the unit introduced four clusters beyond the course-map's one —
  `mc-frameworks` (tripartite vs. MSJCC vs. cultural humility), `acculturation-strategies` (Berry's
  2×2), `microaggression-types` (Sue's taxonomy), and `broaching-styles` (Day-Vines continuum) — and
  one page beyond the promised six (`concept-microaggressions`, split out per one-concept-per-page).
  Course-map entry updated to match. 12 items (privilege, help-seeking, mcc-evidence topics) are
  intentionally unclustered — no confusable sibling.
- **Unit 4 forward handoffs:** `concept-acculturation` and the hub forward-reference the *pending*
  Unit 6 (culture-bound presentations / misreading acculturative stress as disorder) and Unit 7
  (culture-fair assessment) by name, not wikilink. Wire when those units are built.
- **Unit 4 contested-material load is deliberately high** (humility-vs-competence, MCC measurement
  validity, Lilienfeld-vs-Sue): items quiz the debates themselves at evaluate level — if study
  sessions surface confusion between "what the framework says" and "what the critique says," that's
  the intended discrimination, not a bug.
- **Elective cluster design:** `pfa-frameworks` has analyze/evaluate items but no dedicated
  `compare`-type item; explicit compares live in `grief-models` (Kübler-Ross vs. dual process) and
  `bereavement-support` (the three "where is she?" notification scenarios, added 2026-07-08). Add a
  `pfa-frameworks` compare on a later `lint`/`generate` pass if desired (e.g. WHO Look/Listen/Link
  vs. NCTSN 8 Core Actions).
- **Death-notification addition (2026-07-08):** `concept-death-notification` added to the PFA
  elective (Core Action 2 territory: notification, missing loved ones, viewing the body) with an
  8-item set inside `bereavement-support`. Viewing-the-body evidence is qualitative (Chapple &
  Ziebland, n=80) — the practice standard is an *offered, prepared choice*; don't overstate it as
  proof viewing helps. When Unit 8 is built, add notification-after-suicide specifics and wire the
  forward wikilink (same handoff pass as the rest of the module).
