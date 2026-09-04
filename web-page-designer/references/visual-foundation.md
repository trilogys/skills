# Visual Foundation

This is the default blue-and-white visual language for the skill. It is a self-contained specification: bright, operational, data-first, and lightly layered. Apply it across projects and page functions without copying any one interface literally. Preserve an intentional existing brand, but do not invent a different aesthetic for every project.

## Visual Calibration Assets

The optional images in `assets/reference-blue-white-dashboard-01.png` and `assets/reference-blue-white-dashboard-02.png` define the finish target, not a page template. When visual comparison is warranted, inspect:

- cool blue-gray outside the application and white or near-white inside it;
- large outer-shell curvature paired with smaller, related panel and control radii;
- light card borders, broad low-opacity shadows, and generous separation instead of heavy elevation;
- medium-weight interface typography with stronger emphasis reserved for key values;
- blue concentrated in selected navigation, one primary action, and high-value data marks;
- small outline icons with consistent stroke weight and restrained containers.

Ignore the sample brands, metrics, charts, navigation labels, and finance/dashboard structure. Derive those from the user's product.

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

- A cool blue-gray exterior frame may surround the product, while the application interior stays white or near-white. Do not flood the working canvas with visible blue-gray.
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
  --canvas: #f6f8fb;
  --canvas-strong: #d8e4ec;
  --surface: #ffffff;
  --surface-subtle: #fafcfe;
  --surface-tinted: #f4f7ff;

  --text: #2b3445;
  --text-strong: #172033;
  --text-muted: #6b7689;
  --text-faint: #9aa6b7;

  --border: #e8edf3;
  --border-strong: #dbe3ec;

  --accent: #6a90ea;
  --accent-hover: #5c83df;
  --accent-active: #4f76d5;
  --accent-text: #3a64b9;
  --accent-action: #4772d1;
  --accent-soft: #eaf0ff;
  --accent-subtle: #f4f7ff;
  --chart-blue: #75a0f3;
  --chart-blue-soft: #c7d8fa;
  --cyan: #77c5e8;
  --teal: #66b8b1;
  --ink: #2d3440;

  --success: #2f9b6a;
  --warning: #c99237;
  --danger: #c95f6c;
  --info: #5b82e9;
}
```

### Color discipline

- Let white and near-white surfaces occupy roughly 85-95% of a productivity interface. Concentrate the cooler blue-gray on the exterior frame, separators, or selected regions.
- Use the medium blue `--accent` for leading data, selection fills, focus rings, and non-text decoration. Use `--accent-text` for links and blue text so contrast remains accessible.
- Reserve the deeper `--accent-action` for small primary buttons that need white text. Do not fill large page regions with it.
- Use lighter blue tints for navigation selection and card emphasis. Use cyan or teal only for supporting data series or a distinct semantic category; they must not compete with blue for primary-action emphasis.
- Use green, amber, and red semantically. Never use color as the only status signal.
- Avoid page-wide gradients. A subtle two-color gradient may appear on one emphasized KPI or balance block, but a solid fill is usually better.
- Keep charts legible in grayscale: combine color with labels, shape, position, or line style.
- Meet WCAG AA contrast for essential text and controls. Do not put low-contrast gray text on tinted surfaces.

## Geometry And Radius

Use a radius hierarchy instead of applying the same large radius everywhere.

| Element | Default radius | Notes |
|---|---:|---|
| App frame shown inside a marketing mockup | 28-32 px | Presentation only; a full-viewport product shell normally has no outer radius |
| Dialog or large bounded tool | 12-14 px | Use only when it is genuinely framed |
| Standard card or chart panel | 10-12 px | Reference-style internal panel radius |
| Input, button, select trigger | 8-10 px | Keep controls softer than generic browser defaults |
| Tooltip, menu, and popover | 10-12 px | Match the trigger family while preserving anchored geometry |
| Status chip, segmented selection, avatar | 999 px | Only for semantically pill-shaped elements |

- Dense enterprise and operational tools should normally keep internal cards at 8-10 px. General product panels can use 10-12 px; consumer or media products may reach 12-14 px when that softness supports their character. Do not change radius merely to make a page feel redesigned.
- Do not nest visually rounded cards inside rounded cards. Use dividers, headings, or a grid inside a parent surface.
- Do not use pills for ordinary navigation, labels, or every button.
- Align neighboring radii and insets. Inner controls should usually be equal to or slightly less rounded than their container and must not visually collide with the parent's curvature.

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
- Keep the theme recognizable across different topologies, but derive topology from work. An editor may need canvas plus inspector, a mailbox may need three panes, and a scheduler may need a time grid; none should inherit a dashboard layout merely to preserve visual consistency.

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
  border-radius: 12px;
  box-shadow: 0 1px 2px rgb(15 23 42 / 0.025), 0 10px 28px rgb(38 58 84 / 0.018);
}
```

