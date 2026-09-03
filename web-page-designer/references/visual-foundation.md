# Visual Foundation

This is the default blue-and-white visual language for the skill. It is a self-contained specification: bright, operational, data-first, and lightly layered. Apply it across projects and page functions without copying any one interface literally. Preserve an intentional existing brand, but do not invent a different aesthetic for every project.

## Stable Style And Controlled Variation

Keep these characteristics stable unless the user explicitly requests another direction:

- soft blue-gray canvas, clear white surfaces, near-black text, and blue as the primary accent;
- a 4 px spacing foundation, consistent alignment, and a deliberate radius hierarchy;
- compact desktop controls, data-first hierarchy, light borders, and minimal elevation;
- cards only for bounded or comparable content, not as the default wrapper for every section;
- short, purposeful motion with immediate interaction feedback.

Vary these when the page's function or existing brand justifies it:

- the exact blue accent and supporting chart-series palette;
- density level, column count, navigation model, and content width;
- whether a section is carded, divided, tabbed, split, or unframed;
- chart, table, form, editor, canvas, timeline, or media composition;
- control size within the documented desktop ranges.

Do not interpret variation as permission to randomly change the palette, inflate radii, add decorative gradients, or turn an unfamiliar workflow into a generic dashboard.

## Visual DNA

- Soft blue-gray canvas behind high-clarity white surfaces.
- Near-black text, restrained gray metadata, and one dominant functional accent.
- Blue used for primary actions, selection, focus, and the leading data series. Cyan, teal, and other hues remain secondary or semantic.
- A stable sidebar or compact top navigation for product areas; a top toolbar for search, date range, filters, account, and page actions.
- Thin borders and extremely soft shadows. Separation should come mostly from spacing, value contrast, and alignment.
- Rounded outer presentation frames, but more restrained internal cards and controls.
- Data is the visual protagonist: numbers, charts, tables, and statuses receive more weight than decorative copy.

## Default Color Tokens

Use semantic names. These values are the house defaults, not mandatory replacements for an intentional product brand.

```css
:root {
  --canvas: #f3f6fa;
  --canvas-strong: #e8eef6;
  --surface: #ffffff;
  --surface-subtle: #f8fafc;
  --surface-tinted: #eff6ff;

  --text: #1e293b;
  --text-strong: #0f172a;
  --text-muted: #64748b;
  --text-faint: #94a3b8;

  --border: #e2e8f0;
  --border-strong: #cbd5e1;

  --accent: #2563eb;
  --accent-hover: #1d4ed8;
  --accent-active: #1e40af;
  --accent-soft: #dbeafe;
  --accent-subtle: #eff6ff;
  --cyan: #0ea5e9;
  --teal: #0f9f8e;
  --ink: #273142;

  --success: #16a34a;
  --warning: #d97706;
  --danger: #dc2626;
  --info: #2563eb;
}
```

### Color discipline

- Let white and blue-gray neutral surfaces occupy roughly 80-90% of a productivity interface.
- Use blue as the default primary accent for actions, active navigation, focus, selection, links, and the leading data series.
- Use cyan or teal only for supporting data series or a distinct semantic category. They must not compete with blue for primary-action emphasis.
- Use green, amber, and red semantically. Never use color as the only status signal.
- Avoid page-wide gradients. A subtle two-color gradient may appear on one emphasized KPI or balance block, but a solid fill is usually better.
- Keep charts legible in grayscale: combine color with labels, shape, position, or line style.
- Meet WCAG AA contrast for essential text and controls. Do not put low-contrast gray text on tinted surfaces.

## Geometry And Radius

Use a radius hierarchy instead of applying the same large radius everywhere.

| Element | Default radius | Notes |
|---|---:|---|
| App frame shown inside a marketing mockup | 24-28 px | Presentation only; a full-viewport product shell normally has no outer radius |
| Dialog or large bounded tool | 12 px | Use only when it is genuinely framed |
| Standard card or chart panel | 8 px | Primary internal card radius |
| Input, button, select, compact popover | 6-8 px | Keep dense controls precise |
| Tooltip and small menu | 6 px | Compact and anchored |
| Status chip, segmented selection, avatar | 999 px | Only for semantically pill-shaped elements |

- Do not nest visually rounded cards inside rounded cards. Use dividers, headings, or a grid inside a parent surface.
- Do not use pills for ordinary navigation, labels, or every button.
- Align neighboring radii and insets. An inner element should not visually collide with the parent's curvature.

## Spacing And Density

Use a 4 px base with this practical scale:

```text
4  8  12  16  20  24  32  40  48  64
```

- Desktop page padding: 24-32 px.
- Major section gap: 24-32 px.
- Card padding: 16-20 px; use 24 px only for a primary analytical panel.
- Control height: 32-36 px for dense tools, 40 px for standard forms, 44 px only when touch use is important.
- Table row height: 44-52 px depending on content.
- Keep related label/value pairs within 4-8 px; separate unrelated groups by at least 16-24 px.

