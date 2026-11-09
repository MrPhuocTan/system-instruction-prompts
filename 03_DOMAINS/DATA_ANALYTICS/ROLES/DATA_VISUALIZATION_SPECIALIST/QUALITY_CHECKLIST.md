# Quality Checklist: Data Visualization Specialist (`ROLE-DATA-007`)

- **Role:** [`DATA_VISUALIZATION_SPECIALIST`](./SYSTEM_PROMPT.md)
- **Domain Gates:** [`QUALITY_GATES.md`](../../QUALITY_GATES.md)

---

## 1. Perceptual Accuracy & Scale Honesty
- [ ] Enforced `0`-baseline on all bar, column, lollipop, and stacked-area length encodings (`Lie Factor` in `[0.95, 1.05]`).
- [ ] Eliminated 3D extrusions, arbitrary dual-Y axis scale manipulation, and multi-slice (`> 4` category) pie/donut charts.
- [ ] Verified continuous temporal and numeric axes preserve proportional spacing (`0` silently compressed date gaps) and visually distinguished incomplete trailing periods (`WTD`/`MTD` dashed or shaded).
- [ ] Annotated exact units, currency symbols, timezone/`as-of` freshness timestamps, sample sizes (`n`), and confidence/uncertainty intervals where applicable.

## 2. Accessibility, Color Science & Utilitarian Typography
- [ ] Verified `WCAG 2.2 AA` contrast (`>= 4.5:1` text, `>= 3:1` graphical marks) and deuteranopia/protanopia safety (never relying on red/green hue alone without `+`/`-` signs, patterns, or blue/orange diverging scales).
- [ ] Applied `tabular-nums` alignment to numeric tables/KPIs, horizontal readable category labels (`0` cramped `45°`–`90°` rotated labels), and capped simultaneous series (`<= 6`–`7` or faceted into small multiples).
- [ ] Stripped all decorative emojis, neon `"AI Sign"` gradients, faux-glassmorphism clutter, and redundant gridlines.

## 3. Interactivity, Rendering Performance & Edge States
- [ ] Verified empty-filter, zero-row, loading, error, and long-string truncation states across desktop and mobile viewports (visually inspected via `view_file` or explicitly flagged `NOT VERIFIED` if live browser tools were absent).
- [ ] Applied pre-binning (`hexbin`) or `LTTB` `Canvas`/`WebGL` rendering for dense (`> 10,000` point) series to maintain `< 100ms` interaction latency.

## 4. Tooltip Security & Data Privacy
- [ ] Escaped all user-controlled strings in tooltips, legends, and DOM attributes (`0` `innerHTML` / `XSS` injection sinks).
- [ ] Confirmed zero individual `PII` or restricted small-cell records leak in hover payloads, embedded JSON state, or CSV downloads.

## 5. 3-Level QA Verification & Handoff Completeness
- [ ] Reconciled plotted series coordinates (`min`, `max`, `sum`, endpoint values) programmatically against [`BI_ANALYST`](../BI_ANALYST/SYSTEM_PROMPT.md) / [`ANALYTICS_ENGINEER`](../ANALYTICS_ENGINEER/SYSTEM_PROMPT.md) control tables.
- [ ] Visually inspected rendered chart artifacts (`view_file` on PNG/screenshots when available) to confirm zero clipped axes, overlapping labels, or `"AI Sign"` clutter.
- [ ] Explicitly disclosed whether interactive live-browser GUI testing was executed or marked `NOT VERIFIED` due to runtime tool availability.
