---
description: Query the LLM Wiki and synthesize answers from wiki pages
---

# /query — Query the Wiki

Search the wiki for relevant pages and synthesize an answer to the user's question.

## Usage

```
/query What are the main themes across all sources?
/query Compare X and Y based on what we know
/query What do we know about [entity]?
/query What are the open questions in [topic]?
```

## Steps

1. **Read the schema.** Open and read `SCHEMA.md` to load wiki conventions.

2. **Understand the question.** Parse the user's query and identify what kind of answer is needed (factual, comparative, analytical, exploratory).

3. **Read the index.** Open `wiki/index.md` and identify all potentially relevant pages based on the question.

4. **Read relevant pages.** Read the identified wiki pages. If a page references other relevant pages via `[[wikilinks]]`, follow those links and read them too.

5. **Synthesize the answer.** Compose a thorough answer that:
   - Directly addresses the question
   - Cites wiki pages using `[[wikilinks]]`
   - Notes any gaps in the wiki's coverage
   - Flags any contradictions between sources
   - Suggests follow-up questions if relevant

6. **Offer to file.** If the answer is substantive (comparison, analysis, synthesis), offer to save it as a new page in `wiki/analyses/`. If the user agrees:
   - Create the page with proper frontmatter
   - Add it to the index
   - Cross-reference it from relevant existing pages

7. **Log the operation.** Append an entry to `wiki/log.md`:
    ```
    ## [YYYY-MM-DD] query | Brief question summary
    Question: [full question]
    Answer referenced: [[page1]], [[page2]]
    Filed as: [[analysis-page]] (if applicable)
    ```

## Answer Formats

Depending on the question, the answer may take different forms:
- **Prose** — for narrative or explanatory answers
- **Table** — for comparisons or structured data
- **List** — for enumerations or recommendations
- **Page** — for substantive analyses that should be preserved

## Notes

- Always search the wiki first, not raw sources. The wiki is the compiled knowledge.
- If the wiki doesn't have enough information, say so and suggest what sources to ingest.
- Answers should add value beyond what's on individual wiki pages — synthesize, don't just copy.
