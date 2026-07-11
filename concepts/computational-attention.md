version: 0.1

repository:
  name: computational-attention-engineering
  title: Computational Attention Engineering
  description: >
    An open engineering discipline for designing how autonomous systems
    allocate finite computational attention under uncertainty.

document_template:
  sections:
    - Purpose
    - Position within Computational Attention Engineering
    - Summary
    - Key Concepts
    - Engineering Guidance
    - Examples
    - Related Documents
    - Open Questions
    - Research Directions
    - Keywords
    - Revision History

directories:

  - name: concepts
    description: Core terminology and foundational definitions.

  - name: principles
    description: Engineering principles that remain stable over time.

  - name: policies
    description: Attention allocation strategies and decision policies.

  - name: patterns
    description: Reusable engineering solutions.

  - name: anti-patterns
    description: Common failure modes.

  - name: telemetry
    description: Measurement and observability.

  - name: verification
    description: Trust, validation and evidence.

  - name: memory
    description: Memory architectures.

  - name: search
    description: Retrieval and search methodologies.

  - name: budgeting
    description: Compute, latency and token allocation.

  - name: orchestration
    description: Multi-agent coordination.

  - name: experiments
    description: Experimental methodology.

  - name: metrics
    description: Quantitative evaluation.

  - name: adr
    description: Architecture Decision Records.

  - name: case-studies
    description: Practical applications.

  - name: glossary
    description: Canonical terminology.

documents:

  - path: README.md
    title: Computational Attention Engineering
    purpose: Repository overview

  - path: MANIFESTO.md
    title: CAE Manifesto
    purpose: Why the discipline exists

  - path: concepts/computational-attention.md
    title: Computational Attention

  - path: concepts/attention-budget.md
    title: Attention Budget

  - path: concepts/attention-policy.md
    title: Attention Policy

  - path: principles/search-before-generation.md
    title: Search Before Generation

  - path: principles/evidence-over-confidence.md
    title: Evidence Over Confidence

  - path: principles/model-agnostic-design.md
    title: Model Agnostic Engineering

  - path: principles/continuous-improvement.md
    title: Continuous Improvement

  - path: search/search-strategies.md
    title: Search Strategies

  - path: search/retrieval-architectures.md
    title: Retrieval Architectures

  - path: memory/working-memory.md
    title: Working Memory

  - path: memory/long-term-memory.md
    title: Long-Term Memory

  - path: patterns/verification-loop.md
    title: Verification Loop

  - path: patterns/search-first.md
    title: Search First Workflow

  - path: patterns/iterative-refinement.md
    title: Iterative Refinement

  - path: anti-patterns/prompt-roulette.md
    title: Prompt Roulette

  - path: anti-patterns/unbounded-search.md
    title: Unbounded Search

  - path: telemetry/attention-tracing.md
    title: Attention Tracing

  - path: telemetry/token-accounting.md
    title: Token Accounting

  - path: verification/source-verification.md
    title: Source Verification

  - path: budgeting/token-budgets.md
    title: Token Budgets

  - path: budgeting/compute-budgets.md
    title: Compute Budgets

  - path: orchestration/multi-agent-coordination.md
    title: Multi-Agent Coordination

  - path: experiments/experimental-methodology.md
    title: Experimental Methodology

  - path: metrics/attention-efficiency.md
    title: Attention Efficiency

  - path: glossary/glossary.md
    title: Glossary
