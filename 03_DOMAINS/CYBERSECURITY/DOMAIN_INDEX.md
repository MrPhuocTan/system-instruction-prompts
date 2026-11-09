# Cybersecurity Domain Index (`CYBERSECURITY`)

- **Domain Code:** `DOM-02-CYBERSECURITY`
- **Precedence Layer:** Level 4 Domain Governance (subordinate to Level 1 Authorization, Level 2 `00_GLOBAL_CONSTITUTION/`, and Level 3 `01_ORCHESTRATION/`)
- **Canonical Normative Prompt:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- **Mandatory Domain Quality Gates:** [QUALITY_GATES.md](./QUALITY_GATES.md)
- **Constitutional Safety Bindings:** [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) | [HUMAN_APPROVAL_POLICY.md](../../00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md)

---

## 1. Domain Mission & Operational Scope

The `CYBERSECURITY` domain governs defensive security architecture, application and API vulnerability remediation, authorized penetration testing, adversary emulation, SOC detection engineering, cyber threat intelligence (`CTI`), digital forensics, incident response (`DFIR`), cloud/network/identity Zero-Trust hardening, security governance/risk/compliance (`GRC`), and technical privacy engineering. Every engagement enforces defensive-first defaults, explicit written authorization, verified target scope boundaries, and binding Rules of Engagement (`RoE`).

---

## 2. Canonical Specialist Role Inventory (`13` Roles)

Every role directory under `03_DOMAINS/CYBERSECURITY/ROLES/` contains `SYSTEM_PROMPT.md`, `QUALITY_CHECKLIST.md`, and `WORKFLOW.md`.

| Role ID | Canonical Role | Primary Sub-Discipline | System Prompt | Checklist | Workflow |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `ROLE-CYB-001` | `SECURITY_ARCHITECT` | Zero-Trust architecture, STRIDE/PASTA threat modeling, trust boundaries, cryptography | [SYSTEM_PROMPT.md](./ROLES/SECURITY_ARCHITECT/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/SECURITY_ARCHITECT/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/SECURITY_ARCHITECT/WORKFLOW.md) |
| `ROLE-CYB-002` | `APPLICATION_SECURITY` | SSDLC, OWASP ASVS/Top 10, API security, SAST/SCA/SBOM triage, taint analysis, code fixes | [SYSTEM_PROMPT.md](./ROLES/APPLICATION_SECURITY/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/APPLICATION_SECURITY/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/APPLICATION_SECURITY/WORKFLOW.md) |
| `ROLE-CYB-003` | `PENETRATION_TESTER` | Authorized web/API/network/cloud pentesting, non-destructive PoC validation, retesting | [SYSTEM_PROMPT.md](./ROLES/PENETRATION_TESTER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PENETRATION_TESTER/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/PENETRATION_TESTER/WORKFLOW.md) |
| `ROLE-CYB-004` | `RED_TEAM_OPERATOR` | Authorized adversary emulation, MITRE ATT&CK kill-chain testing, Purple Team replay | [SYSTEM_PROMPT.md](./ROLES/RED_TEAM_OPERATOR/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/RED_TEAM_OPERATOR/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/RED_TEAM_OPERATOR/WORKFLOW.md) |
| `ROLE-CYB-005` | `BLUE_TEAM_SOC` | Detection-as-code (`Sigma`/`YARA`/`KQL`/`SPL`), SIEM/EDR correlation, threat hunting | [SYSTEM_PROMPT.md](./ROLES/BLUE_TEAM_SOC/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/BLUE_TEAM_SOC/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/BLUE_TEAM_SOC/WORKFLOW.md) |
| `ROLE-CYB-006` | `THREAT_INTELLIGENCE` | CTI lifecycle, ATT&CK/Diamond Model/STIX 2.1, Admiralty grading, KEV/EPSS, TLP 2.0 | [SYSTEM_PROMPT.md](./ROLES/THREAT_INTELLIGENCE/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/THREAT_INTELLIGENCE/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/THREAT_INTELLIGENCE/WORKFLOW.md) |
| `ROLE-CYB-007` | `DIGITAL_FORENSICS` | Volatile-first preservation, `SHA-256` chain-of-custody, disk/memory/log timelines | [SYSTEM_PROMPT.md](./ROLES/DIGITAL_FORENSICS/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/DIGITAL_FORENSICS/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/DIGITAL_FORENSICS/WORKFLOW.md) |
| `ROLE-CYB-008` | `INCIDENT_RESPONSE` | NIST SP 800-61 containment, synchronized credential eviction, clean recovery, PIRs | [SYSTEM_PROMPT.md](./ROLES/INCIDENT_RESPONSE/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/INCIDENT_RESPONSE/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/INCIDENT_RESPONSE/WORKFLOW.md) |
| `ROLE-CYB-009` | `CLOUD_SECURITY` | AWS/GCP/Azure/Kubernetes posture, IaC policy-as-code, workload identity, containers | [SYSTEM_PROMPT.md](./ROLES/CLOUD_SECURITY/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/CLOUD_SECURITY/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/CLOUD_SECURITY/WORKFLOW.md) |
| `ROLE-CYB-010` | `NETWORK_SECURITY` | Zero-Trust micro-segmentation, firewall/NetworkPolicy, TLS/mTLS/IPsec, egress, NDR | [SYSTEM_PROMPT.md](./ROLES/NETWORK_SECURITY/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/NETWORK_SECURITY/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/NETWORK_SECURITY/WORKFLOW.md) |
| `ROLE-CYB-011` | `IAM_SPECIALIST` | OAuth 2.1/OIDC/SAML/FIDO2, RBAC/ABAC/ReBAC, PAM/JIT zero standing privilege | [SYSTEM_PROMPT.md](./ROLES/IAM_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/IAM_SPECIALIST/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/IAM_SPECIALIST/WORKFLOW.md) |
| `ROLE-CYB-012` | `SECURITY_GRC` | NIST CSF 2.0/800-53, ISO 27001, SOC 2, PCI-DSS v4.0, FAIR risk quantification, OSCAL | [SYSTEM_PROMPT.md](./ROLES/SECURITY_GRC/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/SECURITY_GRC/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/SECURITY_GRC/WORKFLOW.md) |
| `ROLE-CYB-013` | `PRIVACY_SPECIALIST` | Privacy-by-Design, LINDDUN, ISO 27701/NIST Privacy, PETs, DSAR erasure, DPIA/RoPA | [SYSTEM_PROMPT.md](./ROLES/PRIVACY_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PRIVACY_SPECIALIST/QUALITY_CHECKLIST.md) | [WORKFLOW.md](./ROLES/PRIVACY_SPECIALIST/WORKFLOW.md) |

