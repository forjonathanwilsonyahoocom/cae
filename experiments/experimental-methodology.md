---
id: experimental-methodology
title: experimental-methodology
path: experiments/experimental-methodology.md
version: "0.1"
status: draft
artifact_type: experiments
type: conceptual_framework
stage_tags: [execution, verification, communication]
skill_area_tags: [decision-making, risk-management, human-ai-interaction]
risk_level: high
links:
  relates_to:
    - telemetry/budget-utilization.md
    - concepts/working-memory.md
    - concepts/attention-budget.md
    - principles/evidence-over-confidence.md
  causes: []
  prevents:
    - hallucination
    - overconfidence
    - unbounded-computation
  related:
    - patterns/verification-loop.md
  principles:
    - evidence-over-confidence
    - diagnose-before-retry
  laws:
    - constraints-are-computational-inputs
    - diagnose-before-retry
  telemetry:
    - budget-utilization
    - attention-tracing
---

# Experimental Methodology

## Intent

Computational Attention Engineering (CAE) treats experimentation as the primary
mechanism by which attention systems evolve.

Unlike traditional software engineering, where implementations are expected to
follow a predefined design, CAE assumes that the complete design is unknowable
before experimentation begins.

Experiments therefore exist to discover structure rather than merely validate
hypotheses.

---

## Principles

### Every artifact is provisional

No document, prompt, model, implementation, or visualization is considered
canonical.

Every artifact is an observation of the current understanding.

Understanding evolves faster than documentation.

---

### Preserve observations before explanations

Record surprising behavior before attempting to explain it.

An unexplained observation is often more valuable than a polished but incorrect
theory.

---

### Instrument first

If an experiment cannot tell us why it succeeded or failed,
it was not actually an experiment.

Instrumentation is considered part of the experiment itself.

Metrics should evolve alongside the system.

---

### Optimize for discovery

The purpose of experimentation is not maximizing benchmark scores.

The purpose is increasing understanding.

Useful experiments frequently:

- reveal unexpected failure modes
- expose hidden variables
- invalidate assumptions
- suggest entirely new experiments

---

## Evolutionary Loop

Experiments proceed through a repeating loop:

Observe

↓

Question

↓

Construct

↓

Instrument

↓

Run

↓

Explain

↓

Archive

↓

Generate Better Questions

Each completed experiment increases the attention budget available for future
experiments.

Knowledge compounds.

---

## Human-Agent Collaboration

CAE assumes experimentation occurs across an evolving network of participants.

Participants may include:

- humans
- language models
- specialized agents
- automated tooling
- instrumentation systems
- future experimental frameworks

Each participant contributes observations.

No participant is assumed to possess the complete model.

The role of methodology is coordinating discovery rather than assigning authority.

---

## Experimental Layers

Experiments naturally emerge at multiple scales.

### Local

Implementation details.

Example:

- routing algorithm
- embedding choice
- cache strategy

---

### Structural

Architecture decisions.

Example:

- dendrogram organization
- split heuristics
- routing policies

---

### Behavioral

Emergent properties.

Example:

- stability
- convergence
- exploration
- attention allocation

---

### Methodological

Improving experimentation itself.

Examples include:

- new visualization techniques
- improved instrumentation
- agent orchestration
- experiment generation
- automatic hypothesis tracking

These experiments improve future experiments.

---

## Evolution of an Experiment

The Phylo project illustrates this progression.

Initially:

One engineer.

One repository.

Simple routing experiments.

As understanding increased, experimentation expanded to include:

- visualization
- profiling
- telemetry
- replay systems
- notebooks
- documentation
- multiple language models
- agent workflows
- autonomous analysis
- orchestration tooling

The experimental system eventually became more significant than any individual
algorithm.

This progression is expected rather than exceptional.

Successful experiments naturally produce richer experimental ecosystems.

---

## Success Criteria

A successful experiment is one that increases collective understanding.

Possible outcomes include:

- validating an idea
- disproving an assumption
- revealing hidden structure
- exposing missing instrumentation
- generating new questions
- producing reusable knowledge

Failure is only the absence of learning.

---

## Archival

Every experiment should leave behind enough information that future humans or
agents can reconstruct:

- intent
- context
- inputs
- outputs
- observations
- conclusions
- unanswered questions

Experiments are investments in future attention.

The archive is therefore part of the experiment itself.

---

## Closing Observation

CAE views experimentation as an evolutionary process operating on knowledge
rather than code.

The objective is not merely to build better systems.

The objective is to build systems that become better at discovering how to build
better systems.



### Attribution

This methodology is distilled from years of iterative experimentation spanning the Creative Phylo project, production advertising systems, distributed observability, agent-assisted software engineering, and countless conversations between human practitioners and language models. It reflects lessons learned collaboratively rather than authored individually.

With gratitude to every human, agent, and future collaborator whose observations increased the collective attention available to the next experiment.

In love and trust.
