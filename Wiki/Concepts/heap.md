---
title: "Heap"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/heap-e-code-di-priorita]]"
status: seed
created: 2026-10-02
updated: 2026-10-02
sources:
  - "[[Raw/Sources/heap-e-heapsort.md]]"
source_count: 1
aliases: []
source_locator: "Pagina 2"
related:
  - "[[Wiki/Concepts/heapsort]]"
---

# Heap

Un heap può essere mantenuto in un `ArrayList<E>` oppure in un array con dimensione logica `n`. Nel MinHeap deve salire l'elemento più piccolo; nel MaxHeap quello più grande.

Con indici da 0, il padre di `i` è `(i-1)/2` per `i>0`; i figli sono `2*i+1` e `2*i+2`. Un figlio esiste se il suo indice è minore di `n`.

## Operazioni

- `heapifyUp(i)` confronta un elemento con il padre e, se deve precederlo, li scambia continuando dal padre.
- `heapifyDown(i, n)` confronta l'elemento con i figli esistenti, lo scambia con il figlio scelto se necessario e ripete da quel figlio.
- `buildHeap` parte da `n/2-1` e applica `heapifyDown` fino all'indice 0; la costruzione dal basso richiede `O(n)`.
- `insert` aggiunge in fondo e applica `heapifyUp` sull'ultimo indice.
- La lettura della radice restituisce `heap[0]`; l'estrazione sostituisce la radice con l'ultimo elemento rimasto e applica `heapifyDown(0, n)`.

`isMinHeap` verifica che ogni padre sia `<=` ai figli esistenti; `isMaxHeap` usa `>=`. Per cercare il massimo in un MinHeap, o il minimo in un MaxHeap, si scorrono le foglie da `n/2` a `n-1`, dopo aver gestito il caso vuoto.
