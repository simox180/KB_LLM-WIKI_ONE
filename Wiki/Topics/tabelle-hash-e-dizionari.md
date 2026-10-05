---
title: "Tabelle hash e dizionari"
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
source_locator: "Pagine 9-10"
related:
  - "[[Wiki/Concepts/tabella-hash]]"
  - "[[Wiki/Concepts/iteratore-fail-fast]]"
  - "[[Wiki/Topics/collections-e-oggetti-java]]"
---

# Tabelle hash e dizionari

Nel chaining la tabella mantiene bucket, liste di nodi, dimensione, capacità, fattore di carico e funzione hash. Ricerca, inserimento e rimozione lavorano nella lista del bucket calcolato con la capacità corrente. Se una crescita richiede rehash, ogni elemento deve ricevere un nuovo indice: copiare i bucket nelle stesse posizioni non è corretto. Una variante dizionario confronta e calcola l'hash sulla chiave; put sostituisce il valore quando la chiave esiste senza incrementare la dimensione.

Nell'indirizzamento aperto, ricerca e inserimento devono usare la medesima sequenza di probing e un limite di tentativi. Se è supportata la rimozione, una cella cancellata è distinta da una mai occupata: assegnare direttamente null interromperebbe le ricerche oltre una collisione. L'inserimento ricorda il primo slot cancellato, ma continua a cercare possibili duplicati.

Il rehash a indirizzamento aperto reinserisce soltanto le celle occupate nella nuova tabella e non copia i marcatori di cancellazione. Nel probing quadratico e nel doppio hashing cambiano gli indici generati, ma ricerca e inserimento devono usare gli stessi parametri.
