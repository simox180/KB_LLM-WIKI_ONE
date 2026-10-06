---
title: Command reference
tags:
  - llm-wiki
  - tooling
---

# Command reference

Eseguire tutti i comandi dalla radice del repository con `python3 scripts/wiki_tool.py <comando>`.

| Comando | Effetto |
| --- | --- |
| `doctor` | Controllo non mutante di directory, Python, catalogo, manifest e conteggi. |
| `build` | Rigenera `Wiki/catalog.jsonl`, `Wiki/index.md` e gli indici delle sottocartelle Wiki. |
| `lint` | Valida il frontmatter delle note compilate, tag, fonti e `source_count`. |
| `source-scan` | Elenca le fonti Raw e le note Wiki idonee che le collegano; non valuta la completezza semantica. |
| `source-scan --update --accept-covered` | Rigenera il manifest dai collegamenti alle note dopo una revisione semantica esplicita. |
| `source-lint` | Valida il frontmatter Raw e impedisce fonti processate senza note Wiki idonee collegate. |
| `source-delta` | Elenca le fonti Raw assenti dal manifest. |
| `source-coverage` | Mostra le note Wiki idonee collegate a ciascuna fonte Raw; non attesta la copertura semantica. |
| `search-catalog --query "testo"` | Cerca nel catalogo già generato. |
| `log --title "titolo" --details "dettagli"` | Aggiunge una voce breve a `Wiki/log.md`. |

Il hook si installa con `sh scripts/install_hooks.sh`. Prima di un commit esegue build, lint e source-lint. Per controllare il contenuto prima di una pubblicazione, usare `python3 scripts/audit_public.py`.
