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

设计流程强调：

- 根据产品、用户、品牌、内容、使用环境和操作频率选择主题；
- 没有明确方向时，使用“冷蓝灰外框 + 白色或近白工作画布”的精致蓝白主题；
- 采用 4 px 间距基础和协调的圆角家族：展示外框 28-32 px、产品面板 10-12 px、控件 8-10 px、浮层菜单 10-12 px；
- 使用中等字重的界面字体、等宽数字节奏、克制蓝色、浅边框和大范围低透明阴影；
- 根据用户、任务、语言、观看距离、内容密度和字体度量建立项目专属的语义字号体系，而不是复制固定像素常量；
- 使用同一套线性图标，统一尺寸、线宽、颜色、容器和光学校准；
- 只在内容确实有边界或需要比较时使用卡片，页面拓扑始终根据真实工作流推导；
- 使用 300 ms 以内的功能性动画、完整交互状态、减少动态效果支持和多轮截图修正。

包内文档包括：

- [视觉基础](web-page-designer/references/visual-foundation.md)：色彩、排版、圆角、间距、布局、表面、卡片、图表、表格、表单和动画；
- [自适应排版](web-page-designer/references/typography-system.md)：密度基准、语义角色、中英文校准、字重、行高、响应式排版和缩放检查；
- [主题选择](web-page-designer/references/theme-selection.md)：主题优先级、项目适配信号、一致性调整和主题残留审计；
- [页面模式](web-page-designer/references/page-patterns.md)：结构示例，以及为任意功能推导布局的方法；
- [框架实现](web-page-designer/references/framework-implementation.md)：React、Vue、HTML/CSS、可访问浮层控件、响应式行为和组件库选择；
- [质量门槛](web-page-designer/references/quality-gates.md)：产品、布局、字体、图标、展开态浮层、无障碍和截图检查；
- [HTML 校准 Demo](web-page-designer/examples/blue-white-operations-dashboard.html)：包含圆角可访问下拉、筛选、图表、弹窗状态和响应式布局的交互式蓝白运营页面；
- [视觉参考资产](web-page-designer/assets/NOTICE.md)：两张用户提供的截图，仅用于校准质感，不作为可复用品牌或页面模板。

该 skill 会检查控件的展开状态，而不只检查收起外观。当操作系统原生下拉菜单与整体视觉规范冲突时，它要求使用成熟的可访问组件，或实现完整的按钮/Listbox 模式，包括键盘导航、Escape 关闭、点击外部关闭、选中语义和焦点归还。

排版示例只是校准范围，不是一张通用字号表。密集专业工具、标准 SaaS、阅读工作台、消费流程和远距展示会分别建立正文、控件、元数据、标题和数据字号；中文界面不会直接套用拉丁字体的数值，并要求在浏览器 100%、125% 和 200% 缩放下验证。

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
    ├── assets/
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

项目采用 [Apache License 2.0](LICENSE)。用户提供的第三方视觉参考截图按[资产说明](web-page-designer/assets/NOTICE.md)排除在该许可证之外。
