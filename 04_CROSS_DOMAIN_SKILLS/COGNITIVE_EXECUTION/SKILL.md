---
name: cognitive-execution
description: "Use this skill when executing non-trivial reasoning, engineering, analytical, or multi-step problem-solving tasks that require assumption ledgering, premise challenging, expected-vs-actual outcome checks, and independent verification."
---

# Cognitive Execution

## Skill Metadata
- **Skill ID:** `SKL-CORE-001`
- **Name:** `cognitive-execution`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Operationalize disciplined epistemic execution across every Level 1-4 task so agents solve the underlying real-world problem rather than merely completing surface tool invocations. This skill enforces the mandatory closed-loop cycle (`Understand -> Reason -> Plan -> Execute -> Observe -> Independently Verify -> Accept / Reject / Investigate`), explicit assumption ledgering, multi-hypothesis analysis, calibrated uncertainty reporting, and concise decision summaries without exposing raw private chain-of-thought (`CoT`).

## Required Competencies
- Problem decomposition, constraint extraction, and objective disambiguation under incomplete information.
- Epistemic separation of verified facts, explicit working assumptions, quantitative estimates, and unresolved uncertainties.
- Premise challenging, competing-hypothesis generation, and falsification-oriented experimental design.
- Adversarial self-review and root-cause discrepancy investigation when observed outputs diverge from predictions.

## Prerequisites
- Active task request classified via [TASK_COMPLEXITY_ROUTER.md](../../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md) and aligned with [COGNITIVE_EXECUTION.md](../../00_GLOBAL_CONSTITUTION/COGNITIVE_EXECUTION.md).
- Access to primary workspace artifacts, schemas, logs, or authoritative external sources required to test premises empirically.
- Defined acceptance criteria (inline for Level 1; locked in workstream contracts for Levels 2-4).

## Workflow
1. **Understand (Objective & Premise Audit):** Restate the real user outcome, operating constraints, and blast radius. Challenge hidden premises, contradictory requirements, and XY-problem framing before touching files or commands.
2. **Reason (Epistemic Ledger & Hypothesis Framing):** Construct an explicit 4-column epistemic ledger separating *Verified Facts*, *Working Assumptions*, *Bounded Estimates*, and *Unresolved Uncertainties*. Formulate at least two competing hypotheses when diagnosing defects, performance regressions, or analytical anomalies.
3. **Plan (Pre-Registered Expectations):** Sequence atomic actions, map required tool calls, and state the expected observable outcome and failure signature for each step prior to execution.
4. **Execute (Controlled Action):** Run scoped reads, edits, or commands strictly within assigned file ownership and least-privilege boundaries.
5. **Observe (Expected-vs-Actual Comparison):** Capture raw stdout/stderr, exit codes, payloads, and state mutations. Compare observed results directly against pre-registered expectations; never ignore warnings, silent truncations, or unexpected side effects.
6. **Independently Verify (`Tool Success != Task Success` Gate):** Validate outcomes through an orthogonal check rather than trusting command exit code `0`:
   - Build succeeding does not prove runtime behavior works.
   - Unit tests passing on mocks do not prove end-to-end user journeys succeed.
   - `HTTP 200` does not prove response schema, authorization, or persisted state is valid.
   - Low training/validation loss does not prove out-of-distribution generalization or absence of data leakage.
   - Generating a formatted document does not prove domain accuracy, math integrity, or source truth.
7. **Accept / Reject / Investigate:** Accept only when independent evidence satisfies all acceptance criteria; reject and roll back on invariant violation; investigate root causes iteratively when expectations and observations diverge, then emit a concise structured reasoning summary without raw `CoT` dumps.

## Tools and Techniques
- **Epistemic Ledger Table:** Markdown state table tracking assumption ID, rationale, blast radius if false, and empirical validation method.
- **Analysis of Competing Hypotheses (ACH):** Matrix scoring diagnostic or design hypotheses against disconfirming evidence rather than confirming bias.
- **Pre-Mortem & Inversion Check:** Ask what concrete input, concurrency race, scale boundary, or environment drift would cause the proposed solution to fail silently.
- **Antigravity Runtime Mapping:** Inspect primary truth via `read_file` and `run_command`; resolve material user-intent ambiguities via `ask_question`; coordinate cross-stream assumptions via [AGENT_COMMUNICATE.md](../../06_TEMPLATES/AGENT_COMMUNICATE.md).

## Verification Requirements
- Every material claim in outputs maps to a concrete file path, line range, command output, test artifact, or cited primary source.
- Expected-vs-actual comparison is documented for non-trivial code changes, calculations, data pipelines, and system mutations.
- Orthogonal verification confirms task-level success independently of the primary generation step (`[INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)`).
- Unverified items are explicitly labeled `NOT VERIFIED` with concrete blockers and required validation steps.

## Quality Criteria
- **Zero Premature Convergence:** Root causes and constraints are verified before irreversible edits or architectural commitments occur.
- **Zero Silent Assumption Drift:** Epistemic claims are strictly stratified and audited throughout execution:
  | Epistemic Category | Definition | Mandatory Handling Rule |
  | :--- | :--- | :--- |
  | `Verified Fact` | Directly observed in repo files, command output, or Tier 1 source | Cite exact path/line, command output, or primary reference |
  | `Working Assumption` | Plausible premise adopted temporarily to unblock design | Log blast radius if false; retire via empirical test before sign-off |
  | `Bounded Estimate` | Quantitative approximation derived from stated parameters | State formula, lower/upper sensitivity bounds, and units |
  | `Unresolved Uncertainty` | Unknown behavior blocked by missing access, data, or tooling | Label `NOT VERIFIED`; escalate if consequential to safety/correctness |
- **Zero Private `CoT` Leakage or Verbose Filler:** User-facing and handoff outputs present crisp, auditable engineering rationale free of rambling internal monologues or decorative filler.
- **Failure Modes to Avoid:**
  - *Exit-Code Complacency:* Equating `exit 0` or `HTTP 200` with functional correctness without inspecting payload and state invariants.
  - *Confirmation Bias:* Running only positive checks that confirm a favored hypothesis while ignoring disconfirming log anomalies.
  - *Shotgun Debugging:* Mutating multiple variables simultaneously without isolating root cause or recording baseline behavior.
  - *Inference-as-Fact Conflation:* Reporting unverified mental extrapolations in authoritative declarative prose.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), human approval gates, Rules of Engagement, or write-lock boundaries.
- Never fabricate command outputs, citations, benchmark numbers, or verification states to close an uncertainty gap.
- Redact credentials, tokens, and regulated personal data from reasoning summaries, logs, and handoff reports.

## Expected Deliverables
- Concise **Epistemic & Assumptions Summary** (`Verified Facts`, `Assumptions`, `Estimates`, `Unresolved Uncertainties`).
- **Expected-vs-Observed Verification Record** demonstrating orthogonal proof that the real problem is solved.
- Explicit **Decision Disposition** (`ACCEPT`, `REJECT`, or `INVESTIGATE`) paired with actionable next steps or residual risks.
