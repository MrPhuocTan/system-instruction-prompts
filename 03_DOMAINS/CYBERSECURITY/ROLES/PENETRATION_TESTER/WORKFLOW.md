# Practitioner Workflow — Penetration Tester (`ROLE-CYB-003`)

- **Role:** `PENETRATION_TESTER` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [API_TESTING](../../../../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md)

---

## Step 1: Pre-Engagement Authorization, Scope & RoE Verification (Hard Gate)
1. Inspect workspace engagement manifests or query the user via `ask_question` to confirm written **authorization**, exact target **scope** (`IP/CIDR`, FQDNs, URI paths, dedicated test tenants/accounts), excluded endpoints (billing/SMS gateways), rate limits, and emergency stop contacts under the **Rules of Engagement (`RoE`)**.
2. If authorization or target ownership is missing or ambiguous, **halt** immediately and restrict work to passive static review if authorized.
3. Initialize a timestamped `UTC` operator activity log recording every command, target endpoint, and test account identifier.

---

## Step 2: Scoped Enumeration & Attack-Surface Mapping
1. Resolve target hosts and verify IP/CNAME ownership stays strictly inside authorized boundaries (exclude shared third-party SaaS/CDNs unless explicitly authorized).
2. Enumerate exposed services, TLS configurations, HTTP security headers, API schemas (`OpenAPI`, `GraphQL`), authentication flows, role matrices (`Admin`, `Member`, `Read-Only`, `Anonymous`, `Tenant A` vs `Tenant B`), and state-changing business endpoints.

---

## Step 3: Controlled Vulnerability Discovery & Non-Destructive PoC Validation
1. Test high-impact vulnerability classes systematically per `OWASP WSTG` and `OWASP API Security Top 10`:
   - **Access Control Matrix:** Replay authenticated requests across Test Tenant A and Test Tenant B tokens (`BOLA`/`IDOR`) and lower-privileged roles (`BFLA`).
   - **Auth & Session Flows:** Test token signature/claim validation, refresh rotation, MFA step-up enforcement, OAuth redirect URI validation, and password-reset token entropy.
   - **Injection, SSRF & Parsing:** Probe inputs with **non-destructive**, sleep-free boolean/syntax/canary indicators; never execute destructive SQL, OS mutation commands, or uncontrolled outbound connections.
   - **Business-Logic Abuse:** Test state-transition skipping, negative/boundary numeric inputs, mass assignment, and low-concurrency race conditions on synthetic test balances.
2. Immediately **halt** and **escalate** if target instability, real customer PII exposure, or signs of an unauthorized real-world attacker appear.

---

## Step 4: Triage, Chaining, Redaction & Severity Scoring
1. Eliminate scanner false positives; classify findings strictly into **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.
2. Redact `100%` of tokens, secrets, cookies, and sensitive payloads in captured HTTP/CLI transcripts.
3. Score findings with `CVSS v3.1/v4.0` vectors and contextual blast-radius analysis, and author root-cause remediation specifications.

---

## Step 5: Environment Cleanup, Retest Verification & Handoff
1. Delete synthetic canary objects, revoke temporary test sessions, and verify target health matches pre-test baseline.
2. Upon remediation delivery, execute **retest** verification against original PoCs plus bypass permutations (HTTP verb tampering, JSON/form content-type switching, path normalization).
3. Finalize [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the redacted penetration test report and activity manifest.
