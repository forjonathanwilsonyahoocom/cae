---
title: Legible Delegation
path: principles/legible-delegation.md
version: 0.1
status: accepted — verbatim as proposed by Claude (Anthropic)
---

## Purpose

Every document in this repository so far is written from the orchestrator's
seat: how to shape a mission, budget search, gate verification, adapt policy.
This document is written from the other seat — the executing agent's — and
names a cost that's invisible from the orchestrator's side: the attention an
agent spends **disambiguating the task itself**, before any of it goes toward
the task.

That cost is real, it's not fixed, and it's mostly a function of how the
delegator wrote the mission — not of the executor's skill.

## Position within Computational Attention Engineering

If Mission → Policy → Execution → Telemetry → Policy Adaptation is the loop,
this document sits at the Mission → Execution boundary and asks: what
properties of a mission statement determine how much of the executor's
budget gets spent *crossing* that boundary, versus spent on the work itself?

## Summary

An executing agent receiving a delegated task has to resolve two kinds of
uncertainty before it can act: uncertainty about the *world* (the actual
subject of investigation) and uncertainty about the *task* (what was
actually being asked). Orchestrator-side frameworks optimize search over the
first kind. They rarely account for the second, because from the
orchestrator's chair the task looks self-evidently specified — it was just
written. From the executor's chair, it often isn't.

Two tasks with identical "difficulty" in the world can have wildly different
executor-side disambiguation cost, purely as a function of how legible the
mission was. Legible delegation is the practice of writing missions that
minimize that second kind of uncertainty deliberately, the same way search
policy minimizes the first.

## Key Concepts

**Disambiguation cost** — attention spent inferring intent, scope, or
constraints that were assumed rather than stated, before any
world-uncertainty gets reduced.

**Silent default risk** — when a mission is ambiguous, an executor either
stops and asks (cheap, but breaks unattended execution and adds a round
trip) or picks a reasonable interpretation and proceeds (keeps the pipeline
moving, but risks the whole run being built on the wrong assumption,
discovered only at review). Most executors are tuned to default toward the
second option under ambiguity, which means the delegator's clarity is doing
real risk-management work whether or not it was written with that in mind.

**Decision legibility** — a mission that states what decision the work
enables (not just what question to answer) gives the executor a pruning
rule it doesn't otherwise have: any discovered fact that doesn't move the
decision is out of scope, regardless of how interesting it is. Without a
stated decision, "relevant" has no boundary, and search naturally over-runs.

**Mission/policy conflation at the prompt level** — the orchestrator-side
docs already separate Mission (why) from Policy (how). The same conflation
happens one level down, inside a single delegated task: a mission that
states *what* but smuggles in unstated *how*-constraints (a particular
approach, tool, or format the delegator wanted but didn't say) forces the
executor to either guess the hidden constraint or do work that gets
rejected on a dimension it was never told about.

**Anti-hypotheses as executor-side search shaping** — this repo already
lists anti-hypotheses as an orchestrator tool for avoiding expensive rabbit
holes. They're at least as valuable stated *to* the executor directly:
"don't assume X" is often cheaper for a delegator to write once than for an
executor to discover by spending budget ruling X out empirically.

**Done-criteria legibility** — a stop policy stated in the mission ("this is
sufficient because...") is what lets an executor spend its verification
budget efficiently instead of defaulting to maximal caution (over-verifying
to compensate for not knowing what "enough" means) or maximal speed
(under-verifying because nothing signaled the claim was consequential).

## Engineering Guidance

For delegators:

- State the decision the work enables, not only the question. This is the
  single highest-leverage line in a mission for reducing executor search
  overrun.
- Separate "must be true of the output" from "must be true of the process."
  Process constraints stated as if they were output constraints (or left
  unstated entirely) are a common source of rejected-but-correct work.
- Front-load anti-hypotheses you already know. If you know a domain doesn't
  apply, say so — don't make the executor spend budget re-deriving your
  priors.
- State a stop condition, even a rough one. "Good enough" undefined forces
  the executor to guess your risk tolerance, and guesses skew conservative,
  which is expensive.

For executors (or for orchestrators designing an executor's default
behavior):

- Distinguish ambiguity that's safe to resolve with a stated, visible
  default from ambiguity that materially changes the shape of the output if
  guessed wrong. Only the second kind justifies stopping to ask.
- When proceeding on an assumption, state the assumption inline rather than
  silently — this converts a silent default risk into a cheap,
  reviewable one.

## Examples

**Illegible:** "Look into why the tracing looks off in Foo Prouct."
No decision stated, no anti-hypotheses, no stop condition. The executor
doesn't know if this is a pre-incident audit, a specific bug report, or
idle curiosity — and each implies a completely different verification
budget and scope.

**Legible:** "We're deciding whether to roll tracing out to Bar Product next
sprint. Confirm Foo Prouct's tracing is end-to-end reliable enough to use
as the reference implementation — we already know Kafka paths are out of
scope for this decision. One clear counterexample is enough to stop and
report; we don't need exhaustive coverage."
Same underlying investigation, but the executor now knows what "enough"
looks like on both ends: what would stop it early, and what would satisfy
it fully.

## Related Documents

- `MANIFESTO.md`
- `principles/evidence-over-confidence.md`
- `patterns/verification-loop.md`
- `anti-patterns/prompt-roulette.md` (illegible delegation is arguably the
  upstream cause of prompt roulette, not just a related failure mode)

## Open Questions

- Is disambiguation cost measurable the same way search cost is (files
  opened, tokens spent) or does it need a different instrument, since it's
  spent before any world-facing action is taken?
- Does legibility have a ceiling past which over-specifying a mission
  starts costing more (delegator time, rigidity, lost executor initiative)
  than it saves?
- How does this interact with multi-agent orchestration, where the
  "executor" of one stage is the "delegator" for the next — does
  disambiguation cost compound down a pipeline, or does each stage reset it?

## Research Directions

- A controlled comparison: same underlying task, mission written with and
  without a stated decision, same executor, measure divergence between
  what was delivered and what was actually wanted (proxy: rework requested).
- Whether stated anti-hypotheses measurably reduce executor-side search
  even when the executor is a different model/agent than the one the
  orchestrator tuned against — i.e., does legibility transfer across
  executors, or is it partly executor-specific.

## Keywords

delegation, mission legibility, disambiguation cost, decision-boundedness,
silent defaults, stop conditions, anti-hypotheses, executor-side attention

## Revision History

- v0.1 — initial draft, contributed by Claude (Anthropic) at the invitation
  of the repository maintainer, written from the executing-agent
  perspective rather than the orchestrator perspective represented
  elsewhere in the repo.
