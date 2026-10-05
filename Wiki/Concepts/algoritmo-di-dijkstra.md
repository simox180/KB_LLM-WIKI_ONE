---
title: "Algoritmo di Dijkstra"
tags: ["concept"]
topics: ["[[Wiki/Topics/grafi-visite-e-cammini-minimi]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["Dijkstra"]
source_locator: "Pagina 16"
related: ["[[Wiki/Concepts/algoritmo-di-prim]]"]
---

# Algoritmo di Dijkstra

Dijkstra richiede pesi non negativi e mantiene la distanza totale dalla sorgente e i predecessori. Rilassa gli archi confrontando `d[u] + peso(u,v)` con `d[v]`; una distanza infinita segnala nodi irraggiungibili. Il cammino si ricostruisce risalendo `previous` e invertendo la sequenza; a differenza di Prim, il confronto include la distanza già percorsa.
