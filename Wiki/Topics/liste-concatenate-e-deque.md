---
title: "Liste concatenate, deque e liste ricorsive"
tags:
  - "topic"
topics: []
status: seed
created: 2026-10-05
updated: 2026-10-05
sources:
  - "[[Raw/Sources/mappe-operative-laboratorio-pagine-1-e-4-19.md]]"
source_count: 1
aliases: []
source_locator: "Pagine 4-6"
related:
  - "[[Wiki/Concepts/liste-concatenate-e-deque]]"
  - "[[Wiki/Concepts/iteratore-fail-fast]]"
  - "[[Wiki/Topics/collections-e-oggetti-java]]"
---

# Liste concatenate, deque e liste ricorsive

Una lista semplicemente concatenata mantiene head, tail, size e nodi con item e next. Per accedere, sostituire o rimuovere un elemento l'indice deve essere compreso tra 0 e size - 1; per inserire è ammesso anche size. Inserire in testa aggiorna anche tail se la lista era vuota; inserire in fondo può essere O(1) se tail è disponibile. Una rimozione deve aggiornare estremità e dimensione, azzerando entrambe le estremità quando la lista diventa vuota.

Nella deque doppiamente concatenata, head, tail, next e previous permettono operazioni alle estremità in O(1). Per rimuovere tutte le occorrenze, il prossimo nodo va salvato prima di scollegare quello corrente. L'inversione della lista semplice reindirizza progressivamente next; nella lista doppia si scambiano next e previous per ogni nodo e infine head e tail.

Un iteratore fail-fast conserva il prossimo nodo e il contatore atteso delle modifiche: next segnala modifiche concorrenti o fine sequenza con le eccezioni previste. Per una lista ricorsiva immutabile, ogni trasformazione lavora su first() e rest() e ricostruisce il risultato con cons; il caso base non invoca first o rest sulla lista vuota.
