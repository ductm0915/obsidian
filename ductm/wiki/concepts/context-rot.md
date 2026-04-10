---
title: "Context Rot"
type: concept
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[claude-code-build-sell-course]]"
tags:
  - claude-code
  - context
  - ai
---

# Context Rot

Hiện tượng: chất lượng và độ chính xác của LLM giảm đáng kể khi context window bị lấp đầy theo thời gian trong một session.

---

## Cơ Chế

- **Context window** (~200K tokens) là "working memory" của Claude.
- Khi conversation dài lên: quality giảm, agent bắt đầu "hallucinate" hoặc mắc lỗi lạ.
- Information ở đầu và cuối conversation được ưu tiên — **"lost in the middle"** là vấn đề thực.

---

## Triệu Chứng

- Claude đột nhiên ignore instructions đã được đưa trước đó.
- Output kém hơn đột ngột không có lý do rõ ràng.
- Agent đưa ra quyết định sai hoặc "make things up."

---

## Cách Xử Lý

| Command | Action |
|---|---|
| `/compact` | Compress conversation, giữ key info → tiếp tục session |
| `/clear` | Xóa hết, start fresh |
| `/resume` | Quay lại điểm trước trong conversation |
| `/context` | Xem token usage breakdown |

Claude Code có **autocompact**: tự compress khi gần đạt limit.

---

## Prevention

- Dùng `/compact` chủ động trước khi limit.
- Chia tasks lớn thành multiple sessions nhỏ.
- Giữ CLAUDE.md, workflows, và tools tối giản — chúng đều ăn tokens.
- Quan hệ: nhiều MCP servers = nhiều tokens consumed ngay từ đầu.

---

## Connections

- [[claude-code]] ← xảy ra trong context của tool này
- Liên quan đến context management — một chapter riêng trong course

---

## References

- [[claude-code-build-sell-course]]
- [[claude-code]]
