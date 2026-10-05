---
title: Allineamento e RLHF
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
  - "fondamenti-e-uso-responsabile-degli-llm: pagine 21-22"
  - "fondamenti-nlp-e-deep-learning: pagina 10"
aliases:
  - RLHF
  - Reinforcement Learning from Human Feedback
---

# Allineamento e RLHF

L'allineamento mira a rendere il comportamento di un LLM utile, sicuro e conforme alle aspettative umane. Le fonti presentano supervised fine-tuning su risposte umane e RLHF: persone valutano più risposte, si addestra un reward model sulle preferenze e il modello principale viene ottimizzato rispetto a quel segnale.

L'RLHF non è un alias del reinforcement learning generale: è un'applicazione dell'apprendimento per rinforzo al feedback umano sui comportamenti del modello.
