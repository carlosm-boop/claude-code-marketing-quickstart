---
name: aeo-strategy
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Analyze how WeKan is represented in AI answer engines (ChatGPT, Claude, Perplexity, Google AI Overviews) and build a plan to close the citation gap. Runs the real prompts a buyer would ask, records what gets cited, and identifies which sources need to change. Triggers - "aeo strategy", "aeo audit", "ai engine optimization", "do we show up in chatgpt", "citation gap", "answer engine optimization", "llm visibility"
goal: Find out what AI answer engines actually say about WeKan and its category, and fix the sources they draw from.
outcome: marketing/seo-aeo/research/MMYY-aeo-audit.md plus a citation-gap plan in strategy/.
primitive: research
ontology_type: aeo-audit
review_gate: 1
inputs:
  required:
    - positioning
  recommended:
    - competitor-aggregate
    - seo-strategy
outputs:
  - type: aeo-audit
    feeds_into:
      - aeo-content
      - seo-strategy
owned_by_agent: aeo-specialist
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /aeo-strategy
status: draft
---

# aeo-strategy — seo-aeo research skill

Search is no longer the only front door. This skill measures the other one.

## When to use

- Establishing an AEO baseline (nothing measured yet)
- Quarterly visibility check
- After a positioning change — answer engines lag, and stale framing persists in them longer than on your own site
- When a prospect says "I asked ChatGPT about modernization partners and you weren't there"

## When NOT to use

- For classic SERP ranking work (that's `/seo-strategy`)
- To write the corrective content (that's `/aeo-content`)

## How it works

1. **Build the prompt set** — 15–25 questions a real buyer would ask, spanning:
   - Category: "who are the best enterprise legacy modernization partners"
   - Problem: "how do I migrate off Realm before end of life"
   - Comparison: "WeKan vs {competitor}"
   - Branded: "what does WeKan do", "is WeKan MongoDB only"
   - Adjacent: "how do enterprises operationalize AI on legacy systems"
2. **Run each prompt** and record verbatim: is WeKan mentioned, in what position, with what framing, and **which sources are cited**.
3. **Diagnose the gap.** Answer engines cite what is structured, specific, and corroborated across sources. Classify each miss:
   - *Absence* — no source exists making the claim
   - *Weak source* — the claim exists only on wekancode.com, uncorroborated
   - *Misframing* — WeKan appears but as "a MongoDB partner" or "a database migration shop" (the exact narrowing `brand-voice.md` rule 4 forbids)
   - *Competitor capture* — a competitor owns the answer
4. **Plan the fix** — which pages need to exist, which need restructuring into direct question-answer form, which third-party sources need to carry the claim.
5. **Write** the audit to `marketing/seo-aeo/research/MMYY-aeo-audit.md` and the plan to `marketing/seo-aeo/strategy/MMYY-aeo-plan.md`.

## Invoke

```
/aeo-strategy
/aeo-strategy focus on Realm EOL and modernization-partner queries
```

## Guardrails

- **Record verbatim.** Paraphrasing what an engine said destroys the baseline's value for the next run.
- Note the date and engine version — results shift, and an undated audit can't show movement.
- No invented citation-share percentages. If it wasn't counted, it's `[UNAVAILABLE]`.

## Dependencies

- **Reads:** `positioning/`, `messaging/`, `company/`, `competitors/`
- **Writes:** `marketing/seo-aeo/research/MMYY-aeo-audit.md`, `marketing/seo-aeo/strategy/MMYY-aeo-plan.md`

## Refresh cadence

Quarterly, with the same prompt set each time so results are comparable.
