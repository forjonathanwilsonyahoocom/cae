---
title: Prompt Roulette
path: anti-patterns/prompt-roulette.md
version: 0.1
status: draft — proposed by Claude (Anthropic), for review
---

## Purpose

Name a specific, common failure mode: re-running a failed delegation with
surface-level changes to the prompt, without diagnosing which part of the
Mission → Policy → Execution → Telemetry loop actually broke.

## Position within Computational Attention Engineering

This is the anti-pattern version of `principles/legible-delegation.md`. That
document describes what makes a mission legible on the first attempt.
Prompt roulette is what happens when the first attempt fails and the
response treats the *symptom* (bad output) rather than locating *where in
the loop* the failure occurred.

## Summary

When a delegated task comes back wrong, there are several distinct places
the failure could have originated: an illegible mission, a bad policy, a
sound policy executed against the wrong evidence, or a sound execution the
delegator misjudged in review. Prompt roulette is the practice of skipping
that diagnosis and instead perturbing the prompt — rewording it, adding
adjectives ("be thorough," "be careful"), lengthening it, or re-running it
verbatim — and hoping the next roll lands differently.

It's called roulette because the delegator is spending attention (their own
and the executor's) on repeated tries without a model of why any given try
succeeds or fails. Each re-roll costs a full execution budget and produces
at best one bit of information: pass or fail.

## Key Concepts

**Undiagnosed retry** — a retry issued without first identifying which
stage of the loop failed. Distinguishable from a legitimate retry, which
follows a stated hypothesis about the cause ("the mission didn't state a
stop condition, adding one") and is falsifiable by the next attempt.

**Adjective inflation** — a specific, very common form of undiagnosed
retry: adding intensifiers ("really," "thoroughly," "make sure to")
without adding information. This changes emphasis, not the search space or
the disambiguation available to the executor, so it rarely changes the
outcome and burns a full retry to find that out.

**Verbatim re-roll** — re-running an identical or near-identical prompt on
the hope that stochastic variance produces a better result. Sometimes
reasonable as a cheap first move against a single flaky run, but it
becomes roulette specifically when it substitutes for diagnosis after
repeated failures, rather than being tried once and then abandoned in
favor of a diagnosed retry.

**Diagnosis-free feedback** — telling an executor "no, that's wrong, try
again" without stating *what* was wrong. This looks like feedback but
carries close to zero information — it doesn't tell the executor which
part of its mission-reading, search, or verification to change, so the
next attempt is exploring the same space with the same policy and no new
constraint.

## Engineering Guidance

When a delegated task fails, before re-issuing it, locate the failure:

- **Mission failure** — the executor solved a different problem than the
  one intended. Fix: make the mission more legible (see
  `principles/legible-delegation.md`), don't just resend it.
- **Policy failure** — the mission was clear but the search/verification
  policy was wrong for this task (e.g., insufficient verification budget
  for a claim that turned out to be consequential). Fix: change the
  policy, not the wording.
- **Execution failure given a sound policy** — the policy was reasonable
  but the run happened to explore a bad branch, or the world genuinely
  didn't match the priors. Fix: this is the one case where a retry with
  the same mission and policy is legitimate — the failure was
  variance, not design.
- **Review failure** — the output was actually correct or defensible but
  the delegator's expectation was different from what was asked for. Fix:
  this isn't an execution problem at all; revise the mission, because the
  delegator's real intent wasn't captured the first time either.

A retry is not roulette if it's accompanied by a stated, falsifiable
change: "I'm adding an anti-hypothesis this time because I think the
executor wasted budget on X" is a diagnosed retry. "Let's just try that
again but more carefully" is not — "carefully" isn't a policy change,
it's a hope.

## Examples

**Roulette:**
> Attempt 1: "Investigate the failure." → wrong scope.
> Attempt 2: "Please thoroughly investigate the failure, be sure to be
> comprehensive." → same wrong scope, more tokens spent getting there.

**Diagnosed retry:**
> Attempt 1: "Investigate the failure." → wrong scope; executor explored
> config but the actual failure was in a dependency neither party had
> named.
> Attempt 2: "Investigate the failure. Known priors: config was checked
> and ruled out in the last run. New anti-hypothesis: don't re-check
> config. Check the dependency chain instead." → targeted, informed by
> what the first run actually established rather than discarding it.

## Related Documents

- `principles/legible-delegation.md` — the positive-case document this
  anti-pattern is the failure mode of.
- `principles/evidence-over-confidence.md`
- `telemetry/attention-tracing.md` — a reasoning trace from the failed
  run is usually sufficient to do the diagnosis this anti-pattern skips.

## Open Questions

- Can undiagnosed retry be detected automatically from telemetry alone
  (e.g., near-identical prompt text across consecutive failed runs), or
  does it require the delegator's stated reasoning to distinguish from a
  legitimate variance-driven retry?
- Is there a cheap middle ground between full diagnosis and verbatim
  re-roll — e.g., a minimal "what changed since last attempt" checklist
  that's fast enough to not defeat its own purpose?

## Research Directions

- Compare success-rate-per-retry between undiagnosed re-rolls and
  diagnosed retries on matched failed tasks, to quantify how much
  diagnosis actually buys versus just trying again.
- Study whether adjective inflation ever measurably changes executor
  behavior, or whether it's reliably inert — if reliably inert, that's
  worth stating plainly so delegators stop spending effort on it.

## Keywords

anti-pattern, retry, prompt roulette, diagnosed retry, adjective inflation,
undiagnosed retry, failure attribution

## Revision History

- v0.1 — initial draft, contributed by Claude (Anthropic) at the invitation
  of the repository maintainer.
