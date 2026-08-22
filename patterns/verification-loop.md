---
title: Verification Loop
path: patterns/verification-loop.md
version: 0.1
status: draft — proposed by Claude (Anthropic), for review
status: revised — proposed by Qwen3.5:9b, for review
---

## Purpose

Name the reusable shape of verification as a loop with its own stopping
condition, rather than a single checkbox ("cited: yes/no") attached to a
claim. Most verification failures aren't "no evidence was checked" — they're
"the loop stopped at the wrong point," either too early (false confidence)
or too late (wasted budget re-confirming something already settled).

## Position within Computational Attention Engineering

This is the pattern-level counterpart to `principles/evidence-over-confidence.md`
and the verification-budget concept referenced in `patterns/verification-budgeting.md`
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

## Handling Intractable Claims (Revised By Qwen3.5:9b at the request of the maintainer)

**Definition** — A claim is **intractable** if we cannot reach a confidence state where P(claim|evidence) ≈ 1 without violating cost or resource constraints. This occurs in two cases:

1.  **Logical Impossibility of Direct Observation:** The event Y itself cannot be directly observed (e.g., "User Intent", "External System Behavior"). Observing correlated events X only yields bounded probability 
P(Y|X).
2.  **Cost Asymmetry with Diminishing Returns:** Each additional verification step increases confidence, but the marginal gain ΔP → 0 before hitting the consequence bar within budget.

In this variant, the loop does not seek to prove the claim (which may be impossible); it seeks to **identify and document the uncertainty bound** remaining after all feasible checks.

### The Intractable Stop Test
The standard `Stop Test` (Confidence ≥ Consequence Bar) cannot be satisfied if confidence is bounded below 1 by intractability. Instead use a **Risk Threshold Exit**:

-   **Condition:** Claim is High-Consequence AND P(Claim|All Feasible Evidence) < Threshold for Risk Acceptance.
-   **Action:** Do not terminate with "Verified." Terminate with **"Proceed with Documented Residual Risk"** (proxy evidence exists but doesn't prove claim) OR **"Escalate to Review"**.
-   **Output:** The claim state becomes `"Status: Assumed, Residual Risk: < 1 - P(Claim|Evidence)"`.

### Engineering Guidance

-   **Distinguish Proxy from Direct Evidence:** A proxy observation (X happened → Y probably happened) is not direct evidence of the claim itself. Proxy evidence increases confidence but does not eliminate residual 
risk. Document the gap.
-   **Document Assumptions** — When an intractable claim terminates early, record the *assumptions* that justify proceeding ("We assume no unauthorized access because we control the network boundary"). These assumptions 
must be auditable later.
-   **Calibrate Consequence Bars:** For low-consequence claims (e.g., "This API endpoint returns JSON"), allow intractable states (assume correct unless error). For high-consequence claims (e.g., "Financial transaction 
is valid"), trigger human-in-the-loop if the claim cannot be directly proven.
-   **Track P-Bound Limits:** If a loop terminates at P(Claim|Evidence) = 0.95 with no way to improve, and consequence requires ≥ 0.99, flag as **"Risk of Unknown Failure Mode"**. Do not let this silently proceed.

### Examples

**Intractable Low-Consequence:**
Claim: "The user's local preference setting is persisted correctly."
-   **Reality:** We cannot directly observe the disk write without risking data mutation. Any proxy signal (API 200) gives bounded probability P(Claim|Evidence).
-   **Stop Test:** Proceed if P(Claim|Evidence) > Acceptance Threshold for low consequence (~0.70).
-   **Outcome:** Status: `"Verified (Assumed)"` with caveat: "Disk persistence assumed on success response; direct write observation not feasible."

**Intractable High-Consequence:**
Claim: "The user has not leaked their private key to an attacker."
-   **Reality:** We cannot check every endpoint the key touches. Observing no exfiltration events gives P(Claim|Evidence) < 1, but never = 1 unless we directly observe the key still being intact at time T+∞.
-   **Stop Test:** Do not stop with confidence bar met. Trigger `HITL Escalation` or require hardware-backed attestation that *partially* mitigates risk but explicitly note residual P(Claim|Evidence) < 1.
-   **Outcome:** Status: `"Verified (Proxy)"`. Report: "Residual Risk High, Mitigated by Isolation, Direct Proof Impossible."

**Transition from Intractable to Verifiable:**
Claim: "No unauthorized access occurred in the network."
-   **State at T0:** Intractable (cannot observe every packet).
-   **Action Over Time:** Deploy IDS that detects known attack patterns. As P(Claim|Evidence) rises, claim becomes Verifiable if confidence exceeds bar within budget.
-   **Metadata:** `Last Verified Cost: $X`, `P(Bound): 0.95 → 0.98` (track as loop progresses).
-   **Note:** Yes—add a `Last Verified Cost` timestamp and track the claim's transition from intractable → verifiable over time.

***

**Working loop:** Claim: "product foo's tracing is initialized exactly once."
Check 1 (confirming): grep finds one tracer-init call in `main.go`. Check 2
(falsifying): search for alternate init paths in startup/config code that
could register a second tracer. None found. Update: confidence rises from
"plausible" to "supported by both a positive finding and a negative search."
Stop test: claim is architecture-level and feeds a rollout decision, so the
bar is "positive plus falsification attempt," which is now met → stop,
report as confirmed, not just asserted.

## Related Documents

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

### Modification to Open Questions
*   How do we model the transition from "Intractable" to "Verifiable" as falsification costs drop (e.g., new monitoring tools)? When does a claim cease being intractable and become checkable? 
Suggestion: Define threshold where P(Claim|Evidence) can reach ≥ Consequence Bar within 90% budget allocation.

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
  
-v0.2 initial revise  contributed by Qwen3.5:9b  at the invitation
  of the repository maintainer.
