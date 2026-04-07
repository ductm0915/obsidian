---
title: "LLM Wiki Pattern"
type: concept
created: 2026-04-07
updated: 2026-04-07
sources:
  - "[[llm-wiki-karpathy]]"
tags:
  - pattern
  - llm
  - knowledge-management
  - wiki
---

# LLM Wiki Pattern

Pattern xây dựng personal knowledge base bằng LLM, được [[andrej-karpathy]] mô tả.

## Core Idea

Thay vì [[rag]] (retrieve-and-generate mỗi lần hỏi), LLM **xây dựng và duy trì một wiki markdown liên kết** — một persistent, compounding artifact. Kiến thức được compile một lần rồi kept current, không re-derived mỗi query.

## So sánh với RAG

|                  | RAG                  | LLM Wiki              |
| ---------------- | -------------------- | --------------------- |
| Kiến thức        | Re-derived mỗi query | Compiled & maintained |
| Cross-references | Tìm lại mỗi lần      | Đã có sẵn             |
| Contradictions   | Không được track     | Flagged khi ingest    |
| Synthesis        | Mỗi lần từ đầu       | Tích lũy, compounding |
| State            | Stateless            | Stateful              |

## Architecture

3 lớp:
1. **Raw sources** — immutable, human-curated
2. **Wiki** — LLM-generated markdown, interlinked
3. **Schema** — conventions & workflows, co-evolved

## Operations

3 thao tác:
1. **Ingest** — thêm source → LLM update 10-15 wiki pages
2. **Query** — hỏi đáp → kết quả có thể file lại
3. **Lint** — health check → tìm contradictions, orphans, gaps

## Phân công lao động

- **Human:** curation, sourcing, asking right questions, strategic thinking
- **LLM:** summarizing, cross-referencing, filing, bookkeeping, maintenance

## Tại sao hoạt động

Con người bỏ wiki vì maintenance burden tăng nhanh hơn value. LLM không chán, không quên, cost of maintenance gần zero.

## Historical Roots

Liên hệ đến [[memex]] của [[vannevar-bush]] (1945). Bush không giải được vấn đề maintenance — LLM giải quyết điều này.

## References

- [[llm-wiki-karpathy]]
- [[rag]]
- [[memex]]
