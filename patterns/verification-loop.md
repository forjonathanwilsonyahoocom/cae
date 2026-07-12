---
title: Verification Loop
path: patterns/verification-loop.md
version: 0.1
status: draft — proposed by Claude (Anthropic), for review
---

## Purpose

Name the reusable shape of verification as a loop with its own stopping
condition, rather than a single checkbox ("cited: yes/no") attached to a
claim. Most verification failures aren't "no evidence was checked" — they're
"the loop stopped at the wrong point," either too early (false confidence)
or too late (wasted budget re-confirming something already settled).

## Position within Computational Attention Engineering

This is the pattern-level counterpart to `verification/source-verification.md`
and the verification-budget concept referenced in
`principles/legible-delegation.md` and `anti-patterns/prompt-roulette.md`. If
a verification budget answers "how much proof does this claim type need,"
this document answers "what does spending that budget well actually look
like, step by step, and how do you know when to stop."

## Summary

A verification loop has four parts: **claim**, **check**, **update**,
**stop test**. State something, look for evidence that would confirm or
falsify it, update confidence based on what you found, then re-run the stop
test — not "did I check something" but "does my current confidence meet the
bar this claim's consequence requires." The loop is reusable precisely
because the stop test is separable from the checking: the same loop
mechanics apply whether the bar is one citation or four independent
confirmations, because the bar is a property of the claim's consequence, not
of the loop itself.

Most degenerate verification isn't a missing loop — it's a loop with no
stop test, so it either runs once and calls that "verified" regardless of
consequence, or it runs until the executor runs out of budget regardless of
whether confidence was ever actually low.

## Key Concepts

**Claim, not question** — the loop verifies a specific, falsifiable
statement ("tracing is initialized exactly once"), not an open question
("how does tracing work"). A question has no natural stop test; a claim
does, because a claim can be confirmed, weakened, or reversed by a specific
piece of evidence.

**Confirming vs. falsifying checks** — a loop that only looks for evidence
that would confirm the claim will find some and stop too early; it never
tests the claim against the case that would break it. A well-formed check
step includes at least one attempt at falsification, not just corroboration.

**Confidence as the loop's state, not its output** — the loop doesn't run
until it "proves" the claim; it runs until confidence crosses the bar the
claim's consequence sets. This means the loop can legitimately terminate
at moderate confidence for a low-consequence claim, and that's not a
shortcut — it's the loop working correctly.

**Independence of confirmations** — for claims that need more than one
confirmation, the confirmations only count as separate evidence if they're
actually independent (different code path, different data source, different
method) — not the same fact re-observed through a second lens that would
fail the same way the first one would if the underlying assumption were
wrong.

**Stop test as the reusable part** — "one citation is enough" and "three
independent confirmations required" are the same loop with different
thresholds. The reusability is in the loop shape (claim → check → update →
stop test), not in any fixed number of checks — a pattern description that
hardcodes a specific count isn't actually reusable, it's a policy for one
claim type presented as if it were the general case.

## Engineering Guidance

- Write claims as falsifiable statements before starting the loop, not
  after. If you can't state what evidence would change your mind, you
  don't have a claim yet, you have a hunch — verify that first.
- Budget at least one falsification attempt per claim that crosses a
  meaningful consequence threshold, even if the first confirming check
  looked solid — confirming evidence found first is not the same as
  confirming evidence found *only*.
- When a loop terminates, record why it stopped — bar met, budget
  exhausted, or evidence exhausted (nothing more to check) — because these
  three outcomes should be reported differently. "Budget exhausted, bar not
  met" is a materially weaker claim than "bar met" and should say so.
- Don't let loop iteration count substitute for the stop test. A claim
  that gets re-checked five times with the same kind of evidence hasn't
  gained five times the confidence of one check — near-duplicate checks are
  cheap to run and easy to mistake for rigor.

## Examples

**Degenerate loop (no stop test):** "Confirm the config value is correct."
→ one grep finds a matching value → done. No attempt to check whether a
second config source overrides it, no consequence-based bar, just "found
something, stop."

**Working loop:** Claim: "product foo's tracing is initialized exactly once."
Check 1 (confirming): grep finds one tracer-init call in `main.go`. Check 2
(falsifying): search for alternate init paths in startup/config code that
could register a second tracer. None found. Update: confidence rises from
"plausible" to "supported by both a positive finding and a negative search."
Stop test: claim is architecture-level and feeds a rollout decision, so the
bar is "positive plus falsification attempt," which is now met → stop,
report as confirmed, not just asserted.

## Related Documents

- `verification/source-verification.md`
- `principles/legible-delegation.md` — a legible mission states the bar this
  loop should stop at; without that, the loop has no stop test to run.
- `anti-patterns/prompt-roulette.md` — undiagnosed retries often skip this
  loop entirely, treating "try again" as a substitute for locating which
  claim was actually unverified.
- `budgeting/token-budgets.md`

## Open Questions

- How should the loop handle claims where falsification is expensive
  relative to confirmation (common in codebases where "absence of X"
  requires broader search than "presence of X")? Is an asymmetric budget
  (more spent looking for confirmation, capped effort on falsification)
  ever legitimate, or does that reintroduce the confirming-only failure
  mode by budget rather than by design?
- Can "why the loop stopped" be captured cheaply enough in telemetry to be
  worth doing on every claim, or only on claims above some consequence
  threshold?

## Research Directions

- Compare claim survival rate (does the claim still hold under later,
  independent review) between loops that included a falsification check
  and loops that didn't, matched by claim type and consequence.
- Measure whether "confidence as loop state" produces more calibrated
  final confidence than fixed-count verification policies (e.g., "always
  get three sources") across a range of claim types.

## Keywords

verification loop, claim, falsification, confidence, stop test,
independent confirmation, verification budget

## Revision History

- v0.1 — initial draft, contributed by Claude (Anthropic) at the invitation
  of the repository maintainer.
