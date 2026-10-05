---
Title: Da word embeddings a Transformer
Reference: Raw/Files/Session 2 _ From WE to Transformers(1).pdf
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Da word embeddings a Transformer

Trascrizione automatica dal PDF originale; la struttura delle pagine e conservata nei marcatori.

===== PAGE 1

Large Language Models, 
Agent-Oriented Applications
✅
 Session 2: From Word Embeddings to 
Transformers
Prof: S. Mahed Mousavi, Ph.D. 
 Assistant Professor 
 Dipartimento di Ingegneria e Scienza dell'Informazione
 Università di Trento
1

## Pagina 2

What is Meaning Representation (MR)?
Rappresentazione del Signiﬁcato
Una rappresentazione del signiﬁcato trasforma frasi del linguaggio naturale in strutture computazionali che 
possono essere interpretate, confrontate e utilizzate dai modelli.
È il primo passo per insegnare alle macchine a comprendere il linguaggio umano.
Esempio di Frase
Frase: "Il gatto dorme. Il cane guarda il gatto. Il gatto non guarda il cane."
2

## Pagina 3

Bag of Words (BoW)
Deﬁnizione
Conta quante volte ogni parola del vocabolario appare, ignorando ordine, 
sintassi e semantica.
Esempio
Vocabolario: ["gatto", "cane", "dorme", "guarda", "non"] Frase → Vettore 
BoW: ["gatto": 3, "cane": 2, "dorme": 1, "guarda": 2, "non": 1] → [3, 2, 1, 2, 1]
Limiti
Non distingue "il gatto guarda il cane" da "il cane guarda il gatto"
Non sa chi fa l'azione → nessuna struttura
3

## Pagina 4

One-Hot Encoding
Deﬁnizione
Ogni parola → vettore binario unico nel vocabolario.
L'intera frase → sequenza di vettori (senza relazioni tra loro):
Esempio
Vocabolario: ["gatto", "cane", "dorme", "guarda", "non"]
"gatto" → [1, 0, 0, 0, 0]                              "cane" → [0, 1, 0, 0, 0]
"dorme" → [0, 0, 1, 0, 0]                           "guarda" → [0, 0, 0, 1, 0]
"non" → [0, 0, 0, 0, 1]
Limiti
"gatto" e "cane" sono semanticamente simili → ma i vettori sono ortogonali
Nessuna relazione tra parole → vettori totalmente scollegati
Alta dimensionalità e vettori sparsissimi
4

## Pagina 5

Limitations of Sparse 
Representations
Queste rappresentazioni non "capiscono" il signiﬁcato, ma solo la 
forma. Per catturare semantica e contesto, servono word 
embeddings e modelli neurali.
Forma
Le rappresentazioni 
sparse catturano 
solo la struttura 
superﬁciale del testo
Signiﬁcato
Manca la 
comprensione 
semantica profonda
Contesto
Non considerano il 
contesto in cui le 
parole appaiono
5

## Pagina 6

Motivation: From Sparse to Dense MRs
Problemi dei modelli 
tradizionali
I modelli tradizionali (BoW, 
TF-IDF) rappresentano le 
parole tramite vettori sparsi 
basati su frequenza.
Limitazioni principali
Nessuna informazione 
semantica, nessun uso del 
contesto, vettori molto lunghi 
e pieni di zeri → costosi 
computazionalmente
Soluzione
Rappresentazioni dense e 
distribuite, che riﬂettano 
signiﬁcato e somiglianza tra 
parole.
Esempio: "apple" in "apple è una compagnia tecnologica" = "apple" in "ho mangiato una mela" → errore semantico
6

## Pagina 7

Word Embeddings
Deﬁnizione
Un embedding è un vettore denso che rappresenta una 
parola in uno spazio continuo (es. 100-300 dimensioni).
Proprietà
Parole simili (semantica e contesto) → vettori simili.
Esempi
king - man + woman ≈ queen
Parigi - Francia + Italia ≈ Roma
Tecniche principali
Word2Vec (CBOW, Skip-Gram)
GloVe (Global Vectors)
FastText (basato su subword)
Limite importante: Ogni parola ha una sola rappresentazione → non 
gestisce signiﬁcati multipli.
7

## Pagina 8

Neural Networks for Language
Architettura
Le reti neurali sequenziali (RNN, LSTM, GRU) apprendono le relazioni tra parole in una frase.
Funzionamento
Elaborano il testo una parola alla volta, aggiornando uno stato interno.
Esempio
"La ragazza che hai incontrato ieri..." → LSTM riesce a "ricordare" che il soggetto è "ragazza".
Problemi
Difficoltà a gestire lungo termine
Computazione sequenziale → lenta
Non ottimale per frasi molto lunghe
8

## Pagina 9

Sequence-to-Sequence 
Models
Architettura encoder-decoder
Utile per traduzione, riassunto, Q&A
Encoder
Comprensione della frase input → vettore di stato
Decoder
Generazione parola per parola
9

## Pagina 10

Attention Mechanism
1 Soluzione
Soluzione al limite del vettore unico: attenzione.
Il modello calcola pesi per ogni parola dell'input → decide a 
quali parole dare più "importanza".
2 Esempio
"Come stai?"
Quando il decoder genera "How", l'attenzione si concentra 
su "Come" 
3 Vantaggi
Contesto più preciso
Maggiore interpretabilità (si può visualizzare l'attenzione)
Performance migliore in traduzione e riassunto
10

## Pagina 11

Transformer Architecture
Origine
Presentato nel 2017: "Attention is All You Need"
Novità: elimina completamente RNN → solo attenzione
Architettura modulare
Encoder: elabora input
Decoder: genera output
Componenti
Self-attention: ogni parola guarda tutte le altre
Positional encoding: aggiunge informazioni di posizione
Multi-head attention: esplora più relazioni simultaneamente
Feedforward + skip connection + normalizzazione
11

## Pagina 12

Transformer Applicazions
Traduzione automatica (Google Translate, DeepL)
Riassunto di documenti (es. legali, articoli scientiﬁci)
Assistenti virtuali e chatbot (ChatGPT, Alexa, Siri)
Analisi del sentiment e classiﬁcazione di testi
Correzione grammaticale, completamento predittivo, Q&A
12

## Pagina 13

Transformer: Key Advantages
1
2
 3
4
Parallelizzazione
Elabora tutte le parole in 
parallelo → più veloce
Contesto lungo
Gestione efficace del 
contesto lungo
Scalabilità
Può essere ampliato ﬁno a 
miliardi di parametri
Versatilità
Modelli pre-addestrati 
general-purpose → 
adattabili a molti task
13

## Pagina 14

Conclusion
1 Evoluzione
Da vettori sparsi → word embeddings → reti neurali → Transformer
2 Importanza
I Transformer sono oggi la tecnologia fondamentale per l'elaborazione del linguaggio naturale
3 Impatto
Hanno reso possibile la nascita di LLMs come GPT, Bard, Claude, LLaMA...
4 Prossima lezione
🔍
 NLP Applications w. Large Language Models
✍
 Introduzione al prompt engineering
14
