# Quality Checklist — Cyber Threat Intelligence Analyst (`ROLE-CYB-006`)

Complete all checks prior to dissemination and `SA_GATE` review per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Passive Scope & OPSEC (`RoE`)
- [ ] Collection **scope**, Priority Intelligence Requirements (`PIRs`), `TLP 2.0` handling rules, and passive **Rules of Engagement (`RoE`)** / **authorization** boundaries were verified prior to collection.
- [ ] Collection remained strictly passive and **non-destructive**: zero direct probing of suspected adversary C2 hosts, zero uploading of confidential internal files to public sandboxes, and zero illicit data acquisition.
- [ ] All malicious URLs, FQDNs, IPs, and email indicators are properly defanged (`hxxps://`, `[.]`, `[@]`) to prevent accidental execution or beacon callbacks.

---

## 2. Analytic Tradecraft, Grading & Epistemic Classification
- [ ] Sources are corroborated and graded with the `Admiralty System` (`A1`–`F6`), explicitly distinguishing verified facts from `ICD 203` analytic estimates (`Low` / `Moderate` / `High` confidence).
- [ ] Attribution claims (if any) document Analysis of Competing Hypotheses (`ACH`) across the `Diamond Model` (Adversary, Infrastructure, Capability, Victim) rather than single-indicator assumptions.
- [ ] Adversary behaviors map to exact `MITRE ATT&CK` (`TAxxxx`/`Txxxx.xxx`) IDs.
- [ ] Organizational exposures are classified strictly into **Confirmed Vulnerability**, **Potential Finding**, **False Positive** (shared CDN/cloud IP or unaffected build), or **Unverified (`NOT VERIFIED`)**.

---

## 3. Evidence Quality, TLP Marking & Secret/PII Redaction
- [ ] Deliverables carry explicit `TLP 2.0` markings (`TLP:RED/AMBER+STRICT/AMBER/GREEN/CLEAR`), `UTC` intelligence cutoff timestamps, and IOC expiration/TTL guidance.
- [ ] `100%` of leaked organizational credentials, session tokens, internal keys, and victim PII/PHI are redacted in intelligence briefs and `STIX 2.1` bundles.

---

## 4. Actionable Prioritization, Remediation & Retest Guidance
- [ ] Vulnerability intelligence combines `CVSS v3.1/v4.0`, `CISA KEV` status, `EPSS` score, and internal asset reachability into an actionable remediation priority order.
- [ ] Intelligence outputs translate directly into concrete `BLUE_TEAM_SOC` hunt hypotheses, preventive architectural controls, and deterministic **retest** / validation checks confirming exposure closure.
