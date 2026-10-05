---
title: "Grafi, visite, Prim e Dijkstra"
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
  - "Algoritmi sui grafi"
source_locator: "Pagine 13-16"
related:
  - "[[Wiki/Concepts/visite-e-cammini-nei-grafi]]"
  - "[[Wiki/Topics/collections-e-oggetti-java]]"
---

# Grafi, visite, Prim e Dijkstra

Un grafo può usare liste di adiacenza, con un nodo associato a un insieme di archi, oppure una matrice. In un grafo non orientato un arco è registrato per entrambi gli estremi e il conteggio aumenta una sola volta. La rimozione di un nodo richiede prima la rimozione degli archi incidenti; in un grafo orientato vanno considerati anche gli archi entranti. Uguaglianza e hash degli archi devono rispettare la direzione.

La BFS usa una coda, colori, distanze intere e predecessori: marca un nodo prima di accodarlo e restituisce il minimo numero di archi dalla sorgente. La DFS usa ricorsione, colori, predecessori e tempi di entrata/uscita; la visita completa riparte da ogni nodo bianco.

Prim sceglie l'arco più leggero che collega un nodo all'albero, perciò confronta il solo peso dell'arco con la priorità del vicino. Dijkstra richiede pesi non negativi e confronta invece la distanza di u più il peso dell'arco con la distanza del vicino. In entrambi i casi previous permette di ricostruire il risultato; in Dijkstra si risale dalla destinazione alla sorgente e si inverte la sequenza.
