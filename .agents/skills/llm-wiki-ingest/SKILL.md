---
name: llm-wiki-ingest
description: Ingest sources into the LLM Wiki without confusing raw source material with compiled knowledge.
---

# LLM Wiki ingest

Use this skill when importing, registering, or preparing a new source.

1. Store original or binary material (PDF, ZIP, images, DOCX, and similar files) under `Raw/Files/`; preserve its content and extension. These files are not compiled knowledge and are ignored by Git.
2. Create Markdown-only normalized or transcribed sources under `Raw/Sources/`, derived from the originals in `Raw/Files/`; record the original file and relevant location when available.
3. Do not write summaries, conclusions, or reusable knowledge in either `Raw/Files/` or `Raw/Sources/`.
4. Search `Wiki/catalog.jsonl` before inspecting broad `Raw/Sources/` context, to detect existing coverage.
5. Record enough provenance in the `Raw/Sources/` Markdown file to let a future compiled note link back to that source and its original material or relevant location.
6. Create or update content in `Wiki/` only when the task explicitly requires compiled knowledge; derive it exclusively from `Raw/Sources/` and follow `Schema/frontmatter-schema.md`.
7. Never invent a source, citation, URL, page number, timestamp, or claim.

Before committing, run the repository's build, lint, and source checks and resolve failures.
