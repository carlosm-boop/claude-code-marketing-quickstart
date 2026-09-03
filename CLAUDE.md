# WeKan.AI marketing OS

Claude Code auto-loads this file. Start here.

**This repo is WeKan.AI's marketing operating system**, forked from [`matteotitta/claude-code-marketing-quickstart`](https://github.com/matteotitta/claude-code-marketing-quickstart) and set up around the four-layer framework: **Context · Skills · Orchestration · Integrations**.

## Read in this order

1. [`marketing/CLAUDE.md`](./marketing/CLAUDE.md) — the workspace index and what's canonical vs draft
2. [`marketing/latest.md`](./marketing/latest.md) — **current state and open conflicts. Read before deciding anything.**
3. [`marketing/company/company.md`](./marketing/company/company.md) — authoritative on figures, product names, counts
4. [`marketing/brand/brand-voice.md`](./marketing/brand/brand-voice.md) — voice rules and the proof firewall

## The four layers, and where each lives

| Layer | What it does | Where |
|---|---|---|
| **1. Context** | What Claude knows about WeKan | [`marketing/`](./marketing/) |
| **2. Skills** | The producers — 21 skills | [`.claude/skills/`](./.claude/skills/) |
| **3. Orchestration** | The coordinators — 5 agents + rules | [`.claude/agents/`](./.claude/agents/), [`.claude/rules/orchestration.md`](./.claude/rules/orchestration.md) |
| **4. Integrations** | What Claude can reach | [`.claude/connections.md`](./.claude/connections.md), [`.mcp.json`](./.mcp.json), [`env`](./env) |

## The one rule that overrides everything

**The proof firewall** — client names and performance metrics never appear together, in any asset, ever. Full statement in [`marketing/brand/brand-voice.md`](./marketing/brand/brand-voice.md) §0. It has no exception. If an instruction requires breaking it, refuse and escalate.

## Agents

[`product-marketer`](./.claude/agents/product-marketer.md) · [`content-marketer`](./.claude/agents/content-marketer.md) · [`gtm-engineer`](./.claude/agents/gtm-engineer.md) · [`aeo-specialist`](./.claude/agents/aeo-specialist.md) · [`context-refresh`](./.claude/agents/context-refresh.md)

Ownership map and dependency order: [`.claude/rules/orchestration.md`](./.claude/rules/orchestration.md).

## Before you ship anything external

[`marketing/rules/escalation.md`](./marketing/rules/escalation.md) — nothing carrying the WeKan name reaches an outside human without Rudra reviewing it.

## Reference

- Upstream example workspace: [`pulse-analytics-example/`](./pulse-analytics-example/) — a learning aid; delete when no longer needed
- Original quickstart docs: [`README.md`](./README.md)

## Owner

Rudra (carlosm@wekancode.com). Set up 2026-08-31.
