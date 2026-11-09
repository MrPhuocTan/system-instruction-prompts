---
name: quality-assurance
description: "Use this skill when designing verification plans, auditing deliverables against acceptance criteria, constructing boundary and negative test matrices, or executing pre-handoff quality gates across any domain."
---

# Quality Assurance

## Skill Metadata
- **Skill ID:** `SKL-CORE-009`
- **Name:** `quality-assurance`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Establish systematic defect prevention, requirements-to-verification traceability, boundary/negative testing, and independent pre-delivery sign-off across software, data, AI, financial, scientific, legal, and industrial deliverables. This skill ensures outputs satisfy both technical contract correctness and genuine end-user utility before `SA_GATE` or `PM_GATE` review.

## Required Competencies
- Requirements Traceability Matrix (`RTM`) construction mapping every functional, non-functional, and domain constraint to deterministic verification checks.
- Equivalence partitioning, boundary-value analysis, state-transition testing, negative/adversarial input testing, and regression containment.
- Defect triage and taxonomy classification (`CRITICAL / BLOCKER`, `HIGH`, `MEDIUM`, `LOW`) with reproducible minimal failing cases.
- Separation-of-duties review discipline distinguishing author self-checks from independent reviewer verification.

## Prerequisites
- Explicit acceptance criteria and interface contracts defined in the user prompt, [WORKSTREAM_CONTRACT.md](../../06_TEMPLATES/WORKSTREAM_CONTRACT.md), or domain `QUALITY_GATES.md`.
- Access to deliverables under test and validation tooling via `read_file` and `run_command` (plus [HUMAN_CENTRIC_APPLICATION_QA](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) for interactive applications).
- Clear canonical status definitions (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, `NOT VERIFIED`).

## Workflow
1. **Build the Traceability Matrix (`RTM`):** Enumerate every explicit user requirement, `SA` interface contract clause, and domain quality gate; assign at least one objective pass/fail verification method to each item.
2. **Design Multi-Path Test Coverage:** Cover four mandatory quadrants for every deliverable:
   - *Happy Path:* Nominal valid inputs and primary workflows.
   - *Boundary Conditions:* Zero, empty, `null`, single-element, exact max-limit, off-by-one, leap-year/timezone rollover, precision extremes.
   - *Negative & Malformed Inputs:* Invalid schemas, unauthorized roles, missing dependencies, timeouts, duplicate idempotency retries.
   - *Regression & Cross-Module Invariants:* Existing behavior, backward compatibility, and shared state integrity.
3. **Execute Deterministic & Independent Checks:** Run automated test suites, linters, schema validators, math reconciliations, or citation audits via `run_command`, inspecting actual assertions rather than exit code alone (preventing vacuous empty-test passes).
4. **Perform End-to-End Integration & UX Sanity Check:** Verify components work together across real module boundaries without stubbed-away integration seams.
5. **Log Defects with Reproducible Evidence:** Record every failure with exact severity, reproduction steps, expected vs. actual output, root cause, and regression test requirement.
6. **Verify Fixes & Issue Honest Gate Disposition:** Re-run full regression checks after remediation and assign an honest canonical gate status (`PASS`, `PARTIAL`, `BLOCKED`, `FAILED`, or `NOT VERIFIED`) in [QA_REPORT.md](../../06_TEMPLATES/QA_REPORT.md).

## Tools and Techniques
- **Boundary-Value Checklist:** Systematically probe `min - 1`, `min`, `min + 1`, nominal, `max - 1`, `max`, `max + 1`, UTF-8 multibyte strings, and concurrent mutations.
- **Assertion Density & Mutation Sanity Check:** Inspect test files via `read_file` to ensure tests assert meaningful domain invariants rather than merely asserting `result is not None` or mocking the system under test to return itself.
- **Cross-Artifact Reconciliation:** Reconcile code behavior, API documentation, configuration defaults, and handoff claims for 100% consistency.
- **Canonical Gate Classification:** Never mark a gate `PASS` when untested scope remains; classify unverified scope explicitly as `PARTIAL` or `NOT VERIFIED`.

## Verification Requirements
- 100% of acceptance criteria map to executed verification evidence (command logs, test outputs, calculation checks, or inspected artifacts).
- Zero open `CRITICAL` or `HIGH` defects in `PASS` deliverables; any waived `LOW` residual defect is explicitly documented with rationale.
- Test execution confirms real test discovery count (`N > 0` tests actually ran) and clean workspace state (`0` stray temp artifacts or secret leaks).

## Quality Criteria
- **Non-Vacuous Verification:** Tests fail reliably when the underlying invariant is broken and test real logic rather than tautological mocks:
  | Canonical Gate Status | Objective Criteria | Delivery Permission |
  | :--- | :--- | :--- |
  | `PASS` | `100%` RTM verified; `0` Critical/High defects; clean state | Cleared for `SA_GATE` + `PM_GATE` sign-off |
  | `PARTIAL` | Core scope verified; specific non-core items pending/waived | Requires explicit `PM + SA` waiver disclosure |
  | `BLOCKED` | External environment, credential, or dependency blocker | Halt affected scope; escalate blocker immediately |
  | `FAILED` | Any Critical/High defect, contract breach, or broken regression | Reject handoff; return for root-cause remediation |
  | `NOT VERIFIED` | Code/artifact exists on disk without empirical execution proof | Forbidden to claim `PASS`; disclose exact unverified scope |
- **Complete Reproducibility:** Another engineer or reviewer agent can re-run the exact commands in the QA report and observe identical results.
- **Honest Coverage Disclosure:** Environment or tool constraints (missing hardware, offline SaaS, absent GUI driver) are transparently disclosed, never hidden.
- **Failure Modes to Avoid:**
  - *Happy-Path Tunnel Vision:* Verifying nominal valid inputs while skipping `null`, boundary, unauthorized, and duplicate-retry paths.
  - *Tautological Mocking:* Mocking the database or service client to return hardcoded success when real SQL/HTTP schemas have drifted.
  - *Green-Washing CI:* Deleting, skipping (`@skip`), or loosening failing assertions to force a green test run.
  - *Vacuous Test Discovery:* Trusting `0 errors` when the test runner discovered `0` matching test files.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), production safety rules, or write-lock isolation.
- Run destructive, load, or fuzz tests strictly against isolated local/test fixtures—never against live production databases or unauthorized third-party services.
- Never alter test expectations or relax tolerances silently to mask genuine regressions.

## Expected Deliverables
- **Requirements Traceability & Test Coverage Matrix** mapping each acceptance criterion to test scenarios and pass/fail results.
- **Defect & Remediation Log** detailing severity, reproduction steps, root cause, fix verification, and regression coverage.
- **Structured QA Sign-Off Report** (aligned with [QA_REPORT.md](../../06_TEMPLATES/QA_REPORT.md)) declaring canonical status and residual risks.
