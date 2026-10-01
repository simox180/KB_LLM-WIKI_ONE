---
name: llm-wiki-ingest
description: Ingest sources into the LLM Wiki without confusing raw source material with compiled knowledge.
---

# LLM Wiki ingest

Use this skill when importing, registering, or preparing a new source.

1. Store the original material under `Raw/Sources/`; preserve its content and extension.
2. Do not write summaries, conclusions, or reusable knowledge in `Raw/`.
3. Search `Wiki/catalog.jsonl` before inspecting broad Raw context, to detect existing coverage.
4. Record enough provenance to let a future compiled note link back to the exact Raw file and relevant location.
5. Create or update content in `Wiki/` only when the task explicitly requires compiled knowledge; follow `Schema/frontmatter-schema.md`.
6. Never invent a source, citation, URL, page number, timestamp, or claim.

Before committing, run the repository's build, lint, and source checks and resolve failures.
