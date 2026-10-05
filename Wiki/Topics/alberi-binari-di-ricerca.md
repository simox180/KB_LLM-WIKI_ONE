---
title: "BST e ReverseBST"
tags:
  - "topic"
topics: []
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "Alberi binari di ricerca"
source_locator: "Pagine 7-8"
related:
  - "[[Wiki/Concepts/albero-binario-di-ricerca]]"
  - "[[Wiki/Topics/liste-concatenate-e-deque]]"
---

# BST e ReverseBST

Un BST mantiene root, dimensione e nodi con label, left, right e parent. Nel BST i valori minori sono nel sottoalbero sinistro e i maggiori nel destro; nel ReverseBST le direzioni sono invertite. Le classi descritte non ammettono duplicati: l'inserimento di una chiave presente non cambia size.

La visita in ordine di un BST produce valori crescenti; nello stesso ReverseBST produce valori decrescenti. L'altezza di un nodo nullo è -1 e quella di una foglia è 0. In un BST, minimo e massimo si trovano seguendo rispettivamente il ramo sinistro e destro; nel ReverseBST sono invertiti.

La rimozione distingue nodi con zero, uno o due figli. Per due figli si copia nel nodo il valore del successore e si rimuove il successore dalla sua posizione originale, dove ha al massimo un figlio. Il successore in un BST è il minimo del sottoalbero destro, se esiste; altrimenti si risale finché si proviene da un figlio sinistro. In un ReverseBST queste direzioni si invertono, ma “successore” resta il valore immediatamente maggiore.
