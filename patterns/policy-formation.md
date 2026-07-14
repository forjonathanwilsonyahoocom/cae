---
id: policy-formation
title: Policy Formation (Attention-to-Policy)
path: patterns/policy-formation.md
version: 0.1
status: draft — proposed
artifact_type: force
type: force
stage_tags: ["planning", "verification", "memory", "stopping"]
skill_area_tags: ["evaluation", "grounding", "process design"]
risk_level: medium
links:
  relates_to: ["principles/attention-to-policy.md", "concepts/attention-artifacts.md"]
  causes: []
  prevents: ["repeated rediscovery", "non-durable retries", "knowledge thrash across agents"]
  related:
    principles: ["evidence-over-confidence", "durable-evidence"]
    laws: ["policy-compression", "verification-stability"]
    patterns: ["telemetry-as-evidence", "stage-diagnosed-correction"]
    anti-patterns: ["prompt-roulette", "retry-without-constraint"]
    telemetry: ["attention-tracing", "stage-diagnosed-telemetry"]
---

# Policy Formation (Attention-to-Policy)

## Rule
Durable attention should be promoted into policy so future computation inherits the constraint and avoids rediscovering the same information.

## When to apply
- After a solved problem reveals durable constraints (not transient preferences, local accidents, or accidental heuristics).
- When multiple agents or iterations repeat the same discovery step despite having “learned” something informally.
- When you can name what is stable: the invariant, the failure mode, the decision boundary, or the verification requirement.
- When telemetry or observation provides evidence that a discovery persists across runs, contexts, or users.

## Failure signature
- The team repeatedly reallocates computational attention to re-derive the same fact, guideline, or stopping condition.
- Documentation, prompts, or playbooks drift into “reworded folklore” without turning into enforced constraints.
- Retries fix symptoms (wording/temperature/verbosity) rather than promoting the underlying durable constraint.
- Improvements cannot be expressed as a check, rule, or bounded operating condition.

## Corrective action (steps)
- **Separate ephemeral from durable:** Identify which discoveries reduce future uncertainty across contexts or time.
- **State the constraint:** Turn the durable constraint into a policy form (rule, checklist, schema, acceptance criteria).
- **Attach evidence:** Use telemetry/observations as the decision record for promotion (what was observed, when, and why it mattered).
- **Bind the policy to execution:** Ensure downstream artifacts (prompts, libraries, lint rules, APIs, playbooks) inherit the policy.
- **Measure impact as prevention:** Evaluate effectiveness by how much unnecessary exploration it prevents (not by “compliance rates”).
- **Close the loop:** Continue collecting evidence to refine or roll back policies when durability assumptions fail.

## Verification (checks)
- A reader can point to: (1) the durable observation, (2) the promoted policy, and (3) the downstream inheritance point.
- Future agents/tasks can operate without rediscovering the same constraint (the constraint is in a bounded form).
- The policy has an explicit verification check (how it will be known to be “working”).
- When a failure occurs, the system can distinguish between (a) policy violation vs (b) policy falsification (durability was wrong).

## Agent hooks
- Planner: emit a “durability candidate” list (what to promote) alongside the explicit constraint it represents.
- Executor: apply candidate policies and record whether the change eliminated exploratory steps or uncertainty.
- Verifier: run stage-diagnosis to decide whether evidence supports promotion, refinement, or rollback.

## Definitions (condensed)
- **Attention artifact:** An artifact whose primary purpose is to preserve previously expended computational attention so future computation can avoid rediscovering the same information.
- **Policy:** A compressed constraint that future work must operate under (rules, checks, schemas, playbooks, validation gates).
- **Durable attention:** Attention that discovers constraints that persist and generalize enough to remain useful without re-derivation.
- **Promotion:** The step that converts durable observations into policy-bound operating constraints.

## Position within Computational Attention Engineering
This force formalizes a recurring organizational mechanism: expensive discovery is converted into inexpensive constraint. The goal is durable reduction in exploratory compute by promoting stable constraints into policy.

## Summary
When a task reveals durable constraints, those constraints should be promoted into policy rather than rediscovered. Telemetry is useful primarily as evidence for deciding what qualifies as durable and therefore worth promoting. Over time, promoted policies become attention artifacts that bound future attention and reduce thrash.

## Examples
### Example 1: Coding standards
A repeated review outcome (e.g., a specific class of bug) becomes a lint rule and an acceptance check, so future changes inherit the constraint instead of re-deriving the rule.

### Example 2: Prompt refinements
A prompt modification that consistently removes a recurring failure mode is promoted into a named policy: a checklist of required fields, verification steps, and stop conditions—then embedded into future prompts and templates.

### Example 3: Architectural guidelines + validation
A stable performance/latency constraint becomes an architectural policy (interfaces, sizing assumptions, and automated validation), preventing future exploration of incompatible designs.

## Keywords
attention, policy, promotion, durable constraints, compressed computational attention, attention artifacts, telemetry-as-evidence, bounded attention

## Open Questions
- What minimum evidence threshold makes an observation “durable enough” for promotion?
- How should policies decay or be rolled back when durability assumptions fail?
- What is the right granularity: policy as a rule vs policy as a composite artifact (library/tests)?

## Research Directions
- Formalize a durability test: when an observation reduces future exploratory search across stages.
- Define a taxonomy of attention artifacts and map each to a promotion mechanism.
- Measure prevention directly (exploration avoided) rather than indirectly (compliance inferred).

## Revision History
- v0.1 — initial draft gpt5.4nano at duckai revision of discussion w gpt on pregression of telemetry response artifacts — repo maintainer

