---
id: working-memory
title: Working Memory
path: concepts/working-memory.md
version: 0.1
status: draft — proposed
artifact_type: concept
type: concept

stage_tags: ["planning", "execution", "memory", "verification"]
skill_area_tags: ["reasoning", "attention", "state-management"]

risk_level: medium

links:
  relates_to: ["concepts/computational-attention.md"]
  causes: []
  prevents: ["prompt-roulette"]
  related: []

  principles: ["evidence-over-confidence"]
  laws: ["token-budgets"]
  patterns: []
  anti-patterns: []
  telemetry: ["attention-tracing"]

---

# Working Memory

## Rule

Maintain a progressive, lossy summary of the current problem that preserves only the information necessary to guide future attention allocation under bounded compute and context.

## When to apply

- Multi-step reasoning tasks.
- Long-running agent workflows.
- Any system operating under limited context windows.
- Situations where previous observations must influence future search.

## Failure signature

- Agent repeatedly rediscovers previously known information.
- Context window fills with obsolete details.
- Previously disproved hypotheses are revisited.
- Search continues in low-value directions.
- Confidence increases without supporting evidence.

## Corrective action (steps)

1. Compress current state into a bounded summary.
2. Record hypotheses that have been falsified.
3. Re-rank outstanding unknowns by expected information gain.
4. Update confidence only from corroborating evidence.
5. Decay low-confidence and low-priority information over time.

## Verification (checks)

- Working memory remains within its allocated budget.
- State summary reflects current best explanation.
- Disproved hypotheses are retained and prevent repeated exploration.
- Search priorities change as new evidence arrives.
- Confidence tracks accumulated evidence rather than elapsed computation.

## Agent hooks

- Planner: initialize working memory before task execution.
- Executor: append observations and evidence.
- Reviewer: identify contradictions and update disproved hypotheses.
- Memory manager: compress state and remove low-value information.
- Budget manager: enforce fixed memory allocation.

## Definitions (condensed)

- **Working Memory**: A bounded, continuously updated representation of task state.
- **State Summary**: Best current explanation of the problem.
- **Disproved Hypotheses**: Previously tested explanations that evidence rejected.
- **Search Priorities**: Ordered unknowns ranked by expected information gain.
- **Confidence**: Estimated reliability of the current state summary.

## Position within Computational Attention Engineering

Working Memory is the persistent state maintained between attention-allocation cycles. Rather than storing conversation history verbatim, it stores compressed decision-relevant information that guides future computation. It exists to maximize expected information gain while respecting fixed computational budgets.

## Summary

Working Memory is a progressive, lossy representation of current understanding. It enables an agent to preserve evidence, avoid repeating failed reasoning paths, prioritize unresolved questions, and continuously reallocate computational attention as new evidence arrives.

## Structure

1. **State Summary** — Current best estimate of user and system state.
2. **Disproved Hypotheses** — Tested explanations that evidence has rejected.
3. **Search Priorities** — Outstanding unknowns ranked by expected information gain.
4. **Confidence** — Scalar estimate of belief in the current state summary.

## Invariants

- Fixed computational budget.
- Progressive compression.
- Evidence-driven confidence updates.
- Controlled forgetting of low-value information.

## Update Rule

On new evidence *E*:
Summary' = Compress(Summary + E)
Disproved' = Disproved ∪ Contradicted(H, E)
Priorities' = Rerank(Priorities, InformationGain(E))
Confidence' = BayesianUpdate(Confidence, E)



## Examples

### Example 1

A debugging agent records that a database connection is healthy after testing it. Future searches no longer spend attention investigating connectivity failures.

### Example 2

An autonomous research agent discovers that three candidate explanations have been falsified. Those hypotheses remain in working memory, preventing repeated investigation while attention shifts toward unresolved possibilities.

## Keywords

working memory, bounded memory, computational attention, state compression, evidence accumulation, hypothesis tracking, information gain, confidence estimation

## Open Questions

- How aggressively should summaries be compressed?
- Should confidence be represented probabilistically or heuristically?
- What decay schedule best balances forgetting with recovery?

## Research Directions

- Adaptive compression policies.
- Learned information-gain estimators.
- Shared working memory across cooperating agents.
- Attention-budget allocation driven by uncertainty.

## Revision History

- v0.1 — Initial adaptation from Meta AI working memory proposal.


