---
title: "Contratti di uguaglianza Java"
tags: ["concept"]
topics: ["[[Wiki/Topics/collections-e-oggetti-java]]"]
status: seed
created: 2026-10-05
updated: 2026-10-05
sources: ["[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"]
source_count: 1
aliases: ["equals e hashCode"]
source_locator: "Pagine 18-19"
related: ["[[Wiki/Concepts/ordinamento-naturale-e-treeset]]"]
---

# Contratti di uguaglianza Java

Gli attributi che identificano un oggetto devono essere usati coerentemente in `equals` e `hashCode`: oggetti uguali producono lo stesso hash. In `HashSet` e `HashMap` non vanno modificati, mentre l'oggetto è memorizzato, i campi che determinano identità.
