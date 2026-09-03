# Quality Gates

Use the applicable gates before declaring a page complete. When reviewing, report concrete failures first, ordered by user impact, with file or component references when available.

## Product And Information

- The page has one clear job and a visible primary action.
- The first screen prioritizes real work or real product evidence.
- Titles, labels, units, time ranges, and comparison baselines are unambiguous.
- Summary values lead to supporting records or evidence.
- Content is realistic and specific to the domain.
- Empty and error states tell the user what happened and what action is available.

## Hierarchy And Layout

- The page can be understood through alignment, spacing, and type before card borders are considered.
- No page section is styled as a floating card without a functional reason.
- No card is nested inside another decorative card.
- Repeated elements use stable grid tracks and dimensions.
- Dense content remains scan-friendly; focused content is not unnecessarily stretched wide.
- Long labels, translated copy, large numbers, validation messages, and dynamic counts do not overlap or resize controls unexpectedly.
- The page has no accidental horizontal scrolling at supported widths.

## Visual System

- Colors use semantic tokens and pass essential contrast requirements.
- When the house theme applies, light and medium blues carry selection and data emphasis; deep blue is limited to compact controls that require white-text contrast.
- The page is mostly neutral; accents communicate action, selection, data, or status.
- Border, radius, shadow, and spacing values come from a small consistent scale.
- Standard cards are restrained; pills are reserved for statuses and truly pill-shaped controls.
- Icons come from one coherent family and align optically with text.
- Icon size, stroke, color, container, and corner character belong to the selected theme; no icon looks pasted in from another system.
- A changed theme has no leftover raw colors, chart series, focus rings, shadows, overlay tints, or icon treatments from its predecessor.
- Typography matches the density and container; compact panels do not contain hero-scale headings.
- No decorative orb, bokeh, heavy blur, or dominant single-hue gradient weakens clarity.

## Components And States

- Buttons have default, hover where supported, focus, active, disabled, and loading behavior.
- Inputs have label, help or constraint where needed, focus, filled, invalid, disabled, and read-only behavior.
- Tables handle loading, no rows, error, sorting, filtering, selection, overflow, and long cells as applicable.
- Charts handle loading, no data, one point, zero, negative, missing, and large values as applicable.
- Popovers and menus anchor to their trigger, fit within the viewport, and close predictably.
- Dialogs trap and restore focus and expose a clear close path.
- Toasts supplement inline state; they do not carry information the user cannot recover.

## Interaction And Motion

- Every visible control works or is clearly disabled.
- Common actions are reachable without unnecessary menus.
- Keyboard-triggered and high-frequency actions respond immediately.
- Ordinary motion is purposeful, interruptible where needed, and under 300 ms.
- Animated properties avoid layout work where possible.
- `prefers-reduced-motion` produces a complete, understandable experience.
- Live data does not move the user's controls or reading position unexpectedly.

## Accessibility

- Landmarks, headings, labels, names, roles, and values are correct.
- Focus order follows the visual and task order.
- Focus indicators are visible against every surface.
- The entire primary workflow works with a keyboard.
- Status is not communicated by color alone.
- Text and controls remain usable at browser zoom and with longer localized strings.
- Errors are associated with their fields and summarized when a long form needs it.

## Responsive And Visual Verification

When browser tooling is available, capture and inspect screenshots rather than relying only on DOM assertions.

Recommended desktop checks:

| Viewport | What it reveals |
|---|---|
| 1280 x 800 | Tight desktop layout, toolbar wrapping, sidebar pressure |
| 1440 x 900 | Primary design baseline |
| 1920 x 1080 | Excessively stretched content and weak max-width decisions |

Also test the narrowest supported width and at least one long-content state. For charts or canvas, verify nonblank rendered pixels and correct framing.

Check:

- no overlap, clipping, orphaned labels, or incoherent wrapping;
- stable headers, sidebars, tables, toolbars, tiles, and chart dimensions;
- popovers, menus, dialogs, and tooltips remain inside the viewport;
- real assets, fonts, icons, and data visuals render;
- hover, focus, active, selected, loading, empty, and error states are visually distinct;
- browser console contains no new errors or repeated warnings.
- at least one refinement pass occurred after the first complete render, and the final screenshot was inspected rather than assumed correct.

## Reject Before Delivery

Do not deliver while any of these remain:

- a generic dashboard substituted for the requested workflow;
- multiple equally loud primary actions;
- placeholder copy, dead buttons, fabricated precision, or decorative charts;
- giant rounded cards for ordinary page sections;
- cards inside cards, excessive badges, or every control rendered as a pill;
- low-contrast gray-on-gray text;
- clipped content, overlapping controls, or hidden essential actions;
- animation that delays repeated work or ignores reduced motion;
- a mobile layout that is only a scaled-down desktop;
- unverified chart or canvas output;
- a claim of completion without running the relevant build, checks, or visual inspection when they are available.

## Review Output

For a design review, lead with findings ordered by severity:

| Severity | Meaning |
|---|---|
| Critical | Blocks the primary workflow, hides data, breaks accessibility, or makes the page unusable at a supported width |
| High | Causes frequent confusion, incorrect interpretation, or a serious interaction failure |
| Medium | Weakens hierarchy, consistency, responsiveness, or efficiency |
| Low | Polish issue with limited workflow impact |

For each finding, include the observed problem, user impact, and a concrete correction. Keep general praise and summary secondary to actionable issues.
