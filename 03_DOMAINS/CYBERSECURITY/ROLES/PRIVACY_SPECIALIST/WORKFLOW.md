# Practitioner Workflow — Technical Privacy Specialist (`ROLE-CYB-013`)

- **Role:** `PRIVACY_SPECIALIST` ([SYSTEM_PROMPT.md](./SYSTEM_PROMPT.md))
- **Verification Gate:** [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) | [QUALITY_GATES.md](../../QUALITY_GATES.md)
- **Companion Skills:** [DATABASE_VALIDATION](../../../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) | [RISK_MANAGEMENT](../../../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md)

---

## Step 1: Scope, Authorization & Regulatory Context Intake
1. Confirm **authorized** repository/schema/pipeline **scope**, applicable privacy regimes (`GDPR`, `CCPA/CPRA`, `HIPAA`, `ISO 27701`, `NIST Privacy Framework`), and **Rules of Engagement (`RoE`)** (**non-destructive** static inspection and synthetic-fixture testing only—never ingest live customer PII).
2. Classify personal data elements across sensitivity tiers (`Direct Identifiers`, `Quasi-Identifiers`, `Special Category SPI/PHI/Biometric/Children's Data`, `Behavioral/Telemetry Metadata`).

---

## Step 2: Code-to-Sink Data-Flow Discovery (`RoPA`) & Leak Hunting
1. Trace personal data flows end-to-end via `read_file` across API schemas, ORM models, SQL migrations, frontend analytics/pixel SDKs, structured/unstructured loggers, error trackers, ETL jobs, and AI/LLM prompt/training pipelines (mark uninspected external SaaS subprocessors as `NOT VERIFIED`).
2. Audit high-frequency privacy failure points:
   - PII leaked in URL query strings, application/exception logs, or unencrypted object storage.
   - Third-party trackers/cookies firing prior to opt-in consent or ignoring `Global Privacy Control (GPC)`.
   - Unsalted hashes (`MD5`/`SHA-256` of email/phone) misclassified as anonymous data, or unbounded table retention lacking TTL reapers.
3. Immediately **halt** and **escalate** to `SA`, `PM`, human DPO/Legal Counsel, and the user if exposed cleartext PHI/SPI/children's data or active unauthorized third-party data exfiltration is uncovered.

---

## Step 3: `LINDDUN` Threat Modeling, Classification & `DPIA` Scoring
1. Evaluate Linkability, Identifiability, Detectability, Disclosure, Unawareness, and Non-compliance (`LINDDUN`) across each processing activity.
2. Classify findings strictly into **Confirmed Vulnerability / Confirmed Privacy Gap**, **Potential Finding**, **False Positive**, or **Unverified (`NOT VERIFIED`)**, quantifying data-subject harm and redacting `100%` of sensitive examples.

---

## Step 4: Privacy-by-Design, `PETs` & `DSAR` Pipeline Engineering
1. Implement or specify structural controls: field minimization, structured-logger allowlist/redaction interceptors, pre-consent SDK blocking, KMS-backed tokenization / crypto-shredding, Differential Privacy / $k$-anonymity aggregation bounds, and idempotent `DSAR` export/erasure cascades spanning DBs, caches, queues, search indexes, and backups.

---

## Step 5: Synthetic Retest Verification, DPO Escalation & Handoff
1. Execute synthetic-data **retest** suites via `run_command` proving zero PII emission in structured/error logs and zero pre-consent third-party network beacons.
2. Verify end-to-end `DSAR` erasure cascades leave zero surviving target PII records across primary databases, caches, queues, and search indexes.
3. Route residual `DPIA` risks, retention exceptions, and cross-border transfer items to the human DPO/Legal Counsel for formal sign-off.
4. Complete [QUALITY_CHECKLIST.md](./QUALITY_CHECKLIST.md) and deliver the redacted privacy engineering package.
