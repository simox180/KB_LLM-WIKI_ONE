# LLM Wiki: agent rules

## Confini della conoscenza

- `Raw/Files/` contiene gli originali o binari; `Raw/Sources/` contiene solo le loro fonti Markdown normalizzate o trascritte. Nessuno dei due è conoscenza compilata.
- Scrivi conoscenza riutilizzabile esclusivamente in `Wiki/`, derivandola da `Raw/Sources/`.
- Ogni nota compilata deve avere almeno una fonte esistente in `Raw/Sources/` nel frontmatter `sources`. Non inventare fonti, citazioni, URL o affermazioni non supportate.

## Scegli la procedura

- Per importare, normalizzare e compilare una fonte usa `llm-wiki-ingest`; leggi `Schema/knowledge-quality.md` e i contratti che la skill indica.
- Per cercare o rispondere a domande usa `llm-wiki-query`; parti da `Wiki/catalog.jsonl`.
- Per correggere, deprecare, riorganizzare o aggiornare conoscenza esistente usa `llm-wiki-maintain`.
- Per validare modifiche o prima di un commit usa `llm-wiki-lint` e `Schema/lint-checklist.md`.

Leggi soltanto gli schemi, le fonti e le note pertinenti all'operazione: non aprire contesti Raw ampi prima della ricerca nel catalogo.

## Qualità e commit

- Rispetta `Schema/frontmatter-schema.md` e `Schema/naming-conventions.md` quando crei o modifichi note.
- Prima di un commit esegui i controlli previsti dal repository. Non effettuare il commit se un controllo applicabile fallisce.
- Limita ogni modifica allo scopo richiesto e non proseguire il setup senza istruzioni esplicite.
