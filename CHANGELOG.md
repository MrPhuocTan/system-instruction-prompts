# Changelog

All notable changes to the **Centralized Agent Framework and System Instruction Library** are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this library adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html) as specified in [VERSION.md](./VERSION.md).

---

## [1.0.0] - 2026-11-08

### Added

#### Root Catalog, Versioning & Skill Manifest (`5` files)
- Created [README.md](./README.md) documenting the 10 Design Principles, natural-language-first autonomous orchestration, 9-layer directory organization, 6-level instruction precedence hierarchy, external workspace connection protocol (`.agents/rules/`, `AGENTS.md`, `.agents/skills.json`), 10-step skill discovery workflow, persistent `PM + SA` lifecycle, dynamic subagent creation, extension workflow, and dual quality/security gates.
- Created [LIBRARY_INDEX.md](./LIBRARY_INDEX.md) cataloging all `356` canonical library files across root, constitution, orchestration, `4` core roles, `15` domains (`108` specialist roles), `22` skills, `12` templates, `7` subagent prompts, and `7` walkthrough examples with version, dependency, and usage metadata.
- Created [VERSION.md](./VERSION.md) locking baseline release `1.0.0` (`2026-11-08`) and establishing `MAJOR.MINOR.PATCH` governance rules.
- Created [CHANGELOG.md](./CHANGELOG.md) establishing auditable Keep-a-Changelog release tracking.
- Created [skills.json](./skills.json) conforming to Antigravity's native customization schema (`entries` pointing to `04_CROSS_DOMAIN_SKILLS` and `05_SPECIALIZED_SKILLS` for cross-project `inherits` consumption).

#### Global Constitution (`00_GLOBAL_CONSTITUTION/` — `8` files)
- Added [GLOBAL_SYSTEM_PROMPT.md](./00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) and [AGENT_GOVERNANCE.md](./00_GLOBAL_CONSTITUTION/AGENT_GOVERNANCE.md) codifying the 10 Core Design Principles, 6-level instruction precedence hierarchy (`Level 1` Runtime/Authorization through `Level 6` Procedural Skills), and vertical/horizontal conflict resolution algorithm.
- Added [TASK_COMPLEXITY_ROUTER.md](./00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md) defining objective triage across `Level 0` (Direct Factual Lookup) through `Level 4` (High-Assurance / Regulated Multi-Domain Program).
- Added [COGNITIVE_EXECUTION.md](./00_GLOBAL_CONSTITUTION/COGNITIVE_EXECUTION.md) and [INDEPENDENT_VERIFICATION.md](./00_GLOBAL_CONSTITUTION/INDEPENDENT_VERIFICATION.md) enforcing structured pre-action reasoning, assumption ledgering, and post-action empirical verification (`Tool Success != Task Success`).
- Added [SECURITY_AND_PRIVACY.md](./00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md), [TOOL_USAGE_AND_LIMITATIONS.md](./00_GLOBAL_CONSTITUTION/TOOL_USAGE_AND_LIMITATIONS.md), and [HUMAN_APPROVAL_POLICY.md](./00_GLOBAL_CONSTITUTION/HUMAN_APPROVAL_POLICY.md) governing least privilege, secret/PII protection, verified Antigravity tool mechanics, honest runtime limitation disclosures, and mandatory human approval triggers.

