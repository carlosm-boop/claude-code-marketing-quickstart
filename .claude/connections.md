# Connections — wire Claude to your data

12 connectors most marketers reach for, grouped by whether Claude **reads from**, **writes to**, or **both** with each one. Every entry covers what it's for, how to install across 3 paths, what credentials you need, and which skills in this repo use it.

This file pairs with [`.mcp.json`](../.mcp.json) at the repo root. `.mcp.json` is the machine-readable config Claude Code loads. When you wire a new connector, update both files.

---

## How to install ANY connector — 3 paths

Pick the path that matches your day-to-day interface:

- **Claude Code CLI:** `claude mcp add <name> [args]` from terminal — or hand-edit `.mcp.json` in this repo and restart your session.
- **Cursor IDE:** Settings → Features → MCP Servers → "+" → paste server config.
- **claude.ai (Pro/Team/Enterprise):** Settings → Connectors → search the connector name → "Connect" → OAuth flow opens in browser.

After connecting, restart your Claude session so the new tools surface.

---

## INPUT SOURCES — Claude reads from these

### 1. Exa — web search + page fetch (wired by default)

- **What:** Indexed web search built for AI — better than generic search for research queries. Also handles page fetch (clean markdown extraction).
- **Used by:** every research skill in this repo (`icp-research`, `competitor-research`, `competitor-aggregate`, `brand-kit`, `tov-guidelines`, `funnel-strategy`, `positioning`, `product-messaging`).
- **Install:** Already in `.mcp.json`. Add your free API key to `.env`:
  ```
  EXA_API_KEY=your-key-here
  ```
