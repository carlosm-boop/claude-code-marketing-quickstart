---
name: product-launch
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Build a go-to-market launch plan for a product, platform capability, or practice - positioning for the thing being launched, audience and belief shift, tiered launch scope, channel plan, asset checklist, and success metrics. Triggers - "launch plan", "product launch", "gtm plan for", "we are launching", "launch brief", "go to market plan"
goal: Turn a product or capability release into a sequenced launch with a defined tier, owned assets, and metrics agreed before anything ships.
outcome: marketing/content/strategy/MMYY-launch-{product-slug}.md with tier, narrative, channel plan, asset checklist, and metrics.
primitive: strategy
ontology_type: launch-plan
review_gate: 2
inputs:
  required:
    - positioning
    - product-messaging
  recommended:
    - icp-research
    - content-strategy
outputs:
  - type: launch-plan
    feeds_into:
      - website-copy
      - aeo-content
      - outreach-emails
owned_by_agent: product-marketer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /product-launch
status: draft
---

# product-launch — product-marketing strategy skill

For WeKan this covers platform releases (NitroStack components, Evolve capabilities, Helix), new practice launches (Manufacturing), and campaign wedges (Realm EOL).

## When to use

- A platform capability is shipping and needs a market motion
- A new practice or vertical is being stood up
- A wedge campaign needs a coordinated multi-channel push

## When NOT to use

- For a single asset (go straight to the producing skill)
- Before the thing being launched has a settled name — see the Helix / Build Mode conflict in `company.md`

## How it works

1. **Read** `positioning/positioning.md`, `messaging/messaging.md`, `icp/ICP.md`, `company/company.md`, `goals/goals.md`.
2. **Pick the launch tier and say why.** Scope follows tier; tier does not follow enthusiasm.

   | Tier | When | Scope |
   |---|---|---|
   | **T1 — category moment** | Changes what WeKan is understood to be | Full narrative, site changes, founder POV, outbound, PR, analyst |
   | **T2 — capability launch** | New platform capability with real buyer impact | Page, article, LinkedIn, outbound angle, sales enablement |
   | **T3 — increment** | Improvement worth telling existing buyers about | Changelog, one post, sales note |

3. **Write the launch narrative** — it must ladder to a value pillar in `messaging.md` §2, not stand alone. A launch that doesn't reinforce the arc weakens it.
4. **Name the belief shift** — 3–5 things the audience must believe. Every asset moves one or gets cut.
5. **Build the channel plan and asset checklist**, naming the producing skill and owner for each item.
6. **Define success metrics before launch**, tied to `goals/goals.md`. Metrics agreed after the fact are not metrics.
7. **Write** to `marketing/content/strategy/MMYY-launch-{product-slug}.md`.

## Invoke

```
/product-launch NitroCloud
/product-launch the Realm EOL wedge campaign, T2
```

## Guardrails

- Product names come from `company.md`, which is authoritative. Do not use a name from an older doc.
- Proof firewall applies to every launch asset.
- Do not position the launched thing as standalone — it is a stage of the arc.
- Escalate the plan before any asset production begins.

## Dependencies

- **Reads:** `positioning/`, `messaging/`, `icp/`, `company/`, `goals/`
- **Writes:** `marketing/content/strategy/MMYY-launch-{product-slug}.md`

## Refresh cadence

Per launch. Post-mortem into `history.md` within two weeks of launch.
