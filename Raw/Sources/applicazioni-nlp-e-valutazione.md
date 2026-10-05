---
Title: Applicazioni NLP e valutazione
Reference: Raw/Files/Session 3 _ NLP Application.pdf
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Applicazioni NLP e valutazione

Trascrizione automatica dal PDF originale; la struttura delle pagine e conservata nei marcatori.

===== PAGE 1

Large Language Models, 
Agent-Oriented Applications
✅
 Session : NLP Applications
Prof: S. Mahed Mousavi, Ph.D. 
 Assistant Professor 
 Dipartimento di Ingegneria e Scienza dell'Informazione
 Università di Trento
1

## Pagina 2

Lecture 3 – NLP 
Applications
2

## Pagina 3

Sentiment Analysis
Obiettivo
Classiﬁcare la polarità dell'opinione espressa in un testo Etichette 
tipiche: positivo, negativo, neutro
Come funziona
Apprendimento supervisionato su dati testuali etichettati
Modelli: SVM, Naive Bayes, Reti Neurali, BERT
Esempi
"Questo prodotto è fantastico!" → Positivo
"Mi aspettavo di meglio." → Neutro
"Servizio lento e scortese." → Negativo
Sﬁde
Ironia, ambiguità, contesto culturale
3

## Pagina 4

Emotion Recognition
Obiettivo
Rilevare l'emozione nel 
testo (più ﬁne-grained 
del sentiment)
Etichette comuni: gioia, 
rabbia, tristezza, paura, 
disgusto, sorpresa, 
entusiasmo
Differenze rispetto 
al sentiment
Il sentiment misura 
polarità, l'emozione 
misura stato psicologico 
speciﬁco
Può essere multi-label 
(es. triste + deluso)
Esempi
"Finalmente ho ﬁnito!" → 
Sollievo
"Sei sempre lo stesso..." 
→ Rabbia + delusione
Sﬁde
Ambiguità semantica
Variabilità interpersonale
4

## Pagina 5

Text Summarization
Obiettivo
Generare una versione breve e informativa di un testo più 
lungo
Tipologie
Estrattiva: seleziona frasi esistenti
Astrattiva: riscrive in linguaggio naturale
Esempio:
Testo completo: "La NASA ha lanciato un satellite per lo studio climatico"
Estrattivo
"La NASA ha lanciato un satellite"
Astrattivo
"Nuova missione NASA per il 
monitoraggio del clima"
Applicazioni
News, documenti legali, report 
medici, email
5

## Pagina 6

Summarization
La sintesi automatica (summarization) è il processo di ridurre un testo lungo a una versione più breve, preservandone le 
informazioni chiave.
📌
 Due approcci principali:
🟦
 Extractive Summarization
Seleziona frasi originali rilevanti dal testo
• Non riformula, non parafrasa
• Basata su punteggi di rilevanza (es. TF-IDF, TextRank, BERT embeddings)
Esempio: Testo originale: 
"La NASA ha lanciato un nuovo satellite per studiare il clima. La missione durerà tre anni." Riassunto estrattivo: 
"La NASA ha lanciato un nuovo satellite. La missione durerà tre anni."
6

## Pagina 7

Summarization
La sintesi automatica (summarization) è il processo di ridurre un testo lungo a una versione più breve, preservandone le 
informazioni chiave.
📌
 Due approcci principali:
🟨
 Abstractive Summarization
Genera nuove frasi usando comprensione semantica e riformulazione
• Usa modelli neurali (es. LLM, T5, GPT)
• Più simile a come riassume un essere umano
Esempio: Testo originale: 
"La NASA ha lanciato un nuovo satellite per studiare il clima. La missione durerà tre anni." "Riassunto astrattivo:
"La NASA ha avviato una missione triennale per studiare il clima tramite un nuovo satellite.""
7

## Pagina 8

Topic Modeling – Clustering
Obiettivo
Raggruppare documenti in 
base a temi latenti, senza 
etichette
Metodo
Apprendimento non 
supervisionato (es. LDA, 
K-Means)
Rappresentazioni
TF-IDF, BERT embeddings
Esempio:
Cluster A
"borsa, investimenti, azioni"
Cluster B
"covid, vaccini, ospedali"
Usi: esplorazione contenuti, analisi tendenze, segmentazione semantica
8

## Pagina 9

Topic Modeling – Classiﬁcation
Obiettivo
Assegnare un'etichetta 
tematica a ogni testo
2 Metodo
Apprendimento supervisionato 
(es. classiﬁcatori neurali)
Dataset
Con topic predeﬁniti
Esempio:
Testo: "Un nuovo algoritmo AI genera testo poetico."
→ Etichetta: Tecnologia / Intelligenza Artiﬁciale
Usi: moderazione contenuti, catalogazione, raccomandazione
9

## Pagina 10

