---
title: "Iteratore fail-fast"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/liste-concatenate-e-deque]]"
  - "[[Wiki/Topics/tabelle-hash-e-dizionari]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases: []
source_locator: "Pagine 5 e 9"
related:
  - "[[Wiki/Concepts/liste-concatenate-e-deque]]"
---

# Iteratore fail-fast

Un iteratore fail-fast conserva il prossimo elemento da restituire e il valore atteso del contatore delle modifiche strutturali. Prima di avanzare, `next` confronta i due contatori: se differiscono, segnala una modifica concorrente; se non rimangono elementi, segnala la fine della sequenza. Una sostituzione del solo valore non è normalmente una modifica strutturale.