#### Multi-Agent Orchestration (`01_ORCHESTRATION/` — `13` files)
- Added [AUTONOMOUS_ORCHESTRATION.md](./01_ORCHESTRATION/AUTONOMOUS_ORCHESTRATION.md) (`SEC-18`) enforcing natural-language-first user interaction with zero manual command modes (`INIT`/`CONTINUE`/`DOMAIN`/`ROLE`/`AUDIT`/`STATUS`), autonomous handling of all 13 internal orchestration phases, checkpoint auto-resume, and sequential/state-file runtime fallbacks.
- Added [ORCHESTRATION_SYSTEM_PROMPT.md](./01_ORCHESTRATION/ORCHESTRATION_SYSTEM_PROMPT.md), [PROJECT_INITIALIZATION.md](./01_ORCHESTRATION/PROJECT_INITIALIZATION.md), [PROJECT_CONTEXT_MANAGEMENT.md](./01_ORCHESTRATION/PROJECT_CONTEXT_MANAGEMENT.md), and [PERSISTENT_PM_SA.md](./01_ORCHESTRATION/PERSISTENT_PM_SA.md) establishing intra-session `conversationId` reuse via `send_message` and cross-session state persistence on disk.
- Added [DYNAMIC_AGENT_ALLOCATION.md](./01_ORCHESTRATION/DYNAMIC_AGENT_ALLOCATION.md) and [SUBAGENT_CREATION.md](./01_ORCHESTRATION/SUBAGENT_CREATION.md) separating static specialist Roles from runtime Agent instances and codifying the 10-step skill discovery and loading sequence.
- Added [WORKSTREAM_MANAGEMENT.md](./01_ORCHESTRATION/WORKSTREAM_MANAGEMENT.md), [AGENT_COMMUNICATION.md](./01_ORCHESTRATION/AGENT_COMMUNICATION.md), [FILE_OWNERSHIP_AND_LOCKING.md](./01_ORCHESTRATION/FILE_OWNERSHIP_AND_LOCKING.md), [CONTRACT_AND_HANDOFF.md](./01_ORCHESTRATION/CONTRACT_AND_HANDOFF.md), [REVIEW_AND_SIGNOFF.md](./01_ORCHESTRATION/REVIEW_AND_SIGNOFF.md), and [PROGRESS_REPORTING.md](./01_ORCHESTRATION/PROGRESS_REPORTING.md) enforcing disjoint Exclusive Write-Locks, contract-first handoffs, `SA_GATE` + `PM_GATE` dual sign-off, and `schedule`-driven 20-minute progress reporting.

#### Core Governance Roles (`02_CORE_ROLES/` — `4` roles, `8` files)
- Added `SYSTEM_PROMPT.md` and `QUALITY_CHECKLIST.md` packages for `PROJECT_MANAGER` (`ROLE-CORE-001`), `SYSTEM_ARCHITECT` (`ROLE-CORE-002`), `DOMAIN_LEAD` (`ROLE-CORE-003`), and `QUALITY_REVIEWER` (`ROLE-CORE-004`).

#### Specialized 15-Domain Role Library (`03_DOMAINS/` — `15` domains, `108` specialist roles, `274` files)
- Added `DOMAIN_INDEX.md`, `DOMAIN_SYSTEM_PROMPT.md`, and `QUALITY_GATES.md` (`45` domain-level files) plus `SYSTEM_PROMPT.md` (covering all 9 mandatory architectural sections) and `QUALITY_CHECKLIST.md` across all `108` domain specialist roles:
  - `IT_SOFTWARE` (`11` roles: `ROLE-IT-001` through `ROLE-IT-011`, `25` files)
  - `CYBERSECURITY` (`13` roles: `ROLE-CYB-001` through `ROLE-CYB-013`, `42` files including dedicated `WORKFLOW.md` per role and strict written authorization, target scope, and Rules of Engagement safety controls)
  - `AI_MACHINE_LEARNING` (`10` roles: `ROLE-AIML-001` through `ROLE-AIML-010`, `23` files)
  - `ECONOMICS_FINANCE` (`10` roles: `ROLE-FIN-001` through `ROLE-FIN-010`, `23` files)
  - `BUSINESS_PRODUCT` (`7` roles: `ROLE-BIZ-001` through `ROLE-BIZ-007`, `17` files)
  - `RESEARCH_SCIENCE` (`6` roles: `ROLE-SCI-001` through `ROLE-SCI-006`, `15` files)
  - `LEGAL_COMPLIANCE` (`6` roles: `ROLE-LEG-001` through `ROLE-LEG-006`, `15` files)
  - `DESIGN_CREATIVE` (`7` roles: `ROLE-DES-001` through `ROLE-DES-007`, `17` files)
  - `HEALTHCARE_LIFE_SCIENCES` (`6` roles: `ROLE-HLT-001` through `ROLE-HLT-006`, `15` files)
  - `DATA_ANALYTICS` (`7` roles: `ROLE-DATA-001` through `ROLE-DATA-007`, `17` files)
  - `MANUFACTURING_INDUSTRIAL` (`5` roles: `ROLE-MFG-001` through `ROLE-MFG-005`, `13` files)
  - `ROBOTICS_AUTOMATION` (`5` roles: `ROLE-ROB-001` through `ROLE-ROB-005`, `13` files)
  - `SUPPLY_CHAIN_LOGISTICS` (`5` roles: `ROLE-SCM-001` through `ROLE-SCM-005`, `13` files)
  - `ENERGY_SUSTAINABILITY` (`5` roles: `ROLE-ENG-001` through `ROLE-ENG-005`, `13` files)
  - `EDUCATION_TRAINING` (`5` roles: `ROLE-EDU-001` through `ROLE-EDU-005`, `13` files)

