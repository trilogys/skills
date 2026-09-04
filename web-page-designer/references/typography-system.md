# Adaptive Typography System

Typography must be selected for the product in front of you. Do not copy font sizes from a screenshot, calibration demo, previous project, or fixed page-type template.

## Decide The Reading Context

Before choosing values, determine:

- **Audience and expertise:** expert operators tolerate higher density than occasional or first-time users.
- **Primary activity:** scanning a queue, reading documents, editing code, comparing data, presenting status, or completing a guided flow.
- **Language and script:** CJK glyphs carry more visual density than Latin at the same nominal size; mixed Chinese, English, numbers, and code need optical balancing.
- **Viewing distance:** a laptop workbench, wall display, mobile device, or presentation screen requires different sizing.
- **Font metrics:** x-height, CJK box size, width, available weights, and rendering quality change the apparent scale.
- **Content pressure:** long labels, localization, user-generated content, tables, and large values may require more space or different wrapping.
- **Accessibility:** browser zoom, text enlargement, contrast, cognitive load, and reduced visual acuity.

## Choose A Density Baseline

Use these as starting bands, not rules:

| Product context | Typical body starting point | Character |
|---|---:|---|
| Dense expert console | 13-14 px | Compact controls, short labels, frequent scanning; never let essential text become faint or cramped |
| Standard SaaS product | 14-16 px | Balanced scanning and reading with moderate information density |
| Reading or content workspace | 16-18 px | Longer line-height, controlled measure, fewer simultaneous columns |
| Consumer or guided flow | 15-17 px | Clear actions and relaxed grouping; tune for device and audience |
| Presentation or distant display | 18 px and above | Fewer elements, stronger hierarchy, and larger targets |

For Chinese-heavy interfaces, begin optical comparison at the upper half of the relevant band. Chinese at 13 px may feel denser and less legible than Latin at the same value even when both technically fit.

## Build Semantic Roles

Define tokens by role, then assign project-specific values:

```css
:root {
  --type-body: 1rem;
  --type-control: 0.925rem;
  --type-meta: 0.825rem;
  --type-card-title: 1rem;
  --type-section-title: 1.25rem;
  --type-page-title: 1.75rem;
  --type-data: 2rem;
}
```

These ratios are only a coherent starting relationship. Adjust the whole system after rendering real content rather than tuning isolated elements one by one.

Role decisions:

- **Body:** establishes the reading baseline and default line-height.
- **Control:** may be slightly smaller in dense desktop tools, but must remain legible and vertically centered.
- **Metadata:** lower hierarchy through size and color together, without becoming inaccessible.
- **Card title:** compact and close to body size; a card is not a hero.
- **Section title:** separates work regions without overpowering the page title.
- **Page title:** identifies context; its scale depends on density and frequency, not viewport width.
- **Data/KPI:** uses tabular numbers and optical sizing based on digit length, unit, and container.

## Weight And Line Height

- Use weight to create hierarchy only after size and spacing are coherent.
- Prefer 400-500 for body, 500-600 for controls and compact labels, and 550-650 for most headings.
- Reserve 700+ for a brand mark, a rare high-emphasis value, or a typeface whose metrics require it.
- Body line-height normally needs 1.45-1.65 in Latin UI copy and 1.55-1.8 for Chinese paragraphs. Dense single-line controls use their stable control height instead.
- Do not use negative tracking. Keep letter spacing at `0` for ordinary UI; evaluate font-specific tracking only when the brand system explicitly requires it.
- Enable tabular figures for values that must align or change in place.

## Fit And Hierarchy Tests

Render real content and verify:

1. Squint at the page: page context, primary action, main evidence, and supporting metadata should separate without relying on borders.
2. Compare the longest label, largest number, mixed-language row, and two-line error state.
3. Check 100%, 125%, and 200% browser zoom.
4. Confirm buttons, tabs, cards, sidebars, chart labels, and tables do not resize unpredictably.
5. Ensure body text remains comfortable over several paragraphs, not only in a short mockup.
6. Verify numbers use consistent width and do not dominate simply because they contain more digits.

## Responsive Type

- Do not scale font size continuously with viewport width.
- Use explicit semantic steps only when reading context changes, such as desktop workspace to mobile sequence or dashboard to wall display.
- Preserve role order across breakpoints. A card title must not become visually stronger than the page title after reflow.
- Reduce simultaneous columns and secondary content before shrinking essential text.

## Reject

- one fixed size table applied to every project;
- viewport-width formulas such as `clamp()` used only to make type grow with the screen;
- 700+ weight on every title and number;
- tiny gray text carrying essential information;
- desktop type shrunk to preserve too many columns;
- Latin-calibrated sizes copied into Chinese-heavy UI without optical comparison;
- card or panel headings styled at hero scale;
- truncation used to hide a type-scale or container problem.
