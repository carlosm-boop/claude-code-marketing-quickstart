# history.md — long-term operations log

Append-only. Newest at top. Never edit a past entry; if one was wrong, append a correction.

**What goes here:** quarterly prunings, canonical refreshes, ownership transfers, MCP changes, first agent fires, system-wide changes.
**What does not:** routine skill runs (noise at this granularity) or recent-activity summaries (that's `latest.md`).

---

## 2026-09-03 — Layer 2 extended: retrieval and audit split out of scoring

Two skills added to `.claude/skills/`, both `status: draft`, both owned by `gtm-engineer`:

- **`origami-sourcing`** — composes and prices origami.chat retrieval prompts for one ICP and one trigger. Fifteen standing constraints, a seven-step template, an eleven-case failure catalogue, and the credit table. Pushing to origami.chat remains non-autonomous.
- **`sourcing-csv-audit`** — tool-agnostic audit of a sourced list before anything scores it. Five-way column classification, ten checks, an explicit unrepairable-column call.

**Why two and not one.** The originating spec described a single skill. The halves trigger on different inputs and have different scopes: prompt-writing is Origami-specific, list auditing is not.

**Structural consequence.** The outbound dependency chain gains two upstream stages: `icp-research → origami-sourcing → sourcing-csv-audit → lead-scoring → abm-campaign → outreach-emails`. `lead-scoring` no longer owns sourcing, and the audit is a gate rather than a recommendation. Ownership map in `.claude/rules/orchestration.md` updated accordingly.

Derived from the 8-pull, 400-credit ICP-M2 Origami trial (26 Aug – 3 Sep 2026): 120 companies screened, 32 qualified, and a measured capability map — 60 of 65 repeat companies contradicted themselves on a derived-judgment field while only 5 had any factual conflict.

Owner: Rudra

---

## 2026-08-31 — Decisions locked; stack corrected to reality

Rudra resolved all three open conflicts and corrected the integration picture.

- **Proof firewall confirmed as standing policy** — anonymization always; named customers added by hand by Rudra only.
- **Helix** adopted as the external product-engineering name; "Build Mode" retired.
- **Counts locked** at 100+ engineers / 40+ clients / 160+ projects.
- **Stack corrected.** Removed Exa, Granola, Gong, Notion, Linear, Ahrefs, Firecrawl, GA4 as assumptions. Real stack: origami.chat, Google Workspace, Slack, Google Meet now; TheirStack, HubSpot Smart CRM, SmartLead, HeyReach, Customer.io planned. None of the GTM tools have MCP connectors — n8n / Make webhook bridge is the path.
- **All 21 skills rewired** from Exa to built-in WebSearch / WebFetch. The research layer now needs zero wiring.
- **`/win-loss-analysis` unblocked** — Google Meet transcripts are reachable through the already-connected Google Drive connector.
- **Both hooks activated** in `.claude/settings.json`, written in Node for Windows compatibility. Canonical guard ships in warn mode.
- **Line endings normalized** and `.gitattributes` committed.

Owner: Rudra

---

## 2026-08-31 — Four-layer workspace setup

Repo forked from `matteotitta/claude-code-marketing-quickstart` and set up as the WeKan.AI marketing OS.

- **Layer 1 (Context):** `marketing/` seeded — added `company/`, `latest.md`, `history.md`, seeded `positioning.md`, `messaging.md`, `brand-kit.md`, `brand-voice.md`, draft `ICP.md`, `goals.md` template, `rules/escalation.md` + `rules/gate-rules.md`. Source: `wekan-client-deck` skill references, Q2 2026 baseline.
- **Layer 2 (Skills):** 10 skills added — `outreach-emails`, `abm-campaign`, `lead-scoring`, `content-strategy`, `seo-strategy`, `aeo-strategy`, `aeo-content`, `product-launch`, `website-copy`, `content-audit`. Eight of these fixed dangling slash-command references that already existed in the lane `CLAUDE.md` files.
- **Layer 3 (Orchestration):** 5 agents added — `product-marketer`, `content-marketer`, `gtm-engineer`, `aeo-specialist`, `context-refresh`. Plus `.claude/rules/orchestration.md`. Hooks documented but left disabled (Windows shell compatibility).
- **Layer 4 (Integrations):** `.mcp.json` and `env` remapped to the WeKan stack; `connections.md` extended with a WeKan section.

Lanes in scope: product-marketing, content, outbound, seo-aeo. `paid/` and `lifecycle/` left scaffolded, out of scope.

Owner: Rudra

---
