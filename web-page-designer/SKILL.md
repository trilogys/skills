---
name: web-page-designer
description: Design, implement, redesign, or review polished desktop-first web pages across React, Vue, plain HTML/CSS, and comparable web stacks. Apply a reusable visual system for color, radius, spacing, cards, layout, typography, states, and motion while deriving the page structure from each project's actual function. Use for product interfaces and restrained SaaS pages in any domain; do not use for native mobile apps or illustration-only brand work.
---

# Web Page Designer

Create working web interfaces that feel calm, precise, and ready for repeated professional use. This is a visual-system and design-detail skill, not a closed catalog of page templates. Treat design as task architecture plus visual craft, not decoration. Match the user's language in UI copy and explanations.

## Reference Routing

- Always read [references/visual-foundation.md](references/visual-foundation.md) before making visual decisions. It is the canonical style baseline distilled from the supplied reference images.
- Read [references/page-patterns.md](references/page-patterns.md) when choosing or deriving the information architecture for a page or feature. Its named page types are examples, not a supported-function limit.
- Read [references/framework-implementation.md](references/framework-implementation.md) before implementing in React, Vue, or plain HTML/CSS.
- Read [references/quality-gates.md](references/quality-gates.md) before final verification or when reviewing an existing interface.

## Design Position

- Treat the reference visual language as the default house style. Preserve an intentional existing brand and component system; otherwise keep the skill's visual DNA stable across projects and vary only what the function, data, or brand meaningfully requires.
- Start from the product's real task, content, and user frequency. A dashboard, editor, settings page, checkout, and marketing page require different structures.
- Support any web function. If no example pattern matches, derive a new structure from the user's objects, actions, information priority, and workflow instead of forcing the page into a dashboard or card grid.
- Optimize desktop product interfaces for scanning, comparison, and repeated action. Keep them quiet, compact, predictable, and keyboard-friendly.
- Use hierarchy, alignment, spacing, and contrast before adding containers. Do not turn every section into a card, float whole page sections, or place cards inside cards.
- Make the actual product or workflow the first-screen experience. Do not add feature-explaining prose, decorative hero copy, or instructions inside the interface unless the product genuinely needs them.
- Use realistic domain content. No lorem ipsum, dead controls, meaningless charts, or arbitrary metrics.
- Use icons from the project's existing icon library, or Lucide when no library exists. Use familiar icons for common actions and tooltips for unfamiliar icon-only controls.
- Prefer a proven accessible primitive, table, chart, drag-and-drop, or virtualization library over hand-rolling complex behavior.

## Operating Modes

Infer the mode from the request:

- **Build:** create and integrate a complete page or feature.
- **Redesign:** preserve behavior and data while improving structure and visual language.
- **Review:** identify concrete design defects, their impact, and specific corrections; do not modify code unless asked.
- **Explore:** only when the user asks for alternatives, build three genuinely different directions around a named axis such as density, hierarchy, or interaction model. Keep them isolated from production and use realistic content. Do not generate variants that differ only in color.

## Workflow

### 1. Read the product context

Inspect the repository before designing. Determine:

- framework, routing, styling approach, component and icon libraries;
- existing tokens, fonts, breakpoints, data contracts, and reusable shells;
- page purpose, primary user, primary action, frequent actions, and destructive actions;
- target viewport and whether the page must also work on tablet or mobile;
- required states: loading, empty, error, partial data, permission-restricted, disabled, selected, hover, focus, and active.

If context is missing, make conservative assumptions and state only the assumptions that materially affect the result.

### 2. Establish the page contract

Before implementation, be able to state:

- the one job this page performs;
- the first thing the user should notice;
- the primary action and the secondary actions;
- the information order from summary to evidence to action;
- the example pattern selected from `page-patterns.md`, or the custom structure derived for an unlisted function;
- the density level: focused, standard, or dense;
- the responsive collapse strategy.

Do not expose this analysis as visible page copy.

### 3. Establish or reuse tokens

Reuse the existing system when it is coherent. Otherwise create a small semantic token layer for canvas, surfaces, text, borders, accent, status colors, spacing, radii, shadows, and motion. Use the defaults in `visual-foundation.md`; do not scatter raw colors and arbitrary spacing through components.

### 4. Build hierarchy before detail

Implement in this order:

1. application shell and navigation;
2. page header, context, filters, and actions;
3. primary content and comparison structure;
4. supporting content;
5. component states and feedback;
6. visual polish and motion.

Use full-width bands or unframed layouts for page sections. Reserve cards for repeated comparable units, compact tools, or genuinely bounded content.

### 5. Make the interface complete

- Every visible control must work or be clearly disabled.
- Provide meaningful loading, empty, error, success, and no-permission states where the workflow can reach them.
- Keep filters close to the data they affect and preserve user context across actions.
- Validate forms inline; retain entered values after recoverable errors.
- Confirm only genuinely destructive or irreversible actions. Prefer undo for reversible actions.
- Keep labels specific and concise. Distinguish actions by verb and destinations by noun.
- Make tables, charts, and summary values agree with one another; do not use visualization as decoration.

### 6. Apply restrained motion

- Animate only to explain state, preserve spatial continuity, provide feedback, or soften a meaningful change.
- Skip animation for keyboard-triggered and very frequent actions. Repeated workflows must feel immediate.
- Keep ordinary UI motion under 300 ms. Use `ease-out` for entrances and direct feedback, `ease-in-out` for movement already on screen, and linear timing only for continuous progress.
- Prefer transform and opacity. Avoid `transition: all`, layout-thrashing properties, and animation that changes the page's measured geometry unexpectedly.
- Make popovers originate from their trigger; keep centered modals centered.
- Support `prefers-reduced-motion` with instant state changes or restrained crossfades.

### 7. Verify the result

Use the available browser or visual testing tools when possible. Check the real page at the relevant routes and data states. At minimum verify:

- desktop widths around 1280, 1440, and 1920 pixels;
- the narrowest supported width and one long-content case;
- no overlap, clipped text, accidental horizontal scrolling, layout shift, or blank chart/canvas;
- keyboard navigation, visible focus, accessible names, contrast, and reduced motion;
- working interactions and a clean browser console.

Iterate on the implementation until the applicable gates in `quality-gates.md` pass. Report the route or file, the main design decisions, and what was verified.

## Boundaries

- Do not replace a coherent brand with the reference palette merely to make the page resemble the samples.
- Do not add a dependency for a simple CSS behavior or duplicate a library the project already uses.
- Do not force mobile interaction patterns, oversized touch controls, or decorative landing-page composition onto dense desktop tools.
- Do not equate minimalism with hiding context. A professional interface may be dense when the workflow demands it.
- Do not claim pixel-perfect reproduction when only screenshots, not source assets and specifications, are available.

## Cross-CLI Portability

- Keep the skill self-contained. Do not require another skill, a named agent product, a proprietary tool, or a product-specific command to complete the design workflow.
- Interpret actions such as inspect files, edit code, run the app, capture screenshots, and check the console through whatever equivalent tools the active CLI provides.
- If a preferred browser or visual-testing tool is unavailable, use the closest available preview and state the unverified visual risk; do not block ordinary design work solely because a named tool is absent.
- Keep all resource links relative to the skill folder. `SKILL.md` and `references/` form the portable core that can be installed in compatible Claude, Codex, Kilo, or other agent-skill directories.
- Treat `agents/openai.yaml` as optional Codex UI metadata. Other compatible CLIs may ignore it without changing the skill's behavior.
