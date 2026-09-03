# Rule — orchestration: which agent owns what, and what may fire unattended

*Added 2026-08-31. This is the System of Orchestration's rulebook. Agents live in [`../agents/`](../agents/); the escalation table they obey lives in [`../../marketing/rules/escalation.md`](../../marketing/rules/escalation.md).*

---

## Ownership map — one owner per lane, no overlaps

| Agent | Owns | Skills it manages |
|---|---|---|
| [`product-marketer`](../agents/product-marketer.md) | The PMM spine: positioning, messaging, competitors, launches, page copy | `positioning`, `product-messaging`, `competitor-research`, `competitor-aggregate`, `product-launch`, `website-copy`, `win-loss-analysis` |
| [`content-marketer`](../agents/content-marketer.md) | Content strategy and production | `content-audit`, `content-strategy`, `aeo-content`, `expert-pov`, `tov-guidelines` |
| [`gtm-engineer`](../agents/gtm-engineer.md) | Outbound and its automation | `origami-sourcing`, `sourcing-csv-audit`, `lead-scoring`, `abm-campaign`, `outreach-emails`, `icp-research` |
| [`aeo-specialist`](../agents/aeo-specialist.md) | Search + answer-engine visibility | `seo-strategy`, `aeo-strategy`, `aeo-content` |
| [`context-refresh`](../agents/context-refresh.md) | The maintenance loop | `level` — reports only, ships nothing |

`aeo-content` is shared between `content-marketer` and `aeo-specialist`. That is deliberate: the AEO specialist commissions it from an audit finding, the content marketer writes it from the calendar. Whoever invokes it owns that run.

## The dependency order — enforced, not suggested

```
competitor-research ──┐
                      ├─→ icp-research ──→ positioning ──→ product-messaging ──┬─→ content-strategy ──→ aeo-content
win-loss-analysis ────┘                                                        ├─→ lead-scoring ──→ abm-campaign ──→ outreach-emails
                                                                               ├─→ seo-strategy ──→ aeo-content
                                                                               ├─→ aeo-strategy ──→ aeo-content
                                                                               └─→ product-launch ──→ website-copy
```

**Sourcing sits upstream of scoring.** `icp-research` → `origami-sourcing` → `sourcing-csv-audit` → `lead-scoring`. No account list reaches `lead-scoring` without passing the audit — the audit is the gate, not a suggestion. Pushing to origami.chat stays non-autonomous: `origami-sourcing` composes and estimates, a human approves, then it runs.

**No skill runs against an upstream file still marked DRAFT.** `marketing/icp/ICP.md` is a draft skeleton today. Any agent consuming it must say so in its output rather than presenting inference as research.

## The refresh loop — what makes this compound

Research → strategy → execution → **refresh**. The fourth stage is what turns a folder structure into a system:

1. `context-refresh` scans weekly and writes findings to `marketing/latest.md`
2. Findings name the specific file and the specific skill that resolves each
3. The owning agent runs that skill **under review**
4. Refreshed canonical files change every downstream output on its next run
5. Structural events append to `marketing/history.md`

Skip stage 4 and the system doesn't compound — it just accumulates files.

## What may fire unattended

**Autonomous:** reading anything · writing to `*/research/` and `*/strategy/` · updating `latest.md` · appending to `history.md` · `context-refresh` in full.

**Never autonomous:** anything external-facing (email, social, web, articles) · overwriting a canonical file · anything containing a client name or an unsourced metric · creating or editing skills, agents, hooks, or `.mcp.json` · pushing to HubSpot, SmartLead, HeyReach, Customer.io, or origami.chat.

The full table is in [`../../marketing/rules/escalation.md`](../../marketing/rules/escalation.md) and it is the authority. This section is a summary, not a second source of truth.

## Escalation ergonomics

Batch. An agent producing five drafts surfaces all five in one review pass with a single summary — never five separate interruptions.

## Owner

Rudra. Review quarterly alongside `quarterly-maintenance.md`.
