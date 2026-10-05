---
title: "Visite e cammini nei grafi"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/grafi-visite-e-cammini-minimi]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "BFS"
  - "DFS"
  - "Dijkstra"
  - "Prim"
source_locator: "Pagine 13-16"
related:
  - "[[Wiki/Concepts/collezioni-java-e-contratti-di-uguaglianza]]"
---

# Visite e cammini nei grafi

La BFS marca un nodo prima di accodarlo e, con distanze e predecessori, trova il minimo numero di archi dalla sorgente. La DFS usa ricorsione, colori e tempi di entrata e uscita; la visita completa riparte da ciascun nodo ancora non scoperto.

Prim confronta il peso del singolo arco con la priorità del vicino per costruire un albero ricoprente minimo. Dijkstra richiede pesi non negativi e confronta invece la distanza già raggiunta più il peso dell'arco; i predecessori consentono di ricostruire un cammino minimo.
