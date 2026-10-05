---
title: Architettura e controlli per agenti LLM
tags:
  - concept
topics:
  - "[[Wiki/Topics/agenti-llm]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/agenti-llm.md]]"
source_count: 1
aliases:
  - Agente LLM
---

# Architettura e controlli per agenti LLM

La fonte descrive un agente come LLM più logica, memoria e uso di strumenti. Pianificatore, memoria, strumenti e feedback sostengono un ciclo di comprensione dell'obiettivo, pianificazione, azione, osservazione e possibile adattamento.

La memoria breve vive nel prompt o nella finestra di contesto; quella lunga è esterna, ad esempio in file, log o database vettoriale. ReAct e Plan-and-Execute sono presentati come due stili architetturali.

I controlli necessari includono limiti di passaggi contro loop, validazione e grounding contro allucinazioni, function calling e controlli sulle azioni, logging e human-in-the-loop.