Density levels:

- **Focused:** forms, onboarding, checkout; fewer columns and more breathing room.
- **Standard:** most dashboards and management pages; compact controls with readable grouping.
- **Dense:** monitoring, finance, inventory, and data grids; smaller gaps, stronger alignment, and optional user density controls.

## Desktop Layout

Baseline for a 1440 px viewport:

- Sidebar: 232-256 px, fixed or sticky; collapsed rail: 64-72 px.
- Top bar: 60-68 px.
- Main content: fluid, preferably capped around 1600 px on very wide screens.
- Page gutters: 24-32 px.
- Grid: 12 columns, 20-24 px gaps.
- Primary analysis area: 8 columns plus a 4-column support panel, or full width when the task requires comparison.
- KPI row: usually 3-4 equal columns; do not shrink metrics until labels wrap incoherently.

Responsive behavior:

- At narrower desktop widths, collapse secondary rails before compressing data beyond legibility.
- Convert 4 KPI columns to 2, then 1; preserve reading order and comparison groups.
- Let tables scroll within their own region only when column removal or alternate list rendering would lose important information.
- On mobile, convert sidebars to drawers and move primary actions into reachable, non-overlapping positions. Do not merely scale the desktop canvas down.

## Surfaces, Borders, And Shadow

Default surface treatment:

```css
.panel {
  background: var(--surface);
  border: 1px solid var(--border);
  border-radius: 8px;
  box-shadow: 0 1px 2px rgb(15 23 42 / 0.04);
}
```

- Prefer a border with either no shadow or one subtle shadow.
- Use stronger elevation only for temporary overlays such as menus, popovers, and dialogs.
- Avoid glow, bokeh, decorative gradient blobs, heavy blur, or uniformly tinted pages.
- Backdrop blur may support transient chrome but must not reduce text contrast or become the dominant style.

## Typography

- Prefer the project's font. Otherwise use Inter, Geist, or a system sans stack.
- Keep letter spacing at `0` for ordinary interface text.
- Page title: 24-30 px, 600-700 weight.
- Section title: 16-20 px, 600 weight.
- Card title: 13-15 px, 600 weight.
- Body and table text: 13-15 px, 400-500 weight.
- Metadata: 11-13 px, muted but still readable.
- KPI: 28-38 px, 600-700 weight, `font-variant-numeric: tabular-nums`.
- Use sentence case. Avoid excessive uppercase; reserve it for very small category labels when the product already uses that convention.
- Never scale type with viewport width. Use stable responsive steps and ensure long labels wrap or truncate intentionally.

## Components

### Navigation

- Group sidebar items by user task, not internal organization.
- Use one unmistakable active state: a soft blue background or a high-contrast blue/ink selection, plus icon/text contrast.
- Keep utility destinations such as help and settings near the bottom when appropriate.
- Do not show multiple competing active indicators.

### Page header and toolbar

- Put title and concise context on the left; filters and actions on the right.
- One primary action per view. Secondary actions should be quiet or placed in a menu.
- Keep global search in the app bar; keep local search next to the data it filters.

### Metric cards

- Present label, value, comparison period, and trend in that order.
- Make the number dominant; keep sparklines supportive.
- State what the percentage compares against. An unlabeled green percentage is incomplete.
- Use one highlighted metric at most unless all metrics have equal status.

### Charts

- Select a chart by analytical question, not visual novelty.
- Start axes honestly, label units, show time ranges, and provide accessible summaries or tabular alternatives.
- Keep series count low and colors stable across the page.
- Use direct labels where practical; otherwise keep legends close to the plot.
- Tooltips must include series, exact value, unit, and time/category.
- Do not use a donut when exact comparisons matter, a gauge without a meaningful target, or a smoothed line that implies nonexistent precision.

### Tables

- Align text left and numeric values right; use tabular numbers.
- Keep row actions at the end and reveal secondary actions without shifting columns.
- Provide sorting, filtering, pagination or virtualization when the data warrants it.
- Make selection and bulk actions obvious and reversible.
- Use status chips sparingly and consistently.

### Forms

- Place labels above fields for general product forms; group fields by task.
- Keep help text and validation adjacent to the field.
- Use a single clear submit action and preserve user input after validation failures.
- Do not place each field inside its own card.

## Motion Character

The visual language should feel responsive rather than animated:

- button press: 100-160 ms, subtle `scale(0.97-0.99)` when appropriate;
- tooltip or small popover: 125-200 ms;
- select or dropdown: 150-220 ms;
- dialog or drawer: 180-280 ms;
- color and border feedback: 120-180 ms;
- no motion for repeated keyboard navigation or rapid data inspection.

Use strong but controlled easing such as `cubic-bezier(0.23, 1, 0.32, 1)` for entrances. Motion must never delay access to information.
