# .claude/ — Claude Code runtime directory

Everything Claude Code needs to run sits here: skills, agents, hooks, rules, configuration. Three of the four systems in this repo's framework (action / orchestration / integrations) have their definitions in this folder.

## What's in here

| Path | Purpose |
|---|---|
| [`skills/`](./skills/) | 21 skills — the 10 upstream research skills plus 10 WeKan lane skills (`lead-scoring`, `abm-campaign`, `outreach-emails`, `content-strategy`, `seo-strategy`, `aeo-strategy`, `aeo-content`, `product-launch`, `website-copy`, `content-audit`) and `level` |
| [`agents/`](./agents/) | 5 agents — `product-marketer`, `content-marketer`, `gtm-engineer`, `aeo-specialist`, `context-refresh`. Ownership map in [`rules/orchestration.md`](./rules/orchestration.md) |
| [`hooks/`](./hooks/) | Two **active** Node hooks — `session-context.js` (injects working memory at session start) and `canonical-guard.js` (flags canonical-file writes). Wired in [`settings.json`](./settings.json); see [`hooks/README.md`](./hooks/README.md) |
| [`rules/`](./rules/) | Repo-level discipline: [`one-page-rule.md`](./rules/one-page-rule.md) (every CLAUDE.md stays one page) + [`quarterly-maintenance.md`](./rules/quarterly-maintenance.md) (90-day review ritual) + transcript discipline for `/win-loss-analysis` ([`pii-redaction.md`](./rules/pii-redaction.md), [`evidence-bound-outputs.md`](./rules/evidence-bound-outputs.md)) |
| [`connections.md`](./connections.md) | 12-connector setup guide — pairs with `.mcp.json` at the repo root (system of integrations) |
| `settings.local.json.example` | Claude Code per-machine settings template — copy to `settings.local.json` (gitignored) for machine-specific config |

## How `.claude/` relates to the 4 systems

| System | Where it lives |
|---|---|
| **1. Context** | `marketing/` — WeKan.AI data, seeded 2026-08-31 |
| **2. Action** | `.claude/skills/` |
| **3. Orchestration** | `.claude/agents/` + `.claude/hooks/` |
| **4. Integrations** | `.claude/connections.md` (the setup guide) + root-level `.mcp.json` + `env` (the wiring, root by tooling requirement) |

## Owner

Default: whoever owns the repo overall (named in the root [`README.md`](../README.md)).
