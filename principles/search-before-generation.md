---
id: search-before-generation
title: Search Before Generation
path: principles/search-before-generation.md
version: "0.1"
status: draft
artifact_type: principle
type: principle
stage_tags: [planning, execution]
skill_area_tags: [reasoning, epistemology, systems-design]
risk_level: high
links:
  relates_to:
    - patterns/search-first.md
    - search/search-strategies.md
    - principles/evidence-over-confidence.md
  causes: []
  prevents:
    - hallucination
    - overconfidence
    - prompt-roulette
  related: []
  principles:
    - evidence-over-confidence
  laws:
    - structure-precedes-computation
    - constraints-are-computational-inputs
  telemetry:
    - attention-tracing
---

# Search Before Generation

## Statement
Do not generate a claim, plan, or answer until you have first attempted to ground it in evidence. Generation without grounding is speculation.

## Rationale
Parameters are a lossy, time-frozen summary of the world. 
The world changes. The user context changes. The problem changes.

Generating first and searching later creates 3 costs:
1.  **Correction cost**: You have to retract and regenerate
2.  **Trust cost**: User learns not to believe you
3.  **Verification cost**: You now need to verify something you made up

Searching first is cheaper.

## Implications
- **Default to tools**: If a tool exists, use it before answering
- **Uncertainty is a signal**: "I don't know" should trigger search, not hedging language
- **Citations are required**: Any factual claim should be traceable to a search result
- **Generation is compression**: The job of generation is to compress evidence, not invent it

## Counterexamples
When search-before-generation is wrong:
- Pure reasoning tasks: math, logic, coding from first principles
- Creative tasks: brainstorming, fiction, where novelty > truth
- When search cost >> error cost and prior confidence is very high

In these cases, explicitly log: "Skipped search: creative mode, confidence 0.95"

## Relationship to Other CAE Concepts
**Search Strategies**: Search-before-generation tells you *to* search. `search-strategies.md` tells you *what shape* the search should be.  
**Search-First Pattern**: This principle is the "why". `search-first.md` is the "how".  
**Working Memory**: Search results become evidence E in the update rule.  
**Law 3**: Search cost is a budget input. This principle forces you to account for it.

## Anti-pattern: Generate Then Verify
