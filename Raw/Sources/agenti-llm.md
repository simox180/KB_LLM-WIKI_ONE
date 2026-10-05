---
Title: Agenti LLM
Reference: Raw/Files/Session 5 Agents.pdf
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Agenti LLM

Trascrizione automatica dal PDF originale; la struttura delle pagine e conservata nei marcatori.

===== PAGE 1

Large Language Models, 
Agent-Oriented Applications
✅
 Session 3: LLM Agents
    
Prof: S. Mahed Mousavi, Ph.D. 
 Assistant Professor 
 Dipartimento di Ingegneria e Scienza dell'Informazione
 Università di Trento


## Pagina 2

Architetture Orientate agli Agenti con LLM
🧠
 Gli LLM non servono solo per generare testo — possono diventare agenti autonomi che:
• Comprendono obiettivi
• Pianiﬁcano azioni
• Utilizzano strumenti
• Si adattano e ricordano
Oggi: come passare dalla chat → al ragionamento → all'azione.

## Pagina 3

Che Cos'è un Agente LLM?
Deﬁnizione
💡
 Un Agente LLM si comporta 
come un assistente digitale che:
Caratteristiche
• Comprende un obiettivo
• Ragiona attraverso più 
passaggi
• Agisce utilizzando strumenti o 
API
• Si adatta in base ai risultati
• Può ricordare contesto o fatti
Formula
🧠
 Agente = LLM + logica + 
memoria + uso di strumenti

## Pagina 4

Comportamento dell'Agente – Pensiero Simile 
all'Umano
Comprendere l'intento
"Voglio dormire meglio."
Pianiﬁcare i passaggi
"Ridurre la caffeina, stabilire una routine del sonno."
Agire
"Aprire il calendario, impostare promemoria."
Valutare
"Ha funzionato? Dovrei modiﬁcare?"
Questo ciclo continua ﬁno a quando un obiettivo non viene soddisfatto.

## Pagina 5

Componenti Principali degli Agenti LLM
Componente Scopo
🧠
 Pianiﬁcatore Suddivide gli obiettivi in attività (tramite prompting)
🧾
 Memoria Memorizza fatti e conversazioni passate
⚙
 Uso degli strumenti Chiama API, esegue codice, recupera dati
🔁
 Feedback Reagisce ai risultati, riprova, si adatta
Insieme consentono un comportamento dinamico e contestuale.

## Pagina 6

Memoria e Strumenti nella Pratica
🧠
 Tipi di memoria:
A breve termine: all'interno di un prompt / ﬁnestra di 
contesto
A lungo termine: salvata esternamente (DB vettoriale, ﬁle, 
log)
⚙
 Esempi di utilizzo degli strumenti:
• Calcolatrice
• Ricerca web
• API meteo
• Calendario / database / esecuzione di codice
Gli agenti utilizzano strumenti quando l'LLM da solo non può rispondere in modo affidabile.

## Pagina 7

Architetture e Modelli di Agenti
ReAct (Reason + Act)
Pensare, agire, osservare, 
ripetere.
Plan-and-Execute
Pianiﬁcare tutti i passaggi 
prima, poi eseguirli uno per 
uno.
Stile Toolformer
Imparare quando utilizzare gli 
strumenti durante la 
generazione.
🧩
 Tutti utilizzano prompting + ﬂusso di controllo + strumenti.

## Pagina 8

Esempio – Flusso di Lavoro dell'Agente
Comprendere l'obiettivo
🎯
 Utente: "Voglio risparmiare denaro 
questo mese"
1
Suggerire azioni
Tracciare le spese, ridurre i pasti fuori 
casa
2
Chiedere il tuo budget
Raccogliere informazioni necessarie
3
Utilizzare la calcolatrice
Stimare i risparmi
4
Fornire un piano di spesa 
giornaliero
Dettagliare le azioni concrete
5
🔁
 Se dici: "È troppo rigido" → ripianiﬁca
🧠
 Se gli hai detto che vivi a Milano → consigli locali

## Pagina 9

Framework per Agenti nel Mondo Reale
AutoGPT
Agenti completamente 
autonomi (sperimentale)
BabyAGI
Pianiﬁcazione basata su 
attività con memoria
LangGraph
Flussi di lavoro 
multi-agente con stato
CrewAI
Team di agenti con ruoli e 
obiettivi
LangChain
Strumenti generali per 
agenti + catene + memoria
Questi permettono agli LLM di interagire con API, documenti, strumenti.

## Pagina 10

Rischi e Limitazioni
Rischio Causa Mitigazione
Allucinazione LLM inventa informazioni o 
strumenti falsi
Validazione, fondamento (RAG)
Loop inﬁniti Logica di pianiﬁcazione errata o 
cicli di feedback
Aggiungere limiti di passaggi
Azioni errate Uso improprio degli strumenti, 
output ambiguo
Function calling + controlli
Eccessiva sicurezza Risposta ﬂuente, ma errata Logging, human-in-the-loop
È necessario limitare, testare e osservare gli agenti nell'uso reale.

## Pagina 11

Riepilogo – Cosa Rende un Agente LLM
Sistemi
Pensare oltre la chat
Componenti
LLM + memoria + API strumenti
Strutture
ReAct o Plan-and-Execute
Framework
AutoGPT, LangGraph, CrewAI
Rischi
Allucinazione, pianiﬁcazione errata, 
costo
✅
 Recap:

## Pagina 12

Conclusione – Perché Questo è Importante
🚀
 Gli agenti LLM sono il prossimo livello di intelligenza nelle app:
• Assistenti di ricerca
• Agenti di codice
• Bot per ﬂussi di lavoro
• Analisti di dati
• Pianiﬁcatori personali
📌
 Non costruire una chatbot usa e getta. Costruisci qualcosa che pensa, agisce, si adatta.
Prossimo: Simuliamone uno.
