---
id: attention-tracing
title: Attention Tracing
path: telemetry/attention-tracing.md
version: "0.1"
status: draft
artifact_type: telemetry
type: telemetry
stage_tags: [monitoring, verification, debugging, learning]
skill_area_tags: [observability, interpretability, systems-design]
risk_level: medium
links:
  relates_to:
    - telemetry/budget-utilization.md
    - concepts/working-memory.md
    - concepts/attention-budget.md
    - search/search-strategies.md
  causes: []
  prevents:
    - unbounded-computation
    - prompt-roulette
    - verification-starvation
  related:
    - principles/legible-delegation.md
  principles:
    - evidence-over-confidence
  laws:
    - diagnose-before-retry
    - constraints-are-computational-inputs
---

# Attention Tracing

## Rule
Every autonomous system should emit a trace of where attention was allocated, why, and what changed as a result. 
If you can’t replay the decision, you can’t improve it.

## When to apply
- Debugging agent failures
- Measuring attention efficiency
- Training and evaluating policies
- Auditing high-stakes decisions
- Optimizing token/compute cost

## Problem
Current LLM logs: `prompt in, text out`. 
That tells you nothing about:
1.  What was considered and rejected
2.  Why this search shape was chosen
3.  What evidence changed confidence
4.  Where the budget went

Result: Incomprehensible graphs. No learning.

## Solution: The 5-Field Trace
Log 1 record per "attention allocation cycle". Keep it small.

| Field | Type | Example |
| --- | --- | --- |
| **cycle_id** | int | 7 |
| **strategy** | enum | exploratory, confirmatory, eliminative |
| **working_memory_snapshot** | json | `{hypotheses: [A,B], disproved: [C], confidence: 0.4}` |
| **budget_state** | json | `{tokens_spent: 1200, tokens_budget: 2000, verification_left: 0.3}` |
| **evidence_in** | list | ["search_result_3", "user_answer_Q2"] |
| **decision** | string | "Ask: work or sleep?" |
| **info_gain_estimate** | float | 0.35 |
| **timestamp** | iso | 2026-04-20T02:14:00Z |

That’s it. 8 fields. You can now replay any run.

## What a Trace Tells You

### 1. Strategy Mismatch
Cycle 1-4: strategy=exploratory, info_gain=0.01
Cycle 5: strategy=exploratory, info_gain=0.00
→ Should have switched to eliminative at Cycle 3

### 2. Budget Blowout
Cycle 1: tokens=500
Cycle 10: tokens=18000
→ Unbounded computation. No stopping condition.

### 3. Verification Starvation  
verification_left: 0.2 → 0.2 → 0.2 → 0.0
→ Never spent budget on checking outcomes

### 4. Working Memory Drift
confidence: 0.8 → 0.8 → 0.8
disproved: []
→ Confidence increasing without evidence. Overconfidence.

## Cross-Sector Examples

### 1.  AdTech
**Trace**: `strategy=eliminative, evidence_in=[device=android], decision="skip leaf_892"`
**Use**: Count how many times eliminative saved a scoring pass. × 75M tokens = $ saved.

### 2. Healthcare  
**Trace**: `strategy=confirmatory, working_memory.confidence=0.4, decision="confirm: work or sleep"`
**Use**: Did confirming actually raise confidence? If not, question was bad.

### 3. DevOps / Incident
**Trace**: `strategy=exploratory, evidence_in=[logs], decision="check network"`
**Use**: Replay postmortem. Was network checked before DB? Why?

### 4. Finance / Fraud
**Trace**: `budget_state.verification_left=0.0, decision="auto-decline"`
**Use**: Audit. Did we spend verification budget before declining?

## Implementation
1. **Minimal**: Log to JSONL. 1 line per cycle.
2. **Better**: Attach to Working Memory. Trace IS the delta of WM.
3. **Best**: Visualize as graph. Nodes=WM states. Edges=evidence.

Rule: Trace cost < 5% of total attention budget.

## Verification
- Can you replay a failure and see where strategy should have switched?
- Can you compute `outcome_delta / tokens_spent` per trace?
- Can a new engineer understand why the agent did X in 60s?
- Is trace used to update policy for next run?

## Anti-pattern: "Monologue Logs"
Dumping the entire CoT. 
That’s 10,000 tokens of noise. Attention Tracing is 200 tokens of signal.

## Relationship to CAE
**Working Memory**: Trace is the changelog of WM  
**Attention Budget**: Trace proves where budget went  
**Law 2**: Trace is the evidence used for diagnosis  
**Law 3**: Trace proves constraints were respected

No trace = you are flying blind.

## Open Questions
- What compression of WM is sufficient for useful traces?
- Can traces be used to automatically suggest policy updates?
- What is the minimal trace for regulatory audit?

## Keywords
observability, provenance, decision-log, interpretability, debugging, replay
---

