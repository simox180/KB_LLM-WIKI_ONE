---
title: Workflow examples
tags:
  - llm-wiki
  - workflow
---

# Workflow examples

## Da fonte a nota compilata

1. Deposita il documento originale o binario in `Raw/Files/`; resta non compilato ed è ignorato da Git.
2. Crea in `Raw/Sources/` una fonte Markdown normalizzata o trascritta derivata dall'originale, indicando il file e il passaggio di provenienza quando disponibili.
3. Cerca prima in `Wiki/catalog.jsonl` se esistono note o fonti già indicizzate sul tema.
4. Esamina integralmente la fonte in `Raw/Sources/`, anche per blocchi, annotando percorso e localizzatore quando disponibile. Consulta `Raw/Files/` per verificare l'originale se testo, immagini, tabelle o formule non sono sufficienti.
5. Crea o aggiorna una nota in `Wiki/`, derivandola esclusivamente da `Raw/Sources/`, con il frontmatter previsto e almeno un link in `sources`.
6. Conserva il contenuto rilevante della fonte, scrivi solo sintesi e affermazioni supportate e marca limiti, conflitti, inferenze o parti non verificabili. Non trattare il semplice collegamento come prova di copertura completa.
7. Riesamina la compilazione rispetto a `Schema/knowledge-quality.md`; aggiorna il catalogo con gli strumenti del repository quando disponibili, quindi esegui build, lint e controlli delle fonti.

## Esempio di nota

```markdown
---
title: Strategie di chunking per documenti tecnici
tags:
  - concept
status: draft
topics:
  - "[[Wiki/Topics/retrieval]]"
sources:
  - "[[Raw/Sources/retrieval-guide.md]]"
source_count: 1
source_locator: "pp. 12-14"
created: 2026-10-02
updated: 2026-10-02
aliases: []
---

# Strategie di chunking per documenti tecnici

La fonte confronta chunk a dimensione fissa e chunk guidati dalla struttura; la scelta dipende dalla struttura del documento e dal metodo di recupero. [Fonte: pp. 12-14]
```

## Aggiornare una nota esistente

- Individua la nota e le fonti con `Wiki/catalog.jsonl` prima di esplorare `Raw/Sources/` in modo esteso.
- Conserva i link alle fonti precedenti e aggiungi solo fonti effettivamente consultate.
- Aggiorna `updated`; aggiorna `reviewed` soltanto dopo avere ricontrollato tutte le affermazioni rilevanti.
- Se una fonte non sostiene più un'affermazione, correggi o rimuovi l'affermazione invece di mantenere una citazione vaga.
