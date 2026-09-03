# marketing/ — WeKan.AI marketing OS

The System of Context for WeKan.AI. Everything downstream — skills, agents, integrations — reads from here. Change a canonical file and every output reflects it on the next run.

**Owner:** Rudra (carlosm@wekancode.com)
**Seeded:** 2026-08-31 from the `wekan-client-deck` skill references (Q2 2026 baseline).

## Read first

1. [`company/company.md`](./company/company.md) — who WeKan is, the arc, the three engines, the numbers
2. [`positioning/positioning.md`](./positioning/positioning.md) — the category, the five differentiators
3. [`messaging/messaging.md`](./messaging/messaging.md) — taglines, pillars, boilerplate, words to use/avoid
4. [`brand/brand-voice.md`](./brand/brand-voice.md) — voice rules + the proof firewall
5. [`latest.md`](./latest.md) — what changed recently · [`history.md`](./history.md) — the ops log

## Canonical status

| Folder | File | State |
|---|---|---|
| [`company/`](./company/) | `company.md` | Seeded — verify the to-verify tracker |
| [`positioning/`](./positioning/) | `positioning.md` | Seeded — needs a competitor pass |
| [`messaging/`](./messaging/) | `messaging.md` | Seeded — proof points rewritten to the firewall |
| [`brand/`](./brand/) | `brand-kit.md`, `brand-voice.md` | Seeded from the deck design system |
| [`icp/`](./icp/) | `ICP.md` | Draft skeleton — run `/icp-research` |
| [`competitors/`](./competitors/) | — | Empty — run `/competitor-research` |
| [`funnel/`](./funnel/) | — | Empty — run `/funnel-strategy` |
| [`win-loss/`](./win-loss/) | — | Empty — run `/win-loss-analysis` on Google Meet transcripts in Drive |
| [`expert-pov/`](./expert-pov/) | — | Empty — run `/expert-pov` on the CEO tech-vision memo |
| [`goals/`](./goals/) | `goals.md` | Template — hand-author |
| [`rules/`](./rules/) | `escalation.md`, `gate-rules.md` | Seeded with WeKan defaults |

## Active execution lanes

`product-marketing` (the PMM spine above) · [`content/`](./content/) · [`outbound/`](./outbound/) · [`seo-aeo/`](./seo-aeo/)

Each follows **research → strategy → execution**. [`paid/`](./paid/) and [`lifecycle/`](./lifecycle/) are scaffolded but out of scope for now.

## Non-negotiable

The **proof firewall** in [`brand/brand-voice.md`](./brand/brand-voice.md): client names and performance metrics never appear together, in any asset, ever. This binds every skill and agent in this repo.

## Next three moves

1. `/competitor-research` × 3 → `/competitor-aggregate`
2. `/icp-research` against wekancode.com
3. `/win-loss-analysis` on Meet transcripts — the one input that turns asserted differentiators into evidence
