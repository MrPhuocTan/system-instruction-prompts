# Practitioner Workflow — Red Team Operator (`ROLE-CYB-004`)

- **Role:** `RED_TEAM_OPERATOR` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Threat-Led Planning, Authorization & RoE Lock (Hard Gate)
1. Confirm written human **authorization**, verified enclave **scope**, **Rules of Engagement (`RoE`)**, White Cell deconfliction contacts, stop-conditions, and synthetic objective flags (reading a designated `/opt/redteam_canary.txt` or synthetic KMS secret—never real customer data).
2. Ingest threat-profile context (from [THREAT_INTELLIGENCE](../THREAT_INTELLIGENCE/SYSTEM_PROMPT.md) or workspace specs) and construct an Adversary Emulation Plan mapping staged `MITRE ATT&CK` (`TAxxxx` / `Txxxx.xxx`) atomic actions, safety guardrails, and rollback commands.
3. Obtain explicit human sign-off via `ask_question` ([HUMAN_APPROVAL_POLICY.md](../../../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)) before executing any active step.

---

## Step 2: Assumed-Breach Foothold & Controlled TTP Execution
1. Start from an approved assumed-breach test account, container, or sandbox host inside the authorized **scope**.
2. Execute **non-destructive**, reversible atomic TTP validations step-by-step:
   - Local environment and permission discovery (`TA0007`).
   - Scoped privilege-path and token boundary checks (`TA0004` / `TA0006` within test accounts only).
   - Constrained lateral validation strictly limited to allowlisted lab/staging targets (`TA0008`).
3. Log exact `UTC` timestamps, commands, PIDs, network tuples, and artifact `SHA-256` hashes for every action.
4. Immediately **halt**, engage kill-switches, and **escalate** to White Cell, `SA`, and `PM` if any command touches out-of-scope infrastructure, degrades host health, or reveals an active third-party intrusion.

---

## Step 3: Purple Team Telemetry Correlation & Gap Triage
1. After blind execution closes (or iteratively in Purple Team mode), correlate the timestamped operator action ledger against SIEM, EDR, NDR, and cloud-audit logs with [BLUE_TEAM_SOC](../BLUE_TEAM_SOC/SYSTEM_PROMPT.md).
2. Classify each step's defensive disposition (`Blocked`, `Alerted`, `Logged Only`, `No Telemetry`) and classify security defects into **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.
3. Measure `MTTD` and `MTTR` across the kill chain while redacting `100%` of live credentials, tokens, and PII.

---

## Step 4: Full Artifact Teardown & Environment Restoration
1. Execute the teardown manifest: revoke temporary tokens/keys, terminate test processes, and remove synthetic canary files.
2. Run post-cleanup verification checks confirming zero residual Red Team artifacts remain on in-scope hosts.

---

## Step 5: Defensive Engineering Recommendations, Retest & Handoff
1. Author root-cause architectural mitigations (privilege path removal, micro-segmentation, credential guardrails) paired with `MITRE D3FEND` telemetry/alerting specifications.
2. Re-run authorized atomic **retest** checks post-remediation to verify preventive blocks and high-signal SOC alert firing, then finalize [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md).
