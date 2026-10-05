---
title: Reinforcement learning e MDP
tags:
  - concept
topics:
  - "[[Wiki/Topics/reinforcement-learning]]"
  - "[[Wiki/Topics/machine-learning-e-reti-neurali]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/introduzione-al-reinforcement-learning.md]]"
source_count: 1
aliases:
  - MDP
  - Funzioni di valore
---

# Reinforcement learning e MDP

Il reinforcement learning affronta problemi di decisione sequenziale apprendendo dall'interazione per tentativi ed errori. La fonte modella l'ambiente con uno MDP: spazio degli stati, spazio delle azioni, transizioni, ricompense, fattore di sconto e distribuzione iniziale.

Una politica seleziona le azioni dell'agente; le funzioni di valore stimano il ritorno scontato atteso per stato o per coppia stato-azione. Le equazioni di Bellman esprimono tale valore tramite ricompensa immediata e valore successivo scontato.

Le famiglie indicate comprendono metodi model-free/model-based, on-policy/off-policy, value-based, policy-based e actor-critic. La fonte cita SARSA e Q-learning come esempi di metodi value-based.
