---
title: "Communication Overhead"
type: concept
created: 2026-04-11
updated: 2026-04-11
sources:
  - "[[sam-ovens-why-communication-inefficient]]"
  - "[[sam-ovens-scale-mess-debt]]"
tags:
  - operations
  - team-building
  - scaling
  - sam-ovens
---

# Communication Overhead

The exponential growth in communication complexity as team size increases linearly. One of the most underappreciated reasons why growing companies slow down — and why more people can produce less output.

---

## The Formula

**Communication lines = n × (n−1) / 2**

Where n = number of people.

| People | Lines | Approx. Net Efficiency |
|--------|-------|------------------------|
| 1 | 0 | 100% |
| 2 | 1 | ~98% |
| 3 | 3 | ~95% |
| 5 | 10 | ~82% |
| 6 | 15 | ~70% |
| 10 | 45 | ~18% |
| 11 | 55 | ~0% |
| 14 | 91 | negative (overhead > capacity) |

At 11 people, assuming 90% of communication lines result in communication hours, the entire team's working hours are consumed by communication. **Zero net productive hours.**

---

## Why This Happens

People assume adding one person linearly adds capacity. It does not:
- Each new person must communicate with every existing person
- Each of those communication lines takes time for alignment, updates, questions, reviews
- The overhead scales as O(n²), not O(n)

Sam saw this directly: with 40+ employees at Consulting.com, the company moved slower than it did with 10. Not from laziness — from mathematical inevitability.

---

## The Implication

**Don't measure team health by headcount. Measure by communication lines.**

The goal is:
1. Minimize the number of people (hire fewer, higher-quality people)
2. Minimize communication requirements between them (clear ownership, async-first, documented decisions)
3. Structure so people can work independently with minimal cross-dependencies

---

## Sam's Solution

After discovering this, Sam:
- Reduced total headcount
- Moved to smaller, more independent teams
- Focused on finding fewer, higher-quality people
- Built processes that reduced coordination requirements

---

## The Drop-Off Cliff

The 5–6 person threshold is where efficiency drops most rapidly. Below 5: mostly manageable. Above 6: declining exponentially. Most companies don't know this cliff exists and keep hiring past it.

---

## Related Concepts

- [[scale-mess-debt]] — team debt is one of the 8 types of business debt
- [[sam-ovens-chaos-4-laws]] — non-linear dynamics and interdependence
- [[discretionary-effort]] — right people produce more; wrong people add communication overhead with less output
- [[kind-not-nice]] — direct feedback culture reduces communication waste (fewer "misunderstood" decisions)
- [[aed-system]] — Automate, Eliminate, Delegate: applied to communication, eliminate meetings before optimizing them
