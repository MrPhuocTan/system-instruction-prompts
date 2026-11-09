# Quality Checklist: Content Strategist (`ROLE-DES-007`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Terminology Consistency & Action Clarity
- [ ] Every core domain object and status state uses a single locked canonical term across navigation, headings, tables, notifications, and documentation (`0` synonym drift).
- [ ] Interactive buttons, menu items, and dialog CTAs use explicit verb-object phrasing (`"Revoke token"` / `"Keep token"`) with zero ambiguous `"OK"` / `"Yes"` / `"No"` pairings or double-negative prompts.
- [ ] Capitalization (Sentence case baseline unless documented otherwise), punctuation (no periods on single-phrase labels/buttons; periods on multi-sentence helper/body text), and numeric/date formatting rules are consistent throughout.

## 2. Error, Empty, Loading & Destructive-Action Copy Completeness
- [ ] Every validation and system error message communicates: (a) what failed in plain language, (b) whether user input/state is preserved, and (c) the exact recovery action—without exposing sensitive backend stack traces or account-enumeration hints.
- [ ] Empty states distinguish first-run onboarding from zero-match filter/search results and provide clear orientation plus an appropriate next step.
- [ ] Destructive-action dialogs explicitly state the target resource name/count, permanent consequences, and whether undo is available.

## 3. Accessibility (`WCAG 2.2`) & Localization (`i18n`) Readiness
- [ ] Standalone links and icon-only buttons carry self-describing labels (`0` bare `"Click here"` or `"Read more"` links lacking accessible context).
- [ ] Dynamic asynchronous state changes specify crisp `aria-live="polite"` (or `"assertive"` for critical errors) screen-reader announcements and non-redundant `alt` text (`alt=""` for purely decorative images).
- [ ] Translatable strings use full-sentence ICU MessageFormat syntax (supporting plural categories and named placeholders) with zero hard-coded fragment concatenation and `+30%–40%` character-expansion headroom verified.

## 4. Zero "AI Sign" Verbal Hygiene & Regulated Copy Gate
- [ ] Copy is completely free of confirmshaming dark patterns, synthetic filler strings, decorative emojis, exclamation-mark spam, and "AI Sign" marketing buzzwords (`"Supercharge"`, `"Unleash"`, `"Seamless"`, `"Delve"`).
- [ ] Privacy consent disclosures, billing terms, and regulated risk disclaimers are flagged for review by [`PRIVACY_SPECIALIST`](../../../LEGAL_COMPLIANCE/ROLES/PRIVACY_SPECIALIST/SYSTEM_PROMPT.md) / qualified human legal counsel before publication.
- [ ] All relative Markdown links resolve cleanly.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Controlled Domain Glossary & CTA Verbs | `0` synonym drift + explicit verb-noun dialog/button actions | `PASS / BLOCKED / FAILED` |
| Error, Empty & Destructive Copy Triad | Plain cause + state preservation + exact recovery step specified | `PASS / BLOCKED / FAILED` |
| Accessible Labels & `aria-live` Specs | Self-describing links/buttons (`0` bare `"Click here"`) + live text | `PASS / BLOCKED / FAILED` |
| ICU MessageFormat & `+40%` Expansion | Plural-safe full templates (`0` concatenated fragments) + expansion | `PASS / BLOCKED / FAILED` |
| Zero "AI Sign" & Anti-Dark-Pattern Check | Zero buzzwords, emojis, confirmshaming, or security-leaking errors | `PASS / BLOCKED / FAILED` |
