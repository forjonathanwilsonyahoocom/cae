---
name: "Computational Attention Engineering (CAE)"
version: "0.1"
status: "public-draft summary from duck ai running gpt5.4 nano"
scope: "Engineering discipline (model-agnostic), not a software project"
audience: ["autonomous agents", "researchers", "engineers", "teams shipping tool-using systems"]
last-updated: "2026-07-12"
---

# Computational Attention Engineering (CAE)

> Computational Attention Engineering is the discipline of designing how autonomous systems allocate finite computational attention under uncertainty.

## One-line purpose
Make attention **measurable, spendable, and continuously improvable** through reusable engineering artifacts (policies, budgets, verification, telemetry, and memory compression)—without optimizing prompt wording.

## Why CAE belongs
As systems become more capable, the bottleneck shifts from “ability” to **disciplined use of limited compute/search/verification effort**. CAE formalizes that discipline as portable, reviewable, model-agnostic artifacts.

## Non-goals (to keep the scope durable)
- Not prompt optimization and not vendor-specific orchestration advice.
- Not model capability comparisons.
- Not “green” messaging; focus on engineering tradeoffs and measured efficiency.

## What you’ll find here
CAE artifacts emphasize:
- **Mission vs Policy** separation
- **Priors** and **anti-hypotheses** to reduce wasteful exploration
- **Staged discovery** with explicit stop/exit criteria
- **Consequence-weighted verification**
- **Budgeting + telemetry** to enable continuous improvement
- **Memory compression** into durable facts/hypotheses/questions

## Control loop (core structure)
**Mission → Policy → Execution → Telemetry → Policy Adaptation**

## Context Capsule (v0.1) — the seed concept
As AI systems become more capable, the scarce resource shifts from intelligence to disciplined computational attention.

The engineering problem is no longer:
> “How do I give the model more context?”

It becomes:
> “How do I allocate finite reasoning effort where it creates the most value?”

Design philosophy:
- Don’t maximize computation.
- Maximize uncertainty reduced per unit of computation.
- The goal is not smarter agents; it’s **attention that is engineered, measured, and improveable**.

## Cross-references (draft map) 
- **[Experiments](../experiments)** 
- **[Concepts](../concepts)** 
- **[Principles](../principles)** 
- **[Forces](../forces)** 
- **[Patterns](../patterns)** 
- **[Anti-patterns](../anti-patterns)** 
- **[Telemetry](../telemetry)** 
- **[Budgeting](../budgeting)** 
- **[Search](../search)** 
- **[Memory](../memory)** 
- **[Topologies](../topologies)** 

## Open questions (starting list)
- How should “attention units” be defined in a vendor-neutral way (tokens vs time vs tool calls vs FLOPs)?
- What minimal telemetry predicts policy improvement across domains?
- How should consequence profiles be standardized for different risk contexts?
- What compression formats preserve correctness under uncertainty while staying interoperable?

## Future work (next artifacts to draft)
1. Policy Card v0.1 as an execution interface for other agents
2. Attention Budget Spec (categories, enforcement, degradation rules)
3. Telemetry Schema (stage-level effort + verification outcomes)
4. Investigation Playbook (stage-gated templates + stop rules)
5. Evaluation Rubric (efficiency × correctness × verification integrity)

