---
name: risk-management
description: "Use this skill when identifying, quantifying, prioritizing, and mitigating technical, operational, security, financial, compliance, safety, or delivery risks across planning and execution phases."
---

# Risk Management

## Skill Metadata
- **Skill ID:** `SKL-CORE-010`
- **Name:** `risk-management`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Proactively identify, analyze, prioritize, treat, and monitor threats across technical architecture, data migrations, cybersecurity, financial exposure, regulatory compliance, physical safety, and project schedules so catastrophic failure modes are prevented before execution and residual risks remain explicitly bounded and owned.

## Required Competencies
- Structured hazard and threat identification (`FMEA` Failure Modes and Effects Analysis, pre-mortems, dependency failure trees, bow-tie analysis).
- Calibrated risk scoring separating *Likelihood / Exposure Frequency*, *Impact Severity*, and *Detection Lead Time* (avoiding vague qualitative hand-waving).
- Risk treatment engineering (`Avoid`, `Mitigate / Reduce`, `Transfer / Share`, `Accept with Contingency`) across preventive, detective, and corrective controls.
- Trigger-based contingency planning, blast-radius containment, and executive escalation governance.

## Prerequisites
- System scope, workstream dependencies, asset sensitivity, and operational environment established via [SYSTEMS_THINKING](../SYSTEMS_THINKING/SKILL.md) and [REQUIREMENTS_ANALYSIS](../REQUIREMENTS_ANALYSIS/SKILL.md).
- Alignment with [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md) for Level 3-4 high-impact or irreversible operations.
- Target risk tracking artifact ([RISK_REGISTER.md](../../06_TEMPLATES/RISK_REGISTER.md) or workstream risk section) identified.

## Workflow
1. **Enumerate Failure Modes & Threat Vectors:** Conduct a systematic sweep across technical failure (data loss, schema lock, thermal/disk exhaustion), security/privacy exposure, external dependency outage, regulatory/licensing breach, financial/model error, and schedule bottlenecks.
2. **Trace Causal Chain (`Cause -> Event -> Impact`):** Express every risk strictly in three-part causal syntax (`Because <root vulnerability/condition>, <trigger event> may occur, resulting in <quantified impact>`), eliminating vague one-word entries like `"Database risk"`.
3. **Score Inherent Risk & Asymmetric Tail Exposure:** Rate inherent *Likelihood* (`1-5`) and *Impact* (`1-5`); flag any `Impact = 5` existential, human-safety, data-loss, or legal violation for mandatory mitigation regardless of low estimated probability.
4. **Engineer Bow-Tie Controls:** Design layered treatments for top risks:
   - *Preventive Controls:* Pre-checks, schema locks, dry-runs, feature flags, staging gates, static analysis.
   - *Detective Controls:* Canary metrics, anomaly alerts, reconciliation checksums, audit logs.
   - *Corrective / Contingency Controls:* Automated rollback, point-in-time backups, circuit breakers, manual runbook failover.
5. **Assign Accountable Owners & Early-Warning Triggers:** Bind each active risk to a named role/workstream owner and define objective leading indicators that activate the contingency plan automatically.
6. **Re-Assess Residual Risk & Escalate:** Compute post-control residual risk; escalate any unmitigated `HIGH` / `CRITICAL` residual risk to `SA`, `PM`, and human stakeholders for formal sign-off before execution proceeds.

## Tools and Techniques
- **Bow-Tie Control Matrix:** Map root causes -> preventive barriers -> central hazard event -> mitigative barriers -> bounded consequences.
- **`FMEA` (`Severity x Occurrence x Undetectability`):** Prioritize silent, hard-to-detect data corruption or subtle logic bugs higher than loud, immediately detected crashes.
- **Blast-Radius Progressive Rollout:** Partition risky changes into dry-run -> shadow mode -> 1% canary -> staged cohorts -> full cutover with automated halt gates.
- **Host Resource Safety Guardrails:** Verify disk headroom (`df -h`), memory bounds, and CPU/GPU batch sizes via `run_command` before launching heavy jobs.

## Verification Requirements
- Every `CRITICAL` and `HIGH` risk has verified preventive AND rollback/contingency controls tested or inspected prior to executing the risky step.
- Backup, snapshot, or git rollback readiness is empirically verified before destructive migrations, bulk refactors, or infrastructure changes.
- Residual risks are transparently disclosed in handoff reports and final delivery summaries—never silently absorbed by worker agents.

## Quality Criteria
- **Concrete Causal Specificity:** Risks specify exact failure mechanics and measurable blast radius (`table lock > 30s dropping checkout writes`) rather than generic platitudes.
- **Tail-Risk Discipline:** Low-probability, catastrophic-impact events (`Impact = 5`) are never dismissed via simple multiplication (`1 x 5 = 5`):
  | Risk Treatment Strategy | When to Apply | Required Control Evidence |
  | :--- | :--- | :--- |
  | `Avoid` | Unacceptable safety, legal, or existential tail impact | Redesign workflow to eliminate hazard source entirely |
  | `Mitigate / Reduce` | Actionable technical, security, or operational exposure | Verified preventive + detective + rollback controls |
  | `Transfer / Share` | Financial/SLA exposure suitable for contractual/insurance bounds | Explicit SLA/contract cap (never transfers safety/compliance duty) |
  | `Accept with Contingency` | Low residual risk below threshold (or stakeholder-signed) | Documented trigger metric + tested fallback runbook |
- **Live Operational Ownership:** Risk registers update dynamically as assumptions retire or new blockers emerge during execution.
- **Failure Modes to Avoid:**
  - *Write-Only Compliance Theater:* Producing a static risk table at kickoff and ignoring it during high-risk schema or infra changes.
  - *Unbacked Irreversibility:* Running destructive migrations or bulk deletions without testing backup restoration first.
  - *Silent Corruption Blindspot:* Monitoring process crashes while omitting checksums/canary alerts for silent calculation corruption.
  - *Unauthorized Risk Absorption:* Worker subagents silently accepting security or data-loss risks that require `SA`, `PM`, and human sign-off.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md), safety laws, or cybersecurity authorization rules.
- Worker agents MUST NEVER unilaterally "accept" residual risks involving human physical safety, unauthorized security exposure, regulatory illegality, secret leakage, or unapproved production data destruction.
- Halt immediately and escalate via `ask_question` / `PM + SA` whenever observed operational risk exceeds pre-approved bounds.

## Expected Deliverables
- **Populated Risk Register** (aligned with [RISK_REGISTER.md](../../06_TEMPLATES/RISK_REGISTER.md)) containing causal statements, inherent/residual scores, owners, and statuses.
- **Preventive, Detective & Rollback Control Plan** detailing concrete safeguards and pre-flight verification checks.
- **Residual Risk & Escalation Brief** highlighting items requiring `SA`, `PM`, or explicit human approval prior to go-live.
