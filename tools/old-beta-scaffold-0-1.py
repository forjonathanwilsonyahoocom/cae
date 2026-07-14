#!/usr/bin/env python3

from pathlib import Path


ROOT = Path(".")


DOCUMENTS = [
    "README.md",
    "MANIFESTO.md",
    "LAWS.md",
    "STYLE.md",

    "concepts/computational-attention.md",
    "concepts/attention-budget.md",

    "principles/search-before-generation.md",
    "principles/evidence-over-confidence.md",
    "principles/model-agnostic-design.md",

    "patterns/verification-loop.md",
    "patterns/search-first.md",

    "anti-patterns/unbounded-computation.md",
    "anti-patterns/prompt-roulette.md",

    "telemetry/attention-tracing.md",

    "experiments/experimental-methodology.md",

    "field-notes/.gitkeep",
]


TEMPLATE = """\
---
title: {title}
status: draft
category: {category}

keywords:
  - computational attention
  - autonomous systems

---

# {title}

## Intent

Why does this artifact exist?

---

## Purpose

What problem does this address?

---

## Scope

What is included?

---

## Non-Goals

What is deliberately excluded?

---

## Background

Context and motivation.

---

## Principles

Relevant engineering principles.

---

## Guidance

Practical implications.

---

## Examples

Examples will be added.

---

## Related Artifacts

Related concepts:

- 

---

## Open Questions

Questions requiring investigation.

---

## Research Directions

Future work.

---

## Revision History

Initial scaffold.
"""


def title_from_path(path):
    name = path.stem.replace("-", " ")
    return name.title()


def category_from_path(path):
    return path.parts[0] if len(path.parts) > 1 else "root"


def create_document(path):
    file = ROOT / path

    if file.exists():
        return

    file.parent.mkdir(parents=True, exist_ok=True)

    file.write_text(
        TEMPLATE.format(
            title=title_from_path(file),
            category=category_from_path(file),
        )
    )

    print(f"created {file}")


for document in DOCUMENTS:
    create_document(Path(document))
