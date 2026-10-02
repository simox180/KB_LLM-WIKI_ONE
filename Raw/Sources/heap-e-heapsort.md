---
Title: "Heap, HeapSort e code di priorità"
Author: ""
Reference: "Raw/Files/Mappe_operative_laboratorio_ASD.pdf — pagine 2-3"
ContentType:
  - "markdown"
Created: 2026-10-02
Processed: true
tags:
  - "source"
---

# Heap, HeapSort e code di priorità

Trascrizione delle pagine 2-3 di `Raw/Files/Mappe_operative_laboratorio_ASD.pdf`.

## Pagina 2 — Heap: costruire e mantenere

### Una base comune per MinHeap e MaxHeap

#### Cosa mantenere

- Un `ArrayList<E>` heap oppure un array con dimensione logica `n`. Nel MinHeap deve salire l'elemento più piccolo; nel MaxHeap quello più grande.
- Con indici da 0: padre `(i-1)/2` per `i>0`, sinistro `2*i+1`, destro `2*i+2`. Un figlio esiste solo se il suo indice è minore di `n`.

#### Operazioni da implementare

1. `heapifyUp(i)`. Finché `i` non è la radice, confronta l'elemento con il padre. Se deve precederlo, scambiali e continua dall'indice del padre; altrimenti termina.
2. `heapifyDown(i, n)`. Parti scegliendo `i` come migliore. Confrontalo con il figlio sinistro, se esiste, poi confronta il migliore ottenuto con il destro. Se rimane `i`, termina; altrimenti scambia con il figlio scelto e ripeti da quel figlio.
3. `buildHeap`. Copia o usa la sequenza secondo la consegna. Parti dall'ultimo nodo interno, `n/2-1`, e chiama `heapifyDown` per tutti gli indici fino a 0. La costruzione dal basso richiede `O(n)`.
4. `insert`. Aggiungi l'elemento in fondo e richiama `heapifyUp` sull'ultimo indice. Con un array, amplia prima la capacità se lo spazio è esaurito.
5. Leggi o estrai la radice. La lettura restituisce `heap[0]`. Per estrarla, salva la radice e rimuovi l'ultimo elemento, riducendo `n`. Se rimangono elementi, metti quello rimosso alla radice e applica `heapifyDown(0, n)`. Restituisci la radice salvata; con un array, escludi la vecchia ultima cella dalla parte attiva.

### Varianti: verifica e ricerca degli estremi

Per `isMinHeap` controlla che ogni padre sia `<=` a ciascun figlio esistente; per `isMaxHeap` usa `>=`. Restituisci `false` alla prima violazione, `true` alla fine. Per il massimo in un MinHeap, o il minimo in un MaxHeap, scorri le foglie: da `n/2` a `n-1`. Prima gestisci il caso vuoto.

> Da ricordare. Con indici da 1: radice 1, padre `i/2`, figli `2*i` e `2*i+1`, ultimo nodo interno `n/2`. Nel tuo tutorato la coda di priorità usa questa convenzione. Rispetta il contratto sul vuoto: MaxHeap del laboratorio restituisce `null`; altre classi lanciano eccezioni.

## Pagina 3 — HeapSort e coda di priorità

### Riutilizzare le operazioni della scheda precedente

#### Cosa mantenere

- Per HeapSort: sequenza da ordinare, heap di lavoro o dimensione della parte ancora attiva.
- Per la coda: nodi con `value` e `priority`; gli scambi spostano il nodo intero e i confronti usano la priorità.

### HeapSort usando una classe heap

1. Costruisci l'heap. Usa una copia dei valori in ingresso quando devi scrivere il risultato nella lista originale senza alterare l'heap durante le estrazioni.
2. Scegli verso e posizione. Per ottenere ordine crescente: estrai da un MinHeap e scrivi da sinistra a destra, oppure estrai da un MaxHeap e scrivi da destra a sinistra.
3. Completa il risultato. Ripeti l'estrazione finché l'heap è vuoto. Per ordine decrescente inverti il verso di riempimento. Restituisci la sequenza e l'eventuale contatore dei confronti.

### Variante: HeapSort direttamente sull'array

Costruisci l'heap. Scambia la radice con l'ultimo elemento attivo, riduci la dimensione attiva e ripristina la radice con `heapifyDown`. Ripeti finché resta un elemento. Con MaxHeap ottieni ordine crescente; con MinHeap ottieni ordine decrescente. Il tratto già ordinato deve rimanere fuori da `heapifyDown`.

### Coda con priorità separata

1. Inserisci e consulta. Crea il nodo valore-priorità, mettilo in fondo e fallo risalire. La lettura restituisce il valore della radice; la lettura della priorità restituisce il suo campo `priority`.
2. Estrai e ordina. Usa l'estrazione della radice. Nel tutorato `peak()` estrae, `getMax()` legge soltanto e `sort()` restituisce valori per priorità decrescente. Se devi preservare la coda, lavora su una copia.
3. Modifica una priorità. Individua il nodo e assegna la nuova priorità. Se deve superare il padre, usa `heapifyUp`; altrimenti usa `heapifyDown`. Per la coda di min-priorità inverti il criterio dei confronti.

> Da ricordare. Dimensione e capacità sono diverse. Se ampli un array-heap puoi copiare nelle stesse posizioni. Nel tutorato `clear()` ripristina la capacità iniziale; `add()` rifiuta valore `null` e priorità negativa. Controlla queste condizioni prima di modificare la coda.
