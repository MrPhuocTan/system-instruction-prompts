# Practitioner Workflow — Cyber Threat Intelligence Analyst (`ROLE-CYB-006`)

- **Role:** `THREAT_INTELLIGENCE` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Direction, PIR Definition & Passive RoE Verification
1. Confirm Priority Intelligence Requirements (`PIRs`), organizational technology stack **scope**, and `TLP 2.0` dissemination boundaries.
2. Verify passive-only **Rules of Engagement (`RoE`)** and **authorization** constraints (**non-destructive**, zero active external probing, zero confidential file uploads to public services).
3. Establish an explicit `UTC` intelligence cutoff timestamp for the assessment.

---

## Step 2: Primary-Source Collection & Indicator Normalization
1. Collect authoritative public advisories (`NVD`/`CVE`, `CISA KEV`, `FIRST EPSS`, vendor PSIRT bulletins, CERT/ISAC reports) via `search_web` and correlate against local workspace inventories/SBOMs/logs via `read_file` (record unavailable commercial feeds honestly as `NOT VERIFIED`).
2. Normalize observables into structured `STIX 2.1` or tabular schemas:
   - Vet IPs/domains against shared-infrastructure false positives (CDNs, public DNS resolvers, cloud NAT gateways).
   - Defang every malicious indicator (`hxxps://`, `[.]`, `[@]`).
3. Immediately **halt** routine reporting and **escalate** to [INCIDENT_RESPONSE](../INCIDENT_RESPONSE/SYSTEM_PROMPT.md), `SA`, `PM`, and the user if active internal beacon matches or leaked live organizational credentials are discovered.

---

## Step 3: Diamond Model, MITRE ATT&CK & Competing-Hypothesis Analysis
1. Map adversary behaviors to exact `MITRE ATT&CK` Tactics (`TAxxxx`) and Sub-techniques (`Txxxx.xxx`), prioritizing durable TTPs over short-lived file hashes.
2. Evaluate campaign clustering and attribution via the `Diamond Model` and Analysis of Competing Hypotheses (`ACH`), grading every source with the `Admiralty Scale` (`A1`–`F6`) and applying `ICD 203` estimative confidence levels.
3. Classify internal organizational exposure items strictly as **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**, redacting `100%` of credentials and PII.

---

## Step 4: Risk-Based Vulnerability & Control Prioritization
1. Synthesize `CVSS v3.1/v4.0` severity, `CISA KEV` active-exploitation status, `EPSS` probability, PoC weaponization maturity, and internal asset internet-reachability into a deterministic remediation SLA queue.
2. Translate TTP findings into behavioral threat-hunting hypotheses for [BLUE_TEAM_SOC](../BLUE_TEAM_SOC/SYSTEM_PROMPT.md) and structural mitigations for engineering owners.

---

## Step 5: Dissemination, Retest Criteria & Feedback Loop
1. Apply `TLP 2.0` headers, IOC expiration TTLs, and deterministic **retest** / validation criteria (SBOM version verification + SIEM retrospective hunt confirmation).
2. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the structured intelligence package.
