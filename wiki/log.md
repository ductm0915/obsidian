---
title: "Wiki Log"
type: log
created: 2026-04-07
updated: 2026-04-08
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

## [2026-04-08] lint | Wiki Health Check
Ran full lint across 24 pages. Results:
- **Orphans:** 0 (all pages reachable)
- **Dead links:** 0 among original pages; forward-reference stubs exist for not-yet-ingested sources
- **Stale metadata:** Fixed `created`/`updated` frontmatter on 16 pages
- **Missing cross-refs:** Added ~20 wikilinks (concept→topic hub, source→topic hub, source↔source, entity→topic)
- **Overview:** Added new sources to frontmatter list, added Key Insight #7 (Offers as Core Leverage), added new Connections
- **Contradictions:** None found (2 tensions noted: RAG characterization, education-vs-reframing spectrum)
- Updated: [[hormozi-ultimate-sales-2026]], [[sales-multipliers]], [[volume-negates-luck]], [[bamfam]], [[sales]], [[branding-vs-advertising]], [[spcl-framework]], [[interest-media]], [[brand-building]], [[alex-hormozi]], [[aaa-method]], [[hormozi-grow-audience-2026]], [[hormozi-3a-reframing]], [[hormozi-best-sales-training]], [[index]], [[overview]], [[log]]

## [2026-04-08] ingest | No BS Business Advice to Get Rich in 2026 — Enrichment
Enriched existing [[hormozi-no-bs-business-2026]] source with new concept pages and cross-references. Created topic hub for Operations. Added three new concept pages for frameworks not yet extracted.
- Created: [[optimization-framework]], [[flywheel-effect]], [[discretionary-effort]], [[operations]]
- Updated: [[hormozi-no-bs-business-2026]], [[alex-hormozi]], [[index]], [[overview]], [[sales]], [[value-equation]], [[brand-building]], [[log]]

## [2026-04-08] ingest | No BS Business Advice to Get Rich in 2026
Ingested Alex Hormozi's comprehensive year-end business review (~1200 lines transcript). Covers 20+ lessons on strategy, operations, culture, branding, content, talent, and personal optimization. Portfolio went from ~$50M to ~$100M EBITDA. Richest single source ingested — touched every existing topic hub and created 10 new pages.
- Created Sources: [[hormozi-no-bs-business-2026]]
- Created Concepts: [[six-horsemen-stagnation]], [[problems-vs-missed-opportunities]], [[sawdust-business]], [[kind-not-nice]], [[what-who-when]]
- Created Entities: [[leila-hormozi]], [[ben-francis]], [[school-platform]]
- Updated: [[alex-hormozi]], [[brand-building]], [[sales]], [[branding-vs-advertising]], [[operations]], [[scale-framework]], [[index]], [[overview]], [[log]]
