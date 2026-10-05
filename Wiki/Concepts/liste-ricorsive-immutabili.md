---
title: "Liste ricorsive immutabili"
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
  - "ADTConsList"
source_locator: "Pagina 6"
related: []
---

# Liste ricorsive immutabili

Una trasformazione su `ADTConsList` tratta il caso della lista vuota senza chiamare `first()` o `rest()`, decide l'azione sul primo elemento e richiama sé stessa sul resto. Se conserva il primo elemento, ricostruisce il risultato con `cons`; ogni modifica logica restituisce quindi una nuova lista.

`append` restituisce la seconda lista al caso base; `reverse` ottenuto con `append` ha costo O(n²), mentre un accumulatore costruito con `cons` permette O(n), se ammesso.
