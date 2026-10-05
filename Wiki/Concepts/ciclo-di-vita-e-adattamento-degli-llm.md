---
title: Ciclo di vita e adattamento degli LLM
tags:
  - concept
topics:
  - "[[Wiki/Topics/transformer-e-llm]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/fondamenti-e-uso-responsabile-degli-llm.md]]"
source_count: 1
aliases:
  - Pretraining e fine-tuning
---

# Ciclo di vita e adattamento degli LLM

La fonte definisce un LLM come modello neurale, basato su Transformer, addestrato su grandi quantità di testo per prevedere il token successivo. Il pretraining usa obiettivi self-supervised, fra cui masked language modeling e causal language modeling, per produrre un modello generalista riutilizzabile.

Un modello può essere adattato mediante fine-tuning completo, adapter leggeri o instruction tuning; in alternativa il prompting guida il comportamento senza aggiornare i pesi. Zero-shot e few-shot differiscono per l'assenza o la presenza di esempi nel prompt.
