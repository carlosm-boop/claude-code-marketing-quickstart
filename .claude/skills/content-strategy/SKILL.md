---
name: content-strategy
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Build a content strategy and editorial calendar from positioning, ICP and goals - pillars, formats, cadence, distribution, and a dated calendar with the skill that produces each piece. Triggers - "content strategy", "editorial calendar", "content plan", "what should we publish", "content pillars", "blog plan", "content calendar"
goal: Decide what to publish and why, so every downstream content piece ladders to a pillar instead of being invented weekly.
outcome: marketing/content/strategy/MMYY-content-strategy.md with pillars, formats, cadence, calendar, and distribution plan.
primitive: strategy
ontology_type: content-plan
review_gate: 2
inputs:
  required:
    - positioning
    - product-messaging
  recommended:
    - icp-research
    - expert-pov
outputs:
  - type: content-plan
    feeds_into:
      - aeo-content
      - seo-strategy
owned_by_agent: content-marketer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /content-strategy
status: draft
---

# content-strategy — content strategy skill

Turns positioning into a publishing plan. Without this, content becomes weekly invention and the pillars never compound.

## When to use

- Standing up or resetting the content motion
- Quarterly planning
- After a positioning change that invalidates the current pillars

## When NOT to use

- To write an individual piece (that's `/aeo-content`)
- For keyword-level planning (that's `/seo-strategy`, which this feeds)

## How it works

1. **Read** `positioning/positioning.md` (the anchor and differentiators), `messaging/messaging.md` (the four value pillars), `icp/ICP.md` (pain priority, where they hang out), `goals/goals.md` (what we're measuring), `expert-pov/` if populated.
2. **Derive content pillars from the value pillars, not from keywords.** For WeKan the natural starting set:
   - *Operationalizing intelligence* — the worldview; the thought-leadership platform
   - *Modernization reality* — legacy estate truths, EOL pressure, migration risk (the Realm wedge lives here)
   - *Clarity before code* — why products fail at decision-making, not engineering
   - *Agentic systems in production* — MCP, orchestration, memory, governance, guardrails
   - *Building the AI-native firm* — WeKan running its own delivery on its own platforms
3. **Assign formats and cadence per pillar** against realistic capacity. Ask what capacity actually is before proposing a calendar — an unrealistic calendar is worse than none.
4. **Map distribution per piece.** A piece with no distribution plan is not scheduled.
5. **Build the dated calendar** naming the producing skill for each item.
6. **Write** to `marketing/content/strategy/MMYY-content-strategy.md`.

## Invoke

```
/content-strategy
/content-strategy for Q4, capacity is one long-form and three LinkedIn posts a week
```

## Output shape

```
## Pillars — pillar · the belief it moves · proof available · formats
## Cadence + capacity assumption (stated explicitly)
## Calendar — date · pillar · format · working title · producing skill · distribution
## Distribution map — per channel
## What we are deliberately not covering
## Measurement — which goal each pillar serves
```

## Guardrails

- Every pillar must trace to a value pillar in `messaging.md` §2 or it doesn't belong.
- Do not propose a cadence without asking about capacity first.
- Proof firewall applies to every planned piece that carries evidence.

## Dependencies

- **Reads:** `positioning/`, `messaging/`, `icp/`, `goals/`, `expert-pov/`
- **Writes:** `marketing/content/strategy/MMYY-content-strategy.md`

## Refresh cadence

Quarterly.
