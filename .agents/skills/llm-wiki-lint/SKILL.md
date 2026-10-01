---
name: llm-wiki-lint
description: Validate LLM Wiki structure, metadata, provenance, and pre-commit checks.
---

# LLM Wiki lint

Use this skill before commits and when validating a Wiki change.

1. Run the repository's build, lint, and source-check commands when they are available.
2. Apply every item in `Schema/lint-checklist.md`; use it as the manual fallback while automation is absent.
3. Verify each changed `Wiki/` note has valid frontmatter according to `Schema/frontmatter-schema.md`.
4. Verify `sources` is non-empty and each target is an existing file under `Raw/`.
5. Check that citations and factual claims are supported by those sources; reject invented or unverifiable citations.
6. Check filenames, tags, paths, and metadata keys against `Schema/naming-conventions.md`.

Report failures clearly and do not represent the change as ready to commit until build, lint, and source checks pass.
