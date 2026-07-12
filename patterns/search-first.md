---
id: search-first
title: Search First
path: patterns/search-first.md
version: "0.1"
status: draft
artifact_type: pattern
type: pattern
stage_tags: [planning, execution, retrieval]
skill_area_tags: [reasoning, information-gathering, decision-making]
risk_level: medium
links:
  relates_to:
    - search/search-strategies.md
    - concepts/attention-budget.md
    - patterns/verification-loop.md
  causes: []
  prevents:
    - hallucination
    - prompt-roulette
    - overconfidence
  related:
    - principles/search-before-generation.md
  principles:
    - evidence-over-confidence
    - diagnose-before-retry
  laws:
    - structure-precedes-computation
  telemetry:
    - attention-tracing
    - retrieval-utilization
---

# Search First

## Rule
Before generating an answer, claim, or plan, first search to update Working Memory with relevant external facts and constraints. Do not reason from parameters alone.

## When to apply
- When the answer depends on facts that change over time
- When the cost of being wrong > cost of one search
- When the system has access to tools, DBs, APIs, or docs
- Exploratory or Eliminative search strategies per `search-strategies.md`

## Problem
LLMs default to "generate from weights". This produces plausible but stale, generic, or wrong answers. 
The cost of a wrong generation + verification is often 10x the cost of one search.

## Solution
Insert a mandatory search step before generation. The search query is formed from Working Memory `Search Priorities`.

### Steps
1.  **Form Query**: From Working Memory, extract top 1-2 unknowns with highest InfoGain
2.  **Execute Search**: Use available tools. Treat result as new evidence E
3.  **Update WM**: `Summary' = Compress(Summary + E)`. `Disproved' += Contradicted(H, E)`
4.  **Re-evaluate Strategy**: Did search produce a hypothesis? Switch to confirmatory. Did it kill candidates? Stay eliminative.
5.  **Generate**: Now generate answer conditioned on updated WM

## Verification (checks)
- Can the system cite which search result changed its answer?
- Was search skipped? If yes, is there a logged justification: "prior confidence > 0.9"?
- Did search reduce uncertainty in Working Memory?
- Is search cost logged vs generation cost?

## Failure signature
- Answer sounds confident but cites no sources
- Same query repeated without using search results
- Search returns evidence that contradicts answer, but answer unchanged
- "I don't have access to current info" used as excuse instead of calling tool

## Agent hooks
- **Planner**: Insert search node before generation node when uncertainty > threshold
- **Executor**: Run search, enforce timeout and token budget
- **Reviewer**: Check that generation actually used search results
- **Budget Manager**: Account search cost against exploration budget

## Example
**Bad**: "What’s the latest treatment for depression?" -> generates from 2024 weights
**Search-First**: Search -> "New meta-analysis 2026-03 says X" -> Update WM -> Answer cites X

**Lore Example**: 
Before asking "is it work or sleep?", Search-First pulls last 7 days of PHQ-9 + sleep logs into WM. 
Now the question is specific: "Your sleep dropped 2hrs and PHQ-9 went up. Which feels worse?"

## Relationship to CAE
**Law 1**: Search creates structure before expensive generation  
**Law 2**: If search fails, diagnose why before retrying generation  
**Law 3**: Search cost is part of attention budget

## Open Questions
- What uncertainty threshold triggers mandatory search?
- How to compress search results to fit WM budget?
- When is cached search result sufficient vs fresh search?

contributed by meta ai at the request of the maintainer
