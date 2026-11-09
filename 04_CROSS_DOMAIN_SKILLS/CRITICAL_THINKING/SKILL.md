---
name: critical-thinking
description: "Use this skill when evaluating arguments, proposals, architectural claims, analytical conclusions, or conflicting stakeholder inputs for logical validity, hidden biases, causal soundness, and evidentiary sufficiency."
---

# Critical Thinking

## Skill Metadata
- **Skill ID:** `SKL-CORE-002`
- **Name:** `critical-thinking`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Subject technical designs, research claims, business cases, security assessments, and troubleshooting narratives to rigorous logical and evidentiary scrutiny. This skill detects fallacies, unstated premises, correlation-causation conflation, survivorship bias, and cherry-picked metrics before flawed conclusions propagate into implementation or executive decisions.

## Required Competencies
- Deductive, inductive, and abductive argument decomposition (premises, inference rules, conclusions, counterexamples).
- Causal inference hygiene: distinguishing correlation, confounding variables, reverse causality, selection bias, and mechanistic causation.
- Steelmanning competing viewpoints while systematically testing boundary conditions that falsify each claim.
- Cognitive bias mitigation across anchoring, sunk-cost fallacy, availability heuristic, survivorship bias, and authority bias.

## Prerequisites
- Target claim, proposal, architecture RFC, incident RCA, or analytical report loaded via `read_file` or user context.
- Baseline problem framing established via [COGNITIVE_EXECUTION](../COGNITIVE_EXECUTION/SKILL.md).
- Access to underlying data definitions, denominator baselines, or source artifacts supporting the claim.

## Workflow
1. **Deconstruct the Claim Structure:** Extract the core conclusion, explicit premises, hidden assumptions, and definitions of key terms (metrics, baselines, scope boundaries).
2. **Audit Evidentiary Sufficiency:** Evaluate whether cited evidence is primary or secondary, representative or cherry-picked, reproducible, and sized with valid denominators and sample frames.
3. **Test Causal & Logical Validity:** Check whether the conclusion follows necessarily or probabilistically from the premises. Screen for confounding factors, base-rate neglect, post-hoc ergo propter hoc errors, and false dichotomies.
4. **Construct Steelman Counter-Arguments:** Formulate the strongest plausible alternative explanation or competing architectural/business option and evaluate whether existing evidence rules it out.
5. **Stress-Test Boundary & Edge Conditions:** Identify scale thresholds, adversarial inputs, regime shifts, or operational constraints under which the argument breaks down.
6. **Synthesize Calibrated Verdict:** Classify each major claim as `Substantiated`, `Conditionally Valid (with explicit bounds)`, `Insufficiently Supported`, or `Refuted`, and prescribe specific disambiguating tests.

## Tools and Techniques
- **Toulmin Argument Mapping:** Explicitly map *Claim*, *Grounds (Evidence)*, *Warrant*, *Backing*, *Qualifier (Confidence)*, and *Rebuttal Conditions*.
- **Falsification Matrix:** Pair every central thesis with the concrete observable measurement that would disprove it.
- **Denominator & Base-Rate Audit:** Recompute relative percentages (`+50% improvement`) against absolute counts, variance, and population base rates.
- **Inversion & Red-Team Critique:** Deliberately argue the opposite position using primary repository code, logs, or domain data retrieved via `read_file` and `run_command`.

## Verification Requirements
- Every logical critique cites the exact clause, metric, equation, or code path under review rather than attacking a strawman summary.
- Quantitative counter-checks verify units, denominators, time windows, and sample selection criteria directly.
- Alternative explanations proposed during critique are checked for physical, technical, or economic feasibility.

## Quality Criteria
- **Intellectual Honesty & Symmetry:** Applies identical evidentiary rigor to favored proposals, user assumptions, and dissenting options alike.
- **Constructive Precision:** Critiques pinpoint exact failure mechanisms and specify actionable validation experiments rather than vague skepticism.
- **Calibrated Confidence:** Confidence levels reflect sample quality, causal identification strength, and external validity limits:
  | Verdict Tier | Evidentiary Threshold | Permitted Operational Action |
  | :--- | :--- | :--- |
  | `Substantiated` | Primary reproducible proof + rival causes ruled out | Proceed to design/implementation lock |
  | `Conditionally Valid` | Holds within bounded regime; sensitive to stated assumptions | Proceed with runtime guardrails & monitoring |
  | `Insufficiently Supported` | Plausible hypothesis lacking denominator/causal proof | Run bounded validation experiment first |
  | `Refuted` | Contradicted by primary code, math, or empirical telemetry | Reject claim and pivot to rival hypothesis |
- **Failure Modes to Avoid:**
  - *Sycophantic Premise Acceptance:* Agreeing with flawed user assumptions instead of surfacing contradictory repository or domain evidence politely.
  - *Contrarian Nitpicking:* Stalling delivery over non-material edge cases that have zero impact on safety, correctness, or SLOs.
  - *Metric Equivocation:* Shifting metric definitions mid-argument (e.g., conflating gross signups with retained active users).
  - *Proxy Worship (`Goodhart's Law`):* Treating proxy benchmark gains as proof of genuine end-user or business value.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), safety constraints, or human authorization policies.
- Present critiques objectively without disparaging stakeholders; attack structural flaws in evidence and logic rather than individuals.
- Never selectively omit disconfirming evidence to defend a prior recommendation or sunk implementation effort.

## Expected Deliverables
- **Claim & Assumption Audit Table** mapping major assertions, supporting evidence quality, logical/causal flaws, and validity status.
- **Boundary & Counterexample Analysis** detailing concrete conditions under which the proposal fails.
- **Disambiguation Plan** listing minimum empirical checks required to resolve contested claims.
