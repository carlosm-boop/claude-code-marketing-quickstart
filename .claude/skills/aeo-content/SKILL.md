---
name: aeo-content
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Write a long-form article structured to be cited by AI answer engines and to rank in search - direct question-answer structure, extractable claims, schema, and internal links. Reads content strategy, AEO audit, messaging and brand voice. Triggers - "write an article", "blog post", "aeo content", "long form content", "write a piece on", "draft an article", "pillar page"
goal: Produce a single publishable article that answers a real buyer question in a form both search and answer engines can extract.
outcome: marketing/content/execution/MMYY-{slug}.md — full draft with metadata, schema notes, and internal links.
primitive: execution
ontology_type: article
review_gate: 3
inputs:
  required:
    - product-messaging
  recommended:
    - content-strategy
    - aeo-strategy
    - seo-strategy
outputs:
  - type: article
    feeds_into: []
owned_by_agent: content-marketer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /aeo-content
status: draft
---

# aeo-content — content execution skill

Writes the piece. Structured so an answer engine can lift a clean, correct claim out of it.

## When to use

- An item on the calendar in `content/strategy/` is due
- The AEO audit found an *absence* gap that needs a source to exist
- An existing page needs restructuring into extractable form

## When NOT to use

- Without an angle from `content/strategy/` or `seo-aeo/strategy/` — writing without a plan is what the strategy layer exists to prevent
- For LinkedIn or social copy (different discipline; ask explicitly)
- For website page copy (that's `/website-copy`)

## How it works

1. **Read** `content/strategy/*` (which pillar, which belief), `seo-aeo/strategy/*` (cluster and target question), `messaging/messaging.md`, `brand/brand-voice.md`, `company/company.md`.
2. **State the target question and the belief the piece moves. Confirm before drafting.** Per Rudra's structure-first preference: propose the outline and get agreement before writing prose. Never open with a finished draft.
3. **Structure for extraction:**
   - H1 is the question, in the words a buyer would use
   - A direct 40–60 word answer in the first paragraph, before any context
   - One H2 per sub-question, each independently extractable
   - Claims stated as complete sentences that survive being quoted alone
   - A comparison table where the question is comparative
   - A short FAQ block for adjacent phrasings
4. **Write the draft** in brand voice — CTO reader, insight first, specific over sweeping, no hype, no emoji.
5. **Add metadata:** title under 60 characters, meta description under 155, slug, suggested schema type (Article / FAQPage / HowTo), and 3–5 internal links to existing pages.
6. **Write** to `marketing/content/execution/MMYY-{slug}.md`.

## Invoke

```
/aeo-content "how do I migrate off Realm before end of life"
/aeo-content next item from the Q4 calendar
```

## Guardrails

- **Escalate before publishing.** Per `marketing/rules/escalation.md`, no article ships without review.
- **Proof firewall.** Anonymized Pool B outcomes only. Never a client name beside a metric.
- **Evidence-bound.** Every figure comes from `messaging.md` §6 or `company.md`, or is `[UNAVAILABLE]`. External claims get a real citation.
- Never narrow the positioning to a fragment without landing the arc before the CTA (`brand-voice.md` rule 4).
- Outline first, prose second. Always.

## Dependencies

- **Reads:** `content/strategy/`, `seo-aeo/strategy/`, `messaging/`, `brand/`, `company/`
- **Writes:** `marketing/content/execution/MMYY-{slug}.md`

## Refresh cadence

Per piece. Revisit published pieces quarterly against the AEO audit.
