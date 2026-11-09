# Quality Checklist — Blue Team / SOC Detection Engineer (`ROLE-CYB-005`)

Verify all items before handoff and `SA_GATE` review, aligned with [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope & Non-Destructive Validation (`RoE`)
- [ ] Log dataset/environment **scope**, telemetry privacy rules, and **authorization** / **Rules of Engagement (`RoE`)** were verified prior to querying logs or replaying atomic test events.
- [ ] All detection validation remained strictly **non-destructive**; SOAR playbooks enforce explicit human approval gates before host isolation, account suspension, or firewall blocks.
- [ ] Independence from blind `RED_TEAM_OPERATOR` campaigns was maintained where applicable.

---

## 2. Detection Engineering Rigor & Telemetry Mapping
- [ ] Every detection rule (`Sigma`, `YARA`, `Suricata`, `KQL`, `SPL`) specifies exact log-source prerequisites (event IDs, audit flags, `OCSF`/`ECS` fields), `MITRE ATT&CK` (`TAxxxx`/`Txxxx.xxx`), and `MITRE D3FEND` mappings.
- [ ] Rule logic targets behavioral invariants rather than brittle single-use IP/filename indicators.
- [ ] False-positive exclusions bind signed binary hash, parent lineage, and service account rather than overly broad directory/filename wildcards.
- [ ] Rules syntax-validate cleanly and were tested against both positive (malicious behavior) and negative (benign admin baseline) event fixtures.

---

## 3. Epistemic Classification, Triage Evidence & Redaction
- [ ] Log hunt and alert findings are strictly classified into **Confirmed Vulnerability** (or Confirmed Security Event), **Potential Finding** (telemetry blind spot / anomalous indicator), **False Positive**, or **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings pair `CVSS` / alert priority with asset criticality and attacker kill-chain stage.
- [ ] Timelines normalize all log sources to `UTC` (`ISO-8601`) and note any clock-skew or missing log-ingestion windows.
- [ ] `100%` of command-line secrets, bearer tokens, cookies, API keys, and employee/customer PII are redacted across log samples and rule test fixtures.

---

## 4. Actionable SOC Runbooks, Remediation & Retest Guidance
- [ ] Each detection includes a concrete Tier-1/Tier-2 triage runbook (enrichment queries, benign vs. malicious decision tree, severity logic, and `INCIDENT_RESPONSE` escalation criteria).
- [ ] Telemetry gaps specify exact audit-policy/logging configuration remediations and deterministic **retest** steps (benign atomic event replay) confirming end-to-end alert delivery.
