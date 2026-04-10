---
title: "Claude Code"
type: entity
created: 2026-04-09
updated: 2026-04-10
sources:
  - "[[claude-code-build-sell-course]]"
  - "[[ship30-cowork-bootcamp-s1]]"
tags:
  - tool
  - ai
  - automation
  - agentic
---

# Claude Code

CLI và IDE extension do [[anthropic]] xây dựng — agent AI có thể đọc/viết files, chạy terminal commands, gọi APIs, và thực thi multi-step tasks trong codebase.

**Note:** Claude Code là một *harness* riêng biệt, khác với [[claude-cowork]]. Claude desktop app có 3 modes: Chat (conversational), Co-work (productivity/business tasks), Code (full-stack dev).

---

## What It Is

Claude Code là **agentic coding tool**: không phải chatbot, mà là agent có tool-use thực sự. Underlying engine giống nhau trên mọi interfaces (terminal, desktop, VS Code, web).

> *"Claude Code is not a subscription. It's a software engineer on your laptop."* — [[nate-herk]]

---

## Interfaces

| Interface | Notes |
|---|---|
| **Terminal (CLI)** | Most powerful, features come here first, any OS |
| **Desktop App** | GUI, scheduled tasks, Mac/Windows only |
| **Web (claude.ai/code)** | Runs on Anthropic cloud, persists when laptop off |
| **IDE Extension** | VS Code, Cursor, Windsurf — zero context switching |
| **VPS** | Always-on, deploy next to real infrastructure |

---

## Core Capabilities

- Read/write/edit files và folders
- Run bash/shell commands
- Call APIs và external services
- Browser automation (screenshot, click, form fill)
- Git workflow management
- Data analysis, content pipelines
- Build apps, websites, automations, games

---

## Architecture Pattern

Claude Code thường được dùng với [[wat-framework]]:
- **Workflows**: markdown files = natural language SOPs
- **Agent**: Claude Code agent đọc workflows, điều phối tools
- **Tools**: scripts/functions thực thi (Python, API calls)

---

## Key Concepts

- **[[context-rot]]**: Chất lượng giảm khi context window đầy — reset session khi cần.
- **Context window**: ~200K tokens (system prompt + CLAUDE.md + MCPs + conversation).
- **Permission modes**: Plan Mode (đọc/plan only) → Accept Edits → Bypass Permissions (full autonomy).
- **CLAUDE.md**: System prompt cho project — instructions, folder structure, frameworks.
- **[[skills-claude-code]]**: Modular system prompts có thể load on demand.
- **Sub-agents**: Claude Code có thể spawn multiple agents cho parallel tasks.

---

## Models

- **Haiku**: fastest, cheapest, lightweight tasks
- **Sonnet**: balanced, daily coding (recommended 80% of work)
- **Opus**: heaviest reasoning, complex architecture/bugs

---

## Useful Commands

| Command | Function |
|---|---|
| `/context` | Show token usage breakdown |
| `/compact` | Compress conversation, keep key info |
| `/clear` | Wipe conversation, start fresh |
| `/resume` | Return to earlier conversation point |
| `/model` | Switch Claude model |

---

## Deployment

Khi workflows + tools đã stable:
1. Push to GitHub repo
2. Sync với [[trigger-dev]] hoặc Modal
3. Run on schedule (e.g. every Monday 6am)

**Lưu ý quan trọng:** Deploy = deploy code + tools, không phải agent. Self-healing chỉ hoạt động khi interactive — deployed automation hoạt động deterministic. Đây là tốt: predictability > magic.

---

## References

- [[claude-code-build-sell-course]]
- [[ship30-cowork-bootcamp-s1]]
- [[claude-cowork]]
- [[wat-framework]]
- [[agentic-workflow]]
- [[anthropic]]
- [[nate-herk]]
- [[trigger-dev]]
