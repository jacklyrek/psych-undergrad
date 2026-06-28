# CLAUDE.md — Psych Learning Wiki schema

This is the operating manual for this repository. It is a **self-maintaining, LLM-built study
system** for a counseling-foundations curriculum. The agent (you) is the researcher, author, and
maintainer; the human provides the syllabus, fires commands, directs emphasis, spot-checks
sourcing, and does the practice.

Two companion documents govern *how* you work and must be consulted:
- [`counseling-syllabus.md`](counseling-syllabus.md) — the spine. 12 units, 3 tiers. The only human-authored input.
- [`learning-science-for-self-study.md`](learning-science-for-self-study.md) — the rulebook for generating study material. **Consult before generating any items.**

> Terminology: the syllabus is organized into **Units**. The driving command is `create chapter X`,
> where "chapter X" == "Unit X". `create chapter`, `create unit`, and `do chapter` are synonyms.

---

## Directory layout

```
psych-undergrad/
├── CLAUDE.md                       # this file — the schema
├── counseling-syllabus.md          # human input: the spine
├── learning-science-for-self-study.md  # the generation rulebook
├── course-map.md                   # research brief: per-unit scope, objectives, deps, clusters
├── index.md                        # content catalog (readings + items), by unit
├── coverage.md                     # what's been built vs. pending; Bloom/item coverage map
├── log.md                          # append-only chronological log
├── research/                       # per-unit sources files (evidence base)
│   └── unitNN-<slug>-sources.md
├── wiki/                           # the readings (LLM-authored markdown, cited)
│   ├── unitNN-<slug>.md            # chapter-level reading page
│   ├── concept-<slug>.md           # one concept per page
│   ├── theory-<slug>.md            # theory/framework page
│   ├── study-<slug>.md             # key-study page
│   └── person-<slug>.md            # researcher/clinician page
├── items/                          # the learning layer (markdown source of truth)
│   ├── unitNN-<slug>.md            # items for a unit, YAML-frontmatter blocks
│   └── build/
│       └── items.json              # compiled bank the apps read (built by build_items.py)
├── apps/                           # Streamlit front-ends + build/scheduler code
│   ├── build_items.py              # compiles items/*.md → items/build/items.json
│   ├── scheduler.py                # SM-2 (upgraded from Leitner; migrates old box-state)
│   └── quiz_runner.py              # the study loop (build first)
└── review_log.csv                  # app-written attempt log (created on first study session)
```

Empty directories carry a short `README.md` until populated.

---

## Storage decision (locked)

