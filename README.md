# Trilogys Skills

English | [简体中文](README.zh-CN.md)

Portable, self-contained Agent Skills for software delivery, engineering growth, and professional web interface design. Each top-level skill directory can be installed independently in any compatible CLI.

## Available Skills

### AI Coding Mentor

[`ai-coding-mentor`](ai-coding-mentor/SKILL.md) helps engineers ship real software with AI while retaining understanding, review judgment, and architecture ownership.

Its work-first model separates tasks into three ownership classes:

- **A:** AI executes boilerplate and mechanical work.
- **B:** AI executes ordinary engineering work and summarizes the important decisions.
- **C:** the user remains involved in architecture, transactions, concurrency, authorization, money, deletion, migrations, security, and other high-risk decisions.

The skill provides intervention levels `L0-L4`, evidence-based capability profiles, project and global learning state, review and security checklists, ADR and bug templates, monthly evidence collection, and profile export/import tools.

Start with:

```text
Use ai-coding-mentor.
/normal
mentor_level=L1

Implement this requirement completely, verify it, and focus my attention on at most one high-value decision.
```

Documentation: [overview](ai-coding-mentor/README.md) | [installation](ai-coding-mentor/INSTALL.md)

### Web Page Designer

[`web-page-designer`](web-page-designer/SKILL.md) designs, implements, redesigns, or reviews polished desktop-first web pages in React, Vue, plain HTML/CSS, and comparable web stacks.

It is a design system and decision workflow rather than a fixed dashboard template. Named patterns such as analytics, CRM, commerce, settings, lists, details, and forms are examples. For any unlisted function, the skill derives a layout from the product's objects, actions, frequency, information hierarchy, working shape, and states.

The stable design language emphasizes:

- soft blue-gray canvases, white surfaces, near-black text, and blue as the primary functional accent;
- a 4 px spacing foundation and a deliberate radius hierarchy;
- light borders, minimal elevation, and cards only where content is genuinely bounded or comparable;
- desktop information density, predictable navigation, readable data, and complete interaction states;
- purposeful motion under 300 ms, reduced-motion support, and visual verification at multiple viewport sizes.

The package includes separate guidance for:

- [visual foundation](web-page-designer/references/visual-foundation.md): color, typography, radius, spacing, layout, surfaces, cards, charts, tables, forms, and motion;
- [page patterns](web-page-designer/references/page-patterns.md): example structures plus a method for deriving layouts for any function;
- [framework implementation](web-page-designer/references/framework-implementation.md): React, Vue, HTML/CSS, other web stacks, accessibility, responsive behavior, and library choices;
- [quality gates](web-page-designer/references/quality-gates.md): product, layout, visual, interaction, accessibility, and screenshot checks.

Start with:

```text
Use web-page-designer to design and implement a desktop-first inventory operations page in React. Preserve the current brand, derive the layout from the workflow, and verify the result at 1280, 1440, and 1920 pixel widths.
```

## Which Skill Should I Use?

| Goal | Skill |
|---|---|
| Deliver code while preserving engineering judgment and growth | `ai-coding-mentor` |
| Design, implement, redesign, or review a web interface | `web-page-designer` |
| Improve both the engineering workflow and the interface | Use both; keep each skill responsible for its own domain |

## Installation

Each top-level directory is one complete skill. Install the entire directory, not only its `SKILL.md`. References, templates, scripts, tests, and metadata are part of a skill when present.

Clone the current `dev` branch:

```bash
git clone --branch dev https://github.com/trilogys/skills.git
cd skills
```

Common skill discovery locations:

| CLI | Personal scope | Project scope |
|---|---|---|
| Codex | `~/.agents/skills/<name>/` | `.agents/skills/<name>/` |
| Claude Code | `~/.claude/skills/<name>/` | `.claude/skills/<name>/` |
| Kilo Code | `~/.kilo/skills/<name>/` or `~/.agents/skills/<name>/` | `.kilo/skills/<name>/` or `.agents/skills/<name>/` |
| OpenCode | `~/.config/opencode/skills/<name>/` or `~/.agents/skills/<name>/` | `.opencode/skills/<name>/` or `.agents/skills/<name>/` |

Install one skill on macOS or Linux:

```bash
mkdir -p ~/.agents/skills
cp -R web-page-designer ~/.agents/skills/web-page-designer
```

Install one skill on Windows PowerShell:

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse .\web-page-designer "$HOME\.agents\skills\web-page-designer"
```

For Claude Code, replace `.agents/skills` with `.claude/skills`. Keep the final layout as `<skills-directory>/<skill-name>/SKILL.md` and avoid a duplicated nested folder.

Restart the CLI if a newly installed skill does not appear. Invoke a skill explicitly by name or let a compatible agent select it from the frontmatter description.

## Repository Layout

```text
skills/
├── README.md
├── README.zh-CN.md
├── LICENSE
├── ai-coding-mentor/
│   ├── SKILL.md
│   ├── README.md
│   ├── INSTALL.md
│   ├── references/
│   ├── templates/
│   ├── scripts/
│   └── tests/
└── web-page-designer/
    ├── SKILL.md
    ├── agents/
    └── references/
```

## Design Principles

- Keep each skill focused on one job.
- Prefer self-contained instructions and relative resource links.
- Preserve the user's existing project conventions and authorization boundaries.
- Copy a complete skill directory when moving between CLIs.
- Keep user profiles, secrets, project evidence, and machine-specific state outside the reusable skill package.

## License

Licensed under the [Apache License 2.0](LICENSE).
