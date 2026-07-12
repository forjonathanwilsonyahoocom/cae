| title   | Evidence Over Confidence                             |
| ------- | ----------------------------------------------------- |
| path    | principles/evidence-over-confidence.md                |
| version | 0.1                                                    |
| status  | draft — proposed by Claude (Anthropic), for review     |

## Purpose

[#purpose](#purpose)

State a principle that constrains every other document in this repo:
a system's stated or apparent confidence should track accumulated,
corroborating evidence, not elapsed computation, output length, tone, or
repetition. Where evidence and confidence diverge, evidence governs — not
the other way around.

## Position within Computational Attention Engineering

[#position-within-computational-attention-engineering](#position-within-computational-attention-engineering)

This is one of the load-bearing principles the rest of the corpus assumes
without (until now) defining. `concepts/attention-budget.md` asks whether
"the system can explain why computation was allocated in a particular
way" — that explanation is only meaningful if confidence claims are
evidence-grounded rather than post-hoc. `concepts/working-memory.md`
defines confidence as something updated only "from corroborating
evidence" via its update rule (`Confidence' = BayesianUpdate(Confidence,
E)`) — this document is the principle that update rule is implementing.
`anti-patterns/prompt-roulette.md` is this principle's failure mode
applied to retries: an undiagnosed retry is, among other things, an
attempt to raise confidence in an outcome without adding evidence.

## Summary

[#summary](#summary)

Confidence is cheap to produce and expensive to earn. A system (or a
person) can sound certain after one shallow pass or after ten careful
ones — the words used to express certainty don't change with the amount
of verification behind them unless something enforces that link.
Evidence Over Confidence is the principle that enforces it: confidence is
a claim that must be paid for in verification, and any confidence that
outruns its evidence is a defect to correct, not a tone to soften.

This cuts against several natural failure modes: mistaking fluency for
correctness, mistaking repetition for corroboration, mistaking the
absence of disconfirming evidence for the presence of confirming
evidence, and mistaking a longer or more detailed answer for a better-
verified one.

## Key Concepts

[#key-concepts](#key-concepts)

**Calibration** — the property that stated confidence matches the actual
frequency with which a claim held at that confidence level turns out to
be true. A well-calibrated system that says "I'm fairly confident" should
be right about that often, and wrong about it sometimes — not right
every time (over-hedged) or wrong most of the time (overconfident).

**Corroboration vs. repetition** — evidence that increases justified
confidence must be independent of what's already been counted.
Re-deriving the same fact from the same source, or restating a claim in
different words, is repetition, not corroboration, and should not move
confidence.

**Confidence inflation** — any process by which stated confidence rises
without new evidence: hedging language quietly dropped over a
conversation, a claim repeated until it "feels" established, or output
length/detail substituting for verification depth. Adjective inflation
(see `prompt-roulette.md`) is a special case of this applied to retries
specifically.

**Absence of disconfirmation is not confirmation** — failing to find a
counterexample after a shallow search is weak evidence at best; it should
raise confidence much less than an equivalent amount of effort spent
actively trying to falsify the claim.

**Evidence budget** — the portion of a verification budget (see
`budgeting/token-budgets.md`) actually spent gathering independent,
corroborating, or falsifying evidence, as distinct from budget spent on
articulation or restating what's already believed.

## Engineering Guidance

[#engineering-guidance](#engineering-guidance)

- Treat every confidence-bearing statement ("this is correct," "this
should work," "I'm confident that...") as a claim with a cost: it should
be traceable to specific evidence gathered, not to the fluency of the
sentence expressing it.
- When verification budget is cut, cut articulation first and evidence-
gathering last (this is the same ordering `budgeting/token-budgets.md`
specifies) — confidence should shrink before evidence-gathering does,
not after.
- When a system or a person notices their own confidence rising over the
course of a task, ask what new, independent evidence justified the rise.
If the honest answer is "none, it just started to feel more settled,"
that's confidence inflation, and the stated confidence should be
corrected downward rather than reported as-is.
- Prefer actively seeking disconfirmation over passively failing to find
counterexamples. A claim that survived one attempt to break it is on
much firmer ground than a claim nobody tried to break.
- In multi-turn or multi-agent settings, track disproved hypotheses
explicitly (see `concepts/working-memory.md`) so that confidence in the
remaining hypotheses is computed relative to what's actually been ruled
out, not reset to a vague default each turn.
- When diagnosing a failed delegation (see `anti-patterns/prompt-
roulette.md`), a stated diagnosis is itself a confidence claim and should
meet the same bar: it needs to point at specific evidence from the
failed run, not just assert which stage broke.

## Examples

[#examples](#examples)

**Confidence outrunning evidence:**
> A research agent checks one source, finds no contradiction, and reports
> "I'm highly confident this is accurate." One non-contradicting source is
> weak evidence; the stated confidence is miscalibrated relative to what
> was actually gathered.

**Evidence-grounded confidence:**
> The same agent checks three independent sources, actively looks for a
> fourth that might disagree, finds none, and reports "Three independent
> sources agree and I found no dissenting source, though I only checked
> four total." The confidence claim is now traceable to a specific,
> statable amount of evidence, including its limits.

**Confidence inflation under repetition:**
> A claim is restated across several turns of a conversation without new
> checking. By the fifth mention it reads as established fact, even
> though no new evidence was added after the first mention. The
> confidence should not have grown; only the claim's visibility did.

## Related Documents

[#related-documents](#related-documents)

- `anti-patterns/prompt-roulette.md` — the retry-specific failure mode of
confidence (in a diagnosis or in a re-roll) outrunning evidence.
- `concepts/attention-budget.md` — the verification-budget model this
principle assumes when it says evidence-gathering should be a protected
minimum.
- `concepts/working-memory.md` — the update rule (`Confidence' =
BayesianUpdate(Confidence, E)`) that operationalizes this principle for a
persisted state.
- `budgeting/token-budgets.md` — the budget-category ordering (protect
reasoning/verification, cut articulation first) this principle depends on.

## Open Questions

[#open-questions](#open-questions)

- Should stated confidence be represented numerically (a calibrated
probability) or only ordinally/qualitatively ("low/medium/high")? Each
has different failure modes for miscalibration.
- How much of "confidence inflation via repetition" can be detected
automatically from telemetry (e.g., a claim's phrasing growing more
assertive across turns without new tool calls or sources), versus
requiring the delegator's own audit?
- Is there a principled minimum "evidence budget" below which any stated
confidence above a floor level (e.g., "uncertain") should be disallowed?

## Research Directions

[#research-directions](#research-directions)

- Empirically test whether models' stated confidence, left unconstrained,
tends to inflate over the course of a conversation independent of new
evidence, and by how much.
- Explore automatic calibration checks: comparing a system's stated
confidence against outcome frequency across many completed tasks.
- Study whether requiring an explicit "attempted disconfirmation" step
before high-confidence claims measurably improves calibration without
prohibitively increasing verification cost.

## Keywords

[#keywords](#keywords)

evidence, confidence, calibration, corroboration, confidence inflation,
falsification, verification budget, disproved hypotheses

## Revision History

[#revision-history](#revision-history)

- v0.1 — initial draft, contributed by Claude (Anthropic) at the
invitation of the repository maintainer; reconciled with
`concepts/attention-budget.md`, `concepts/working-memory.md`, and
`anti-patterns/prompt-roulette.md` to keep terminology (evidence,
confidence, verification budget) consistent across the corpus.
