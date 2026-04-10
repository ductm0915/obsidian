---
title: "Build & Sell with Claude Code (10+ Hour Course)"
type: source
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[claude-code-build-sell-course]]"
tags:
  - claude-code
  - agentic-workflow
  - automation
  - monetization
---

# Build & Sell with Claude Code (10+ Hour Course)

**Author:** [[nate-herk]]  
**Type:** Video course (10+ hours, 24 chapters)  
**Platform:** YouTube / Free School Community  

---

## Summary

Comprehensive course đưa người học từ zero đến thành thạo [[claude-code]], bao gồm setup, workflows, deployment, và monetization. Sử dụng [[wat-framework]] làm nền tảng kiến trúc.

---

## Key Claims

### Agentic Market Shift
- Thị trường Agentic AI tăng từ ~$8B hiện tại lên $40–50B vào 2030.
- 25% enterprises đã deploy Agentic pilots; lên 50% vào 2027.
- [[agentic-workflow]] không phải trend — đây là chuyển dịch thực sự của ngành.

### Self-Healing: Sự Thật Quan Trọng
- Self-healing chỉ hoạt động khi agent đang chạy **interactive** (bạn ngồi cùng nó).
- Khi deploy: bạn deploy **code + tools** — không deploy agent. Tại đó, automation hoạt động **deterministic** như traditional automation.
- Điều này là **tốt**: predictability > magic.

### WAT Framework
- **W**orkflows: markdown files = recipes (natural language instructions)
- **A**gent: Claude Code agent đọc workflows, điều phối tools
- **T**ools: scripts/functions thực thi (Python, API calls, etc.)
- Workflows và Tools cải thiện theo thời gian khi agent học từ errors.

### Build Quality > Speed
- Người thất bại: skip fundamentals, không biết webhook/API/automation logic.
- Hiểu cơ bản → communicate precisely → output tốt hơn.

### Monetization: Doctor, Not Pharmacist
- [[doctor-vs-pharmacist]]: Pharmacist fill prescription người khác viết; Doctor chẩn đoán rồi prescribe.
- Đừng lead với "tôi build agentic workflows" → lead với "tôi tiết kiệm X giờ/tháng cho bạn."
- **Value-based pricing**: build tiết kiệm $10K/tháng → charge $5K = ROI 2 tuần, no-brainer.
- Lộ trình: Freelancer → Consultant → Trusted Partner.
- $3K build → $50K/year relationship nếu track metrics + proactively show value.

---

## Notable Quotes

> *"Traditional automation: building a train track by hand. Agentic workflows: telling a construction crew, 'Build it from here to there.'"*

> *"Claude Code is not a subscription. Think of it as a software engineer on your laptop."*

> *"A vague prompt produces vague results. Garbage in, garbage out."*

> *"Act as the doctor, not the pharmacist."*

> *"Building something in 30 minutes that saves 20 hours/week is not a 30-minute job — it's tens of thousands of dollars in value per year."*

---

## Context Window Concepts

- **[[context-rot]]**: Chất lượng giảm theo token count — reset sessions khi xuất hiện.
- Context window: ~200K tokens (system prompt + tools + CLAUDE.md + MCPs + conversation).
- Best practice: Sonnet cho 80% work, Opus cho complex architecture/bugs.

---

## Claude Code Permission Modes

| Mode | Description |
|---|---|
| Plan Mode | Đọc/search/plan, không build |
| Accept Edits | Read + write files, hỏi trước khi chạy bash |
| Bypass Permissions | Full autonomy |

---

## Claude Code Interfaces (5 Methods)

| Interface | Best For |
|---|---|
| Terminal (CLI) | Power users, features come here first |
| Desktop App | Non-terminal users, scheduled tasks |
| Web (claude.ai/code) | Mobile, runs when laptop off |
| IDE (VS Code, Cursor) | Daily coding, zero context switching |
| VPS (Hostinger) | Always-on AI, next to real infra |

---

## Relevance to Existing Wiki

- **Connects to [[sales]]**: Doctor/pharmacist + value-based pricing reinforces [[value-equation]] từ Hormozi.
- **Connects to [[operations]]**: WAT framework là operational system cho AI-assisted work.
- **New domain**: Source đầu tiên về AI tooling. Mở ra theme mới trong wiki.

---

## References

- [[claude-code]]
- [[wat-framework]]
- [[agentic-workflow]]
- [[context-rot]]
- [[doctor-vs-pharmacist]]
- [[nate-herk]]
- [[anthropic]]
- [[sales]]
- [[operations]]
