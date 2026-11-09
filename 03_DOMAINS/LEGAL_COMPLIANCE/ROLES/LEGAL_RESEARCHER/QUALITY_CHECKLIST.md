# Quality Checklist: Legal Researcher (`ROLE-LEG-001`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass before marking workstream status `PASS`.

## 1. Jurisdictional & Temporal Precision
- [ ] Governing jurisdiction(s) (supranational, federal/national, state/provincial) and court/forum hierarchy are explicitly named in Section 1 of the deliverable.
- [ ] Effective dates, statutory amendment windows, and retroactive vs. prospective applicability are verified and stated.
- [ ] Conflict-of-laws or preemption rules (e.g., federal vs. state preemption, EU Regulation direct applicability vs. Directive transposition) are analyzed where multiple regimes intersect.

## 2. Primary Source & Anti-Fabrication Verification (`ZERO TOLERANCE`)
- [ ] Every cited statute, regulation, constitutional provision, treaty article, or judicial opinion was directly inspected via `read_file` or authoritative `search_web` portals.
- [ ] Zero fabricated, guessed, or reconstructed reporter volumes, page numbers, docket IDs, or statutory subsections appear anywhere in the text.
- [ ] Direct quotations match the primary text verbatim, with omissions/alterations accurately marked using standard legal notation (`[...]`).
- [ ] Any authority whose full text or commercial citator ("good law") status could not be verified via public sources is explicitly flagged `[UNVERIFIED - REQUIRES CITATOR/REPORTER CHECK]`.

## 3. Doctrinal & Structural Completeness
- [ ] Controlling binding precedent is explicitly distinguished from persuasive authority, secondary commentary, agency FAQs, and obiter dicta.
- [ ] Statutory definitions, scope thresholds, exemptions, safe harbors, and affirmative defenses surrounding the cited provision have been checked.
- [ ] Each legal question is structured cleanly via IRAC or CRAC with explicit elements, burden of proof, and remedies/penalties identified.
- [ ] Adverse precedent, circuit/jurisdictional splits, and strongest counter-arguments are surfaced and evaluated honestly rather than omitted.

## 4. Uncertainty, Confidentiality & Counsel Sign-Off Hygiene
- [ ] Settled black-letter rules are separated from unsettled questions and missing factual assumptions (`If Fact X -> Outcome A; If Fact Y -> Outcome B`).
- [ ] External `search_web` queries were sanitized to abstract legal concepts—zero client names, MNPI, PII, or privileged facts leaked externally.
- [ ] Prominent non-representation notice and mandatory human review checkpoint by qualified legal counsel in the applicable jurisdiction(s) are included prior to reliance.
- [ ] Prose is crisp, analytical, and free of decorative emojis, filler superlatives, or broken relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Jurisdiction, Forum & Effective Date | Governing forum, statutory code version, and temporal window pinned | `PASS / BLOCKED / FAILED` |
| Primary Citation & Verbatim Quote Audit | `read_file` / official `search_web` source match (`0` fabricated cites) | `PASS / BLOCKED / FAILED` |
| Binding vs. Persuasive & Counter-Authority | IRAC/CRAC balance + split/adverse precedent explicitly evaluated | `PASS / BLOCKED / FAILED` |
| Sanitized Queries & Confidentiality | Zero client identifiers, MNPI, or PII transmitted externally | `PASS / BLOCKED / FAILED` |
| Qualified Legal Counsel Sign-Off Gate | Explicit pre-reliance human counsel approval notice attached | `PASS / BLOCKED / FAILED` |
