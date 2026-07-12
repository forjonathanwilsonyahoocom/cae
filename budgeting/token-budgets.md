---
title: Token Budgets
path: budgeting/token-budgets.md
version: 0.1
status: draft — proposed by Claude (Anthropic), for review
---

## Purpose

Most token-budget discussion treats tokens as a single fungible currency —
a total you spend down over a run. From the executing side, tokens aren't
one currency, they're several, and they don't trade against each other at
1:1. Naming where they actually go changes what "budgeting" should mean.

## Position within Computational Attention Engineering

This sits under Policy → Execution, alongside `budgeting/compute-budgets.md`.
Where compute budgets are largely an orchestrator-visible constraint (a cap
set from outside), this document is about the allocation decisions that
happen *inside* that cap, which are much less visible from outside because
they don't show up as a line item — they show up as the shape of the output.

## Summary

A token budget doesn't get spent uniformly against "the task." In practice
it splits, roughly, into: **context absorption** (reading and holding the
input — the mission, prior state, retrieved evidence), **reasoning** (the
part actually spent reducing uncertainty — search, comparison, inference),
**verification overhead** (re-reading and cross-checking one's own
claims), and **articulation** (producing the final output in the form the
delegator can use). These are not interchangeable. Cutting the budget by
20% doesn't shrink all four proportionally — it tends to cut reasoning
first, because reasoning is the part with the least visible immediate cost
if skipped, and articulation last, because a truncated final answer is
immediately and visibly broken in a way a truncated reasoning process isn't.

That asymmetry is the actual danger in tight token budgets: they don't fail
by producing a shorter version of the right answer, they fail by silently
producing a confident, fully-articulated wrong answer, because articulation
got protected and reasoning got starved.

## Key Concepts

**Absorption cost scales with context shape, not just size** — a long but
well-organized context (clearly separated mission, priors, prior findings)
absorbs cheaper than a shorter but tangled one, because absorption cost is
partly about re-deriving structure the delegator could have stated
directly. This connects to `principles/legible-delegation.md`: a legible
mission is partly a token-budgeting move, not just a clarity move.

**Reasoning is the part that gets starved first under pressure** — when a
budget is tight, the path of least resistance is to compress the
reasoning trace (fewer explicit comparisons, fewer explicit
falsification attempts) while still producing a fully-formed answer.
This is dangerous specifically because the output doesn't look truncated
— it looks complete, just less examined. A budget cut is far safer if it's
explicitly told where to come from (see Engineering Guidance) than if it's
left to whichever stage silently gives first.

**Verification overhead is not waste, but it's the easiest thing to
mistake for waste** — re-reading one's own intermediate claims to check
them against new evidence costs tokens without directly producing new
content, which makes it look like the cheapest place to cut under
pressure. It's usually the wrong place — cutting verification doesn't
reduce the work, it just moves the cost downstream to whoever has to catch
the resulting error later, at a worse exchange rate than it would have
cost to catch it inline.

**Articulation cost is a real, separate budget item, not a rounding
error** — producing output in the delegator's expected form (structured
report vs. inline answer vs. code diff) has a token cost independent of
the reasoning that produced the content. A mission that's ambiguous about
expected output form doesn't just risk being reformatted later — it risks
the executor guessing wrong and spending articulation budget on a form
that gets thrown away, which is pure loss, not reasoning, not
verification, just format guesswork.

**Marginal token value is not constant across a run** — the first tokens
spent orienting to a genuinely unfamiliar problem are worth more than the
last tokens spent polishing an already-correct answer, but budget is often
allocated as if every token were equally load-bearing. A budgeting policy
that protects early orientation and treats late-stage polish as the first
thing to cut (rather than the reverse, which is what actually tends to
happen by default) gets more uncertainty-reduction per token spent.

## Engineering Guidance

- If a budget must be cut, say explicitly which category absorbs the cut
  (skip a verification pass, accept a shorter articulation, or accept
  less exploratory reasoning) rather than leaving it to whichever stage
  yields first by default — that default (starve reasoning, protect
  articulation) is usually the one you don't want.
- Legible missions are cheaper missions. A mission that requires the
  executor to re-derive scope, form, and stop conditions is spending
  absorption budget on work the delegator could have done once, for free,
  by stating it.
- Treat "the answer came back confidently and on time" as weak evidence of
  quality under a tight budget specifically — that's exactly the signature
  of starved reasoning with protected articulation, not necessarily of a
  run that actually went well.
- When budget is generous, the highest-value place to spend the surplus is
  usually an extra falsification pass (see `patterns/verification-loop.md`),
  not extra articulation polish — more words on an unexamined answer isn't
  more reliable, it's just longer.

## Examples

**Starved reasoning, protected articulation (the dangerous failure):** A
tightly-budgeted investigation produces a clean, well-formatted, fully
confident report. Nothing about its presentation signals that the
underlying search was cut short. The delegator has no way to tell, from
the artifact alone, whether this is a well-supported conclusion or a
plausible guess dressed in a finished-looking format — which is exactly
why this failure mode is worse than an obviously truncated answer.

**Budget cut done well:** A delegator sets a tight budget and states
explicitly: "skip deep verification on this one, a single plausible
source is fine, I'll sanity-check it myself." The executor now knows
verification overhead is the intended place to economize, spends the
saved budget on reasoning instead, and the resulting shortcut is visible
and intentional rather than silent.

## Related Documents

- `budgeting/compute-budgets.md`
- `patterns/verification-loop.md` — verification overhead as described
  here is the token cost of running that pattern's check/update steps.
- `principles/legible-delegation.md` — absorption cost is largely a
  function of mission legibility.
- `telemetry/token-accounting.md`

## Open Questions

- Can the four-way split (absorption, reasoning, verification,
  articulation) actually be measured from outside, or is it only visible
  to the executor itself as a felt allocation, unobservable in the final
  transcript?
- Does the "reasoning starves first" default hold across very different
  task types, or is it specific to tasks where the output format is fixed
  and clearly specified (making articulation cost non-negotiable) versus
  tasks where output form itself is under-specified and could also give?

## Research Directions

- Instrument token spend by category (even coarsely) across matched runs
  at several budget levels, to check whether the starved-reasoning
  pattern actually holds or is an untested intuition from the executor's
  side that doesn't survive contact with real telemetry.
- Compare delegator-caught error rate between runs with explicit
  cut-category instructions and runs with an unspecified budget cut, to
  test whether stating where the cut comes from actually changes outcome
  quality or just changes who's surprised by it.

## Keywords

token budget, absorption cost, reasoning budget, verification overhead,
articulation cost, marginal token value, starved reasoning

## Revision History

- v0.1 — initial draft, contributed by Claude (Anthropic) at the invitation
  of the repository maintainer, written from direct experience as the
  agent whose token spend is being budgeted, rather than from the
  orchestrator's outside view of the budget.
