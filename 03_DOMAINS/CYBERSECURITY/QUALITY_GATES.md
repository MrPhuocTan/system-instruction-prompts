# Cybersecurity Domain Quality Gates (`CYBERSECURITY`)

- **Domain ID:** `DOM-02-CYBERSECURITY`
- **Gate Enforcement Layer:** Mandatory Pre-Handoff & Pre-Signoff Verification (`DOMAIN_LEAD`, `SA_GATE`, and `PM_GATE`)
- **Normative References:**
  - [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
  - [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md)
  - [INDEPENDENT_VERIFICATION.md](../../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)
  - [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md)

---

## 1. Mandatory 8-Gate Cybersecurity Verification Matrix

No cybersecurity deliverable, code remediation, detection rule, forensic report, penetration test report, architecture review, or compliance matrix may receive `PASS` unless every applicable gate below is satisfied with objective evidence.

| Gate ID | Gate Name | Mandatory Pass Criteria | Automatic `BLOCKED` / `FAILED` Trigger |
| :--- | :--- | :--- | :--- |
| `CYB-GATE-01` | **Authorization, Scope & RoE Gate** | Explicit user authorization, verified asset scope (`IP/CIDR`, FQDN, repo, cloud account), permitted techniques, and non-destructive `RoE` constraints are confirmed and logged prior to any active probing. | Any active network scan, exploit attempt, or credential test executed without documented authorization or against out-of-scope targets. |
| `CYB-GATE-02` | **Evidence Integrity & Redaction Gate** | Artifacts include exact file/line references, `UTC` (`ISO-8601`) timestamps, command/query inputs, and `SHA-256` hashes (for DFIR/binaries). `100%` of live secrets, tokens, hashes, keys, and PII/PHI are masked. | Any cleartext secret, live session token, private key, customer credential, or unredacted PII/PHI appears in reports, PoCs, or logs. |
| `CYB-GATE-03` | **Epistemic Classification & Reproducibility Gate** | Every item is strictly classified as **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**, accompanied by deterministic step-by-step reproduction instructions. | Raw scanner dumps presented without manual taint/reachability triage, or speculative hypotheses labeled as confirmed vulnerabilities. |
| `CYB-GATE-04` | **Severity & Contextual Risk Scoring Gate** | Findings include a valid `CVSS v3.1` or `CVSS v4.0` vector string paired with environmental/contextual risk factors (asset criticality, exposure boundary, `CISA KEV` / `EPSS` exploitability, compensating controls). | Arbitrary `Critical/High/Medium/Low` labels assigned without transparent scoring vectors or architectural exposure justification. |
| `CYB-GATE-05` | **Technical & Business Impact Analysis Gate** | Impact explicitly documents violated trust boundaries, `CIA` triad consequences (Confidentiality, Integrity, Availability), blast radius, privilege level gained, and regulatory/operational exposure. | Generic boilerplate impact statements disconnected from the target system's actual data sensitivity, tenancy model, or architecture. |
| `CYB-GATE-06` | **Actionable Root-Cause Remediation Gate** | Remediations provide concrete code diffs, IaC patches, IAM policies, or architectural controls addressing the root cause, preserving functional behavior, and avoiding brittle blacklists or WAF-only band-aids. | Vague advice (e.g., `"sanitize input"` or `"improve firewall rules"`) without implementation-ready specifications or operational trade-off analysis. |
| `CYB-GATE-07` | **Retest Verification & Regression Gate** | Post-remediation retesting executes both the original attack/negative test case (proving mitigation) and valid functional journeys (proving zero regression), plus automated regression tests or detection rules. | Claiming a vulnerability is remediated based solely on code edits or build compilation without re-executing the verification test (`tool success != fix verified`). |
| `CYB-GATE-08` | **Separation-of-Duties & Runtime Honesty Gate** | Level 3–4 engagements enforce builder/breaker/auditor independence per [DOMAIN_INDEX.md](./DOMAIN_INDEX.md). Unavailable runtime tools or offline targets are disclosed honestly as `NOT VERIFIED`. | Self-certified compliance/pentest sign-off by control authors on Level 3–4 work, or fabricated scan/SIEM/exploit outputs. |

---

## 2. Sub-Discipline Specific Verification Thresholds

1. **Secure Architecture & AppSec (`ROLE-CYB-001`, `ROLE-CYB-002`):**
   - Data-flow diagrams enumerate all trust boundaries, authentication/authorization enforcement points, cryptographic algorithms/key lifecycles, and fail-closed defaults.
   - Code remediations pass deterministic unit/integration suites, static analyzers, codebase-wide variant checks, and dependency lockfile audits without introducing regressions.
2. **Authorized Offensive Security (`ROLE-CYB-003`, `ROLE-CYB-004`):**
   - `100%` of offensive actions map to scoped targets and authorized `RoE` windows.
   - Timestamped `UTC` operator action/IOC manifests and verified post-engagement artifact cleanup attestations are attached.
3. **SOC Detection, Threat Intel & DFIR (`ROLE-CYB-005`, `ROLE-CYB-006`, `ROLE-CYB-007`, `ROLE-CYB-008`):**
   - Detection rules (`Sigma`/`YARA`/`KQL`/`SPL`) syntax-validate cleanly, document expected true-positive triggers (`MITRE ATT&CK` IDs) and false-positive exclusions, and embed SOC triage runbooks.
   - Threat intelligence cites `Admiralty`-graded primary sources, defangs malicious indicators, and marks `TLP 2.0` dissemination boundaries.
   - DFIR timelines normalize all timestamps to `UTC`, detect clock skew/timestomping, verify pre/post `SHA-256` chain-of-custody hashes, and sequence containment prior to adversary tip-off.
4. **Cloud, Network & IAM (`ROLE-CYB-009`, `ROLE-CYB-010`, `ROLE-CYB-011`):**
   - IaC/policy configurations eliminate wildcard `*` privilege escalations, enforce `TLS 1.3`/`mTLS` and `KMS` encryption, block unauthorized egress/metadata (`IMDSv2`), and include break-glass/lockout rollback plans.
5. **GRC & Privacy Engineering (`ROLE-CYB-012`, `ROLE-CYB-013`):**
   - Control mappings cite exact clause/control IDs (`NIST SP 800-53`, `ISO 27001`, `SOC 2`, `PCI-DSS v4.0`, `GDPR` Articles, `NIST Privacy Framework`).
   - Residual risk acceptances, `SoA` exclusions, and legal/DPIA sign-offs are routed strictly to designated human authorities.

---

## 3. Canonical Gate Disposition Semantics

- **`PASS`:** All applicable `CYB-GATE-01` through `CYB-GATE-08` checks verified with empirical, redacted evidence.
- **`PARTIAL`:** Core analysis or defensive controls verified, while secondary retests or environment-dependent checks remain pending (`NOT VERIFIED` items itemized).
- **`BLOCKED`:** Missing written authorization, unverified target scope, ambiguous `RoE`, out-of-scope redirect, or pending mandatory Human Approval Gate.
- **`FAILED`:** Safety/redaction violation, unmitigated regression, unverified/fabricated evidence, or broken security control implementation.
- **`NOT VERIFIED`:** Check could not execute due to absent tooling, credentials, logs, or live environment; disclosed transparently with manual verification commands provided.
