---
title: "QuickSort"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/algoritmi-di-ordinamento]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "Quick sort"
source_locator: "Pagina 12"
related:
  - "[[Wiki/Concepts/merge-sort]]"
---

# QuickSort

Con pivot nell'ultimo elemento, QuickSort mantiene una frontiera: durante la scansione porta a sinistra i valori minori del pivot, quindi scambia il pivot nella frontiera. Le chiamate ricorsive agiscono sugli intervalli ai lati, escludendo la posizione finale del pivot. Per pivot casuale o mediana di tre, il candidato viene prima spostato in fondo e si usa la stessa partizione.
