---
description: Run a health check on the LLM Wiki and fix issues
---

# /lint — Wiki Health Check

Scan the wiki for structural issues, stale content, and opportunities for improvement.

## Usage

```
/lint
/lint --fix    (auto-fix simple issues with confirmation)
```

## Steps

1. **Read the schema.** Open and read `SCHEMA.md` to load wiki conventions.

2. **Read the index.** Open `wiki/index.md` to get the full page catalog.

3. **Read all wiki pages.** Scan every page in `wiki/` (sources, entities, concepts, topics, analyses).

4. **Check for issues.** Evaluate each of the following:

   ### Structural Issues
   - **Orphan pages** — pages with no inbound `[[wikilinks]]` from other pages
   - **Dead links** — `[[wikilinks]]` pointing to pages that don't exist
   - **Missing frontmatter** — pages lacking required YAML fields (title, type, created, updated)
   - **Index gaps** — pages that exist on disk but aren't listed in `wiki/index.md`
   - **Stale index entries** — entries in the index for pages that no longer exist

   ### Content Issues
   - **Contradictions** — conflicting claims across different pages
   - **Stale claims** — assertions that newer sources may have superseded
   - **Thin pages** — pages with very little content that could be expanded
   - **Duplicate coverage** — multiple pages covering the same topic

   ### Opportunity Analysis
   - **Missing pages** — concepts or entities frequently mentioned but lacking their own page
   - **Missing cross-references** — pages discussing the same topics but not linking to each other
   - **Suggested questions** — interesting questions the wiki could answer but hasn't explored
   - **Source gaps** — topics where more sources would strengthen the wiki

5. **Generate lint report.** Present findings organized by severity:
   - 🔴 **Errors** — broken links, missing frontmatter, index inconsistencies
   - 🟡 **Warnings** — orphan pages, thin pages, stale content
   - 🔵 **Suggestions** — missing pages, cross-references, questions to explore

6. **Fix (if --fix).** If the user requested auto-fix:
   - Fix dead links (create stub pages or remove links)
   - Add missing frontmatter
   - Sync the index with actual pages
   - Add missing cross-references
   - Confirm each batch of fixes with the user before applying

7. **Log the operation.** Append an entry to `wiki/log.md`:
    ```
    ## [YYYY-MM-DD] lint | Wiki Health Check
    Results: X errors, Y warnings, Z suggestions
    Fixed: [list of auto-fixed issues, if any]
    ```

## Notes

- Run this periodically, especially after ingesting several sources in a row.
- The lint report itself is not saved as a wiki page — it's ephemeral.
- Contradictions should be flagged, not silently resolved. The user decides which claim is correct.
