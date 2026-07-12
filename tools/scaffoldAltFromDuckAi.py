#!/usr/bin/env python3
"""
scaffold.py

Scaffolds CAE markdown docs from a machine-seekable "policy card" template.
- Creates missing docs
- Adds stable frontmatter fields (id, type, artifact_type, links)
- Inserts standardized headings so retrieval can depend on structure

Usage:
  python tools/scaffold.py --root . --dry-run
  python tools/scaffold.py --root . --write
"""

from __future__ import annotations

import argparse
import os
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional

# ----------------------------
# Templates (policy-card style)
# ----------------------------

POLICY_CARD_TEMPLATE = """---
id: {id}
title: {title}
path: {path}
version: {version}
status: {status}
artifact_type: {artifact_type}
type: {type}
stage_tags: [{stage_tags}]
skill_area_tags: [{skill_area_tags}]
risk_level: {risk_level}
links:
  relates_to: [{relates_to}]
  causes: [{causes}]
  prevents: [{prevents}]
  related:
    principles: [{principles}]
    laws: [{laws}]
    patterns: [{patterns}]
    anti-patterns: [{anti_patterns}]
    telemetry: [{telemetry}]
---

# {title}

## Rule
{rule}

## When to apply
{when_to_apply}

## Failure signature
{failure_signature}

## Corrective action (steps)
{corrective_action_steps}

## Verification (checks)
{verification_checks}

## Agent hooks
{agent_hooks}

## Definitions (condensed)
{definitions_condensed}

{optional_narrative}
"""

# For concise “cards” we still keep your richer narrative by appending it.
# You can override/extend this later per-doc.
DEFAULT_NARRATIVE_STUB = """## Position within Computational Attention Engineering
[Fill in the positive/negative relationship to existing docs.]

## Summary
[1–3 sentence summary.]

## Examples
### Example 1
[Short example.]

### Example 2
[Short example.]

## Keywords
[comma-separated keywords]

## Open Questions
- [question]
- [question]

## Research Directions
- [direction]

## Revision History
- v{version} — initial draft — {author_note}
"""


# ----------------------------
# Spec for which files to scaffold
# ----------------------------

@dataclass(frozen=True)
class DocSpec:
    rel_path: str                 # e.g., "anti-patterns/prompt-roulette.md"
    artifact_type: str           # e.g., "antipattern"
    type: str                     # e.g., "anti-pattern"
    id: str                       # e.g., "prompt-roulette"
    title: str
    rule: str
    when_to_apply: str
    failure_signature: str
    corrective_action_steps: str
    verification_checks: str
    agent_hooks: str
    definitions_condensed: str
    optional_narrative: str
    status: str = "draft — proposed"
    version: str = "0.1"
    risk_level: str = "medium"
    stage_tags: Optional[List[str]] = None
    skill_area_tags: Optional[List[str]] = None
    relates_to: Optional[List[str]] = None
    causes: Optional[List[str]] = None
    prevents: Optional[List[str]] = None
    principles: Optional[List[str]] = None
    laws: Optional[List[str]] = None
    patterns: Optional[List[str]] = None
    anti_patterns: Optional[List[str]] = None
    telemetry: Optional[List[str]] = None


