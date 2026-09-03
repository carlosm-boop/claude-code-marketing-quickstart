---
name: lead-scoring
version: '1.0'
last_updated: 2026-08-31
author: wekan
description: Build a scored, prioritized target-account list from firmographic and technographic signals. Reads the ICP and positioning, defines weighted scoring criteria, sources accounts via origami.chat and web research, and writes a ranked list with the trigger evidence behind each score. Triggers - "lead scoring", "target account list", "account prioritization", "who should we go after", "build a prospect list", "score my accounts"
goal: Turn the ICP into a ranked account list so outbound spends effort on accounts that actually match, with the evidence for each score visible.
outcome: marketing/outbound/research/MMYY-target-accounts.md with a weighted scoring model and a ranked account table.
primitive: research
ontology_type: account-list
review_gate: 1
inputs:
  required:
    - icp-research
  recommended:
    - competitor-research
    - positioning
outputs:
  - type: account-list
    feeds_into:
      - abm-campaign
      - outreach-emails
owned_by_agent: gtm-engineer
mcps_used:
  - websearch
  - webfetch
optional_mcps:
  - exa
triggers:
  slash_commands:
    - /lead-scoring
status: draft
---

# lead-scoring — outbound research skill

Converts `marketing/icp/ICP.md` into a weighted scoring model and a ranked account list. Every downstream outbound skill reads the output rather than re-deciding who to target.

## When to use

- Standing up a new outbound motion, before writing any sequence
- Quarterly refresh of the target list
- Entering a new segment or geography
- After a positioning or ICP change that shifts who qualifies

## When NOT to use

