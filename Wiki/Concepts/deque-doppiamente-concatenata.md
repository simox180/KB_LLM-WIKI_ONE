---
title: "Deque doppiamente concatenata"
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
  - "SimpleDequeue"
source_locator: "Pagina 5"
related:
  - "[[Wiki/Concepts/lista-semplicemente-concatenata]]"
---

# Deque doppiamente concatenata

La deque mantiene `head`, `tail`, `size` e nodi con `next` e `previous`, rendendo le operazioni alle estremità O(1). Quando si aggiunge o estrae un elemento, vanno aggiornati i collegamenti reciproci e, per l'unico nodo, entrambe le estremità. Nella rimozione di più occorrenze si salva il nodo successivo prima di scollegare quello corrente.

L'inversione di una lista doppia scambia `next` e `previous` in ogni nodo e infine `head` e `tail`.
