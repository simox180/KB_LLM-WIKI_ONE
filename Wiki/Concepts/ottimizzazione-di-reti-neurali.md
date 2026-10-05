---
title: Ottimizzazione di reti neurali
tags:
  - concept
topics:
  - "[[Wiki/Topics/machine-learning-e-reti-neurali]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/fondamenti-nlp-e-deep-learning.md]]"
  - "[[Raw/Sources/introduzione-al-machine-learning.md]]"
source_count: 2
source_locator:
  - "fondamenti-nlp-e-deep-learning: pagine 6-7"
  - "introduzione-al-machine-learning: pagine 13, 15-19"
aliases:
  - Backpropagation
  - Gradient descent
---

# Ottimizzazione di reti neurali

L'addestramento esegue un forward pass, calcola una loss, propaga i gradienti all'indietro con la regola della catena e aggiorna i pesi. La loss esprime la distanza dall'obiettivo; le fonti associano MSE alla regressione e cross-entropy alla classificazione.

Gradient descent aggiorna i parametri nella direzione opposta al gradiente. SGD usa minibatch per ridurre il costo del gradiente completo, mentre Adam adatta il learning rate usando medie dei gradienti e dei loro quadrati. Nei network profondi la moltiplicazione di derivate può produrre gradienti molto piccoli; le fonti richiamano le connessioni residue come risposta architetturale a questo problema.
