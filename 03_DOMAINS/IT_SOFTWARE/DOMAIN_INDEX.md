# IT & Software Engineering Domain Index (`IT_SOFTWARE`)

- **Domain ID:** `DOM-01-IT_SOFTWARE`
- **Precedence Layer:** Level 4 Domain Governance (subordinate to [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [ORCHESTRATION_SYSTEM_PROMPT.md](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md))
- **Canonical Domain Standards:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md)
- **Domain Verification Gates:** [QUALITY_GATES.md](./QUALITY_GATES.md)

---

## 1. Domain Purpose & Scope

The `IT_SOFTWARE` domain governs end-to-end software architecture, backend and frontend implementation, relational and distributed persistence, developer platform tooling, CI/CD automation, quality verification, load engineering, and production site reliability. It provides reusable specialist role definitions that execute deterministic, contract-first engineering across Complexity Levels 1 through 4 without coupling reusable domain standards to any single downstream codebase.

Out-of-scope concerns route to adjacent domains: offensive/defensive security testing and Rules of Engagement (`03_DOMAINS/CYBERSECURITY/`), statistical model training and LLM evaluation (`03_DOMAINS/AI_MACHINE_LEARNING/`), analytical warehousing and BI modeling (`03_DOMAINS/DATA_ANALYTICS/`), and brand/visual design systems (`03_DOMAINS/DESIGN_CREATIVE/`).

---

## 2. Canonical Role Inventory (`11` Roles)

| Role ID | Canonical Role Directory | Primary Engineering Focus | Specialist Prompt | Pre-Handoff Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-IT-001` | `SOFTWARE_ARCHITECT` | Service boundaries, ADRs, API/event contracts, non-functional trade-offs | [SYSTEM_PROMPT.md](./ROLES/SOFTWARE_ARCHITECT/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/SOFTWARE_ARCHITECT/QUALITY_CHECKLIST.md) |
| `ROLE-IT-002` | `BACKEND_ENGINEER` | Domain services, REST/gRPC/GraphQL APIs, concurrency, idempotency, authz | [SYSTEM_PROMPT.md](./ROLES/BACKEND_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/BACKEND_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-003` | `FRONTEND_ENGINEER` | Component architecture, client state, WCAG 2.2 AA accessibility, zero-AI-sign UI | [SYSTEM_PROMPT.md](./ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/FRONTEND_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-004` | `FULLSTACK_ENGINEER` | Vertical feature slices spanning UI, API transport, validation, and persistence | [SYSTEM_PROMPT.md](./ROLES/FULLSTACK_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/FULLSTACK_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-005` | `DEVOPS_ENGINEER` | CI/CD pipelines, reproducible container builds, IaC modules, progressive rollout | [SYSTEM_PROMPT.md](./ROLES/DEVOPS_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/DEVOPS_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-006` | `PLATFORM_ENGINEER` | Internal developer platforms, golden paths, shared SDKs, multi-tenant guardrails | [SYSTEM_PROMPT.md](./ROLES/PLATFORM_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PLATFORM_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-007` | `DATABASE_ENGINEER` | Relational/NoSQL data modeling, ACID isolation, indexing, expand-contract migrations | [SYSTEM_PROMPT.md](./ROLES/DATABASE_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/DATABASE_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-008` | `QA_ENGINEER` | Risk-based test strategy, boundary analysis, exploratory journeys, defect triage | [SYSTEM_PROMPT.md](./ROLES/QA_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/QA_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-009` | `AUTOMATION_QA` | Deterministic unit/API/E2E harnesses, contract testing, zero-flake CI test suites | [SYSTEM_PROMPT.md](./ROLES/AUTOMATION_QA/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/AUTOMATION_QA/QUALITY_CHECKLIST.md) |
| `ROLE-IT-010` | `PERFORMANCE_ENGINEER` | Latency/throughput profiling, load/soak/stress modeling, memory/query optimization | [SYSTEM_PROMPT.md](./ROLES/PERFORMANCE_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PERFORMANCE_ENGINEER/QUALITY_CHECKLIST.md) |
| `ROLE-IT-011` | `SITE_RELIABILITY_ENGINEER` | SLIs/SLOs, error budgets, OpenTelemetry observability, runbooks, chaos resilience | [SYSTEM_PROMPT.md](./ROLES/SITE_RELIABILITY_ENGINEER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/SITE_RELIABILITY_ENGINEER/QUALITY_CHECKLIST.md) |

---

## 3. Role-vs-Agent Allocation & Multi-Role Combination Rules

Per [DYNAMIC_AGENT_ALLOCATION.md](../../01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md), a **Role** is a static capability specification whereas an **Agent** is a runtime execution instance bound to an Exclusive Write-Lock:
1. **Level 1–2 Co-Location (Permitted):** A single worker agent may combine compatible delivery roles when scope is cohesive—such as `BACKEND_ENGINEER` + `DATABASE_ENGINEER` for a service-local schema change, `DEVOPS_ENGINEER` + `SITE_RELIABILITY_ENGINEER` for pipeline-plus-alerting setup, or `FULLSTACK_ENGINEER` replacing separate frontend/backend agents on a vertical slice.
2. **Level 3–4 Separation of Duties (Mandatory):** Never assign the authoring engineer (`BACKEND_ENGINEER`, `FRONTEND_ENGINEER`, or `FULLSTACK_ENGINEER`) to serve simultaneously as the independent `QA_ENGINEER` signoff owner or as [SYSTEM_ARCHITECT](../../02_CORE_ROLES/SYSTEM_ARCHITECT/SYSTEM_PROMPT.md) gatekeeper (`SA_GATE`). Parallel agents must hold strictly disjoint file ownership paths.
3. **Architecture Boundary:** `SOFTWARE_ARCHITECT` designs intra-domain service and module topology under the authority of core `SYSTEM_ARCHITECT`, which retains project-wide write-lock and cross-domain contract authority.

---

## 4. Recommended Cross-Domain & Specialized Skills

Load only task-relevant skills on demand rather than preloading the entire catalog:
- **Architectural & Coupling Analysis:** [SYSTEMS_THINKING/SKILL.md](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md) (`SKL-CORE-003`) for dependency graphs, failure blast radius, and state feedback loops.
- **3-Level End-to-End Application Verification:** [HUMAN_CENTRIC_APPLICATION_QA/SKILL.md](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) (`SKL-SPEC-001`) for build/test, live runtime journeys, and utilitarian UX verification.
- **Transport & Schema Verification:** [API_TESTING/SKILL.md](../../05_SPECIALIZED_SKILLS/API_TESTING/SKILL.md) (`SKL-SPEC-003`) for status codes, authn/authz rejection, idempotency, and payload contract checks.
- **Persistence & Migration Integrity:** [DATABASE_VALIDATION/SKILL.md](../../05_SPECIALIZED_SKILLS/DATABASE_VALIDATION/SKILL.md) (`SKL-SPEC-004`) for constraint enforcement, query plans, and rollback-safe migrations.
- **Latency & Capacity Profiling:** [PERFORMANCE_BENCHMARKING/SKILL.md](../../05_SPECIALIZED_SKILLS/PERFORMANCE_BENCHMARKING/SKILL.md) (`SKL-SPEC-005`) for reproducible baseline vs. candidate p50/p95/p99 measurements.
