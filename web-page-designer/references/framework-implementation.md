# Framework Implementation

The design system is framework- and CLI-agnostic. Integrate with the project's current stack and dependencies before considering replacements. Use the active coding agent's equivalent file, terminal, preview, browser, and screenshot capabilities; no named vendor tool is required.

## Shared Implementation Rules

1. Inspect the package manifest, app shell, routes, global styles, token files, and two representative pages.
2. Reuse existing primitives and patterns when they are accessible and coherent.
3. Add a dependency only when it removes meaningful complexity or implements behavior that is difficult to make robust.
4. Use semantic HTML landmarks and native elements before adding ARIA.
5. Keep page-specific layout near the page and genuinely reusable primitives in the established component layer.
6. Model loading, empty, error, and success states explicitly rather than overloading `null` or scattered booleans.
7. Keep data formatting centralized for dates, currency, percentages, and compact numbers.

## React

Use the existing React framework and router. Do not migrate between Next.js, Remix, Vite, or another stack for a design task.

Useful choices when the project has no established equivalent:

| Need | Preferred option |
|---|---|
| Accessible dialogs, popovers, menus, selects | Base UI or the project's current primitive library |
| Icons | Lucide React |
| General dashboard charts | Recharts |
| Real-time streaming charts | Liveline |
| Complex data tables | TanStack Table |
| Very long lists or grids | Virtuoso |
| Toasts | Sonner |
| Command palette | cmdk |
| Drag and drop | dnd-kit |
| Shared client state | Zustand only when component state or server-state tools are insufficient |
| Conditional class names | clsx |
| Typed Tailwind variants | cva |
| Springs, layout, exit, or gesture animation | Motion; use CSS for simple hover/fade feedback |

- Prefer server or route data mechanisms already present in the project.
- Avoid unnecessary client components and global state.
- Give chart containers stable dimensions or aspect ratios so loading and rendering do not shift layout.
- Memoize only when measurement shows a real cost; keep state ownership close to the interaction.

## Vue

Use the existing Vue version, router, state approach, and component conventions.

Useful choices when no equivalent exists:

| Need | Preferred option |
|---|---|
| Accessible headless primitives | Reka UI or the project's existing component library |
| Icons | lucide-vue-next |
| General and complex charts | Apache ECharts through the project's Vue wrapper |
| Complex data tables | TanStack Table Vue or the existing grid |
| Shared application state | Pinia when local/composable state is not enough |
| Utility composables | VueUse when it already fits the dependency strategy |

- Keep page orchestration in views and reusable behavior in focused components or composables.
- Do not put unrelated state in a single store merely because Pinia exists.
- Use `<Transition>` for simple state changes; add a motion library only for interruptible gestures, springs, or complex orchestration.
- Keep scoped styles, CSS modules, Tailwind, or the current styling system consistent with the repository.

## Plain HTML, CSS, And JavaScript

- Build semantic, progressively enhanced HTML first.
- Use CSS custom properties for tokens and CSS Grid/Flexbox for layout.
- Use small ES modules for interaction; avoid introducing a framework for one page.
- Use native controls where possible and preserve expected keyboard behavior.
- Native select popups cannot be styled consistently across operating systems. When the visual brief requires a coordinated rounded popup, use a proven accessible primitive or implement the full button/listbox pattern; do not replace `<select>` with an inert styled `<div>`.
- Keep a self-contained prototype in one HTML file only when there is no existing application or build pipeline.
- For production code, separate structure, styles, and behavior according to the existing project conventions.

## Other Web Stacks

- Apply the same semantic tokens, layout logic, component states, accessibility, and verification standards in Svelte, Solid, Astro, server-rendered templates, Web Components, or another web stack.
- Follow the repository's established component and state model instead of translating React patterns literally.
- Choose libraries native to that ecosystem only when the project lacks an equivalent and the behavior is complex enough to justify a dependency.

## Styling

- Use the project's current styling mechanism. Do not introduce Tailwind, CSS-in-JS, CSS modules, or a component system solely for this task.
- Define semantic tokens at the narrowest shared scope that benefits multiple components.
- Use grid tracks, min/max constraints, `aspect-ratio`, and stable control dimensions to prevent layout shift.
- Avoid viewport-width font scaling. Use explicit breakpoint steps.
- Target text wrapping deliberately. Use truncation only when the full value is available through a detail view, tooltip, or accessible label.
- Scope hover behavior to devices that support hover where touch emulation would cause sticky states.

```css
@media (hover: hover) and (pointer: fine) {
  .interactive:hover {
    border-color: var(--border-strong);
  }
}
```

## Responsive Strategy

Design from information priority, not from device names:

- Wide desktop: preserve comparison and optional support rails.
- Standard desktop: keep primary work visible; collapse low-priority chrome.
- Narrow desktop/tablet: reduce columns, collapse the sidebar, and move secondary tools to drawers or menus.
- Mobile: recompose content into a clear sequence; use appropriate navigation and keep tables usable through column prioritization or alternate rows.

Never solve responsiveness by shrinking the whole interface, reducing text below legibility, or allowing controls to overlap.

## Accessibility

- Use one `h1` and a logical heading hierarchy.
- Provide `main`, navigation, header, complementary, form, table, and dialog semantics as appropriate.
- Ensure every control has an accessible name and visible focus indication.
- Custom selects, menus, and popovers support Arrow keys, Enter/Space, Escape, outside click, selected semantics, and focus return.
- Keep focus inside modal dialogs and return it to the trigger when they close.
- Support keyboard operation for menus, tabs, tables, filters, and custom controls.
- Pair status color with text or an icon and announce meaningful asynchronous changes appropriately.
- Respect zoom, text enlargement, high contrast where practical, and `prefers-reduced-motion`.
- Do not disable outline without providing an equally visible replacement.

## Data Visualization

- Use a mature chart library for scales, axes, tooltips, responsiveness, and accessibility support.
- Transform source data through explicit typed or documented functions; do not derive values inside rendering markup.
- Test zero, negative, missing, extremely large, and single-point series.
- Use `ResizeObserver` or the library's responsive container correctly and give its parent a stable nonzero size.
- Provide a text summary and, when decisions depend on exact values, access to a table or detailed list.

## Performance And Motion

- Animate transform and opacity where possible.
- Prefer CSS transitions for simple interruptible feedback.
- Avoid animating height, width, margin, padding, or large blurred regions during frequent interactions.
- Virtualize only when row count and rendering cost justify it; virtualization adds accessibility and measurement complexity.
- Lazy-load heavy charts or secondary panels when doing so does not hide critical first-screen information.
- Prevent loading skeletons, icons, labels, or count changes from resizing controls.
