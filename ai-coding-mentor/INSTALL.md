# Installation and Cross-CLI Continuity

## Recommended layout

Keep one canonical copy of the Skill and one separate global profile.

For Codex, Kilo Code, and OpenCode, the common user-level Skill location is:

```text
~/.agents/skills/ai-coding-mentor/
```

Claude Code uses:

```text
~/.claude/skills/ai-coding-mentor/
```

On macOS/Linux, the Claude directory can be a symlink to the canonical `.agents` copy. On Windows, copying the complete folder to both locations is usually simpler unless symbolic links are already enabled.

Always copy the whole folder, not only `SKILL.md`.

## Platform locations

| CLI | Personal Skill location | Project Skill location |
|---|---|---|
| Codex | `~/.agents/skills/<name>/` | `.agents/skills/<name>/` |
| Kilo Code | `~/.kilo/skills/<name>/` or `~/.agents/skills/<name>/` | `.kilo/skills/<name>/` or `.agents/skills/<name>/` |
| Claude Code | `~/.claude/skills/<name>/` | `.claude/skills/<name>/` |
| OpenCode | `~/.config/opencode/skills/<name>/` or `~/.agents/skills/<name>/` | `.opencode/skills/<name>/` or `.agents/skills/<name>/` |

The shared `.agents/skills` location minimizes duplicate installation for Codex, Kilo, and OpenCode. Claude Code still needs its compatible path or a symlink.

## Windows example

Extract the ZIP, then copy the top-level `ai-coding-mentor` folder to:

```text
C:\Users\<your-user>\.agents\skills\ai-coding-mentor\
C:\Users\<your-user>\.claude\skills\ai-coding-mentor\
```

Kilo can alternatively use:

```text
C:\Users\<your-user>\.kilo\skills\ai-coding-mentor\
```

Restart the CLI if the Skill does not appear after installation. In Codex, list or invoke it with `/skills` or `$ai-coding-mentor`. In Claude Code it is available as a Skill command. Other clients can select it implicitly from the description or by name.

## Initialize shared state

The Skill files do not contain your profile. Initialize state from a repository:

```bash
python <skill-folder>/scripts/init_state.py --scope all
```

This creates:

- global state at `~/.ai-coding-mentor/`;
- project state at `<repo>/.ai-mentor/`;
- ADR templates at `<repo>/docs/adr/`.

Nothing existing is overwritten.

To keep the global profile elsewhere:

```bash
python <skill-folder>/scripts/init_state.py --scope all --global-dir D:\private\ai-mentor-profile
```

Then set `AI_MENTOR_HOME` to the same location for every local CLI. The profile stays shared even when the Skill is installed in several CLI-specific folders.

## Recommended first request

```text
Use ai-coding-mentor.
/profile

Initialize or review my mentor profile. If V2 project profile files exist, preserve them and migrate only generalized evidence. Do not infer mastery from AI-generated code.
```

For everyday work:

```text
Use ai-coding-mentor.
/normal
mentor_level=L1

Implement this requirement completely, verify it, and focus my attention on at most one high-value decision.
```

## Different machine or remote container

A local user profile is not automatically visible in a remote shell, cloud session, container, or another computer.

Use one of:

- a private synchronized directory selected through `AI_MENTOR_HOME`;
- a private Git repository containing only generalized global profile files;
- the bundled export/import helper.

Never put project evidence, secrets, proprietary code, customer data, or internal incident payloads in a public profile repository.

Export and stage an import:

```bash
python <skill-folder>/scripts/profile_portability.py export --output mentor-profile.zip
python <skill-folder>/scripts/profile_portability.py import --bundle mentor-profile.zip
```

The importer writes only to a new `imports/<timestamp>/` directory. Run `/profile` to compare and merge; it does not overwrite live state.

## Existing V2 project

Run the initializer in the existing repository. It will preserve V2's `CAPABILITY_PROFILE.md` and `SKILL_MATRIX.md` and create the current files beside them.

Do not delete V2 files until you have reviewed the first `/profile` result and confirmed the evidence was retained.

## Official format and client references

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Kilo Code: Skills](https://kilo.ai/docs/customize/skills)
- [Claude Code: Extend Claude with skills](https://code.claude.com/docs/en/skills)
- [OpenCode: Agent Skills](https://opencode.ai/docs/skills/)
- [Agent Skills specification](https://agentskills.io/specification)
