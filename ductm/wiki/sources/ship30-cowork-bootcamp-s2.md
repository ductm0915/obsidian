---
title: "Claude Cowork Bootcamp 2.0 — Session 2: Content Creator"
type: source
created: 2026-04-10
updated: 2026-04-10
sources:
  - "raw/articles/Ship 30 For 30/Claude Cowork Bootcamp 2.0 Live Session 2 Content Creator.md"
tags: ["claude-code", "cowork", "content-creation", "ship30", "ai-tools"]
---

# Claude Cowork Bootcamp 2.0 — Session 2: Content Creator

**Author:** [[mitch-harris]] (instructor), [[ship-30-for-30]]  
**Type:** Live session transcript  
**Date ingested:** 2026-04-10  
**Companion:** [[ship30-cowork-bootcamp-s1]] (Session 1: FileMaster)

## Summary
Session 2 of the Claude Cowork Bootcamp 2.0 focuses on a full content creation pipeline inside Claude desktop's co-work harness. The session builds on Session 1's FileMaster foundation and adds: Notion connector integration, scheduled tasks, and a one-shot prompt that executes the entire writing workflow (idea → publish-ready draft → repurpose → organize → schedule).

## Session Content

### Token Management
- Co-work uses more tokens than chat because it loads all skills/abilities into context.
- Recommendation: use **Sonnet** model in co-work (not Opus) for more tokens per plan.
- "The everyday task razor": use co-work for big, repeatable, chainable tasks. Use chat for quick one-off queries.
- Hard limits on chat (tool use caps, no plugins); co-work has full plugin/skill access.

### Notion Connector Integration
- Load Notion projects as context folders alongside local files.
- Import existing chat Projects into co-work (Projects = cloud context, not just local folders).
- This week's new feature: co-work projects with recurring task support.
- Naming note: "Create new project" button is misleading — it imports/creates a folder, not a new project from scratch.

### The One-Shot Content Workflow
Full pipeline in a single prompt:
1. Search for ideas
2. Build subject lines
3. Generate hooks for long-form
4. Build outline
5. Draft the piece
6. Edit the draft
7. Hunt for AI fingerprints
8. Deliver to Notion
9. Generate social hooks
10. Repurpose for short-form
11. Organize into FileMaster knowledge base
12. Set recurring schedule

Alternative: step-by-step version for more token control.

### Scheduled Tasks
- Co-work supports scheduled recurring tasks — a new feature not available in Session 1's original boot camp.
- Doubles the utility of co-work for content workflows (e.g., daily content creation pipeline).

### Troubleshooting Live
- Skills sometimes fail to load (described as "kernel panic") — workaround: Claude reads the files directly instead of executing skills as functions.
- Notion MCP connector had live errors during the session — handled by troubleshooting live.
- Lesson: troubleshooting IS the skill. Mastering what to do when it breaks is more valuable than watching perfect demos.

## Key Concepts
- [[claude-cowork]] — Updated: co-work now supports projects and scheduled tasks
- [[filemaster]] — FileMaster as the knowledge base that content feeds back into

## Relevant Existing Concepts
- [[agentic-workflow]] — One-shot content prompt is a self-orchestrating agentic workflow
- [[skills-claude-code]] — Skills loaded on-demand in co-work

## References
- [[ship-30-for-30]]
- [[mitch-harris]]
- [[nicholas-cole]]
- [[ai-development-tools]]
- [[ship30-cowork-bootcamp-s1]]
