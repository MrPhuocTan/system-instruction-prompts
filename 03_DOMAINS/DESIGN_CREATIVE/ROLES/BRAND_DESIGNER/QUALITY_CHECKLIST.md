# Quality Checklist: Brand Designer (`ROLE-DES-005`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Identity Architecture & Mark Resilience
- [ ] Brand architecture (master brand, sub-brands, product lockups, partner co-branding hierarchy) is explicitly defined and aligned with project scope.
- [ ] Mark system includes full-color primary, horizontal/stacked lockups, symbol-only icon, pure 1-bit dark-on-light, pure 1-bit light-on-dark knockout, and `16x16px` / `32x32px` favicon variants.
- [ ] Clear-space exclusion zone (in proportional unit `X`) and minimum digital (`px`) / physical (`mm`) legibility thresholds are specified quantitatively.
- [ ] SVG mark files are valid, self-contained vector XML with clean `viewBox` coordinates, zero raster embeds, and zero dependency on locally installed system fonts to render geometry.

## 2. Accessible Brand-to-Product Color & Typography Bridge
- [ ] Brand color specifications provide exact HEX, RGB, and OKLCH values and explicitly distinguish expressive marketing accents from WCAG 2.2 AA compliant UI text/interactive shade pairings (`>= 4.5:1` / `>= 3.0:1`).
- [ ] Approved vs. prohibited logo-on-background combinations are contrast-verified mathematically.
- [ ] Brand typography pairs display/editorial, UI sans, and monospace stacks cleanly, including verified open-license (`OFL-1.1`) options or explicit commercial font licensing disclosures.

## 3. Cross-Medium Governance & Zero "AI Sign" Originality
- [ ] Explicit "Do / Do Not" misuse rules forbid aspect-ratio stretching, unapproved drop shadows/outlines, low-contrast busy photo overlays, and unauthorized recoloring.
- [ ] Identity avoids generic "AI Sign" cliches (sparkle stars, neon purple-cyan blobs, stock hex-brain tropes, decorative emojis, or empty marketing buzzwords).

## 4. Trademark & Licensing Safeguards
- [ ] Zero third-party trademarks, certification badges, or protected trade dress are imitated or embedded without authorization.
- [ ] Deliverable includes an explicit checkpoint routing candidate names, taglines, and marks to [`INTELLECTUAL_PROPERTY_SPECIALIST`](../../../LEGAL_COMPLIANCE/ROLES/INTELLECTUAL_PROPERTY_SPECIALIST/SYSTEM_PROMPT.md) and qualified trademark counsel before public launch.
- [ ] All relative Markdown links resolve to existing canonical library files.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Monochrome & `16px` Small-Scale Geometry | Full-color, 1-bit light/dark knockouts, and `16x16px` favicon SVG | `PASS / BLOCKED / FAILED` |
| Clear-Space `X` & Minimum-Size Rules | Quantitative exclusion zone, minimum `px`/`mm`, and misuse rules | `PASS / BLOCKED / FAILED` |
| Brand-to-UI Accessible Palette Bridge | Marketing accents separated/paired with `>= 4.5:1` UI shade tokens | `PASS / BLOCKED / FAILED` |
| Zero "AI Sign" & Distinctiveness | Domain-authentic geometry free of generic sparkle/neon tropes | `PASS / BLOCKED / FAILED` |
| Font Licensing & Trademark Counsel Gate | Open/licensed font audit + human trademark counsel review gate | `PASS / BLOCKED / FAILED` |
