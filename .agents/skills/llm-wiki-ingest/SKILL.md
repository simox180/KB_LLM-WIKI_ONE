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
6. After normalizing the source, always integrate its reusable knowledge into `Wiki/`. First update compatible existing `Wiki/Concepts/` notes when they cover the same concept. Create a new Concept only when no suitable one exists and the concept is autonomously significant: it can be sensibly queried on its own and has its own algorithms, behavior, invariants, constraints, or edge cases. Do not create micro-Concepts for helpers, examples, minor details, or simple variants. Treat Topics as organizational hubs: they synthesize the domain, describe relationships, and link Concepts without duplicating their detailed explanations. Update related Topic links only when necessary. Derive compiled knowledge exclusively from `Raw/Sources/` and follow `Schema/frontmatter-schema.md`.
7. Never invent a source, citation, URL, page number, timestamp, or claim.

Before committing, run the repository's build, lint, and source checks and resolve failures.
