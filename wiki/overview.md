---
title: "Overview"
type: overview
created: 2026-04-07
updated: 2026-04-07
sources:
  - "[[llm-wiki-karpathy]]"
tags:
  - overview
  - synthesis
---

# Overview

High-level synthesis of everything in this wiki.

---

## Themes

### Knowledge Management với LLM
Wiki này hiện tập trung vào pattern sử dụng LLM để xây dựng và duy trì knowledge base cá nhân — [[llm-wiki-pattern]] của [[andrej-karpathy]]. Đây là cách tiếp cận khác biệt so với [[rag]] truyền thống: kiến thức được compile và tích lũy, không re-derived mỗi lần hỏi.

## Key Insights

1. **Wiki là persistent, compounding artifact** — giá trị tăng theo thời gian, không phải giảm như knowledge bases truyền thống.
2. **Phân công human/LLM rõ ràng** — human lo curation & strategic thinking, LLM lo bookkeeping & maintenance.
3. **Maintenance cost gần zero** — lý do chính wikis truyền thống thất bại (maintenance burden > value). LLM giải quyết điều này.
4. **Ý tưởng có gốc rễ lịch sử** — [[memex]] của [[vannevar-bush]] (1945) đã hình dung điều này, nhưng thiếu "ai làm maintenance."

## Open Questions

- Pattern này scale đến đâu trước khi cần tooling bổ sung (search engine, embeddings)?
- Chất lượng wiki phụ thuộc vào LLM nào? Có khác biệt lớn giữa các models?
- Làm sao handle contradictions giữa nhiều sources một cách có hệ thống?

## Connections

- [[llm-wiki-pattern]] ← giải pháp cho vấn đề của → [[rag]]
- [[llm-wiki-pattern]] ← hiện thực hóa tầm nhìn → [[memex]] / [[vannevar-bush]]
- [[obsidian]] + [[qmd]] ← tooling cho → [[llm-wiki-pattern]]
