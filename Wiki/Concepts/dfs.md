---
title: "DFS"
tags: ["concept"]
topics: ["[[Wiki/Topics/grafi-visite-e-cammini-minimi]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["Depth-first search"]
source_locator: "Pagina 14"
related: ["[[Wiki/Concepts/bfs]]"]
---

# DFS

La DFS completa inizializza tutti i nodi bianchi e avvia la visita ricorsiva da ogni nodo ancora non scoperto. All'ingresso marca il nodo grigio e registra il tempo; per ogni vicino bianco imposta il predecessore e visita ricorsivamente. Dopo i vicini, il nodo diventa nero e riceve il tempo di uscita. Non garantisce il minimo numero di archi.
