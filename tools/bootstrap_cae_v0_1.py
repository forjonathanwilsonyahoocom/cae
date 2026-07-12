from pathlib import Path

ROOT = Path("computational-attention-engineering")
APP = ROOT  # shorthand

# Change this if your repo folder is different / already exists.
# The script will create files if missing and overwrite only if empty.
# (If you want overwrite-everything, set OVERWRITE_EMPTY_ONLY = False.)
OVERWRITE_EMPTY_ONLY = True

def ensure_file(path: Path, content: str):
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() and OVERWRITE_EMPTY_ONLY:
        existing = path.read_text(encoding="utf-8").strip()
        if existing:
            return
    path.write_text(content, encoding="utf-8")

def fence(text: str) -> str:
    return text.strip() + "\n"

COMMON_VOICE = """<!--
CAUTION: This repository is an academic-practitioner artifact, not a vendor guide.
Voice: optimistic but skeptical; vendor-neutral; evidence-oriented; future-proof.
-->

"""

# Repository tree to “touch each file” in this initial bootstrap.
# If your repo already has different structure, paste your repo tree and I’ll adapt the script.
FILES = {
    "README.md": None,
    "docs/00-terminology.md": None,
    "docs/01-principles.md": None,
    "docs/02-control-loop.md": None,
    "docs/03-staged-discovery.md": None,
    "docs/04-verification-and-consequence.md": None,
    "docs/05-budgeting-telemetry.md": None,
    "docs/06-memory-compression.md": None,
    "docs/07-anti-patterns.md": None,
    "concepts/Context-Capsule-v0.1.md": None,
    "artifacts/01-policy-card-template.md": None,
    "artifacts/02-attention-budget-spec.md": None,
    "artifacts/03-telemetry-schema.md": None,
    "artifacts/04-evaluation-rubric.md": None,
    "artifacts/05-investigation-playbook.md": None,
    "open-questions/00-index.md": None,
    ".github/ISSUE_TEMPLATE/cae-proposal.md": None,
    ".github/ISSUE_TEMPLATE/cae-update.md": None,
    ".github/pull_request_template.md": None,
    "CONTRIBUTING.md": None,
    "LICENSE.md": None,
}

README = f"""{COMMON_VOICE}# Computational Attention Engineering (CAE) — v0.1 (Initial Public Draft)

## Purpose
CAE is a proposed engineering discipline: **the design of how autonomous systems allocate finite computational attention under uncertainty**.

This repository is not a software project. It is a durable set of engineering artifacts intended to remain useful even if today’s frontier AI models disappear.

## Why “attention engineering” (and not prompt engineering)?
CAE is not about optimizing prompt wording. It is about **repeatable, model-agnostic policies** and **measurement** for:
- search and exploration,
- memory and compression,
- verification and falsification,
- budgeting,
- telemetry,
- and continuous improvement.

## Working definition
**Computational Attention Engineering is the discipline of designing how autonomous systems allocate finite computational attention under uncertainty.**

## Control loop (high level)
**Mission → Policy → Execution → Telemetry → Policy Adaptation**

## How this repository will evolve
We will draft one artifact at a time as publication-quality Markdown, with:
- purpose,
- why it belongs in the discipline,
- cross-references to principles,
- open questions / future work,
- and explicit TODOs for future contributors.

## Context Capsule (first artifact)
Start here: `concepts/Context-Capsule-v0.1.md`

"""

TERMINOLOGY = f"""{COMMON_VOICE}# Terminology (v0.1)

## Why this file exists
Without shared definitions, “attention” becomes a slogan. This file standardizes terms so future artifacts interoperate across teams and model families.

## Core terms
- **Computational attention:** the finite capacity an autonomous system uses to pursue information under uncertainty (e.g., search depth, reasoning budget, tool calls, retries, exploration width).
- **Mission:** the objective or decision the system is trying to serve.
- **Policy:** the constrained strategy for allocating attention across stages and actions.
- **Execution:** the concrete operational steps taken under the policy.
- **Verification:** evidence gathering or checks intended to reduce the probability of being wrong.
- **Budget:** an explicit constraint on attention expenditure, paired with a priority ordering.
- **Telemetry:** measurement produced during execution that supports analysis and policy improvement.
- **Memory compression:** transforming intermediate working memory into durable artifacts (facts, hypotheses, and open questions).

## TODO
- Add precise, testable definitions for “attention unit” (tokens vs wall-clock vs FLOPs vs tool calls), while staying vendor-neutral.
- Define “uncertainty” operationally for different system types.
"""

