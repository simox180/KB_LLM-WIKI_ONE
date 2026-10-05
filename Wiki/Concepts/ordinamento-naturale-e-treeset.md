---
title: "Ordinamento naturale e TreeSet"
tags: ["concept"]
topics: ["[[Wiki/Topics/collections-e-oggetti-java]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["compareTo"]
source_locator: "Pagine 18-19"
related: ["[[Wiki/Concepts/contratti-di-uguaglianza-java]]"]
---

# Ordinamento naturale e TreeSet

`compareTo` applica prima il criterio principale e poi quello secondario. In un `TreeSet` un confronto uguale a zero identifica un duplicato, quindi l'ordinamento deve essere coerente con l'uguaglianza rilevante e i suoi campi non vanno modificati mentre l'oggetto è nell'insieme.
