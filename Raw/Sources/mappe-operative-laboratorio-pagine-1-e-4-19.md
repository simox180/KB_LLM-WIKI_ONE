---
Title: Mappe operative di laboratorio — pagine 1 e 4-19
Author: Materiale di studio per Simone
Reference: Raw/Files/Mappe_operative_laboratorio_ASD.pdf — pagine 1, 4-19
ContentType:
  - markdown
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Mappe operative di laboratorio — pagine 1 e 4-19

## Pagina 1

```text
GUIDA ALLA CONSULTAZIONE
Mappe operative di laboratorio
Algoritmi e Strutture Dati | Java | Schede per scrivere e ripassare
Ogni scheda raccoglie cosa mantenere, passaggi operativi e differenze delle varianti. I nomi
richiamano le tue esercitazioni; i frammenti Java compaiono solo nei punti utili. Le varianti
riprendono le strutture e gli algoritmi delle esercitazioni concordate.
Indice delle schede
Heap, HeapSort e code di priorità
 2-3
Liste concatenate, deque e liste ricorsive
 4-6
BST standard, ReverseBST e varianti
 7-8
Tabelle hash e dizionari
 9-10
Ordinamenti e varianti del pivot
 11-12
Grafi, visite, Prim e Dijkstra
 13-16
Catena di matrici
 17
Oggetti e Collections
 18
Strutture dati: quando usarle e metodi utili
 19
Prima di implementare un metodo
 1. Leggi il contratto. Individua input, risultato, strutture già presenti, eccezioni e vincoli:
 ricorsione, complessità, modifica dell’input o nuova struttura.
2. Controlla il caso iniziale. Gestisci null e indici come richiesto. Per una collezione
 distinguere vuoto, un elemento, elemento assente e duplicato risolve molti errori.
3. Mantieni coerente lo stato. Aggiorna collegamenti, dimensione e contatori solo quando
 l’operazione li modifica. Se riusi un algoritmo, reinizializza il suo stato.
4. Segui i metodi richiesti. Completa i TODO e usa gli helper forniti. Un metodo dichiarato
 non supportato non diventa da implementare solo perché esiste nell’interfaccia.
Da ricordare. Convenzioni delle schede: indici da 0, ordinamento crescente e BST senza
duplicati, salvo indicazione diversa. I confronti di valori generici usano compareTo;
l’uguaglianza richiesta dalle collezioni usa equals.
Riferimenti di laboratorio
Esercitazioni personali · Tutorato 1 · Tutorato 2 · Tutorato 3 · ReverseBST · SimpleDequeue
```

## Pagina 4

```text
02 / LISTE
Lista semplicemente concatenata
Ricerca, accesso, inserimento e rimozione
Cosa mantenere
 • head, tail, size; ciascun nodo contiene item e next. Durante una modifica usa nodo corrente
 e precedente.
• Per accesso, sostituzione e rimozione: 0 <= index < size. Per inserimento: 0 <= index <=
 size.
Passaggi per individuare e usare un nodo
 1. Cerca per valore o indice. Parti da head e avanza con next. Per contains/indexOf
 confronta item con equals; per get/set conta gli spostamenti fino all’indice. lastIndexOf
continua la scansione e conserva l’ultima posizione trovata.
2. Leggi o sostituisci. get restituisce item. set salva il vecchio item, assegna il nuovo e
 restituisce quello salvato. La dimensione non cambia.
3. Inserisci in testa. Crea un nodo il cui next sia la vecchia head; assegna head al nuovo
 nodo. Se la lista era vuota, assegna anche tail allo stesso nodo. Incrementa size una volta.
4. Inserisci in mezzo o in fondo. Trova il predecessore della posizione. Collega prima il
 nuovo nodo al successivo, poi il precedente al nuovo nodo. Se aggiungi in fondo, aggiorna
tail; con tail disponibile puoi aggiungere in O(1). Incrementa size una volta.
5. Rimuovi il nodo trovato. Salva item e successivo. Se è head, sposta head al successivo;
 altrimenti collega precedente.next al successivo. Se è tail, sposta tail al precedente.
Decrementa size; se la lista diventa vuota, entrambe le estremità sono null.
6. Restituisci il risultato corretto. remove(index) restituisce l’elemento rimosso;
 remove(value) segnala se lo ha trovato. clear azzera riferimenti e dimensione; toArray
visita i nodi nell’ordine e riempie un array di lunghezza size.
Variante: rimuovere tutte le occorrenze
Dopo una rimozione prosegui dal successivo salvato, mantenendo fermo il precedente. Il
precedente avanza solo quando conservi il nodo corrente. In questo modo gestisci anche
occorrenze consecutive. Restituisci il conteggio richiesto.
Da ricordare. Prima di cambiare next, conserva il riferimento che ti serve per proseguire.
Aggiorna il contatore delle modifiche strutturali secondo il template; la sola sostituzione di item
normalmente non è una modifica strutturale.
```

## Pagina 5

