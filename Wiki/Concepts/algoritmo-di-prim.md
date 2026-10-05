---
title: "Algoritmo di Prim"
tags: ["concept"]
topics: ["[[Wiki/Topics/grafi-visite-e-cammini-minimi]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["Prim"]
source_locator: "Pagina 15"
related: ["[[Wiki/Concepts/algoritmo-di-dijkstra]]"]
---

# Algoritmo di Prim

Prim costruisce un albero ricoprente minimo in un grafo non orientato e pesato. Per ogni nodo conserva il peso del miglior arco che lo collega all'albero e il predecessore; aggiorna un vicino non visitato se il solo peso dell'arco è minore della sua priorità. Una priorità infinita esaurisce la componente della sorgente.
