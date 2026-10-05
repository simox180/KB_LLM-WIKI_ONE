---
title: "Oggetti e Collections Java"
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
  - "Collections Java"
source_locator: "Pagine 18-19"
related:
  - "[[Wiki/Concepts/collezioni-java-e-contratti-di-uguaglianza]]"
  - "[[Wiki/Topics/tabelle-hash-e-dizionari]]"
  - "[[Wiki/Topics/grafi-visite-e-cammini-minimi]]"
---

# Oggetti e Collections Java

Gli attributi che identificano un oggetto devono essere usati coerentemente in equals e hashCode. Per oggetti destinati a insiemi ordinati, compareTo applica prima il criterio principale e poi il secondario e deve essere coerente con l'uguaglianza richiesta da TreeSet.

Per gli intervalli, si verificano riferimenti e ordine tra inizio e fine; l'intersezione usa il massimo degli inizi e il minimo delle fini. Nella fonte del laboratorio, un'intersezione non positiva restituisce -1 e un conflitto di prenotazione è rilevante oltre cinque minuti.

ArrayList è adatta a sequenze indicizzate; HashSet a visitati e unicità; HashMap ad associazioni chiave-valore; ArrayDeque a code, deque e pile. TreeSet mantiene elementi unici ordinati; Iterator permette la rimozione durante la visita quando supportata. Una PriorityQueue non si riordina automaticamente se si modifica la priorità interna di un elemento già inserito.
