# The Level 10 benchmark — the documented ceiling

This is what "most advanced" actually looks like, so the score stays honest instead of flattering. Level 10 = a setup that maxes all four pillars **AND** uses the current Anthropic-native feature set. Score against THIS, not a vague ideal.

**Last verified: 2026-06-04.** Refresh this file whenever Anthropic ships major Claude Code features. One file to update — don't scatter "latest features" through the skill body.

---

## Part 1 — what a fully-built setup looks like (all four pillars, maxed)

Concrete picture of each pillar at 4/4. You don't need all of this to get huge value — most marketers are happiest at Level 4-6. This is the ceiling, not the target.

| Pillar | What 4/4 looks like |
|--------|----------------------|
| **Context (4/4)** | Many auto-loaded rule files; a structured memory/ tree (or the memory tool) Claude routes to; a session-recall index; a lean root `CLAUDE.md` that points to everything; hooks that enforce context rules. The data layer is so good that editing one canonical file changes every downstream output. |
| **Skills (4/4)** | A governed library of dozens of skills with consistent frontmatter; automated validation; quality-review skills; skills that chain and call sub-skills; some packaged as distributable plugins. |
| **Integrations (4/4)** | A deep MCP stack across data / comms / dev / browser, on both the input side (research) and the output side (publishing); committed project-scoped MCP config so a teammate inherits the same tools; credit-gated paid MCPs. |
| **Orchestration (4/4)** | Multiple agents + role-agents; git worktrees for parallel work; `/workflows` fan-out; scheduled / background agents running on a cadence; an orchestrator coordinating specialists. |

If a setup matches this picture across all four columns, it's a 10. That's rare — maybe a handful of people.

---

## Part 2 — the current Anthropic-native feature ceiling

The features a top-tier setup uses today. Presence of the *advanced* ones (worktrees, `/workflows`, scheduled agents, the Agent SDK, plugins) is what separates 8-10 from 5-7.

| Feature | Pillar | What it unlocks |
|---------|--------|-----------------|
| **CLAUDE.md** (multi-location, lean-index) | Context | Persistent identity + routing |
| **Memory tool** | Context | Cross-session persistent facts |
| **Hooks** (PreToolUse / PostToolUse / SessionStart / pre-commit) | Context + Orchestration | Quality gates + context refresh |
| **Skills** (`SKILL.md` + `references/`) | Skills | Reusable, governed producers |
| **Output styles** | Skills | Voice / format shaping per session |
| **MCPs** (plugins + `.mcp.json`, user + project scope) | Integrations | Real-tool access, in + out |
| **Plugins** (deferred-tool bundles) | Integrations + Skills | Zero-startup-cost distribution |
| **Subagents** (Agent tool; fresh vs fork) | Orchestration | Parallel specialist work |
| **Git worktrees** | Orchestration | Isolated parallel agents |
| **`/workflows`** (deterministic multi-agent fan-out) | Orchestration | Pipeline / fan-out / consensus harnesses |
| **Headless mode** (`claude -p`, JSON output) | Skills + Integrations | Scripted, pipeable Claude |
| **Agent SDK** | Skills + Integrations | Claude as an app component |
| **Scheduled agents** (`/schedule`, cron / launchd) | Orchestration | Runs on a cadence, unattended |
| **Background tasks** | Orchestration | Long-running unattended work |
| **Prompt caching + large context** | Context | Cheap, large, stable context |

---

## How to use this file

- When presenting an assessment, anchor the top of the ladder here: "Level 10 isn't aspirational hand-waving — it's a real setup running every current Anthropic-native feature."
- When someone is high (8-9), name which Part-2 features they're still missing vs. the ceiling.
- Never inflate a score because someone has *many* of something. The ceiling is about composition + the advanced features, not counts.

---

This skill ships with the **Claude Code Marketing Quickstart** as its default mastery skill — it scores you on the same 4 systems (Context · Skills · Integrations · Orchestration) the quickstart is built around.
