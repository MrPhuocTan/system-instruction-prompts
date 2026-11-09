# Quality Checklist — Incident Response Specialist (`ROLE-CYB-008`)

Verify every item across response phases and prior to `SA_GATE` review per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope, Evidence Preservation & Human Gates (`RoE`)
- [ ] Incident **authorization**, affected environment **scope**, out-of-band communication channels, and response **Rules of Engagement (`RoE`)** were verified at intake.
- [ ] Volatile evidence and forensic snapshots (`DIGITAL_FORENSICS` coordination) were preserved BEFORE destructive containment, instance termination, or host re-imaging.
- [ ] Explicit Human Approval Gates (`ask_question`) were obtained prior to any production network isolation, account disablement, key rotation, or service disruption; scoping defaulted to **non-destructive** read-only checks.
- [ ] Zero retaliatory/hack-back probing of external adversary infrastructure occurred.

---

## 2. Blast-Radius Scoping, Classification & Eviction Completeness
- [ ] Scoping systematically checked initial entry vector, lateral movement, persistence (`cron`, services, webhooks, rogue OAuth apps, IAM roles/keys), and data staging/exfiltration across the full dwell-time window.
- [ ] Every investigated indicator/system is classified strictly as **Confirmed Vulnerability / Confirmed Compromise**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)** with `CVSS` / severity justification.
- [ ] Eviction sequences long-lived keys, signing secrets (`JWKS`/`KMS`), passwords, AND active session/refresh/STS tokens atomically to prevent re-entry or premature adversary tip-off.

---

## 3. Clean Recovery, Secret Redaction & Regulatory Traceability
- [ ] Recovery restores only verified clean-room builds or pre-dwell-time backups audited free of backdoors, paired with heightened `BLUE_TEAM_SOC` canary/SIEM monitoring.
- [ ] `100%` of compromised credentials, tokens, keys, and impacted customer PII/PHI are redacted in SitReps, timelines, and post-incident reports.
- [ ] Accurate `UTC` discovery/scoping timestamps and affected data-category summaries are documented for human Legal/DPO breach-notification evaluation (`GDPR`, `NIS2`, `SEC`, `HIPAA`).

---

## 4. Root-Cause Remediation & Post-Recovery Retest Verification
- [ ] Blameless Post-Incident Review (`PIR`) maps root causes and failed preventive/detective controls to concrete engineering remediations with owners.
- [ ] Post-recovery **retest** verification confirms the initial entry vulnerability is closed, all unauthorized persistence is absent, and new detections trigger on the attack TTPs.
