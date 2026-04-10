---
title: "Trigger.dev"
type: entity
created: 2026-04-09
updated: 2026-04-09
sources:
  - "[[claude-code-build-sell-course]]"
tags:
  - tool
  - deployment
  - automation
---

# Trigger.dev

Event-driven job và workflow platform — một trong các deployment targets chính khi deploy [[wat-framework]] automations lên production.

---

## Role trong Stack

Khi [[claude-code]] đã build và battle-test workflows + tools:
1. Push code lên GitHub.
2. Sync với Trigger.dev (hoặc Modal).
3. Run on schedule hoặc triggered by webhook.

Trigger.dev phù hợp cho: scheduled jobs, webhook-triggered automations, background tasks.

---

## Alternatives

- **Modal**: Serverless Python, heavy compute tasks
- **Vercel**: Web apps và APIs
- **Hostinger VPS**: Always-on, full server control

---

## References

- [[claude-code-build-sell-course]]
- [[wat-framework]]
- [[claude-code]]
