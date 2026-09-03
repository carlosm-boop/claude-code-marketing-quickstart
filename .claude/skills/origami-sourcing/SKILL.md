---
name: origami-sourcing
version: '1.1'
last_updated: 2026-09-03
author: wekan
description: Write and price origami.chat retrieval prompts for one campaign or ICP and one trigger. Reads the campaign spec and the ICP for gates, composes a one-gate-plus-column-list prompt, prices it at observed per-company rates, and returns facts only - no filters on firmographics, no scores, no verdicts. Triggers - "write an Origami prompt", "source accounts on Origami", "run a trigger search", "look-alike search", "how many credits will this cost", "Origami pull", "sample the trigger population"
goal: Get facts out of origami.chat that survive an audit, at a correctly forecast credit cost, in the unit the decision is denominated in, without letting the tool filter or judge.
outcome: marketing/outbound/research/MMYY-origami-prompt-{campaign-or-icp}-{trigger}.md with the prompt as issued, the cost forecast, the campaign-vs-ICP reconciliation, and the returned facts written to marketing/outbound/research/data/.
primitive: research
ontology_type: sourcing-prompt
review_gate: 2
inputs:
  required:
    - icp-research
  recommended:
    - positioning
outputs:
  - type: account-facts
    feeds_into:
      - sourcing-csv-audit
      - lead-scoring
owned_by_agent: gtm-engineer
mcps_used:
  - websearch
triggers:
  slash_commands:
    - /origami-sourcing
status: draft
---

# origami-sourcing - the retrieval skill

Compose and price origami.chat prompts. Hand back facts and stop.

Pushing anything to origami.chat is **never autonomous** (`.claude/rules/orchestration.md`). Compose, forecast the cost, surface for approval, then run.

## When to use

- A named campaign or ICP needs accounts sourced against a named trigger
- A prompt came back with the wrong shape and needs rewriting before the next pull
- A sample has to settle a threshold question and needs sizing
- Someone needs the credit cost of a pull before committing to it
- A look-alike search against an existing qualified roster

## When NOT to use

- Scoring, tiering or cohort assignment -> `lead-scoring`
- Auditing a file that already came back -> `sourcing-csv-audit`
- Deciding who to target at all -> `icp-research`
- Writing the first touch -> `outreach-emails`

This skill produces no external-facing copy, so `marketing/brand/brand-voice.md` does not bind its output. The escalation rule on pushing to origami.chat does.

## Rule 0 - read the campaign doc before writing a prompt

**`ICP.md` defines a good-fit customer. The campaign spec defines who enters the sequence. When sourcing for a named campaign, the campaign's numbers govern.**

Campaign gates live in the `WeKan Outbound Campaign Prioritization` project doc; the full statement of this rule is in `handoffs/0926-handoff-origami-sourcing.md`.

This is Rule 0 because ignoring it wasted most of a trial. Ten prompts were built at ICP-M2's qualification thresholds (200-2,500 employees, $100M+) instead of campaign C1's targeting thresholds (200-5,000, Series C+/$50M+), and three technographic searches filtered `NOT MongoDB` while C1 gates **on** Atlas signals. The campaign doc was not opened until hour ten.

**Where the two documents disagree, name the conflict and resolve it explicitly - never pick one silently.** C1 names five verticals and says plain "SaaS"; ICP-M2 names six including travel tech and says "vertical SaaS". Neither is wrong. Nobody had reconciled them, so every prompt inherited whichever the author happened to be reading.

## The one rule this skill exists to enforce

**Origami retrieves facts well and judges badly. Take the facts; do the judgment here.**

Measured across 8 pulls on ICP-M2: of the 65 companies appearing in more than one pull, **60 had a derived-judgment field contradict itself between runs**. Only 5 had any factual conflict, 3 of those cosmetic. Carta came back `NO_EVIDENCE`, then `VERIFIED PER-PERIOD`, then `NO EVIDENCE` again, on the same source text.

