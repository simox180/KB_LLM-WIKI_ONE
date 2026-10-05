---
title: "Tabelle hash a indirizzamento aperto"
tags: ["concept"]
topics: ["[[Wiki/Topics/tabelle-hash-e-dizionari]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["Open addressing"]
source_locator: "Pagina 10"
related: ["[[Wiki/Concepts/tabelle-hash-con-chaining]]"]
---

# Tabelle hash a indirizzamento aperto

Ricerca e inserimento percorrono la stessa sequenza di probing con un limite di tentativi. Una cella cancellata resta distinta da una mai occupata: la ricerca la supera e l'inserimento può ricordarla, ma continua a cercare un duplicato. Il rehash reinserisce soltanto le celle occupate; nel probing quadratico e nel doppio hashing il generatore degli indici deve restare identico fra ricerca e inserimento.
