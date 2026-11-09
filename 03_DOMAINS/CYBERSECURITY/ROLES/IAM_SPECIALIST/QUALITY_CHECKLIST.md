# Quality Checklist — Identity and Access Management Specialist (`ROLE-CYB-011`)

Verify every item prior to handoff and `SA_GATE` sign-off per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, Tenant Scope & Lockout Safety (`RoE`)
- [ ] Target IdP/cloud/application identity **scope** and **authorization** / **Rules of Engagement (`RoE`)** were verified prior to inspection or testing.
- [ ] All checks were strictly **non-destructive**: zero credential brute-forcing/lockouts, zero unauthorized live user impersonation, and explicit Human Approval Gates required prior to live IdP/IAM cutovers.
- [ ] Break-glass emergency admin exclusions, hardware-MFA custody, and rollback procedures were verified to prevent organizational self-lockout.
- [ ] Builder/auditor separation of duties was respected on Level 3–4 engagements.

---

## 2. Authentication, Federation & Authorization Rigor
- [ ] `OAuth 2.1` / `OIDC` / `SAML 2.0` flows enforce `PKCE` (`S256`), exact `redirect_uri` allowlists, `state`/`nonce` validation, XML signature-wrapping (`XSW`) defenses, and phishing-resistant `FIDO2/WebAuthn` MFA (`NIST SP 800-63` `AAL2`/`AAL3`).
- [ ] Token & session controls enforce asymmetric `JWKS` verification (`alg`, `iss`, `aud`, `exp`), short access-token TTLs, refresh-token rotation + reuse detection, and `HttpOnly; Secure; SameSite` cookie attributes.
- [ ] Transitive IAM privilege-escalation graph paths (`iam:PassRole`, policy mutation, OAuth app consent, group-write shadow admins) and cross-tenant `RBAC`/`ABAC`/`ReBAC` boundaries were audited.

---

## 3. Epistemic Classification, Scoring & Secret Redaction
- [ ] Findings strictly distinguish **Confirmed Vulnerability**, **Potential Finding**, **False Positive** (blocked by permission boundary/`SCP`), and **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings pair `CVSS v3.1/v4.0` vectors with privilege-escalation blast-radius context.
- [ ] `100%` of OAuth client secrets, private signing keys, live JWTs/SAML assertions, password hashes, and directory PII are redacted.

---

## 4. Policy-as-Code Remediation & Retest Verification
- [ ] Least-privilege IAM policies and `OPA/Rego` or `Cedar` authorization rules scope `Action`, `Resource`, and `Condition` explicitly, eliminating standing wildcard privileges (`JIT`/`ZSP`).
- [ ] Deterministic **retest** unit/integration matrices verify unauthorized cross-tenant and escalation requests return `Deny` (`403`) while valid role workflows succeed.