**The corollary matters just as much: it is reliable about itself.** On 3 September it gave five honest, itemised, self-critical answers to direct capability questions - retiring `Matching Posting Count`, defining its own confidence scale, defining its hiring filter, explaining the Coupa mechanism, and recommending against scaling a pull with the right structural fix attached. The same day, its derived columns were wrong on fit, on database extraction, on public status and on its own row counts. **Ask it about itself freely. Never accept its verdict about a company.**

There is a third failure class: **fields that look factual but are artefacts of the retrieval path or of a polluted index.** `Date Posted` on Job Posting Search returns the crawl date. The company index is LinkedIn company pages, so it contains personal profiles with four-figure employee counts. Only a spread check, a magnitude check or a description read catches these.

## Step A - settle the shape before spending anything

Reasoning, filtering and export are free. Only retrieval costs. Iterate for free until the shape is settled, then pull once.

Establish, in this order:

1. **Campaign or ICP?** If a campaign, read its spec first (Rule 0) and record the reconciliation against `ICP.md`.
2. Which **single** trigger. Separate triggers get separate searches - they draw from separate universes and **add** rather than intersect.
3. Sample or census. If a sample, **what decision it has to settle** - that sets the size, not the budget.
4. **What unit the decision is denominated in.** Accounts, requisitions, postings, domains. A trigger population counted in postings cannot answer a threshold table denominated in accounts without a divisor, and the divisor must be requested at retrieval time.
5. The credit ceiling - against the **observed** rate in Step D, not the list price.

Gates come from the campaign spec, then `marketing/icp/ICP.md` for the named ICP. Lift the trigger list, qualifiers and disqualifiers rather than inventing them. If a source file is marked DRAFT, say so in the output rather than presenting inference as research.

**Cite a gate, never re-derive one.** ICP.md documents each gate's semantics as well as its value, and the semantics are what a prompt gets wrong. ICP-M2's *Founded 2018 or earlier* is defined there as a **floor with no upper bound** - the sourcing proxy for MVP-era architecture, which needs elapsed time. Read as a range it would exclude exactly the older digital platforms that carry the deepest estates. If a threshold in a prompt does not match its source, the source wins; if the source has no note on it, ask before inventing the semantics.

**Evidence status.** This procedure is derived from one worked trial, ICP-M2 / campaign C1. The other five WeKan ICPs are untested against it. State that when applying it to a new ICP.

## Step B - the template: one gate, everything else a column

**This is the shape, and the shape is the point.** Filter on what the company *does*. Everything else is a column you read, not a gate you apply.

Measured over **296 unique companies** consolidated from all 16 sourcing CSVs, by counting **sole-cause rejections** - how many more companies would qualify if a given filter were deleted:

| Filter | Rejects | Sole cause |
|---|---|---|
| **Company type / transaction-volume qualifier** | 232 | **110** |
| Public / SPAC-bound | 31 | 5 |
| Not-a-company | 101 | 4 |
| Founded year | 5 | 1 |
| Geography | 2 | **0** |
| Headcount | 6 | **0** |
| Capital (Series C+ / $50M+) | 17 | **0** |

Company type does essentially all the work. Headcount, geography and capital uniquely reject **nobody** - every company they catch is already caught by type. A gate stack of seven numbered filter steps is what produced two days of oscillation between over-filtering with no reasons and no filtering with raw junk.