```text
02 / LISTE
Deque, inversione e iteratore
Varianti della gestione dei collegamenti
Cosa mantenere
 • Nella deque: head, tail, size e nodi con item, next e previous. Le operazioni alle estremità
 devono essere O(1).
• Per l’iteratore: riferimento al prossimo nodo da restituire e copia del contatore delle
 modifiche, adattando i nomi al template.
Operazioni della SimpleDequeue
 1. Aggiungi a un’estremità. In testa: il nuovo nodo ha previous=null e next=vecchia head;
 aggiorna previous della vecchia head e poi head. Se era vuota, aggiorna anche tail. In coda
esegui gli aggiornamenti simmetrici. Incrementa size.
2. Leggi o estrai. La lettura restituisce item senza modifiche. L’estrazione salva item e
 sposta l’estremità al nodo vicino; azzera il collegamento verso l’esterno. Se rimuovi l’unico
nodo, head e tail diventano null. Decrementa size e restituisci item.
3. Rimuovi tutte le occorrenze. Scorri con un corrente e salva sempre il prossimo. Quando
 item coincide, collega previous e next tra loro; se uno manca, aggiorna head o tail. Riduci
size e conta le rimozioni. Continua dal prossimo salvato.
Variante: reverse della lista semplice
Mantieni precedente=null e corrente=head; la vecchia head sarà la nuova tail. A ogni passo
salva corrente.next, indirizza corrente.next al precedente, sposta precedente sul corrente e
corrente sul successivo salvato. Alla fine head=precedente. Nella lista doppia puoi scambiare
next/previous di ogni nodo, proseguendo sul vecchio next, poi scambiare head e tail.
Variante: eliminare duplicati, pila e coda
Se è consentito, usa un HashSet dei valori già incontrati: conserva il primo, scollega i
successivi uguali. Senza strutture aggiuntive, per ogni nodo cerca e rimuovi gli uguali nel
resto della lista. Per una pila inserisci/estrai dalla testa; per una coda inserisci dalla tail ed
estrai dalla head.
Iteratore fail-fast
hasNext verifica se resta un nodo. In next confronta il contatore atteso con quello della lista:
se diverso, lancia ConcurrentModificationException. Se non resta un nodo, lancia
NoSuchElementException; altrimenti restituisci item e avanza. Una scansione per indice a
ogni next non è necessaria.
Da ricordare. SimpleDequeue: lettura/estrazione da vuoto lanciano IllegalStateException;
removeAll restituisce il numero rimosso ed è O(n). Nell’iteratore implementa remove solo se
previsto dalla consegna.
```

## Pagina 6

```text
02 / LISTE
Lista ricorsiva immutabile
ADTConsList: lavorare su first, rest e cons
Cosa mantenere
 • La lista corrente, il suo primo elemento first() e il resto rest(). cons(x) crea una lista con x
 davanti alla lista su cui è chiamato.
• Ogni metodo che modifica logicamente la lista restituisce una lista risultato: conserva i
 riferimenti al risultato delle chiamate ricorsive.
Schema comune
 1. Gestisci la lista vuota. Per una ricerca restituisci false. Per una trasformazione restituisci
 la lista vuota, o la seconda lista nel caso append. Non chiamare first/rest su una lista vuota.
2. Decidi che cosa fare del primo elemento. Confrontalo con il valore cercato, oppure
 verifica la condizione del filtro. La scelta è conservarlo, sostituirlo o eliminarlo.
3. Lavora sul resto. Richiama lo stesso metodo su rest, salvo quando la prima occorrenza
 trovata conclude l’operazione.
4. Ricostruisci il risultato. Se conservi il primo, aggiungilo davanti al risultato ricorsivo con
 cons; se lo elimini, restituisci direttamente il risultato sul resto.
Ricerca, rimozione e sostituzione
find termina con true alla prima uguaglianza. removeFirst, quando trova l’elemento,
restituisce direttamente rest; removeAll continua la ricorsione anche dopo una rimozione.
updateFirst sostituisce il primo trovato e conserva il resto; updateAll continua a trasformare
anche rest. Per print, combina il testo di first con quello ottenuto dal resto.
append e reverse
append(seconda): se questa lista è vuota, restituisci seconda; altrimenti concatena
ricorsivamente rest con seconda e rimetti first davanti. reverse: inverti rest e aggiungi first in
fondo al risultato, usando append con una lista di un solo elemento. Questa versione di
reverse richiede O(n²); un accumulatore costruito con cons permette O(n), se ammesso.
Variante: filtro
Se first soddisfa la condizione, aggiungilo con cons davanti al risultato del filtro su rest. Se non
la soddisfa, restituisci solo il filtro su rest. L’ordine degli elementi conservati rimane quello
originale.
Da ricordare. Esempio utile di ricostruzione: rest().removeAll(x).cons(first()) è il ramo
in cui il primo elemento va conservato. La ricorsione deve usare rest, così il problema diventa
più piccolo.
```

## Pagina 7