PRINCIPLES = f"""{COMMON_VOICE}# Primary Design Principles (v0.1)

## Why this file belongs
Principles are the stable backbone that artifacts should reference. Implementations should be removable; principles should not.

## Working principles
1. **Separate Mission from Policy**
   - Mission states *why*; policy states *how attention is spent*.
2. **Use priors to reduce unnecessary search**
   - Encode baseline expectations so the system does not explore everything equally.
3. **Use anti-hypotheses to avoid expensive rabbit holes**
   - Actively maintain what would disconfirm a candidate direction.
4. **Budget attention as resource allocation**
   - Token/compute budgets are not cost estimates only; they are control variables.
5. **Use staged discovery**
   - Organize investigations into stages with explicit entry/exit criteria.
6. **Allocate verification by consequence**
   - Spend more verification effort when being wrong is costly.
7. **Compress memory periodically**
   - Retain durable facts, surviving hypotheses, and open questions.
8. **Instrument with telemetry**
   - Measure effort, outcomes, and failure modes to enable continuous improvement.

## Cross-references
- Context Capsule v0.1: `concepts/Context-Capsule-v0.1.md`
- Control loop: `docs/02-control-loop.md`
- Budgeting/telemetry: `docs/05-budgeting-telemetry.md`

## TODO
- Add “principle failure modes” (how each principle can be violated and what to log).
"""

CONTROL_LOOP = f"""{COMMON_VOICE}# CAE Control Loop (v0.1)

## Purpose
This file defines the minimal loop structure CAE expects from autonomous systems.

## Loop
**Mission → Policy → Execution → Telemetry → Policy Adaptation**

### Mission
- Inputs: task, constraints, consequence profile.
- Outputs: a bounded goal statement and success criteria.

### Policy
- Inputs: mission, priors, budgets, risk profile.
- Outputs: a staged plan specifying attention allocations and stop rules.

### Execution
- Operate tools/search/memory updates according to the policy.

### Telemetry
- Capture: effort spent, decisions made, verification results, and where uncertainty remained.

### Policy adaptation
- Update policy parameters based on observed outcomes and measured waste.

## TODO
- Define what “policy adaptation” means in practice (parameter update, rule revision, or new stage thresholds) without tying to a specific vendor.
"""

STAGED_DISCOVERY = f"""{COMMON_VOICE}# Staged Discovery (v0.1)

## Purpose
CAE needs a repeatable structure for turning open-ended tasks into bounded attention expenditures.

## Pattern: Stage-gated investigation
A staged discovery plan is a sequence of stages with:
- **Entry criteria** (what must be true to start this stage),
- **Exit criteria** (what must be learned/verified to stop),
- **Attention allocation** (budgeted effort for the stage),
- **Anti-hypothesis hooks** (what would disconfirm progress).

## Example stages (template)
1. **Scoping**
2. **Hypothesis generation**
3. **Targeted exploration**
4. **Verification / falsification**
5. **Synthesis**
6. **Memory compression**

## Cross-reference
- Principles #5, #6, #7, #8: `docs/01-principles.md`

## TODO
- Provide canonical stage interfaces so agents can swap implementations.
"""

VERIFICATION = f"""{COMMON_VOICE}# Verification and Consequence (v0.1)

## Purpose
Verification is where energy is often wasted or misspent. CAE treats verification as an engineered, risk-aware allocation.

## Consequence-weighted verification
- Define a consequence profile for being wrong (low/medium/high or numeric).
- Allocate verification effort proportionally to consequence and residual uncertainty.

## Verification should reduce uncertainty with evidence
Verification is not “more text.” It is:
- checkable claims,
- falsifiable tests,
- and evidence-backed confidence calibration.

## TODO
- Add a “verification decision rule” artifact (thresholds, stop rules, and logging requirements).
"""

BUDGETS_TELEMETRY = f"""{COMMON_VOICE}# Budgeting and Telemetry (v0.1)

## Purpose
This file distinguishes CAE budgets from informal “limits,” and telemetry from vague logging.

## Attention budgets (conceptual)
Budget at least these categories:
- **Search/Exploration budget**
- **Reasoning/Interpretation budget**
- **Verification budget**
- **Synthesis/Articulation budget**
- **Tool-use budget** (if applicable)

## Telemetry (minimum viable schema)
Telemetry should support:
- effort measurement,
- outcome measurement,
- and identification of policy failure modes.

Minimum fields (conceptual):
- mission_id
- stage_id
- effort_observed (unit-agnostic)
- verification_pass/fail (or graded)
- uncertainty_remaining (proxy)
- retry_count / search_depth (where applicable)
- final outcome vs success criteria

## TODO
- Provide an “attention unit” mapping guide that remains vendor-neutral.
- Define which telemetry are mandatory vs optional.
"""

