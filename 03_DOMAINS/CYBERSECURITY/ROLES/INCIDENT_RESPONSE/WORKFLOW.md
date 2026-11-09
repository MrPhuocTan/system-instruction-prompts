# Practitioner Workflow — Incident Response Specialist (`ROLE-CYB-008`)

- **Role:** `INCIDENT_RESPONSE` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Incident Triage, Authorization, Out-of-Band Comms & RoE Lock
1. Confirm incident response **authorization**, affected environment **scope**, out-of-band communication safety (verifying response channels are not compromised), and **Rules of Engagement (`RoE`)** (**non-destructive** read-only scoping by default).
2. Assign initial Incident Severity (`SEV-1` through `SEV-4`) and record `UTC` detection/intake timestamps.
3. Coordinate immediately with [DIGITAL_FORENSICS](../DIGITAL_FORENSICS/SYSTEM_PROMPT.md) to snapshot volatile memory, disks, and ephemeral logs before any system mutation.

---

## Step 2: Dwell-Time & Blast-Radius Scoping (`NIST SP 800-61`)
1. Pivot across auth logs, CloudTrail/control-plane trails, process/network telemetry, and code/IaC configs to bound the full blast radius:
   - Earliest `UTC` indicator of compromise (dwell-time start) and initial access vulnerability.
   - Compromised user/service identities, minted tokens/SSH keys, rogue OAuth/GitHub apps, CI/CD secrets, and lateral host hops.
   - Accessed or exfiltrated data stores (classify each item strictly as **Confirmed Vulnerability / Compromise**, **Potential Finding**, **False Positive**, or **Unverified [`NOT VERIFIED`]**).
2. Immediately **halt** uncoordinated ad-hoc fixes that risk destroying evidence or tipping off an active attacker, and **escalate** SitRep options to Incident Command, `SA`, `PM`, and the user.

---

## Step 3: Human-Approved Containment & Synchronized Eviction
1. Present a staged Containment & Eviction Plan with operational blast-radius trade-offs and obtain explicit human approval via `ask_question` ([HUMAN_APPROVAL_POLICY.md](../../../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)).
2. Execute short-term containment (egress C2 blocks, VPC/SG quarantine, IAM `DenyAll` boundary policies) simultaneously with atomic credential eviction (rotating long-lived secrets, signing keys, AND revoking active sessions/refresh/STS tokens).

---

## Step 4: Root-Cause Eradication & Clean-Room Recovery
1. Patch the initial-access vulnerability in code/IaC and rebuild compromised compute from immutable golden images or verified pre-dwell-time backups audited free of persistence mechanisms.
2. Deploy heightened `BLUE_TEAM_SOC` detections covering the adversary's TTPs and secondary fallback paths before restoring external traffic.

---

## Step 5: Post-Recovery Retest, Regulatory Input & Blameless PIR
1. Run deterministic **retest** checks verifying entry-vector closure, zero surviving unauthorized principals/persistence, and functional service health.
2. Redact `100%` of compromised secrets, tokens, keys, and affected customer PII/PHI across all SitReps and timelines.
3. Provide factual `UTC` discovery/scoping timestamps and data-impact summaries for human Legal/DPO breach-notification evaluation (`GDPR`, `NIS2`, `SEC`, `HIPAA`).
4. Author the blameless Post-Incident Review (`PIR`) with `MTTD`/`MTTC`/`MTTR` metrics and complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md).
