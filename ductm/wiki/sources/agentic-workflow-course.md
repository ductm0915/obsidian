---
title: "Agentic Workflows for Business — Definitive Guide"
type: source
created: 2026-04-09
updated: 2026-04-09
sources: []
tags:
  - ai
  - agentic-workflow
  - do-framework
  - claude-code
  - mcp
---

# Agentic Workflows for Business — Definitive Guide

**Author:** Unknown instructor (built 2 AI-based service agencies to $160K/month combined revenue; consulted for billion-dollar businesses)  
**Type:** Video course — agentic workflow fundamentals to advanced  
**Focus:** Practical business applications of agentic workflows  

## Overview

Comprehensive course on agentic workflows with a business-first orientation. Core argument: AI is in an "overhang state" — capabilities far exceed what most people know how to use. The arbitrage window is open now but closing.

## Core Thesis

> "Most people are using AI as glorified copy-and-paste tools. They're drinking the Pacific Ocean through a tiny straw."

People who master agentic workflows will experience a **river of value** diversion — they will capture increasingly large shares of economic value as AI-enabled productivity compounds.

## Key Frameworks

### The DO Framework (Directive, Orchestration, Execution)
Core architecture for agentic workflows:
- **Directive** — natural language instructions defining what the agent should do
- **Orchestration** — the coordination layer that breaks objectives into executable steps and manages tool calls
- **Execution** — the actual task execution (running code, calling APIs, writing files)

This maps to Claude Code's architecture: system prompts (directive) + orchestrator layer + execution tools.

### Horizontal Leverage
Unlike *vertical automation* (replacing one role 100%), agentic workflows offer **horizontal leverage**: automating 90% of 10,000 roles simultaneously.

> "Automating 100% of one role = 1 unit of economic value. Automating 90% of 10,000 roles = 9,000 units of economic value."

Industrial revolution analogy: one seamstress → 10 garments/day. One loom → 10,000 garments/day. But now we can rebuild the loom in seconds via natural language.

### Claude Skills
Modular system prompts for specialized tasks, loaded on demand. See [[skills-claude-code]].

### MCP (Model Context Protocol)
External tool/service connectors for agents. Allows agents to interact with Gmail, Slack, databases, web search, etc. Came out recently; Anthropic is building heavily on it.

### Self-Annealing Workflows
Agents designed to detect errors and self-correct without human intervention. Uses reflection loops at the orchestration layer. The goal: *self-healing during build, deterministic when deployed* (consistent with [[agentic-workflow]]).

### Sub-Agents and Parallelization
Multiple agents running simultaneously on different parts of a task. Requires careful orchestration to merge outputs and handle conflicts.

## The AI Overhang
AI capabilities are far beyond public perception and utilization. A "knowledge arbitrage window" exists now — those who learn agentic workflows early will monetize the gap before it closes.

## Demo Case
Instructor asked Claude Opus 4.5 to: find 5 local meal prep companies in Vancouver → find their emails → send custom meal plan inquiry emails → complete autonomously. Took <15 seconds vs 20 minutes manually. No "AI-isms" in output.

## Connection to Existing Wiki

This source is deeply complementary to [[claude-code-build-sell-course]] (Nate Herk's WAT framework). Key differences:
- This course focuses on the **DO framework** (lower-level architecture)
- Herk's course focuses on **WAT framework** (higher-level workflow categorization)
- Both converge on: Claude Skills, MCP, self-healing workflows, Trigger.dev/cloud deployment

## References

- [[claude-code]]
- [[agentic-workflow]]
- [[wat-framework]]
- [[skills-claude-code]]
- [[context-rot]]
- [[ai-development-tools]]
- [[do-framework]]
- [[horizontal-leverage]]