#### Cross-Domain & Specialized Reusable Skills (`04_CROSS_DOMAIN_SKILLS/` & `05_SPECIALIZED_SKILLS/` — `22` skills)
- Added `12` cross-domain `SKILL.md` packages (`SKL-CORE-001` through `SKL-CORE-012`: `COGNITIVE_EXECUTION`, `CRITICAL_THINKING`, `SYSTEMS_THINKING`, `RESEARCH_AND_SOURCE_VALIDATION`, `DATA_INTERPRETATION`, `DECISION_ANALYSIS`, `TECHNICAL_WRITING`, `DOCUMENTATION`, `QUALITY_ASSURANCE`, `RISK_MANAGEMENT`, `COMMUNICATION`, `REQUIREMENTS_ANALYSIS`) with Antigravity YAML frontmatter and 13 mandatory operational sections.
- Added `10` specialized `SKILL.md` packages (`SKL-SPEC-001` through `SKL-SPEC-010`: `HUMAN_CENTRIC_APPLICATION_QA` with 3-level QA gates, `BROWSER_AND_GUI_INTERACTION`, `API_TESTING`, `DATABASE_VALIDATION`, `PERFORMANCE_BENCHMARKING`, `SECURITY_ASSESSMENT`, `FINANCIAL_MODEL_VALIDATION`, `SCIENTIFIC_REPRODUCIBILITY`, `MODEL_EVALUATION`, `SKILL_DISCOVERY_AND_LOADING`).

#### Operational Templates, Subagent Prompts & Walkthrough Examples (`06_TEMPLATES/`, `07_SUBAGENT_PROMPTS/`, `08_EXAMPLES/` — `26` files)
- Added `12` operational project templates in `06_TEMPLATES/`, including [PROJECT_MANIFEST.md](./06_TEMPLATES/PROJECT_MANIFEST.md), [PROJECT_STATE.md](./06_TEMPLATES/PROJECT_STATE.md), the 15-section [AGENT_COMMUNICATE.md](./06_TEMPLATES/AGENT_COMMUNICATE.md) coordination bus, contracts, handoff reports, technical/business reviews, QA reports, risk registers, and final delivery summaries.
- Added `7` subagent invocation prompts in `07_SUBAGENT_PROMPTS/`, anchored by the 16-field [SUBAGENT_CREATION_PROMPT.md](./07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md) plus domain worker, research, implementation, QA, security, and reviewer blueprints.
- Added `7` end-to-end walkthrough examples in `08_EXAMPLES/` demonstrating `Level 0` through `Level 4` execution across software engineering, AI/ML, authorized cybersecurity assessment, financial analysis, and multi-domain programs.

#### Deterministic Architecture & Inventory Validation (`scripts/validate_library.py`)
- Added `scripts/validate_library.py` (stdlib Python 3 CLI + `pytest` suite) validating `356/356` canonical files, `< 24 KB` per-rule size caps, `skills.json` schema rules, YAML frontmatter, autonomous natural-language orchestration invariants (`SEC-18`), role/skill/template structural contracts, Cybersecurity RoE guardrails, content hygiene, and 100% relative Markdown link integrity.
