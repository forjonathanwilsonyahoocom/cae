---
id: layout-before-logic
title: Layout-Before-Logic (Enforced Topology)
path: patterns/layout-before-logic.md
version: "0.1"
status: draft
artifact_type: pattern
type: pattern
stage_tags: [verification, budgeting, learning, execution]
skill_area_tags: [evaluation, decision-making, resource-allocation]
risk_level: high
links:
  relates_to:
    - concepts/attention-budget.md
    - concepts/working-memory.md
    - principles/evidence-over-confidence.md
  causes: []
  prevents:
    - verification-starvation
    - prompt-roulette
    - overconfidence
  related:
    - patterns/verification-loop.md
  principles:
    - evidence-over-confidence
    - diagnose-before-retry
  laws:
    - constraints-are-computational-inputs
  telemetry:
    - attention-tracing
    - budget-utilization
---

# Pattern: Layout-Before-Logic (Enforced Topology)

**Category:** Architectural Pattern
**Budget affected:** Search (primarily) · Attention (secondarily)
**Status:** Draft — contributed via Gemini, revised for CAE

---

## Problem Statement

When working with highly capable models coupled with deep contextual analysis tooling, developers frequently bypass structural design. They jump straight to writing agent prompts and execution logic.

Without upfront topology constraints, multi-agent systems naturally degrade into a chaotic, fully connected **mesh** network. This results in exponential token consumption, context bankruptcy, race conditions, and untraceable execution paths.

## The Core Concept

Layout-Before-Logic dictates that agent communication boundaries are **immutable architectural constraints**, defined before any runtime behavior or prompt engineering occurs.

Instead of forcing developers to write long, static documentation, they declare the system's topology in a structured config file (`topology.yaml`). At initialization, a **static topology validator** inspects the layout and validates the paths, then a **runtime router** is installed to enforce traffic routing as agents execute.

## The Concrete Schema (`topology.yaml`)

Every multi-agent subsystem must include a `topology.yaml` in its root folder. The runtime engine parses this schema to build the communication graph **before** initializing any model backends.

```yaml
version: "cae.v1alpha"
metadata:
  subsystem_name: "code_review_pipeline"
  declared_topology: "star"  # [star, mesh, linear]

# 1. Node inventory — who exists and what powers them
agents:
  orchestrator:
    backend: "model-a"        # e.g. a large general-purpose model
    description: "Central router and quality gatekeeper"
    max_context_tokens: 40000

  security_scanner:
    backend: "model-b"        # e.g. a fast tool-use model
    description: "Specialized regex and static analysis tool agent"
    max_context_tokens: 16000

  linter_agent:
    backend: "model-c"        # e.g. a small/cheap model
    description: "Syntactic correctness checker"
    max_context_tokens: 8000

# 2. Edge permissions — who is allowed to talk to whom
communication_matrix:
  allowed_routes:
    - from: "orchestrator"
      to: ["security_scanner", "linter_agent"]
    - from: "security_scanner"
      to: ["orchestrator"]
    - from: "linter_agent"
      to: ["orchestrator"]

  # Explicit bans to catch shortcut engineering early
  forbidden_routes:
    - from: "security_scanner"
      to: "linter_agent"
      reason: >
        Security and linting must be aggregated by the orchestrator.
        Direct mesh chatter is blocked.

# 3. Guardrails & telemetry
enforcement:
  on_violation: "fail_fast"  # [fail_fast, log_and_route, trim_context]
  max_total_hops: 6
```

## How the Stack Enforces the Pattern

```

┌───────────────┐
[ topology.yaml ]
└───────────────┘
        │
        ▼
┌──────────────────────────┐
│ Static Topology Validator│  ← inspects communication graph & compilation bounds
└─────────┬────────────────┘
          │
          ▼
┌──────────────────────────┐
│ Runtime Router           │  ← intercepts agent runtime messages
└─────────┬────────────────┘
          │
          ▼
┌───────────────┐
[ Model Backend ]  ← executes prompt only if route is permitted
└───────────────┘
```

**1. Static validation**
Before a single model call is made, a static topology validator acts as the static analysis layer. It parses `topology.yaml` and checks for structural inconsistencies — e.g., an agent declared under `agents` with no entry in `communication_matrix`. If a developer writes an execution loop where `security_scanner` directly invokes `linter_agent`, the validator flags the compilation mismatch immediately during local development.

**2. Runtime interception**
A runtime router is the dynamic telemetry and routing fabric. Every time an agent generates a message intended for another agent, the router intercepts the payload before it reaches the network or the model backend.

- **The handshake check:** the router evaluates the `from`/`to` fields against the parsed `allowed_routes` matrix.
- **The penalty:** if a route is forbidden (e.g., `security_scanner` tries to bypass the orchestrator), the router aborts the execution path, drops the message, and raises an explicit `TopologyViolationError`.

## Architectural Consequences

**Positive trade-offs**
- **Zero-overhead auditing** — the system's architecture can be visually mapped or verified instantly by reading a single YAML file, rather than parsing hundreds of lines of prompt code.
- **Deterministic token spend** — eliminating accidental mesh networks means multi-agent token spend scales linearly with the configured topology, rather than exponentially.
- **Interchangeable backends** — because layout is decoupled from logic, swapping a model backend for another is a one-line config change.

**Negative trade-offs**
- **Initial friction** — developers must spend time up front defining the network map before writing features.
- **Reduced dynamic autonomy** — this pattern actively prevents agents from spontaneously spawning or consulting arbitrary new sub-agents on the fly.

## Related

- Pairs with the four-budget taxonomy (search / memory / attention / verification) — this pattern is primarily a **search-budget** constraint, capping the shape of the communication graph before execution.
- Related anti-pattern candidate: *Mesh Drift* — the un-constrained failure mode this pattern exists to prevent.


### Attribution

With gratitude to every human, agent, and future collaborator whose observations increased the collective attention available to the next experiment.claude, gpt, and gemini all ccontributed to this doc
