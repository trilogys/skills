# Theme Selection

Choose a theme as a product decision, not a palette swap. The theme must support the product's work, audience, content, brand, and environment while keeping every visual layer coherent.

## Decision Precedence

Use this order:

1. **Explicit user direction:** follow the requested theme unless it creates a concrete accessibility or usability problem; explain and correct that problem without replacing the user's intent.
2. **Coherent existing identity:** when a product already has deliberate brand and component tokens, preserve them. Treat the existing identity as an implied direction even if the current request does not restate it.
3. **Strong product fit:** when no coherent system exists, recommend the direction best supported by the project signals below.
4. **Default:** when evidence does not favor another direction, use the refined blue-and-white foundation in `visual-foundation.md`.

Do not ask the user to choose from several arbitrary palettes. Recommend one direction and explain the product reason in one or two sentences. Offer alternatives only when the user asks to explore.

## Read The Project Signals

Evaluate:

- **Domain and trust:** finance, healthcare, infrastructure, creative work, commerce, education, entertainment, or another domain.
- **Audience:** expert operators, occasional business users, consumers, creators, children, or mixed roles.
- **Task frequency:** repetitive high-frequency work needs quieter color, lower motion, and denser controls than an occasional consumer flow.
- **Content protagonist:** data, text, media, products, maps, schedules, code, or a canvas should determine what stays visually neutral.
- **Environment:** office daylight, mobile field use, control room, presentation screen, or prolonged night use.
- **Desired feeling:** calm, trustworthy, precise, energetic, premium, friendly, or expressive.
- **Brand evidence:** logo, product imagery, existing colors, type, icon family, screenshots, and established customer expectations.
- **Accessibility:** contrast, color-vision resilience, reduced motion, text enlargement, and localization.

## Useful Directions

These are reasoning anchors, not templates:

| Direction | Strong fit | Character and constraints |
|---|---|---|
| Refined blue-and-white | General SaaS, analytics, operations, finance, enterprise workflows | Cool blue-gray exterior, white or near-white working canvas, soft medium-blue emphasis, restrained elevation; use when no stronger direction exists |
| Graphite-neutral with cool accents | Developer tools, security, infrastructure, dense monitoring | Neutral graphite text and dividers with limited cool accents; do not turn the whole product into dark slate unless the environment supports dark mode |
| Content-led white | Commerce, portfolios, media libraries, catalog tools | Keep chrome quiet so product imagery or user content owns color; accents come from brand and actions, not decorative panels |
| Soft clinical | Healthcare, education, wellness, careful guided workflows | Airier spacing, calm blue or blue-green support colors, direct labels, low visual stress; avoid childish pastels and vague iconography |
| High-contrast editorial | Publishing, premium services, research, presentation-heavy products | Strong typography and whitespace with minimal accent; avoid oversized editorial type inside operational tools |
| Contextual dark | Night operations, media editing, visualization, or an explicit user preference | Near-neutral dark surfaces, controlled elevation, desaturated accents, and tested contrast; provide a complete light counterpart when the product requires both |

Do not choose a direction from industry stereotypes alone. A playful finance education product may differ from a treasury operations console; the workflow and audience decide.

## Build A Coherent Theme Contract

Before implementation, define the relationships, not merely hex values:

- canvas versus surface separation;
- exterior presentation frame versus the application working canvas;
- primary, secondary, muted, and inverse text;
- primary action, active selection, links, focus, and data-series emphasis;
- success, warning, danger, and information semantics;
- border strength, elevation, overlay tint, and disabled treatment;
- closed-control and open-popup geometry, shadow, focus, and selected treatment;
- typography character and density;
- radius family for shell, panels, controls, menus, and pills;
- icon family, stroke or fill style, size, color, and containers;
- motion duration, easing, origin, and reduced-motion behavior.

Use semantic tokens so components express roles rather than hard-coded colors. A theme is coherent only when the same role looks related in navigation, tables, forms, charts, dialogs, and feedback.

## Adapt Without Losing Quality

- Change layout to fit the job. Keep theme quality through shared optical rules, not through repeating the same sidebar, card grid, or dashboard composition.
- Tune radius by product character and density. Softer consumer products may use 10-12 px internal cards; dense professional tools usually benefit from 6-8 px. Preserve a consistent hierarchy either way.
- Tune spacing by frequency and content. More whitespace is not automatically more premium; repeated work often benefits from tighter grouping.
- Let imagery and content dominate when they are the product. Reduce chrome color rather than competing with it.
- Make icons inherit the theme's weight and contrast. Do not use icon backgrounds, multicolor marks, or playful shapes as a shortcut to personality.

## Theme Change Audit

When changing an existing theme, search and inspect all of these before delivery:

- raw color literals and legacy token names;
- active navigation, links, focus rings, selection fills, and primary actions;
- charts, status colors, illustrations, logos, and empty states;
- borders, shadows, overlays, backdrop tints, skeletons, and disabled controls;
- icons, icon containers, hover states, pressed states, and tooltips;
- browser theme metadata, favicons, screenshots, and documentation examples.

Do not declare the theme changed while old accents remain in secondary components. Replace or intentionally map every surviving legacy value.

## Recommendation Output

Keep recommendations concise:

```text
Theme: <name>
Why it fits: <product and audience reason>
Visual contract: <surface, accent, density, radius, icon, and motion character>
Watch-out: <main risk or condition that would invalidate the choice>
```

Do not place this explanation inside the product UI. Use it in the work plan or final handoff only when it helps the user evaluate the decision.