```text
03 / ALBERI
BST e ReverseBST
Stessa struttura, direzione dei confronti invertita
Cosa mantenere
 • Un riferimento root, la dimensione e nodi con label, left, right, parent. Root è null quando
 l’albero è vuoto.
• BST: valori minori a sinistra, maggiori a destra. ReverseBST: maggiori a sinistra, minori a
 destra. Le classi di riferimento non ammettono duplicati.
Ricerca e inserimento
 1. Confronta nel nodo corrente. Se il nodo è null, la ricerca fallisce. Se il valore coincide, la
 ricerca restituisce il nodo; l’inserimento segnala che il valore è già presente, senza
cambiare size.
2. Scegli il sottoalbero. Nel BST segui left se il valore è minore, right se è maggiore. Nel
 ReverseBST segui left se è maggiore, right se è minore. Ripeti ricorsivamente quando
richiesto.
3. Collega il nuovo nodo. Se il ramo scelto è vuoto, crea il nodo, imposta il suo parent e
 collegalo al padre. Se root era null, assegna direttamente root. Incrementa size una sola
volta e restituisci il risultato previsto.
Visite, altezza ed estremi
 1. Visita in ordine. Sul nodo null non fare nulla. Nel BST visita left, elabora label, visita right
 per l’ordine crescente. Nel ReverseBST questo stesso percorso produce ordine
decrescente; per averlo crescente visita right, label, left.
2. Calcola l’altezza. Sul nodo null restituisci -1. Altrimenti calcola le altezze dei due figli e
 restituisci 1 + max(altezzaLeft, altezzaRight): una foglia ha altezza 0.
3. Trova minimo e massimo. Nel BST il minimo si trova seguendo left e il massimo
 seguendo right fino all’ultimo nodo. Nel ReverseBST il minimo segue right e il massimo left.
Gestisci prima l’albero vuoto.
Risultato
Ricerca e inserimento seguono un solo ramo per livello. Le visite producono una sequenza
nell’ordine richiesto; il calcolo dell’altezza combina invece i risultati di entrambi i sottoalberi.
Da ricordare. Nel ReverseBST inverti coerentemente le direzioni in tutti i metodi. Per i
confronti usa il segno di compareTo: < 0, == 0, > 0; non supporre che restituisca soltanto -1, 0
o 1.
```

## Pagina 8

```text
03 / ALBERI
BST: rimozione e varianti
Riutilizzare ricerca, estremi e collegamenti al padre
Cosa mantenere
 • Nodo da rimuovere, suo parent ed eventuale figlio che prenderà il suo posto. Per i nodi con
 due figli serve anche il successore.
• Per una raccolta di risultati usa una lista; per contare nodi o foglie bastano i risultati interi
 restituiti dalla ricorsione.
Rimuovere un valore
 1. Cerca il nodo. Se non esiste, restituisci l’esito richiesto senza modificare l’albero.
 2. Gestisci zero o un figlio. Se è una foglia, sostituisci il collegamento del padre con null. Se
 ha un figlio, collega il padre a quel figlio e aggiorna child.parent. Se togli root, il figlio
diventa root con parent=null.
3. Gestisci due figli. Trova il successore, copia la sua label nel nodo da eliminare e rimuovi il
 successore dalla posizione originale. Quel nodo ha al massimo un figlio, quindi usa il caso
precedente.
4. Concludi una sola volta. Decrementa size per l’unico valore eliminato. Se richiesto,
 restituisci il valore originale salvato prima della sostituzione.
Successore e predecessore nel BST
Successore: se esiste right, prendi il minimo di right; altrimenti risali tramite parent finché
arrivi da un figlio sinistro. Il padre raggiunto è il successore; se finisci oltre root, non esiste.
Predecessore: massimo di left, altrimenti risali finché arrivi da un figlio destro.
Come cambiano nel ReverseBST
Successore: minimo di left; se left manca, risali finché arrivi da un figlio destro. Predecessore:
massimo di right; se right manca, risali finché arrivi da un figlio sinistro. “Successore”
continua a significare il valore immediatamente maggiore.
Varianti: foglie, intervalli e duplicati
Conta foglie: null vale 0, nodo senza figli vale 1, altrimenti somma i due risultati. Per
restituirle, visita l’albero e aggiungi alla lista soltanto le etichette dei nodi senza figli. Per
raccogliere valori in [a,b], visita nell’ordine richiesto e aggiungi quelli nell’intervallo; elimina i
rami impossibili solo se richiesta maggiore efficienza. Per ammettere duplicati puoi
aggiungere un contatore nel nodo: incrementalo all’inserimento uguale e decrementalo alla
rimozione prima di scollegare il nodo.
Da ricordare. Con duplicati, chiarisci se size conta valori o nodi distinti. Se sostituisci un nodo
con il successore, trasferisci label e contatore insieme e rimuovi fisicamente il nodo successore,
evitando due nodi con la stessa chiave.
```

## Pagina 9

```text
04 / HASH
Hash con liste di collisione
Chaining: prima il bucket, poi la lista
Cosa mantenere
 • Tabella di bucket, liste di nodi, size, capacità, fattore di carico e funzione hash. L’indice
 dipende dalla capacità attuale.
• Per un iteratore fail-fast: indice del bucket, prossimo nodo e contatore atteso delle modifiche
 strutturali.
Ricerca, inserimento e rimozione
 1. Calcola il bucket. Valida l’elemento e usa la funzione hash fornita per ottenere un indice
 da 0 a capacità-1. Cerca nella lista di quel bucket confrontando i valori con equals.
2. Inserisci solo se assente. Se trovi un uguale, restituisci false. Altrimenti amplia la tabella
 se la nuova dimensione supera la soglia; ricalcola il bucket dopo l’ampliamento. Collega il
nuovo nodo secondo il template e incrementa size.
3. Rimuovi nella lista. Mantieni corrente e precedente. Se trovi l’elemento, scollegalo; se
 era il primo, aggiorna il riferimento nel bucket. Decrementa size e restituisci true. Se
termini la lista, restituisci false.
4. Esegui il rehash. Crea una tabella più grande, visita tutti i nodi della vecchia e
 ridistribuiscili calcolando gli indici con la nuova capacità. Conserva la dimensione totale:
non contare gli stessi elementi due volte.
Operazioni su collezioni
containsAll: controlla ogni elemento e termina con false al primo assente. addAll/removeAll:
applica l’operazione elementare a ciascun valore e conserva un flag che diventa true se
almeno una modifica riesce. Se sorgente e destinazione coincidono, gestisci il caso senza
invalidare la scansione.
Iteratore sui bucket
Trova il primo bucket non vuoto. next restituisce il valore del nodo corrente e passa al suo
next; quando la lista termina, cerca il bucket non vuoto successivo. hasNext indica se esiste
un prossimo elemento. Controlla le modifiche concorrenti e il caso di esaurimento come
nell’iteratore di lista.
Variante: dizionario chiave-valore
Il nodo contiene key e value. Hash ed uguaglianza lavorano sulla chiave. Se put trova la
chiave, sostituisce il valore senza aumentare size; altrimenti crea una nuova coppia. get
restituisce il valore associato e remove elimina la coppia, secondo il contratto.
Da ricordare. Un rehash deve ricalcolare gli indici: copiare i bucket nelle stesse posizioni è
sbagliato. Se implementi la funzione di divisione, Math.floorMod(hashCode, capacità) gestisce
anche hash negativi; non modificare gli helper che la consegna vieta di cambiare.
```

