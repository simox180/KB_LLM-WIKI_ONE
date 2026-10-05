---
title: Adattamento di LLM
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
source_locator: "pagine 13, 15-16"
aliases:
  - Fine-tuning
---

# Adattamento di LLM

Il fine-tuning specializza un LLM preaddestrato su un compito usando esempi supervisionati e aggiornando i pesi. Il full fine-tuning modifica tutti i parametri; l'adapter-based fine-tuning aggiorna moduli leggeri, come LoRA o BitFit, mantenendo i pesi originari. L'instruction tuning insegna a seguire istruzioni testuali.

Il prompting è un'alternativa di adattamento in input senza aggiornamento dei pesi, trattata in [[Wiki/Concepts/prompting-per-llm]].
