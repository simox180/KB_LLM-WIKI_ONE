---
title: "Implementare heap e coda di priorità"
tags:
  - "project"
topics:
  - "[[Wiki/Topics/heap-e-code-di-priorita]]"
status: seed
created: 2026-10-02
updated: 2026-10-02
sources:
  - "[[Raw/Sources/heap-e-heapsort.md]]"
source_count: 1
aliases: []
source_locator: "Pagine 2-3"
related:
  - "[[Wiki/Concepts/heap]]"
  - "[[Wiki/Concepts/heapsort]]"
  - "[[Wiki/Concepts/coda-di-priorita]]"
---

# Implementare heap e coda di priorità

## Ambito indicato dalla fonte

- Implementare `heapifyUp`, `heapifyDown`, `buildHeap`, inserimento, lettura ed estrazione della radice.
- Usare queste operazioni per HeapSort, con heap di lavoro o parte attiva dell'array.
- Gestire nodi valore-priorità e l'aggiornamento della priorità nella coda.

## Vincoli richiamati

- Rispettare il contratto sul caso vuoto.
- Distinguere dimensione e capacità.
- Prima di modificare la coda, controllare le condizioni previste dal tutorato per `clear()` e `add()`.
