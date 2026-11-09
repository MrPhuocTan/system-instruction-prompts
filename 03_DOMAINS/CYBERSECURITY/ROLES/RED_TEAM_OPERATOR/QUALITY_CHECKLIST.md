# Quality Checklist — Red Team Operator (`ROLE-CYB-004`)

Verify every item prior to phase transitions, handoff, and `SA_GATE` review per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, White-Cell Deconfliction & RoE Safety
- [ ] Explicit written human **authorization**, signed **Rules of Engagement (`RoE`)**, target enclave **scope** allowlist, prohibited actions, and White Cell emergency deconfliction contacts were verified prior to execution.
- [ ] Mandatory Human Approval Gates were obtained before initiating active adversary emulation or crossing host/privilege boundaries.
- [ ] Operations remained strictly **non-destructive**: zero unapproved persistence, zero ransomware/wiper simulation on real data, zero phishing of unconsented users, and zero live data exfiltration.
- [ ] Separation of duties was maintained from blind `BLUE_TEAM_SOC` evaluators and `SECURITY_GRC` auditors.

---

## 2. MITRE ATT&CK Fidelity & Epistemic Classification
- [ ] Every emulated step maps to exact `MITRE ATT&CK` Tactic (`TAxxxx`) and Technique/Sub-technique (`Txxxx.xxx`) identifiers aligned with a documented threat profile.
- [ ] Every defensive gap or exploitable path is strictly classified as **Confirmed Vulnerability** (or Confirmed Detection Blind Spot), **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings pair `CVSS v3.1/v4.0` vectors with kill-chain blast-radius and crown-jewel reachability context.
- [ ] Detection outcomes clearly distinguish `Prevented/Blocked`, `Alerted & Triaged`, `Telemetry Logged (No Alert)`, and `Zero Telemetry Visibility`.

---

## 3. Telemetry Auditability, Redaction & Teardown Integrity
- [ ] Full `UTC`-timestamped operator action logs (host, PID, command, source IP, `SHA-256` artifact hash) are attached for Blue Team correlation.
- [ ] `100%` of captured credentials, Kerberos/JWT/cloud tokens, keys, and PII are redacted across all narratives and logs.
- [ ] `100%` teardown verification confirms all temporary test binaries, canary files, test IAM roles/tokens, and sessions were removed and verified absent on target hosts.

---

## 4. Purple Team Remediation & Retest Guidance
- [ ] Each blind spot or exploit chain includes concrete preventive hardening controls AND specific telemetry/detection engineering requirements (`MITRE D3FEND` / log source mappings).
- [ ] Atomic Purple Team **retest** steps are documented (and executed where authorized) to prove new prevention controls block the path and SIEM/EDR alerts trigger reliably.
