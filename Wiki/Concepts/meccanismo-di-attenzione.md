---
title: Meccanismo di attenzione
tags:
  - concept
topics:
  - "[[Wiki/Topics/transformer-e-llm]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/da-word-embeddings-a-transformer.md]]"
source_count: 1
source_locator: "pagine 9-11"
aliases:
  - Attention
  - Self-attention
---

# Meccanismo di attenzione

L'attenzione attribuisce pesi alle parti dell'input rilevanti per generare o interpretare un elemento dell'output. Nella formulazione encoder-decoder evita di comprimere tutto l'input in un unico vettore; la self-attention permette invece a ciascun token di considerare gli altri token della sequenza.

Il Transformer usa anche attenzione multi-head per esplorare più relazioni in parallelo. La fonte associa l'attenzione a contesto più preciso e a migliori risultati in traduzione e riassunto.
