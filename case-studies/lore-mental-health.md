# Case Study: Lore Health - Computational Attention Engineering for Digital Mental Health

## Purpose
Apply the Computational Attention Engineering discipline to Lore Health’s core problem:
allocating finite AI attention to reduce user anxiety/stress/burnout and prove healthcare savings.

## Position within Computational Attention Engineering
This case study demonstrates CAE primitives in a high-stakes, human domain.
Attention is scarce: user cognitive load, clinician time, token budget, and safety budget.
Poor allocation = harm. Good allocation = measurable outcomes.

## Summary
LoreBot uses reverse-prompting: it asks questions instead of giving advice.
The core engineering problem is not "better LLM". It is:
"Given uncertain user state, what should the system attend to next, for how long, and with what evidence?"

CAE provides the framework: Budget -> Policy -> Trace -> Verify -> Learn.

## Key Concepts Applied

### 1. Attention Budget
**Problem**: Users in crisis have ~5 minutes of cognitive bandwidth. Asking 20 questions causes dropout.
**CAE Solution**: `budgeting/attention-budget.md` + `budgeting/token-budgets.md`
- Per-session budget: 12 question-turns max
- Per-topic budget: 3 probes max before reflecting
- Compute budget: prefer smaller model for triage, reserve GPT-4 for deep probes

### 2. Attention Policy
**Problem**: When to probe vs support vs escalate?
**CAE Solution**: `policies/attention-policy.md`
- Inputs: user state = text sentiment + session history + time-of-day + clinician flags
- Policy: Bandit over clinician-approved question bank. No LLM freestyle in safety zones.
- Hysteresis: Once escalated to human, do not probe again for 24h

### 3. Attention Tracing
**Problem**: "Why did LoreBot ask that?" Needed for clinician audit + model improvement.
**CAE Solution**: `telemetry/attention-tracing.md`
- Trace: [user_state_vector] -> [policy_decision] -> [question_id] -> [user_response]
- Store with error bars. Enables hindsight analysis.

### 4. Verification Loop
**Problem**: Did the question help? Correlation ≠ causation. Healthcare savings is the north star.
**CAE Solution**: `patterns/verification-loop.md` + `experiments/experimental-methodology.md`
- Run RCTs: Question Set A vs Question Set B for same user state
- Metric: 30-day PHQ-9 delta, ER visit reduction, aggregate claims cost
- Feedback: Update policy weights. This is agent hindsight.

### 5. Evidence Over Confidence
**Problem**: LLM hallucinates advice. Dangerous in mental health.
**CAE Solution**: `principles/evidence-over-confidence.md` + `verification/source-verification.md`
- All responses grounded in: clinician question bank + user memory + peer-reviewed protocols
- Confidence score must be < threshold to ask. Otherwise default to "tell me more"

## Engineering Guidance

| Component | CAE Artifact | Lore Implementation |
| --- | --- | --- |
| **State Modeling** | `memory/working-memory.md` + `long-term-memory.md` | User profile: stress triggers, sleep, social patterns. Updated each session. |
| **Question Selection** | `search/search-strategies.md` | Retrieve top-5 questions from bank given state vector. Rerank with policy. |
| **Safety** | `anti-patterns/prompt-roulette.md` | Block unbounded LLM generation. Route to clinician if risk flags. |
| **Evaluation** | `metrics/attention-efficiency.md` | Outcome delta / attention spent. Optimize for max health per token. |
| **B2B Reporting** | `telemetry/token-accounting.md` | Aggregate only. Prove value to employer without PII. |

## Example: User at 2am, "I can't sleep, work is killing me"

1. **Budget Check**: 10/12 turns used. Low budget -> concise.
2. **State**: high arousal, work stress, night. Load from long-term memory.
3. **Policy**: Select "reflective probe" not "advice". From bank: "What part feels heaviest right now?"
4. **Trace**: log decision + rationale
5. **Verify**: 2 weeks later, did sleep scores improve? Update policy weight.

## Related Documents
- `concepts/computational-attention.md`
- `principles/evidence-over-confidence.md`
- `patterns/verification-loop.md`

## Open Questions
1. How to fuse passive biofeedback HRV into attention budget without violating privacy?
2. What is the optimal attention budget for crisis vs maintenance users?
3. How to measure counterfactual: what would have happened without the probe?

## Research Directions
- Causal inference for question -> outcome
- Multi-agent: LoreBot + Clinician + User coordination
- Attention efficiency as a billable unit for value-based care

## Keywords
reverse-prompting, mental-health, value-based-care, safety, policy, verification, state-modeling

## Revision History
v0.1 - Initial mapping to Lore Health