## Pagina 10

```text
04 / HASH
Hash a indirizzamento aperto
Scansione lineare e varianti della sequenza di tentativi
Cosa mantenere
 • Un array di celle, size, capacità e funzione di probing. Nel probing lineare: indice = (inizio
 + tentativo) % capacità.
• Se è prevista la rimozione, distingui tre stati: mai occupato, occupato, cancellato. Puoi usare
 un marcatore dedicato o un array degli stati.
Ricerca e inserimento
 1. Parti dall’hash iniziale. Genera gli indici della sequenza usando la stessa funzione per
 tutte le operazioni. Limita la scansione al numero massimo di tentativi previsto, evitando
cicli infiniti.
2. Cerca un valore. Se la cella è occupata, confronta con equals. Se è cancellata, prosegui.
 Se non è mai stata occupata, il valore è assente; se esaurisci la sequenza senza trovarlo, è
comunque assente.
3. Cerca dove inserire. Conserva il primo slot cancellato incontrato, ma continua a cercare
 un possibile duplicato. Quando arrivi a una cella mai occupata, inserisci nel primo
cancellato salvato oppure in quella cella. Se trovi un uguale, non inserire.
4. Gestisci fine scansione e crescita. Se non trovi un duplicato e hai uno slot cancellato,
 puoi usarlo. Se manca spazio, o superi la soglia di carico, amplia e ripeti con la nuova
tabella. Incrementa size solo quando l’inserimento riesce.
Variante: cancellazione
Esegui la ricerca normale. Se trovi il valore, marca la cella come cancellata, elimina il
riferimento al valore e decrementa size. Una semplice assegnazione a null interromperebbe
ricerche di elementi collocati più avanti dopo una collisione.
Rehash
Crea la nuova tabella e reinserisci soltanto le celle occupate, usando la nuova capacità. I
marcatori di cancellazione non si copiano. Mantieni il numero degli elementi e il contatore
delle modifiche coerenti con il template.
Varianti: quadratico e doppio hashing
Cambia solo il generatore degli indici: quadratico h0 + c1*i + c2*i*i, doppio hashing h1 +
i*h2, sempre modulo capacità. Usa gli stessi parametri in ricerca e inserimento. Le scelte di
capacità e passo devono garantire la copertura richiesta; nel doppio hashing il passo deve
essere coprimo con la capacità.
Da ricordare. Nel tutorato di riferimento la rimozione non era richiesta: il marcatore serve
nella variante che la aggiunge. “Tabella con celle libere” non garantisce che qualunque probing
le raggiunga: dopo i tentativi ammessi, applica la gestione prevista senza continuare all’infinito.
```

## Pagina 11

```text
05 / ORDINAMENTI
Insertion, Bubble e MergeSort
Passaggi base e modifiche comuni alle varianti
Cosa mantenere
Lista di valori confrontabili; indici e temporanei. Se richiesto dal laboratorio, restituisci anche
countCompare: incrementalo quando confronti due valori, non quando controlli un indice. Nei
metodi ricorsivi accumula anche i confronti dei sottoproblemi.
InsertionSort
 1. Estrai la chiave. Per i da 1 fino all’ultimo indice, salva il valore in posizione i e poni j=i-1.
 2. Apri il posto e reinserisci. Finché j>=0 e il valore in j è maggiore della chiave, spostalo
 in j+1 e decrementa j. Scrivi la chiave in j+1. Non spostare gli uguali se vuoi mantenere la
stabilità.
BubbleSort
 1. Confronta le coppie adiacenti. Poni limite all’ultimo indice attivo. Azzera il flag degli
 scambi e, per j da 0 a limite-1, confronta j e j+1: se il primo valore è maggiore, scambiali e
attiva il flag.
2. Riduci il tratto attivo. Dopo il passaggio, l’elemento maggiore è in fondo al tratto:
 accorcia il limite. Se un intero passaggio non ha prodotto scambi, termina.
MergeSort
 1. Dividi e ordina. Con zero o un elemento restituisci la sequenza. Altrimenti dividi in due
 metà e ordinale ricorsivamente; mantieni distinti il risultato sinistro e quello destro.
2. Fondi con due indici. Parti dall’inizio di entrambe le metà. Confronta i valori correnti,
 aggiungi il minore al risultato e avanza soltanto nella metà scelta. In caso di uguaglianza
scegli la metà sinistra per un ordinamento stabile.
3. Completa e restituisci. Quando una metà termina, copia in ordine tutti i valori rimasti
 nell’altra. Restituisci la lista fusa e, se richiesto, il totale dei confronti.
Varianti comuni
Per ordine decrescente inverti il verso del confronto, conservando la gestione degli uguali. Per
ordinare oggetti per attributo, usa il compareTo richiesto o un Comparator e applicalo in tutti i
confronti. Per verificare l’ordine, controlla le coppie adiacenti e termina alla prima inversione.
Per fondere due liste già ordinate, usa soltanto i passi 2-3 di MergeSort.
Da ricordare. ArrayList.set(i,x) sostituisce; add(i,x) inserisce e sposta gli elementi. Nei
passaggi in-place di Insertion e Bubble usa set per riscrivere posizioni già esistenti. Per
HeapSort riprendi la scheda a pagina 3.
```

