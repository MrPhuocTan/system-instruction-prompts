# Quality Checklist: Visual Designer (`ROLE-DES-004`)

Pre-handoff verification checklist aligned with [`SYSTEM_PROMPT.md`](./SYSTEM_PROMPT.md) and [`QUALITY_GATES.md`](../../QUALITY_GATES.md). Every item must pass prior to handoff.

## 1. Perceptual Color & Accessibility Verification
- [ ] Color scales (`50`–`950`) are calibrated using perceptual lightness (OKLCH / relative luminance) with exact sRGB hex equivalents provided—never naive HSL lightness steps.
- [ ] Deterministic contrast math confirms `>= 4.5:1` for all normal text pairings and `>= 3.0:1` for large text, UI borders, and graphical indicators across both light and dark surface tiers.
- [ ] Semantic status palettes (`success`, `warning`, `danger`, `info`) remain distinguishable under deuteranopia, protanopia, and tritanopia and are always paired with non-color cues (icons/text).
- [ ] Dark-mode surfaces use stepped luminance elevation (`L` hierarchy + subtle hairline borders) rather than pure-black/pure-white halation or illegible dark drop shadows.

## 2. Typography, Rhythm & Optical Craft
- [ ] Font stack specifies primary typeface, metric-compatible system fallbacks, modular type scale, line heights (`1.15–1.25` headings, `1.45–1.60` prose), and `45–75ch` measure bounds.
- [ ] Numeric tables, KPI counters, timestamps, and currency figures explicitly enable `font-variant-numeric: tabular-nums`.
- [ ] Visual hierarchy establishes unmistakable 1st-, 2nd-, and 3rd-order reading scan paths using spatial grouping (`4px`/`8px` rhythm) and weight before adding extra borders or chrome.

## 3. SVG Vector Hygiene & Asset Licensing
- [ ] Custom SVGs are valid XML, snap cleanly to a standardized `viewBox` (`16`/`20`/`24`), maintain uniform stroke width/caps/joins, inherit `currentColor` where appropriate, and contain zero stray raster blobs.
- [ ] Decorative SVGs carry `aria-hidden="true" focusable="false"`, while standalone informative graphics provide accessible `<title>` / `aria-label` semantics.
- [ ] All recommended web fonts and icon sets carry verified permissive/commercial licenses (`OFL-1.1`, `MIT`, `Apache-2.0`) free of unlicensed proprietary assets.

## 4. Zero "AI Sign" Restraint & Handoff Completeness
- [ ] Zero gratuitous purple-blue neon gradients, floating glassmorphic orbs, sparkle badges, synthetic filler strings, or decorative emojis appear anywhere in the visual system.
- [ ] Visual specifications map directly into semantic tokens consumable by [`UI_DESIGNER`](../UI_DESIGNER/SYSTEM_PROMPT.md) and [`FRONTEND_ENGINEER`](../../../IT_SOFTWARE/ROLES/FRONTEND_ENGINEER/SYSTEM_PROMPT.md), with honest disclosure if live browser rendering was unavailable.
- [ ] All relative Markdown links resolve cleanly.

## 5. Pre-Handoff Independent Verification Summary

| Verification Dimension | Evidence Inspected | Status |
| :--- | :--- | :--- |
| Perceptual OKLCH Ramp & Contrast Math | Light/dark luminance steps verified (`>= 4.5:1` / `>= 3.0:1`) | `PASS / BLOCKED / FAILED` |
| Color-Vision Deficiency (CVD) Parity | Status ramps distinguishable + paired with non-color cues | `PASS / BLOCKED / FAILED` |
| Typographic Scale & `tabular-nums` | Modular hierarchy, `45–75ch` measure, tabular numeric alignment | `PASS / BLOCKED / FAILED` |
| SVG XML Cleanliness & Font Licensing | Grid-snapped `viewBox`, uniform strokes, `OFL-1.1`/`MIT` license | `PASS / BLOCKED / FAILED` |
| Zero "AI Sign" Visual Discipline | Zero neon gradients, glassmorphic orbs, or decorative clutter | `PASS / BLOCKED / FAILED` |
