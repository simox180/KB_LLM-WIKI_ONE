---
title: "Lista semplicemente concatenata"
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
source_locator: "Pagina 4"
related:
  - "[[Wiki/Concepts/deque-doppiamente-concatenata]]"
  - "[[Wiki/Concepts/iteratore-fail-fast]]"
---

# Lista semplicemente concatenata

Una lista semplicemente concatenata mantiene `head`, `tail`, `size` e nodi con `item` e `next`. Accesso, sostituzione e rimozione richiedono indici tra 0 e `size - 1`; l'inserimento ammette anche `size`. Inserimenti e rimozioni aggiornano estremità e dimensione una sola volta; quando la lista diventa vuota, `head` e `tail` sono entrambi `null`.

Durante una rimozione in scansione, conserva il riferimento al successivo prima di modificare `next`, così da gestire anche occorrenze consecutive.
