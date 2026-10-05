---
title: "Invarianti di implementazione"
tags:
  - "concept"
topics:
  - "[[Wiki/Topics/metodo-operativo-implementazione]]"
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases:
  - "Invarianti di struttura"
source_locator: "Pagina 1"
related:
  - "[[Wiki/Concepts/liste-concatenate-e-deque]]"
  - "[[Wiki/Concepts/albero-binario-di-ricerca]]"
---

# Invarianti di implementazione

Prima di implementare un metodo, il contratto determina input, risultato, eccezioni, vincoli di complessità e se l'operazione modifica l'input. I casi iniziali da distinguere includono valori nulli, indici, struttura vuota, elemento assente e duplicato.

Un'operazione aggiorna soltanto lo stato che modifica: collegamenti, dimensione e contatori. Se un algoritmo viene riusato, il suo stato va reinizializzato. I confronti di valori generici usano `compareTo`, mentre l'uguaglianza nelle collezioni usa `equals`.
