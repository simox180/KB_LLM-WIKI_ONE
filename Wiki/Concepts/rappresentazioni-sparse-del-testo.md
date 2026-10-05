---
title: Rappresentazioni sparse del testo
tags:
  - concept
topics:
  - "[[Wiki/Topics/elaborazione-del-linguaggio-naturale]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/da-word-embeddings-a-transformer.md]]"
source_count: 1
source_locator: "pagine 2-6"
aliases:
  - Bag of Words
  - One-hot encoding
---

# Rappresentazioni sparse del testo

Bag of Words conta le occorrenze del vocabolario e ignora ordine, sintassi e semantica. One-hot encoding assegna invece un vettore binario distinto a ogni parola. Entrambe sono rappresentazioni sparse: non esprimono direttamente somiglianze semantiche o relazioni contestuali e possono avere alta dimensionalità.

Questi limiti motivano l'uso di rappresentazioni dense e distribuite, ma BoW e one-hot non sono alias: sono due tecniche mantenute insieme perché rispondono alla medesima domanda sulle rappresentazioni lessicali sparse e sulle loro limitazioni.
