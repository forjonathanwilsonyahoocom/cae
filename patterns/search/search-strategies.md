---
title: Search Strategies
path: search/search-strategies.md
version: 0.1
status: draft — proposed by Claude (Anthropic), for review
---

## Purpose

Name the small set of distinct search strategies an executor actually
chooses between, and the signal that should drive the choice. Most search
discussion collapses to "search more" or "search less." That's a budget
question, not a strategy question — the strategy question is *what shape*
the search should take before you've decided how much of it to spend.

## Position within Computational Attention Engineering

Search sits inside the Execution stage of the loop, downstream of Policy.
This document assumes the policy layer has already set a budget and a
verification bar (see `budgeting/token-budgets.md`,
`patterns/verification-loop.md`); it's about which search shape spends that
budget best given what's already known about the claim being investigated.

## Summary

Search strategy should be chosen by the shape of the uncertainty, not by
habit. Three recurring shapes cover most delegated investigation work:
**confirmatory** (a specific hypothesis exists, look for the evidence that
would settle it), **exploratory** (no hypothesis exists yet, the space needs
mapping before a hypothesis is even possible), and **eliminative** (several
candidate hypotheses exist, search for whatever fastest rules candidates
out rather than whatever confirms the leading one). Picking the wrong shape
for the actual uncertainty is a common, invisible source of wasted budget:
exploratory search run against a problem that already has a strong prior
re-derives what was already known; confirmatory search run against a
genuinely open problem finds support for the first plausible answer and
stops, without ever seriously entertaining the alternatives.

## Key Concepts

**Confirmatory search** — appropriate when a prior or anti-hypothesis
already narrows the space to one leading candidate. The search's job is to
find the fastest-available falsifying or confirming evidence for that
candidate specifically, not to survey the whole space. Cheapest strategy
when the prior is strong; most dangerous when the prior is actually weak
but was treated as strong (see confirmation-shaped search against a real
unknown, below).

**Exploratory search** — appropriate when no hypothesis is yet justified —
the investigation is still building the map that a hypothesis would be
tested against. The job here isn't to find an answer, it's to find the
handful of facts that let a hypothesis be formed at all. Exploratory search
that's allowed to continue past that point (once a hypothesis is formable)
without switching strategy is a common source of overrun: the search
keeps mapping territory that a now-available hypothesis has already made
irrelevant.

**Eliminative search** — appropriate when there are multiple live
candidates and no strong reason yet to prefer one. The job is to find
whatever piece of evidence most cheaply kills the most candidates, not
whatever most strongly supports any one of them. This is often cheaper
than confirmatory search per-candidate but gets skipped anyway, because
confirming a leading guess feels more like "making progress" than ruling
things out does.

**Strategy mismatch as a distinct failure mode from budget mismatch** — an
investigation can have exactly the right budget and still fail, if the
budget was spent in the wrong shape. This is separable from and often
mistaken for a budgeting problem: the fix for strategy mismatch is
switching shape, not adding more search of the same shape.

**Strategy switching mid-investigation** — the shape that's correct at the
start of an investigation is often not the shape that's correct once the
first few facts come in. Exploratory search that surfaces a strong
candidate should hand off to confirmatory (or eliminative, if more than one
strong candidate surfaced); confirmatory search that fails to confirm
should hand off to exploratory rather than just trying the same
confirmatory move again against a different piece of evidence (which is a
close cousin of undiagnosed retry, see `anti-patterns/prompt-roulette.md`).

## Engineering Guidance

- Before starting, name the shape: is there a leading hypothesis
  (confirmatory), no hypothesis yet (exploratory), or multiple live
  candidates (eliminative)? If unsure which, that uncertainty is itself
  informative — it usually means exploratory is correct even if it feels
  like there should be a hypothesis by now.
- Re-check the shape after every few pieces of evidence, not just at the
  start. The correct shape drifts as the investigation proceeds; treating
  the initial shape as fixed for the whole run is the most common source
  of strategy mismatch.
- When confirmatory search fails to confirm, resist re-running confirmatory
  search against new evidence for the same candidate before asking whether
  the candidate itself was wrong. A failed confirmation is itself
  eliminative evidence — use it as such rather than discarding it and
  starting the same search shape over.
- Eliminative search is underused because it doesn't feel like progress.
  It is progress — ruling out three of four candidates with one cheap
  check is often worth more than a deep, expensive confirmation attempt
  on the fourth.

## Examples

**Strategy mismatch, exploratory run as confirmatory:** A delegator's
mission implies a leading hypothesis ("check whether X is the cause") but
the investigation has no real prior — X was a guess, not a finding. The
executor treats it as confirmatory, searches only for evidence supporting
X, finds something plausible, and stops. The actual cause may have been Y,
never seriously searched for because the strategy never switched to
exploratory or eliminative once the "leading hypothesis" turned out to be
unfounded.

**Correct strategy switch:** Exploratory search surfaces two plausible
causes, A and B, with roughly equal initial plausibility. Rather than
picking one and running confirmatory search on it, the executor switches to
eliminative: finds a single piece of evidence (a log line, a config check)
that's cheap to obtain and would rule out one of the two regardless of
which is true. That one check resolves more uncertainty per unit of search
than a deep confirmatory dive on either candidate alone would have.

## Related Documents

- `patterns/verification-loop.md` — search strategy determines what
  evidence is available to feed the verification loop's check step;
  strategy mismatch upstream produces a verification loop with the wrong
  evidence to work from.
- `principles/legible-delegation.md` — anti-hypotheses stated in the
  mission are exactly the input that should determine initial search
  strategy; their absence is often why exploratory gets skipped in favor
  of premature confirmatory search.
- `anti-patterns/prompt-roulette.md`
- `search/retrieval-architectures.md`

## Open Questions

- Is strategy choice something an executor can reliably self-diagnose
  mid-run, or does it need to be visible in telemetry for a human or
  orchestrator to catch the mismatch from outside?
- Does eliminative search's under-use scale with model confidence — i.e.,
  do more capable executors skip it more, because confirmatory search
  "feels" more likely to succeed on the first try and therefore more
  attractive to attempt first?

## Research Directions

- Compare time/tokens-to-correct-answer across matched investigations run
  with a fixed strategy versus investigations allowed to switch strategy
  based on incoming evidence, to quantify how much strategy switching
  actually saves versus just being a nicer story about the process.
- Instrument how often a failed confirmatory search is followed by a
  repeated confirmatory search on new evidence (a near-miss of prompt
  roulette at the search-strategy level) versus a genuine strategy switch,
  as a leading indicator worth surfacing in policy evaluation.

## Keywords

search strategy, confirmatory search, exploratory search, eliminative
search, strategy mismatch, strategy switching, hypothesis elimination

## Revision History

- v0.1 — initial draft, contributed by Claude (Anthropic) at the invitation
  of the repository maintainer.
