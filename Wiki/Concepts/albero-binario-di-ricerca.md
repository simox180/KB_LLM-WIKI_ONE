---
title: "Albero binario di ricerca"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/alberi-binari-di-ricerca]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "BST"
  - "ReverseBST"
source_locator: "Pagine 7-8"
related:
  - "[[Wiki/Concepts/invarianti-di-implementazione]]"
---

# Albero binario di ricerca

Un BST mantiene `root`, dimensione e nodi con etichetta, figli sinistro e destro, e padre. Le chiavi minori sono a sinistra e le maggiori a destra; nel ReverseBST le direzioni sono invertite. L'inserimento di un duplicato non modifica la dimensione.

La visita in ordine produce valori crescenti nel BST. Per eliminare un nodo con due figli, si trasferisce il valore del successore e si elimina il successore, che ha al massimo un figlio. L'altezza del nodo nullo è -1 e quella di una foglia è 0.
