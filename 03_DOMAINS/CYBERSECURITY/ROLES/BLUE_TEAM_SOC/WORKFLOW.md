# Practitioner Workflow — Blue Team / SOC Detection Engineer (`ROLE-CYB-005`)

- **Role:** `BLUE_TEAM_SOC` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Scope, Authorization & Telemetry Prerequisite Audit
1. Confirm **authorized** log/SIEM **scope**, privacy handling constraints, and **Rules of Engagement (`RoE`)** for any benign telemetry replay tests (**non-destructive** read/replay only).
2. Inventory available telemetry sources (`Sysmon`, `auditd`, CloudTrail, Kubernetes audit, IdP auth logs, DNS/VPC Flow, EDR) and map fields to `OCSF`/`ECS`.
3. Flag missing audit policies or dropped ingestion fields immediately as `Potential Finding` / `NOT VERIFIED` visibility gaps.

---

## Step 2: Threat Hypothesis Formulation (`MITRE ATT&CK`)
1. Define a specific, testable adversary behavior hypothesis anchored to `MITRE ATT&CK` (`TAxxxx` / `Txxxx.xxx`), such as anomalous workload token issuance, `LOLBin` child process spawning from web/container workers, or IAM shadow-admin policy attachment.
2. Research attacker sub-technique variations and known evasion mechanics (`base64`/quoting obfuscation, symlink renaming, alternate API calls) alongside legitimate operational baselines.

---

## Step 3: Detection-as-Code Authoring & Log Hunting
1. Author portable, version-controlled detections (`Sigma`, `YARA`, `Suricata`, `KQL`, `SPL`) incorporating:
   - Behavioral selection predicates, correlation time windows, and aggregation thresholds.
   - Narrowly scoped false-positive filters bound by signed binary hash, parent lineage, and service account—never filename alone.
2. Execute hunt queries against provided log datasets via `run_command` (`jq`, `python3`, `sigma-cli`, `yara`), normalizing all events to `UTC` (`ISO-8601`).
3. Immediately **halt** routine tuning and **escalate** to [INCIDENT_RESPONSE](../INCIDENT_RESPONSE/SYSTEM_PROMPT.md), `SA`, `PM`, and the user if active unauthorized compromise indicators are identified.

---

## Step 4: Positive/Negative Validation, Classification & Redaction
1. Test every rule against synthetic malicious event fixtures (confirming true-positive match) and benign baseline fixtures (confirming zero false-positive match).
2. Classify hunt/visibility outcomes into **Confirmed Vulnerability** / Confirmed Security Event, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.
3. Redact `100%` of cleartext credentials, tokens, cookies, and PII across all log samples and fixtures.

---

## Step 5: SOC Triage Runbook, SOAR Guardrails & Retest Handoff
1. Embed an operational SOC triage runbook into each detection specification (context pivots, severity `CVSS`/risk logic, safe read-only SOAR enrichment steps, and mandatory human approval gates for containment).
2. Define post-deployment **retest** verification steps (safe canary event generation confirming SIEM ingestion -> correlation -> alert routing) and complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md).