DEFAULT_DOCS: List[DocSpec] = [
    # Concepts / core
    DocSpec(
        rel_path="concepts/computational-attention.md",
        artifact_type="concept",
        type="concept",
        id="computational-attention",
        title="Computational Attention",
        rule="(Define what CAE means operationally: attention, missions, policies, execution, telemetry.)",
        when_to_apply="- Whenever you formalize agent delegation as attention allocation.\n- Whenever you design an agent workflow that needs measurable feedback loops.",
        failure_signature="- Outputs are produced but the loop (mission → policy → execution → telemetry) is implicit.\n- Retries happen without stage diagnosis.\n- Budgets are unclear, so verification varies arbitrarily.",
        corrective_action_steps="- Define the loop stages explicitly.\n- Specify what “telemetry” means for your system.\n- Connect budgets to verification and search choices.\n- Add stop conditions and falsifiable hypotheses to each delegated step.",
        verification_checks="- Can a reader point to mission, policy, execution, telemetry sections?\n- Can an agent generate a stage-diagnosis artifact from telemetry?\n- Does budgeting determine which verification steps are run?",
        agent_hooks="- Planner: emit mission/policy objects and stage labels.\n- Executor: produce telemetry aligned to the policy.\n- Verifier: run stage diagnosis and decide whether to stop or adapt.",
        definitions_condensed="- Computational Attention: treating attention as an engineered resource allocated across mission, policy, execution, and telemetry.",
        optional_narrative=DEFAULT_NARRATIVE_STUB.format(
            version="0.1", author_note="repo maintainer"
        ),
        version="0.1",
        status="draft — scaffolded",
        risk_level="low",
        stage_tags=["planning", "tool_use", "verification", "stopping", "memory"],
        skill_area_tags=["reasoning", "grounding", "evaluation"],
        relates_to=["(link to principles folder root if you have one)"],
        causes=[],
        prevents=[],
        principles=[],
        laws=[],
        patterns=[],
        anti_patterns=[],
        telemetry=[],
    ),

    # Budgeting
    DocSpec(
        rel_path="budgeting/token-budgets.md",
        artifact_type="principle",
        type="law",
        id="token-budgets",
        title="Token Budgets",
        rule="Allocate token/compute budget by category (absorption, reasoning, verification, articulation) and prevent “starved reasoning, protected articulation.”",
        when_to_apply="- When an agent has limited context or compute.\n- When you want predictable failure modes and reliable verification behavior.",
        failure_signature="- Confident but shallow reasoning.\n- Verification steps are skipped or degraded.\n- Outputs become more verbose while evidence/validation does not improve.",
        corrective_action_steps="- Classify budget usage into categories.\n- Protect reasoning + verification minimums.\n- Reduce articulation when it would consume the protected budget.\n- Explicitly state what gets shortened and what stays invariant (e.g., verification checks).",
        verification_checks="- The doc/workflow reports budget category allocations.\n- Verification steps run (or are explicitly traded off) consistently.\n- Shortening preserves decision-relevant evidence.",
        agent_hooks="- Planner: tag planned tokens by category.\n- Executor: enforce minimum reasoning/verification passes.\n- Verifier: log which categories were cut and whether that changed correctness.",
        definitions_condensed="- Token budget categories: what the budget buys (absorption vs reasoning vs verification vs articulation).",
        optional_narrative=DEFAULT_NARRATIVE_STUB.format(
            version="0.1", author_note="repo maintainer"
        ),
        version="0.1",
        status="draft — scaffolded",
        risk_level="medium",
        stage_tags=["budgeting", "planning", "verification"],
        skill_area_tags=["reasoning", "evaluation", "grounding"],
        relates_to=["(link to principles/evidence-over-confidence if relevant)"],
        causes=[],
        prevents=[],
        principles=[],
        laws=[],
        patterns=[],
        anti_patterns=[],
        telemetry=[],
    ),

    # Example antipattern card (you can add more)
    DocSpec(
        rel_path="anti-patterns/prompt-roulette.md",
        artifact_type="antipattern",
        type="anti-pattern",
        id="prompt-roulette",
        title="Prompt Roulette",
        rule="Before retrying a delegated task, diagnose which stage (mission → policy → execution → telemetry) failed; don’t perturb the prompt (adjective inflation / rewording / re-roll) as a substitute.",
        when_to_apply="- Delegated task returns wrong or fails.\n- Retries differ only by wording/verbosity/adjectives.\n- Feedback is “try again” without falsifiable change to mission/policy/evidence.",
        failure_signature="- Repeated failures with near-identical prompts.\n- “More careful/thorough” messages with no policy/stop/budget change.\n- Diagnosis is missing from telemetry or delegator notes.",
        corrective_action_steps="- Identify which stage failed (mission vs policy vs execution-variance vs review intent).\n- Apply a falsifiable change to the failed stage only.\n- Allow variance retry only when prior telemetry indicates design/policy likely correct.",
        verification_checks="- Next retry reflects the hypothesized stage change.\n- Telemetry indicates stage diagnosis and whether change helped.\n- No further retries occur without a stated falsifiable reason.",
        agent_hooks="- Planner: require stage diagnosis + falsifiable change.\n- Pre-execution gate: reject undiagnosed retries.\n- Post-run: record diagnosis + outcome for future budgets/policies.",
        definitions_condensed="- Undiagnosed retry, adjective inflation, verbatim re-roll, diagnosis-free feedback.",
        optional_narrative=DEFAULT_NARRATIVE_STUB.format(
            version="0.1", author_note="repo maintainer"
        ),
        version="0.2",
        status="draft — scaffolded",
        risk_level="high",
        stage_tags=["execution", "verification", "stopping"],
        skill_area_tags=["reasoning", "evaluation"],
        relates_to=["principles/legible-delegation.md"],
        causes=[],
        prevents=[],
        principles=["evidence-over-confidence"],
        laws=[],
        patterns=[],
        anti_patterns=[],
        telemetry=["attention-tracing"],
    ),
]


