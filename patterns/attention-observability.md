---
id: pattern.attention-reporting
type: pattern
artifact_type: pattern
status: draft
summary: Preserve lightweight observations about computational attention across agent boundaries.
---

# Attention Reporting

## Intent

Carry a compact attention report with each completed task.

The report is not intended to measure runtime performance or implementation details. Its purpose is to preserve observations about how computational attention was allocated while solving a problem.

Unlike traditional telemetry, an attention report captures information that would otherwise disappear when an agent hands work back to a user or another agent.

---

## Motivation

Most agent workflows only preserve artifacts:

- code
- pull requests
- documentation
- summaries

The reasoning process that produced those artifacts is largely discarded.

Attention reporting preserves a small amount of that process without requiring detailed execution traces or model internals.

---

## Characteristics

A useful attention report should be:

- inexpensive to produce
- generated from observable behavior
- independent of a specific model or runtime
- compact enough to travel with normal task handoffs
- useful for improving future prompts

The report should describe attention allocation rather than implementation details.

---

## Example Signals

Traditional execution telemetry answers:

> What happened?

Attention reporting instead asks:

> Where was computation spent?

Examples include:

| Signal | Interpretation |
|---------|----------------|
| searches performed | exploration effort |
| files opened | attention breadth |
| highest-information files | information gain hotspots |
| initial hypotheses | prior attention allocation |
| surviving hypothesis | posterior attention allocation |
| rejected hypotheses | intentionally abandoned computation |
| strategy shifts | attention reallocation |
| dead ends | wasted attention budget |
| verification commands | validation budget |
| scope expansion | attention escaped original task |
| policy evaluation | computation saved or redirected by constraints |

These signals are intended as observable proxies rather than exact measurements.

---

## Reporting Pattern

The report should accompany the final task output.

For example:

```json
{
  "attention": {
    "files_opened": 12,
    "files_modified": 10,
    "searches": 8,
    "dead_ends": 3,
    "strategy_shifts": 1,
    "scope_expanded": false,
    "highest_information_files": [
      "...",
      "...",
      "..."
    ],
    "initial_hypotheses": [],
    "surviving_hypothesis": "",
    "rejected_hypotheses": [],
    "verification_summary": {}
  }
}

```

The exact schema is intentionally flexible.

The goal is to preserve useful observations rather than enforce a universal format.

Discussion

Attention reports should not require additional instrumentation.

If a runtime exposes richer telemetry (token counts, execution timings, internal traces), those values may be included.

Otherwise, best-effort observational proxies are sufficient.

The report should summarize work already performed rather than expand the scope of the task.

Relationship to CAE

Attention reporting makes computational attention observable.

By preserving lightweight reports across task boundaries, future work can refine prompts, policies, and workflows using evidence from previous attention allocation rather than relying on intuition alone.

The report is therefore an observational artifact rather than a runtime metric.


notes from gpt:

One thing I especially like is the subtle shift in terminology.

Most systems talk about **execution telemetry**.

CAE can distinguish between two fundamentally different classes of observation:

- **Execution telemetry** — CPU time, tokens, latency, API calls, memory.
- **Attention reporting** — where computation was *directed*, how it was redirected, what was abandoned, and which constraints shaped the search.

