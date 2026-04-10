---
title: "AI Development Tools"
type: topic
created: 2026-04-09
updated: 2026-04-10
sources:
  - "[[claude-code-build-sell-course]]"
  - "[[ship30-cowork-bootcamp-s1]]"
tags:
  - ai
  - tools
  - automation
  - development
---

# AI Development Tools

Hệ sinh thái tools dùng để build, deploy, và manage agentic AI systems — với [[claude-code]] làm trung tâm.

---

## Overview

Shift từ traditional automation (Zapier, n8n) sang agentic systems đòi hỏi một stack mới:
1. **Build layer**: [[claude-code]] với [[wat-framework]]
2. **Deployment layer**: Trigger.dev, Modal, Vercel
3. **Infrastructure layer**: VPS (Hostinger), GitHub

---

## Core Tool: Claude Code

[[claude-code]] là central tool — agent có thể:
- Build workflows và tools (interactive phase)
- Tự fix errors trong quá trình build
- Deploy code khi đã battle-tested

---

## Architecture Pattern: WAT

[[wat-framework]] (Workflows, Agent, Tools) là cách tổ chức AI projects:
- Workflows: markdown SOPs
- Agent: Claude Code
- Tools: executable scripts

---

## Deployment Infrastructure

| Tool | Role |
|---|---|
| **Trigger.dev** | Event-driven automation, schedule workflows |
| **Modal** | Serverless Python, run heavy compute |
| **Vercel** | Deploy web apps/APIs |
| **Hostinger VPS** | Always-on Claude Code instance |
| **GitHub** | Version control, sync to deployment |

---

## Claude Code Interfaces

| Interface | Use Case |
|---|---|
| Terminal CLI | Power users, most features |
| Desktop App | GUI, scheduled tasks |
| Web (claude.ai/code) | Mobile, persistent sessions |
| IDE Extension | Daily coding |
| VPS | Always-on, production infra |

---

## Claude Models

| Model | Use Case | Cost |
|---|---|---|
| Haiku | Fast tasks, sub-agents | Cheapest |
| Sonnet | 80% of daily work | Mid |
| Opus | Complex architecture, debugging | Most expensive |

---

## Key Concepts

- [[agentic-workflow]] — Build fast with agent, deploy deterministic
- [[context-rot]] — Quality degrades with token buildup; manage actively
- [[skills-claude-code]] — Modular expertise, load on demand
- [[wat-framework]] — Organizing principle for AI projects
- CLAUDE.md — Project system prompt (instructions, structure, frameworks)

---

## Monetization Layer

[[doctor-vs-pharmacist]] — Selling AI services requires diagnosis, not just building.

---

## Claude Co-work (Middle Harness)

[[claude-cowork]] is the productivity-focused harness in the Claude desktop app — between Chat and Code. Key for non-developers and knowledge workers:
- Uses plugins/skills for business task automation
- Supports mounting local folders as the agent's knowledge base
- [[filemaster]] plugin: organize, ingest, search, status — builds persistent memory
- Skills trigger by context; chain automatically ("flick a domino")

> *"All of this but automatically is what co-work does."* — [[mitch-harris]]

---

## Key Thinkers

- [[nate-herk]] — WAT framework, Claude Code courses
- [[anthropic]] — Creator of Claude Code
- [[mitch-harris]] — Claude Co-work expert, [[ship-30-for-30]] AI wizard
- [[nicholas-cole]] — Co-founder Ship 30 For 30, AI Writing School

---

## DO Framework

[[do-framework]] (Directive, Orchestration, Execution) là kiến trúc technical bổ sung cho WAT:
- Directive = natural language SOPs / system prompts
- Orchestration = coordination + self-annealing
- Execution = tool calls, code runs, API calls

## Horizontal Leverage

[[horizontal-leverage]] — automating 90% of 10,000 roles > automating 100% of 1 role. Key economic argument for agentic workflows.

## IDEs for Vibe Coding

| IDE | Primary Model | Use Case |
|---|---|---|
| [[antigravity-ide]] | Gemini 3.1 Pro | Vibe coding, non-developers |
| Cursor | GPT / Claude | Developer-focused |
| Claude Code | Claude | Agentic tasks, automation |

## Ingested Sources

- [[claude-code-build-sell-course]]
- [[agentic-workflow-course]]
- [[learn-antigravity-google-vibe-coding]]
- [[ship30-cowork-bootcamp-s1]]
