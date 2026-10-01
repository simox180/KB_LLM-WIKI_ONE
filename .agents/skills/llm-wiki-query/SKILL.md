---
name: llm-wiki-query
description: Answer LLM Wiki questions with catalog-first retrieval and source-grounded claims.
---

# LLM Wiki query

Use this skill when finding or answering knowledge-base content.

1. Search `Wiki/catalog.jsonl` first.
2. Prefer the matching compiled notes under `Wiki/` as the answer context.
3. Open Raw material only when needed to verify a claim, resolve a gap, or locate a source passage; avoid broad Raw scans.
4. Keep a distinction between a sourced fact, a synthesis, and an uncertainty.
5. Do not fabricate citations or make unsupported claims. State when the available sources do not establish an answer.
6. If the query reveals reusable missing knowledge, create it only under `Wiki/`, with valid frontmatter and one or more `Raw/` sources.

Do not modify Raw sources merely to make a query easier to answer.
