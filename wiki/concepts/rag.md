---
title: "RAG (Retrieval-Augmented Generation)"
type: concept
created: 2026-04-07
updated: 2026-04-07
sources:
  - "[[llm-wiki-karpathy]]"
tags:
  - llm
  - ai
  - architecture
---

# RAG (Retrieval-Augmented Generation)

Pattern phổ biến trong LLM applications: upload documents → retrieve relevant chunks at query time → generate answer.

## Đặc điểm

- **Stateless** — mỗi query, LLM phải tìm và ghép nối kiến thức từ đầu
- Không có tích lũy — synthesis không được lưu lại
- Các hệ thống dùng RAG: NotebookLM, ChatGPT file uploads, hầu hết RAG systems

## Hạn chế (theo Karpathy)

- Câu hỏi phức tạp cần tổng hợp từ nhiều documents → LLM phải piece together mỗi lần
- Không có cross-references sẵn
- Contradictions không được track
- "Nothing is built up"

## So sánh với LLM Wiki

Xem chi tiết tại [[llm-wiki-pattern]] — LLM Wiki là giải pháp thay thế, biến kiến thức từ stateless thành stateful, compounding.

## References

- [[llm-wiki-karpathy]]
- [[llm-wiki-pattern]]
