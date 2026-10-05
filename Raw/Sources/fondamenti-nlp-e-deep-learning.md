---
Title: Fondamenti di NLP e deep learning
Reference: Raw/Files/Session 1 _ Intro to NLP – Lecture.pdf
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Fondamenti di NLP e deep learning

Trascrizione automatica dal PDF originale; la struttura delle pagine e conservata nei marcatori.

===== PAGE 1

Large Language Models, 
Agent-Oriented Applications
✅
 Session 1: Introduction to & Machine Learning
   Deep Learning & Natural Language Processing 
    
Prof: S. Mahed Mousavi, Ph.D. 
 Assistant Professor 
 Dipartimento di Ingegneria e Scienza dell'Informazione
 Università di Trento
1

## Pagina 2

Part 1 : 
Recap on Machine Learning
2

## Pagina 3

What is Machine Learning?
Machine Learning è un paradigma dell'intelligenza artiﬁciale in cui i 
computer apprendono modelli e regolarità a partire da dati, senza 
essere esplicitamente programmati.
Componenti chiave: 
● Dati di input: esempi numerici, testuali, visivi..., 
● Algoritmo di apprendimento: costruisce una funzione f(x),
● Modello: rappresentazione appresa dai dati
● Obiettivo: Generalizzare da dati osservati → fare predizioni 
accurate su dati nuovi
Esempi: Predire il prezzo di una casa, classiﬁcare email come spam, 
riconoscere oggetti in immagini, tradurre automaticamente una frase
3

## Pagina 4

Part 2 : 
Recap on Deep Learning
4

## Pagina 5

Deep Learning vs. Machine Learning
Caratteristica Machine Learning Deep Learning
Modello Alberi, SVM, KNN, regressione Reti neurali profonde (DNN, CNN, RNN)
Feature extraction Manuale (feature engineering) Automatica (end-to-end)
Dati richiesti Pochi dati, feature ben curate Molti dati grezzi
Prestazioni su dati complessi Limitate Eccellenti (testo, immagini, audio)
Potenza computazionale Relativamente bassa Molto elevata
Cos'è il Deep Learning?
Il Deep Learning (DL) è una sottoarea del Machine Learning che utilizza reti neurali profonde (deep neural networks) per apprendere direttamente 
dai dati in modo gerarchico.
Esempio pratico
Compito: Classiﬁcare immagini di cani e gatti
- ML classico: Estrai a mano colore, forma, texture → dai al classiﬁcatore
- DL: Rete convoluzionale (CNN) impara automaticamente caratteristiche visive → ﬁne-tuning del modello
➡ Oggi, il Deep Learning è la tecnologia dominante per l'elaborazione di immagini, linguaggio naturale e segnali complessi. 5

## Pagina 6

