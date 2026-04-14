---
description: Ingest a new source into the LLM Wiki
---

# /ingest — Ingest a Source

Process a new source document and integrate it into the wiki.

## Usage

```
/ingest raw/articles/article-name.md
/ingest raw/books/chapter-1.md
/ingest raw/notes/my-note.md
```

## Steps

1. **Read the schema.** Open and read `SCHEMA.md` to load wiki conventions.

2. **Read the source file.** Read the full contents of the specified file in `raw/`.

3. **Read the current index.** Open `wiki/index.md` to understand what already exists in the wiki.

4. **Discuss key takeaways.** Briefly share the most important points from the source with the user. Ask if there's anything specific to emphasize or de-emphasize.

5. **Create source summary page.** Create a new page in `wiki/sources/` following the page format in SCHEMA.md. Include:
   - Structured summary of the source
   - Key claims and arguments
   - Notable quotes (with context)
   - Relevance to existing wiki content
   - Metadata (author, date, type, URL if applicable)

6. **Extract and file entities.** For each significant person, organization, tool, or product mentioned:
   - Search the index for an existing page
   - If exists: read the page, update it with new information from this source, add the source to its references
   - If new: create a page in `wiki/entities/` with information from this source

7. **Extract and file concepts.** For each significant idea, framework, or mental model mentioned:
   - Search the index for an existing page
   - If exists: read the page, update it — note agreements, contradictions, or new angles
   - If new: create a page in `wiki/concepts/` with a clear explanation

8. **Update topic pages.** If the source is relevant to any existing topic page in `wiki/topics/`, update that page.

9. **Update overview.** Read `wiki/overview.md`. If this source materially changes the big picture — new themes, shifted understanding, important connections — update the overview.

10. **Update index.** Add all newly created pages to `wiki/index.md` with one-line summaries. Update summaries of any pages that were significantly changed.

11. **Log the operation.** Append an entry to `wiki/log.md` in the standard format:
    ```
    ## [YYYY-MM-DD] ingest | Source Title
    Brief description. Pages affected:
    - Created: [[page1]], [[page2]]
    - Updated: [[page3]], [[page4]]
    ```

12. **Report.** Tell the user what was done — pages created, pages updated, key connections found, any contradictions flagged.

## Notes

- If the source contains images, note their locations but don't try to move them.
- If the source contradicts existing wiki content, flag it explicitly — don't silently overwrite.
- Prefer updating existing pages over creating near-duplicate pages.
- Use `[[wikilinks]]` extensively for cross-referencing.
