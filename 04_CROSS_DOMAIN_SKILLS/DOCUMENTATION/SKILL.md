---
name: documentation
description: "Use this skill when creating or maintaining living repository documentation, API references, architecture guides, operational runbooks, onboarding playbooks, or changelogs synchronized with system behavior."
---

# Documentation

## Skill Metadata
- **Skill ID:** `SKL-CORE-008`
- **Name:** `documentation`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Design, author, and synchronize living operational and developer documentation systems so engineers, operators, analysts, and downstream agents can install, integrate, operate, troubleshoot, and evolve a project without tribal knowledge or code-to-doc drift.

## Required Competencies
- Documentation architecture using the **Diataxis Framework** (*Tutorials* for learning, *How-To Guides* for task execution, *Reference* for exhaustive contract lookup, *Explanation* for architectural rationale).
- Machine-synced API/CLI/schema reference authoring (`OpenAPI`, `JSON Schema`, `--help` CLI parity, config environment tables).
- Production runbook and Standard Operating Procedure (`SOP`) engineering with copy-pasteable diagnostics, rollback steps, and blast-radius warnings.
- Semantic versioning (`SemVer`) changelog curation (`Keep a Changelog`), deprecation lifecycle notices, and migration playbooks.

## Prerequisites
- Direct inspection of source code, build scripts, configuration loaders, CLI entrypoints, and tests via `read_file` and `run_command`.
- Assigned documentation write-lock paths confirmed in [AGENT_COMMUNICATE.md](../../06_TEMPLATES/AGENT_COMMUNICATE.md) when working in parallel streams.
- Clarity principles from [TECHNICAL_WRITING](../TECHNICAL_WRITING/SKILL.md) applied to prose formatting.

## Workflow
1. **Audit Existing Docs Against Ground-Truth Code:** Inspect repository entrypoints, environment variable parsers, package scripts, and schemas first; catalog stale commands, undocumented prerequisites, and dead links.
2. **Partition by Diataxis Mode (Never Mix Concerns):** Keep step-by-step *How-To* runbooks separate from exhaustive *Reference* parameter tables and conceptual *Architecture Explanations* so each artifact stays focused and maintainable.
3. **Author Reproducible Setup & Task Guides:** Document exact OS/runtime prerequisites, deterministic installation commands, required environment variables (with safe example defaults), expected command outputs, and common error fixes.
4. **Build Exhaustive Interface References:** Document every public endpoint, CLI flag, config key, type, default value, validation constraint, error code, and idempotency guarantee directly from source definitions.
5. **Write Operational Runbooks & Migration Notes:** For operational systems or breaking changes, specify pre-flight checks, exact execution commands, health verification probes, rollback procedures, and escalation contacts.
6. **Verify Every Command & Example Empirically:** Execute documented setup, build, test, and CLI examples via `run_command` (or compile-check code snippets) to prove zero drift between documentation and reality.

## Tools and Techniques
- **Diataxis Matrix Mapping:** Explicitly tag each document section's mode (*Quickstart*, *How-To*, *Reference*, *Architecture/ADR*) to prevent sprawling monolithic `README` dumps.
- **Single-Source Reference Extraction:** Generate or cross-verify CLI flags (`--help`), OpenAPI specs, and config tables directly against code constants via `run_command`.
- **Runbook Safety Callouts:** Place explicit `Pre-Check`, `Impact`, `Command`, `Expected Output`, and `Rollback` blocks around any state-mutating operational step.
- **Keep-a-Changelog Discipline:** Group release changes strictly under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, and `Security` with exact migration instructions for breaking changes.

## Verification Requirements
- Every documented shell command, file path, config variable name, port, and code import is verified against the live workspace (`Tool Success != Task Success`: run commands where safe, or verify exact parser definitions).
- Zero broken internal Markdown links across repository docs; single-source-of-truth links replace copy-pasted duplicate instructions.
- Fresh-clone mental/empirical walkthrough confirms no hidden global dependencies or undocumented `.env` keys block onboarding.

## Quality Criteria
- **Zero Code-to-Doc Drift:** Parameter names, types, defaults, and CLI outputs match the current commit exactly:
  | Diataxis Quadrant | Primary Reader Goal | Mandatory Structural Focus |
  | :--- | :--- | :--- |
  | `Tutorial (Quickstart)` | First successful end-to-end run | Deterministic `<= 5 min` path with verified copy-paste outputs |
  | `How-To / Runbook` | Accomplish a concrete operational task | Pre-checks, exact commands, expected health signals, rollback |
  | `Reference` | Look up exact contract details | Exhaustive flags, types, defaults, error codes, idempotency |
  | `Explanation (ADR)` | Understand architectural *why* | Context, trade-offs, system invariants, rejected alternatives |
- **Copy-Paste Operational Safety:** Runbook commands use explicit safe flags, placeholder variable names (`<TARGET_ENV>`), and verification checks before destructive steps.
- **Progressive Discoverability:** Root `README` or index routes readers cleanly to deeper architecture, API, and operational modules within two clicks.
- **Failure Modes to Avoid:**
  - *Aspirational Fiction:* Documenting planned future endpoints or flags as if they already work in the codebase.
  - *Duplicate-Table Rot:* Copy-pasting environment variable tables across multiple Markdown files instead of linking one canonical table.
  - *One-Way Runbooks:* Writing state-mutating deployment steps with zero verification probes or rollback commands.
  - *Hidden Local Tribalism:* Omitting required system libraries, seed steps, or port prerequisites that worked only on the author's machine.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [SECURITY_AND_PRIVACY.md](../../00_GLOBAL_CONSTITUTION/SECURITY_AND_PRIVACY.md) or workspace rule caps (`< 24 KB` per rule file).
- Use synthetic example values (`example.com`, `192.0.2.0/24` RFC 5737 TEST-NET, `<YOUR_API_TOKEN>`)—never commit real internal IPs, private stream endpoints, or live credentials in documentation.
- Clearly warn operators before any documented command that truncates data, restarts services, or modifies access controls.

## Expected Deliverables
- **Synchronized Documentation Artifact(s)** (`README`, API/CLI reference, architecture guide, operational runbook, or `CHANGELOG` / migration guide).
- **Environment & Configuration Reference Table** listing keys, types, defaults, secret sensitivity, and validation rules.
- **Doc-to-Code Verification Log** confirming empirical validation of commands, links, and code snippets.