```
ONE GATE - WHAT THE COMPANY DOES.
  <the operative test, judged from the company's own description and
  keywords - never from an industry label>
  e.g. ICP-M2: a digital-native platform with real transaction
  volume. The transaction-volume qualifier is the operative test.

  EXCLUDE, by named category: <e.g. companies whose own product is
  infrastructure - databases, hosting, PaaS, developer platforms,
  observability, data connectivity, GPU compute, workflow
  orchestration; portfolio and holding companies operating
  independent brands; publicly listed or SPAC-bound>

  NOT-A-COMPANY REJECT: description under ~25 characters, or
  ownership SELF_EMPLOYED / PARTNERSHIP / GOVERNMENT_AGENCY.

  Return every excluded row with its reason, as a table. A row
  excluded with no reason is a defect, not an exclusion.
  Resolve identity on domain, never on name.
  Where an adjacent-industry company qualifies on substance, flag it
  ADJACENT and name the industry rather than dropping it.

COLUMNS - EVERYTHING ELSE, EXPLICITLY NOT A FILTER.
  company · domain · description (verbatim, required) · founded year ·
  headcount · ownership type and sub-type · total funding · latest
  round · current public/private status · HQ · industry label as
  returned · infra-posting boolean · detected technologies with
  confidence · <trigger-specific facts>
  Do not filter, gate, screen, rank or score on any column above.
  No fit verdict, no evidence classification, no pass/fail screen.

BLANKS. A blank field is UNKNOWN, not FAIL. Return the row with the
  field marked unknown.

NO SORT, NO RANK, ON ANYTHING. Report the sequence as returned. Do
  not order the output by any column above, and do not order within
  any group or band.

COST. Report cost per returned company, broken down by call type.

If anything above cannot be established without a further retrieval,
say so rather than estimating.
```

The closing line is the highest-yield sentence in the corpus, and it is what produced all five honest self-diagnoses. Never omit it.

**When the pull is trigger-first**, the trigger search precedes the gate and is not itself a company filter - see `P10`. Add the per-document requirements that a repeating-document pull needs: a signal audit that quotes the sentence establishing the match rather than returning a boolean, content-hash deduplication to distinct requisitions with the rate reported, verbatim source dates, one row per document, and the report block that keeps rows, requisitions and unique companies distinct.

## Worked examples

| Example | Status | Where |
|---|---|---|
| `P10` | **Current reference for a trigger-first pull.** Four steps, worked on first return | `handoffs/0926-origami-prompt-log.md` §P10 |
| Prompt v3 | **WITHDRAWN 3 Sep 2026.** Provenance only - do not run | `handoffs/0926-origami-300-posting-prompt-v3.md` |

**Why v3 was withdrawn.** Two reasons, both fatal. It was priced in its handoff at 300 credits for 300 postings; at observed rates it is **~1,560**, because enrichment is charged per company on top of retrieval. And its shape is the seven-step gate stack this skill now rejects - four of its filters have zero or near-zero discriminative power. Its individual amendments remain sound and are folded into the constraints below; the prompt block itself is not to be reused.

## Step C - standing constraints

Numbering is referenced from `marketing/latest.md` - do not renumber 10 or 11.

**Above all of them: Rule 0, and the shape rule - one gate, everything else a column.**

1. **Trigger first, firmographics second.** Intent is 30 of 100 points in the `lead-scoring` model; a firmographic-first search scores zero on it by construction.
2. **A blank field is UNKNOWN, not FAIL** - and UNKNOWN is not zero. It must not rank below a real low value downstream.
3. **Facts only.** No fit scores, evidence classifications, pass/fail screens, or public-status determinations.
4. **Never sort or rank on any dimension you cap or band - including inside a band.** Fifth recurrence on 3 September: output banded 200-1,000 / 1,000-2,500 / 2,500-5,000 and sorted descending *within each band*, sampling **2.2%, 12% and 25%** of the three bands, all monotonic descending. Banding alone is not the fix. Require the returned sequence, verify it is not monotonic, and state the sampled min and max against each band's bounds as a coverage percentage. Any fit-density conclusion from a banded sample is void until within-band ordering is checked. **Better still, drop the cap** - headcount uniquely rejects nobody, so capping on it buys nothing.
5. **Do not gate on revenue** (0% coverage in two of three runs, 37% in the third) **or on transaction volume** (unverifiable).
6. **Require an exclusion reason per excluded row**, as a table, not a count.
7. **Reset context explicitly** when changing search shape. Origami carries state between runs.
8. **Pause after the first sample** in a multi-stage plan, so a correction costs one sample rather than the whole pull.
9. **Ignore Fit Score.** A platform default, not a data defect; prompting against it wastes instructions.
10. **Close every prompt with the refusal clause:** *"If anything above cannot be established without a further retrieval, say so rather than estimating."*
11. **Require scope with every count.** Role scope, domain scope, deduplication method. A count missing any of the three is UNKNOWN, not a number - the scope cannot be recovered after the fact.
12. **Never accept a date field without checking its spread against the pull timestamp.** A date column where every value equals the retrieval date is UNKNOWN, not data.
13. **One row per unit, never per company, and deduplicate to distinct units by content hash with visible working.** Rows are not requisitions. 14-29% of one pull's rows carried no new requisition, all charged.
14. **Denominate the report in the unit the decision uses, and request the divisor.** Ask what the population figure itself counts.
15. **No boolean without its verbatim quote**, and name every known leaky term with the false positive it produced.
16. **Lift gates from the campaign spec and `ICP.md` verbatim, with their stated semantics.** A floor is not a range, a band is not a sort key, a qualifier is not optional.
17. **Ask the tool about itself; never accept its verdict about a company.** Capability questions are free and reliably answered. Verdicts are neither.
18. **Never search on an industry label.** Search the company description and keywords, and require the description as a column.
19. **Reject the polluted universe explicitly** with the not-a-company test in the template. The index is LinkedIn company pages; it contains people.

