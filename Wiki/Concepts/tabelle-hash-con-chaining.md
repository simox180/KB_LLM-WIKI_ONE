---
title: "Tabelle hash con chaining"
tags: ["concept"]
topics: ["[[Wiki/Topics/tabelle-hash-e-dizionari]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["Hash table con liste di collisione"]
source_locator: "Pagina 9"
related: ["[[Wiki/Concepts/tabelle-hash-a-indirizzamento-aperto]]", "[[Wiki/Concepts/iteratore-fail-fast]]"]
---

# Tabelle hash con chaining

Nel chaining ogni bucket contiene una lista di nodi. Ricerca, inserimento e rimozione lavorano nella lista determinata dall'hash e dalla capacità corrente; l'inserimento evita duplicati confrontando con `equals`. Un rehash ricalcola il bucket di ogni elemento con la nuova capacità. Nella variante dizionario, hash e uguaglianza sono della chiave e `put` sostituisce il valore esistente senza aumentare la dimensione.
