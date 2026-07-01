#!/usr/bin/env python3
"""Compile the item source (items/*.md) into items/build/items.json.

Source of truth = markdown files in items/, each containing one or more fenced ```json blocks,
where every block is a JSON array of item objects. This compiler extracts every json block, merges
them, validates required fields and the controlled vocab, checks id uniqueness and that each
source_page exists, then writes the merged bank.

Stdlib only (no PyYAML) so it runs on a bare Python install. Run from anywhere:
    python apps/build_items.py
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ITEMS_DIR = ROOT / "items"
OUT = ITEMS_DIR / "build" / "items.json"

REQUIRED = ("id", "prompt", "answer", "type", "source_page", "topic", "bloom_level")
TYPES = {"cloze", "recall", "mcq", "vignette", "compare", "explain"}
BLOOM = {"remember", "understand", "apply", "analyze", "evaluate"}

FENCE = re.compile(r"```json\s*(.*?)```", re.DOTALL)
CLOZE_BLANK = re.compile(r"\{\{.*?\}\}")
UNIT_FILE = re.compile(r"^unit0*(\d+)\b")
AUX_FILE = re.compile(r"^aux-(.+)$")


def unit_of(src: Path) -> str:
    """Derive an item's unit label from its source filename — the directory convention is
    the source of truth: items/unitNN-<slug>.md -> "NN", items/aux-<slug>.md -> "aux-<slug>".
    This lets the apps filter by unit without an extra per-item field."""
    stem = src.stem
    m = UNIT_FILE.match(stem)
    if m:
        return m.group(1)
    m = AUX_FILE.match(stem)
    if m:
        return f"aux-{m.group(1)}"
    return stem


def extract_blocks(md_text: str, src: Path) -> list[dict]:
    items: list[dict] = []
    unit = unit_of(src)
    for i, block in enumerate(FENCE.findall(md_text)):
        try:
            data = json.loads(block)
        except json.JSONDecodeError as e:
            sys.exit(f"ERROR: {src.name} json block #{i + 1}: invalid JSON — {e}")
        if not isinstance(data, list):
            sys.exit(f"ERROR: {src.name} json block #{i + 1}: expected a JSON array")
        for it in data:
            # Stamp unit from the filename unless the item already declares one (explicit wins).
            it.setdefault("unit", unit)
        items.extend(data)
    return items


def validate(items: list[dict]) -> list[str]:
    problems: list[str] = []
    seen: set[str] = set()
    for it in items:
        iid = it.get("id", "<no id>")
        for field in REQUIRED:
            if not it.get(field):
                problems.append(f"{iid}: missing required field '{field}'")
        if it.get("id") in seen:
            problems.append(f"{iid}: duplicate id")
        seen.add(it.get("id"))
        if it.get("type") not in TYPES:
            problems.append(f"{iid}: bad type '{it.get('type')}' (allowed: {sorted(TYPES)})")
        if it.get("bloom_level") not in BLOOM:
            problems.append(f"{iid}: bad bloom_level '{it.get('bloom_level')}'")
        sp = it.get("source_page")
        if sp and not (ROOT / sp).exists():
            problems.append(f"{iid}: source_page not found -> {sp}")
        if it.get("type") == "mcq":
            if not it.get("options"):
                problems.append(f"{iid}: type 'mcq' requires an 'options' array")
            # The exact correct option must be identified and present verbatim in options,
            # otherwise the app can't auto-grade the radio selection (answer carries extra
            # explanation text that won't match any option).
            if not it.get("correct"):
                problems.append(f"{iid}: type 'mcq' requires a 'correct' field (exact option string)")
            elif it.get("options") and it["correct"] not in it["options"]:
                problems.append(f"{iid}: 'correct' is not one of 'options'")
        # cloze well-formedness: a cloze must have a {{...}} blank so the app can hide it;
        # any other type with a {{...}} is a mis-tagged cloze (the answer would show in the prompt).
        has_blank = bool(CLOZE_BLANK.search(it.get("prompt") or ""))
        if it.get("type") == "cloze" and not has_blank:
            problems.append(f"{iid}: type 'cloze' but prompt has no {{{{...}}}} blank "
                            f"(the answer would show in the question)")
        if it.get("type") != "cloze" and has_blank:
            problems.append(f"{iid}: non-cloze prompt contains a {{{{...}}}} blank "
                            f"(tag it 'cloze' or remove the braces)")
    return problems


def main() -> None:
    # Compile both syllabus units (unit*.md) and off-spine elective modules (aux*.md).
    # Skip README.md and anything under build/. See the "Ad-hoc / elective modules" section of CLAUDE.md.
    sources = sorted(p for p in ITEMS_DIR.glob("*.md") if p.name != "README.md")
    if not sources:
        sys.exit("No item source files found (items/unit*.md or items/aux*.md).")

    all_items: list[dict] = []
    per_file: dict[str, int] = {}
    for src in sources:
        found = extract_blocks(src.read_text(encoding="utf-8"), src)
        per_file[src.name] = len(found)
        all_items.extend(found)

    problems = validate(all_items)
    if problems:
        print("BUILD FAILED — fix these and re-run:\n  - " + "\n  - ".join(problems))
        sys.exit(1)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(all_items, indent=2, ensure_ascii=False), encoding="utf-8")

    # summary
    by_bloom: dict[str, int] = {}
    for it in all_items:
        by_bloom[it["bloom_level"]] = by_bloom.get(it["bloom_level"], 0) + 1
    print(f"Built {OUT.relative_to(ROOT)} — {len(all_items)} items from {len(sources)} file(s).")
    for name, n in per_file.items():
        print(f"  {name}: {n}")
    print("  Bloom spread: " + ", ".join(f"{k}={by_bloom.get(k, 0)}" for k in
          ("remember", "understand", "apply", "analyze", "evaluate")))


if __name__ == "__main__":
    main()
