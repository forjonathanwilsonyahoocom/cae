Star (Hub & Spoke): A central orchestrator handles all routing; minimizes agent-to-agent chatter but creates a single point of congestion and failure.


Anti-Pattern: Orchestrator Bloat (The Degraded Form of Star Topology)
    • Architectural Definition: Occurs when a central hub agent absorbs too much state-tracking, intent-parsing, and routing logic. The central hub ceases to be a lean traffic controller and transforms into a massive monolithic prompt containing all global instructions.
    • Underlying Forces:
        1. Cognitive Drift: As the central prompt grows to handle every possible edge case for its workers, its compliance with underlying routing rules rapidly degrades.
        2. Attention Saturation: The model backend's internal attention mechanisms fail to prioritize small, critical routing hooks buried under piles of system metadata.
    • The "No-Planning" Symptom: Instead of splitting a complex task into localized sub-topologies, developers simply append new instructions to the main orchestrator's system prompt whenever a worker fails.
    • System Breakdown State: The orchestrator misroutes messages, ignores exit criteria, experiences extreme latency, and burns massive budgets by processing the entire corporate prompt infrastructure for a simple two-word message handoff.

