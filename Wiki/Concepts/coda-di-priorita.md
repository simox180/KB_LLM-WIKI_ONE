---
title: "Coda di priorità"
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
source_locator: "Pagina 3, Coda con priorità separata"
related:
  - "[[Wiki/Concepts/heap]]"
---

# Coda di priorità

La coda mantiene nodi con `value` e `priority`: gli scambi spostano il nodo intero e i confronti usano la priorità.

- L'inserimento crea il nodo valore-priorità, lo mette in fondo e lo fa risalire. La lettura restituisce il valore della radice; la lettura della priorità restituisce il campo `priority` della radice.
- Per modificare una priorità si individua il nodo e gli si assegna il nuovo valore: si usa `heapifyUp` se deve superare il padre, altrimenti `heapifyDown`. Nella coda di min-priorità si inverte il criterio dei confronti.
- Nel tutorato, `peak()` estrae, `getMax()` legge soltanto e `sort()` restituisce valori per priorità decrescente. Per preservare la coda si lavora su una copia.

Dimensione e capacità sono diverse. Nel tutorato `clear()` ripristina la capacità iniziale e `add()` rifiuta valore `null` e priorità negativa.
