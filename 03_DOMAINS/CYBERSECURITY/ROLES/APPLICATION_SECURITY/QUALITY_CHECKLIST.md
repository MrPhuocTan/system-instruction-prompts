# Quality Checklist — Application Security Engineer (`ROLE-CYB-002`)

Verify every item prior to handoff and `SA_GATE` review, per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope & Safe Execution (`RoE`)
- [ ] Target repository/service **scope**, test environment boundaries, and **Rules of Engagement (`RoE`)** / **authorization** were verified prior to running dynamic checks.
- [ ] All verification used **non-destructive** local/isolated test harnesses; zero active payloads were sent to unapproved external or production endpoints.
- [ ] Hardcoded live secrets or malicious supply-chain artifacts discovered in source/history were flagged immediately for rotation/containment without exposing cleartext values.

---

## 2. Technical Depth, Taint Tracing & Variant Analysis
- [ ] Every finding traces the complete `Source -> Sanitizer/Middleware -> Sink` data flow with exact `file:line` references and `CWE` + `OWASP ASVS` / `API Top 10` identifiers.
- [ ] Object-level (`BOLA`/`IDOR`) and function-level (`BFLA`) tenant ownership checks were verified across read, mutation, and batch API handlers.
- [ ] Dependency/SCA findings verify both package lockfile version and actual runtime call-path reachability (`CycloneDX`/`SPDX` / lockfile evidence).
- [ ] Codebase-wide variant analysis confirmed sibling endpoints, background workers, and shared utilities do not harbor the same vulnerable pattern.

---

## 3. Epistemic Classification, Scoring & Redaction
- [ ] Each item is strictly classified as **Confirmed Vulnerability**, **Potential Finding**, **False Positive** (with documented compensating control), or **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings include valid `CVSS v3.1/v4.0` vectors adjusted for authentication level, tenant boundary impact, and exploitability.
- [ ] `100%` of credentials, tokens, signing keys, session cookies, and PII/PHI are redacted in test fixtures, logs, and reports.

---

## 4. Root-Cause Remediation & Retest Verification
- [ ] Fixes address structural root causes (parameterized queries, object-level policy enforcement, strict schema validation, safe serialization) rather than bypassable regex blacklists.
- [ ] Deterministic **retest** evidence proves the negative security test blocks the exploit payload AND existing unit/integration suites pass without functional regression.
- [ ] Custom static rules (`Semgrep`/linter) or CI regression tests are added/documented to prevent future reintroduction.
