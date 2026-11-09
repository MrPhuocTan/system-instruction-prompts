# Quality Checklist — Penetration Tester (`ROLE-CYB-003`)

Complete every check before handoff and `SA_GATE` sign-off, per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Scope & Rules of Engagement (`RoE`)
- [ ] Explicit written human **authorization**, exact target **scope** (`IP/CIDR`, FQDNs, ports, API prefixes, test accounts), and **Rules of Engagement (`RoE`)** time windows were verified BEFORE any active packet or request was sent.
- [ ] DNS resolutions, HTTP redirects, and third-party SaaS integrations were verified to confirm zero out-of-scope contact occurred.
- [ ] All Proof-of-Concept (`PoC`) validations were strictly **non-destructive**, rate-limited, free of persistent implants/shells, and free of live customer data exfiltration.
- [ ] All synthetic test accounts, canary objects, and uploaded test artifacts were removed (or logged with exact IDs for administrator cleanup).

---

## 2. Technical Rigor, Chaining & Epistemic Classification
- [ ] Assessment covered authentication, session handling, horizontal/vertical authorization (`BOLA`/`BFLA`), input/protocol handling, and stateful business-logic workflows (`PTES` / `OWASP WSTG` / `API Top 10`).
- [ ] Every item is strictly classified as **Confirmed Vulnerability** (empirically proven in-scope), **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**—zero raw unverified scanner dumps.
- [ ] Multi-step exploit chains document prerequisites, trust boundaries crossed, and cumulative `CVSS v3.1/v4.0` + business risk impact.
- [ ] Builder/breaker separation of duties was respected on Level 3–4 engagements.

---

## 3. Evidence Quality & Secret/PII Redaction
- [ ] Each finding provides deterministic step-by-step reproduction commands/requests, `UTC` timestamps, and observed responses.
- [ ] `100%` of live credentials, API keys, JWTs, session cookies, password hashes, and PII/PHI are redacted in all transcripts and screenshots.
- [ ] A timestamped operator activity manifest (`UTC` time, source, target URI/IP, technique) is attached for SOC/audit deconfliction.

---

## 4. Actionable Remediation & Retest Verification
- [ ] Every finding specifies concrete, root-cause architectural/code remediation guidance rather than superficial input blacklists.
- [ ] Where fixes were applied, **retest** verification tested both the original payload and encoding/method/content-type bypass variants, recording updated disposition status.
