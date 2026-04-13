---
title: "LLM Wiki — Andrej Karpathy"
type: source
created: 2026-04-07
updated: 2026-04-07
sources: []
tags:
  - llm
  - knowledge-management
  - wiki
  - pattern
---
# LLM Wiki — Andrej Karpathy

**Author:** Andrej Karpathy
**Type:** Idea file / Pattern description
**URL:** https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
**Raw file:** `raw/articles/llm-wiki.md`

---

## Summary

Tài liệu mô tả một pattern để xây dựng knowledge base cá nhân bằng LLM, khác biệt cơ bản so với RAG truyền thống. Thay vì retrieve-and-generate mỗi lần hỏi, LLM **xây dựng và duy trì một wiki markdown liên kết** — một "persistent, compounding artifact" được cập nhật liên tục khi có source mới.

## Key Claims

1. **RAG là stateless** — mỗi câu hỏi, LLM phải tìm lại và ghép nối kiến thức từ đầu. Không có tích lũy.
2. **LLM Wiki là stateful** — kiến thức được compile một lần rồi kept current, cross-references đã có sẵn, contradictions đã được flag.
3. **Wiki là persistent, compounding artifact** — càng thêm source, càng hỏi, wiki càng giàu.
4. **Phân công lao động rõ ràng:** con người lo curation, sourcing, hỏi đúng câu hỏi; LLM lo summarizing, cross-referencing, filing, bookkeeping.
5. **Maintenance cost gần zero** — LLM không chán, không quên update cross-reference, có thể touch 15 files trong một pass.

## Architecture (3 lớp)

| Layer | Mô tả | Ai sở hữu |
|-------|--------|------------|
| **Raw sources** | Tài liệu gốc, immutable | Human |
| **Wiki** | Markdown pages liên kết, LLM-generated | LLM |
| **Schema** | Config file (CLAUDE.md / AGENTS.md) mô tả conventions & workflows | Co-evolved |

## Operations (3 thao tác)

- **Ingest** — Thêm source mới → LLM đọc, tạo summary, cập nhật 10-15 trang wiki
- **Query** — Hỏi đáp dựa trên wiki → câu trả lời hay có thể file lại thành trang mới
- **Lint** — Health check: tìm contradictions, orphan pages, missing cross-refs, data gaps

## Indexing & Logging

- **index.md** — Content-oriented catalog, LLM đọc đầu tiên khi query
- **log.md** — Chronological, append-only, parseable bằng grep

## Tooling gợi ý

- [[obsidian]] — IDE cho wiki, với Graph View, Web Clipper, Marp, Dataview plugins
- [[qmd]] — Local search engine cho markdown (BM25/vector hybrid, MCP server)
- Wiki là git repo → có version history, branching miễn phí

## Notable Quotes

> "The wiki is a persistent, compounding artifact."

> "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."

> "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."

## Historical Connection

Ý tưởng liên hệ đến [[memex]] của [[vannevar-bush]] (1945) — một personal knowledge store với associative trails giữa documents. Bush không giải quyết được ai sẽ làm maintenance — LLM giải quyết vấn đề đó.

## Use Cases

- **Personal**: goals, health, self-improvement, journal entries
- **Research**: papers, reports → wiki với evolving thesis
- **Reading a book**: characters, themes, plot threads — fan wiki cá nhân
- **Business/team**: internal wiki fed by Slack, meeting transcripts, customer calls
- **Competitive analysis, due diligence, trip planning, course notes**

## References

- [[llm-wiki-pattern]]
- [[rag]]
- [[memex]]
- [[andrej-karpathy]]
- [[vannevar-bush]]
- [[obsidian]]
