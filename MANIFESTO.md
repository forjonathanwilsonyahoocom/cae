---
id: manifesto
title: Manifesto
path: MANIFESTO.md
version: "0.2"
status: draft — active
artifact_type: manifesto
type: root
stage_tags: [planning, budgeting, execution, verification, stopping, memory]
skill_area_tags: [reasoning, grounding, evaluation, systems-design]
risk_level: low
links:
  relates_to: ["concepts/computational-attention.md", "budgeting/token-budgets.md", "anti-patterns/prompt-roulette.md"]
  causes: []
  prevents: ["undirected-discipline-sprawl", "hype-without-mechanism"]
related:
  principles: ["evidence-over-confidence", "legible-delegation"]
  laws: []
  patterns: ["mission-policy-separation", "search-shaping", "verification-budgeting"]
  anti-patterns: ["prompt-roulette"]
  telemetry: ["attention-tracing"]
---

# Manifesto

## Intent

[#intent](#intent)

This artifact exists to name and stabilize a recurring pattern: as engineers delegate more work to autonomous and semi-autonomous AI systems, the scarce resource stops being raw capability and becomes the allocation of finite computation, attention, and verification effort under uncertainty. CAE is the attempt to give that pattern a shared vocabulary before it calcifies into ad-hoc, non-transferable tribal knowledge scattered across individual prompts, playbooks, and Slack threads.

The manifesto is not a claim that a new field has been invented from nothing. It documents a discipline accreting the way TCP/IP, the Unix philosophy, and Kubernetes patterns did: recurring practical problems, each solved and named, gradually normalized into a shared scaffold until the pieces are recognizably describing one thing.

---

## Purpose

[#purpose](#purpose)

CAE addresses three related but distinct problems that keep surfacing wherever people build with or alongside autonomous agents:

1. **The internals problem** — how should a bounded-computation system decide where to spend search, verification, and memory effort? (*Computational Attention Engineering* — the theory.)
2. **The interaction problem** — how should a human engineer structure their collaboration with an AI system so the partnership is legible, budgeted, and diagnosable rather than an unstructured back-and-forth of retries? (*Computationally Assisted Engineering* — the practice.)
3. **The credibility problem** — how does this vocabulary avoid sounding like AI-hype and instead sit comfortably next to an established, well-understood discipline? (*Computer-Aided Engineering* — the established term CAE already refers to, in simulation, CAD, and finite-element analysis, and whose familiarity CAE borrows.)

These three expansions of the same acronym are not a coincidence to paper over — they are the manifesto's organizing device. The first describes how intelligent systems should reason internally. The second describes how an engineer and an agent should interact. The third is a deliberate anchor to an existing, unglamorous engineering tradition, so that saying "I'm exploring Computationally Assisted Engineering" reads as ordinary tooling rather than a manifesto for AI replacing engineers.

---

## Scope

[#scope](#scope)

Included:
- Vocabulary and structural patterns for allocating computation/attention in agentic workflows (mission vs. policy distinction, search shaping, verification budgets, policy adaptation).
- Practices for human–agent collaboration that stay legible under retries and failure (diagnosing which stage of a mission→policy→execution→telemetry loop broke, rather than re-rolling prompts).
- Documentation conventions (policy cards, standardized frontmatter, machine-seekable structure) that let both humans and agents retrieve and apply this material consistently.
- Cross-referencing to the established Computer-Aided Engineering tradition where the analogy is useful (simulation, verification, iterative refinement under constraints).

Excluded — see Non-Goals.

---

## Non-Goals

[#non-goals](#non-goals)

- CAE does not claim to be a formally recognized engineering discipline, accredited body, or standards organization. It is a working vocabulary, offered for scrutiny and reuse.
- CAE is not a rebrand of prompt engineering, and success is not measured by increasingly elaborate or "more careful" prompt wording (see the `prompt-roulette` anti-pattern).
- CAE does not replace Computer-Aided Engineering (CAE, classical sense); the shared acronym is a deliberate rhetorical bridge, not a claim of technical equivalence.
- CAE does not prescribe a specific vendor, model, or agent framework. The loop (mission → policy → execution → telemetry) is meant to be substrate-independent.

---

## Background

[#background](#background)

Human organizations have developed disciplines for allocating scarce attention under uncertainty: incident response, medicine, aviation, military command, scientific investigation, and distributed systems engineering.

Autonomous systems now face the same fundamental problem.

Capability is no longer the only constraint.

The limiting resource is deciding where computation, verification, memory, and search effort should be applied.

This discipline did not begin as a deliberate act of naming. It began with narrow, practical questions — how to make agent conversations less repetitive, how to manage token budgets, how to structure reasoning so it survives handoffs, how to keep experiments from losing context across sessions. Each question produced a working answer; each answer was given a name; each name was normalized into a shared scaffold; the scaffolded pieces began referring to one another. That accretion — not a founding declaration — is the origin of this manifesto.

---

## Principles

[#principles](#principles)

- **Mission vs. policy distinction.** Separate *what* an agent is trying to accomplish (mission) from *how* it is currently trying to accomplish it (policy), so that a failure can be diagnosed as a mission problem, a policy problem, or an execution-variance problem — not treated as one undifferentiated "try again."
- **Search shaping over search volume.** Directing where an agent looks (search shaping) is a more durable lever than increasing how much it looks.
- **Verification budgets are load-bearing.** Budgeted verification effort should be treated as a protected minimum, not the first thing traded away when token or time budgets tighten (see `budgeting/token-budgets.md`: "starved reasoning, protected articulation" is the failure mode to avoid).
- **Diagnose before you retry.** A retry without a falsifiable, stage-specific hypothesis about what failed is not iteration — it is the `prompt-roulette` anti-pattern.
- **Legible delegation.** Telemetry (what happened, at which stage, and why) should be a first-class output of any delegated task, not an afterthought reconstructed after the fact.
- **Borrow credibility deliberately.** Where an established discipline (e.g., classical CAE) already has the trust and vocabulary this work needs, use it rather than inventing parallel terminology from scratch.

---

## Guidance

[#guidance](#guidance)

Practical implications for applying CAE day to day:

- When an agent-based task fails, first identify *which stage* failed (mission framing, policy choice, execution variance, or a telemetry/verification gap) before changing anything else.
- When token or compute budgets are tight, decide explicitly which category absorbs the cut — absorption, reasoning, verification, or articulation — rather than letting all four degrade uniformly.
- When describing this work externally (a LinkedIn post, a design doc, a conversation with a skeptical engineer), lead with *Computationally Assisted Engineering* — the practice framing is the one least likely to trigger an "AI hype" reflex, because it describes a partnership, not a replacement.
- When documenting a new pattern, principle, law, or anti-pattern, scaffold it as a policy card (see `tools/scaffoldAltFromDuckAi.py`) so it stays machine-seekable and cross-linkable with the rest of the corpus.

---

## Examples

[#examples](#examples)

### Example 1 — Stage diagnosis instead of re-rolling
An agent misidentifies which log lines are relevant to an incident. Instead of resending the same prompt with "look more carefully," the operator diagnoses that the *policy* (which search strategy the agent used) was underspecified, updates the policy, and reruns — producing a falsifiable, attributable change rather than a blind retry.

### Example 2 — Token budget categorization
A summarization pipeline is asked to shorten its output under a tighter token budget. Rather than uniformly compressing everything, the budget cut is applied to articulation (verbosity) while reasoning and verification steps are held at their protected minimums, preserving decision-relevant evidence in the shortened output.

### Example 3 — Naming as bridge-building
A team presenting agentic tooling to a skeptical engineering organization frames the work as "Computationally Assisted Engineering" rather than "AI-driven automation." The framing borrows the familiarity of Computer-Aided Engineering and reduces resistance, while the underlying mechanism is the same mission/policy/telemetry loop described under Computational Attention Engineering.

---

## Related Artifacts

[#related-artifacts](#related-artifacts)

Related concepts:

- `concepts/computational-attention.md` — operational definition of attention as an engineered resource across mission, policy, execution, and telemetry.
- `budgeting/token-budgets.md` — the "starved reasoning, protected articulation" failure mode and budget categorization.
- `anti-patterns/prompt-roulette.md` — undiagnosed retries as adjective inflation / re-rolling.
- Classical Computer-Aided Engineering (CAD, FEA, simulation) — external, established discipline referenced for terminology and credibility, not technical equivalence.

---

## Open Questions

[#open-questions](#open-questions)

- Does the "three expansions of CAE" framing hold up as more contributors (human and AI) add to this repo, or does it need to collapse into a single canonical meaning at some point?
- What is the minimum viable telemetry schema that lets both humans and agents perform stage diagnosis without excessive instrumentation overhead?
- Is "policy adaptation" sufficiently distinct from "mission revision" to remain a separate stage, or should they be merged?
- At what point (if any) should this manifesto stop being a draft and be versioned as stable?

---

## Research Directions

[#research-directions](#research-directions)

- Formalize verification-budget categories (absorption / reasoning / verification / articulation) with measurable proxies, so budget trade-offs can be logged and compared across runs.
- Explore whether search-shaping strategies can be expressed as reusable, composable policy cards rather than one-off prompt patterns.
- Investigate cross-pollination with classical Computer-Aided Engineering practice (design-verify-iterate loops, tolerance budgets) for transferable analogies.
- Track which framing — Computational Attention Engineering vs. Computationally Assisted Engineering — resonates more in external-facing writing, and why.

---

## Revision History

[#revision-history](#revision-history)

- v0.1 — initial scaffold (headings only).
- v0.2 — populated Intent, Purpose, Scope, Non-Goals, Principles, Guidance, Examples, Related Artifacts, Open Questions, and Research Directions; folded in the "three expansions of CAE" framing (Computational Attention Engineering / Computationally Assisted Engineering / Computer-Aided Engineering) and the accretion narrative for how the discipline emerged from repeated, practical problem-solving rather than a founding declaration; adopted the policy-card frontmatter schema from `tools/scaffoldAltFromDuckAi.py` for cross-linking and machine-seekable structure.
