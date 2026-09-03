---
name: outreach-emails
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Write a cold email sequence for a target segment or named account - full copy for every step, with timing, branching, exit conditions, and the trigger-specific angle. Reads ICP, positioning, messaging, brand voice, and the scored account list. Triggers - "cold email", "outbound sequence", "outreach emails", "write a sequence", "smartlead sequence", "email cadence", "prospecting emails"
goal: Produce ready-to-load outbound sequences that lead with a trigger and a point of view rather than a company introduction.
outcome: marketing/outbound/execution/MMYY-sequence-{segment-slug}.md with full copy per step, timing, and exit conditions.
primitive: execution
ontology_type: email-sequence
review_gate: 3
inputs:
  required:
    - product-messaging
  recommended:
    - lead-scoring
    - abm-campaign
    - icp-research
outputs:
  - type: email-sequence
    feeds_into: []
owned_by_agent: gtm-engineer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /outreach-emails
status: draft
---

# outreach-emails — outbound execution skill

Writes the actual sequence. Every step is full copy, not a brief.

## When to use

- A segment or cohort from `/lead-scoring` is ready to work
- A named account plan from `/abm-campaign` needs its email touches written
- An existing sequence is underperforming and needs a rewrite against a sharper trigger

## When NOT to use

- Before the segment's trigger is known — a sequence with no trigger is a company introduction, and those don't get replies
- For lifecycle or nurture email to existing contacts (that's the `lifecycle/` lane)
- For LinkedIn message copy (different medium, different length discipline — ask for it explicitly)

## How it works

1. **Read** `messaging/messaging.md` (pillars, audience framing, words to use/avoid), `brand/brand-voice.md` (all six rules plus the firewall), `icp/ICP.md` (pain priority order), and the relevant `outbound/research/` or `outbound/strategy/` file for the trigger.
2. **Confirm the angle before writing.** State the segment, the trigger, the pain being led with, and the single belief the sequence is trying to shift. Get agreement, then write.
3. **Write the sequence.** Default shape — 5 steps over 18 days:

   | Step | Day | Job |
   |---|---|---|
   | 1 | 0 | The trigger + the insight. No pitch. Ends on a question, not a meeting ask. |
   | 2 | 3 | The specific mechanism — what actually makes it work (agents, blueprint-first, MCP). |
   | 3 | 8 | Anonymized proof from the same industry. Firewall applies. |
   | 4 | 13 | Reframe — the arc, not the fragment. Names the "three vendors" problem. |
   | 5 | 18 | Short break-up. One line, one easy out. |

4. **Constraints per email:** under 120 words, one idea, one ask, no more than one link, plain text, no emoji, subject lines under 45 characters. Sentence-case subjects.
5. **Define exits:** reply, meeting booked, out-of-office, unsubscribe, anti-ICP signal discovered mid-sequence.
6. **Write** to `marketing/outbound/execution/MMYY-sequence-{segment-slug}.md`, with three subject-line variants per step for A/B testing.

## Invoke

```
/outreach-emails BFSI segment, Realm EOL trigger
/outreach-emails for the {Account} ABM plan
```

## Guardrails

- **Escalate before sending. Always.** Per `marketing/rules/escalation.md`, no cold email ships without Rudra reviewing it.
- **Proof firewall.** Step 3 uses Pool B anonymized outcomes only. Never a client name beside a number.
- Never open with "WeKan is a global technology consulting company" — that violates `brand-voice.md` rule 2. Lead with the insight.
- Never open with MongoDB — it narrows the positioning (rule 4, and `messaging.md` §7).
- No invented personalization. If the research doesn't support a specific claim about the account, write the segment-level line instead.

## Dependencies

- **Reads:** `messaging/messaging.md`, `brand/brand-voice.md`, `icp/ICP.md`, `outbound/research/*`, `outbound/strategy/*`
- **Writes:** `marketing/outbound/execution/MMYY-sequence-{segment-slug}.md`
- **Pushes to (manual in v1):** SmartLead

## Refresh cadence

Rewrite when reply rate drops below the baseline in `goals/goals.md`, or when the trigger goes stale.
