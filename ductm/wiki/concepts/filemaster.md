---
title: "FileMaster"
type: concept
created: 2026-04-10
updated: 2026-04-10
sources:
  - "[[ship30-cowork-bootcamp-s1]]"
tags:
  - ai
  - claude-cowork
  - tools
  - productivity
  - plugin
---

# FileMaster

Flagship plugin for the [[claude-cowork]] bootcamp. A bundle of 4 skills for building and maintaining the agent's workspace and persistent memory. Developed by [[mitch-harris]] / [[ship-30-for-30]].

---

## The 4 Skills

| Skill | Command | What It Does |
|---|---|---|
| **Organize** | `/organize` | Project-based file organization of mounted local folders |
| **Ingest** | `/ingest` | Feeds files/context into the agent's config, index, and activity log |
| **Search** | `/search` | Find any file or content within the co-worker workspace or mounted folders |
| **Status** | `/status` | Check the agent's self-understanding of the job; validate and update context |

---

## Organize

Scans a mounted folder and proposes a project-based structure. Presents a checklist of moves before executing. Can clear gigabytes of clutter from downloads folders.

> *"A lot of people declaring organizational bankruptcy on their documents folder."* — [[mitch-harris]]

---

## Ingest

The most important skill for building persistent memory. Drag a file into the co-work window and run `/ingest`:
1. Agent reads the file
2. Classifies it (instructional, voice sample, reference, etc.)
3. Asks where to file it in the co-worker folder
4. Updates the config index + activity log

This is how you "train" the agent on your voice, your business context, your preferences — without touching model weights.

> *"Ingest is the command because I want them to eat the context."* — [[mitch-harris]]

---

## Search

Semantic or keyword search across all mounted folders and the co-worker workspace. More capable than OS file search because the agent understands context.

---

## Status

Ask the agent what it understands about your job. Returns a summary of its current configuration. Useful for:
- Validating that training actually landed
- Spotting mismatches between what you intended and what it learned
- In-conversation correction of its understanding

---

## Installation

Two methods:
1. **Zip upload** — Download `filemaster.zip`, drag into Claude Co-work's plugin upload dialog. Do not unzip.
2. **Marketplace** — Paste a GitHub-hosted marketplace URL → sync → install with one click. Auto-updates when the skill improves.

---

## Why Start Here

FileMaster solves the "temp employee" problem: every new Claude session starts fresh. By building an indexed, logged, organized co-worker folder, the agent knows who you are across sessions.

> *"As you grow with your agent, as the agent's knowledge grows... it will keep things organized and efficient. You'll get more from using your Claude than other people who are just vibing."* — [[mitch-harris]]

---

## References

- [[ship30-cowork-bootcamp-s1]]
- [[claude-cowork]]
- [[skills-claude-code]]
- [[mitch-harris]]
- [[ship-30-for-30]]
