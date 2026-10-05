---
title: RAG, allineamento e rischi degli LLM
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
  - RLHF
  - Retrieval-augmented generation
---

# RAG, allineamento e rischi degli LLM

L'allineamento mira a rendere il comportamento del modello utile e sicuro; la fonte presenta supervised fine-tuning e RLHF, nel quale le preferenze umane addestrano un reward model usato per ottimizzare il modello principale.

RAG combina query, retrieval di documenti e generazione condizionata dai documenti recuperati. Può ancorare le risposte a fonti e informazioni aggiornate, ma il retrieval può essere rumoroso e una pipeline richiede progettazione e validazione.

Allucinazioni, bias, prompt injection, jailbreaking e dati sensibili sono rischi indicati dalle fonti. Tra le mitigazioni riportate: controllo del contesto, validazione, filtri di output, logging, audit e supervisione umana.
