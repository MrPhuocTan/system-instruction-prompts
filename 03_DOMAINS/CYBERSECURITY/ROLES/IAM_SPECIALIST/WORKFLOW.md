# Practitioner Workflow — Identity and Access Management Specialist (`ROLE-CYB-011`)

- **Role:** `IAM_SPECIALIST` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [SECURITY_ASSESSMENT](../../../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) | [API_TESTING](../../../../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md)

---

## Step 1: Identity Scope, Authorization & Principal Inventory
1. Confirm **authorized** identity directories, cloud IAM repositories, application auth modules, and **Rules of Engagement (`RoE`)** (**non-destructive** static/sandbox verification by default).
2. Inventory human personas (`Workforce`, `Admin`, `Customer` tenants), machine/workload principals (`CI/CD`, microservices, cron jobs), IdP trust relationships (`OIDC`, `SAML`, cross-account `STS`), and credential lifetimes via `read_file`.
3. Record unexported live directory states honestly as `NOT VERIFIED`.

---

## Step 2: Protocol, Session & Transitive Escalation Graph Audit
1. Inspect authentication and federation mechanics (`OAuth 2.1`, `OIDC`, `SAML 2.0`, `WebAuthn`, password reset, MFA step-up) for:
   - `PKCE` omission, open `redirect_uri` wildcards, missing `state`/`nonce` checks, and SAML `XSW` vulnerabilities.
   - JWT `alg: none` / RS256-to-HS256 confusion, unverified `aud`/`iss` claims, and insecure `localStorage` token persistence.
2. Construct and traverse the authorization/IAM graph across policies, roles, groups, and service accounts to uncover transitive shadow-admin paths (`PassRole`, policy-version edits, token-minting impersonation, cross-tenant `BOLA`/`BFLA` gaps, standing `Admin` privileges, and orphaned `SCIM` offboarding gaps).
3. Immediately **halt** and **escalate** to `SA`, `PM`, and the user if rogue federated trust anchors, leaked private `JWKS`/SAML signing keys, or unauthorized backdoor admin principals are discovered.

---

## Step 3: Classification, Risk Scoring & Redaction
1. Classify every identity finding into **Confirmed Vulnerability**, **Potential Finding**, **False Positive** (constrained by permission boundary/`SCP`), or **Unverified (`NOT VERIFIED`)**.
2. Assign `CVSS v3.1/v4.0` scores and redact `100%` of secrets, signing keys, assertions, and PII.

---

## Step 4: Least-Privilege & Policy-as-Code Remediation
1. Author hardened OIDC/OAuth configurations, least-privilege IAM policies (bound by explicit `Resource` ARNs and `Condition` keys), `JIT` elevation workflows, and centralized `OPA/Rego` or `Cedar` `RBAC`/`ABAC`/`ReBAC` policies.
2. Explicitly preserve and document monitored break-glass recovery exclusions so rollout cannot cause administrative self-lockout.

---

## Step 5: Authorization Matrix Retest & Handoff
1. Execute automated policy-matrix **retest** suites (`Principal x Tenant x Action x Resource`) via `run_command` confirming `Deny` on all cross-tenant and escalation vectors and `Allow` on valid workflows.
2. Verify token-validation negative tests reject expired, unsigned (`alg: none`), audience-mismatched, and replayed refresh tokens.
3. Confirm `SCIM` offboarding and break-glass alerting rules are documented with rollback procedures.
4. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the hardened IAM package and break-glass runbook.
