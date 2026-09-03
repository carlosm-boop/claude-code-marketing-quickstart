---
name: abm-campaign
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Design an account-based campaign for one named enterprise account - the belief shift required, the buying committee, the entry point, the multi-touch plan, and the assets each touch needs. Reads the scored account list, ICP, positioning and messaging. Triggers - "abm campaign", "account plan", "campaign for [account]", "how do we break into [company]", "account based marketing", "target account plan"
goal: Turn a single high-value account from a name on a list into a sequenced plan with a named belief shift and a defined buying committee.
outcome: marketing/outbound/strategy/MMYY-abm-{account-slug}.md with committee map, belief shift, touch plan, and asset checklist.
primitive: strategy
ontology_type: campaign-plan
review_gate: 2
inputs:
  required:
    - lead-scoring
  recommended:
    - icp-research
    - product-messaging
outputs:
  - type: campaign-plan
    feeds_into:
      - outreach-emails
      - website-copy
owned_by_agent: gtm-engineer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /abm-campaign
status: draft
---

# abm-campaign — outbound strategy skill

One account, one plan. Use on Tier 1 accounts from `/lead-scoring` where a generic sequence would waste the opportunity.

## When to use

- A Tier 1 account with a real trigger and a deal size that justifies bespoke effort
- Re-engaging an account that went dark after a first conversation
- A competitive displacement where a named incumbent has to be unseated

## When NOT to use

- For a cohort of similar accounts (use `/outreach-emails` with a segment angle instead)
- Before `/lead-scoring` has produced evidence that this account qualifies
- As a substitute for sales account planning — this is the marketing surface, not the deal strategy

## How it works

1. **Read** `marketing/outbound/research/MMYY-target-accounts.md` for the account's trigger evidence, plus ICP, positioning, messaging, and `company.md`.
2. **Research the account** via WebSearch / WebFetch (and HubSpot once wired): tech stack signals, recent announcements, leadership changes, engineering blog, job postings, earnings language on AI and modernization.
3. **Map the buying committee** — for WeKan deals typically: VP Engineering / Head of Platform (champion), CTO or CIO (economic buyer), Enterprise Architect (technical validator), Procurement/Vendor Management (blocker), and in BFSI/Healthcare a Risk or Compliance stakeholder.
4. **Write the belief shift** — the 3–5 things this specific account must come to believe to take the next step. Anything that doesn't move one of these gets cut from the plan.
5. **Choose the entry point** — which stakeholder, which trigger, which pillar from `messaging.md` §2.
6. **Sequence the touches** across channels with a stated purpose per touch.
7. **Write** to `marketing/outbound/strategy/MMYY-abm-{account-slug}.md`.

## Invoke

```
/abm-campaign {Account Name}
/abm-campaign {Account Name} — they just announced a Realm EOL migration
```

## Output shape

```
## Account snapshot — what's true, with sources
## Trigger — why now
## Buying committee — role · name if public · what they care about · likely objection
## Belief shift — the 3-5 beliefs, each with the proof that moves it
## Entry point — who first, on what
## Touch plan — sequence · channel · purpose · asset needed · owner
## Assets to produce — with the skill that produces each
## Disqualifiers — what would tell us to stop
```

## Dependencies

- **Reads:** `marketing/outbound/research/*-target-accounts.md`, `icp/ICP.md`, `positioning/positioning.md`, `messaging/messaging.md`, `company/company.md`
- **Writes:** `marketing/outbound/strategy/MMYY-abm-{account-slug}.md`

## Guardrails

- **Proof firewall applies.** No named-client-plus-metric pairing anywhere in the plan or its assets. See `marketing/brand/brand-voice.md` §0.
- Buying-committee names come from public sources only. No scraped personal contact data — see `.claude/rules/pii-redaction.md`.
- Every belief in the belief shift needs a proof point that exists in `messaging.md` §6. If one doesn't, mark it `[UNAVAILABLE]` and escalate rather than inventing support.

## Refresh cadence

Per-account. Revisit when the trigger changes or the committee turns over.
