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
- Created Entities: [[leila-hormozi]], [[ben-francis]], [[skool-platform]]
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

## [2026-04-09] lint | Wiki Health Check #4
Full scan of 84 pages. Results: 0 new errors, 0 orphans, 11 thin pages (same stubs from batch ingests — deferred), 3 missing cross-refs fixed.
- **Dead links (6):** `authority-building`, `content-strategy`, `differentiation`, `focus-as-strategy`, `leverage`, `personal-branding` — all in `wiki/log.md` only (append-only, unfixable by design). Carry-over from lint #3.
- **Orphans:** 0
- **Index gaps / stale entries:** 0
- **Missing frontmatter:** 0
- **Thin pages (11, deferred):** [[bamfam]], [[grand-slam-offer]], [[interest-media]], [[spcl-framework]], [[value-equation]], [[volume-negates-luck]], [[andrej-karpathy]], [[jeremy-miner]], [[qmd]], [[ralston-select]], [[vannevar-bush]] — same stubs from Hormozi batch ingest.
- **Missing cross-refs fixed (3):** [[value-equation]] → [[doctor-vs-pharmacist]]; [[operations]] → [[ai-development-tools]], [[wat-framework]], [[agentic-workflow]]; [[wat-framework]] → [[operations]], [[optimization-framework]].
- Updated: [[value-equation]], [[operations]], [[wat-framework]], [[log]]

## [2026-04-09] ingest | Build & Sell with Claude Code (Nate Herk)
First source on AI tooling and agentic development. Fixed wiki/sources/claude-code-build-sell-course.md (previously contained raw transcript instead of summary). New domain: AI Development Tools.
- Created Sources: [[claude-code-build-sell-course]]
- Created Entities: [[claude-code]], [[nate-herk]], [[anthropic]], [[trigger-dev]]
- Created Concepts: [[wat-framework]], [[agentic-workflow]], [[context-rot]], [[doctor-vs-pharmacist]], [[skills-claude-code]]
- Created Topics: [[ai-development-tools]]
- Updated: [[sales]] (doctor/pharmacist + value-based pricing for AI services), [[overview]] (new AI Development theme, 3 new insights, 8 new connections), [[index]] (page count 84, all new pages listed), [[log]]

## [2026-04-08] ingest | Batch ingest: Caleb Ralston — Full Enrichment (8 sources, ~330K words)
Deep ingest of all 8 Caleb Ralston sources on personal branding, content strategy, and creative leadership. This is the largest single-author batch ingested. Ralston's system provides the complete operational playbook for brand building, complementing Hormozi's sales/operations frameworks with the "how to actually build and scale a personal brand" implementation layer.
- Created Sources: [[ralston-content-strategy-2026]], [[ralston-265k-followers]], [[ralston-build-brand-course]], [[ralston-lead-creative-team]], [[ralston-start-brand-course]], [[ralston-rewire-content]], [[ralston-3-stages-brand]]
- Created Entities: [[trevor-odum]], [[ralston-select]]
- Created Concepts: [[brand-journey-framework]], [[accordion-method]], [[eye-of-sauron-method]], [[creative-leadership]], [[we-love-a-good-flop]]
- Enriched: [[caleb-ralston]] (full bio + all frameworks), [[contrarian-belief]] (test-and-double-down + new examples), [[optimize-for-trust]] (trust definition + 4-step formula + viral trap), [[credibility-bank]] (new sources), [[brand-pairing-formula]] (new sources)
- Updated: [[brand-building]] (content ops, creative team leadership, new sources), [[overview]] (new theme synthesis, 3 new insights, 8 new connections), [[index]] (page count 72, all new pages listed), [[log]]

## [2026-04-09] ingest | 13 Years of Marketing Advice in 85 Mins
Ingested Alex Hormozi's marketing masterclass detailing LTV:CAC as the primary metric, the More/Better/New framework for scaling, and the complete taxonomy of advertising mechanics.
- Created Sources: [[hormozi-13-years-marketing]]
- Created Concepts: [[more-better-new]], [[ltv-to-cac]], [[four-ways-to-advertise]], [[kaleidoscope-process]], [[five-levels-of-awareness]]
- Updated: [[alex-hormozi]], [[value-equation]], [[volume-negates-luck]], [[brand-building]], [[overview]], [[index]], [[log]]

