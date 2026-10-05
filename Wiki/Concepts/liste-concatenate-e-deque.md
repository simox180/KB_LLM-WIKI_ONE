---
title: "Liste concatenate e deque"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/liste-concatenate-e-deque]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "Linked list"
source_locator: "Pagine 4-6"
related:
  - "[[Wiki/Concepts/invarianti-di-implementazione]]"
  - "[[Wiki/Concepts/iteratore-fail-fast]]"
---

# Liste concatenate e deque

Una lista semplicemente concatenata mantiene `head`, `tail`, `size` e nodi con `item` e `next`. Inserimento e rimozione devono aggiornare estremità e dimensione in modo coerente; quando la lista diventa vuota, entrambe le estremità sono `null`.

Una deque doppiamente concatenata aggiunge `previous`: le operazioni alle due estremità sono O(1). Prima di scollegare un nodo durante una scansione, va conservato il riferimento al nodo successivo.

Nelle liste ricorsive immutabili, le trasformazioni operano su `first()` e `rest()` e restituiscono una nuova lista, ricostruita con `cons`; il caso base non invoca `first()` o `rest()` sulla lista vuota.
