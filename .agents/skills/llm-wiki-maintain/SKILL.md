---
name: llm-wiki-maintain
description: Maintain compiled LLM Wiki notes, provenance, indexes, and quality over time.
---

# LLM Wiki maintain

Use this skill when revising, deprecating, reorganizing, or refreshing Wiki knowledge.

1. Start with `Wiki/catalog.jsonl`, then inspect only the relevant `Wiki/` notes and Raw sources.
2. Keep reusable knowledge in `Wiki/`; leave `Raw/Sources/` as source material.
3. Preserve or repair at least one valid Raw source link for every compiled note.
4. When a source no longer supports a claim, correct, qualify, or remove the claim and update `updated`.
5. Mark a note `deprecated` instead of silently retaining obsolete guidance; link to its replacement when one exists.
6. Keep metadata, links, names, and tags compliant with the Schema documents.
7. Regenerate or validate catalogues and indices with repository tools when available.

Before committing, run build, lint, and source checks. Never invent citations or unsupported statements to fill gaps.