- Before `/icp-research` has run — scoring against a draft ICP produces confident nonsense
- For scoring inbound leads already in HubSpot (that's a CRM workflow, not this skill)
- For per-account research depth (use `/abm-campaign` on the top N)

## How it works

1. **Read** `marketing/icp/ICP.md` (firmographics, anti-ICP), `marketing/positioning/positioning.md` (what we displace), `marketing/company/company.md` (current wedges).
2. **Propose a weighted model** and confirm the weights with the user before scoring. **Pick the model that matches the ICP being scored** — WeKan has two live:

### Model A — ICP-M1, The Legacy Estate Owner

| Signal | Weight | Why |
|---|---|---|
| Legacy estate evidence (Oracle / MSSQL / C++ / stored-procedure logic) | 25 | The core qualifier |
| End-of-life pressure (Realm EOL, unsupported versions, licensing renewal) | 25 | The live wedge; adds a deadline |
| MongoDB ecosystem presence | 15 | Warm path via the partnership |
| Regulated / workflow-intensive vertical (BFSI, Healthcare) | 15 | Where the moat is real |
| Public AI mandate with no visible foundation work | 10 | The gap WeKan names |
| Scale (enterprise / upper mid-market) | 10 | Deal-size floor |
| **Anti-ICP hit** (staff-aug intent, pure greenfield, migration-only scope) | **−40** | Disqualifier, not a penalty |


### Model B — ICP-M2, The Scaled Digital Platform

Model A above is M1-shaped (legacy estate, EOL pressure). M2 scores differently: the qualifier is a founding-era core under margin pressure, not a 25-year relational estate. Derived and validated 2026-09-02 against 119 companies across six Origami sourcing runs; the two heaviest signals are the two that predicted a meeting.

| Signal | Weight | Why |
|---|---|---|
| **Named estate or database pain** (multi-engine estate, founding-era monolith, migration named in a job posting) | **25** | The core qualifier, and the only one that ever came from the target's own words |
| **Margin-scrutiny trigger** (PE sponsor mandate, post-acquisition integration, public retrenchment, IPO prep) | **20** | Supplies the person who owns the infra line personally |
| **Live infra hiring** (SRE, platform, DBRE, infrastructure — posted ≤90 days) | **15** | The in-market signal; also the cheapest to observe |
| **MongoDB / Atlas presence** | **15** | Trigger and Accessibility channel at once — the BSI credential and co-sell path |
| **Company-side transaction volume**, stated per-period | 10 | Orders, payments, policies, bookings, cards. **Not** customer AUM, spend-under-management or market size |
| **Founded 2018 or earlier** | 10 | "MVP-era architecture" is a claim about elapsed time; 2019+ has no MVP era to modernize |
| Scale: $100M+ raised at Series C or later, OR PE-owned, OR bootstrapped-and-profitable; 200–2,500 employees | 5 | Deal-size floor. Revenue estimates are unusable — coverage was 0% in two of three source runs |
| **Anti-ICP hit** | **−40** | Hard filter, see below |

**M2 anti-ICP — hard filter, never outvoted**

- The company's own product is infrastructure: databases, hosting, PaaS, developer platforms, observability, data connectivity, GPU compute, workflow orchestration. Deepest in-house benches, lowest winnability, sometimes competitors.
- Portfolio or holding companies operating independent brands — no single estate, no single margin owner.
- Publicly listed or SPAC-bound. The ICP stops at pre-IPO.
- Production telemetry access will not be granted (gov/defence data platforms, some regulated data vaults). Assessment-by-hearsay fails.
- Founded 2019 or later.

**Three rules that cost real credits to learn**

1. **A blank field is UNKNOWN, not FAIL.** Return the row with the field marked unknown and let a human judge. Silently dropping rows for missing data once caused 59 of 60 accounts to be reported as failing on a screening column that had never been populated.
2. **Never accept a derived judgment column from the sourcing tool.** Take facts (founded year, headcount, funding, stage, ownership, HQ, job-posting text, tech-stack enrichment); do the scoring here. A transaction-volume classifier failed three times in three different ways, the third time marking 21 companies "verified" when 20 of them had no supporting text at all.
3. **Magnitude-check every count before it ranks anything, including counts from a defined, factual column — then demand its scope.** Origami's `Matching Posting Count` had a clean definition (infrastructure/SRE postings, same domain, same 90-day window, postings not companies) and still produced values that cannot be true. Normalised per 100 employees the sample split sharply: FreedomPay 0.5, Kraken 0.5, Lighthouse 0.7, Chainlink Labs 9.7, **Alan 25.7** — 396 infrastructure postings against 1,542 employees. Asked to verify, Origami could confirm the role list but **could not establish the domain scope or the deduplication method**, and correctly called its own numbers unverified aggregates. The breakdown had never been stored, so the values were unrepairable. **Working band: ~0.5–1 matching posting per 100 employees is normal; above ~5 per 100, do not rank on it until role scope, domain scope and deduplication method are all stated.** A count missing any of the three is UNKNOWN, not a number.

   Corollary: **UNKNOWN is not zero.** Origami returns UNKNOWN when the domain lookup fails, so an account with no count must not rank below an account with a count of 3.

3. **Source accounts** — origami.chat for the account universe **and for technographic signals** — its Enrich Tech Stack call costs 2.5 credits per company and returns the MongoDB/Postgres presence Model B weights at 15. Its Job Posting Search costs 1 credit per posting, so scale the trigger pull deliberately. Reasoning, filtering and export are free — only new data costs. TheirStack goes deeper once wired; WebSearch / WebFetch otherwise: job postings naming legacy stacks, engineering blogs, conference talks, EOL/migration discussion, funding and earnings signals.
4. **Score and rank.** Every score cites the evidence that produced it. No evidence, no points — never infer a signal to make a number look better.
5. **Write** to `marketing/outbound/research/MMYY-target-accounts.md`: the model, the ranked table (account · score · tier · trigger evidence · suggested entry point), and an explicit **disqualified** section with reasons.

## Invoke

```
/lead-scoring
/lead-scoring focus on BFSI in North America, 40 accounts
```

## Output shape

```
## Scoring model
{weights table, as confirmed}

## Tier 1 — score 70+  (N accounts)
| Account | Score | Trigger evidence (with source) | Entry point |

## Tier 2 — score 45–69
## Tier 3 — score 25–44 (nurture only)
## Disqualified — anti-ICP hits, with the reason
```

## Dependencies

- **Reads:** `marketing/icp/ICP.md` (required), `marketing/positioning/positioning.md`, `marketing/company/company.md`
- **Reads via:** **origami.chat** for the account universe, job-posting triggers and tech-stack enrichment (Company Search 0.5/result · Job Posting Search 1/result · Enrich Tech Stack 2.5/company · Enrich Tech Stack by domain 1/domain · Web Research 1/call · Verified Email 3/email). **TheirStack** once wired for deeper technographics. WebSearch / WebFetch across engineering blogs, news and EOL announcements.
- **Writes:** `marketing/outbound/research/MMYY-target-accounts.md`
- **Model B provenance:** derived from the September 2026 ICP-M2 sourcing trial (119 companies, six Origami runs, 400 credits). The ranked output of that trial is the current M2 list; do not re-source it.

## Guardrails

- Evidence-bound per `.claude/rules/evidence-bound-outputs.md`. A signal with no citation does not score.
- The anti-ICP list is a **hard filter**, not a weight to be outvoted.
- No PII beyond publicly-listed role titles — see `.claude/rules/pii-redaction.md`.

## Refresh cadence

Quarterly, or on a major EOL announcement that opens a new cohort.