## Pagina 12

```text
05 / ORDINAMENTI
QuickSort e scelta del pivot
Una sola partizione, più modi per scegliere il riferimento
Cosa mantenere
 • La sequenza, gli estremi inclusi left e right, il valore pivot e un indice boundary che separa i
 valori già riconosciuti come minori.
• La scheda usa la partizione con pivot alla fine, coerente con il QuickSort del laboratorio.
 Mantieni la stessa convenzione in tutte le chiamate.
Partizione con ultimo elemento come pivot
 1. Gestisci il caso base. Se left>=right, il tratto contiene al massimo un elemento: termina
 la chiamata.
2. Prepara il confine. Salva il valore in right come pivot e poni boundary=left.
 3. Esamina il tratto. Per j da left a right-1 confronta il valore con il pivot. Se è minore,
 scambia le posizioni j e boundary e incrementa boundary; altrimenti prosegui senza
spostare il confine.
4. Colloca il pivot. Scambia il pivot in right con il valore in boundary. Il pivot è ora nella sua
 posizione finale: a sinistra ci sono valori minori, a destra maggiori o uguali.
5. Ordina le due parti. Richiama QuickSort su [left, boundary-1] e su [boundary+1, right]. Il
 pivot non entra nelle chiamate ricorsive.
Variante: pivot casuale
Scegli un indice casuale dentro [left,right], inclusi gli estremi. Scambia quell’elemento con
quello in right e applica la stessa partizione. La scelta va ripetuta nel tratto della chiamata
corrente.
Variante: mediana di tre
Considera i valori nelle posizioni left, left + (right-left)/2 e right. Individua quello
intermedio per valore, scambialo con l’elemento in right e richiama la partizione. Non
scegliere semplicemente l’indice centrale: devi confrontare i tre valori.
Risultato e altre modifiche
La lista viene ordinata nel posto, se questo è il contratto. Per ordine decrescente porta a
sinistra i valori maggiori del pivot. Per oggetti usa coerentemente il confronto sull’attributo
richiesto. Se devi contare i confronti, includi anche quelli usati per scegliere il pivot, quando lo
prevede la traccia.
Da ricordare. Mantieni la ricorsione su intervalli più piccoli. Escludi sempre boundary dalle due
chiamate: è l’errore che più facilmente causa ricorsione infinita. Molti valori uguali possono
produrre partizioni sbilanciate, ma la scansione deve comunque terminare.
```

## Pagina 13

```text
06 / GRAFI
Rappresentare e modificare un grafo
Liste di adiacenza e MatrixGraph
Cosa mantenere
 • Liste: una mappa GraphNode → Set<GraphEdge>. Matrice: elenco dei nodi e tabella di archi,
 con null per le celle senza arco.
• Numero dei nodi e degli archi, direzione e peso. Usa il nodo effettivamente conservato nel
 grafo quando devi modificarne lo stato: un nodo nuovo con la stessa etichetta non è lo
stesso oggetto.
Operazioni con liste di adiacenza
 1. Aggiungi e cerca un nodo. Controlla se l’etichetta esiste già. Se assente, inserisci il nodo
 nella mappa con un insieme di archi vuoto. Per le ricerche recupera il nodo presente nel
grafo.
2. Aggiungi o leggi un arco. Valida gli estremi e la direzione richiesta. Nel grafo non
 orientato registra l’arco negli insiemi di entrambi gli estremi; in quello orientato segui la
rappresentazione degli archi uscenti. Evita duplicati e incrementa il conteggio una sola
volta.
3. Rimuovi un arco. Verifica che esista, elimina tutti i riferimenti che lo rappresentano e
 decrementa il numero degli archi una sola volta.
4. Rimuovi un nodo. Raccogli prima gli archi incidenti, poi rimuovili con la stessa operazione
 elementare e infine elimina il nodo. Nel grafo orientato considera anche gli archi entranti.
Non modificare un insieme mentre lo scorri con un normale for-each.
Come cambia nella matrice
Per aggiungere un nodo, aggiungi una colonna null a ogni riga e una nuova riga della
dimensione aggiornata. Individua gli indici dei due estremi e scrivi l’arco nella cella [i][j]; nel
non orientato anche in [j][i]. Per rimuoverlo azzera le celle corrispondenti. Per rimuovere un
nodo elimina prima i suoi archi, poi riga, colonna e voce nell’elenco, aggiornando gli eventuali
indici memorizzati.
Vicini e conteggio degli archi
getEdgesOf restituisce archi: per ottenere il vicino, nel non orientato scegli l’estremo diverso
dal nodo corrente tramite equals; nel diretto usa l’estremo di arrivo degli archi uscenti. Per
l’insieme globale degli archi non orientati, unisci i bucket in un HashSet. Non dividere sempre
per due: gli autoarchi richiedono attenzione.
Da ricordare. equals e hashCode degli archi devono concordare: nel non orientato gli estremi
scambiati identificano lo stesso arco; nel diretto l’ordine conta. Le classi di riferimento non
usano il peso per distinguere due archi con gli stessi estremi.
```

