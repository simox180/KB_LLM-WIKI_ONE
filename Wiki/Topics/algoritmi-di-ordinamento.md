---
title: "Algoritmi di ordinamento"
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
  - "Ordinamenti"
source_locator: "Pagine 11-12"
related:
  - "[[Wiki/Concepts/algoritmi-di-ordinamento]]"
  - "[[Wiki/Topics/heap-e-code-di-priorita]]"
---

# Algoritmi di ordinamento

Insertion sort estrae la chiave dalla posizione corrente, sposta a destra gli elementi maggiori e la reinserisce; non spostare gli uguali conserva la stabilità. Bubble sort confronta coppie adiacenti nel tratto attivo, lo accorcia dopo ogni passaggio e può terminare se un passaggio non effettua scambi.

Merge sort divide ricorsivamente fino a sequenze di al più un elemento e fonde con due indici. Nella fusione, scegliere l'elemento della metà sinistra in caso di uguaglianza mantiene l'ordinamento stabile. Per ordinare in senso decrescente si inverte il confronto; per gli oggetti, il confronto richiesto deve essere applicato coerentemente.

QuickSort usa qui un pivot in fondo e una frontiera che separa i valori minori da quelli rimanenti. Dopo la scansione, il pivot viene scambiato nella frontiera e le chiamate ricorsive escludono quella posizione. Con pivot casuale o mediana di tre, il candidato viene prima portato in fondo e si applica la stessa partizione.
