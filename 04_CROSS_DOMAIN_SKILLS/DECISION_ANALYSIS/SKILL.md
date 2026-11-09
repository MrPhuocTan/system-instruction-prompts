---
name: decision-analysis
description: "Use this skill when selecting among competing architectures, vendors, algorithms, investment options, or operational trade-offs under multiple constraints, uncertainty, and differing reversibility profiles."
---

# Decision Analysis

## Skill Metadata
- **Skill ID:** `SKL-CORE-006`
- **Name:** `decision-analysis`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Provide structured, transparent, and auditable trade-off evaluation when choosing among mutually exclusive or resource-constrained alternatives. This skill prevents ad-hoc gut selection, single-metric tunnel vision, and disguised bias by enforcing hard-constraint filtering, weighted multi-criteria scoring, reversibility classification (Type 1 vs. Type 2 decisions), expected-value/downside modeling, and sensitivity testing.

## Required Competencies
- Multi-Criteria Decision Analysis (`MCDA`), Pareto frontier identification, and explicit non-negotiable constraint gating.
- Decision framing under uncertainty: expected value, minimax regret, tail-risk bounding, and Value of Information (`VoI`) calculation.
- Reversibility and switching-cost assessment (two-way door rapid iteration vs. one-way door high-rigor commitment).
- Architecture Decision Record (`ADR`) and executive trade-off documentation with clear kill/reversal triggers.

## Prerequisites
- Decision trigger, decision owner (`PM`, `SA`, `DOMAIN_LEAD`, or human stakeholder), and deadline established.
- Hard constraints (budget ceiling, latency SLO, regulatory residency, hardware/thermal envelope, license compatibility) enumerated via [REQUIREMENTS_ANALYSIS](../REQUIREMENTS_ANALYSIS/SKILL.md).
- Empirical baseline facts gathered via [RESEARCH_AND_SOURCE_VALIDATION](../RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) or [DATA_INTERPRETATION](../DATA_INTERPRETATION/SKILL.md).

## Workflow
1. **Frame Decision & Classify Reversibility:** Define the exact question, decision horizon, and reversibility class (*Type 2 reversible two-way door* -> optimize speed and bounded experimentation; *Type 1 irreversible/high-switching-cost one-way door* -> require deep modeling, `SA` review, and human sign-off).
2. **Generate Genuine Alternatives (Including Baseline):** Assemble at least three distinct, viable options—including a `Status Quo / Do Nothing` or `Minimal Viable Change` baseline—rather than padding a pre-chosen winner with strawman options.
3. **Apply Hard Pass/Fail Knock-Out Gates:** Eliminate any option that violates mandatory security, legal/licensing, safety, compliance, or physical resource constraints before scoring trade-offs.
4. **Evaluate Surviving Options Against Weighted Criteria:** Define orthogonal evaluation criteria (e.g., TCO, operational complexity, p99 performance, implementation lead time, vendor lock-in, failure blast radius) with explicit weights summing to `100%` locked *prior* to scoring options.
5. **Run Sensitivity & Downside Stress Tests:** Perturb criterion weights (`+/- 15%`) and key input assumptions (2x traffic growth, vendor price hike, 50% schedule slip) to test whether the top-ranked option flips; compute Value of Information (`VoI`) to decide if a quick spike/prototype is warranted before committing.
6. **Lock Recommendation & Reversal Triggers:** State the recommended option, explicit trade-offs accepted, rejected alternatives with rationale, migration path, and concrete metric thresholds that would trigger contingency fallback.

## Tools and Techniques
- **Hard-Gate + Weighted Trade-Off Matrix:** Two-stage table separating binary knock-out invariants from weighted utility scores backed by concrete evidence per cell.
- **Pareto Frontier Pruning:** Identify and discard dominated options (worse or equal on all criteria and strictly worse on at least one) before stakeholder review.
- **Expected Value & Tail-Risk Scenario Tree:** Weight `Base`, `Upside`, and `Adverse Stress` scenarios while enforcing survival constraints against catastrophic tail loss.
- **Time-Boxed Empirical Spike:** Use `run_command` micro-benchmarks or proof-of-concept validation when `VoI` exceeds the cost of a short test.

## Verification Requirements
- Criterion weights sum accurately to `1.0` (`100%`), and weighted totals are computed deterministically without arithmetic errors.
- Every score assigned in the trade-off matrix cites measurable technical, financial, or operational justification rather than subjective adjectives alone.
- Sensitivity check explicitly confirms whether the recommendation remains stable under plausible assumption shifts or identifies the exact tipping threshold.

## Quality Criteria
- **Explicit Trade-Off Candor:** Clearly articulates what the chosen option sacrifices (cost, flexibility, latency, complexity) rather than claiming one option wins every dimension.
- **Proportional Rigor:** Matches analytical depth strictly to reversibility and blast radius:
  | Decision Class | Switching / Rollback Cost | Required Governance & Analysis Depth |
  | :--- | :--- | :--- |
  | `Type 2 — Two-Way Door` | Low (`< 1 day` refactor, feature-flagged, local module) | Fast 3-option check, pick cleanest path, verify empirically |
  | `Type 1 — One-Way Door` | High (public API, DB schema, cloud lock-in, capital commit) | Hard-gate filter + weighted `MCDA` + sensitivity test + `SA`/human gate |
- **Actionable Reversal Criteria:** Includes objective post-deployment metrics and contingency plans if core assumptions fail in production.
- **Failure Modes to Avoid:**
  - *Post-Hoc Weight Rigging:* Adjusting criterion weights after scoring until a pre-selected favorite option wins.
  - *Strawman Padding:* Surrounding one preferred architecture with two obviously broken alternatives to create false choice.
  - *TCO Blindness:* Comparing initial build effort while ignoring 3-year operational toil, licensing escalators, and exit lock-in.
  - *Analysis Paralysis:* Running heavy `MCDA` ceremonies on cheap, reversible two-way door implementation details.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md), legal compliance, or safety non-negotiables.
- Security, privacy, human safety, and regulatory legality MUST be modeled as **binary hard knock-out gates**, never traded off as soft weighted scores against cost or speed.
- Escalate consequential irreversible architectural, financial, legal, or production-infrastructure decisions for explicit human approval before execution.

## Expected Deliverables
- **Decision Record (`ADR` / Trade-Off Brief)** stating context, reversibility class, hard knock-out gates, and weighted comparison matrix.
- **Sensitivity & Risk Analysis** detailing tipping points, accepted downsides, and Value-of-Information spike findings.
- **Execution & Reversal Plan** specifying immediate implementation actions, monitoring metrics, and fallback triggers.
