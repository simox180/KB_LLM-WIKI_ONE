---
title: Architettura Transformer
tags:
  - concept
topics:
  - "[[Wiki/Topics/transformer-e-llm]]"
  - "[[Wiki/Topics/elaborazione-del-linguaggio-naturale]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/da-word-embeddings-a-transformer.md]]"
  - "[[Raw/Sources/fondamenti-e-uso-responsabile-degli-llm.md]]"
source_count: 2
source_locator:
  - "da-word-embeddings-a-transformer: pagine 11-13"
  - "fondamenti-e-uso-responsabile-degli-llm: pagine 6-7"
aliases:
  - Transformer
---

# Architettura Transformer

Il Transformer sostituisce la ricorrenza con livelli di attenzione. Gli elementi descritti nelle fonti sono embedding di input, positional encoding, self-attention e multi-head attention, livelli feed-forward, connessioni residue e normalizzazione; nelle configurazioni encoder-decoder l'encoder elabora l'input e il decoder genera l'output.

L'elaborazione parallela delle sequenze, il supporto del contesto lungo e la scalabilità rendono questa architettura la base indicata per molti LLM e per task come traduzione, sintesi, classificazione e dialogo.
