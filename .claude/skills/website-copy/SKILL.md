---
name: website-copy
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Write or rewrite page copy for the website - homepage, product, solution, and landing pages - structured fold by fold with the belief each section moves and the proof it uses. Reads positioning, messaging, brand voice and ICP. Triggers - "website copy", "landing page", "homepage copy", "rewrite our site", "page copy", "hero copy", "product page"
goal: Produce page copy that leads with the point of view, lands the full arc, and never narrows WeKan to a fragment.
outcome: marketing/content/execution/MMYY-page-{slug}.md — fold-by-fold copy with rationale and proof mapping.
primitive: execution
ontology_type: page-copy
review_gate: 3
inputs:
  required:
    - positioning
    - product-messaging
  recommended:
    - icp-research
    - aeo-strategy
outputs:
  - type: page-copy
    feeds_into: []
owned_by_agent: product-marketer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /website-copy
status: draft
---

# website-copy — product-marketing execution skill

## When to use

- A page doesn't exist and the strategy calls for it
- An existing page misframes the positioning (a common AEO-audit finding)
- A campaign needs a dedicated landing page — the Realm EOL wedge is the obvious first one

## When NOT to use

- For an article or pillar page (that's `/aeo-content`)
- Before positioning is settled — rewriting copy against unstable positioning is wasted work

## How it works

1. **Read** `positioning/positioning.md`, `messaging/messaging.md`, `brand/brand-voice.md`, `brand/brand-kit.md`, `icp/ICP.md`, `company/company.md`.
2. **Define the page job:** one audience, one belief shift, one primary CTA. A page trying to do two jobs does neither — say so and propose splitting it.
3. **Propose the fold structure and confirm it before writing copy.** Structure first.
4. **Write fold by fold.** Default homepage-class structure:

   | Fold | Job |
   |---|---|
   | Hero | The insight, not the company. Headline carries the POV; subhead names who it's for. |
   | The gap | The three-vendor problem — the reader recognizes themselves. |
   | The arc | Legacy → modernize → build → operationalize. One partner. |
   | The engine | Evolve · Helix · NitroStack — the differentiator competitors can't copy. |
   | Proof | Anonymized outcomes. Separately, a names-only trust strip. **Never on the same fold as numbers.** |
   | Depth | BFSI and Healthcare practices. |
   | CTA | Consulting → implementation → enablement. One ask. |

5. **Map each fold to the belief it moves and the proof it uses.** Anything moving no belief gets cut.
6. **Add** page title, meta description, and heading hierarchy notes for AEO extraction.
7. **Write** to `marketing/content/execution/MMYY-page-{slug}.md`.

## Invoke

```
/website-copy homepage
/website-copy landing page for the Realm EOL campaign
```

## Guardrails

- **Proof firewall, and it is easiest to break here.** A logo strip and a stats band on the same fold reads as attribution even if the copy never says so. Keep them in different sections with different framing.
- **Escalate before publishing.** Always.
- Hero must never open with "WeKan is a global technology consulting company" (`brand-voice.md` rule 2) or with MongoDB (rule 4).
- Colors, type, and layout motifs come from `brand/brand-kit.md`. It is LOCKED.

## Dependencies

- **Reads:** `positioning/`, `messaging/`, `brand/`, `icp/`, `company/`
- **Writes:** `marketing/content/execution/MMYY-page-{slug}.md`
- **Pushes to (manual in v1):** the site CMS

## Refresh cadence

Per page. Re-audit all pages quarterly against `/aeo-strategy` findings.
