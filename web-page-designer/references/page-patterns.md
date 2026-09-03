# Page Patterns

This is an example library, not an exhaustive list of supported pages. The skill applies to any web function. Select a nearby pattern when it fits; otherwise derive a new layout from the actual workflow. Never reject, omit, or force a feature because its page type is not named here.

## Derive A Pattern For Any Function

For an unlisted page, determine:

1. **Objects:** what users inspect or manipulate, such as files, records, messages, media, nodes, schedules, documents, or inventory.
2. **Actions:** the primary creation, editing, comparison, approval, navigation, or monitoring task.
3. **Frequency:** which actions happen continuously, regularly, occasionally, or rarely.
4. **Hierarchy:** what must remain visible, what can move to a secondary surface, and what needs progressive disclosure.
5. **Working shape:** choose the structure that best supports the task, such as canvas plus inspector, split pane, timeline, calendar, inbox, board, editor, gallery, map, command surface, or a new composition.
6. **States:** include the real loading, empty, error, selection, editing, permission, and collaboration states of that function.
7. **Visual application:** apply the shared color, radius, spacing, surface, typography, card, and motion language after the workflow structure is correct.

The patterns below demonstrate how function changes structure while the visual system remains recognizable.

## Pattern Matrix

| Page type | Recommended structure | Primary design risk |
|---|---|---|
| Executive dashboard | Header and period controls; 3-4 KPIs; one dominant trend; supporting breakdown; exceptions table | Too many equally weighted cards |
| Analytics workspace | Query/filter bar; metric context; large chart; comparison or segmentation; underlying data table | Charts without a clear analytical question |
| Operational list | Title and create action; local search/filter/saved views; bulk actions; data table; pagination | Decorative cards replacing an efficient table |
| Entity detail | Breadcrumb/back; identity and status; primary actions; summary; tabs; activity or related records | Scattering one entity across disconnected cards |
| Create/edit form | Focused header; grouped form sections; inline validation; sticky or final action row | Excessive columns and hidden errors |
| Settings | Product or account context; sub-navigation; narrow settings content; save/revert feedback | Treating every toggle as a separate card |
| CRM/pipeline | Scope and ownership filters; table or stages; record preview; fast updates; activity context | Losing context when opening a record |
| Finance | Balance and date context; cash-flow or performance view; accounts/categories; transactions; clear units | Decorative financial charts and ambiguous periods |
| Commerce/admin | Sales or inventory summary; actionable exceptions; product/order/customer table; fulfillment status | Surface-level KPIs with no path to action |
| Monitoring/operations | Environment and time range; status summary; live signals; incidents/exceptions; dense event log | Over-animation and low information density |
| Authentication/onboarding | Focused identity surface; one task per step; progress only when meaningful; recovery paths | Carrying the entire app shell into a focused flow |
| SaaS marketing | Product name and literal offer; real product visual; primary action; proof; feature evidence; pricing or conversion path | Turning the page into abstract decoration |

## Dashboard And Analytics

Use a dashboard only when users need several signals at once. A strong default composition is:

```text
Page header: title, context, date range, primary action
KPI row: 3-4 comparable metrics
Main row: dominant trend (8 cols) + breakdown/exceptions (4 cols)
Evidence row: full-width table or operational queue
```

- Lead with decisions, not chart variety. If a metric cannot change a decision, demote or remove it.
- Show the current value, comparison baseline, time range, and data freshness.
- Prefer one large explanatory chart to a grid of small unrelated plots.
- Put exception lists, unpaid items, low stock, failed jobs, or anomalies where users can act on them.
- Keep global and local filters visually distinct.

## Lists And Data Grids

- Use tables for comparison across stable attributes. Use cards only when records are visually rich or have highly variable content.
- Keep title, result count, create action, search, filters, and saved views in a predictable toolbar.
- Allow users to clear filters and see which filters are active.
- Keep important columns visible; move low-value metadata into a detail view or column chooser.
- Preserve scroll, selection, filters, and pagination after viewing or editing an item.
- For large sets, use server-side pagination or virtualization based on the data source and workflow.

## Detail Views

- The header owns identity, status, and high-value actions.
- Present a concise summary before tabs. Do not make users open tabs to confirm the entity they are viewing.
- Use tabs for distinct bodies of work, not for avoiding a thoughtful page hierarchy.
- Put activity, comments, or audit history in a right rail only when users need it while working in the main content.
- Destructive actions belong in a clearly separated menu or danger section.

## Forms And Workflows

- Default content width: 640-760 px for simple forms; wider only for side-by-side fields with a real relationship.
- Order fields according to the user's mental model, not the database schema.
- Use sections with headings and short context. Avoid an accordion unless the form is long and users understand the section boundaries.
- Show dependencies immediately when one choice reveals or disables another.
- For long workflows, save drafts and expose progress. For short workflows, avoid unnecessary steppers.
- Keep cancel/revert and save/submit visually distinct.

## Settings

- Separate account, organization, billing, integrations, notifications, and security by user intent.
- Use a compact sub-navigation and a readable content column instead of a wall of cards.
- Save immediately only when the change is low risk and feedback is clear. Otherwise use an explicit save action.
- Explain consequences near high-impact controls, not in a distant help panel.

## CRM, Commerce, And Operational Work

- Design for repeated scanning and action: stable columns, predictable controls, compact filters, and preserved context.
- Place actionable exceptions before historical summaries.
- Use status colors consistently across charts, chips, rows, and detail views.
- Pair aggregate numbers with a route to the underlying records.
- Favor drawers or split views for quick inspection when returning to the list context matters.

## Finance

- Always show currency, period, account scope, and whether a number is actual, pending, projected, gross, or net.
- Use tabular numerals and align decimals.
- Separate positive/negative semantics from category colors. Green must not ambiguously mean both income and healthy status.
- Provide transaction-level evidence behind summaries.
- Keep exports and date controls close to the scoped data.

## Monitoring

- Favor fast, dense, low-motion interfaces.
- Treat current state, change, severity, ownership, and time as first-class fields.
- Use color with text/icon redundancy for alert severity.
- Keep live updates from moving controls or changing the user's reading position.
- Provide pause, time-window, and filtering controls when data streams continuously.

## SaaS Marketing

- The first viewport must establish the product name or literal offer and show the real interface, product, or outcome.
- Do not use a split hero where text and an unrelated decorative card compete equally.
- Use a strong real screenshot or interactive product scene; avoid abstract gradient/SVG decoration as the primary visual.
- Let the next section remain partially visible across common viewport sizes.
- Build proof from product evidence, customer outcomes, integrations, or concrete capabilities rather than generic claims.
- Keep card grids limited. Use full-width bands and unframed layouts for major sections.

## Cross-Pattern Rules

- One page, one dominant job, one primary action.
- Put controls near what they affect.
- Keep common actions visible and advanced options one level deeper.
- Use progressive disclosure without hiding essential context.
- Preserve spatial and navigational context after modal, drawer, or detail interactions.
- For destructive changes, prefer undo; confirm only when reversal is impossible or costly.
- Every screen must answer: where am I, what can I do, what changed, and how do I leave?
