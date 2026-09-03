# Trilogys Skills

[English](README.md) | 简体中文

面向软件交付、工程师成长和专业 Web 界面设计的可移植、自包含 Agent Skills。每个顶层 skill 目录都可以独立安装到兼容的 CLI 中。

## 可用 Skills

### AI Coding Mentor

[`ai-coding-mentor`](ai-coding-mentor/SKILL.md) 帮助工程师在使用 AI 交付真实软件的同时，保留对代码的理解、评审判断和架构所有权。

它采用工作优先的三类任务模型：

- **A：** AI 执行样板代码和机械性工作。
- **B：** AI 执行常规工程工作，并总结重要决策。
- **C：** 用户继续参与架构、事务、并发、授权、资金、删除、迁移、安全及其他高风险决策。

该 skill 提供 `L0-L4` 干预等级、基于证据的能力档案、项目与全局学习状态、代码评审和安全清单、ADR 与 Bug 模板、月度证据收集，以及档案导入导出工具。

开始使用：

```text
使用 ai-coding-mentor。
/normal
mentor_level=L1

完整实现并验证这个需求，同时只提醒我一个最值得关注的高价值决策。
```

文档：[功能说明](ai-coding-mentor/README.md) | [安装说明](ai-coding-mentor/INSTALL.md)

### Web Page Designer

[`web-page-designer`](web-page-designer/SKILL.md) 用于设计、实现、重构或评审 React、Vue、原生 HTML/CSS 以及其他 Web 技术栈中的专业桌面优先页面。

它是一套设计系统和决策流程，不是固定的仪表盘模板。它会根据产品、用户、品牌、内容和使用环境推荐主题；没有明确方向时默认使用精致的蓝白主题。数据分析、CRM、电商、设置、列表、详情和表单等命名模式只是示例。面对未列出的功能时，skill 会根据产品对象、操作、使用频率、信息层级、工作形态和状态重新推导布局。

稳定的设计语言强调：

- 浅蓝灰画布、白色内容表面、近黑正文，并以蓝色作为主要功能强调色；
- 4 px 间距基础和有层级的圆角体系；
- 轻边框、极弱阴影，仅在内容确实有边界或需要比较时使用卡片；
- 适合桌面工作的内容密度、可预测导航、可读数据和完整交互状态；
- 300 ms 以内的功能性动画、减少动态效果支持，以及多视口视觉检查。

包内文档包括：

- [视觉基础](web-page-designer/references/visual-foundation.md)：色彩、排版、圆角、间距、布局、表面、卡片、图表、表格、表单和动画；
- [主题选择](web-page-designer/references/theme-selection.md)：主题优先级、项目适配信号、一致性调整和主题残留审计；
- [页面模式](web-page-designer/references/page-patterns.md)：结构示例，以及为任意功能推导布局的方法；
- [框架实现](web-page-designer/references/framework-implementation.md)：React、Vue、HTML/CSS、其他 Web 技术栈、无障碍、响应式行为和组件库选择；
- [质量门槛](web-page-designer/references/quality-gates.md)：产品、布局、视觉、交互、无障碍和截图检查。
- [HTML 校准 Demo](web-page-designer/examples/blue-white-operations-dashboard.html)：使用同一套 tokens 和质量规则实现的可交互蓝白运营页面。

开始使用：

```text
使用 web-page-designer，通过 React 设计并实现一个桌面优先的库存运营页面。保留现有品牌，根据实际工作流推导布局，并在 1280、1440 和 1920 像素宽度下验证结果。
```

## 应该使用哪个 Skill？

| 目标 | Skill |
|---|---|
| 交付代码，同时保留工程判断和成长 | `ai-coding-mentor` |
| 设计、实现、重构或评审 Web 界面 | `web-page-designer` |
| 同时改善工程流程和界面 | 同时使用两个 skill，并保持各自职责边界 |

## 安装

每个顶层目录都是一个完整 skill。安装时需要复制整个目录，不能只复制 `SKILL.md`。目录中的参考文档、模板、脚本、测试和元数据在存在时都属于 skill 的组成部分。

克隆当前 `dev` 分支：

```bash
git clone --branch dev https://github.com/trilogys/skills.git
cd skills
```

常见的 skill 发现目录：

| CLI | 个人范围 | 项目范围 |
|---|---|---|
| Codex | `~/.agents/skills/<name>/` | `.agents/skills/<name>/` |
| Claude Code | `~/.claude/skills/<name>/` | `.claude/skills/<name>/` |
| Kilo Code | `~/.kilo/skills/<name>/` 或 `~/.agents/skills/<name>/` | `.kilo/skills/<name>/` 或 `.agents/skills/<name>/` |
| OpenCode | `~/.config/opencode/skills/<name>/` 或 `~/.agents/skills/<name>/` | `.opencode/skills/<name>/` 或 `.agents/skills/<name>/` |

在 macOS 或 Linux 上安装单个 skill：

```bash
mkdir -p ~/.agents/skills
cp -R web-page-designer ~/.agents/skills/web-page-designer
```

在 Windows PowerShell 上安装单个 skill：

```powershell
New-Item -ItemType Directory -Force "$HOME\.agents\skills" | Out-Null
Copy-Item -Recurse .\web-page-designer "$HOME\.agents\skills\web-page-designer"
```

Claude Code 需要将 `.agents/skills` 替换为 `.claude/skills`。最终目录应当是 `<skills目录>/<skill名称>/SKILL.md`，不要产生重复嵌套的同名目录。

如果新安装的 skill 没有出现，请重启 CLI。可以通过名称显式调用，也可以由兼容的 Agent 根据 frontmatter 中的描述自动选择。

## 仓库结构

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
    ├── examples/
    └── references/
```

## 设计原则

- 每个 skill 只聚焦一个明确任务。
- 优先使用自包含指令和相对资源链接。
- 保留用户项目已有的约定和授权边界。
- 在不同 CLI 之间迁移时复制完整的 skill 目录。
- 将用户档案、密钥、项目证据和机器特定状态放在可复用 skill 包之外。

## 许可证

项目采用 [Apache License 2.0](LICENSE)。