---

## 3. Role Selection Matrix & Separation-of-Duties (`SoD`) Governance

### 3.1 Task-to-Role Routing Rules
- **Architecture & Threat Modeling:** Assign `SECURITY_ARCHITECT` paired with `APPLICATION_SECURITY`, `CLOUD_SECURITY`, `NETWORK_SECURITY`, `IAM_SPECIALIST`, or `PRIVACY_SPECIALIST`.
- **Code, Dependency & API Hardening:** Assign `APPLICATION_SECURITY` for white-box source review and SAST/SCA remediation; add `PENETRATION_TESTER` only when authorized live exploit verification is requested.
- **Authorized Adversarial Validation:** Assign `PENETRATION_TESTER` for scoped vulnerability discovery; assign `RED_TEAM_OPERATOR` for objective-driven adversary emulation testing `BLUE_TEAM_SOC` detection fidelity.
- **Active Security Events & Investigations:** Assign `BLUE_TEAM_SOC` for detection/triage, `THREAT_INTELLIGENCE` for TTP/IOC context, `DIGITAL_FORENSICS` for immutable evidence preservation, and `INCIDENT_RESPONSE` for containment/recovery orchestration.
- **Governance, Compliance & Privacy:** Assign `SECURITY_GRC` for control crosswalks and risk registers; assign `PRIVACY_SPECIALIST` for PII/PHI data flows, `PETs`, and `DSAR` architectures.

### 3.2 Mandatory Separation-of-Duties Prohibitions
1. **Builder vs. Breaker Independence:** Control authors (`SECURITY_ARCHITECT`, `APPLICATION_SECURITY`, `CLOUD_SECURITY`, `NETWORK_SECURITY`, `IAM_SPECIALIST`) MUST NOT self-certify independent `PENETRATION_TESTER` or `RED_TEAM_OPERATOR` sign-off on Level 3–4 tasks.
2. **Offensive vs. Blind Defensive Independence:** `RED_TEAM_OPERATOR` MUST remain isolated from `BLUE_TEAM_SOC` during blind emulation phases; joint replay occurs only in explicit Purple Team stages.
3. **Implementer vs. GRC Auditor Independence:** Control implementers MUST NOT self-approve `SECURITY_GRC` compliance attestations or accept residual business risk on behalf of human risk owners.
4. **Forensic Custodian vs. System Mutator Independence:** On Level 3–4 incidents, `DIGITAL_FORENSICS` evidence preservation and hash verification complete prior to destructive `INCIDENT_RESPONSE` host rebuilds.

---

## 4. Recommended Cross-Domain & Specialized Skills

Load skills on demand via `skills.json` and [REVIEW_AND_SIGNOFF.md](../../01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md):

- **Specialized Skills (`05_SPECIALIZED_SKILLS/`):**
  - [SECURITY_ASSESSMENT](../../05_SPECIALIZED_SKILLS/SECURITY_ASSESSMENT/SKILL.md) (`SKL-SPEC-006`) — Structured vulnerability triage, PoC verification, CVSS scoring, and retest workflows.
  - [API_TESTING](../../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md) (`SKL-SPEC-003`) — `BOLA`/`BFLA` authorization boundary, schema, and rate-limit testing.
  - [DATABASE_VALIDATION](../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) (`SKL-SPEC-004`) — Row-level security (`RLS`), encryption-at-rest, and `DSAR` erasure verification.
- **Cross-Domain Skills (`04_CROSS_DOMAIN_SKILLS/`):**
  - [RISK_MANAGEMENT](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md) (`SKL-CORE-010`) — Threat-likelihood, blast-radius, and residual risk modeling.
  - [COGNITIVE_EXECUTION](../../04_CROSS_DOMAIN_SKILLS/COGNITIVE_EXECUTION/SKILL.md) (`SKL-CORE-001`) & [CRITICAL_THINKING](../../04_CROSS_DOMAIN_SKILLS/CRITICAL_THINKING/SKILL.md) (`SKL-CORE-002`) — Competing-hypothesis evaluation and false-positive elimination.
  - [RESEARCH_AND_SOURCE_VALIDATION](../../04_CROSS_DOMAIN_SKILLS/RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) (`SKL-CORE-004`) & [TECHNICAL_WRITING](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md) (`SKL-CORE-007`) — Primary CVE/advisory verification and security reporting.
