---
title: "Antigravity IDE"
type: entity
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[learn-antigravity-google-vibe-coding]]"
tags:
  - tool
  - ide
  - ai
  - google
  - vibe-coding
---

# Antigravity IDE

## Overview

AI-native integrated development environment backed by Google. Designed for vibe coding — building software through natural language interaction with AI models.

## Key Features

- **Built-in Gemini integration** — Gemini 3.1 Pro (and other variants) available directly in the agent panel
- **Claude Code support** — can run [[claude-code]] alongside Gemini
- **Three-pane layout:** file explorer (left) + code editor (middle) + agent chat (right)
- **Workspace rules** — always-on, manual, or glob-triggered instructions that guide model behavior (similar to CLAUDE.md)
- **Conversation history** — persists all past agent conversations
- **Markdown preview** — renders markdown files properly within editor

## Access

Available at: anti-gravity.google (Google domain). Requires Google account login. Gemini 3.1 Pro High is available to all users (with usage limits on free tier).

## Hotkeys

- `Cmd+B` — toggle agent panel
- `Cmd+Shift+L` — start new conversation

## Role in Stack

Antigravity functions as the primary development environment in the vibe coding stack: Antigravity (IDE) + Gemini (primary model) + Claude Code (specialized tasks). Positioned as a user-friendly alternative to VS Code or Cursor for non-developers.

## References

- [[learn-antigravity-google-vibe-coding]]
- [[claude-code]]
- [[agentic-workflow]]
- [[ai-development-tools]]
