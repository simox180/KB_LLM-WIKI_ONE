---
title: Naming conventions
tags:
  - llm-wiki
  - schema
---

# Naming conventions

## Directory

- `Raw/Files/`: file originali o binari (PDF, ZIP, immagini, DOCX e simili), non compilati e ignorati da Git; conserva il nome e l'estensione originali quando possibile.
- `Raw/Sources/`: fonti Markdown normalizzate o trascritte derivate dai file in `Raw/Files/` (o da originali non disponibili nel repository); sono sorgenti, non note compilate.
- `Wiki/`: conoscenza compilata e riutilizzabile, derivata esclusivamente da `Raw/Sources/`.
- `Schema/`: contratti, convenzioni ed esempi operativi.
- `.agents/skills/<skill-name>/`: istruzioni locali per gli agenti.

## File delle note Wiki

Usa kebab-case descrittivo: `argomento-specifico.md`.

- Solo lettere minuscole ASCII, numeri e trattini.
- Nessuno spazio, underscore, carattere di controllo o prefisso generico come `note-`.
- Scegli un nome stabile basato sul concetto, non su una data o sul nome del modello che ha creato la nota.
- Esempio: `strategie-di-chunking.md`.

## File Raw

Per i file originali in `Raw/Files/`, conserva, se possibile, il nome originario. Se è necessario rinominarli, usa `yyyy-mm-dd-origine-descrizione.estensione`; non modificare l'estensione e non usare un nome che faccia sembrare il file una nota compilata.

Per le fonti derivate in `Raw/Sources/`, usa un nome Markdown descrittivo in kebab-case, per esempio `strategie-di-chunking.md`, e registra nel frontmatter il riferimento all'originale quando disponibile.

## Metadati e tag

- Chiavi frontmatter: minuscolo e `snake_case` per nomi composti.
- Valori enum: minuscolo inglese, come definiti in `frontmatter-schema.md`.
- Tag: kebab-case minuscolo; per gerarchie usare `/`, per esempio `retrieval/chunking`.
- Titoli: linguaggio naturale, con maiuscole secondo la lingua della nota.
