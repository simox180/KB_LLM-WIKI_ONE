# LLM Wiki: agent rules

## Confini della conoscenza

- Tratta `Raw/Sources/` come materiale sorgente: non è una raccolta di note compilate e non va riscritto come tale.
- Scrivi conoscenza riutilizzabile, sintesi, procedure e conclusioni solo sotto `Wiki/`.
- Ogni nota compilata in `Wiki/` deve collegarsi ad almeno una fonte in `Raw/` tramite il campo frontmatter `sources`.
- Non inventare citazioni, URL, attribuzioni o riferimenti di fonte.
- Non creare affermazioni fattuali non supportate dalle fonti collegate. Se la fonte è incompleta o incerta, dichiaralo esplicitamente.

## Ricerca e contesto

- Prima di aprire un contesto ampio in `Raw/`, cerca in `Wiki/catalog.jsonl` per individuare le note e le fonti pertinenti.
- Apri soltanto le fonti Raw necessarie a verificare o compilare la nota richiesta.
- Mantieni le citazioni abbastanza specifiche da permettere a un lettore di ritrovare il passaggio sorgente.

## Qualità e commit

- Rispetta lo schema in `Schema/frontmatter-schema.md` e le convenzioni in `Schema/naming-conventions.md`.
- Prima di ogni commit esegui build, lint e controlli delle fonti previsti dal repository; non effettuare il commit se uno di questi controlli fallisce.
- Usa `Schema/lint-checklist.md` per il controllo manuale quando gli script non sono ancora disponibili.
- Limita ogni modifica allo scopo richiesto e non procedere agli step successivi del setup senza istruzioni esplicite.
