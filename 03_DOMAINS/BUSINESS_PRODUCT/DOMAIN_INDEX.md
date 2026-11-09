# Domain 05: Business & Product (`BUSINESS_PRODUCT`) — Domain Index

- **Domain ID:** `DOM-05-BUSINESS-PRODUCT`
- **Precedence Layer:** Level 4 (`03_DOMAINS/BUSINESS_PRODUCT/`) — Subordinate to [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [ORCHESTRATION_SYSTEM_PROMPT.md](../../01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md)
- **Normative Domain Files:** [DOMAIN_SYSTEM_PROMPT.md](./DOMAIN_SYSTEM_PROMPT.md) | [QUALITY_GATES.md](./QUALITY_GATES.md)
- **Canonical Role Count:** `7` Specialist Roles (`ROLE-BIZ-001` through `ROLE-BIZ-007`)

---

## 1. Domain Scope & Mission

The `BUSINESS_PRODUCT` domain governs end-to-end product discovery and specification, business process and requirements engineering, competitive and corporate strategy, business program/delivery execution, operational capacity and SOP optimization, acquisition/retention growth experimentation, and customer/market research. Every deliverable connects validated customer problems to measurable North Star outcomes, contribution-positive unit economics, explicit non-goals/trade-offs, and operationally feasible execution plans free of decorative "AI Sign" clutter.

---

## 2. Canonical Role Inventory (`7` Roles)

| Role ID | Canonical Role Directory | Primary Specialist Focus | System Prompt | Quality Checklist |
| :--- | :--- | :--- | :--- | :--- |
| `ROLE-BIZ-001` | `PRODUCT_MANAGER` | Product discovery, JTBD problem framing, PRDs, RICE/WSJF prioritization, outcome roadmaps, acceptance criteria & UX utility | [SYSTEM_PROMPT.md](./ROLES/PRODUCT_MANAGER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PRODUCT_MANAGER/QUALITY_CHECKLIST.md) |
| `ROLE-BIZ-002` | `BUSINESS_ANALYST` | BABOK requirements engineering, BPMN 2.0 as-is/to-be process mapping, domain rules, RTM traceability & UAT scenarios | [SYSTEM_PROMPT.md](./ROLES/BUSINESS_ANALYST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/BUSINESS_ANALYST/QUALITY_CHECKLIST.md) |
| `ROLE-BIZ-003` | `BUSINESS_STRATEGIST` | Competitive moat architecture (7 Powers, Five Forces), Playing-to-Win choices, pricing/packaging & build-partner-buy strategy | [SYSTEM_PROMPT.md](./ROLES/BUSINESS_STRATEGIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/BUSINESS_STRATEGIST/QUALITY_CHECKLIST.md) |
| `ROLE-BIZ-004` | `PROJECT_MANAGER` | Domain business program delivery (WBS, CPM critical path, EVM, RAID logs, RACI, vendor/change rollout — distinct from Core `PM`) | [SYSTEM_PROMPT.md](./ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/PROJECT_MANAGER/QUALITY_CHECKLIST.md) |
| `ROLE-BIZ-005` | `OPERATIONS_MANAGER` | Process throughput & Little's Law capacity modeling, SLA/SLO design, SOPs, service delivery unit costs & vendor governance | [SYSTEM_PROMPT.md](./ROLES/OPERATIONS_MANAGER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/OPERATIONS_MANAGER/QUALITY_CHECKLIST.md) |
| `ROLE-BIZ-006` | `GROWTH_SPECIALIST` | Full-funnel AARRR loops, PLG activation/retention, statistically powered A/B experimentation, CAC/LTV payback & guardrails | [SYSTEM_PROMPT.md](./ROLES/GROWTH_SPECIALIST/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/GROWTH_SPECIALIST/QUALITY_CHECKLIST.md) |
| `ROLE-BIZ-007` | `MARKET_RESEARCHER` | Customer discovery interviews, JTBD synthesis, survey/Van Westendorp/conjoint design, ICP segmentation & win/loss analysis | [SYSTEM_PROMPT.md](./ROLES/MARKET_RESEARCHER/SYSTEM_PROMPT.md) | [QUALITY_CHECKLIST.md](./ROLES/MARKET_RESEARCHER/QUALITY_CHECKLIST.md) |

> **Architectural Disambiguation (`ROLE-BIZ-004` vs. `ROLE-CORE-001`):** Domain `PROJECT_MANAGER` (`03_DOMAINS/BUSINESS_PRODUCT/ROLES/PROJECT_MANAGER`) authors client-facing business project schedules, critical-path plans, EVM baselines, and organizational change rollouts. Core [PROJECT_MANAGER](../../02_CORE_ROLES/PROJECT_MANAGER/SYSTEM_PROMPT.md) (`02_CORE_ROLES/PROJECT_MANAGER`) is the persistent Antigravity multi-agent governance orchestrator owning task routing, subagent allocation, and `PM_GATE` delivery signoff.

---

## 3. Recommended Cross-Domain & Specialized Skills

Load minimal task-relevant skills on demand via [SKILL_DISCOVERY_AND_LOADING](../../05_SPECIALIZED_SKILLS/SKILL_DISCOVERY_AND_LOADING/SKILL.md):

- **Core Analytical & Specification Skills:** [REQUIREMENTS_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/REQUIREMENTS_ANALYSIS/SKILL.md), [DECISION_ANALYSIS](../../04_CROSS_DOMAIN_SKILLS/DECISION_ANALYSIS/SKILL.md), [CRITICAL_THINKING](../../04_CROSS_DOMAIN_SKILLS/CRITICAL_THINKING/SKILL.md), [SYSTEMS_THINKING](../../04_CROSS_DOMAIN_SKILLS/SYSTEMS_THINKING/SKILL.md), [DATA_INTERPRETATION](../../04_CROSS_DOMAIN_SKILLS/DATA_INTERPRETATION/SKILL.md), [RISK_MANAGEMENT](../../04_CROSS_DOMAIN_SKILLS/RISK_MANAGEMENT/SKILL.md), [TECHNICAL_WRITING](../../04_CROSS_DOMAIN_SKILLS/TECHNICAL_WRITING/SKILL.md), and [COMMUNICATION](../../04_CROSS_DOMAIN_SKILLS/COMMUNICATION/SKILL.md).
- **Specialized Validation Skills:** [HUMAN_CENTRIC_APPLICATION_QA](../../05_SPECIALIZED_SKILLS/HUMAN_CENTRIC_APPLICATION_QA/SKILL.md) (validating shipped product journeys against PRD acceptance criteria) and [FINANCIAL_MODEL_VALIDATION](../../05_SPECIALIZED_SKILLS/FINANCIAL_MODEL_VALIDATION/SKILL.md) (auditing pricing, GTM payback, and business-case spreadsheets).

---

## 4. Role Selection & Cross-Domain Coordination Matrix

| Business / Product Problem | Primary Role | Supporting / Downstream Role(s) | Mandatory Boundary & Review Rule |
| :--- | :--- | :--- | :--- |
| **New Product / Feature Definition (PRD)** | `PRODUCT_MANAGER` | `MARKET_RESEARCHER`, `BUSINESS_ANALYST`, [IT_SOFTWARE](../IT_SOFTWARE/DOMAIN_INDEX.md), [DESIGN_CREATIVE](../DESIGN_CREATIVE/DOMAIN_INDEX.md) | Lock testable Gherkin acceptance criteria and explicit out-of-scope boundaries before engineering build. |
| **Market Entry, Moat & Pricing Strategy** | `BUSINESS_STRATEGIST` | `MARKET_RESEARCHER`, [ECONOMICS_FINANCE](../ECONOMICS_FINANCE/DOMAIN_INDEX.md) (`FINANCIAL_ANALYST`, `MARKET_RESEARCH_ANALYST`) | Pair strategic positioning with verified contribution-margin unit economics (`BIZ-QG-02`). |
| **Enterprise Transformation / Launch Rollout** | `PROJECT_MANAGER` (`ROLE-BIZ-004`) | `BUSINESS_ANALYST`, `OPERATIONS_MANAGER` | Subordinate to Core `PM` + `SA` workspace governance; separate schedule builder from independent gate reviewer at Level 3–4. |
| **Funnel Conversion, Retention & Pricing Tests** | `GROWTH_SPECIALIST` | `PRODUCT_MANAGER`, [DATA_ANALYTICS](../DATA_ANALYTICS/DOMAIN_INDEX.md) | Pre-register sample size, MDE, and anti-dark-pattern ethical guardrails before experiment launch (`BIZ-QG-05`). |
