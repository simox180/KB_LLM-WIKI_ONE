---
title: Naming conventions
tags:
  - llm-wiki
  - schema
---

# Naming conventions

## Directory

- `Raw/Sources/`: fonti originali o acquisizioni non compilate.
- `Wiki/`: note compilate e riutilizzabili.
- `Schema/`: contratti, convenzioni ed esempi operativi.
- `.agents/skills/<skill-name>/`: istruzioni locali per gli agenti.

## File delle note Wiki

Usa kebab-case descrittivo: `argomento-specifico.md`.

- Solo lettere minuscole ASCII, numeri e trattini.
- Nessuno spazio, underscore, carattere di controllo o prefisso generico come `note-`.
- Scegli un nome stabile basato sul concetto, non su una data o sul nome del modello che ha creato la nota.
- Esempio: `strategie-di-chunking.md`.

## File Raw

Conserva, se possibile, il nome originario. Se è necessario rinominarlo, usa `yyyy-mm-dd-origine-descrizione.estensione`. Non modificare l'estensione e non usare un nome che faccia sembrare il file una nota compilata.

## Metadati e tag

- Chiavi frontmatter: minuscolo e `snake_case` per nomi composti.
- Valori enum: minuscolo inglese, come definiti in `frontmatter-schema.md`.
- Tag: kebab-case minuscolo; per gerarchie usare `/`, per esempio `retrieval/chunking`.
- Titoli: linguaggio naturale, con maiuscole secondo la lingua della nota.
