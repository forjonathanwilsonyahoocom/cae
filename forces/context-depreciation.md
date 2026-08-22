---
title: context-depreciation
category: Cognitive Forces
status: Draft - proposed by ornith:9b & Maintainer

keywords:
  - context window
  - working memory
  - signal-to-noise ratio
  - agent state
  - conversation history

related:
  - attention-fragmentation
  - model-volatility
  - cognitive-drift

---

# context-depreciation

## Intent

Context degrades as it accumulates — not because of forgetting, but because the ratio of useful signal to total tokens declines. An agent's effective working memory is bounded by what it can currently process, and that window fills with noise faster than it fills with signal.

## Purpose

To make explicit that context is not a free resource. Every token added — conversation history, tool outputs, intermediate states — competes with the tokens needed for the current reasoning task. This force exists to prevent the assumption that "more context = better reasoning."

## Scope

Intentionally included:
- The mechanical reality that context windows have finite capacity.
- The observation that accumulated tokens are not uniformly valuable.
- The distinction between *state* (which should be compressed) and *history* (which often should be dropped).

Intentionally excluded:
- Model architecture differences (this force applies across models).
- Long-term memory mechanisms (RAG, persistent state) — those are mitigations, not part of the force itself.
- Human memory analogies — keep the focus on agent behavior.

## Background

In single-agent development, a human developer can hold the entire design in their working memory and reference earlier parts of a conversation without degradation. Agents lack this capacity: their effective memory is the context window at the moment of inference.

As a conversation grows, the probability that any given token in the context is relevant to the current task decreases. This isn't a soft concern — it's a hard constraint of the inference model.

## Principles

1. **Context is perishable.** Earlier context loses value over time, not because it becomes false, but because it becomes irrelevant to the current task.
2. **Signal degrades linearly, noise accumulates.** Useful information stays useful; everything else just takes up space.
3. **Compression is a feature, not a bug.** Summarizing, pruning, and replacing early context with distilled state is an engineering practice, not a workaround.
4. **The agent should know what it can and cannot reason over.** An agent that assumes full access to all prior context will overestimate its own capabilities.

## Guidance

- **Prune early context.** Replace long-running conversation history with summaries or checkpoints.
- **Compress state.** When an agent completes a subtask, encode its output into a compact representation rather than retaining the full derivation.
- **Track relevance.** Explicitly tag which parts of context are still active vs. archived.
- **Design for bounded context.** Assume the agent can only work with the current window — structure work so that each step is self-contained.
- **Don't accumulate for the sake of it.** More history is not more intelligence.

## Examples

A coding agent that retains the full 50,000-token conversation while working on a 200-token task has 250x the noise. The equivalent human developer reads the 200-token task and refers back to a summary of earlier decisions.

## Related Artifacts

- attention-fragmentation
- cognitive-drift
- model-volatility

## Open Questions

- At what point does context-depreciation become a failure mode vs. a manageable constraint?
- Can agents develop "context hygiene" habits that outperform manual pruning?
- Is there a measurable relationship between context age and task accuracy?

## Future Research

- Empirical measurement of context utilization over conversation length.
- Automated context pruning strategies that learn from task completion patterns.
- Comparison of different compression techniques (summarization, state encoding, semantic hashing) on agent task performance.

## References

- Attention is All You Need
- Transformer architectures and context window limitations
- Working memory models in cognitive science

## Revision History

Initial scaffold.

**context-depreciation.md** — context has a half-life. The more you accumulate (logs, state, conversation history), the more the signal-to-noise ratio drops. In agent-driven dev, this is acute: an agent's working memory 
is effectively the context it's currently processing, and that context degrades as the conversation grows. Unlike human memory, which can be refreshed with a summary, agents can't "remember" what they said earlier unless that's explicitly in context. So context-depreciation is a hard, mechanical constraint — not a soft one.


