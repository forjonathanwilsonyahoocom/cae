---
id: forcastable-attention
title: Forecasting AI Agent Costs in Production
path: principals/forcastable-attention.md
version: 0.1
status: draft — proposed
artifact_type: principal
type: principal
stage_tags: ["planning", "verification", "memory", "stopping"]
skill_area_tags: ["evaluation", "grounding", "process design"]
risk_level: medium
links:
  relates_to: ["patterns/attention-observability.md", "patterns/policy-formation.md", "concepts/computational-attention.md"]
  causes: []
  prevents: ["repeated rediscovery", "non-durable retries", "wasted-computation"]
  related:
    principles: ["evidence-over-confidence", "durable-evidence"]
    laws: [ "verification-stability"]
    patterns: ["telemetry-as-evidence"]
    anti-patterns: ["unbounded-computation", "retry-without-constraint"]
    telemetry: ["attention-tracing", "stage-diagnosed-telemetry"]
---


[Rohan Khatavkar et machina
Forecasting AI Agent Costs in Production](https://gist.github.com/rohankhatavkar-source/5e73adb5cdd0ecef2f1f5e44ce0868ab)

## relates to concepts/computational-attention.md in the following ways

 - "Separate fixed-cost from variable-cost workflows" → different attention distributions.
 - "Measure interaction classes" → characterize attention policies rather than average behavior.
 - "Pilot before projecting" → instrument before optimizing.
 - "Cost controls into the architecture" → bounded attention.
 - "The cheapest agent solves the problem in fewer steps" → attention efficiency.

