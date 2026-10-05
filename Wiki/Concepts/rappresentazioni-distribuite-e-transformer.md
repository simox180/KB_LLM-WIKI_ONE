---
title: Rappresentazioni distribuite e Transformer
tags:
  - concept
topics:
  - "[[Wiki/Topics/elaborazione-del-linguaggio-naturale]]"
  - "[[Wiki/Topics/transformer-e-llm]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/da-word-embeddings-a-transformer.md]]"
source_count: 1
aliases:
  - Word embeddings
  - Transformer
---

# Rappresentazioni distribuite e Transformer

Bag of Words e one-hot encoding sono rappresentazioni sparse che ignorano o non esprimono relazioni semantiche e di contesto. I word embedding sono vettori densi che rappresentano la somiglianza appresa dai contesti, ma una rappresentazione unica per parola non risolve la polisemia.

Il Transformer usa self-attention, positional encoding, multi-head attention e livelli feed-forward; sostituisce la ricorrenza con attenzione e abilita elaborazione parallela delle sequenze. Le fonti lo collegano a traduzione, sintesi, classificazione e assistenti conversazionali.