MEMORY = f"""{COMMON_VOICE}# Memory Compression (v0.1)

## Purpose
Without compression, attention becomes unbounded and repeat work grows. With naive compression, correctness can degrade.

## Pattern: Compress into durable artifacts
Periodically compress working memory into:
- **Durable facts** (claims with evidence links/IDs),
- **Surviving hypotheses** (what remains plausible and why),
- **Open questions** (what is unknown and how it will be tested).

## Cross-reference
- Principles #7 and #8: `docs/01-principles.md`

## TODO
- Define quality criteria for compression (what must not be dropped).
"""

ANTI_PATTERNS = f"""{COMMON_VOICE}# Anti-patterns (v0.1)

## Purpose
Anti-patterns are reusable warnings—faster than reinventing failure analysis.

## Common CAE anti-patterns
1. **Retry inflation**
   - Repeating the same strategy without stage diagnosis or new evidence.
2. **Flat exploration**
   - Treating the task as a single-stage prompt; no exit criteria.
3. **Verification theater**
   - Generating additional narrative instead of checkable evidence.
4. **Budget amnesia**
   - Budgets exist but are not enforced in the control loop (or telemetry doesn’t measure them).
5. **Memory bloat**
   - Carrying transient context indefinitely instead of compressing.

## TODO
- Add “detection signals” for each anti-pattern (what telemetry flags it).
"""

CONTEXT_CAPSULE = f"""{COMMON_VOICE}# Context Capsule: Computational Attention Engineering (v0.1)

## Core thesis
As AI systems become more capable, the scarce resource shifts from intelligence to disciplined computational attention.

The engineering problem is no longer **“How do I give the model more context?”**

It becomes:

> **“How do I allocate finite reasoning effort where it creates the most value?”**

## Working definition
Computational Attention Engineering is the discipline of designing how autonomous systems allocate finite computational attention under uncertainty.

## Mission statement
CAE exists to produce durable, model-agnostic engineering artifacts that:
- make attention measurable and budgetable,
- enforce stage structure and stop rules,
- prioritize verification based on consequence,
- compress memory into durable decision assets,
- and enable continuous improvement via telemetry.

## Primary design principles (summary)
- Separate Mission from Policy.
- Use priors to reduce unnecessary search.
- Use anti-hypotheses to avoid expensive rabbit holes.
- Budget attention as a control policy.
- Organize investigations into staged discovery.
- Allocate verification effort based on consequence of being wrong.
- Periodically compress working memory into durable facts/hypotheses/questions.
- Instrument with telemetry so strategies can be measured and improved.

## Control loop
Mission → Policy → Execution → Telemetry → Policy Adaptation

## Design philosophy
Don’t maximize computation.
Maximize uncertainty reduced per unit of computation.

The goal is not smarter agents.
The goal is making their attention measurable, spendable, and continuously improvable.

## Cross-references
- Principles: `docs/01-principles.md`
- Control loop: `docs/02-control-loop.md`

## TODO
- Rename “attention” units operationally (vendor-neutral mapping).
- Define a minimal “capsule interface” other agents can follow to execute CAE policy cards.
"""

POLICY_CARD = f"""{COMMON_VOICE}# Policy Card Template (v0.1)

## Purpose
This artifact is the lingua franca between teams and agents. It externalizes attention policy as a checkable specification.

## Why it belongs
Policies need to be portable, reviewable, and measurable. A template enforces consistent structure.

## Template fields
1. **Mission**
   - Objective and success criteria.
2. **Priors**
   - Baseline assumptions used to reduce search.
3. **Budgets**
   - Attention allocations by category.
4. **Stages**
   - Stage list with entry/exit criteria.
5. **Anti-hypotheses**
   - What evidence would disconfirm the current direction.
6. **Verification rule**
   - Consequence-weighted verification plan.
7. **Stop rules**
   - When to stop, downgrade, or escalate.
8. **Telemetry plan**
   - What to log to support policy adaptation.
9. **Memory compression output**
   - What durable artifacts the run must emit.

## Cross-references
- Principles: `docs/01-principles.md`
- Budgets/telemetry: `docs/05-budgeting-telemetry.md`

## TODO
- Add a formal “policy validation checklist” other agents can run.
"""

