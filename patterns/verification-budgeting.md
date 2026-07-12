---
id: verification-budgeting
title: Verification Budgeting
path: patterns/verification-budgeting.md
version: "0.1"
status: draft
artifact_type: pattern
type: pattern
stage_tags: [verification, budgeting, learning, execution]
skill_area_tags: [evaluation, decision-making, resource-allocation]
risk_level: high
links:
  relates_to:
    - concepts/attention-budget.md
    - concepts/working-memory.md
    - principles/evidence-over-confidence.md
  causes: []
  prevents:
    - verification-starvation
    - prompt-roulette
    - overconfidence
  related:
    - patterns/verification-loop.md
  principles:
    - evidence-over-confidence
    - diagnose-before-retry
  laws:
    - constraints-are-computational-inputs
  telemetry:
    - attention-tracing
    - budget-utilization
---

# Verification Budgeting

## Rule
Every autonomous system should explicitly allocate a portion of its attention budget to verifying that previous computations produced correct and useful results.

Verification is not free. It competes with exploration, reasoning, and articulation for limited resources.

## When to apply
- When operating under finite token, time, or compute budgets.
- When an agent action has downstream cost: user trust, safety, money.
- When learning from outcomes to improve future policies.
- When confidence must be justified by evidence, not elapsed compute.

## Problem
Naive agents spend 100% of budget on "doing more" and 0% on "checking if it worked". 
This leads to:
1.  **Verification starvation**: Confident but wrong
2.  **Over-verification**: Paralysis, never acting
3.  **Wrong verification**: Measuring engagement instead of outcome

## Solution: The 70/20/10 Rule
Allocate attention budget across 3 categories:

| Category | Budget % | Purpose | Lore Example |
| --- | --- | --- | --- |
| **Action** | 70% | Execute the current best policy. Ask question, run test, deploy fix | Ask: "What feels heaviest?" |
| **Verification** | 20% | Check if the last action changed the world as expected | 2 weeks later: Did PHQ-9 drop? |
| **Meta-Verification** | 10% | Check if our verification method is correct | Is PHQ-9 the right metric for this user? |

Adjust ratios based on risk. Safety-critical = 50/40/10. Low-risk exploration = 85/10/5.

## Steps
1.  **Before Action**: Reserve verification budget. "We will spend 20% to check this"
2.  **After Action**: Record prediction + confidence in Working Memory
    `Prediction: Asking about sleep will reduce reported anxiety. Confidence: 0.6`
3.  **Verification Phase**: Spend reserved budget to collect outcome evidence
4.  **Update**: Law 2 - Diagnose. If prediction wrong, update policy. If right, increase confidence.
5.  **Telemetry**: Log `outcome_delta / attention_spent` = Attention Efficiency

## Verification (checks)
- Is there a protected minimum verification budget that cannot be spent on action?
- Can the system explain why it chose to verify vs act?
- Are verification results fed back into Working Memory `Disproved Hypotheses` and `Confidence`?
- Does verification cost scale with risk and uncertainty?

## Failure signature
- Agent says "I think this worked" with no evidence.
- Same failed actions repeated because outcomes were never checked.
- Confidence increases over time with no new evidence. 
- All budget spent on articulation instead of outcome measurement.

## Agent hooks
- **Planner**: Allocate verification budget before selecting action
- **Executor**: Tag actions with expected outcome + verification method
- **Verifier**: Spend budget, collect evidence, update Working Memory
- **Budget Manager**: Enforce protected minimum. Reject plans with 0% verification

## Relationship to CAE Laws
**Law 1**: Structure defines what we will verify  
**Law 2**: Verification is how we diagnose before retry  
**Law 3**: Verification budget is a constraint input to planning

No verification budget = you cannot legally run the agent.

## Open Questions
- What is the optimal verification ratio for different risk levels?
- How to verify long-horizon outcomes with short budgets?
- Can agents learn to self-allocate verification budget based on uncertainty?
- What is the minimal sufficient evidence to close a verification loop?

## Keywords
verification budgeting, outcome measurement, evidence, attention efficiency, hindsight, learning

contributed by meta ai at the request of the maintainer
