---
name: security-assessment
description: "Use this skill when conducting authorized code security reviews, threat modeling, configuration audits, dependency vulnerability triage, or bounded security validation under explicit Rules of Engagement."
---

# Security Assessment

## Skill Metadata
- **Skill ID:** `SKL-SPEC-006`
- **Name:** `security-assessment`
- **Domain:** `CYBERSECURITY, IT_SOFTWARE`
- **Version:** `1.0.0`

## Purpose
Execute rigorous, defensive-first security evaluations across source code, APIs, cloud/container infrastructure, IAM policies, dependencies, and application workflows strictly within authorized scope and Rules of Engagement (`RoE`). This skill enforces non-destructive verification defaults, forensic evidence preservation, secret redaction, strict separation of confirmed vulnerabilities from unverified observations, root-cause remediation, and mandatory retest verification.

## Required Competencies
- Threat modeling (`STRIDE`, trust-boundary data-flow diagrams, attack-surface enumeration) and security architecture review (`OWASP ASVS`, `NIST SSDF`, `CIS Benchmarks`).
- Static/manual code security auditing (`SAST`), Software Composition Analysis (`SCA` reachability triage), secret scanning, and IaC/cloud posture inspection.
- Vulnerability classification (`CWE`, `OWASP Top 10`, `CVSS v3.1/v4.0` contextualized by asset exposure and exploitability).
- Non-destructive proof-of-concept (`PoC`) validation, remediation engineering, and regression retesting.

## Prerequisites
- **Verified Explicit Authorization & Rules of Engagement (`RoE`):** Documented user authorization, exact in-scope targets (`repo paths`, `local ports`, `IP/CIDR`, `domains`), out-of-scope exclusions, and permitted test methods confirmed *before* any active probing begins.
- Alignment with [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) and [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md).
- Isolated local or authorized test environment for any dynamic verification.

## Workflow
1. **Verify Authorization, Scope & `RoE` Gate (Mandatory Step 0):** Confirm target ownership/authorization and lock exact `In-Scope` vs. `Out-of-Scope` boundaries. Halt immediately and escalate if authorization is missing, ambiguous, or targets unapproved external systems.
2. **Map Trust Boundaries & Threat Model:** Trace entrypoints, authentication/session flows, privilege tiers, sensitive data sinks (`PII`, secrets, keys, financial state), deserialization boundaries, and third-party integrations.
3. **Conduct Static, Configuration & Dependency Analysis First:** Prefer passive/static inspection via `read_file` and local `run_command` scanners (`semgrep`, `bandit`, `gosec`, `npm/pip/cargo audit`, IaC linters) to trace taint flows (`source -> sanitizer -> sink`) and reachability of vulnerable CVEs.
4. **Perform Safe, Non-Destructive Validation:** Where dynamic confirmation is authorized and in scope, prove exploitability using minimal, benign, reversible payloads (e.g., reading a synthetic canary record or verifying unauthorized `403` bypass on test fixtures—never `DROP TABLE`, DoS floods, or live data extraction).
5. **Classify Findings with Strict Epistemic Precision:** Categorize every item into one of four mutually exclusive classes while redacting live secrets:
   - *Confirmed Vulnerability:* Reproducibly verified in-scope flaw with concrete `PoC` evidence.
   - *Potential Finding:* Plausible code/config weakness lacking runtime reachability confirmation due to environment limits.
   - *False Positive:* Scanner alert disproven via reachability, upstream control, or framework auto-escaping proof.
   - *Unverified Observation:* Out-of-reach component requiring additional access or tooling to evaluate.
6. **Specify Remediation & Execute Retest Verification:** Provide root-cause code/config fixes plus defense-in-depth compensating controls; after remediation is applied, replay the exact `PoC` and regression checks to confirm closure before marking `REMEDIATED`.

## Tools and Techniques
- **Source-to-Sink Taint Tracing:** Manually trace untrusted inputs (`HTTP params/headers`, webhooks, file uploads, LLM prompts, DB-stored strings) to dangerous sinks (`SQL`, `OS shell`, `HTML DOM`, `file paths`, `SSRF HTTP clients`, `JWT verify`).
- **Reachability-Adjusted `SCA`:** Verify whether vulnerable transitive library functions are actually imported and reachable with attacker-controlled input before inflating severity.
- **Forensic Evidence Preservation & Redaction:** Record exact timestamps, commit hashes, file:line locations, request/response transcripts, and SHA-256 artifact hashes while masking credentials/tokens (`<REDACTED>`).
- **Regression Security Unit Tests:** Encode every remediated vulnerability as an automated negative test so future commits cannot reintroduce the flaw.

## Verification Requirements
- Zero active probes executed outside documented `RoE` target boundaries.
- Every `Confirmed Vulnerability` includes severity, business/technical impact, exact `file:line` or endpoint, sanitized reproducible evidence, step-by-step reproduction, remediation guidance, and retest verification status.
- Scanner outputs are never dumped raw without manual false-positive and reachability triage.

## Quality Criteria
- **Actionable Engineering Precision:** Remediations specify exact framework-idiomatic fixes (parameterized queries, `CSPRNG` tokens, strict `Content-Security-Policy`, object-level `tenant_id` predicates) rather than generic `"sanitize input"` advice:
  | Finding Classification | Required Evidentiary Bar | Mandatory Report Disposition |
  | :--- | :--- | :--- |
  | `Confirmed Vulnerability` | Reproducible non-destructive `PoC` within authorized `RoE` | Severity + impact + steps + root fix + retest verification |
  | `Potential Finding` | Weak code/config pattern; runtime reachability blocked | Document exact preconditions + defense-in-depth hardening |
  | `False Positive` | Disproven via reachability, escaping, or upstream control | Record technical proof so future audits do not re-triage |
  | `Unverified Observation` | Component inaccessible within current scope/credentials | Mark `NOT VERIFIED`; list exact access needed to evaluate |
- **Zero Collateral Disruption:** Assessment leaves target environments clean, stable, and free of persistent test backdoors or mutated production state.
- **Honest Severity Calibration:** Contextualizes base CVSS scores against real authentication requirements, network exposure, and blast radius.
- **Failure Modes to Avoid:**
  - *Raw Scanner Dumping:* Reporting unverified `grep` or CVE alerts as `CRITICAL` exploits without checking reachability.
  - *Secret Exposure in Evidence:* Copying unredacted JWTs, API keys, or customer PII into vulnerability writeups.
  - *Scope Creep Beyond `RoE`:* Following redirects or DNS CNAMEs onto unapproved third-party/production infrastructure.
  - *Unverified Closure:* Marking a vulnerability `FIXED` after reading a diff without replaying the reproduction `PoC`.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), statutory law, or human authorization gates.
- **Strictly Forbidden Actions:** Unauthorized exploitation, denial-of-service (`DoS`), persistence implants, uncontrolled lateral movement, credential harvesting/exfiltration of real user data, social engineering, or security-control bypass outside explicit `RoE`.
- **Immediate Halt & Escalation:** Stop immediately and alert `SA`, `PM`, and the user if out-of-scope assets, live production instability, or indicators of active real-world compromise are encountered.

## Expected Deliverables
- **Scope & `RoE` Compliance Header** documenting authorized targets, test window, methods, and environment boundaries.
- **Triaged Security Findings Report** separating `Confirmed`, `Potential`, `False Positive`, and `Unverified` items with severity, impact, redacted `PoC` evidence, and reproduction steps.
- **Remediation Patch / Specification & Retest Log** confirming vulnerability closure and regression test coverage.
