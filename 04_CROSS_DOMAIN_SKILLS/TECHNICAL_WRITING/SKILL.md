---
name: technical-writing
description: "Use this skill when authoring RFCs, engineering specifications, research reports, postmortems, regulatory filings, or executive briefs requiring high information density, unambiguous terminology, and zero filler."
---

# Technical Writing

## Skill Metadata
- **Skill ID:** `SKL-CORE-007`
- **Name:** `technical-writing`
- **Domain:** `CROSS_DOMAIN`
- **Version:** `1.0.0`

## Purpose
Produce high-precision, scannable, and audience-calibrated technical documents—including RFCs, formal specifications, incident postmortems, audit reports, whitepapers, and policy standards—that convey complex domain mechanics with zero ambiguity and zero decorative "AI Sign" fluff.

## Required Competencies
- Audience task modeling (executive decision-makers vs. implementing engineers vs. compliance auditors vs. operators).
- Bottom-Line-Up-Front (`BLUF`) Pyramid structuring, normative language precision (`MUST`, `MUST NOT`, `SHOULD`, `MAY` per RFC 2119), and controlled terminology glossaries.
- Information architecture: visual hierarchy, orthogonal Markdown tables, deterministic Mermaid diagrams, and exact inline code/equation formatting.
- Ruthless editorial pruning of passive-voice evasion, marketing superlatives, weasel words, and repetitive transition filler.

## Prerequisites
- Verified technical facts, architectural contracts, or empirical findings compiled via [RESEARCH_AND_SOURCE_VALIDATION](../RESEARCH_AND_SOURCE_VALIDATION/SKILL.md) or [DATA_INTERPRETATION](../DATA_INTERPRETATION/SKILL.md).
- Clear identification of primary reader persona, decision action required from the reader, and target deliverable path within exclusive write-locks.
- Terminology alignment with domain standards and existing project glossaries.

## Workflow
1. **Define Reader Persona & Action Objective:** Specify exactly who reads the document, what baseline context they possess, and what concrete action or decision the document enables.
2. **Structure via `BLUF` & Progressive Depth:** Open with a concise executive summary (`Outcome`, `Scope`, `Key Decisions/Findings`, `Action Required`), followed by structured normative sections, detailed evidence tables, and appendices.
3. **Lock Canonical Terminology & Normative Modals:** Define domain terms once and use identical nouns throughout (never alternate synonyms for the same component or metric). Apply RFC 2119 modals (`MUST`, `SHOULD`, `MAY`) explicitly in specifications.
4. **Author Concrete, Active-Voice Prose:** Attribute every action to an explicit actor or system module (`The API gateway rejects expired JWTs with HTTP 401` rather than `Tokens are validated appropriately`). Pair abstract rules with concrete input/output examples.
5. **Integrate Structured Tables & Validated Diagrams:** Replace dense multi-clause paragraphs with comparison tables, numbered state transitions, or valid Mermaid diagrams (`flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `erDiagram`).
6. **Execute Editorial, Hygiene & Link Audit:** Strip promotional adjectives, decorative emojis, and unfinished markers; verify every relative file link, command flag, metric unit, and cross-reference against primary workspace artifacts.

## Tools and Techniques
- **RFC 2119 Precision Audit:** Replace vague qualifiers (`fast`, `secure`, `scalable`, `seamless`, `robust`) with measurable bounds (`p99 < 120 ms at 500 RPS`, `AES-256-GCM`, `RPO <= 5 min`).
- **Actor-Action-Outcome Sentence Pattern:** Ensure every operational requirement names *who/what* acts, *under what trigger*, *performing what operation*, and *producing what observable state*.
- **Anti-"AI Sign" Editorial Filter:** Eliminate throat-clearing openings (`In today's rapidly evolving landscape...`), emoji-stuffed headings, and hollow summary repetitions.
- **Deterministic Link & Path Check:** Verify referenced files and symbols via `read_file` and `run_command` so zero broken links or invented CLI flags enter deliverables.

## Verification Requirements
- All quantitative figures, CLI flags, config keys, equations, and citations in prose match underlying source code or verified analytical outputs 100%.
- Every relative Markdown link resolves on disk, and illustrative non-existent target paths are formatted in inline backticks rather than broken links.
- Mermaid code blocks use supported diagram types with quoted labels containing special characters so rendering succeeds without syntax errors.

## Quality Criteria
- **Immediate Scannability:** A reader scanning headings, bold lead-ins, and tables grasps the complete decision and operational constraints in under two minutes:
  | Document Archetype | Mandatory Opening (`BLUF`) | Core Structural Body |
  | :--- | :--- | :--- |
  | `Engineering RFC / Spec` | Status, Context, Decision, Non-Goals | Invariants, Interface Contracts, Failure Modes, Rollout Plan |
  | `Incident Postmortem` | Impact Window, Root Cause, Customer Blast Radius | Minute-by-Minute Timeline, `5 Whys`, Preventive Action Items |
  | `Executive / Audit Brief` | Verdict, Quantified Exposure, Required Action | Methodology, Triaged Evidence Table, Risk-Ranked Recommendations |
- **Zero Referential Ambiguity:** No dangling pronouns (`this`, `it`, `they`), undefined acronyms, or conflicting terms across sections.
- **Clean Utilitarian Presentation:** Crisp engineering prose free of decorative emojis, marketing buzzwords, or placeholder tokens.
- **Failure Modes to Avoid:**
  - *Buried Lead:* Hiding breaking changes, security exposures, or budget overruns deep inside late paragraphs.
  - *Passive-Voice Evasion:* Writing `"Mistakes were made and validation was skipped"` instead of naming exact system components and gaps.
  - *Weasel Qualifiers:* Leaving non-testable words (`fast`, `robust`, `adequate`) where exact numeric SLOs belong.
  - *Decorative "AI Sign" Prose:* Padding technical specs with hollow transitions, emoji bullets, or self-congratulatory summaries.

## Security and Ethical Boundaries
- This Level 6 procedural skill is strictly subordinate to Levels 1-5 of the instruction hierarchy; it never overrides [GLOBAL_SYSTEM_PROMPT.md](../../00_GLOBAL_CONSTITUTION/GLOBAL_SYSTEM_PROMPT.md) or confidentiality boundaries.
- Scrub live API keys, internal credentials, customer PII, and proprietary secrets from examples, logs, and screenshots before writing documents (`<REDACTED_SECRET>`).
- Never overstate verification status or mask unresolved defects behind optimistic phrasing.

## Expected Deliverables
- **Publication-Ready Technical Document** (`RFC`, specification, postmortem, audit report, or executive brief) structured with `BLUF` clarity.
- **Terminology & Normative Constraints Table** locking key definitions, units, and RFC 2119 compliance rules.
- **Verified Cross-Reference & Artifact Index** linking supporting code, schemas, datasets, or authoritative sources.