ATTENTION_BUDGET_SPEC = f"""{COMMON_VOICE}# Attention Budget Specification (v0.1)

## Purpose
CAE budgets must be explicit and enforceable. This artifact defines a vendor-neutral budget spec.

## Budget model (conceptual)
A budget is:
- a **cap** (maximum resource),
- a **priority ordering** (what must not be sacrificed),
- and a **spend policy** (how to decide where to allocate).

## Attention categories
At minimum:
- search/exploration
- reasoning/interpretation
- verification
- synthesis/articulation
- tool use (optional)

## TODO
- Define normalized budget units and mapping strategy (tokens vs time vs tool calls).
- Define how budgets degrade gracefully when uncertain.
"""

TELEMETRY_SCHEMA = f"""{COMMON_VOICE}# Telemetry Schema (v0.1)

## Purpose
Telemetry is the substrate for continuous improvement.

## Requirements
Telemetry must answer:
- How much attention was spent?
- What decisions were made?
- Did verification succeed?
- Where did time go (stage-level)?
- What policy adaptation should follow?

## Minimal schema (conceptual)
- run_id
- mission_id
- stage_id
- effort_observed (unit-agnostic field)
- decision_trace (high-level actions, not raw prompts)
- verification_result
- uncertainty_proxy
- outcome_metric (success/failure and/or score)
- failure_mode_tags

## TODO
- Add examples using multiple “effort unit” choices to stay vendor-neutral.
"""

EVAL_RUBRIC = f"""{COMMON_VOICE}# Evaluation Rubric (v0.1)

## Purpose
Evaluation prevents CAE from becoming an aesthetic.

## Rubric dimensions (suggested)
1. **Decision quality**
2. **Verification integrity**
3. **Efficiency**
4. **Budget adherence**
5. **Stage discipline**
6. **Memory compression quality**
7. **Telemetry completeness**

## TODO
- Define concrete metrics or at least measurement proxies.
- Add a template for reporting outcomes that avoids model-specific bias.
"""

PLAYBOOK = f"""{COMMON_VOICE}# Investigation Playbook (v0.1)

## Purpose
This playbook is a reusable procedure for executing CAE policies.

## Procedure (high level)
1. Clarify mission and success criteria.
2. Select priors and construct anti-hypotheses.
3. Allocate budgets and stage plan.
4. Execute stage-by-stage with stop rules.
5. Perform consequence-weighted verification.
6. Compress memory into durable outputs.
7. Emit telemetry and propose policy adaptation.

## Cross-reference
- Control loop: `docs/02-control-loop.md`
- Verification: `docs/04-verification-and-consequence.md`

## TODO
- Provide a stage-gated example run report using the telemetry schema.
"""

OPEN_Q = f"""{COMMON_VOICE}# Open Questions Index (v0.1)

## Purpose
Document what we do not know yet. This prevents premature standardization.

## Candidate open questions
- How should we define “attention units” without losing comparability?
- What is the minimal telemetry that still predicts policy improvements?
- How do we standardize consequence profiles across domains?
- What memory compression formats are universally interoperable?

## TODO
- Convert open questions into labeled issues with explicit resolution criteria.
"""

ISSUE_PROPOSAL = f"""{COMMON_VOICE}name: CAE Proposal
description: Propose a new CAE artifact or principle update.
title: "CAE Proposal: <short name>"
labels: ["cae", "proposal"]

body:
  - type: textarea
    id: purpose
    attributes:
      label: Purpose
      description: What artifact/principle is proposed and why it belongs.
    validations:
      required: true
  - type: textarea
    id: evidence_or_rationale
    attributes:
      label: Rationale (evidence-oriented)
      description: What failures or results motivated this proposal?
    validations:
      required: true
  - type: textarea
    id: spec_outline
    attributes:
      label: Specification sketch
      description: Bullet sketch or section outline.
    validations:
      required: true
  - type: textarea
    id: crossrefs
    attributes:
      label: Cross-references
      description: Which principles/docs does this relate to?
    validations:
      required: false
  - type: textarea
    id: open_questions
    attributes:
      label: Open questions / future work
    validations:
      required: false
"""