**Hybrid.** Markdown in `items/` (with fenced ```json item blocks) is the **source of truth** — I
author and edit it, it stays browsable in Obsidian and diffs cleanly in git. A build step (`apps/build_items.py`) compiles
it to `items/build/items.json`, which the Streamlit apps load. Apps **read** `items.json` and
**write** attempts to `review_log.csv`. **Apps never modify readings or item source.** Scheduler
state for now lives in `review_log.csv` / a small state file the app owns, not in the item source —
the item markdown holds the *content and metadata*, the app owns the *scheduling state*.

---

## The driving command: `create chapter X`

Runs readings **and** items in one pass (locked default). Pause for human input where flagged.

1. **Scope.** Read Unit X's entry in [`course-map.md`](course-map.md) (objectives, core concepts,
   dependencies, anchor resource). If the course-map entry is thin or the syllabus gives only a
   title, first research the *standard* scope of the topic, propose an outline, and **confirm with
   the human before deep research.**
2. **Research thoroughly.** Go to the open web. Triangulate across several reputable free sources
   (see Research rules). Save everything used to `research/unitNN-<slug>-sources.md` with a one-line
   authority note per source.
3. **Draft & discuss.** Surface key takeaways and any points where sources disagree or evidence is
   shaky/dated/contested. Let the human steer emphasis toward what counseling programs (CACREP) care
   about.
4. **Write the readings.** Concept / theory / study / person pages + a `unitNN-<slug>.md` chapter
   reading page. Clean interlinked markdown, **inline citations** back to the sources file. Link new
   pages into `course-map.md` and to related earlier pages (wikilinks).
5. **Generate learning opportunities** (see "Generate rules"). Consult the learning-science doc.
6. **Bookkeep.** Update `index.md`, `coverage.md`; append a `## [date] create-chapter | Unit X | …`
   line to `log.md`. Rebuild `items/build/items.json` (run/refresh `build_items.py`).

Sibling commands: `generate items X` (step 5 only), `query "…"`, `lint`.

---

## Research rules (the part that earns trust)

- **Triangulate.** Corroborate substantive claims across multiple independent sources. Never build a
  page on a single blog post.
- **Prefer authority.** Open textbooks (OpenStax, Noba Project), university/OpenCourseWare and `.edu`
  pages, professional bodies (APA, ACA, NIMH), and peer-reviewed work outrank SEO content. Use
  lower-tier sources for orientation only, and say so.
- **Cite everything.** Every non-obvious claim links to a numbered source in the unit's sources file.
  **A reading with no citations is a bug.**
- **Flag uncertainty & disagreement** rather than smoothing it over — note contested, dated, or
  replication-shaky findings. (Counseling-specific: clinical claims, diagnostic boundaries, and
  "what works" are often contested — surface it.)
- **One-line authority note** per source in the sources file (what it is, why it's trustworthy).
- This is grad-school prep: a confidently-wrong page is worse than no page.

---

## Page conventions (wiki/)

- **One concept per page.** Split if a page is doing two jobs.
- **YAML frontmatter on every page:**
  ```yaml
  ---
  title: Unconditional Positive Regard
  type: concept            # concept | theory | study | person | unit
  tags: [rogers, person-centered, microskills]
  unit: 1                  # primary unit
  source_units: [1, 2]     # units that touch this page
  cluster: rogers-conditions   # confusable group (optional)
  ---
  ```
- **Wikilinks** for cross-references: `[[concept-empathy]]`.
- **A `## Sources` section on every page**, with inline `[^n]`-style or `[n]` references resolving to
  the unit sources file.
- When a later unit complicates an earlier claim, **edit the earlier page** to flag it and note which
  unit did so (don't silently overwrite — note the tension).

---

## Item conventions (items/)

Items live in one markdown file per unit (`items/unitNN-<slug>.md`) as one or more fenced
**```json** blocks, each a JSON array of item objects. Rationale: JSON parses with Python's stdlib
(no PyYAML dependency), the apps load it trivially, and the fenced block still renders browsably in
Obsidian. The compiler (`apps/build_items.py`) extracts every ```json block and merges them. Shape:

````
```json
[
  {
    "id": "u1-upr-apply-01",
    "prompt": "A client says they relapsed and braces for judgment. You respond without approval or disapproval, conveying you still value them fully. Which Rogerian condition is this, and why is it not mere agreement?",
    "answer": "Unconditional positive regard — prizing the person independent of behavior. Not endorsing the relapse; refusing to make worth contingent on it.",
    "type": "vignette",
    "source_page": "wiki/concept-core-conditions.md",
    "topic": "rogers-conditions",
    "cluster": "rogers-conditions",
    "bloom_level": "apply"
  }
]
```
````

Field vocab: `type` ∈ cloze | recall | mcq | vignette | compare | explain ·
`bloom_level` ∈ remember | understand | apply | analyze | evaluate. For `cloze`, write the blank as
`{{...}}` in `prompt` and put the deleted text in `answer`. For `mcq`, add an `"options": [...]`
array. Scheduler state (`ease`, `interval`, `repetitions`, `due_date`) is **owned by the app**, not
authored here.

---

## Generate rules (the learning layer)

Grounded in [`learning-science-for-self-study.md`](learning-science-for-self-study.md). For each major
concept in a unit:

- **Span Bloom levels.** Don't ship only "define X." Produce remember → understand → apply → analyze →
  evaluate. Apply/Analyze items are where understanding lives and where exams concentrate. Definitions
  are the easy 30%.
- **Prefer production over recognition.** Default to **cloze** and **short free-recall**. Reserve
  **mcq** for genuine discrimination tasks ("which disorder matches this vignette?").
- **One idea per item.** Split multi-target items.
- **Always store answer/feedback with the item** so the app reveals it *after* the attempt — never
  alongside the prompt.
- **Cluster confusable concepts** (`cluster:` tag) so the app can interleave — similar disorders,
  similar theorists, similar designs, similar defense mechanisms. Counseling is rich in these.
- **Vignettes for clinical discrimination** — disorders, theories, defense mechanisms, microskill
  types. This mirrors real clinical reasoning.
- **Compare-and-contrast items** that pair confusables (interleaving baked into the item).
- **Link every item to its `source_page`** (and through it, the evidence).

---

## Apps rule

Streamlit apps in `apps/` **read** `items/build/items.json`, **write** attempts to `review_log.csv`,
and **never** modify readings or item source. Build order: quiz runner + scheduler first (80% of the
value), then workbook mode, then calibration dashboard. Scheduler: started on **Leitner** (get the
loop running), now **upgraded to SM-2** (per-item easiness + adaptive interval). Legacy box-state is
migrated transparently on load; the self-grades map to SM-2 quality `q` (missed→2, shaky→3, correct→5).

---

## Bookkeeping files

- **`index.md`** — content catalog: every reading and every quiz/item set, with a link and one-line
  summary, organized by unit. Read this first when answering a `query`.
- **`coverage.md`** — units created vs. pending; per-concept map of which item types / Bloom levels
  exist; cluster coverage. The `lint` pass updates this.
- **`log.md`** — append-only, chronological, greppable. Prefix convention:
  `## [YYYY-MM-DD] <op> | Unit N <name> | <counts>`.

---

## `lint`

Health-check both layers and update `coverage.md`.
- **Readings:** contradictions, stale claims a newer unit superseded, orphan pages, missing concept
  pages, missing cross-references, **thin/missing citations**.
- **Learning layer:** concepts with no items, topics with only "define"-level items, confusable
  clusters with no compare-and-contrast prompts, items whose `source_page` has changed since.

---

## Counseling-specific notes

- The syllabus is ordered by **clinical payoff**, not the usual academic sequence. Tier 1 (Units 1–4)
  first. Respect that ordering in suggestions.
- The human comes from CS — strong on stats/research (Unit 12) and protocols; the *stance* shift
  (resisting the urge to "fix") is the hard part. Generate items that probe stance, not just facts,
  where the material allows.
- Map units to **CACREP** core areas where relevant; programs test these.
- Unit 8 (crisis/suicide/trauma) is emotionally heavy. Keep generated material clinical and precise;
  no sensationalism.
