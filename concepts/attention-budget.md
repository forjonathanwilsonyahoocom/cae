id: attention-budget
title: Attention Budget
path: concepts/attention-budget.md
version: "0.2"
status: draft — active
artifact_type: concept
type: concept

stage_tags: [planning, budgeting, execution, verification, stopping, memory]
skill_area_tags: [reasoning, resource-allocation, evaluation, systems-design]
risk_level: medium

links:
  relates_to:
    - concepts/computational-attention.md
    - budgeting/token-budgets.md
    - concepts/working-memory.md
  causes: []
  prevents:
    - unbounded-search
    - verification-starvation
    - context-loss
  related:
    principles:
      - evidence-over-confidence
      - legible-delegation
    laws:
      - structure-precedes-computation
      - diagnose-before-retry
    patterns:
      - search-shaping
      - verification-budgeting
    anti-patterns:
      - prompt-roulette
    telemetry:
      - attention-tracing
      - budget-utilization


# Attention Budget

## Rule

Every autonomous system should treat available computational resources and environmental constraints as part of the problem state.

Attention is not an unlimited capability. It is a budget that must be allocated across search, reasoning, memory, verification, articulation, and recovery.

## When to apply

- When designing autonomous agent workflows.
- When deciding how much computation to spend on exploration versus verification.
- When operating under context, token, latency, or availability constraints.
- When failures occur due to resource exhaustion rather than incorrect reasoning.

## Failure signature

- The system behaves as if compute, context, or verification are unlimited.
- Important reasoning is sacrificed while low-value articulation is preserved.
- Agents restart after interruption because state was not preserved.
- Retry strategies ignore current resource availability.
- Planning assumes resources that do not exist.

## Corrective action (steps)

1. Identify available computational resources:
   - token budget
   - time budget
   - memory/context budget
   - verification budget
   - external dependency availability

2. Classify which resources are constrained.

3. Allocate attention explicitly:
   - exploration
   - reasoning
   - verification
   - articulation
   - recovery/state preservation

4. Adapt policy based on current constraints.

5. Record constraint state as telemetry for future decisions.

## Verification (checks)

- Does the workflow explicitly model resource constraints?
- Are budget tradeoffs visible?
- Are protected minimums defined for reasoning and verification?
- Can the system explain why computation was allocated in a particular way?
- Does the agent preserve useful state across interruptions?

## Agent hooks

- Planner:
  - estimate available resources before selecting strategy.
  - include budget assumptions in mission/policy.

- Executor:
  - track consumption and remaining capacity.

- Verifier:
  - distinguish insufficient resources from incorrect reasoning.

- Memory manager:
  - preserve high-value state when context boundaries approach.

## Definitions (condensed)

- Attention Budget: The finite allocation of computational resources toward achieving understanding and validated outcomes.
- Computational Context: The environmental constraints in which reasoning occurs.
- Resource State: Current availability of compute, memory, time, verification, and external dependencies.

## Position within Computational Attention Engineering

Attention Budget defines the resource model of CAE.

Computational Attention Engineering treats reasoning as a constrained allocation problem. The quality of an autonomous system depends not only on its ability to compute, but on its ability to decide where computation is valuable given current constraints.

A system that ignores its computational context may produce locally reasonable actions while pursuing globally impossible strategies.

## Summary

Constraints are not external obstacles to computation. They are inputs to computation.

An autonomous system must reason about both the problem it is solving and the resources available to solve it.

## Examples

### Example 1 — Rate limiting

An agent reaches an API rate limit. A naive system treats this as failure and retries.

A CAE system incorporates availability into its state, preserves working memory, and chooses whether to wait, switch strategy, or continue locally.

### Example 2 — Token pressure

A system approaches context limits.

A naive system compresses everything equally.

A CAE system protects reasoning artifacts and verification evidence while reducing articulation.

## Open Questions

- Which constraints should always be modeled explicitly?
- Can agents learn optimal budget allocation policies?
- How should budget telemetry influence future planning?
- Is computational context itself a form of working memory?

## Research Directions

- Adaptive attention budgeting.
- Resource-aware agent planning.
- Constraint-aware policy selection.
- Learned recovery strategies.