ISSUE_UPDATE = f"""{COMMON_VOICE}name: CAE Update
description: Update an existing artifact with measured improvements.
title: "CAE Update: <short name>"
labels: ["cae", "update"]

body:
  - type: textarea
    id: file_changed
    attributes:
      label: What changed (files)
      description: List paths and summary.
    validations:
      required: true
  - type: textarea
    id: measured_improvement
    attributes:
      label: Measured improvement
      description: What telemetry or evaluation rubric results improved?
    validations:
      required: true
  - type: textarea
    id: tradeoffs
    attributes:
      label: Tradeoffs
      description: What got worse or riskier?
    validations:
      required: false
"""

PR_TEMPLATE = f"""{COMMON_VOICE}## Summary
<!-- What artifact changed and why. -->

## Cross-references
<!-- Principles / docs referenced. -->

## Evidence / evaluation
<!-- Telemetry or rubric outcomes. -->

## Tradeoffs and open questions
<!-- What remains uncertain. -->
"""

CONTRIB = f"""{COMMON_VOICE}# Contributing

## Goal
Improve CAE artifacts via proposals that are:
- publication-quality Markdown,
- vendor-neutral,
- evidence-oriented,
- academically grounded practitioner voice,
- and optimistic but skeptical.

## Expected workflow
1. Propose (issue) an artifact/principle update.
2. Draft the Markdown spec.
3. Include cross-references and open questions.
4. Update after measured evaluation where possible.
"""

LICENSE = f"""{COMMON_VOICE}# License

TODO: Choose an OSI-approved license (e.g., MIT, Apache-2.0, BSD-3-Clause).
"""

def main():
    mapping = {}
    for rel_path in FILES:
        if rel_path == "README.md":
            mapping[rel_path] = README
        elif rel_path == "docs/00-terminology.md":
            mapping[rel_path] = TERMINOLOGY
        elif rel_path == "docs/01-principles.md":
            mapping[rel_path] = PRINCIPLES
        elif rel_path == "docs/02-control-loop.md":
            mapping[rel_path] = CONTROL_LOOP
        elif rel_path == "docs/03-staged-discovery.md":
            mapping[rel_path] = STAGED_DISCOVERY
        elif rel_path == "docs/04-verification-and-consequence.md":
            mapping[rel_path] = VERIFICATION
        elif rel_path == "docs/05-budgeting-telemetry.md":
            mapping[rel_path] = BUDGETS_TELEMETRY
        elif rel_path == "docs/06-memory-compression.md":
            mapping[rel_path] = MEMORY
        elif rel_path == "docs/07-anti-patterns.md":
            mapping[rel_path] = ANTI_PATTERNS
        elif rel_path == "concepts/Context-Capsule-v0.1.md":
            mapping[rel_path] = CONTEXT_CAPSULE
        elif rel_path == "artifacts/01-policy-card-template.md":
            mapping[rel_path] = POLICY_CARD
        elif rel_path == "artifacts/02-attention-budget-spec.md":
            mapping[rel_path] = ATTENTION_BUDGET_SPEC
        elif rel_path == "artifacts/03-telemetry-schema.md":
            mapping[rel_path] = TELEMETRY_SCHEMA
        elif rel_path == "artifacts/04-evaluation-rubric.md":
            mapping[rel_path] = EVAL_RUBRIC
        elif rel_path == "artifacts/05-investigation-playbook.md":
            mapping[rel_path] = PLAYBOOK
        elif rel_path == "open-questions/00-index.md":
            mapping[rel_path] = OPEN_Q
        elif rel_path == ".github/ISSUE_TEMPLATE/cae-proposal.md":
            mapping[rel_path] = ISSUE_PROPOSAL
        elif rel_path == ".github/ISSUE_TEMPLATE/cae-update.md":
            mapping[rel_path] = ISSUE_UPDATE
        elif rel_path == ".github/pull_request_template.md":
            mapping[rel_path] = PR_TEMPLATE
        elif rel_path == "CONTRIBUTING.md":
            mapping[rel_path] = CONTRIB
        elif rel_path == "LICENSE.md":
            mapping[rel_path] = LICENSE
        else:
            mapping[rel_path] = COMMON_VOICE + "# TODO"

    for rel, content in mapping.items():
        ensure_file(APP / rel, content)

    print(f"Bootstrap complete. Created/updated files under: {APP}")

if __name__ == "__main__":
    main()