# ----------------------------
# Implementation
# ----------------------------

def slug_to_id(path: str) -> str:
    # anti-patterns/prompt-roulette.md -> prompt-roulette
    p = path.replace("\\", "/")
    stem = Path(p).stem
    return stem


def ensure_dir(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def fmt_list(xs: List[str]) -> str:
    return ", ".join([f"{x}" for x in xs]) if xs else ""


def to_bracket_list(xs: Optional[List[str]]) -> str:
    xs = xs or []
    # already expects "plain tokens" like principles/legible-delegation
    # Keep them as strings in YAML list.
    return ", ".join([f"\"{x}\"" for x in xs])


def make_card(spec: DocSpec, root: str, author_note: str = "repo maintainer") -> str:
    path = spec.rel_path.replace("\\", "/")
    stage_tags = spec.stage_tags or []
    skill_tags = spec.skill_area_tags or []
    relates_to = spec.relates_to or []
    causes = spec.causes or []
    prevents = spec.prevents or []
    principles = spec.principles or []
    laws = spec.laws or []
    patterns = spec.patterns or []
    anti_patterns = spec.anti_patterns or []
    telemetry = spec.telemetry or []

    optional_narrative = spec.optional_narrative
    # If the stub still contains placeholder author_note, it’s already filled.
    # Otherwise, we leave as-is.

    return POLICY_CARD_TEMPLATE.format(
        id=spec.id or slug_to_id(path),
        title=spec.title,
        path=path,
        version=spec.version,
        status=spec.status,
        artifact_type=spec.artifact_type,
        type=spec.type,
        stage_tags=to_bracket_list(stage_tags),
        skill_area_tags=to_bracket_list(skill_tags),
        risk_level=spec.risk_level,
        relates_to=to_bracket_list(relates_to),
        causes=to_bracket_list(causes),
        prevents=to_bracket_list(prevents),
        principles=to_bracket_list(principles),
        laws=to_bracket_list(laws),
        patterns=to_bracket_list(patterns),
        anti_patterns=to_bracket_list(anti_patterns),
        telemetry=to_bracket_list(telemetry),
        rule=spec.rule,
        when_to_apply=spec.when_to_apply,
        failure_signature=spec.failure_signature,
        corrective_action_steps=spec.corrective_action_steps,
        verification_checks=spec.verification_checks,
        agent_hooks=spec.agent_hooks,
        definitions_condensed=spec.definitions_condensed,
        optional_narrative=optional_narrative.format(
            version=spec.version, author_note=author_note
        )
        if "{author_note}" in optional_narrative
        else optional_narrative,
    )


def scaffold(root: str, write: bool) -> None:
    root_path = Path(root).resolve()

    for spec in DEFAULT_DOCS:
        target = root_path / spec.rel_path
        if target.exists():
            print(f"SKIP (exists): {spec.rel_path}")
            continue

        ensure_dir(target)
        content = make_card(spec=spec, root=root)

        if write:
            target.write_text(content, encoding="utf-8")
            print(f"CREATE: {spec.rel_path}")
        else:
            print(f"DRY RUN: would create {spec.rel_path}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".", help="Repo root (default: current dir)")
    ap.add_argument("--write", action="store_true", help="Actually write files (default is dry-run)")
    args = ap.parse_args()

    scaffold(root=args.root, write=args.write)


if __name__ == "__main__":
    main()
