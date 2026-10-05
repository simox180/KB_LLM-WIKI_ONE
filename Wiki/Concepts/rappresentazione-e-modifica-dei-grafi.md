---
title: "Rappresentazione e modifica dei grafi"
tags: ["concept"]
topics: ["[[Wiki/Topics/grafi-visite-e-cammini-minimi]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: []
source_locator: "Pagina 13"
related: ["[[Wiki/Concepts/contratti-di-uguaglianza-java]]"]
---

# Rappresentazione e modifica dei grafi

Un grafo può usare liste di adiacenza oppure una matrice di archi. In un grafo non orientato un arco è registrato per entrambi gli estremi ma conteggiato una sola volta; la rimozione di un nodo rimuove prima gli archi incidenti e, nel caso orientato, considera anche gli entranti. `equals` e `hashCode` degli archi rispettano la direzione.
