---
title: Pretraining di LLM
tags:
  - concept
topics:
  - "[[Wiki/Topics/transformer-e-llm]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/fondamenti-e-uso-responsabile-degli-llm.md]]"
  - "[[Raw/Sources/fondamenti-nlp-e-deep-learning.md]]"
source_count: 2
source_locator:
  - "fondamenti-e-uso-responsabile-degli-llm: pagine 10-12"
  - "fondamenti-nlp-e-deep-learning: pagina 9"
aliases: []
---

# Pretraining di LLM

Il pretraining costruisce un modello generalista a partire da testo grezzo con obiettivi self-supervised. Le fonti distinguono masked language modeling, in cui si predice materiale mascherato, e causal language modeling, in cui si predice il token successivo dai precedenti.

Lo scopo è apprendere pattern sintattici e semantici e rappresentazioni riutilizzabili prima dell'applicazione a task specifici.
