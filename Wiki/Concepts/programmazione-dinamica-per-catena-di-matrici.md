---
title: "Programmazione dinamica per catena di matrici"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/catena-di-matrici]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "Matrix-chain multiplication"
source_locator: "Pagina 17"
related: []
---

# Programmazione dinamica per catena di matrici

Nel problema della catena di matrici, `m[i][j]` memorizza il costo minimo per il sottoproblema da `i` a `j`, mentre `b[i][j]` conserva la separazione ottimale. Le celle diagonali valgono zero e la tabella viene riempita per lunghezze crescenti della catena.

Per ogni separazione `k`, il costo candidato è `m[i][k] + m[k+1][j] + p[i] * p[k+1] * p[j+1]`. La ricostruzione della parentesizzazione usa le separazioni in `b` senza ricalcolare il minimo.
