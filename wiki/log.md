---
title: "Wiki Log"
type: log
created: 2026-04-07
updated: 2026-04-07
---

# Wiki Log

Append-only chronological record of all wiki operations. Each entry uses a parseable prefix.

**Tip:** `grep "^## \[" wiki/log.md | tail -10` returns the last 10 entries.

---

## [2026-04-07] init | Wiki Initialization
Scaffolded the LLM Wiki system with the following structure:
- Created: directory structure (`raw/`, `wiki/`, `.agents/workflows/`)
- Created: [[index]], [[log]], [[overview]]
- Created: `SCHEMA.md` (wiki conventions and workflows)
- Created: Antigravity workflows (`/ingest`, `/query`, `/lint`)

## [2026-04-07] ingest | LLM Wiki — Andrej Karpathy
Ingested Karpathy's LLM Wiki pattern document. Core idea: LLM builds & maintains a persistent wiki instead of RAG. 3-layer architecture (raw/wiki/schema), 3 operations (ingest/query/lint). Historical connection to Vannevar Bush's Memex (1945).
- Created: [[llm-wiki-karpathy]], [[andrej-karpathy]], [[vannevar-bush]], [[obsidian]], [[qmd]], [[llm-wiki-pattern]], [[rag]], [[memex]]
- Updated: [[index]], [[overview]]

## [2026-04-08] ingest | The Ultimate Sales Training for 2026 Full Course
Ingested Alex Hormozi's extensive sales masterclass covering operational multipliers, extreme volume repetition, objection handling frameworks, and sales mindset.
- Created: [[hormozi-ultimate-sales-2026]], [[alex-hormozi]], [[sales-multipliers]], [[volume-negates-luck]], [[aaa-method]], [[bamfam]], [[sales]]
- Updated: [[index]], [[overview]]

## [2026-04-08] ingest | If I Wanted To Grow An Audience In 2026, I'd Do This
Ingested Alex Hormozi's audience growth masterclass detailing the transition to interest media, the six content strategy changes, the SPCL framework for influence, and the distinction between branding and advertising.
- Created: [[hormozi-grow-audience-2026]], [[branding-vs-advertising]], [[spcl-framework]], [[interest-media]], [[brand-building]]
- Updated: [[alex-hormozi]], [[index]], [[overview]]

## [2026-04-08] ingest | After Closing 4000+ Sales — 3A Reframing Deep Dive
Ingested Alex Hormozi's detailed breakdown of the 3A Reframing framework with 5 ethical rules for objection handling. Enriched existing [[aaa-method]] concept page with new details.
- Created: [[hormozi-3a-reframing]]
- Updated: [[aaa-method]], [[index]]

## [2026-04-08] ingest | Batch ingest: raw/books/ (18 PDFs)
Batch ingested the entire $100M Playbook library and supplementary sales materials from raw/books/. This includes books, playbooks, and video transcripts from Alex Hormozi and Jeremy Miner.
- Created Sources: [[hormozi-100m-offers]], [[hormozi-100m-playbooks]], [[hormozi-100m-lost-chapters]], [[hormozi-100m-branding]], [[hormozi-sales-2025]], [[hormozi-9-sales-concepts]], [[hormozi-best-sales-training]], [[hormozi-sell-better-99]], [[miner-nepq-black-book]]
- Created Concepts: [[value-equation]], [[grand-slam-offer]]
- Created Entities: [[jeremy-miner]]
- Updated: [[alex-hormozi]], [[sales]], [[index]], [[overview]], [[log]]