## Step D - cost, at observed rates

> Only data costs credits. The thinking is free.

| Call | List rate |
|---|---|
| Company Search | 0.5 / result |
| Job Posting Search | 1 / result |
| Enrich Tech Stack | 2.5 / company (website variant 1 / domain) |
| Web Research | 1 / call |
| Verified Email | 3 / email |
| Verified Phone | 15 / phone |
| Browser Automation | 5 / session |

**List price is not the price you pay. Enrichment is charged per company on top of retrieval.**

**Forecast every pull as `rows × (retrieval + per-company enrichment)`, and warn when the enrichment column list is long.** Measured on 3 September:

| Configuration | Observed |
|---|---|
| Tech-stack Company Search, thin table | **1.2 credits / company** - the cheapest all day |
| Trigger-first pull | **~5.2 credits / returned row** |
| Trigger-first with full enrichment and a fit verdict | **~24 credits / qualified company** |

The 20x spread between the cheapest and most expensive configurations is mostly the fit verdict, which is also the thing constraint 3 forbids - it discards rows you already paid for. **A prompt that asks for a verdict pays twice: once in credits, once in lost accounts.**

Quote a forecast before any pull, at observed rates, and refuse to run one that exceeds the stated ceiling without explicit confirmation. Ask the tool for cost per returned company broken down by call type - it answers that honestly, and it is how the rates above were established.

**Size the sample against the decision, not the budget.** A 30-posting sample gave a ~7% qualify rate with a confidence interval of roughly 1%-22% - useless for a threshold decision. Say what interval the operator is buying, at what real cost, before spending.

## Step E - hand over

Facts written to `marketing/outbound/research/data/`, with the prompt as issued, the campaign-vs-ICP reconciliation, the cost forecast against actual, and the answers to any capability questions. No tiers, no scores, no cohorts.

Route the file through `sourcing-csv-audit` before `lead-scoring` touches it. Its check 11 - filter discriminative power - is what keeps the gate list honest over time.

## Failure catalogue

All are measured and reproducible from the committed corpus.

