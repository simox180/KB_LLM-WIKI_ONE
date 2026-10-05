# KB_LLM-WIKI_ONE

Knowledge base personale costruita in Obsidian e gestita con Git/GitHub.

L'obiettivo del progetto � creare una LLM Wiki strutturata, interrogabile e mantenibile, separando le fonti grezze dalla conoscenza compilata.

## Struttura principale

- `Raw/Files/`  file originali o binari (PDF, ZIP, immagini, DOCX ecc.), non compilati e ignorati da Git
- `Raw/Sources/`  fonti Markdown normalizzate o trascritte derivate dagli originali, usate come sorgenti dalla Wiki
- `Wiki/`  conoscenza compilata e riutilizzabile derivata esclusivamente da `Raw/Sources/`
- `Schema/`  regole, convenzioni e controlli
- `_templates/`  template delle note
- `.agents/skills/`  skill usate dagli agenti
- `scripts/`  strumenti di manutenzione e validazione

## Workflow

1. Depositare gli originali in `Raw/Files/` (ignorati da Git)
2. Creare o aggiornare in `Raw/Sources/` la fonte Markdown normalizzata o trascritta, con il riferimento all'originale quando presente
3. Compilare la conoscenza in `Wiki/` esclusivamente dalle fonti in `Raw/Sources/`
4. Collegare ogni nota Wiki alle rispettive fonti in `Raw/Sources/`
5. Ricostruire indici e cataloghi
6. Eseguire i controlli prima dei commit


## Ispirazione generale

- [Wanderloots — LLM Wiki Core Setup](https://github.com/wanderloots-tutorials/vibe-coding/blob/main/wanderloots-llm-wiki-core-setup-v1.0.0.md)

## Skills installate

- [Kepano — Obsidian Skills](https://github.com/kepano/obsidian-skills)