## Pagina 14

```text
06 / GRAFI
BFS e DFS
Scoprire i nodi una volta e conservare i predecessori
Cosa mantenere
 • BFS: una Queue<GraphNode<L>> realizzata con ArrayDeque, colore, integerDistance e
 previous.
• DFS: ricorsione, colore, previous e contatore del tempo per enteringTime e exitingTime.
 Bianco=non scoperto, grigio=in lavorazione, nero=concluso.
BFS da una sorgente
 1. Inizializza. Recupera la sorgente dal grafo e prepara una coda vuota. Per tutti i nodi
 imposta bianco, distanza infinita e previous=null. La sorgente diventa grigia, con distanza
0, e viene inserita in coda.
2. Estrai e scopri i vicini. Finché la coda non è vuota, estrai u con poll. Per ogni vicino v
 ancora bianco: rendilo grigio, assegna d[v] = d[u] + 1, poni previous[v]=u e inseriscilo in
coda.
3. Concludi il nodo. Dopo avere esaminato tutti i vicini, rendi u nero. Al termine, le distanze
 indicano il minimo numero di archi dalla sorgente; i nodi non raggiunti restano a infinito.
DFS completa
 1. Prepara lo stato. Azzera il tempo e imposta tutti i nodi bianchi con previous=null. Scorri i
 nodi del grafo: per ciascuno ancora bianco avvia la visita ricorsiva.
2. Entra nel nodo. Rendilo grigio e registra il tempo di ingresso incrementando il contatore.
 Per ogni vicino bianco, imposta previous al nodo corrente e richiama la visita sul vicino.
3. Esci dal nodo. Dopo tutte le chiamate sui vicini, rendi il nodo nero e registra il tempo di
 uscita incrementando il contatore. Ogni nodo riceve una sola coppia di tempi.
Varianti: sorgente, ordine e raggiungibilità
Per una DFS da una sola sorgente avvia soltanto quella visita dopo l’inizializzazione. Se serve
l’ordine di scoperta, aggiungi il nodo alla lista quando diventa grigio; per l’ordine di
completamento, quando diventa nero. Dopo una visita dalla sorgente, un nodo è raggiungibile
se è stato scoperto. Il percorso tramite previous è nella scheda di pagina 16.
Da ricordare. In BFS marca il nodo prima di accodarlo; in DFS all’inizio della sua visita, prima
di esplorarne gli archi: così non lo visiti più volte. La DFS produce un percorso di visita; solo la
BFS garantisce il minimo numero di archi.
```

## Pagina 15

```text
06 / GRAFI
Prim
Costruire l’albero ricoprente minimo con le classi del laboratorio
Cosa mantenere
 • HashSet<GraphNode<L>> visitati per i nodi già inseriti nell’albero e
 ArrayList<GraphNode<L>> coda per quelli ancora da scegliere.
• Per ogni nodo: floatingPointDistance è il peso del miglior arco che lo collega all’albero;
 previous è il nodo attraverso cui entra. La coda è una lista dalla quale cerchi il minimo a
ogni iterazione.
Passaggi operativi
 1. Controlla grafo e sorgente. Usa un grafo non orientato e pesato; recupera la sorgente
 effettiva dal grafo. Rispetta anche i vincoli aggiuntivi del template, come il controllo dei
pesi non negativi.
2. Inizializza tutto. Svuota visitati e coda. Per ogni nodo imposta priorità a infinito e
 previous=null; assegna priorità 0 alla sorgente. Inserisci tutti i nodi nella coda, compresa la
sorgente.
3. Scegli il prossimo nodo. Scorri la coda, conserva il nodo con priorità minima e rimuovilo.
 Aggiungilo a visitati: da questo momento appartiene all’albero.
4. Esamina gli archi incidenti. Per ogni arco di u, trova l’altro estremo v usando equals. Se
 v è già in visitati, passa all’arco successivo.
5. Aggiorna il collegamento migliore. Se il peso dell’arco (u,v) è minore della priorità di v,
 assegna a v quel peso e poni previous[v]=u. Non sommare la priorità di u: qui stai
scegliendo un singolo arco di collegamento.
6. Ripeti e costruisci il risultato. Continua finché la coda è vuota. In un grafo connesso, per
 ogni nodo diverso dalla sorgente, l’arco tra nodo e previous fa parte dell’albero minimo. La
sorgente mantiene previous=null.
Esempio del confronto
Se la priorità attuale di v è 8 e trovi un arco da u a v di peso 5, sostituisci 8 con 5 e imposta
previous[v]=u. Il costo già necessario per raggiungere u non entra nel confronto.
Da ricordare. Se estrai un nodo con priorità infinita, la componente della sorgente è esaurita:
non esiste un unico albero ricoprente di tutto il grafo. Gestisci errore o foresta secondo la
consegna. Con ArrayList non serve riordinare la coda dopo un aggiornamento: cerchi
nuovamente il minimo al passo successivo.
```

