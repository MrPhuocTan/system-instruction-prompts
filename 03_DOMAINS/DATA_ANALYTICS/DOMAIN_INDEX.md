# Domain 10: Data Engineering & Analytics (`DATA_ANALYTICS`)

- **Domain ID:** `DOM-10-DATA`
- **Precedence Layer:** Level 4 Domain Governance (subordinate to [`00_GLOBAL_CONSTITUTION`](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [`01_ORCHESTRATION`](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md))
- **Normative Policy:** [`DOMAIN_SYSTEM_PROMPT.md`](./DOMAIN_SYSTEM_PROMPT.md)
- **Verification Standard:** [`QUALITY_GATES.md`](./QUALITY_GATES.md)
- **Canonical Specialist Roles:** `7` (`ROLE-DATA-001` through `ROLE-DATA-007`)

---

## 1. Domain Scope & Engineering Charter

The `DATA_ANALYTICS` domain governs enterprise data architecture, batch/streaming ingestion (`CDC`, event buses, lakehouse storage), analytical transformation (`ELT`/`dbt` dimensional and semantic layers), automated data quality observability, metadata/privacy governance, business intelligence (`BI`), and truthful perceptual visualization. Workstreams in this domain uphold a zero-ambiguity data standard: every dataset declares an explicit grain and primary key, every pipeline executes idempotently under replay and late-arriving events, every business KPI resolves to one canonical semantic formula, and every chart represents underlying uncertainty and scale without visual distortion or decorative `"AI Sign"` clutter.

---

## 2. Canonical Role Inventory (`7` Roles)

| Role ID | Canonical Role Name | System Prompt | Quality Checklist | Primary Responsibility Boundary |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-DATA-001` | `DATA_ARCHITECT` | [`SYSTEM_PROMPT.md`](./ROLES/DATA_ARCHITECT/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DATA_ARCHITECT/QUALITY_CHECKLIST.md) | Enterprise lakehouse/warehouse topology, Medallion/dimensional/Data Vault modeling, partitioning/clustering, storage formats (`Iceberg`/`Parquet`), and SLA/cost governance. |
| `ROLE-DATA-002` | `DATA_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/DATA_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DATA_ENGINEER/QUALITY_CHECKLIST.md) | Batch and streaming ingestion (`CDC`, `Kafka`, `Spark`/`Flink`/`Polars`/`DuckDB`), idempotent backfills, watermarks, schema evolution, and orchestration (`Airflow`/`Dagster`). |
| `ROLE-DATA-003` | `ANALYTICS_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/ANALYTICS_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/ANALYTICS_ENGINEER/QUALITY_CHECKLIST.md) | Modular `SQL`/`dbt` marts (`staging -> intermediate -> fct/dim`), `SCD Type 2` snapshots, fan-out/chasm-trap prevention, and governed semantic metric layers. |
| `ROLE-DATA-004` | `BI_ANALYST` | [`SYSTEM_PROMPT.md`](./ROLES/BI_ANALYST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/BI_ANALYST/QUALITY_CHECKLIST.md) | KPI trees, cohort retention/unit-economics decomposition, variance/driver attribution (`price-volume-mix`), self-serve dashboard semantics, and executive readouts. |
| `ROLE-DATA-005` | `DATA_QUALITY_ENGINEER` | [`SYSTEM_PROMPT.md`](./ROLES/DATA_QUALITY_ENGINEER/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DATA_QUALITY_ENGINEER/QUALITY_CHECKLIST.md) | Write-Audit-Publish (`WAP`) circuit breakers, source-to-target reconciliation, row/null/uniqueness/referential/distribution assertions, and anomaly SLAs. |
| `ROLE-DATA-006` | `DATA_GOVERNANCE_SPECIALIST` | [`SYSTEM_PROMPT.md`](./ROLES/DATA_GOVERNANCE_SPECIALIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DATA_GOVERNANCE_SPECIALIST/QUALITY_CHECKLIST.md) | Data catalogs, column-level lineage, `PII`/`PHI` classification, RBAC/ABAC row-access and dynamic masking policies, retention/right-to-erasure, and producer-consumer contracts. |
| `ROLE-DATA-007` | `DATA_VISUALIZATION_SPECIALIST` | [`SYSTEM_PROMPT.md`](./ROLES/DATA_VISUALIZATION_SPECIALIST/SYSTEM_PROMPT.md) | [`QUALITY_CHECKLIST.md`](./ROLES/DATA_VISUALIZATION_SPECIALIST/QUALITY_CHECKLIST.md) | Perceptual encoding accuracy, small-multiples/information hierarchy, colorblind-safe (`WCAG`) palettes, interactive dashboard ergonomics, and zero chartjunk/`"AI Sign"` clutter. |

---

## 3. Role Selection & Multi-Domain Routing Matrix

| Problem Pattern | Primary Role(s) | Mandatory Supporting / Review Role(s) | Cross-Domain Touchpoints |
| :--- | :--- | :--- | :--- |
| End-to-end lakehouse or warehouse platform | `DATA_ARCHITECT`, `DATA_ENGINEER` | `DATA_GOVERNANCE_SPECIALIST`, `DATA_QUALITY_ENGINEER` | `PLATFORM_ENGINEER`, `DATABASE_ENGINEER` (`IT_SOFTWARE`) |
| Core dimensional marts & semantic KPI layer | `ANALYTICS_ENGINEER` | `DATA_QUALITY_ENGINEER`, `BI_ANALYST` | `FINANCIAL_ANALYST` (`ECONOMICS_FINANCE`) |
| Executive dashboard, KPI investigation, or BI app | `BI_ANALYST`, `DATA_VISUALIZATION_SPECIALIST` | `DATA_QUALITY_ENGINEER` | `FRONTEND_ENGINEER` (`IT_SOFTWARE`), `PRODUCT_MANAGER` (`BUSINESS_PRODUCT`) |
| Point-in-time ML feature tables or `RAG` corpus sync | `DATA_ENGINEER`, `ANALYTICS_ENGINEER` | `DATA_GOVERNANCE_SPECIALIST` | [`MACHINE_LEARNING_ENGINEER`](../AI_MACHINE_LEARNING/ROLES/MACHINE_LEARNING_ENGINEER/SYSTEM_PROMPT.md), [`LLM_ENGINEER`](../AI_MACHINE_LEARNING/ROLES/LLM_ENGINEER/SYSTEM_PROMPT.md) |
| `GDPR`/`HIPAA` data masking, lineage, & retention | `DATA_GOVERNANCE_SPECIALIST`, `DATA_ARCHITECT` | `DATA_QUALITY_ENGINEER` | `PRIVACY_SPECIALIST` (`LEGAL_COMPLIANCE` / `CYBERSECURITY`) |

---

## 4. Recommended Reusable Skills

- **Cross-Domain Skills (`04_CROSS_DOMAIN_SKILLS`):**
  - [`DATA_INTERPRETATION`](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md) — Denominator discipline, aggregation bias (`Simpson's paradox`), and seasonality/cohort awareness.
  - [`SYSTEMS_THINKING`](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) — Upstream OLTP schema mutations, backfill blast radius, and downstream BI/ML lineage propagation.
  - [`QUALITY_ASSURANCE`](../../04_CROSS_DOMAIN_SKILLS/QUALITY_ASSURANCE/SKILL.md) — Deterministic reconciliation and boundary edge-case testing (`NULL`s, timezones, leap days, duplicates).
- **Specialized Skills (`05_SPECIALIZED_SKILLS`):**
  - [`DATABASE_VALIDATION`](../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) — Query plan inspection, grain/key uniqueness, referential integrity, and ACID/isolation checks.
  - [`HUMAN_CENTRIC_APPLICATION_QA`](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) — 3-Level functional, stateful filter/drill-down, and visual cleanliness verification for BI/data applications.
  - [`PERFORMANCE_BENCHMARKING`](../../05_SPECIALIZED_SKILLS/PERFORMANCE_BENCHMARKING/SKILL.md) — Partition pruning, spill-to-disk elimination, shuffle skew mitigation, and query cost profiling.
