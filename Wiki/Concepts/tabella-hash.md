---
title: "Tabella hash"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/tabelle-hash-e-dizionari]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "Hash table"
source_locator: "Pagine 9-10"
related:
  - "[[Wiki/Concepts/iteratore-fail-fast]]"
  - "[[Wiki/Concepts/collezioni-java-e-contratti-di-uguaglianza]]"
---

# Tabella hash

Nel chaining, ricerca, inserimento e rimozione lavorano nella lista del bucket calcolato con la capacità corrente. Quando la tabella cresce, il rehash ricalcola il bucket di ogni elemento: copiare i bucket alle stesse posizioni non è corretto.

Nell'indirizzamento aperto, ricerca e inserimento usano la stessa sequenza di probing e un limite di tentativi. Una cella cancellata deve restare distinguibile da una mai occupata, altrimenti una ricerca oltre una collisione può interrompersi in modo errato. Il rehash reinserisce solo le celle occupate.
