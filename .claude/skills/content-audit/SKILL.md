---
name: content-audit
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Audit existing published content against positioning, pillars and buyer questions - what exists, what performs, what misframes WeKan, and what is missing. Produces a prioritized keep/rewrite/kill/create list. Triggers - "content audit", "audit our content", "what content do we have", "content inventory", "content gaps", "which pages should we fix"
goal: Establish what content actually exists and how it performs before planning more of it, so strategy starts from reality rather than a blank page.
outcome: marketing/content/research/MMYY-content-audit.md with an inventory, a verdict per asset, and a prioritized gap list.
primitive: research
ontology_type: content-inventory
review_gate: 1
inputs:
  required:
    - positioning
  recommended:
    - product-messaging
    - aeo-strategy
outputs:
  - type: content-inventory
    feeds_into:
      - content-strategy
      - seo-strategy
owned_by_agent: content-marketer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /content-audit
status: draft
---

# content-audit — content research skill

The research stage of the content lane. `/content-strategy` plans; this establishes what is already true. Run it first.

## When to use

- Before any content strategy work — planning without an inventory is planning in the dark
- After a positioning change, to find every asset that now misframes WeKan
- Quarterly, as input to the maintenance ritual

## When NOT to use

- To plan future content (that's `/content-strategy` — this feeds it)
- To audit AI-answer visibility (that's `/aeo-strategy` — different mechanics)

## How it works

1. **Read** `positioning/positioning.md`, `messaging/messaging.md` (the four pillars), `brand/brand-voice.md`, `goals/goals.md`.
2. **Inventory** every published asset via WebSearch / WebFetch: site pages, blog posts, resources, and any founder-led content worth counting. Record URL, title, format, publish date, and target audience.
3. **Judge each asset on four axes:**

   | Axis | Question |
   |---|---|
   | **Pillar fit** | Does it ladder to a value pillar in `messaging.md` §2, or is it orphaned? |
   | **Framing** | Does it hold the full arc, or narrow WeKan to a fragment (database shop, MongoDB partner, migration vendor)? |
   | **Evidence** | Are its claims sourced? **Does it violate the proof firewall by pairing a client name with a metric?** |
   | **Structure** | Is it extractable — direct answer up front, claims that survive being quoted alone? |

4. **Assign one verdict per asset:** KEEP · REWRITE · KILL · MERGE. Every verdict states the reason and, for rewrites, the specific fix.
5. **Find the gaps** — buyer questions from `icp/ICP.md` and the AEO audit with no asset answering them. Rank by intent, not volume.
6. **Write** to `marketing/content/research/MMYY-content-audit.md`.

## Invoke

```
/content-audit https://wekancode.com
/content-audit just the blog
```

## Output shape

```
## Inventory — URL · title · format · date · pillar · verdict
## FIREWALL VIOLATIONS — assets pairing a client name with a metric (fix first, always)
## Misframing — assets that narrow the positioning
## Orphans — assets laddering to no pillar
## Gaps — buyer questions with no asset, ranked by intent
## Prioritized action list — quick wins vs structural
```

## Guardrails

- **Firewall violations are the top of the report, above everything else.** A published asset pairing a name with a metric is live exposure, not a content-quality issue. Escalate immediately rather than filing it in a list.
- No invented traffic or engagement numbers. Without GSC or site analytics wired, performance is `[UNAVAILABLE]` — say so and note what would produce it.
- KILL verdicts always escalate. Unpublishing has SEO consequences a content audit can't fully price.

## Dependencies

- **Reads:** `positioning/`, `messaging/`, `brand/`, `icp/`, `goals/`, `seo-aeo/research/`
- **Reads via:** WebSearch / WebFetch; GSC when wired
- **Writes:** `marketing/content/research/MMYY-content-audit.md`

## Refresh cadence

Quarterly, or immediately after a positioning change.
