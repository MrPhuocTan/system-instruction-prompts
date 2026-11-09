# Library Version Specification

- **Current Version:** `1.0.0`
- **Release Date:** `2026-11-08`
- **Versioning Standard:** Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`)
- **Canonical File Inventory:** `356` files (`5` root + `351` across `00_GLOBAL_CONSTITUTION` through `08_EXAMPLES`)

---

## 1. Semantic Versioning Policy (`MAJOR.MINOR.PATCH`)

All modifications to `<LIBRARY_ROOT>` are governed by deterministic Semantic Versioning rules so downstream workspaces inheriting rules or [skills.json](./skills.json) maintain predictable compatibility:

### `MAJOR` Version Increment (`X.0.0`)
Increment `MAJOR` whenever making incompatible or breaking architectural changes that require downstream workspaces or active orchestration harnesses to update their bootstrap rules, state schemas, or contract parsers:
- Altering or reordering the 6-level Instruction Precedence Hierarchy in [GLOBAL_SYSTEM_PROMPT.md](./00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) or [AGENT_GOVERNANCE.md](./00_GLOBAL_CONSTITUTION/AGENT_GOVERNANCE.md).
- Removing, renaming, or relocating canonical directories (`00_GLOBAL_CONSTITUTION` through `08_EXAMPLES`), Role IDs (`ROLE-*`), or Skill IDs (`SKL-*`).
- Changing mandatory structural schemas across role prompts (`9` required sections), skill packages (`YAML` frontmatter + `13` required sections), [AGENT_COMMUNICATE.md](./06_TEMPLATES/AGENT_COMMUNICATE.md) (`15` sections), [SUBAGENT_CREATION_PROMPT.md](./07_SUBAGENT_PROMPTS/SUBAGENT_CREATION_PROMPT.md) (`16` fields), or root [skills.json](./skills.json).
- Weakening or restructuring mandatory human approval, privacy, or Cybersecurity Rules of Engagement (`RoE`) boundaries.

### `MINOR` Version Increment (`1.Y.0`)
Increment `MINOR` whenever adding backward-compatible capabilities without breaking existing relative paths, Role IDs, Skill IDs, or governance contracts:
- Adding a new specialist domain package under `03_DOMAINS/<NEW_DOMAIN>/` (`DOMAIN_INDEX.md`, `DOMAIN_SYSTEM_PROMPT.md`, `QUALITY_GATES.md`, and `ROLES/`).
- Adding new specialist roles (`SYSTEM_PROMPT.md` + `QUALITY_CHECKLIST.md`, plus `WORKFLOW.md` for Cybersecurity) within an existing domain.
- Adding new cross-domain skills (`04_CROSS_DOMAIN_SKILLS/<SKILL>/SKILL.md`) or specialized skills (`05_SPECIALIZED_SKILLS/<SKILL>/SKILL.md`).
- Adding new project templates (`06_TEMPLATES/`), subagent invocation blueprints (`07_SUBAGENT_PROMPTS/`), or end-to-end walkthroughs (`08_EXAMPLES/`).

### `PATCH` Version Increment (`1.0.Z`)
Increment `PATCH` for backward-compatible refinements that preserve all existing file paths, schemas, and authority boundaries:
- Clarifying domain methodologies, decision heuristics, failure modes, or quality checklist items.
- Fixing typographical errors, Markdown formatting defects, or relative link targets.
- Tightening verification commands or adding non-breaking validation checks in `scripts/validate_library.py`.

---

## 2. Canonical Baseline Inventory (`v1.0.0`)

| Layer | Path Scope | Canonical File Count |
| :--- | :--- | ---: |
| Root Catalog & Manifest | [README.md](./README.md), [LIBRARY_INDEX.md](./LIBRARY_INDEX.md), [VERSION.md](./VERSION.md), [CHANGELOG.md](./CHANGELOG.md), [skills.json](./skills.json) | `5` |
| Global Constitution | `00_GLOBAL_CONSTITUTION/` | `8` |
| Multi-Agent Orchestration | `01_ORCHESTRATION/` (including [AUTONOMOUS_ORCHESTRATION.md](./01_ORCHESTRATION/AUTONOMOUS_ORCHESTRATION.md)) | `13` |
| Core Governance Roles | `02_CORE_ROLES/` (`4` roles x `2` files) | `8` |
| Domain Specialist Library | `03_DOMAINS/` (`15` domains, `108` roles, including `13` Cybersecurity `WORKFLOW.md` files) | `274` |
| Cross-Domain Skills | `04_CROSS_DOMAIN_SKILLS/` (`12` skills) | `12` |
| Specialized Skills | `05_SPECIALIZED_SKILLS/` (`10` skills) | `10` |
| Project Templates | `06_TEMPLATES/` | `12` |
| Subagent Prompts | `07_SUBAGENT_PROMPTS/` | `7` |
| Walkthrough Examples | `08_EXAMPLES/` | `7` |
| **Total** | **Complete Locked `v1.0.0` Library** | **`356`** |

---

## 3. Release Verification Gate

Every version update requires:
1. Updating `Current Version` and `Release Date` in [VERSION.md](./VERSION.md) and synchronizing modified skill `Version` fields.
2. Recording categorized release notes in [CHANGELOG.md](./CHANGELOG.md) and updating [LIBRARY_INDEX.md](./LIBRARY_INDEX.md) for any added or retired files.
3. Passing deterministic validation (`python3 scripts/validate_library.py` exiting `0`) and obtaining `SA_GATE` + `PM_GATE` sign-off.
