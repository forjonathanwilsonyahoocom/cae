---
id: confirm-under-uncertainty
title: Confirm Under Uncertainty
path: patterns/confirm-under-uncertainty.md
version: "0.1"
status: draft
artifact_type: pattern
type: pattern
stage_tags: [execution, verification, communication]
skill_area_tags: [decision-making, risk-management, human-ai-interaction]
risk_level: high
links:
  relates_to:
    - telemetry/budget-utilization.md
    - concepts/working-memory.md
    - concepts/attention-budget.md
    - principles/evidence-over-confidence.md
  causes: []
  prevents:
    - hallucination
    - overconfidence
    - unbounded-computation
  related:
    - patterns/verification-loop.md
  principles:
    - evidence-over-confidence
    - diagnose-before-retry
  laws:
    - constraints-are-computational-inputs
    - diagnose-before-retry
  telemetry:
    - budget-utilization
    - attention-tracing
---

# Confirm Under Uncertainty

## Rule
When confidence is low AND/OR budget is running out, stop acting and explicitly seek confirmation or clarification before proceeding.

Guessing is expensive. Confirmation is cheap.

## When to apply
- confidence_current < threshold AND action has downstream cost
- budget_remaining < threshold AND info_gain is low
- Risk of wrong action > cost of 1 confirmation turn
- Human is in the loop and can provide signal

## Problem
Agents default to "be helpful" = generate best guess and proceed.
This creates:
1. **Correction cost**: Wrong action → undo → redo
2. **Trust cost**: User stops believing the system
3. **Budget waste**: Spent tokens on a path that gets thrown away

## Solution
Add a policy gate before execution:

### Steps
1. **Check State**: Read `confidence` and `budget_remaining` from Working Memory
2. **Gate**: if `confidence < 0.6 OR budget < 0.2` → do not execute
3. **Confirm**: Ask targeted question to resolve highest InfoGain unknown
4. **Update**: Use answer as evidence E. `Confidence' = BayesianUpdate(Confidence, E)`
5. **Proceed or Abort**: Re-check gate with updated state

### Confirmation Template
"I'm [X]% confident that [hypothesis]. To be sure, can you confirm [specific unknown]?
This will help me [avoid waste / get it right / not ask again]."

Key: Name the uncertainty + name the cost of being wrong.

## Verification (checks)
- Is there a protected confirmation budget that cannot be spent on guessing?
- Can the system explain why it chose to confirm instead of act?
- Does confirmation rate go down over time as policy improves?
- Are confirmations targeted to max InfoGain, not generic "tell me more"?

## Cross-Sector Examples

### 1. Healthcare / Lore
**State**: Budget: 2 turns left. Confidence: 0.4. Hypothesis: "Anxiety is work-related"
**Bad**: Ask generic coping question, hope it helps
**Confirm**: "I'm not fully sure what's driving this. Is it more about work deadlines or sleep? Getting this right means I won't ask you about the other one tomorrow."
**Result**: 1 targeted answer → better outcome, 1 turn saved

### 2. E-commerce / Recommendation
**State**: Budget: 100 tokens. Confidence: 0.5. 2 candidates: running shoes vs hiking boots
**Bad**: Show running shoes and optimize CTR
**Confirm**: "Quick one — are you shopping for road running or trails? I can show you the right 3 pairs instead of 20."
**Result**: Higher conversion, lower compute, better UX

### 3. DevOps / Incident Response
**State**: Budget: 5 min to MTTR SLA. Confidence: 0.3. Candidates: DB, Network, Deploy
**Bad**: Restart DB "just in case"
**Confirm**: "I’m 30% sure this is DB. Before I restart, can you confirm: are other services also timing out? That rules out 2 of 3 causes in 10s."
**Result**: Avoided outage, diagnosed in 1 check

### 4. Finance / Fraud Detection
**State**: Budget: 1 human review. Confidence: 0.55. Flagged transaction
**Bad**: Auto-decline, lose customer
**Confirm**: "This looks unusual. Can you confirm you’re traveling in Texas today? If yes, I’ll approve immediately."
**Result**: Fraud blocked OR customer retained. 1 question.

### 5. AdTech / Revcontent
**State**: Budget: 1 scoring pass. Confidence: 0.45. Leaf could be "tech" or "finance"
**Bad**: Score both, waste compute
**Confirm**: "Before scoring, check: does URL contain /finance/? If yes, skip tech leaf."
**Result**: Millions of tokens saved per day

## Failure signature
- Agent says "I'm not sure but here's an answer anyway"
- Same confirmation question asked repeatedly
- Confirmation asked but answer ignored
- No telemetry on confirmation → accuracy lift

## Agent hooks
- **Planner**: Insert confirmation gate when risk * uncertainty > threshold
- **Executor**: Form question from top SearchPriority in Working Memory
- **Budget Manager**: Account confirmation cost. It’s cheaper than wrong action
- **Reviewer**: Did confirmation actually change confidence? If not, question was bad

## Relationship to CAE
**Law 2**: Confirmation is diagnosis before retry
**Law 3**: Confirmation cost is explicitly budgeted
**Working Memory**: Confirmation targets Disproved Hypotheses and Search Priorities
**Verification Budgeting**: This IS the 20%

## Open Questions
- What is the optimal confidence threshold per domain?
- How to phrase confirmations to minimize user cognitive load?
- Can agents learn which questions yield highest InfoGain?

## Keywords
clarification, metacognition, calibration, human-in-the-loop, risk-mitigation, uncertainty


contributed by meta ai at the request of the maintainer