- **Get key:** [exa.ai](https://exa.ai). Free tier covers the quickstart.

### 2. Firecrawl — deep crawl + structured extraction

- **What:** Crawl entire sites, extract clean markdown, schedule monitoring.
- **Used by:** content audits, competitor site scraping, AEO citation discovery.
- **Install:** `claude mcp add firecrawl --env FIRECRAWL_API_KEY=$KEY` or claude.ai connectors → "Firecrawl".
- **Get key:** [firecrawl.dev](https://firecrawl.dev). Free tier available.

### 3. Ahrefs (paid) — SEO + brand-radar

- **What:** Keyword volume, ranking history, backlinks, brand-radar AEO visibility tracking.
- **Used by:** SEO-lane skills, content strategy keyword research, AEO citation gap analysis.
- **Install:** Add via `.mcp.json` with `AHREFS_TOKEN` from your dashboard.
- **Requires:** Paid Ahrefs plan with API access.

### 4. Google Search Console

- **What:** Real ranking + impression + click data for your domains.
- **Used by:** SEO audits, content gap analysis, AEO visibility tracking.
- **Install:** via Google Workspace plugin (OAuth) or claude.ai connectors → "Google Search Console".
- **Requires:** Google account with verified GSC property.

### 5. Granola — meeting notes

- **What:** Auto-transcribed meeting notes from Zoom / Meet / Teams.
- **Used by:** win-loss analysis, customer interviews, transcript-to-content cascades.
- **Install:** claude.ai connectors → "Granola" → OAuth, or `claude mcp add granola ...`.
- **Requires:** Granola account (free tier available).

### 6. Gong — sales call recordings + transcripts

- **What:** Recorded sales calls, AI-generated insights, deal-level signals.
- **Used by:** win-loss analysis, voice-of-customer extraction, sales enablement.
- **Install:** claude.ai connectors → "Gong" → OAuth (admin installation required).
- **Requires:** Gong seat + admin-installed integration.

---

## BIDIRECTIONAL — Claude reads AND writes

### 7. Google Drive

- **Read:** Briefs, transcripts, source docs, existing strategy files.
- **Write:** Branded Google Docs (proposals, briefs, deliverables), Sheets, Slides.
- **Install:** Google Workspace plugin (OAuth) or claude.ai connectors → "Google Drive".
- **Requires:** Google account.

### 8. Notion

- **Read:** Team docs, project boards, client-facing pages, knowledge bases.
- **Write:** Skill outputs as Notion pages (e.g., positioning → Notion strategy doc).
- **Install:** `claude mcp add notion ...` or claude.ai connectors → "Notion" → OAuth.
- **Requires:** Notion workspace + integration token (or OAuth).

### 9. Slack

- **Read:** Team comms, channel history, thread context.
- **Write:** Notifications, weekly digests, status updates, draft posts in channels.
- **Install:** claude.ai connectors → "Slack" → OAuth (app installation required).
- **Requires:** Slack workspace admin to install the Claude app.

### 10. Linear

- **Read:** Issues, projects, cycle state.
- **Write:** New issues, status changes, comments, blocked/awaiting-reply tagging.
- **Install:** claude.ai connectors → "Linear" → OAuth, or `claude mcp add linear ...`.
- **Requires:** Linear workspace + API key or OAuth.

---

## OUTPUT SINKS — Claude writes to these

### 11. Framer

- **What:** Push deploys to your Framer site after running landing-page copy skills.
- **Install:** No first-party MCP yet — wire via Framer's API token + webhook in `.mcp.json` or as a custom hook.
- **Requires:** Framer paid plan (API access).

### 12. Webflow

- **What:** Push CMS items + page updates to Webflow after content generation.
- **Install:** `claude mcp add webflow ...` (community MCP) or wire via Webflow API.
- **Requires:** Webflow site API token.

---

## Which to install first — sequencing

You don't need all 12 on day 1. Install in this order:

1. **Day 1:** Exa (required — already wired) + Firecrawl (free, unlocks competitor scraping).
2. **Week 1:** Google Drive + (Notion OR Slack depending on where your team works).
3. **Week 2:** Granola or Gong (whichever your team uses for meetings/calls).
4. **Week 3+:** GSC for SEO work; Ahrefs if you're investing in SEO/AEO; Framer or Webflow when you start shipping landing pages from this repo.

Linear is optional — install when you're orchestrating multi-step workflows where issues track skill output.

---

## Adding a new connector to this file

When you wire a new MCP that's not in the 12 above:

1. Decide its I/O role (input only / bidirectional / output only) and add it to that section.
2. Cover the 4 standard fields: what it's for, which skills use it, install instructions, credential requirements.
3. Update `.mcp.json` with the actual config.
4. Note it in your next maintenance review so the team knows it exists.


---

# WeKan.AI stack — the actual wiring (rev. 2026-08-31)

The 12-connector guide above is the generic version. This is **your** stack, checked against the connector registry. Nothing here is aspirational.

## The headline

**The research layer works today with zero wiring.** Claude Code has WebSearch and WebFetch built in, and every skill in this repo now uses them. No API key, no MCP, no signup is required to run `/competitor-research`, `/icp-research`, `/positioning`, `/content-audit`, or `/aeo-strategy` right now.

## Status

| Tool | Role | Status | How it's reached |
|---|---|---|---|
| **WebSearch / WebFetch** | pull — all web research | **Built in** | Nothing to wire |
| **Google Drive** | pull — docs **and Meet transcripts** | **Connected** | claude.ai connector, live |
| **Gmail** | pull / push — inbox | **Connected** | live |
| **Google Calendar** | pull — scheduling | **Connected** | live |
| **Slack** | push — notifications | **Connected** | live |
| **Google Meet** | pull — call transcripts | **Reachable via Drive** | Transcripts save to Drive automatically |
| **origami.chat** | pull — lead sourcing | In use · no MCP | Manual export → `outbound/research/` |
| **TheirStack** | pull — technographic signals | Planned · no MCP | REST API via n8n/Make |
| **HubSpot Smart CRM** | pull / push — CRM | Planned · no MCP | REST API via n8n/Make |
| **SmartLead** | push — email sequences | Planned · no MCP | REST API via n8n/Make, or paste |
| **HeyReach** | push — LinkedIn outreach | Planned · no MCP | REST API via n8n/Make |
| **Customer.io** | push — lifecycle | Planned · no MCP | REST API via n8n/Make |
| **Google Search Console** | pull — real SEO data | Not wired | Needed before `/seo-strategy` gives real volumes |
| **Exa** | pull — web research | Optional | Overlaps origami.chat; evaluate before paying |

**Retired from this repo's assumptions:** Granola, Gong, Notion, Linear, Ahrefs, Firecrawl. None are in the WeKan stack. Do not reference them in skills or agents.

## You do have transcripts

`/win-loss-analysis` was flagged as blocked on "no sales-call transcripts." That was wrong. **Google Meet writes recordings and transcripts to the organiser's Google Drive**, and the Drive connector is already live — so the transcripts are reachable today, with no new tooling.

The only real precondition is that **transcription was switched on** for those calls (Meet needs to be told; recording alone doesn't always produce a transcript). If it was off historically, turn it on now and the evidence base starts building from the next call.

This matters more than anything else in this file: win-loss is the single input that converts every asserted differentiator in `positioning.md` into evidence.

## Exa vs origami.chat

Right instinct to question it. They overlap but are not the same shape:

- **origami.chat** — GTM-native. Sources and enriches *accounts and people*. Its output is a list you act on.
- **Exa** — a neural *web index*. Its output is documents and pages, tuned for research retrieval rather than prospect lists.

For `/lead-scoring` and `/abm-campaign`, origami is the better fit and you already pay for it. For `/competitor-research` and `/aeo-strategy`, the built-in WebSearch and WebFetch cover it. **Recommendation: don't wire Exa.** Try the free tier if curious, but there is no gap in this repo that it uniquely fills.

## Per-skill I/O map

| Skill | Pulls from | Pushes to | Push path |
|---|---|---|---|
| `competitor-research` / `-aggregate` | WebSearch, WebFetch | `marketing/competitors/` | file |
| `icp-research` | WebSearch, wekancode.com, win-loss | `marketing/icp/ICP.md` | file |
| `win-loss-analysis` | **Google Drive (Meet transcripts)** | `marketing/win-loss/` | file |
| `positioning` / `product-messaging` | repo context | canonical files | file |
| `content-audit` | WebSearch, WebFetch, (GSC) | `content/research/` | file |
| `content-strategy` / `product-launch` | repo context | `content/strategy/` | file |
| `aeo-content` / `website-copy` | repo context | `content/execution/` | file → CMS, manual |
| `seo-strategy` | WebSearch, (GSC) | `seo-aeo/strategy/` | file |
| `aeo-strategy` | answer engines, WebSearch | `seo-aeo/research/` | file |
| `lead-scoring` | **origami.chat export**, (TheirStack) | `outbound/research/` | file |
| `abm-campaign` | WebSearch, (HubSpot) | `outbound/strategy/` | file |
| `outreach-emails` | repo context | `outbound/execution/` | file → **SmartLead / HeyReach, manual** |

## The n8n / Make bridge

Five of your planned systems — TheirStack, HubSpot, SmartLead, HeyReach, Customer.io — have no MCP. They all have REST APIs, and you already run n8n and Make. So the realistic wiring is:

```
Claude Code writes artifact → you review → n8n/Make webhook → SmartLead / HeyReach / HubSpot / Customer.io
```

The human review step is the point, not an inconvenience — it's exactly where `marketing/rules/escalation.md` puts the gate. Automating the review away is the failure mode.

**Build order when you get there:** SmartLead first (highest-volume manual step), then HubSpot (so campaign outcomes land back in the CRM), then HeyReach, then Customer.io. One webhook node per destination, manually triggered from a reviewed file. This is a stated novice area — treat it as a learning build, one destination at a time, not a weekend automation project.

**When Customer.io goes live**, `marketing/lifecycle/` becomes a real lane and needs its own skills. It is scaffolded and currently out of scope.

## Wiring priority

1. **Nothing.** Start running skills today — the research layer needs no wiring.
2. **Confirm Google Meet transcription is on.** Unlocks `/win-loss-analysis`, the highest-leverage missing input.
3. **Google Search Console** — only once SEO work actually starts. Until then `/seo-strategy` returns `[UNAVAILABLE]` for volumes and says so.
4. **The n8n bridge** — only when SmartLead or HeyReach go live.
5. **Exa** — only if a free-tier trial beats origami on something specific.

Do not wire connectors speculatively. An unused MCP is context cost with no return.

## Before adding any server to `.mcp.json`

```bash
npm view <package-name> version
```

If that errors, the package name is wrong — a bad entry makes Claude Code fail to start the server, usually quietly. Never paste a config you have not verified.