- Prefer a faint border with either no shadow or a broad, very low-opacity shadow. Strong card outlines make the page feel assembled rather than integrated.
- Use stronger elevation only for temporary overlays such as menus, popovers, and dialogs.
- Avoid glow, bokeh, decorative gradient blobs, heavy blur, or uniformly tinted pages.
- Backdrop blur may support transient chrome but must not reduce text contrast or become the dominant style.

## Typography

- Read `typography-system.md` and choose a semantic type scale for the current product. The values below are calibration ranges for this visual style, not fixed requirements.
- Prefer the project's font. Otherwise use Inter, Geist, or a system sans stack.
- Keep letter spacing at `0` for ordinary interface text.
- Page title: 24-30 px, usually 600-650 weight.
- Section title: 16-20 px, 550-650 weight.
- Card title: 13-15 px, 550-650 weight.
- Body and table text: 13-15 px, 400-500 weight.
- Metadata: 11-13 px, muted but still readable.
- KPI: 28-38 px, 550-650 weight, `font-variant-numeric: tabular-nums`.
- Avoid using 700+ throughout the interface. Reserve the strongest weight for the brand, a single critical value, or rare emphasis; reference-quality layouts feel confident because hierarchy is controlled, not because every heading is bold.
- Use sentence case. Avoid excessive uppercase; reserve it for very small category labels when the product already uses that convention.
- Never scale type with viewport width. Use stable responsive steps and ensure long labels wrap or truncate intentionally.

## Components

### Navigation

- Group sidebar items by user task, not internal organization.
- Use one unmistakable active state: a soft blue background with `--accent-text`, or a compact high-contrast blue selection when necessary.
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

### Selects, menus, and floating controls

- Inspect controls both closed and open. A rounded select trigger with a square operating-system popup is not a visually complete result.
- Use the project's accessible popover or select primitive when available. In plain HTML, keep the native `<select>` when platform consistency is acceptable; when the visual brief requires a coordinated popup, implement a real accessible listbox/combobox with a button trigger, `aria-expanded`, keyboard navigation, Escape handling, outside-click dismissal, focus return, and selected-state semantics.
- Match trigger, popup, and option radii as a family: roughly 8-10 px trigger, 10-12 px popup, and 7-8 px option for this reference style.
- Give floating menus a white surface, one faint border, and a broad low-opacity shadow. Avoid sharp corners, heavy black shadows, or a menu that is visually darker than its trigger.
- Make dropdown arrows point down when closed and up when open. Keep them in the same stroke family and optical weight as the rest of the interface.

## Iconography

Icons are part of the theme, not decoration added after layout.

- Reuse the project's established icon family. If none exists, use one coherent library such as Lucide and keep its default stroke character unless the product has a reason to tune it globally.
- Never mix outline, filled, duotone, emoji, and hand-drawn icons in the same functional layer.
- Use icons only when they improve recognition, scanning, or space efficiency. A small icon beside every label adds noise rather than quality.
- Prefer 16-18 px icons in 32-36 px desktop controls, 14-16 px in dense table actions, and 20-24 px only for visually important standalone actions or empty states.
- Keep icon-and-label gaps around 8 px. Center icons optically, not only mathematically; chevrons, play symbols, and asymmetric marks often need a 1 px correction.
- Let icons inherit text color. Use `--accent-text` for active blue icons and semantic colors only when the icon communicates that status.
- Use a 28-32 px icon container with a 6-8 px radius only when grouping or hit area requires it. Do not put every icon in a colored circle or rounded square.
- Keep stroke weight, cap style, corner character, and visual size consistent across navigation, toolbars, tables, and dialogs.
- Use familiar symbols for icon-only actions and provide an accessible name plus a tooltip for anything that may be ambiguous.
- Verify icons at 100% browser zoom against adjacent type. Reject icons that appear heavier, sharper, more saturated, or more playful than the surrounding interface.

## Motion Character

The visual language should feel responsive rather than animated:

- button press: 100-160 ms, subtle `scale(0.97-0.99)` when appropriate;
- tooltip or small popover: 125-200 ms;
- select or dropdown: 150-220 ms;
- dialog or drawer: 180-280 ms;
- color and border feedback: 120-180 ms;
- no motion for repeated keyboard navigation or rapid data inspection.

Use strong but controlled easing such as `cubic-bezier(0.23, 1, 0.32, 1)` for entrances. Motion must never delay access to information.
