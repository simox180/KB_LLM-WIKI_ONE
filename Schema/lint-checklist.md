---
title: Lint checklist
tags:
  - llm-wiki
  - quality
---

# Lint checklist

Questa checklist separa la validazione automatizzabile dalla revisione semantica. Un collegamento tra una nota e una fonte attesta soltanto la provenienza dichiarata: non dimostra che la compilazione sia completa.

## Controlli automatici

- [ ] Esegui `doctor`, `build`, `lint` e `source-lint` quando applicabili.
- [ ] Build, lint e source-lint terminano con successo.
- [ ] Nomi, percorsi, tag e frontmatter delle note modificate rispettano `Schema/naming-conventions.md` e `Schema/frontmatter-schema.md`.
- [ ] Ogni `sources` di una nota compilata punta a un file esistente sotto `Raw/Sources/` e `source_count` è coerente.
- [ ] Catalogo e indici generati sono aggiornati o verificati secondo gli strumenti del repository.

## Revisione del contenuto

- [ ] Per un'ingestione, la fonte è stata esaminata integralmente e la compilazione è stata confrontata con `Schema/knowledge-quality.md`.
- [ ] Affermazioni, citazioni e localizzatori sono supportati dalle fonti collegate e non sono inventati.
- [ ] Definizioni, funzionamento, formule, parametri, esempi significativi, condizioni e limiti rilevanti sono stati conservati oppure la loro omissione è giustificata dalla pertinenza della nota.
- [ ] Immagini, tabelle e formule con estrazione insufficiente sono state verificate sull'originale o dichiarate non verificabili.
- [ ] Sono distinguibili contenuto della fonte, sintesi e inferenze; incertezze, conflitti e limiti sono dichiarati.
- [ ] Sono state integrate le note esistenti e aggiunti collegamenti pertinenti senza duplicare conoscenza.
- [ ] Nessuna fonte è considerata semanticamente completa solo perché collegata a una nota, né se restano parti sostanziali omesse o non verificate.
