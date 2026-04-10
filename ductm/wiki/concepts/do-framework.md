---
title: "DO Framework (Directive, Orchestration, Execution)"
type: concept
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[agentic-workflow-course]]"
tags:
  - ai
  - agentic-workflow
  - architecture
  - claude-code
---

# DO Framework (Directive, Orchestration, Execution)

## Definition

The **Directive-Orchestration-Execution (DO)** framework is a 3-layer architecture for designing agentic workflows. It maps the three distinct functional layers in any agent system.

## Three Layers

### Directive
Natural language instructions defining *what* the agent should accomplish. Written in bullet points or structured markdown. Functions like an SOP (Standard Operating Procedure) that the agent reads before acting.

Corresponds to: system prompts, Claude skills, CLAUDE.md files, workflow SOPs.

### Orchestration
The coordination layer that:
- Breaks high-level objectives into executable steps
- Manages tool call sequences
- Handles reflection loops (self-annealing)
- Coordinates sub-agents in parallel workflows

Corresponds to: the orchestrator in a multi-agent system, Claude's internal planning before tool use.

### Execution
The actual task execution:
- Running code / shell commands
- Calling APIs (via MCP)
- Writing/reading files
- Sending emails, posting content

Corresponds to: Claude Code's tool use layer (Bash, Write, Read, WebFetch, etc.)

## Relation to Other Frameworks

| DO Framework | WAT Framework ([[wat-framework]]) |
|---|---|
| Directive | Workflows |
| Orchestration | Agent |
| Execution | Tools |

Both frameworks describe the same architecture at different levels of abstraction. WAT is higher-level (business-oriented); DO is lower-level (technical implementation).

## Self-Annealing
A well-designed orchestration layer includes *reflection* — the agent detects when execution fails and re-tries or re-routes without human intervention. Goal: *self-healing during build, deterministic when deployed.*

## References

- [[agentic-workflow-course]]
- [[agentic-workflow]]
- [[wat-framework]]
- [[skills-claude-code]]
- [[claude-code]]
- [[ai-development-tools]]
