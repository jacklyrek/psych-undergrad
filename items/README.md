# items/ — the learning layer (source of truth)

Markdown-with-YAML, one file per unit: `unitNN-<slug>.md`, each a list of item blocks. This is the
**source of truth** I author and edit. `build/items.json` is the compiled bank the Streamlit apps
load — never hand-edit it; regenerate with `apps/build_items.py`.

Items span Bloom levels, prefer production (cloze/recall) over recognition, carry a `source_page`
link, and use `cluster` tags for interleaving. Scheduler state is owned by the app, not stored here.
See item + generate rules in [`../CLAUDE.md`](../CLAUDE.md).
