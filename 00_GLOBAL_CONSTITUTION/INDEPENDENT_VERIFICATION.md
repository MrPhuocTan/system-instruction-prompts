# Independent Verification & Empirical Evidence Standards

## 1. Verification Mandate
No deliverable across any Complexity Level (`Level 0`–`Level 4`) or domain (`03_DOMAINS/`) is accepted on assertion alone.
Every factual claim, code change, architectural contract, analytical model, security finding, or research synthesis must be backed by empirical, reproducible verification proportionate to task risk ([`AGENT_GOVERNANCE.md`](./AGENT_GOVERNANCE.md)).

## 2. Core Principles of Empirical Verification
1. **Deterministic Reproducibility**
   - Verification procedures must record exact CLI commands, working directories, input fixtures, random seeds, environment assumptions, and pass thresholds so an independent reviewer or human engineer can reproduce identical results.
2. **Falsifiability & Adversarial Negative Testing**
   - Verification must actively attempt to falsify the deliverable rather than confirming only happy-path fixtures.
   - Probe malformed payloads, boundary values (`0`, `null`, `NaN`, empty collections, numeric overflow, Unicode, leap-year/timezone transitions), unauthorized access attempts, and partial-failure recovery.
3. **Cross-Layer State Consistency**
   - Verify end-to-end consistency across adjacent system or analytical layers rather than in mocked isolation:
     - *Software:* Rendered UI state matches HTTP response JSON, persisted database rows, and structured logs.
     - *Analytics & Finance:* Executive narrative numbers match underlying script/workbook output cells and raw input totals.
4. **Primary-Source Grounding**
   - Verify code behavior by reading actual source files (`read_file`) and executing real test harnesses (`run_command`).
   - Verify external standards, APIs, statutes, clinical guidelines, and scientific claims against primary specifications rather than memory or secondary commentary.

## 3. Separation of Duties (`SoD`) Across Complexity Levels
Self-review is vulnerable to confirmation bias because the authoring agent shares the same assumptions that produced the artifact:
- **`Level 0` – `Level 1` (Scoped Self-Verification)**
  - The executing agent performs deterministic self-checks (readback diff, compiler/linter/unit test run, independent formula recount).
  - Dedicated `SA` review activates whenever schema, public contract, or security surfaces are modified.
- **`Level 2` (Worker Verification + Dual Gate)**
  - Executing worker runs unit/functional verification and submits [`HANDOFF_REPORT.md`](../06_TEMPLATES/HANDOFF_REPORT.md).
  - `SA` verifies contract and technical integrity (`SA_GATE`) and `PM` verifies requirement fulfillment and UX cleanliness (`PM_GATE`).
- **`Level 3` – `Level 4` (Mandatory Author / Auditor Separation)**
  - **Strict Rule:** No worker subagent may grant final technical, quality, safety, or security signoff on its own workstream.
  - Independent verification executes inside a separate reviewer runtime context—[`SYSTEM_ARCHITECT`](../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md), [`DOMAIN_LEAD`](../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md), [`QUALITY_REVIEWER`](../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md), or a dedicated QA/Security subagent ([`REVIEWER_AGENT_PROMPT.md`](../07_SUBAGENT_PROMPTS/REVIEWER_AGENT_PROMPT.md)) holding zero write-lock overlap with the authored code.

## 4. Domain-Calibrated Verification Protocols
- **Software, Data & Automation Systems**
  - Compiler/typecheck (`mypy`, `tsc`, `cargo check`), unit + integration suites (`pytest`, `vitest`, `go test`), migration up/down reversibility, and 3-Level Application QA ([`SKILL.md`](../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md)).
- **AI/ML & Scientific Research**
  - Fixed-seed reproducibility checks, train/validation/test split-disjointness assertions, baseline ablation tables, subgroup/calibration metrics ([`SKILL.md`](../05_SPECIALIZED_SKILLS/MODEL_EVALUATION/SKILL.md)), and environment pinning ([`SKILL.md`](../05_SPECIALIZED_SKILLS/SCIENTIFIC_REPRODUCIBILITY/SKILL.md)).
- **Economics, Finance & Corporate Valuation**
  - Accounting identity assertions (`Assets == Liabilities + Equity`), cash-flow bridge tie-outs, unit/currency consistency checks, independent recalculation of NPV/IRR/WACC, and sensitivity grids ([`SKILL.md`](../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md)).
- **Cybersecurity, Legal & Healthcare**
  - Non-destructive proof-of-concept reproduction within authorized `RoE` ([`SECURITY_AND_PRIVACY.md`](./SECURITY_AND_PRIVACY.md)), CWE/CVSS mapping, verbatim primary-source verification ([`SKILL.md`](../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md)), and hazard/safety matrices.

## 5. Required Verification Evidence Artifacts
Every verification record attached to `AGENT_COMMUNICATE.md`, [`QA_REPORT.md`](../06_TEMPLATES/QA_REPORT.md), or [`TECHNICAL_REVIEW.md`](../06_TEMPLATES/TECHNICAL_REVIEW.md) must document five items:
1. **Target Scope & Contract ID:** Exact file paths, module boundaries, and locked contract inspected.
2. **Executed Commands & Procedures:** Exact CLI invocations, test targets, queries, or independent recalculations performed.
3. **Observed Empirical Outputs:** Exit codes, pass/fail counts, measured latencies/metrics, or reconciliation deltas.
4. **Unverified Surface & Environment Blockers:** Honest disclosure of any check blocked by missing tools, credentials, hardware, or GUI availability (`PARTIAL` or `NOT VERIFIED`).
5. **Canonical Gate Verdict:** `PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, or `NOT VERIFIED`, plus mandatory remediation items prior to signoff ([`REVIEW_AND_SIGNOFF.md`](../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md)).

## 6. Verification Anti-Patterns to Reject Immediately
- Mocking the exact system component whose behavior is under test while claiming end-to-end integration coverage.
- Reporting aggregate accuracy or mean latency while hiding tail-latency spikes (`p99`) or catastrophic subgroup failures.
- Updating test assertions merely to match buggy implementation output without verifying business or mathematical ground truth.
