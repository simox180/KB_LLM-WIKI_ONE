---
title: Knowledge quality
tags:
  - llm-wiki
  - quality
---

# Knowledge quality

Questo documento definisce la qualità semantica dell'ingestione e della compilazione. Si applica insieme agli schemi strutturali, senza introdurre stati o registri aggiuntivi.

## Esame e copertura della fonte

- Durante l'ingestione esamina integralmente la fonte normalizzata, anche se la elabori per blocchi. La lettura completa e la compilazione completata sono attività distinte: non dedurre la seconda dalla prima.
- Conserva quanto è rilevante e presente nella fonte: definizioni, funzionamento, formule, parametri, esempi significativi, condizioni e limiti.
- Non aggiungere contenuti assenti dalla fonte per riempire sezioni. Non dichiarare completata una fonte con parti sostanziali ancora omesse o non verificate.

## Fedeltà e rintracciabilità

- Se l'estrazione testuale non basta per immagini, tabelle o formule, verifica l'originale. Se non è possibile verificarlo, dichiaralo esplicitamente e non trasformarlo in un fatto.
- Rendi rintracciabili le affermazioni con fonte e posizione (pagina, sezione, timestamp o altro localizzatore) quando disponibili.
- Distingui chiaramente il contenuto della fonte da sintesi e inferenze. Qualifica le inferenze e dichiara limiti, ambiguità o incertezze della fonte.

## Integrazione nella Wiki

- Cerca prima le note esistenti nel catalogo; aggiorna o integra quelle compatibili, evita duplicati e aggiungi collegamenti pertinenti.
- I controlli strutturali confermano schema, percorsi e collegamenti. La revisione semantica verifica fedeltà e copertura: la sola presenza di note collegate non prova la completezza della compilazione.
