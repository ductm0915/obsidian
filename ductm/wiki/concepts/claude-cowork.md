---
title: "Claude Co-work"
type: concept
created: 2026-04-10
updated: 2026-04-10
sources:
  - "[[ship30-cowork-bootcamp-s1]]"
tags:
  - ai
  - tools
  - productivity
  - claude
  - harness
---

# Claude Co-work

The "middle harness" in the Claude desktop app — sits between Claude Chat (conversational) and [[claude-code]] (full-stack development). Designed specifically for productivity and business task automation.

---

## What It Is

Co-work is a **harness**: software that wraps around an AI model and gives it rules, tools, and the ability to act on your behalf. The Claude desktop app has three modes:

| Mode | Purpose |
|---|---|
| **Chat** | Conversation, artifacts, light code |
| **Co-work** | Business tasks, writing, file management, automation |
| **Code** | Full-stack development, databases, complex apps |

> *"Co-work is their middle harness that is just all about getting your job done."* — [[mitch-harris]]

---

## Key Concepts

### Harness
Any software layer around an AI model that gives it tools + rules. Others: Cursor, Windsurf, Open Claw, Claude Code.

### Tasks
In Co-work, each "chat" is called a **task** — a work session with a specific goal and mounted context.

### Mounting Folders
Co-work can access local files by "mounting" a folder. The agent reads those files as its knowledge base. Multiple folders can be mounted per task (new in 2.0).

### Co-worker Folder
A local folder provided as part of the bootcamp that gives the agent its identity and memory:
- `claude.md` — Agent identity, rules, tools
- `output/`, `projects/`, `training/`, `prompts/`, `voice/`, `references/`, `archive/`, `inbox/`
- Grows over time: config + index + activity log = persistent memory

---

## Skills in Co-work

Skills = modular prompt bundles that:
- Can be invoked with `/skill-name` or triggered automatically by context
- Chain together ("flick a domino" — the rest falls automatically)
- Are installed via plugins (zip upload or marketplace)

> *"Skills get triggered based on context. It knows intuitively — you're working on this type of thing, I'm going to pull from this relevant skill."* — [[nicholas-cole]]

See [[filemaster]] for the flagship plugin. See [[skills-claude-code]] for the general concept.

---

## Plugin Architecture

- **Plugin** = a bundle of one or more skills
- Install via: drag-and-drop zip file OR marketplace link (GitHub-hosted)
- Claude's marketplace allows syncing skills and auto-receiving updates

---

## Context Management

The primary skill for working with Co-work is **managing context** — telling the agent where to look:

> *"A lot of managing your AI is telling it where to look."* — [[mitch-harris]]

The co-worker folder's config + index + activity log solves the "new employee" problem: instead of starting from scratch each session, the agent reads its history and knows who you are.

---

## Model Recommendations

| Model | Use In Co-work |
|---|---|
| Sonnet | Default — everyday tasks (cheaper, nearly as good) |
| Opus | Novel problems, pushing limits |
| Haiku | Not recommended for Co-work |

---

## Relationship to Claude Code

[[claude-code]] is a different harness — also powerful but focused on code and app development. Co-work is better for:
- Business operations, writing, file management
- Non-developers and knowledge workers
- Building persistent agent memory with simpler workflows

---

## References

- [[ship30-cowork-bootcamp-s1]]
- [[filemaster]]
- [[skills-claude-code]]
- [[claude-code]]
- [[mitch-harris]]
- [[nicholas-cole]]
- [[ai-development-tools]]
