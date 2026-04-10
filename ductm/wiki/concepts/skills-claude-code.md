---
title: "Skills (Claude Code)"
type: concept
created: 2026-04-09
updated: 2026-04-10
sources:
  - "[[claude-code-build-sell-course]]"
  - "[[ship30-cowork-bootcamp-s1]]"
tags:
  - claude-code
  - claude-cowork
  - automation
---

# Skills (Claude Code)

Modular system prompts trong [[claude-code]] có thể được load on demand khi cần — giúp agent specialized hơn cho một domain cụ thể.

---

## Cơ Chế

- Skills = system prompts được activate khi relevant.
- Agent tự check: "Request này có require skill nào không?" — tương tự cách nó quyết định dùng tool.
- Ví dụ: "front-end design skill" → Claude Code trở nên tốt hơn đáng kể khi build websites.

---

## Create Your Own Skills

Khi bạn nhận ra một pattern nhất quán trong output, bạn có thể:
1. Instruct agent: "Turn this into a skill."
2. Skill được save, có thể reuse across projects.

Ví dụ từ course:
- Sau khi build newsletter infographics, tạo "infographic skill" với rules: logo top-left, brand colors, specific font.
- Mỗi lần tạo infographic mới, skill được load → output consistent hơn.

---

## Trong [[wat-framework]]

Skills là layer trên cùng của WAT:
- Tools = executable scripts.
- Workflows = orchestration SOPs.
- **Skills = specialized knowledge** agent load để làm tốt hơn.

---

## In [[claude-cowork]]

In the Co-work harness (Ship 30 / [[mitch-harris]] framework), skills work similarly but with a **plugin architecture**:
- Skills are bundled into **plugins** (zip files or marketplace links)
- Triggered by `/skill-name` or automatically by context
- Chain together: "flick a domino" — one triggers the next
- Marketplace hosted on GitHub; auto-updates when skills improve
- [[filemaster]] is the flagship plugin: organize, ingest, search, status

> *"Installing skills are kind of like downloading Kung Fu in the Matrix."* — [[mitch-harris]]

---

## References

- [[claude-code-build-sell-course]]
- [[ship30-cowork-bootcamp-s1]]
- [[claude-code]]
- [[claude-cowork]]
- [[filemaster]]
- [[wat-framework]]
