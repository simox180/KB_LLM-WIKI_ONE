---
title: Frontmatter schema
tags:
  - llm-wiki
  - schema
---

# Frontmatter schema

Ogni nota compilata sotto `Wiki/` usa frontmatter YAML valido e adotta questo contratto minimo:

```yaml
---
title: Titolo leggibile della nota
type: concept # concept | procedure | reference | decision | index
status: draft # draft | reviewed | deprecated
sources:
  - "[[Raw/Sources/nome-fonte.ext]]"
created: 2026-10-02
updated: 2026-10-02
tags:
  - area-tematica
---
```

## Campi obbligatori

| Campo | Tipo | Regola |
| --- | --- | --- |
| `title` | stringa | Titolo umano, specifico e non vuoto. |
| `type` | enum | Uno tra `concept`, `procedure`, `reference`, `decision`, `index`. |
| `status` | enum | Uno tra `draft`, `reviewed`, `deprecated`. |
| `sources` | lista di wikilink | Una o più fonti in `Raw/`; nessuna fonte inventata. |
| `created` | data ISO `YYYY-MM-DD` | Data di creazione della nota. |
| `updated` | data ISO `YYYY-MM-DD` | Data dell'ultima modifica sostanziale. |
| `tags` | lista di stringhe | Almeno un tag tematico conforme alle convenzioni. |

## Campi opzionali

| Campo | Tipo | Uso |
| --- | --- | --- |
| `aliases` | lista di stringhe | Varianti utili per la ricerca in Obsidian. |
| `summary` | stringa | Riassunto conciso, adatto al catalogo. |
| `source_locator` | stringa o lista | Pagina, sezione, timestamp o altro localizzatore nella fonte. |
| `related` | lista di wikilink | Note compilate correlate in `Wiki/`. |
| `reviewed` | data ISO | Data dell'ultima verifica delle fonti. |

## Regole di validazione

- `sources` non può puntare a `Wiki/`, URL non verificati o percorsi esterni a `Raw/`.
- Una nota `reviewed` deve avere fonti accessibili e un contenuto verificabile rispetto ad esse.
- Le date devono essere reali, in formato ISO, e `updated` non può precedere `created`.
- I valori enum sono in minuscolo. Le chiavi usano `snake_case` se composte.
