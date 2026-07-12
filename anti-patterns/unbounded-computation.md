---
id: unbounded-computation
title: Unbounded Computation
path: anti-patterns/unbounded-computation.md
version: "0.1"
status: draft
artifact_type: anti-pattern
type: anti-pattern
stage_tags: [planning, execution, budgeting]
skill_area_tags: [resource-allocation, decision-making, systems-design]
risk_level: high
links:
  relates_to:
    - concepts/attention-budget.md
    - concepts/working-memory.md
    - search/search-strategies.md
  causes:
    - verification-starvation
    - context-loss
  prevents: []
  related:
    - anti-patterns/prompt-roulette.md
  principles:
    - evidence-over-confidence
  laws:
    - constraints-are-computational-inputs
  telemetry:
    - budget-utilization
    - attention-tracing
---

# Unbounded Computation

## Smell
The system behaves as if compute, context, time, or verification are infinite. 
It keeps searching, reasoning, or generating until stopped by an external timeout.

## Statement
Allocating computation without an explicit budget and stopping condition.

## Why it’s bad
1.  **Violates Law 3**: Constraints are not treated as inputs. They are ignored until they cause failure.
2.  **Hides strategy mismatch**: If you never run out of budget, you never have to ask "is this the right search shape?"
3.  **Verification starvation**: 100% of budget goes to action. 0% to checking if it worked.
4.  **Context loss**: Working Memory gets filled with low-value detail because there’s no pressure to compress.
5.  **Undiagnosable**: When it fails, you don’t know if it was wrong reasoning or just ran too long.

## Typical forms
- **The Infinite Loop**: "Let me search more" instead of "let me switch strategies"
- **The Wall of Text**: Generating 2000 tokens to answer a 1-sentence question
- **The Brute Force**: Trying every candidate instead of eliminative search
- **The Retry Spiral**: Same failed call, more tokens, no diagnosis. Cousin of `prompt-roulette.md`

## What it looks like
Attempt fails
↓
Try again with more tokens
↓
Try again with more search results  
↓
Try again with longer reasoning trace
↓
OOM / Timeout / User rage-quits

## CAE Fix
Apply Law 3 explicitly.

1.  **Name the budget before starting**: tokens, time, turns, verification %
2.  **Name the stopping condition**: confidence > 0.8, or no InfoGain in last 2 steps
3.  **Account every spend**: exploration, reasoning, verification, articulation
4.  **When budget low**: switch from exploratory to eliminative to confirmatory. Don’t just "do more"

## Example
**Unbounded**: 
"User is anxious. Let me ask 20 questions to be sure."
Result: User drops off at Q7. No outcome.

**Bounded**: 
"Budget = 5 questions + 1 verification. 
Q1-3: Exploratory to form hypothesis. 
Q4-5: Confirmatory. 
Verification: Follow up in 1 week."
Result: User completes. Outcome measured.

## Detection
- Budget utilization not tracked
- Latency grows linearly with input size
- "Let me think longer" used as default strategy
- No telemetry on tokens spent vs outcome achieved

## Relationship to CAE
**Law 3**: Constraints Are Computational Inputs. This anti-pattern ignores them.  
**Attention Budget**: The cure. Budget is state.  
**Working Memory**: The victim. Gets filled with garbage when unbounded.

Unbounded computation is what happens when you optimize for "sounding smart" instead of "producing outcomes under constraints."

## Keywords
budget, resource-exhaustion, overthinking, infinite-loop, brute-force, token-bloat
---

Why this one is so important

This is the default mode of every LLM right now.  
"More context. More reasoning. More search. More tokens."

Law 3 exists specifically to kill this. 

