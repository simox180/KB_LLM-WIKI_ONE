---
title: Preparazione e regolarizzazione dei dati
tags:
  - concept
topics:
  - "[[Wiki/Topics/machine-learning-e-reti-neurali]]"
status: active
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/introduzione-al-machine-learning.md]]"
source_count: 1
source_locator: "pagine 14, 20-23"
aliases: []
---

# Preparazione e regolarizzazione dei dati

Le fonti richiedono dati corretti, standardizzati, bilanciati e separati tra training e test. La data augmentation aumenta artificialmente i dati attraverso trasformazioni controllate, ma può introdurre ipotesi a priori e va quindi usata con cautela; è distinta dai dati sintetici.

La regolarizzazione aggiunge una penalità alla loss per contrastare l'overfitting e favorire la generalizzazione, introducendo al contempo un iperparametro da calibrare.