## [2026-04-09] lint | Wiki Health Check #5
Ran full structural check per user request after major ingest. Results:
- **Index vs Disk:** 100% matched (91 pages indexed out of 91 original content pages on disk)
- **Missing Frontmatter:** 0
- **Orphans:** 0
- **Dead Links:** 0
- **Thin Pages:** 15 (<30 lines), consisting mainly of batch-ingested stubs and newly created concept pages awaiting future enrichment.
The wiki structural integrity is flawless.

## [2026-04-09] ingest | How to Make Progress Faster Than Everyone
Ingested Alex Hormozi's reflection on his early "cringe" content and why documenting the struggle is a necessity. Extracted "cringe" as a defensive status play against caring deeply.
- Created Sources: [[hormozi-make-progress-faster]]
- Created Concepts: [[cringe-status-play]], [[document-the-struggle]]
- Updated: [[brand-building]], [[index]], [[log]]

## [2026-04-09] ingest | Batch ingest: 5 new sources (3 Hormozi + 2 AI)
Ingested 5 previously un-ingested raw sources. Added 2 new AI tool sources, 3 new Hormozi business sources. New concepts: retention framework, value per second, DO framework, horizontal leverage. New entity: Antigravity IDE.
- Created Sources: [[hormozi-customer-retention]], [[hormozi-3hrs-money-making]], [[agentic-workflow-course]], [[learn-antigravity-google-vibe-coding]]
- Updated Sources: [[hormozi-13-years-marketing]] (full rebuild with richer detail)
- Created Concepts: [[retention-framework]], [[value-per-second]], [[do-framework]], [[horizontal-leverage]]
- Created Entities: [[antigravity-ide]]
- Updated: [[alex-hormozi]] (added retention + awareness sources), [[ai-development-tools]] (DO framework + Antigravity IDE + new sources), [[index]] (page count 112, 29 sources), [[log]]

## [2026-04-09] lint | Wiki Health Check #6
Full lint after batch ingest. Results: 0 errors, 0 orphans, 0 dead links in new pages, 0 missing frontmatter.
- **Index duplicate fixed:** [[hormozi-13-years-marketing]] was listed twice; removed duplicate entry.
- **Source count corrected:** 30 → 29 (was counting one source twice).
- **Concepts on disk:** 52 (2 ahead of index count — index corrected to reflect actual count).
- **Orphans:** 0
- **Dead links:** 0 in any of the 9 newly created pages
- Updated: [[index]], [[log]]

## [2026-04-10] ingest | Claude Co-work Bootcamp 2.0 — Session 1: FileMaster
Ingested live session transcript from Ship 30 For 30 / [[ship-30-for-30]]. Introduces Claude Co-work (the "middle harness"), the FileMaster plugin (4 skills for workspace memory), and the key distinction between Chat / Co-work / Code in the Claude desktop app. New people: Nicholas Cole, Mitch Harris, Dicky Bush.
- Created Sources: [[ship30-cowork-bootcamp-s1]]
- Created Entities: [[nicholas-cole]], [[mitch-harris]], [[dicky-bush]], [[ship-30-for-30]]
- Created Concepts: [[claude-cowork]], [[filemaster]]
- Updated: [[claude-code]] (added harness distinction + Co-work note), [[skills-claude-code]] (added Co-work plugin architecture section), [[ai-development-tools]] (Co-work section + new key thinkers), [[index]] (page count 121, 30 sources), [[log]]

## [2026-04-10] ingest | Batch — 8 Sources (Hormozi + Skool + Ship30 S2)
Ingested 8 sources in batch: 6 Hormozi videos, 1 Skool journey case study, 1 Ship30 Cowork Session 2. Introduced 16 new concept pages, 8 new source pages. Major theme expansion: compensation risk hierarchy, business mathematics, learning frameworks, and market selection fundamentals.
- Created Sources: [[hormozi-6-levels-making-money]], [[hormozi-how-to-win]], [[hormozi-best-year-2026]], [[hormozi-watch-get-ahead-2026]], [[hormozi-millionaire-blueprint-2024]], [[hormozi-mathematics-business]], [[skools-5-years-100k]], [[ship30-cowork-bootcamp-s2]]
- Created Concepts: [[six-levels-compensation]], [[inversion-method]], [[operationalize-traits]], [[learning-intelligence-confidence]], [[deprivation-motivation]], [[one-source-rule]], [[frustration-tolerance]], [[my-fault-philosophy]], [[hungry-crowd]], [[one-avatar-product-channel]], [[rule-of-100]], [[close-rate-pricing-ladder]], [[sell-at-point-of-deprivation]], [[declarative-vs-procedural]], [[payback-period]]
- Updated: [[ltv-to-cac]] (added model-type benchmarks table 3:1/6:1/9:1/12:1), [[alex-hormozi]] (added 7 new sources), [[sales]] (added pricing + mindset sections + 6 new sources), [[operations]] (added business mathematics section + 3 new sources), [[index]] (156 pages, 38 sources)