Backpropagation - How NNs Learn
Forward Pass
L'input attraversa la rete e 
produce un output
Calcolo Errore
Si misura la differenza tra 
output e target
Backward Pass
L'errore si propaga all'indietro 
attraverso la rete
Aggiornamento Pesi
I parametri vengono modiﬁcati 
per ridurre l'errore
Il Backpropagation (retropropagazione dell'errore) è l'algoritmo utilizzato per aggiornare i pesi in una rete neurale, minimizzando l'errore di 
predizione.
Fasi principali:
1. Forward pass: L'input passa attraverso i layer della rete, si ottiene un output e si calcola l'errore (loss)
2. Backward pass: Si calcola il gradiente della funzione di errore rispetto ai pesi (∂L/∂w), si applica la regola della catena (derivate composte)
3. Update: I pesi vengono aggiornati con una discesa del gradiente: w←w−η⋅∂L∂w dove η è il learning rate
Obiettivo: Ottimizzare tutti i parametri della rete per ridurre l'errore globale tra output previsto e desiderato.
6

## Pagina 7

Objective Function Optimization
L'objective function (o funzione obiettivo) misura quanto il modello è lontano dal comportamento desiderato. Viene usata per guidare 
l'apprendimento.
Funzioni di costo comuni: Errore quadratico medio (MSE) – per regressione, Cross-entropy loss – per classiﬁcazione, Negative 
Log-Likelihood – in modelli probabilistici
Ottimizzazione: Il processo di minimizzazione della funzione di costo avviene tramite algoritmi come: Gradient Descent (discesa del 
gradiente), Stochastic Gradient Descent (SGD), Adam (adaptive moment estimation)
✅
 Senza un obiettivo ben deﬁnito e una strategia di ottimizzazione efficiente, l'addestramento del modello non convergerà verso buone 
prestazioni.
7

## Pagina 8

Supervised Learning
Input
Dati di esempio etichettati
Modello
Elabora i dati e produce una previsione
Confronto
✅
 Confronto con il target etichettato
❌
 Calcolo dell'errore → aggiornamento dei 
pesi
L'apprendimento supervisionato è un paradigma in cui il modello impara da esempi etichettati.
🧠
 Esempi NLP:
Classiﬁcazione di sentiment:
• Input: "Questo ﬁlm è bellissimo"
• Target: positivo
Named Entity Recognition (NER):
• Input: "Mario lavora per Google a Milano"
• Target: [PER, ORG, LOC]
✅
 Vantaggi:
• Alta precisione su task speciﬁci
❌
 Limiti:
Richiede grandi dataset etichettati a mano
8

## Pagina 9

Unsupervised Learning
L'apprendimento non supervisionato avviene senza etichette: il modello apprende pattern e struttura dai dati grezzi.
Obiettivo
Scoprire regolarità 
nascoste
Rappresentazioni compatte 
e semantiche
Word Embeddings
(Word2Vec, GloVe):
Imparano che "gatto" e 
"cane" sono simili dai 
contesti
Topic Clustering
Raggruppa documenti 
secondo argomenti latenti
Pretraining LLM
Il modello impara a predire 
parole senza etichette 
manuali
✅
 Vantaggi:
• Scalabile: usa grandi quantità di testo grezzo
❌
 Limiti:
• Nessun controllo diretto sul comportamento appreso
9

## Pagina 10

Reinforcement Learning
L'apprendimento per rinforzo è un paradigma in cui il modello (agente) interagisce con un ambiente e apprende massimizzando una ricompensa.
Stato
Situazione attuale 
dell'ambiente
Azione
Decisione presa dall'agente
Ricompensa
Feedback sull'efficacia dell'azione
Apprendimento
Aggiornamento della strategia
🧠
 Esempi NLP:
RLHF (Reinforcement Learning from Human Feedback):
• Il modello genera più risposte
Un modello di ricompensa le valuta
Il modello viene aggiornato per massimizzare l'approvazione 
umana
Dialog systems: 
migliorano conversazioni attraverso feedback interattivo
✅
 Vantaggi:
• Apprendimento basato su obiettivi ﬁnali (non solo etichette)
❌
 Limiti:
• Complesso da ottimizzare
• Difficile stabilire ricompense corrette e stabili
10

## Pagina 11

Perceptron – The First Neural Network Unit
Il perceptron è l'unità base delle reti neurali artiﬁciali, proposta da Frank Rosenblatt (1958).
🔸
 Struttura:
Tipica attivazione: funzione di soglia o sigmoide
🧠
 Esempi NLP:
• Classiﬁcazione binaria: email spam vs. non spam
• Tagging POS con feature di base
✅
 Vantaggi:
• Intuitivo e interpretable
• Base per modelli più complessi (MLP , RNN)
❌
 Limiti:
Lineare: non separa dati non linearmente separabili
• Non adatto da solo a sequenze o linguaggio naturale complesso 11

## Pagina 12

LSTM – Long Short-Term Memory
Gates (Porte di Controllo)
Input gate: decide cosa aggiungere
Forget gate: decide cosa dimenticare
Output gate: decide cosa restituire
Stato della Cella
Mantiene uno stato della cella CtC_tCt , separato dallo stato nascosto hth_tht 
Applicazioni NLP
Traduzione automatica sequenziale
Generazione musicale o testuale
Analisi di serie temporali linguistiche
Vantaggi e Limiti
✅
 Gestisce dipendenze lunghe nel tempo
✅
 Mitiga il problema del vanishing gradient
❌
 Computazionalmente più pesante
❌
 Sostituito in molti contesti dai Transformer
Le LSTM sono una variante evoluta delle RNN, progettata per superare il problema della memoria a lungo termine.
12

## Pagina 13

Feed-Forward Neural Network (FFNN)
Input Layer
Riceve i dati iniziali
Hidden Layers
Uno o più strati intermedi di elaborazione
Output Layer
Produce il risultato ﬁnale
Le reti neurali feed-forward sono la forma più semplice di rete neurale: i dati ﬂuiscono in avanti, senza cicli o memoria interna.
🧠
 Esempi NLP:
• Classiﬁcazione binaria o multi-classe (es. analisi del sentiment)
• Moduli ﬁnali per task come NER, POS tagging
Transformer: ogni layer contiene una rete feed-forward per ogni token
✅
 Vantaggi:
• Semplice da implementare
• Estremamente ﬂessibile (universale per l'approssimazione di funzioni)
Costruisce pattern gerarchici via layers profondi
❌
 Limiti:
Non ha memoria temporale → non adatta a sequenze
Funziona bene solo con input indipendenti
13

## Pagina 14

Part 3: Natural Language 
Processing (NLP)
NLP consente ai computer di leggere, comprendere e generare 
linguaggio umano.
Unisce linguistica, informatica e apprendimento automatico.
Obiettivo: creare sistemi che interagiscono con l'uomo in linguaggio 
naturale.
Esempio: "Prenotami un volo per Roma." – il sistema capisce 
l'intenzione dell'utente.
14

## Pagina 15

Why is NLP Important?
Motori di ricerca
"ristorante sushi vicino a me"
Traduzione automatica
"Buongiorno" → "Good morning"
Assistenti virtuali
"Che tempo farà domani?"
Raccomandazioni
recensioni analizzate per consigliare ﬁlm/libri.
L'NLP è ovunque: Gmail, WhatsApp, Siri, ChatGPT...
15

## Pagina 16

Core Challenges in NLP
Ambiguità
"Il professore ha parlato con lo 
studente del progetto." → Di chi è 
il progetto?
"Ho visto un uomo con un 
telescopio."
• L'uomo aveva un telescopio?
• Oppure io usavo il telescopio 
per vedere l'uomo?
Testo informale
"nn ho voglia 😩
" – abbreviazioni, 
emoji, linguaggio social.
Variazione linguistica
"Ci vediamo dopo." = "A dopo!"
Dialetti: "Andiamo al mare" vs. 
"Jemo al mare"
16

## Pagina 17

Natural Language Understanding (NLU)
Estrae signiﬁcato strutturato da frasi non strutturate.
Intent Recognition
"Imposta una sveglia alle 7" → Intenzione: ImpostaSveglia
NER – Riconoscimento Entità Nominate
"Prenota un treno da Milano a Firenze domani." → Milano (LOC), Firenze (LOC), domani (DATA)
Analisi del Sentimento
"Questo prodotto è pessimo!" → Sentimento: Negativo
Input per chatbot
"Mi serve un taxi per l'aeroporto."
17

## Pagina 18

Natural Language Generation (NLG)
Genera frasi coerenti e rilevanti a partire da dati o strutture.
Riassunto
Input: articolo → Output: "Incendio 
domato in 2 ore."
Risposte nei dialoghi
Utente: "A che ora chiude il 
negozio?" → Bot: "Alle 19:30."
Traduzione automatica
"How are you?" → "Come stai?"
Creazione di contenuti
Email automatiche, report, annunci 
pubblicitari.
18

## Pagina 19

NLU vs. NLG – Comparison
NLU (Comprendere) NLG (Generare)
Obiettivo Capire il testo Scrivere il testo
Input "Prenota un tavolo per due" {intenzione: PrenotaTavolo, orario: 
20:00}
Output Intenzione + slot "Ho prenotato un tavolo per due 
alle 20:00."
In un chatbot Analizza l'input dell'utente Produce una risposta naturale
19

## Pagina 20

Tokenization – What is a Token?
Un token è un'unità minima del testo elaborata da un 
modello NLP .
Può essere: parola, punteggiatura, o sottoparte di parola 
(subword).
Esempi in italiano:
• Frase: "Adoro la pizza!" → ["Adoro", "la", "pizza", "!"]
• Subword: "incomprensibile" → ["in", "comprens", 
"ibile"]
Importanza:
I token sono l'input dei modelli NLP .
Inﬂuiscono su:
• Comprensione del testo
• Velocità ed efficienza
• Prestazioni del modello
20

## Pagina 21

Tokenization
Divisione del testo
Divide il testo in parole o sottoparti 
più semplici.
"Adoro la pizza!" → ["Adoro", "la", 
"pizza", "!"]
Subword tokenization
Aiuta con parole sconosciute o 
complesse:
"Incomprensibile" → ["in", 
"comprens", "ibile"]
Applicazione
Utile per lingue morfologicamente 
complesse.
21

## Pagina 22

Part-of-Speech (POS) Tagging
Assegna a ogni parola una categoria grammaticale.
Esempio
"Maria corre 
velocemente."
• Maria → NOUN
• corre → VERB
• velocemente → ADV
Applicazioni
• Traduzione automatica
• Analisi grammaticale
• Parsing sintattico
22

## Pagina 23

Named Entity Recognition (NER)
Riconosce nomi propri e informazioni concrete nel testo.
PERSONA
Luca
LOCALITÀ
Roma
ORGANIZZAZIONE
Google
DATA
martedì
Esempio: "Luca ha un incontro a Roma con Google martedì."
Applicazioni:
• Estrazione da email/documenti
• Sommario notizie
• Risposte automatiche nei chatbot
23

## Pagina 24

Parsing – Understanding Sentence Structure
Parsing Dipendenze
Mostra come le parole si relazionano tra loro.
"Il cane insegue il gatto." → soggetto: cane, verbo: 
insegue, oggetto: gatto
Parsing Costituente
Analizza la struttura a frasi: NP , VP , ecc.
Visualizzabile con graﬁ o alberi.
24

## Pagina 25

NLP Before Deep Learning
era basata su metodi statistici e basati su regole esplicite.
🧱
 Tecniche principali:
Modelli a n-grammi: probabilità basate sulla frequenza di sequenze di parole
Bag-of-Words / TF-IDF: rappresentazione vettoriale senza ordine o contesto
Modelli probabilistici: HMM (Hidden Markov Model), Naive Bayes
SVM, Decision Trees per classiﬁcazione testuale
🔨
 Caratteristiche:
Richiedevano feature engineering manuale
• Sensibili a rumore, sinonimi, polisemia
• Limitata comprensione semantica
Dipendenza da regole linguistiche scritte a mano
⚠
 Limiti:
• Nessuna nozione di contesto
• Incapacità di gestire ambiguità semantica
• Prestazioni mediocri su compiti complessi (dialogo, riassunto, traduzione ﬂuida)
25

## Pagina 26

NLP After Deep Learning
Con il Deep Learning, l'NLP è passato da regole e statistiche a modelli neurali end-to-end che apprendono rappresentazioni contestuali e semantiche in modo automatico.
🔬
 Innovazioni chiave:
Word embeddings (Word2Vec, GloVe): vettori densi che catturano la semantica
Reti neurali ricorrenti (RNN, LSTM): gestione del contesto sequenziale
Transformers (BERT, GPT): elaborazione parallela, attenzione globale
Pretraining su larga scala → foundation models
📈
 Vantaggi:
• Apprendimento automatico di caratteristiche linguistiche profonde
Comprensione e generazione coerente e ﬂuente
Adattabilità tramite prompting o ﬁne-tuning
• Prestazioni all'avanguardia su:
• Classiﬁcazione
• Traduzione automatica
• Riassunto
• Question answering
➡ Il Deep Learning ha trasformato l'NLP in una disciplina più empirica, meno manuale e molto più efficace, spingendo la nascita degli attuali LLM come GPT, BERT, e ChatGPT.
26

## Pagina 27

A Common NN in NLP: Recurrent Neural Network
Architettura
Ogni unità RNN riceve:
• L'input attuale xtx_txt 
Lo stato precedente ht−1h_{t-1}ht−1 
Produce un nuovo stato hth_tht  e (opzionalmente) un output
Applicazioni NLP
• Modellazione del linguaggio: predire la prossima parola
• Analisi del sentiment su frasi
• Generazione di testo carattere per carattere
Vantaggi e Limiti
✅
 Vantaggi:
Usa dipendenze temporali
• Legge testo "naturalmente" da sinistra a destra
❌
 Limiti:
• Vanishing/exploding gradients
• Difficoltà nel mantenere informazioni lontane nel tempo (frasi lunghe)
Le RNN sono reti neurali progettate per elaborare sequenze di dati, una voce alla volta, mantenendo memoria del contesto passato.
27

## Pagina 28

NLP Applications
Analisi del Sentimento
"Servizio ottimo, personale gentile!" 
→ Positivo
Assistenti virtuali
"Che tempo fa oggi a Trento?"
Riassunto di documenti
Input: articolo scientiﬁco → Output: 
3 punti principali
Risposta a domande
"Quanto dista Roma da Napoli?"
28

## Pagina 29

Wrap-Up & Key Takeaways
1
2
3
4
5
Importanza 
dell'NLP
NLP è essenziale per il 
dialogo uomo-macchina.
Processo di 
Elaborazione
NLU interpreta → NLG 
risponde.
Compiti 
Fondamentali
Compiti chiave: 
tokenizzazione, POS, NER, 
parsing.
Applicazioni 
Pratiche
Esempi pratici: chatbot, 
traduttori, assistenti 
vocali.
Prossimi Passi
Word Embeddings to 
Transformers
29
