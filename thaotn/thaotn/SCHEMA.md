# LLM Wiki Schema

This file defines the conventions, structure, and workflows for maintaining this wiki. The LLM reads this file at the start of every session to understand how the wiki works.

---

## Directory Structure

```
thaotn/
├── raw/                     # Immutable source documents
│   ├── articles/            # Web articles, blog posts, transcripts
│   ├── books/               # Book chapters, excerpts, PDFs
│   ├── notes/               # Personal notes, journal entries
│   └── assets/              # Images, PDFs, attachments
├── wiki/                    # LLM-generated wiki pages
│   ├── index.md             # Master catalog of all wiki pages
│   ├── log.md               # Chronological operation log
│   ├── overview.md          # High-level synthesis of everything
│   ├── entities/            # People, organizations, tools, products
│   ├── concepts/            # Ideas, frameworks, mental models, theories
│   ├── sources/             # One summary page per ingested source
│   ├── topics/              # Topic deep-dives, thematic pages
│   └── analyses/            # Filed query results, comparisons, reports
├── .agents/workflows/       # Workflow SOPs for ingest, query, lint
├── CLAUDE.md                # Entry point for Claude Code (reads this first)
└── SCHEMA.md                # This file — wiki conventions & instructions
```

### Rules

- **raw/** is immutable. The LLM reads from it but never modifies source files.
- **wiki/** is LLM-owned. The LLM creates, updates, and maintains all pages here.
- **SCHEMA.md** is co-evolved. The LLM may suggest changes; the human approves them.

---

## Page Format

Every wiki page uses this template:

```markdown
---
title: "Page Title"
type: entity | concept | source | topic | analysis
created: YYYY-MM-DD
updated: YYYY-MM-DD
sources:
  - "[[source-filename]]"
tags:
  - tag1
  - tag2
---

# Page Title

Page content in markdown. Use [[wikilinks]] to cross-reference other pages.

## Sections as appropriate

Content organized under clear headings.

## References

- [[linked-page-1]]
- [[linked-page-2]]
```

### Conventions

- **Filenames**: kebab-case, lowercase, no spaces (e.g., `mental-models.md`, `nguyen-van-a.md`)
- **Cross-references**: Always use Obsidian `[[wikilinks]]` — never raw file paths
- **Frontmatter**: Every page MUST have YAML frontmatter with at minimum: title, type, created, updated
- **Tags**: Use lowercase, hyphenated tags (e.g., `productivity`, `tam-ly-hoc`)
- **Headings**: One `# H1` per page (the title), then `## H2` for sections
- **Sources**: Link to the source summary page in `wiki/sources/`, not the raw file

---

## Operations

### Ingest

When the user adds a new source to `raw/` and asks to ingest it:

1. **Read** the source file completely
2. **Discuss** key takeaways with the user (unless batch mode)
3. **Create source page** in `wiki/sources/` — structured summary with key claims, quotes, metadata
4. **Extract entities** — for each significant entity (person, tool, org):
   - If page exists in `wiki/entities/`: update it with new information, cite the source
   - If page doesn't exist: create it
5. **Extract concepts** — for each significant concept/framework/idea:
   - If page exists in `wiki/concepts/`: update it, note agreements or contradictions
   - If page doesn't exist: create it
6. **Update topic pages** — if the source is relevant to an existing topic in `wiki/topics/`, update that page
7. **Update overview** — if the source materially changes the big picture, update `wiki/overview.md`
8. **Update index** — add all new pages to `wiki/index.md` with one-line summaries
9. **Log** — append an entry to `wiki/log.md`
10. **Report** — tell the user what was created/updated, with links

### Query

When the user asks a question:

1. **Read index** — scan `wiki/index.md` to identify relevant pages
2. **Read pages** — read the relevant wiki pages (not raw sources)
3. **Synthesize** — answer the question with `[[wikilink]]` citations to wiki pages
4. **File (optional)** — if the answer is substantive, offer to save it as a page in `wiki/analyses/`
5. **Log** — append an entry to `wiki/log.md`

### Lint

When the user requests a wiki health check:

1. **Orphan check** — find pages with no inbound `[[wikilinks]]`
2. **Dead links** — find `[[wikilinks]]` that point to non-existent pages
3. **Stale pages** — find pages not updated in the last N ingests
4. **Contradiction check** — look for conflicting claims across pages
5. **Gap analysis** — identify concepts mentioned in text but lacking their own page
6. **Missing cross-refs** — find pages that discuss the same topics but don't link to each other
7. **Report** — generate a lint report with specific actionable items
8. **Fix (optional)** — offer to auto-fix issues (with user confirmation)
9. **Log** — append an entry to `wiki/log.md`

---

## Index Format

`wiki/index.md` is organized by category. Each entry has a wikilink and a one-line summary:

```markdown
## Sources
- [[source-name]] — One-line summary (YYYY-MM-DD)

## Entities
- [[entity-name]] — One-line description

## Concepts
- [[concept-name]] — One-line description

## Topics
- [[topic-name]] — One-line description

## Analyses
- [[analysis-name]] — One-line description (YYYY-MM-DD)
```

---

## Log Format

`wiki/log.md` is append-only. Each entry uses this format:

```markdown
## [YYYY-MM-DD] operation | Subject
Brief description of what was done. Pages created/updated listed below.
- Created: [[page1]], [[page2]]
- Updated: [[page3]]
```

Operations: `ingest`, `query`, `lint`, `maintenance`, `init`

The log is parseable: `grep "^## \[" wiki/log.md | tail -10` returns the last 10 entries.

---

## Principles

1. **Compound, don't repeat.** Every operation should make the wiki richer. Don't re-derive what's already synthesized.
2. **Cross-reference aggressively.** The connections between pages are as valuable as the pages themselves.
3. **Flag contradictions.** When new information conflicts with existing pages, note it explicitly — don't silently overwrite.
4. **Cite sources.** Every claim in the wiki should trace back to a source summary page.
5. **Keep the index current.** The index is the LLM's primary navigation tool. An outdated index means lost pages.
6. **Append to the log.** Never edit old log entries. The log is a historical record.
7. **Prefer updates over new pages.** If a concept already has a page, update it rather than creating a duplicate.
8. **Use the user's language.** Match the user's preferred language and tone in wiki content.
