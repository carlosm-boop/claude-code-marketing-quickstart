---
name: seo-strategy
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Build an SEO strategy for the site - keyword clusters mapped to content pillars and funnel stage, competitor gap analysis, technical checks, and a prioritized action plan split into quick wins and structural work. Triggers - "seo strategy", "keyword research", "seo audit", "keyword clusters", "how do we rank", "organic strategy", "content gaps"
goal: Decide which search demand WeKan can realistically own and in what order, so content effort compounds instead of scattering.
outcome: marketing/seo-aeo/strategy/MMYY-seo-strategy.md with clusters, gaps, technical findings, and a prioritized plan.
primitive: strategy
ontology_type: seo-plan
review_gate: 2
inputs:
  required:
    - positioning
  recommended:
    - content-strategy
    - competitor-aggregate
outputs:
  - type: seo-plan
    feeds_into:
      - aeo-content
      - content-strategy
owned_by_agent: aeo-specialist
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /seo-strategy
status: draft
---

# seo-strategy — seo-aeo strategy skill

## When to use

- No documented keyword strategy exists, or the existing one predates the current positioning
- Quarterly review of organic performance
- Before committing a quarter of content capacity

## When NOT to use

- For AI-engine visibility (that's `/aeo-strategy` — different retrieval mechanics, different work)
- To write a piece (that's `/aeo-content`)

## How it works

1. **Read** `positioning/positioning.md`, `messaging/messaging.md`, `content/strategy/*` if present, `competitors/aggregate.md` if locked, `goals/goals.md` for the baseline.
2. **Build keyword clusters around the pillars**, not around volume. Starting clusters for WeKan:
   - *Legacy modernization* — Oracle to MongoDB migration, stored-procedure modernization, monolith decomposition
   - *EOL migration* — **Realm EOL migration** (the live wedge, deadline-driven, low competition, high intent)
   - *Agentic systems* — MCP server development, agent orchestration, agent governance
   - *AI-native engineering* — AI product engineering, blueprint-first development
   - *Comparison and evaluation* — modernization partner selection, SI evaluation criteria
3. **Score each cluster** on intent match to ICP, realistic difficulty, existing WeKan authority, and proof availability. A cluster WeKan cannot support with real evidence does not get prioritized.
4. **Gap analysis** via WebSearch / WebFetch against competitor content — what they rank for that WeKan has no answer to, and where nobody has a credible answer.
5. **Technical pass** — indexation, titles and metas, internal linking, schema, Core Web Vitals, canonical handling.
6. **Prioritize** into quick wins (under 2 weeks) and structural work (a quarter), each with expected impact and effort.
7. **Write** to `marketing/seo-aeo/strategy/MMYY-seo-strategy.md`.

## Invoke

```
/seo-strategy https://wekancode.com
/seo-strategy focus on the Realm EOL cluster
```

## Guardrails

- Volume estimates are `[UNAVAILABLE]` unless a real data source (GSC) is wired. **Do not invent search volumes** — flag them and say what would produce them.
- Every recommended page must trace to a pillar in `content/strategy/`.
- Proof firewall applies to any page carrying evidence.

## Dependencies

- **Reads:** `positioning/`, `messaging/`, `content/strategy/`, `competitors/`, `goals/`
- **Reads via:** WebSearch / WebFetch (competitor content, SERP reality); GSC when wired
- **Writes:** `marketing/seo-aeo/strategy/MMYY-seo-strategy.md`

## Refresh cadence

Quarterly, or after a major algorithm shift.
