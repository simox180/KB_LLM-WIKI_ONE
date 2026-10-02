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
tags:
  - "concept" # topic | concept | entity | project | log
topics: []
status: seed
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources: []
source_count: 0
aliases: []
---
```

## Campi obbligatori

| Campo | Tipo | Regola |
| --- | --- | --- |
| `tags` | lista di stringhe | Contiene almeno un tag tra `topic`, `concept`, `entity`, `project` e `log`. |
| `topics` | lista | Argomenti associati alla nota; può essere vuota. |
| `status` | stringa | `seed` è il valore predefinito del template. |
| `created` | data ISO `YYYY-MM-DD` | Data di creazione della nota. |
| `updated` | data ISO `YYYY-MM-DD` | Data dell'ultima modifica sostanziale. |
| `sources` | lista di wikilink | Il template può essere vuoto; una nota compilata deve collegare una o più fonti sotto `Raw/Sources/`. Ogni link deve puntare a un file esistente. |
| `source_count` | intero | Uguale al numero di elementi in `sources`. |
| `aliases` | lista di stringhe | Alias della nota; può essere vuota. |

## Campi opzionali

| Campo | Tipo | Uso |
| --- | --- | --- |
| `summary` | stringa | Riassunto conciso, adatto al catalogo. |
| `source_locator` | stringa o lista | Pagina, sezione, timestamp o altro localizzatore nella fonte. |
| `related` | lista di wikilink | Note compilate correlate in `Wiki/`. |
| `reviewed` | data ISO | Data dell'ultima verifica delle fonti. |

## Regole di validazione

- `sources` non può puntare a `Wiki/`, URL non verificati o percorsi esterni a `Raw/Sources/`.
- In una nota compilata `sources` non può essere vuoto; `sources: []` e `source_count: 0` sono riservati al template vuoto.
- `source_count` deve corrispondere esattamente al numero di elementi in `sources`.
- Le date devono essere reali, in formato ISO, e `updated` non può precedere `created`.
- I valori enum sono in minuscolo. Le chiavi usano `snake_case` se composte.
