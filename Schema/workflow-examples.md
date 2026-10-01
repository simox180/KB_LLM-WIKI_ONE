---
title: Workflow examples
tags:
  - llm-wiki
  - workflow
---

# Workflow examples

## Da fonte a nota compilata

1. Deposita il documento originale in `Raw/Sources/` senza trasformarlo in una nota Wiki.
2. Cerca prima in `Wiki/catalog.jsonl` se esistono note o fonti già indicizzate sul tema.
3. Leggi solo le parti Raw utili, annotando percorso e localizzatore del passaggio.
4. Crea o aggiorna una nota in `Wiki/` con il frontmatter previsto e almeno un link in `sources`.
5. Scrivi solo sintesi e affermazioni supportate; marca limiti, conflitti o incertezze.
6. Aggiorna il catalogo con gli strumenti del repository quando disponibili, quindi esegui build, lint e controlli delle fonti.

## Esempio di nota

```markdown
---
title: Strategie di chunking per documenti tecnici
type: concept
status: draft
sources:
  - "[[Raw/Sources/retrieval-guide.pdf]]"
source_locator: "pp. 12-14"
created: 2026-10-02
updated: 2026-10-02
tags:
  - retrieval
  - chunking
---

# Strategie di chunking per documenti tecnici

La fonte confronta chunk a dimensione fissa e chunk guidati dalla struttura; la scelta dipende dalla struttura del documento e dal metodo di recupero. [Fonte: pp. 12-14]
```

## Aggiornare una nota esistente

- Individua la nota e le fonti con `Wiki/catalog.jsonl` prima di esplorare Raw in modo esteso.
- Conserva i link alle fonti precedenti e aggiungi solo fonti effettivamente consultate.
- Aggiorna `updated`; aggiorna `reviewed` soltanto dopo avere ricontrollato tutte le affermazioni rilevanti.
- Se una fonte non sostiene più un'affermazione, correggi o rimuovi l'affermazione invece di mantenere una citazione vaga.
