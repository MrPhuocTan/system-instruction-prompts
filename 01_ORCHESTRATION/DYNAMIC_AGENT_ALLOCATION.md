# Dynamic Agent Allocation — Logical Role vs. Runtime Agent

## 1. Fundamental Architectural Distinction: Role vs. Agent
Orchestration strictly separates **what specialist capability is needed** (`Role`) from **how many execution processes run** (`Agent`).
A professional role prompt (`SYSTEM_PROMPT.md`) is a **reusable capability definition**, never automatically a permanent running agent ([`AUTONOMOUS_ORCHESTRATION.md`](./AUTONOMOUS_ORCHESTRATION.md)).

| Concept | Definition & Canonical Location | Cardinality & Runtime Lifecycle |
| :--- | :--- | :--- |
| **Logical Role** | Static, reusable specialist specification (`02_CORE_ROLES/<ROLE>/` or `03_DOMAINS/<DOMAIN>/ROLES/<ROLE>/`) defining competencies, decision frameworks, failure modes, and quality checklists. | `112` canonical roles (`4` Core + `108` Domain). Stateless Markdown definitions loaded on demand via `read_file`. |
| **Runtime Agent** | Active execution unit—either the main agent or a temporary/session-reused subagent created via `invoke_subagent` ([`SUBAGENT_CREATION.md`](./SUBAGENT_CREATION.md))—holding a context window, tool permissions, and an Exclusive Write-Lock. | Dynamically scaled (`0` subagents at `Level 0` up to bounded parallel batches at `Level 3`–`Level 4`, or `1` sequential agent under fallback). |

## 2. Cardinality Mapping Patterns (`M Roles <-> N Agents`)

### Pattern A: `1` Runtime Agent Holding Multiple Compatible Roles (`M : 1`)
When multiple specialist perspectives touch the **same files** or form a tight sequential pipeline on `Level 1`–`Level 2` tasks (or under sequential fallback), assign **one runtime agent** to load `2–3` compatible role prompts:
- *Software Example:* Building a CRUD microservice with SQL migrations -> `1` worker agent loads `BACKEND_ENGINEER` + `DATABASE_ENGINEER` + skill `DATABASE_VALIDATION`.
- *Finance Example:* Constructing and validating a DCF valuation model -> `1` worker agent loads `FINANCIAL_MODELING` + `VALUATION_SPECIALIST` + skill `FINANCIAL_MODEL_VALIDATION`.
- *Engineering Advantage:* Zero inter-agent handoff latency, zero shared-file write contention, unified mental model.

### Pattern B: `1` Logical Role Scaled Across Multiple Parallel Agents (`1 : N`)
When a single role's workload is large and partitions cleanly across **disjoint file trees** under locked `SA` interfaces (`Level 3`–`Level 4`), instantiate multiple parallel worker subagents sharing the same logical role:
- *Example:* Implementing three isolated payment adapters (`src/adapters/stripe/**`, `src/adapters/adyen/**`, `src/adapters/sepa/**`) -> `3` parallel subagents each loading `BACKEND_ENGINEER`, each bound to its own Exclusive Write-Lock ([`FILE_OWNERSHIP_AND_LOCKING.md`](./FILE_OWNERSHIP_AND_LOCKING.md)).

### Pattern C: Prohibited Co-Location (Mandatory Separation of Duties)
Never combine conflicting roles inside a single runtime agent when independent verification or regulatory assurance is required ([`INDEPENDENT_VERIFICATION.md`](../00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md)):
1. **Author vs. Independent Reviewer (`Level 3`–`Level 4`):**
   - An agent executing implementation roles (`BACKEND_ENGINEER`, `FINANCIAL_MODELING`, `MLOPS_ENGINEER`) must **never** simultaneously act as its own `QUALITY_REVIEWER` (`ROLE-CORE-004`), `SA_GATE` signoff authority (`ROLE-CORE-002`), or `REPRODUCIBILITY_AUDITOR`.
2. **Builder vs. Security Assessor:**
   - On `Level 4` security-sensitive deliverables, `APPLICATION_SECURITY` / `PENETRATION_TESTER` / `SECURITY_GRC` audit runs inside a separate reviewer context from the feature author.
3. **Clinical / Physical Safety Author vs. Safety Auditor:**
   - `PATIENT_SAFETY_REVIEWER` and `ROBOTICS_SAFETY_VALIDATION_ENGINEER` remain strictly independent of primary implementation workers on `Level 4` safety-critical tasks.

## 3. Domain-Aware Team Selection (Preventing IT-Only Bias)
Before allocating workers, `PM` inspects [`LIBRARY_INDEX.md`](../LIBRARY_INDEX.md) across all **15 canonical domains**:
`IT_SOFTWARE`, `CYBERSECURITY`, `AI_MACHINE_LEARNING`, `ECONOMICS_FINANCE`, `BUSINESS_PRODUCT`, `RESEARCH_SCIENCE`, `LEGAL_COMPLIANCE`, `DESIGN_CREATIVE`, `HEALTHCARE_LIFE_SCIENCES`, `DATA_ANALYTICS`, `MANUFACTURING_INDUSTRIAL`, `ROBOTICS_AUTOMATION`, `SUPPLY_CHAIN_LOGISTICS`, `ENERGY_SUSTAINABILITY`, and `EDUCATION_TRAINING`.
- Never staff non-software deliverables (financial valuation, systematic literature review, regulatory analysis, instructional design, supply-chain network optimization) with generic software engineering roles.
- On multi-domain projects (`Level 3`–`Level 4`), combine domain specialists explicitly (e.g., `CLINICAL_RESEARCHER` + `STATISTICIAN` + `PRIVACY_SPECIALIST` + `DATA_ENGINEER`).
- Appoint a [`DOMAIN_LEAD`](../02_CORE_ROLES/DOMAIN_LEAD/SYSTEM_PROMPT.md) (`ROLE-CORE-003`) whenever specialized domain invariants require pre-gate arbitration.

## 4. Scoped Instruction Loading & Sizing Checklist
- **Scoped Loading Rule:** Every runtime agent loads strictly its assigned role prompt(s), domain system prompt, and `1–4` selected `SKILL.md` files—never unrelated peer role files ([`PROJECT_CONTEXT_MANAGEMENT.md`](./PROJECT_CONTEXT_MANAGEMENT.md)).
- **Pre-Spawn Sizing Gate for `PM + SA`:**
  1. Can `1` agent holding `1–2` compatible roles complete the batch cleanly within context and latency budgets? -> Allocate **`1` agent**.
  2. Are candidate parallel workstreams `100%` file-disjoint with pre-locked `SA` interfaces? -> If **No**, serialize batches or consolidate under `1` owner; if **Yes**, parallelize.
  3. Are subagent tools unavailable in the active harness? -> Execute sequentially inline without fabricating parallel agents.
  4. Does the topology spawn `>= 4` concurrent subagents? -> Record explicit justification in `AGENT_COMMUNICATE.md` demonstrating net wall-clock gain or mandatory Separation of Duties ([`TASK_COMPLEXITY_ROUTER.md`](../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md)).

## 5. Allocation Anti-Patterns to Reject
- **One-Agent-Per-Role Reflex:** Spawning 5 separate subagents for a 100-line task merely because 5 logical roles apply -> merge compatible roles into `1` execution agent (`Pattern A`).
- **Pretending Role Prompts Are Daemons:** Treating `SYSTEM_PROMPT.md` files as continuously running background workers when no subagent process is active.
- **Self-Certifying Critical Work:** Allowing a `Level 4` implementation worker to act as its own `QUALITY_REVIEWER` or safety auditor (`Pattern C` violation).
