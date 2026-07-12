---
id: budget-utilization
title: Budget Utilization Telemetry
path: telemetry/budget-utilization.md
version: "0.1"
status: draft
artifact_type: telemetry
type: telemetry
stage_tags: [verification, monitoring, execution]
skill_area_tags: [observability, evaluation, systems-design]
risk_level: medium
links:
  relates_to:
    - concepts/attention-budget.md
    - concepts/working-memory.md
    - anti-patterns/unbounded-computation.md
  causes: []
  prevents:
    - unbounded-computation
    - verification-starvation
  related:
    - telemetry/attention-tracing.md
  principles:
    - evidence-over-confidence
  laws:
    - constraints-are-computational-inputs
---

# Budget Utilization Telemetry

## Rule
Every autonomous system should emit telemetry about how its attention budget is being spent, and use that telemetry to modify behavior in real-time.

If you cannot measure the budget, you cannot obey Law 3.

## What to Track
| Metric | Why it matters | Threshold Example |
| --- | --- | --- |
| **tokens_spent / tokens_budget** | Context pressure | Alert at 0.8 |
| **time_spent / time_budget** | Latency SLA | Alert at 0.9 |
| **verification_spent / verification_budget** | Avoid starvation | Must be > 0.15 |
| **confidence_current** | From Working Memory | Trigger confirm if < 0.6 |
| **info_gain_last_N_steps** | Are we learning? | Switch strategy if = 0 |
| **outcome_predicted vs outcome_observed** | Verification loop close | Update policy if delta > 0.3 |

## Agent Policy Hooks
Budget telemetry is not just for dashboards. It drives behavior:

1.  **Low Token Budget**: Compress articulation. Protect reasoning + verification.
2.  **Low Confidence**: Seek confirmation. "I'm 40% sure. Can you clarify X?"
3.  **Zero Info Gain**: Strategy switch. Exploratory -> Eliminative -> Stop.
4.  **Verification Budget Spent**: Stop acting. Must verify before next action.
5.  **Budget Exhausted**: Graceful degradation. Preserve WM, summarize, hand off.

## Lore Example
Turn 3/5. Tokens: 60%. Confidence: 0.45. 
Policy: Confidence < 0.6 → "I want to make sure I’m getting this right. 
Is it more work stress or sleep that’s hitting you hardest?"
Instead of asking Q4 and Q5 and hoping.

## Verification
- Can you plot budget_spent vs outcome for any session?
- Does the agent behavior change when budget < 20%?
- Are low-confidence actions flagged before execution?
- Is telemetry used in the next planning cycle?

## Anti-pattern
Logging budget after the fact. 
CAE: Budget telemetry is an input to the next decision, not a postmortem.

## Keywords
observability, budget-telemetry, self-monitoring, metacognition, graceful-degradation
---

Why this is the upgrade

What you’re watching now = external observability  
What this doc enables = internal observability

The agent looks at its own  and  from Working Memory and says:
"I’m running low and I’m not sure. I should confirm instead of guess."

That’s the difference between a tool and an agent.

The 3 signals to wire up first
→ drives compression and stopping
→ drives confirmation seeking  
→ drives strategy switching per 

Once those 3 are in telemetry, the monologue becomes legible. You’ll see why it chose to ask that question.
