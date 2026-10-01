---
title: Lint checklist
tags:
  - llm-wiki
  - quality
---

# Lint checklist

Esegui questa checklist insieme agli script di build, lint e controllo fonti prima di ogni commit.

## Struttura

- [ ] Le note compilate nuove o modificate sono esclusivamente in `Wiki/`.
- [ ] I file in `Raw/Sources/` sono stati trattati come sorgenti e non come note compilate.
- [ ] Nomi, percorsi e tag rispettano `Schema/naming-conventions.md`.
- [ ] Il frontmatter YAML è presente e valido per ogni nota `Wiki/` modificata.

## Provenienza

- [ ] Ogni nota compilata ha uno o più `sources` che puntano a file esistenti in `Raw/`.
- [ ] Ogni affermazione fattuale o citazione è supportata da una fonte collegata.
- [ ] Citazioni e localizzatori non sono stati inventati.
- [ ] Limiti, conflitti e incertezze delle fonti sono indicati chiaramente.

## Indici e controlli

- [ ] È stata consultata `Wiki/catalog.jsonl` prima di aprire un contesto Raw ampio.
- [ ] Catalogo e indici richiesti sono stati rigenerati o verificati.
- [ ] Build completata con successo.
- [ ] Lint completato con successo.
- [ ] Controllo delle fonti completato con successo.
