---
title: "Agentic Workflow"
type: concept
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[claude-code-build-sell-course]]"
tags:
  - ai
  - automation
  - agentic
---

# Agentic Workflow

Automation system trong đó AI agent đưa ra quyết định, điều phối tools, và xử lý edge cases — thay vì người dùng phải map out từng bước thủ công.

---

## Điểm Khác Biệt với Traditional Automation

**Traditional** (Zapier, n8n):
- Bạn map out mọi bước.
- Break khi gặp unexpected input.
- Maintenance = manual debugging.

**Agentic**:
- Agent xây dựng logic, xử lý edge cases *trong quá trình build*.
- Khi deployed: deterministic như traditional — nhưng quality cao hơn vì agent đã battle-test.

---

## Self-Healing: Hiểu Đúng

**Misconception**: Agentic workflows tự sửa lỗi mãi mãi.

**Reality**:
- Self-healing hoạt động khi agent **đang chạy interactive** (bạn ngồi cùng nó).
- Khi deploy lên server/schedule: deploy code + tools, không phải agent.
- Deployed automation = deterministic. Đây là **tốt**: predictability là mục tiêu.

> *"You're not deploying magic. You're deploying well-built code that was built by magic."*

---

## Market Context

- Agentic AI market: ~$8B hiện tại → $40–50B vào 2030.
- 25% enterprises đang deploy Agentic pilots (2026); → 50% vào 2027.
- Traditional automation hitting ceilings → companies shift to agentic build process.

---

## Analogy

> *"Traditional automation = building a train track by hand, rail by rail. Agentic = telling a construction crew 'build from here to there' — they handle problems during construction. You battle-test before opening to trains."*

---

## Với [[wat-framework]]

WAT là một cách triển khai agentic workflow pattern:
- W = SOPs (workflows)
- A = [[claude-code]] agent
- T = executable tools

---

## Connections

- [[wat-framework]] ← concrete implementation
- [[claude-code]] ← primary tool
- [[optimization-framework]] ← delete-first approach applies to tool design

---

## References

- [[claude-code-build-sell-course]]
- [[claude-code]]
- [[wat-framework]]