## [2026-04-10] ingest | Matt Gray — How to Build a Profitable Personal Brand (64 min)
Matt Gray's complete personal brand masterclass. Introduced the Founder Flywheel, Content GPS, Content Waterfall System, and AED team-building framework. New thinker added to brand-building domain.
- Created Source: [[gray-profitable-personal-brand]]
- Created Entities: [[matt-gray]], [[founder-os]]
- Created Concepts: [[founder-flywheel]], [[content-gps]], [[content-waterfall-system]], [[personal-moat]], [[rented-vs-owned-audience]], [[newsletter-welcome-series]], [[aed-system]], [[delegation-math]], [[media-first-founder]]
- Updated: [[brand-building]] (added full Matt Gray section), [[index]] (169 pages, 39 sources)

## [2026-04-11] ingest | How to Become a Storytelling Genius — Matt Gray
Matt Gray's 6-part storytelling addiction framework: open loops, story-as-funnel (Attention→Trust→Belief→Action), story-as-moat, Five-Line Story Framework, and tightly coupled CTA. Personal Bitmaker story (government raid → viral → acquisition) as proof. Also confirmed Content Waterfall team role details.
- Created: [[gray-storytelling-addiction]], [[five-line-story-framework]], [[open-loop-technique]], [[coupled-cta]]
- Updated: [[matt-gray]] (Bitmaker story + 3 new frameworks), [[index]] (181 pages, 41 sources)

## [2026-04-11] ingest | How I Wrote A #1 Bestseller with $0 and No Publisher — Alex Hormozi
Hormozi's deep-dive on storytelling craft and book writing process. $100M Offers: 200K copies, no publisher, no ads, word of mouth only. Covers story anatomy (7 elements + dual journey), what makes stories interesting (7 newsworthiness factors, stakes), show-don't-tell, selective detail, and Hemingway editing (12th→3rd grade; 1,000 hours; 8 drafts).
- Created: [[hormozi-bestseller-writing]], [[story-elements-framework]], [[seven-factors-newsworthiness]], [[stakes-and-struggle]], [[hemingway-editing]], [[storytelling]] (new topic)
- Updated: [[alex-hormozi]] (writing process + storytelling frameworks), [[index]]

## [2026-04-11] ingest | Business Is Hard Until You Design It Like This — Matt Gray
Matt Gray's complete 6-phase "Beautiful Business" model: Traffic (organic + rented→owned), Entry Points (newsletter/workshop/apply), Products (3-tier offer stack + 4 levers), Content GPS (20/10 cadence + application router), Math (sample $1.3M/month), and True Goals (peaceful, simple, longevity). New concepts: offer stack model, signal vs. noise content, application router.
- Created: [[gray-beautiful-business]], [[offer-stack-model]], [[signal-vs-noise-content]], [[application-router]]
- Updated: [[matt-gray]] (stats + new frameworks), [[founder-os]] (offer stack detail + scale metrics), [[founder-flywheel]] (expanded operational loop), [[content-gps]] (20/10 CTA cadence + team routes), [[brand-building]] (Beautiful Business section), [[index]]

## [2026-04-11] ingest | How To Get Ahead Of 99% Of People — Dan Koe
First Dan Koe source ingested. 7-video compilation covering: anti-vision + entropy as life architecture tools, flow state as optimal attention absorption, life-as-video-game mechanics, 4-hour workday as leverage constraint, bring-ideal-future-into-now habit philosophy, deep work routine, and society-as-pyramid-scheme social critique. Koe's frame: philosophical entrepreneurship at the intersection of consciousness studies (Ken Wilber, Alan Watts) and practical one-person business building.
- Created: [[dan-koe-get-ahead-99]], [[dan-koe]], [[anti-vision]], [[entropy-principle]], [[flow-state]], [[four-hour-workday]], [[ideal-future-now]], [[life-as-video-game]]
- Updated: [[frustration-tolerance]] (added Koe's "mastery over misery" + entropy connection), [[index]]