## Pagina 16

```text
06 / GRAFI
Dijkstra e risultati delle visite
Distanze minime, percorsi e componenti connesse
Cosa mantenere per Dijkstra
Come in Prim: coda ArrayList, insieme dei nodi conclusi e previous. floatingPointDistance ora
significa distanza totale dalla sorgente. Tutti i pesi devono essere non negativi; sono
ammessi pesi zero.
Dijkstra sulle stesse classi
 1. Inizializza. Imposta tutte le distanze a infinito e previous=null; la sorgente effettiva ha
 distanza 0. Svuota coda e insieme dei conclusi, poi inserisci tutti i nodi in coda.
2. Estrai il minimo. Cerca il nodo u con distanza minima, toglilo dalla coda e concludilo. Se la
 distanza è infinita, termina: tutti i nodi rimasti sono irraggiungibili.
3. Rilassa gli archi. Per ogni vicino v non concluso calcola candidato = d[u] + peso(u,v). Se
 candidato<d[v], assegna il candidato a d[v] e poni previous[v]=u. Nel grafo diretto
considera gli archi uscenti.
4. Ripeti. Continua fino a esaurire la coda o i nodi raggiungibili. Le distanze finali misurano il
 costo minimo dalla sorgente; previous permette di ricostruire un percorso minimo.
Differenza decisiva rispetto a Prim
Prim confronta il peso del solo arco con la priorità di v. Dijkstra confronta la distanza di u più
quel peso con la distanza di v. Per esempio: d[u]=7 e arco di peso 5 producono candidato=12;
aggiorni v solo se la sua distanza attuale è maggiore di 12.
Ricostruire un percorso da previous
 1. Controlla se esiste. Se la destinazione non è stata raggiunta, restituisci il risultato
 previsto per “nessun percorso”. Se coincide con la sorgente, il percorso contiene soltanto
quel nodo.
2. Risalilo e inverti. Parti dalla destinazione, aggiungila alla lista e continua con previous
 fino alla sorgente, includendola. Inverti la lista per ottenere sorgente → destinazione. Se
raggiungi null prima della sorgente, non hai una catena valida.
Variante di BFS/DFS: componenti connesse
Nel grafo non orientato inizializza i visitati una volta sola. Scorri tutti i nodi: quando ne trovi
uno non visitato, incrementa il numero della componente e avvia da lì BFS o DFS, assegnando
quel numero ai nodi scoperti. Non azzerare i visitati tra una componente e la successiva.
Da ricordare. Il percorso di BFS minimizza il numero di archi; quello di Dijkstra minimizza la
somma dei pesi. Nei grafi orientati, ripetere semplicemente BFS/DFS non calcola le componenti
fortemente connesse.
```

## Pagina 17

```text
07 / PROGRAMMAZIONE DINAMICA
Catena di matrici
Calcolare il costo e ricostruire le parentesi
Cosa mantenere
 • Il vettore delle dimensioni p, lungo n+1: la matrice Ai ha p[i] righe e p[i+1] colonne, usando
 indici da 0.
• La tabella m[i][j] del costo minimo per le matrici da i a j e b[i][j] dell’indice dove separare
 la catena ottimale.
Riempire la tabella dei costi
 1. Prepara il caso base. Una sola matrice non richiede moltiplicazioni: imposta m[i][i]=0 per
 ogni i. Le celle sotto la diagonale non servono.
2. Scegli la lunghezza della catena. Fai crescere len da 2 a n. Per ogni inizio i da 0 a n-len,
 calcola j=i+len-1 e inizializza il miglior costo per [i,j] a infinito.
3. Prova ogni separazione. Per k da i a j-1 considera il blocco [i,k] e quello [k+1,j]. Calcola
 m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1].
4. Conserva la scelta migliore. Se il costo candidato è minore del migliore, aggiorna m[i][j]
 e salva k in b[i][j]. Continua a provare gli altri k prima di passare alla catena successiva.
Ricostruire la parentesizzazione
 1. Fermati sulla matrice singola. Nella chiamata traceBack(i,j), se i==j restituisci
 l’etichetta della matrice, con la numerazione richiesta dal template.
2. Usa la separazione memorizzata. Leggi k=b[i][j], ricostruisci ricorsivamente [i,k] e
 [k+1,j], poi combina i due risultati tra parentesi. Non cercare nuovamente il costo minimo
durante la ricostruzione.
Risultato
Il costo della catena completa è m[0][n-1]. La parentesizzazione parte da traceBack(0,n-1). Se
la traccia chiede soltanto una delle due parti, conserva comunque la dipendenza: per
ricostruire la scelta, b deve essere stata calcolata.
Da ricordare. L’ordine per lunghezza assicura che i sottoproblemi siano già risolti. In p il
secondo indice della moltiplicazione è k+1, non k. Usa un tipo numerico adeguato ai limiti della
traccia per evitare overflow nel prodotto delle dimensioni. Non devi moltiplicare realmente le
matrici.
```

## Pagina 18

