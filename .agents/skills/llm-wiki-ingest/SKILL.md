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


8. Before creating or updating compiled knowledge, perform a concept-discovery
pass over the normalized source or source corpus.

9. Treat each independently queryable idea, algorithm, method, architecture,
task, or mechanism as a Concept candidate.

10. A Concept should normally answer one primary standalone question.
If a proposed Concept contains multiple independently searchable ideas,
split them and use a Topic to connect them.

11. Aliases must be alternative names for the same concept. If an alias names
an independently meaningful idea, evaluate it as a separate Concept instead.

12. Titles combining multiple ideas with "and", commas, or slashes require an
explicit granularity check before the Concept is created.

Before committing, run the repository's build, lint, and source checks and resolve failures.
