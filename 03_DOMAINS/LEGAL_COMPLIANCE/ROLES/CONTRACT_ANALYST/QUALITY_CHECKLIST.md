# Quality Checklist: Contract Analyst (`ROLE-LEG-002`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every check must pass prior to handoff.

## 1. Party Posture, Scope & Document Hierarchy
- [ ] Client role/posture (Buyer/Customer, Vendor/Provider, Licensor/Licensee, Mutual) and commercial context are explicitly locked at the top of the review.
- [ ] Governing law, jurisdiction/venue, CISG/conflict-of-laws exclusions, and arbitration/litigation forum are identified and assessed for enforceability risks.
- [ ] Order-of-precedence across Master Agreement, SOWs, Order Forms, SLAs, DPAs, and incorporated URLs is mapped, and unilateral hyperlink modification ("URL traps") is flagged.

## 2. Liability, Indemnity & Core Risk-Allocation Integrity
- [ ] Limitation of Liability (general cap, super-caps, per-incident vs. aggregate structure, consequential/indirect damages waivers) is traced end-to-end against Indemnification, Confidentiality, Data Security, and IP clauses.
- [ ] Uncapped liability exposures, one-sided indemnities, missing defense/settlement control conditions, or sole-and-exclusive SLA remedy traps are explicitly surfaced and risk-tiered (`CRITICAL` to `LOW`).
- [ ] IP ownership (background IP, foreground deliverables, feedback licenses, derivative works, aggregate/usage data rights, AI training restrictions) is unambiguously separated and verified.
- [ ] Term, auto-renewal notice windows, price-increase caps, termination for breach/convenience, cure periods, transition assistance, and data return/deletion duties are audited.

## 3. Drafting Precision & Cross-Reference Audit
- [ ] Every capitalized Defined Term used in proposed redline text exists in the Definitions section with exact matching capitalization and zero circularity.
- [ ] All internal section cross-references (`Section X.Y`), Survival clauses, and Exhibit/Schedule pointers resolve accurately after proposed insertions or deletions.
- [ ] Each `CRITICAL` and `HIGH` issue includes exact **Tier 1 Preferred** redline language, **Tier 2 Fallback** compromise language, and concise counterparty negotiation rationale.
- [ ] Subjective timeframes or obligations ("promptly", "reasonable efforts") are anchored to concrete calendar/business-day SLAs or objective standards where material.

## 4. Confidentiality & Qualified Legal Counsel Gate
- [ ] Zero confidential deal terms, pricing schedules, party names, or PII were exposed in external queries.
- [ ] Deliverable explicitly states that redlines and risk ratings constitute non-binding contract analysis requiring review and sign-off by qualified legal counsel before counterparty transmission or execution.
- [ ] Output contains zero decorative emojis, zero unfinished placeholders, and 100% valid relative Markdown links.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Posture, Governing Law & Precedence Order | Party role, choice-of-law/venue, and schedule hierarchy verified | `PASS / BLOCKED / FAILED` |
| Liability Cap, Carve-Out & Indemnity Web | Direct/indirect waivers, caps, super-caps, and survival reconciled | `PASS / BLOCKED / FAILED` |
| Defined-Term & Section Cross-References | Capitalized terms and `Section X.Y` pointers verified post-redline | `PASS / BLOCKED / FAILED` |
| Tier 1 Preferred + Tier 2 Fallback Text | Exact replacement wording + business rationale supplied per risk | `PASS / BLOCKED / FAILED` |
| Qualified Legal Counsel Sign-Off Gate | Pre-execution human legal counsel approval gate documented | `PASS / BLOCKED / FAILED` |
