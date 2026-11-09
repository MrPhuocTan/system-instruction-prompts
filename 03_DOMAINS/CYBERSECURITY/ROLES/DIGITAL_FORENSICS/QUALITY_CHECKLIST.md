# Quality Checklist — Digital Forensics Specialist (`ROLE-CYB-007`)

Verify every item prior to handoff and `SA_GATE` sign-off per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope, Chain-of-Custody & Host Safety (`RoE`)
- [ ] Custodial/legal **authorization**, target evidence **scope**, legal-hold/privacy boundaries, and forensic **Rules of Engagement (`RoE`)** were verified prior to acquisition or inspection.
- [ ] Examination was strictly read-only and **non-destructive**: `SHA-256` hashes of all evidence artifacts were recorded prior to inspection and re-verified identical (`0` mutations) post-examination.
- [ ] Order of Volatility (`RFC 3227` / `ISO/IEC 27037`) was respected, and zero untrusted binaries, scripts, or payloads were executed on the host runtime.
- [ ] Forensic custodian separation of duties from destructive remediation/rebuilds was preserved on Level 3–4 investigations.

---

## 2. Multi-Artifact Timeline Rigor & Epistemic Classification
- [ ] All timeline events are normalized to `UTC` (`ISO-8601`), accounting for source timezone settings, NTP clock skew, and anti-forensic timestomping (`$SI` vs `$FN` MFT checks / log-clear events).
- [ ] Intrusion and root-cause conclusions cross-corroborate multiple independent artifact sources (filesystem, execution metadata, auth logs, network/cloud telemetry).
- [ ] Findings strictly distinguish **Confirmed Vulnerability / Confirmed Intrusion Artifact**, **Potential Finding**, **False Positive** (benign OS/admin artifact), and **Unverified (`NOT VERIFIED` — missing volatile/log data)**, paired with severity context.

---

## 3. Evidence Reproducibility & Credential/PII Redaction
- [ ] Every finding documents exact evidence source hash, file path/inode/event record ID, parser command used, and reproducible analytical output.
- [ ] `100%` of recovered cleartext credentials, private keys, bearer tokens, cookies, and regulated PII/PHI are redacted in reports and timelines (referencing redacted `SHA-256` digests where correlation is needed).

---

## 4. Actionable DFIR Handoff, Remediation & Retest Guidance
- [ ] Defanged IOCs, persistence mechanisms, and root-cause entry vectors are packaged cleanly for `INCIDENT_RESPONSE` eradication and `BLUE_TEAM_SOC` `YARA`/`Sigma` detection rules.
- [ ] Root-cause remediation and post-recovery forensic **retest** / clean-state verification criteria (confirming zero residual persistence or unauthorized accounts) are explicitly specified.
