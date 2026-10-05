---
Title: Architettura e processo della LLM Wiki
Reference: Raw/Files/_LLM-WIKI_ Schema.png; Raw/Files/LLM_WIK_CORE Schema.png
Created: 2026-10-05
Processed: true
tags:
  - source
---

# Architettura e processo della LLM Wiki

Trascrizione dei due schemi.

## LLM Wiki: three layers

- **Raw**: materiale sorgente acquisito, inclusi articoli, trascrizioni, clip ed estratti PDF; il principio indicato è preservare la fonte.
- **Wiki**: conoscenza compilata per persone e agenti, organizzata in topic, concept, entity e project; il principio indicato è creare note piccole e riutilizzabili.
- **Schema + Agents**: AGENTS.md, schemi, template, skill e documentazione dei comandi; è il livello che rende ripetibile il comportamento.
- L'agente legge Schema, aggiorna Wiki e collega ogni affermazione a Raw.

## Core LLM Wiki workflow

1. Da un vault Obsidian vuoto si inizializza Git e si aggiunge `.gitignore`.
2. Si creano struttura, regole e template: Raw, Wiki, Schema, skill degli agenti e template delle note.
3. Si aggiungono strumenti: `wiki_tool.py`, documentazione comandi, hook setup e audit pubblico.
4. Il primo ingest aggiunge una fonte Raw posseduta e la compila in note Wiki focalizzate.
5. La validazione costruisce catalogo e indici, aggiorna il manifest delle fonti, esegue lint e consente la ricerca.
6. Il ciclo quotidiano è: aggiungere la fonte Raw, cercare nel catalogo, compilare o aggiornare le note Wiki, build e lint, interrogare la Wiki.