Question Answering (QA)
Obiettivo
Rispondere automaticamente a 
domande su un testo
Estrattivo
Estrae risposta dal testo
Generativo
Produce nuova risposta
Sﬁde
Ambiguità, domande implicite, ragionamento logico
Esempio:
Contesto: "Marie Curie ha scoperto il radio nel 1898." → Domanda: "Quando ha scoperto il radio?" → Risposta: "Nel 1898"
10

## Pagina 11

Conversational Agents
Task-oriented
Assistenti per compiti 
(booking, helpdesk)
Open-domain
Chatbot generici (es. ChatGPT)
NLU
Comprensione linguistica
Dialog Manager
Gestione dialogo
NLG
Generazione linguaggio
Esempio:
Utente: "Prenota un tavolo per due alle 20" Bot: "Per quale ristorante?"
11

## Pagina 12

Intent Detection and Slot Filling
Intent Detection
Identiﬁca lo scopo della frase utente
Slot Filling
Estrae informazioni strutturate 
(entità)
Applicazioni
Chatbot, assistenti vocali, sistemi IVR
Esempio:
Utente: "Voglio volare da Milano a Madrid lunedì" → Intent: PrenotazioneVolo → Slots:
• origine: Milano
• destinazione: Madrid
• data: lunedì
12

## Pagina 13

Machine Translation
Sistemi a regole
Modelli statistici
Neural Machine Translation (NMT)
Obiettivo: tradurre testi da una lingua a un'altra in modo coerente e ﬂuente
Tecnologie attuali: Transformer (es. MarianMT, mBART, NLLB)
Esempio:
Input
"Il tempo è bellissimo oggi."
Output
"The weather is beautiful today."
Sﬁde: idiomi, grammatica complessa, contesto interfrase
13

## Pagina 14

Code Generation (NLP → Code)
Obiettivo: generare codice sorgente da input in linguaggio naturale
Tecniche:
• LLM addestrati su codice (Codex, StarCoder, CodeLLaMA)
• Prompting con esempi
Esempio:
Prompt: "Scrivi una funzione Python che calcola la media di una lista" → Output: funzione Python corretta
Applicazioni: assistenti di programmazione, autocompletamento IDE, educational tools
14

## Pagina 15

Story Generation (Creative NLP)
Narrativa Fantastica
Generazione di mondi immaginari con personaggi fantastici
Fantascienza
Creazione di scenari futuristici con tecnologie avanzate
Gialli e Misteri
Sviluppo di trame intricate con colpi di scena
Obiettivo: generare testi narrativi coerenti, creativi e coinvolgenti
Caratteristiche:
• Richiede controllo su stile, tono, coerenza a lungo termine
• Usa modelli generativi (GPT, T5, LLaMA) con ﬁne-tuning su narrativa
Esempio:
Prompt: "Scrivi l'inizio di una storia fantasy su un mago cieco che salva il suo villaggio" → Output: testo narrativo coerente
Sﬁde: coerenza dei personaggi, progressione logica, evitare ripetizioni
15

## Pagina 16

Evaluation – Automatic Metrics for NLP Applications
Task Metriche comuni
Sentiment analysis Accuracy, F1-score
Emotion detection Macro-F1, Recall
Summarization ROUGE-1, ROUGE-L
Machine translation BLEU, chrF, COMET
Question answering Exact Match, F1
Topic modeling Coherence Score
Clustering Silhouette Score, ARI
Ogni applicazione NLP ha metriche speciﬁche di valutazione automatica.
Esempio:
0.45
ROUGE-L
Buona sovrapposizione col riassunto di riferimento
0.38
BLEU
Buona fedeltà nella traduzione⚠
 Limiti:
• Non sempre misurano semantica, tono o contesto
Per compiti complessi è necessaria valutazione umana
16

## Pagina 17

Evaluation – Human Judgments
✅
 Vantaggi:
Coglie aspetti semantici non rilevabili con metodi automatici
• Valuta sfumature: tono, empatia, rispetto del contesto
• Necessaria in RLHF → ranking di risposte
❌
 Svantaggi:
• Costosa e lenta
Soggettiva: giudizi variabili tra annotatori
• Difficile da replicare
• Non scalabile per valutazioni massicce
La valutazione umana resta il metodo più affidabile per giudicare:
• Utilità pratica
• Correttezza fattuale
• Coerenza logica
• Qualità stilistica
➡ Strategia comune:
Usare metriche automatiche per monitoraggio costante
• valutazione umana per analisi approfondita o tuning critico
17

## Pagina 18

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
Compiti 
Fondaentali
Compiti chiave: 
tokenizzazione, POS, NER, 
parsin.
Evaluation
Automatic vs. Human 
Evaluation
Prossimi Passi
LLMs
Applicazioni 
Pratiche
Esempi pratici: chatbot, 
traduttori, assistenti 
vocali.
18