1. **Sort-under-cap.** Headcount-descending under a 60-result cap returned 60 companies pinned at the ceiling. Recurred after the cap was raised, and again *inside* bands on 3 September - five occurrences. Banding is not the fix; not sorting is.
2. **Blank read as FAIL.** A blank `Company Screen` collapsed 59 of 60 accounts to one qualified.
3. **Classifier fabrication.** 20 of 21 rows marked "verified per-period volume" had no period phrase in the source; one company's whole description was a single sentence with no digits.
4. **Neutral title, wrong role.** *Lead Platform Engineer* marked `Role Match = true`; its description named Ember, React, TypeScript and Frontend. "Platform Engineering" is the one leaky term in an otherwise sound role list.
5. **Keyword match in the wrong sense.** Chainlink Labs returned `Database Technology Mentions = oracle`. Chainlink is a blockchain **oracle** network.
6. **A defined column can still be unusable.** `Matching Posting Count` had a clean definition and still changed meaning across pulls (15,398 -> 396) and failed a magnitude check within one (0.5 to 25.7 per 100 employees). Retired as UNKNOWN, not pending.
7. **Name collision.** "Kraken" in the SRE sample was Kraken Technologies (kraken.tech, energy, 2019), not the crypto exchange.
8. **Wrong-shape entities leaking through.** Infrastructure vendors and public companies recurred across runs.
9. **The posting index double-counts requisitions.** One posting returned twice under two source IDs with **byte-identical** 8,238-character descriptions (SHA1 `2dcfb33b902b`); another twice with near-identical bodies. 14-29% of trigger-first rows carried no new requisition. Require content-hash dedup and report rows versus distinct requisitions separately.
10. **A date field that is really a timestamp.** Company Search returned 17 distinct dates spanning 2026-07-06 to 09-01; two Job Posting Searches returned the pull date on all 13 rows. The recency half of the trigger - 15 points in Model B - is unverifiable from that output.
11. **Unit mismatch.** A population in postings against a threshold table in accounts. The same qualify rate resolved to "ABM only", "hybrid" or "volume viable" depending on a divisor nobody had requested.
12. **A floor gate without its qualifier admits anything old.** *Founded 2018 or earlier* has no upper bound by design, so the **digital-native qualifier is load-bearing**. Dropped from a real search, the age gate returned a law firm founded in 1748 and a credit union founded in 1931.
13. **The universe is polluted.** Company search runs over LinkedIn company pages. A facts-only pull returned personal profiles ("Women Developer", 2,187 employees; "Account Manager", 1,242), a freelance consultant listed at 3,927 employees, the City of Hamburg, a US defence agency and a furniture trade newspaper. **Employee counts on those rows are meaningless.** The not-a-company reject in the template is the fix.
14. **The industry taxonomy collapses.** 28 of 30 rows returned `software development`; **zero** returned logistics, insurtech, fintech or marketplace. "Vertical SaaS" is not a taxonomy value at all and behaved as a catch-all. Never search the label; search the description.
15. **A fit verdict silently discards qualified accounts.** `Fit Check` rejected 27 of 30 with no reason given. The rejects contained three insurance platforms (Zinnia, EIS, RGI) and three marketplaces (italki, Sitly, Teachers Pay Teachers). **This is the most expensive form of the standing rule, because it removes rather than adds** - and you have already paid for every row it throws away.
16. **Public status, and the mechanism behind it.** Seven occurrences before Origami explained it: *"Latest Round only checked whether a value existed; it did not penalize POST_IPO_EQUITY. The business check then accepted the later private-equity acquisition."* Two internal checks disagreed and the permissive one won. Require an explicit current-status conflict check - manual review still caught three more afterwards (Fiverr, ACV Auctions, OLX). Note that this explanation is itself an instance of the corollary: it diagnosed its own defect correctly when asked.

## Provenance

- `handoffs/0926-handover-to-workstream3.md` - the corrections this version implements
- `handoffs/0926-handoff-origami-sourcing.md` - workstream 1 operations, owns the source CSVs and the full Rule 0 statement
- `handoffs/0926-origami-prompt-log.md` - 14 verbatim prompts, annotated. `P10` is the trigger-first reference
- `handoffs/0926-origami-300-posting-prompt-v3.md` - **withdrawn**, provenance only
- `handoffs/0926-handoff-origami-skill-spec.md` - the original spec
- `marketing/outbound/research/data/0926-consolidated-graded-296-v2.csv` - 296 companies, the discriminative-power measurement
- `marketing/outbound/research/data/0926-origami-companies.csv` · `0926-origami-job-postings.csv`
- `marketing/outbound/research/0926-m2-pursuit-order-snapshot.md` - the 32 qualified accounts with gate evidence
