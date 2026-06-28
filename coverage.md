# Coverage map

What's built vs. pending, and where the readings and practice have holes. Updated by `lint` and
`create chapter`. The Bloom/item columns fill in as units are created.

## Build status

| Unit | Tier | Readings | Items | Bloom spread | Clusters w/ compare items |
|---|---|---|---|---|---|
| 1 Helping Skills | 1 | ☑ (5) | ☑ (17) | all 5 levels | 1/4 (microskill-types*) |
| 2 Theories | 1 | ☑ (7) | ☑ (36) | all 5 levels | theory-families ✓ (6 compares) |
| 3 Ethics & Law | 1 | ☐ | ☐ | — | — |
| 4 Multicultural | 1 | ☐ | ☐ | — | — |
| 5 Development | 2 | ☐ | ☐ | — | — |
| 6 Psychopathology | 2 | ☐ | ☐ | — | — |
| 7 Assessment | 2 | ☐ | ☐ | — | — |
| 8 Crisis & Trauma | 2 | ☐ | ☐ | — | — |
| 9 Modalities | 3 | ☐ | ☐ | — | — |
| 10 Group | 3 | ☐ | ☐ | — | — |
| 11 Neuroscience | 3 | ☐ | ☐ | — | — |
| 12 Research | 3 | ☐ | ☐ | — | — |

☐ pending · ◐ partial · ☑ complete

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
