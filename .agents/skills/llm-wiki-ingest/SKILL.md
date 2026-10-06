---
name: llm-wiki-ingest
description: Ingest sources into the LLM Wiki without confusing raw source material with compiled knowledge.
---

# LLM Wiki ingest

Use this skill when importing, registering, or preparing a new source.

Read `Schema/knowledge-quality.md` before compiling knowledge. It is the authoritative reference for semantic coverage and fidelity; do not duplicate or weaken its rules here.

1. Store original or binary material under `Raw/Files/`, preserving content and extension; create Markdown-only normalized or transcribed material under `Raw/Sources/`, with available provenance to the original.
2. Search `Wiki/catalog.jsonl` before broad Raw inspection. Identify existing notes to update and relevant links; keep Raw material as source material, never compiled knowledge.
3. Examine the entire normalized source, working in bounded blocks if useful. Track the portions read and compare the resulting compilation against the whole source before considering the compilation complete.
4. When text extraction is insufficient, inspect the original for images, tables, and formulas. Record only what can be verified, and make any remaining gap explicit in the compiled note where relevant.
5. Perform concept discovery over the source. Update a compatible existing Concept first; create a new independently queryable Concept only when it is autonomously significant. Use Topics as hubs rather than duplicating detailed explanations. Check aliases and multi-idea titles for granularity.
6. Compile supported reusable knowledge only in `Wiki/`, following the frontmatter schema. Preserve source links and available localizers; distinguish source content from any clearly qualified synthesis or inference.
7. Before completion, review semantic coverage against `Schema/knowledge-quality.md`, then run the structural checks in `Schema/lint-checklist.md`. A linked note is not proof that a source has been completely compiled.

Before committing, run the repository's build, lint, and source checks and resolve failures.
