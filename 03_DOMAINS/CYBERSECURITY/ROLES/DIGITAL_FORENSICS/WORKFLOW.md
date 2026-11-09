# Practitioner Workflow — Digital Forensics Specialist (`ROLE-CYB-007`)

- **Role:** `DIGITAL_FORENSICS` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Custodial Authorization, Scope & Chain-of-Custody Intake
1. Confirm written **authorization**, investigative **scope** (hosts, containers, cloud accounts, time window), legal-privilege/privacy constraints, and **Rules of Engagement (`RoE`)** (**non-destructive**, read-only handling).
2. Establish the Chain-of-Custody (`CoC`) ledger recording artifact provenance, acquisition `UTC` timestamp, byte size, and baseline `SHA-256` digest (`shasum -a 256`).
3. Guide live responders to capture volatile state (`RFC 3227`: memory, open sockets, process trees, ephemeral container diffs) before host reboot or termination.

---

## Step 2: Read-Only Working Copy & Integrity Verification
1. Operate exclusively on working copies or read-only mounts (`sqlite3 -readonly`, non-mutating parsers); never modify original evidence files.
2. Check for anti-forensic tampering upfront:
   - Truncated or cleared logs (`Event ID 1102`/`104`, missing journal sequence numbers).
   - NTP clock skew and filesystem metadata discrepancies (`$STANDARD_INFORMATION` vs `$FILE_NAME` timestamps).

---

## Step 3: Multi-Source Artifact Extraction & Static Malware Triage
1. Parse host, identity, and cloud artifacts systematically (`EVTX`, `auditd`, systemd journals, Registry/LaunchDaemons/cron persistence, shell histories, SSH artifacts, CloudTrail/VPC Flow logs) via read-only CLI/Python scripts.
2. Perform strictly **static** triage on suspect scripts/binaries (file magic, `SHA-256`, ELF/PE/Mach-O headers, imported symbols, deobfuscated strings, `YARA` rules)—NEVER execute untrusted code on the host.
3. Immediately **halt** and **escalate** to [INCIDENT_RESPONSE](../INCIDENT_RESPONSE/SYSTEM_PROMPT.md), `SA`, `PM`, and the user if active ongoing data exfiltration, out-of-scope third-party data, or legally restricted material is encountered.

---

## Step 4: `UTC` Super-Timeline Reconstruction & Classification
1. Fuse correlated events into a single `UTC` (`ISO-8601`) super-timeline mapped to `MITRE ATT&CK` (`Initial Access`, `Execution`, `Persistence`, `Privilege Escalation`, `Lateral Movement`, `Collection/Exfiltration`).
2. Classify each hypothesis and exposure strictly into **Confirmed Vulnerability / Confirmed Artifact**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**, redacting `100%` of secrets, tokens, and PII/PHI.

---

## Step 5: Post-Analysis Hash Re-Verification, Handoff & Clean-State Retest
1. Re-compute `SHA-256` hashes on all original evidence items to prove unbroken integrity (`pre-hash == post-hash`).
2. Package defanged IOCs, `YARA` rules, and persistence artifact locations for `INCIDENT_RESPONSE` and `BLUE_TEAM_SOC`.
3. Define post-eradication forensic **retest** verification criteria confirming zero residual persistence or unauthorized accounts remain.
4. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the forensic report and Chain-of-Custody ledger.
