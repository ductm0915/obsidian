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

## [2026-04-08] ingest | Your Personal Brand Changes Once You Know How to Stand Out
Ingested Caleb Ralston's article on "Trust-based" personal branding. Core shift: optimizing for deep trust with customers over high reach with followers. Leverage points: Contrarian Belief (the 80% lever) and the Credibility Bank (track record).
- Created: [[ralston-stand-out-brand]], [[caleb-ralston]], [[jony-ive]], [[credibility-bank]], [[contrarian-belief]], [[brand-pairing-formula]], [[optimize-for-trust]]
- Updated: [[brand-building]], [[index]], [[overview]], [[log]]

## [2026-04-08] ingest | Batch ingest: Caleb Ralston articles (7 sources)
Batch ingested 7 additional Caleb Ralston sources covering personal branding courses, content strategy, and creative team leadership.
- Created: [[ralston-265k-followers]], [[ralston-3-stages-brand]], [[ralston-build-brand-course]], [[ralston-content-strategy-2026]], [[ralston-lead-creative-team]], [[ralston-rewire-content]], [[ralston-start-brand-course]]
- Updated: [[caleb-ralston]], [[index]]

## [2026-04-08] lint | Wiki Health Check #2
Comprehensive lint across all pages. Total pages after fixes: 69.
- **Dead links resolved (14):** `[[authority-building]]`, `[[content-strategy]]` (x4), `[[differentiation]]` (x2), `[[focus-as-strategy]]`, `[[jony-ive]]`, `[[leverage]]`, `[[personal-branding]]`, `[[two-column-approach]]` (x2), `[[accordion-method]]`, `[[eye-of-sauron-method]]`, `[[brand-journey-framework]]`, `[[creative-leadership]]`, `[[we-love-a-good-flop]]` — resolved by creating missing pages, replacing with valid links, or inlining text.
- **Pages created (8):** [[jony-ive]], [[accordion-method]], [[eye-of-sauron-method]], [[brand-journey-framework]], [[two-column-approach]], [[creative-leadership]], [[we-love-a-good-flop]] (concepts), [[jony-ive]] (entity)
- **Index gaps fixed:** 7 Ralston source pages + 6 concept pages + 2 entity pages were missing from index. Total count corrected from 58 → 69.
- **Missing cross-refs added:** ~15 new wikilinks across [[credibility-bank]], [[optimize-for-trust]], [[contrarian-belief]], [[brand-pairing-formula]], [[overview]], [[caleb-ralston]].
- **Orphans:** 0
- **Contradictions:** None found
- Updated: [[credibility-bank]], [[contrarian-belief]], [[optimize-for-trust]], [[ralston-stand-out-brand]], [[ralston-content-strategy-2026]], [[ralston-rewire-content]], [[hormozi-no-bs-business-2026]], [[problems-vs-missed-opportunities]], [[brand-building]], [[overview]], [[index]], [[caleb-ralston]], [[log]]

## [2026-04-08] lint | Wiki Health Check #3
Full lint across all 72 pages. Results:
- **Dead links in log.md (6):** `authority-building`, `content-strategy` (x4), `differentiation`, `focus-as-strategy`, `leverage`, `personal-branding` — historical references from lint #2, log is append-only so not fixed.
- **Missing frontmatter fixed (11):** Added `created: 2026-04-08` to [[grand-slam-offer]], [[value-equation]], [[jeremy-miner]]; added `updated: 2026-04-08` to [[hormozi-100m-offers]], [[hormozi-100m-playbooks]], [[hormozi-100m-lost-chapters]], [[hormozi-100m-branding]], [[hormozi-sales-2025]], [[hormozi-9-sales-concepts]], [[hormozi-sell-better-99]], [[miner-nepq-black-book]].
- **Orphan resolved:** `claude-code-build-sell-course.md` (raw course transcript, no frontmatter, off-topic) moved from `wiki/sources/` → `raw/`.
- **Missing cross-refs added (4):** [[contrarian-belief]] → [[brand-journey-framework]]; [[optimize-for-trust]] → [[accordion-method]]; [[we-love-a-good-flop]] → [[discretionary-effort]]; [[brand-journey-framework]] → [[contrarian-belief]].
- **Thin pages (26):** Noted — mostly Hormozi batch-ingested stubs and older entity pages. No fix applied; enrichment deferred to future ingest passes.
- **Orphans:** 0 (after fix above)
- **Contradictions:** None found
- Updated: [[grand-slam-offer]], [[value-equation]], [[jeremy-miner]], [[hormozi-100m-offers]], [[hormozi-100m-playbooks]], [[hormozi-100m-lost-chapters]], [[hormozi-100m-branding]], [[hormozi-sales-2025]], [[hormozi-9-sales-concepts]], [[hormozi-sell-better-99]], [[miner-nepq-black-book]], [[contrarian-belief]], [[optimize-for-trust]], [[we-love-a-good-flop]], [[brand-journey-framework]], [[log]]

## [2026-04-08] ingest | Batch ingest: Caleb Ralston — Full Enrichment (8 sources, ~330K words)
Deep ingest of all 8 Caleb Ralston sources on personal branding, content strategy, and creative leadership. This is the largest single-author batch ingested. Ralston's system provides the complete operational playbook for brand building, complementing Hormozi's sales/operations frameworks with the "how to actually build and scale a personal brand" implementation layer.
- Created Sources: [[ralston-content-strategy-2026]], [[ralston-265k-followers]], [[ralston-build-brand-course]], [[ralston-lead-creative-team]], [[ralston-start-brand-course]], [[ralston-rewire-content]], [[ralston-3-stages-brand]]
- Created Entities: [[trevor-odum]], [[rson-select]]
- Created Concepts: [[brand-journey-framework]], [[accordion-method]], [[eye-of-sauron-method]], [[creative-leadership]], [[we-love-a-good-flop]]
- Enriched: [[caleb-ralston]] (full bio + all frameworks), [[contrarian-belief]] (test-and-double-down + new examples), [[optimize-for-trust]] (trust definition + 4-step formula + viral trap), [[credibility-bank]] (new sources), [[brand-pairing-formula]] (new sources)
- Updated: [[brand-building]] (content ops, creative team leadership, new sources), [[overview]] (new theme synthesis, 3 new insights, 8 new connections), [[index]] (page count 72, all new pages listed), [[log]]
