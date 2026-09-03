# WeKan.AI — escalation rules

*Seeded 2026-08-31 with conservative defaults. These bind every agent in [`../../.claude/agents/`](../../.claude/agents/). Loosen them deliberately as trust is earned — not by drift.*

---

## The default posture

**Nothing that carries the WeKan name to an outside human ships without Rudra seeing it.** Everything internal to the repo ships autonomously. That's the line while the system is new.

## Rules

| Action | Decision | Threshold that flips it | Route | Timeout fallback |
|---|---|---|---|---|
| Cold email sequence drafted | **Escalate** — always | — | Claude Code session | Hold |
| LinkedIn / social post drafted | **Escalate** — always | — | Claude Code session | Hold |
| Website or landing-page copy | **Escalate** — always | — | Claude Code session | Hold |
| Blog / AEO article drafted | **Escalate** — always | — | Claude Code session | Hold |
| Any asset containing a **client name** | **Escalate** — hard stop | No threshold. Never autonomous. | Rudra directly | Hold |
| Any asset containing a **metric not in `messaging.md` §6 or `company.md`** | **Escalate** — hard stop | No threshold. | Rudra directly | Hold |
| Research file written to `*/research/` | Autonomous | Escalate if it overwrites a locked canonical | — | — |
| Strategy doc written to `*/strategy/` | Autonomous | Escalate before anything downstream ships from it | — | — |
| Updating `latest.md` | Autonomous | — | — | — |
| Appending to `history.md` | Autonomous | — | — | — |
| Overwriting a **canonical** file (`ICP.md`, `positioning.md`, `messaging.md`, `company.md`, `brand-*.md`) | **Escalate** — always | — | Claude Code session | Hold |
| Creating or editing a skill, agent, or hook | **Escalate** — always | — | Claude Code session | Hold |
| Wiring a new MCP or editing `.mcp.json` | **Escalate** — always | — | Claude Code session | Hold |
| Spending external API credits | Autonomous | Escalate above ~200 Exa queries in one run | Claude Code session | Hold |
| Pushing to any external system (HubSpot, SmartLead, HeyReach, Customer.io, origami.chat) | **Escalate** — always in v1 | Revisit after 30 days of clean runs | Claude Code session | Hold |

## The two failure modes these prevent

**Over-escalation** wastes review attention on routine work until escalations become noise and stop being read. **Under-escalation** ships something wrong under the WeKan name. The table above deliberately errs toward over-escalation on anything external and toward autonomy on anything internal, because internal mistakes are cheap and reversible in git.

## Rudra-specific note

Given a strong preference for async and a low tolerance for busywork: escalations should arrive **batched**, not one at a time. An agent that produces five drafts surfaces all five in one review pass with a single summary, not five interruptions.

## Refresh cadence

Quarterly. Move a rule from escalate → autonomous only after 30 days of clean output in that category. Log every change in `../history.md`.

## Owner

Rudra.
