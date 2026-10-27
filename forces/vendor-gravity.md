# Vendor‑Gravity

## Intent
Explain the *vendor‑gravity* force: the tendency for an organization’s reliance on a single vendor to grow over time, creating a pull that can lock the organization into that vendor’s ecosystem.

## Purpose
Highlight why vendor‑gravity matters for agent‑based development: increased risk of data breaches, cost escalation, reduced flexibility, and the difficulty of switching when the system has become tightly coupled to a vendor’s APIs, data formats, or proprietary tooling.

## Scope
* All types of vendors: SaaS, hardware, cloud, data‑providers, and third‑party services.
* All stages of the vendor lifecycle: onboarding, usage growth, renewal, and exit.
* The impact on agent‑based systems that depend on vendor‑provided data or services.

## Non‑Goals
* Detailed vendor‑specific contract negotiation.
* Vendor‑specific pricing models.
* Technical implementation of vendor‑independent adapters.

## Background
Industry reports show that 60 % of enterprises experience vendor lock‑in, and 35 % of data breaches originate from third‑party vendors (Gartner, 2025). As agents consume more data and services from a single vendor, the *gravity* increases: the cost of switching rises, and the risk of a single point of failure grows.

## Principles
1. **Maintain vendor diversity** – avoid single points of failure.
2. **Enforce regular contract reviews** – ensure terms remain aligned with business needs.
3. **Monitor usage and cost** – detect runaway growth early.
4. **Keep an exit strategy** – document migration paths and data export procedures.
5. **Apply the same rigor to vendor‑gravity as to other forces** – treat it as a measurable risk.

## Guidance
* **Audit vendor usage** quarterly: track API calls, data volume, and feature adoption.
* **Set renewal thresholds**: if usage exceeds 150 % of the original contract, trigger a review.
* **Implement a vendor‑gravity scorecard**: score vendors on cost, risk, flexibility, and strategic fit.
* **Automate alerts** when a vendor’s score drops below a critical level.
* **Document migration plans** for each critical vendor.

## Examples
* A SaaS analytics platform that grew from 1 user to 200 users, with the contract automatically scaling but the cost per user increasing by 30 %.
* A single hardware supplier providing all compute nodes; a failure in their supply chain halts the entire agent cluster.
* A data‑provider whose API changed, forcing agents to rewrite adapters and causing a 2‑month outage.

## Related Artifacts
* [network‑asynchrony.md](../network-asynchrony.md) – vendor‑gravity can amplify network delays.
* [context‑depreciation.md](../context-depreciation.md) – heavy reliance on a vendor’s data can accelerate context loss.
* [model‑volatility.md](../model-volatility.md) – vendor‑driven parameter drift.

## Open Questions
* How to quantify vendor‑gravity in a single metric?
* What thresholds should trigger a vendor exit?
* How to balance cost savings from vendor consolidation against the risk of gravity?

## Future Research
* AI‑driven gravity detection dashboards.
* Automated migration tooling for agent‑based systems.
* Studies on the impact of vendor‑gravity on agent performance.

## References
* Gartner, "Vendor Lock‑In: The Hidden Cost", 2025.
* McKinsey, "Managing Vendor Risk in the Digital Age", 2024.
* Deloitte, "Global Chief Procurement Officer Survey", 2025.
* HIPAA Journal, "Third‑Party Breach Report", 2025.

## Revision History
* 2026‑10‑09 – Initial draft.
