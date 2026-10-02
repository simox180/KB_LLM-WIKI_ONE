---
title: "HeapSort"
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
source_locator: "Pagina 3, HeapSort"
related:
  - "[[Wiki/Concepts/heap]]"
---

# HeapSort

Con una classe heap, per l'ordine crescente si può estrarre da un MinHeap scrivendo da sinistra a destra, oppure da un MaxHeap scrivendo da destra a sinistra. Per l'ordine decrescente si inverte il verso di riempimento.

Quando il risultato va scritto nella lista originale senza alterare l'heap durante le estrazioni, si usa una copia dei valori in ingresso. L'estrazione si ripete finché l'heap è vuoto.

Nella variante direttamente sull'array, si costruisce l'heap, si scambia la radice con l'ultimo elemento attivo, si riduce la dimensione attiva e si ripristina la radice con `heapifyDown`. Con MaxHeap si ottiene ordine crescente; con MinHeap ordine decrescente. Il tratto già ordinato resta fuori da `heapifyDown`.
