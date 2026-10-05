---
title: Metodi di reinforcement learning
tags:
  - concept
topics:
  - "[[Wiki/Topics/reinforcement-learning]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/introduzione-al-reinforcement-learning.md]]"
  - "[[Raw/Sources/fondamenti-nlp-e-deep-learning.md]]"
source_count: 2
source_locator:
  - "introduzione-al-reinforcement-learning: pagine 56-65"
  - "fondamenti-nlp-e-deep-learning: pagina 10"
aliases: []
---

# Metodi di reinforcement learning

Il reinforcement learning apprende una politica dall'interazione con l'ambiente, massimizzando ricompense, ed è utile quando la dinamica è ignota o troppo complessa da risolvere esattamente. Le fonti classificano i metodi in model-free/model-based, on-policy/off-policy, online/offline, tabulari o con approssimazione di funzione.

I metodi value-based stimano valori e una politica implicita, con SARSA e Q-learning come esempi; quelli policy-based ottimizzano direttamente una politica parametrica; gli actor-critic combinano i due approcci. RLHF applica questa famiglia al feedback umano sugli LLM.
