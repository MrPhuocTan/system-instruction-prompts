---
name: requirements-analysis
description: "Use this skill when translating user requests, business goals, or domain problems into unambiguous functional specifications, non-functional constraints, scope boundaries, edge cases, and testable acceptance criteria."
---

# Requirements Analysis

## Skill Metadata
- **Skill ID:** `SKL-CORE-012`
- **Name:** `requirements-analysis`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Convert high-level, incomplete, or solution-biased user requests into structured, conflict-free, and testable engineering or analytical requirements. This skill surfaces implicit domain invariants, non-functional constraints, negative scope boundaries, state-machine edge cases, and measurable acceptance criteria before design or parallel implementation locks contracts.

## Required Competencies
- Problem-vs-solution separation (identifying underlying user jobs-to-be-done vs. prematurely prescribed implementation mechanisms).
- Functional decomposition (actors, preconditions, triggers, state transitions, invariants, error paths, postconditions).
- Non-Functional Requirements (`NFR`) specification across latency/throughput, availability, data consistency, security/privacy, accessibility, regulatory compliance, and host resource limits.
- Testable acceptance-criteria authoring (`Given / When / Then` and quantitative threshold gates) and scope boundary locking (`In-Scope` vs. `Out-of-Scope`).

## Prerequisites
- Raw user prompt, stakeholder brief, legacy codebase, or domain problem context inspected via `read_file`.
- Complexity level assessed via [TASK_COMPLEXITY_ROUTER.md](../../00_GLOBAL_CONSTITUTION/TASK_COMPLEXITY_ROUTER.md) and active domain(s) identified.
- Coordination with `PM` (scope/UX/value) and `SA` (technical feasibility/contracts) on Level 2-4 initiatives.

## Workflow
1. **Extract Core Objective & Actors:** Identify primary human/system actors, the real business or research outcome desired, and existing workspace assets/constraints before accepting surface implementation assumptions.
2. **Elicit Functional Flows & State Transitions:** Specify nominal flows alongside explicit exception flows (unauthorized access, malformed payloads, concurrent conflicting updates, partial upstream failure, empty-state cold start, cancellation/rollback).
3. **Quantify Non-Functional & Domain Constraints (`NFRs`):** Pin concrete bounds for performance (`p95/p99` latency, batch window), scale, security/compliance (GDPR, HIPAA, PCI, OWASP, RoE), accessibility (`WCAG 2.1 AA`), licensing, and hardware/disk/thermal envelopes.
4. **Detect Contradictions & Hidden Dependencies:** Screen requirements for mutually incompatible goals (e.g., zero-latency synchronous consensus across geo-distributed nodes, or strict offline air-gap alongside live SaaS API calls) and surface trade-offs via [DECISION_ANALYSIS](../DECISION_ANALYSIS/SKILL.md).
5. **Lock Explicit Scope Boundaries:** Enumerate exact `In-Scope` deliverables and `Out-of-Scope` non-goals to prevent scope creep and overlapping parallel subagent edits.
6. **Formulate Verifiable Acceptance Criteria:** Write deterministic pass/fail criteria for every requirement so [QUALITY_ASSURANCE](../QUALITY_ASSURANCE/SKILL.md) and `PM_GATE` / `SA_GATE` reviewers can prove completion empirically without subjective debate.

## Tools and Techniques
- **`EARS` Syntax (Easy Approach to Requirements Syntax):** Author unambiguous clauses using *Ubiquitous* (`The system SHALL...`), *Event-Driven* (`WHEN <trigger>, the system SHALL...`), *State-Driven* (`WHILE <state>, the system SHALL...`), and *Unwanted-Behavior* (`IF <error>, THEN the system SHALL...`) templates.
- **CRUD / Lifecycle Completeness Matrix:** Verify every entity or artifact covers creation, read/list/empty-state, update/idempotency, deletion/archival, authorization, and audit logging.
- **Ambiguity Elimination Sweep:** Flag and replace non-testable adjectives (`intuitive`, `near real-time`, `flexible`, `enterprise-grade`, `etc.`) with explicit behaviors and numeric thresholds.
- **Targeted Stakeholder Clarification:** Use `ask_question` strictly for genuine intent/policy choices that cannot be derived from repository files or domain standards.

## Verification Requirements
- Every functional and non-functional requirement is atomic, internally consistent, feasible within Antigravity runtime/environment constraints, and paired with an objective verification check.
- Zero unresolved conflicting requirements remain prior to locking [WORKSTREAM_CONTRACT.md](../../06_TEMPLATES/WORKSTREAM_CONTRACT.md) on parallel builds.
- Explicit assumptions made when defaults are applied are documented clearly for `PM` and user visibility.

## Quality Criteria
- **100% Testability:** An independent QA engineer or auditor can determine `PASS` vs. `FAIL` for every requirement without asking the author what they meant:
  | Vague Prompt Phrasing (Reject) | Concrete Testable Specification (Enforce) |
  | :--- | :--- |
  | `"Make the search fast and scalable"` | `GET /search` returns `p95 <= 150 ms` and `p99 <= 300 ms` at `200 RPS` over `1M` indexed rows |
  | `"Handle invalid uploads gracefully"` | Reject non-PDF/PNG files or payloads `> 10 MB` with `HTTP 422` and field-level error code |
  | `"Ensure secure multi-tenant access"` | Enforce `tenant_id` row scoping on `100%` of queries; cross-tenant IDs return `404/403` |
  | `"Support exports, reports, etc."` | Enumerate exact export formats (`CSV UTF-8`, `PDF`) and explicit `Out-of-Scope` exclusions |
- **Complete Edge-Case Coverage:** Empty states, invalid inputs, permission denials, concurrency races, and failure recovery are specified upfront, not discovered mid-coding.
- **Clean Scope Discipline:** Prevents gold-plating and unrequested architectural sprawl while ensuring user-critical journeys work end to end.
- **Failure Modes to Avoid:**
  - *Premature Coding:* Jumping straight into implementation against contradictory or underspecified prompts.
  - *Buzzword Echoing:* Copying `"enterprise-grade"`, `"seamless"`, or `"etc."` into contracts without measurable thresholds.
  - *Happy-Path Specification:* Defining nominal creation flows while omitting idempotency, cancellation, empty states, and rollback.
  - *Silent Scope Expansion:* Adding unrequested subsystems that collide with sibling subagent write-locks.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md), legal boundaries, or safety policies.
- Automatically embed mandatory security, privacy, secret-protection, and authorization invariants as baseline requirements even when omitted from a user's informal prompt.
- Refuse or escalate any requirement requesting unauthorized access bypass, covert surveillance, deceptive dark patterns, or regulatory evasion.

## Expected Deliverables
- **Structured Requirements Specification** covering user objectives, actors, `In-Scope` / `Out-of-Scope` boundaries, functional flows, edge cases, and `NFR` thresholds.
- **Testable Acceptance Criteria Checklist** (`Given / When / Then` + measurable bounds) mapped directly to verification methods.
- **Assumptions, Contradictions & Open Questions Log** documenting resolved defaults and any items escalated for stakeholder sign-off.
