# Proportional Review, Domain Quality Gates & Dual Signoff (`SA_GATE` + `PM_GATE`)

## 1. Proportional Quality Governance
Review rigor scales strictly with task complexity ([`TASK_COMPLEXITY_ROUTER.md`](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md)) using the five canonical statuses (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, `NOT VERIFIED` defined in [`AGENT_GOVERNANCE.md`](../00_GLOBAL_CONSTITUTION/AGENT_GOVERNANCE.md)):
- **`Level 0`:** Main agent performs direct factual and logical accuracy verification inline before responding.
- **`Level 1`:** Executing agent runs targeted verification (readback diff, linter/unit check, formula check); `SA` review activates whenever schema, architecture, or security boundaries are affected.
- **`Level 2` – `Level 4`:** Mandatory **Three-Layer Review & Dual Signoff Protocol** below prior to final user delivery.

## 2. Layer 1 — Specialist Checklist & Domain Quality Gates
Before any workstream enters final signoff:
1. **Per-Role Self-Check**
   - The assigned specialist verifies every item in its role's `QUALITY_CHECKLIST.md` and loaded `SKILL.md` `Quality Criteria`.
2. **Domain Quality Gate Enforcement**
   - Outputs must satisfy all objective pass/fail thresholds in `03_DOMAINS/<DOMAIN>/QUALITY_GATES.md`.
   - On `Level 3`–`Level 4` multi-role or regulated tasks, [`DOMAIN_LEAD`](../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md) (`ROLE-CORE-003`) and an independent [`QUALITY_REVIEWER`](../02_CORE_ROLES/QUALITY_REVIEWER/SYSTEM_PROMPT.md) (`ROLE-CORE-004`, invoked via [`REVIEWER_AGENT_PROMPT.md`](../07_SUBAGENT_PROMPTS/REVIEWER_AGENT_PROMPT.md)) audit deliverables using [`QA_REPORT.md`](../06_TEMPLATES/QA_REPORT.md) under strict author/reviewer separation ([`INDEPENDENT_VERIFICATION.md`](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)).

## 3. Layer 2 — `SA_GATE` (Technical Architecture, Integration & Security Signoff)
Owned exclusively by [`SYSTEM_ARCHITECT`](../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md) and documented using [`TECHNICAL_REVIEW.md`](../06_TEMPLATES/TECHNICAL_REVIEW.md) (`Section 12: Technical Signoff` in `AGENT_COMMUNICATE.md`).
`SA_GATE = PASS` requires empirical proof across four pillars:
1. **100% Contract & Schema Compliance**
   - All APIs, data schemas, CLI contracts, file trees, and cross-module interfaces match `SA` pre-execution locks without silent drift ([`CONTRACT_AND_HANDOFF.md`](./CONTRACT_AND_HANDOFF.md)).
2. **Deterministic Automated Verification**
   - Compilers, linters, typecheckers, unit/integration suites, mathematical reconciliations, or repository validators exit `0` with observed output evidence (`Tool Success != Task Success` audited per [`COGNITIVE_EXECUTION.md`](../00_GLOBAL_CONSTITUTION/COGNITIVE_EXECUTION.md)).
3. **Write-Lock & Workspace Cleanliness**
   - Zero unauthorized file mutations, zero merge/overwrite regressions, zero stray scratch files ([`FILE_OWNERSHIP_AND_LOCKING.md`](./FILE_OWNERSHIP_AND_LOCKING.md)).
4. **Security, Privacy & Resource Safety**
   - Zero hardcoded secrets or unmasked `PII`/`PHI`, least-privilege defaults enforced, `RoE` honored on security tasks, and safe disk/CPU/GPU resource footprint ([`SECURITY_AND_PRIVACY.md`](../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md)).

## 4. Layer 3 — `PM_GATE` (Business Value, Completeness & Human-Centric UX Signoff)
Owned exclusively by [`PROJECT_MANAGER`](../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md) and documented using [`BUSINESS_REVIEW.md`](../06_TEMPLATES/BUSINESS_REVIEW.md) (`Section 13: Business/UX Signoff` in `AGENT_COMMUNICATE.md`).
`PM_GATE = PASS` requires empirical proof across four pillars:
1. **100% Requirement Traceability**
   - Every explicit user requirement, edge case, and acceptance criterion in `PROJECT_MANIFEST.md` is satisfied on disk with zero unfinished placeholder stubs.
2. **3-Level Human-Centric Application QA (When Applicable)**
   - Software and interactive deliverables satisfy [`SKILL.md`](../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) across:
     - *Level 1:* Deterministic Build, Schema & Automated Test Gate.
     - *Level 2:* Live Runtime, State Transition & End-to-End Journey Gate.
     - *Level 3:* Human-Centric Usability, Accessibility & Clean Layout Gate.
   - Unavailable live GUI/browser tools are honestly disclosed as `NOT VERIFIED` ([`TOOL_USAGE_AND_LIMITATIONS.md`](../00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md)).
3. **Zero "AI Sign" Clutter**
   - UI components, Markdown reports, financial memos, and documentation remain crisp, utilitarian, and domain-authentic—completely free of decorative emoji headers, marketing superlatives, or artificial filler.
4. **Epistemic Honesty in Delivery**
   - Verified facts, explicit assumptions, calibrated estimates, and residual risks are cleanly separated in [`FINAL_DELIVERY.md`](../06_TEMPLATES/FINAL_DELIVERY.md).

## 5. Gate Rejection & Remediation Loop
Whenever `SA_GATE` or `PM_GATE` evaluates to `FAILED` or unacceptable `PARTIAL`:
1. Record exact defect findings, `file:line` coordinates, and reproducible failure evidence in `Section 14: Outstanding Issues` of `AGENT_COMMUNICATE.md`.
2. Assign a scoped remediation workstream with an explicit Exclusive Write-Lock.
3. Re-execute full regression verification across affected modules before re-submitting to `SA_GATE` and `PM_GATE`.
4. Never ship final user delivery claiming `PASS` while blocking `SA_GATE` or `PM_GATE` findings remain unresolved.
