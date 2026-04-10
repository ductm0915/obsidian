---
title: "WAT Framework"
type: concept
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[claude-code-build-sell-course]]"
tags:
  - claude-code
  - automation
  - architecture
---

# WAT Framework

Framework kiến trúc do [[nate-herk]] phổ biến cho việc build automations với [[claude-code]]. **W**orkflows, **A**gent, **T**ools.

---

## Components

### Workflows (W)
Markdown files viết bằng natural language — tương đương recipes/SOPs.
- Mỗi workflow = hướng dẫn từng bước cho một task cụ thể.
- Ví dụ: `newsletter-workflow.md` mô tả: research → generate HTML → create infographics → send email.
- Dễ đọc, dễ chỉnh sửa — không cần biết code.

### Agent (A)
[[claude-code]] agent đọc workflows, đưa ra quyết định, điều phối tools.
- Khi bạn deploy: bạn deploy W + T, không phải A.
- Agent = phần self-healing, chỉ hoạt động khi interactive.

### Tools (T)
Scripts/functions thực thi các actions cụ thể:
- Ví dụ: `research.py` (call Perplexity), `send_email.py` (Gmail API), `generate_infographic.py`
- Không có tools, workflows vô nghĩa.
- Không có workflows, tools không có thứ tự.

---

## Analogy: Recipe vs Ingredients

> *"The workflow is the recipe. The tools are the ingredients. Without the recipe, the ingredients are useless."*

---

## Key Property: Self-Improvement

Khi agent làm việc, nó có thể:
- Update workflows nếu phát hiện process tốt hơn
- Fix tools khi gặp API errors (update endpoints, etc.)
- Store learnings vào CLAUDE.md

---

## Deployment Flow

1. Build workflows + tools với agent (interactive, self-healing).
2. Battle-test trước khi deploy.
3. Push workflows + tools lên GitHub.
4. Sync với [[trigger-dev]] hoặc Modal.
5. Run on schedule — deterministic, no agent needed.

---

## Phân biệt với Traditional Automation

| | Traditional (Zapier/n8n) | WAT Framework |
|---|---|---|
| Build | Manual, every step | Agent handles edge cases during build |
| Deploy | Deploy logic | Deploy code + tools |
| Self-healing | No | Yes (during build only) |
| Result quality | Limited by builder's foresight | Better — agent caught edge cases |

---

## Connections

- [[operations]] ← WAT là operational system cho AI-assisted work
- [[optimization-framework]] ← delete-first applies to tool design (build minimal tools)
- [[agentic-workflow]] ← the broader pattern WAT implements
- [[skills-claude-code]] ← knowledge layer trên cùng của WAT

## References

- [[claude-code-build-sell-course]]
- [[claude-code]]
- [[agentic-workflow]]
- [[nate-herk]]
