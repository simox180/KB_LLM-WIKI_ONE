---
title: "Catena di matrici"
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
  - "Moltiplicazione a catena di matrici"
source_locator: "Pagina 17"
related:
  - "[[Wiki/Concepts/programmazione-dinamica-per-catena-di-matrici]]"
---

# Catena di matrici

Nel problema della catena di matrici, il vettore p ha lunghezza n + 1 e la matrice Aᵢ ha dimensioni p[i] × p[i+1]. La tabella m[i][j] conserva il costo minimo del sottoproblema, mentre b[i][j] memorizza l'indice di separazione ottimale.

Le celle diagonali hanno costo zero. Si riempie la tabella per lunghezze crescenti della catena, provando ogni separazione k tra i e j e calcolando m[i][k] + m[k+1][j] + p[i] × p[k+1] × p[j+1]. Il costo complessivo è m[0][n-1].

Per ricostruire la parentesizzazione, traceBack(i, j) restituisce la matrice quando i == j; altrimenti legge b[i][j], ricostruisce i due sottoproblemi e li combina. La ricostruzione non ricalcola il minimo.