```text
08 / OGGETTI E COLLECTIONS
Oggetti, filtri e prenotazioni
Riutilizzare le scelte di Aula, GestoreAule e TimeSlot
Cosa mantenere
 • Attributi dell’oggetto, chiave che lo identifica e collezioni: nel laboratorio, HashSet per
 aule/dotazioni e insieme ordinato per le prenotazioni.
• Per ogni ricerca: condizioni richieste, risultato da costruire e flag di verifica. Per gli intervalli:
 inizio e fine.
Identità, ordine e controlli
 1. Implementa equals e hashCode. Usa gli attributi indicati come identità dalla consegna,
 per esempio il nome dell’aula. Oggetti uguali devono produrre lo stesso hashCode.
2. Implementa compareTo. Confronta prima il criterio principale e, a parità, quello
 secondario. Per TimeSlot confronta inizio e poi fine. Allinea l’ordine con l’uguaglianza
richiesta, soprattutto se userai TreeSet.
3. Controlla una dotazione. Verifica il codice; se la dotazione è quantitativa, controlla anche
 che la quantità disponibile sia almeno quella richiesta. Per un insieme di richieste, tutte
devono essere soddisfatte.
Sovrapposizione e disponibilità
 1. Valida l’intervallo. Controlla i riferimenti e verifica che inizio preceda fine. Per due
 intervalli calcola inizioComune=max(inizi) e fineComune=min(fini).
2. Calcola l’intersezione. Se fineComune<=inizioComune, non c’è intersezione positiva: il
 metodo del laboratorio restituisce -1. Altrimenti converti la differenza nella misura
richiesta: nel laboratorio si usano minuti interi e la sovrapposizione rilevante è maggiore di
5 minuti.
3. Scorri le prenotazioni. Se una prenotazione produce una sovrapposizione rilevante,
 l’aula non è libera. Restituisci “libera” soltanto dopo aver escluso conflitti con tutte le
prenotazioni da considerare.
Filtrare, inserire e rimuovere
Per cercare aule adatte crea un insieme risultato: per ogni aula verifica disponibilità e tutte le
dotazioni, poi aggiungila soltanto se supera entrambi i controlli. Prima di aggiungere una
prenotazione applica gli stessi vincoli. Per rimuovere quelle che soddisfano un criterio, usa
iterator.remove dove supportato oppure raccogli prima gli elementi da eliminare.
Da ricordare. Segui esattamente il criterio della traccia: removePrenotazioniBefore del
laboratorio rimuove le prenotazioni con inizio minore o uguale alla soglia. Nelle varianti
cambiano i nomi degli oggetti e gli attributi; restano identità, confronto, filtro e aggiornamento
delle collezioni.
```

## Pagina 19

```text
PROMEMORIA FINALE
Strutture dati e metodi utili
Scelta rapida mentre scrivi un programma
• Array. Per capacità fissa, tabelle e matrici. Accesso a[i], lunghezza a.length; la dimensione
 logica può essere minore della capacità.
• ArrayList / List. Per sequenze indicizzate, heap e coda con ricerca lineare del minimo in
 Prim/Dijkstra. Metodi: add, get, set, remove, size, isEmpty. set sostituisce; add inserisce.
remove(int) usa un indice, remove(Object) un valore.
• HashSet / Set. Per visitati, eliminazione dei duplicati, aule e archi unici. Metodi: add, contains,
 remove, clear, size. Non conserva un ordine; richiede equals e hashCode coerenti.
• HashMap / Map. Per associare un nodo ai suoi archi o una chiave a un valore. Metodi: put,
 get, containsKey, remove, keySet, values, entrySet. put su una chiave già presente sostituisce
il valore.
• ArrayDeque / Queue / Deque. Per BFS: offer, poll, peek. Per una pila: push, pop, peek. Per
 entrambe le estremità: addFirst, addLast, pollFirst, pollLast. Non ammette null; poll/peek
restituiscono null se vuota, pop lancia un’eccezione.
• TreeSet / SortedSet. Per elementi unici mantenuti ordinati, come prenotazioni. Metodi: add,
 contains, remove, first, last, iterator. Il confronto uguale a zero identifica un duplicato per
l’insieme.
• Iterator. Per attraversare una collezione ed eventualmente rimuovere durante la visita.
 Metodi: hasNext, next, remove se supportato. Evita modifiche strutturali esterne mentre un
iteratore fail-fast è in uso.
• PriorityQueue di Java. Per estrarre il minimo tramite offer, poll, peek, con Comparator se
 necessario. Cambiare la priorità dentro un oggetto già inserito non riordina la coda: occorre
rimuoverlo e reinserirlo, oppure usare voci aggiornate e scartare quelle obsolete.
• Nodi concatenati e nodi BST. Per implementare direttamente lista, deque o albero. Mantieni
 next/previous oppure left/right/parent e modifica i riferimenti. Non sono collezioni Java con
add/remove già disponibili.
• ADTConsList. Per le trasformazioni ricorsive immutabili: isEmpty, first, rest, cons. Ogni
 trasformazione restituisce la lista risultato; cons aggiunge in testa alla lista ricevente.
Da ricordare. Usa le collezioni di libreria dove la consegna lo consente. Se devi implementare
heap, lista o hash, non sostituirli con la struttura Java pronta. In HashSet/HashMap o TreeSet
evita di modificare i campi che determinano identità o ordine mentre l’oggetto è memorizzato.
```
