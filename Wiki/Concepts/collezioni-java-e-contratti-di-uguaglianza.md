---
title: "Collezioni Java e contratti di uguaglianza"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/collections-e-oggetti-java]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "equals e hashCode"
source_locator: "Pagine 18-19"
related:
  - "[[Wiki/Concepts/tabella-hash]]"
  - "[[Wiki/Concepts/visite-e-cammini-nei-grafi]]"
---

# Collezioni Java e contratti di uguaglianza

Gli attributi che identificano un oggetto devono essere coerenti fra `equals` e `hashCode`. Per oggetti in un insieme ordinato, `compareTo` applica i criteri richiesti e deve rispettare l'uguaglianza rilevante per `TreeSet`.

`ArrayList` serve per sequenze indicizzate, `HashSet` per unicità e visitati, `HashMap` per associazioni chiave-valore e `ArrayDeque` per code, deque e pile. Una `PriorityQueue` non si riordina automaticamente quando cambia la priorità interna di un elemento già inserito.
