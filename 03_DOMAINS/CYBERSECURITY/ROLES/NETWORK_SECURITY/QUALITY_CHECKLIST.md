# Quality Checklist — Network Security Engineer (`ROLE-CYB-010`)

Verify every item prior to handoff and `SA_GATE` sign-off per [SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md), [WORKFLOW.md](./WORKFLOW.md), and [QUALITY_GATES.md](../../QUALITY_GATES.md).

---

## 1. Authorization, CIDR Scope & Lockout/Blackhole Safety (`RoE`)
- [ ] Target network `IP/CIDR`, VPC, cluster, and domain **scope** plus **authorization** / **Rules of Engagement (`RoE`)** were verified prior to inspection or probing.
- [ ] Analysis remained **non-destructive**: zero unauthorized active scanning (`nmap`/`masscan`), zero unapproved live firewall reloads, and staged `Audit/Count -> Enforce` rollout plans included for all `DENY` policies.
- [ ] Policies preserve essential operational flows (`DNS 53`, health checks, OCSP/KMS endpoints, break-glass bastion access) and include tested rollback commands to prevent outage or lockout.

---

## 2. Zero-Trust Segmentation, Transport & Edge Depth
- [ ] Both ingress AND egress default-deny policies are specified, eliminating `0.0.0.0/0` admin/DB exposure, flat east-west subnet lateral paths, and RFC1918/metadata (`169.254.169.254`) SSRF egress.
- [ ] Cryptographic transport configs mandate `TLS 1.3` (or strong `TLS 1.2` AEAD ciphers only), `mTLS` for east-west service traffic, `HSTS`, and modern `IPsec IKEv2` / `WireGuard` parameters.
- [ ] Edge proxies/WAFs sanitize spoofable headers (`X-Forwarded-For`), mitigate HTTP request smuggling/desync, and pair virtual patches with upstream `APPLICATION_SECURITY` root-cause tracking.

---

## 3. Epistemic Classification, Flow Evidence & Secret Redaction
- [ ] Rulebase and flow/PCAP findings are strictly classified as **Confirmed Vulnerability**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**.
- [ ] Severity ratings pair `CVSS v3.1/v4.0` vectors with lateral-movement blast-radius context.
- [ ] CIDR overlap, rule shadowing, and NAT translation order were programmatically or mathematically verified.
- [ ] `100%` of TLS private keys, WireGuard/IPsec `PSKs`, BGP/RADIUS secrets, SNMP strings, and sensitive PCAP application payloads are redacted.

---

## 4. Actionable Remediation & Retest Verification
- [ ] Deliverables provide syntax-validated network IaC, `NetworkPolicy`/Cilium YAML, TLS/proxy configs, or `Suricata` detections.
- [ ] Deterministic **retest** steps verify blocked unauthorized port/egress paths AND uninterrupted valid service-to-service communication.
