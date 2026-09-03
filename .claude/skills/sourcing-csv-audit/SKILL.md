---
name: sourcing-csv-audit
version: '1.0'
last_updated: 2026-09-03
author: wekan
description: Audit a sourced account or posting list before anything downstream touches it. Classifies every column as factual, extraction, derived judgment, definition-unstable or retrieval artefact, then runs ten checks - coverage, cap-boundary clustering, self-contradicting rows, role match against body text, magnitude, cross-pull contradiction, duplicate units, date spread, unit and divisor integrity, exclusion accounting. Reports failures and recommends drops; never scores or tiers. Triggers - "here's the CSV Origami returned", "does this list look right", "audit this account list", "check this sourcing data", "is this data trustworthy", "can I gate on this column", "why is this count so high"
goal: Establish which columns of a sourced list are safe to gate on and which must be dropped, before anyone scores or sequences it.
outcome: marketing/outbound/research/MMYY-{source}-list-audit.md with a column trust table, the ten check results, the unknown bucket and recommended drops.
primitive: research
ontology_type: data-audit
review_gate: 1
inputs:
  recommended:
    - origami-sourcing
    - icp-research
outputs:
  - type: data-audit
    feeds_into:
      - lead-scoring
owned_by_agent: gtm-engineer
mcps_used:
  - websearch
triggers:
  slash_commands:
    - /sourcing-csv-audit
status: draft
---

# sourcing-csv-audit - the gate before scoring

Audit a sourced list **before** anything scores, sequences or presents it. Report failures with the affected rows. Do not fix the list silently.

Tool-agnostic by design - Origami, TheirStack, Sales Nav, Clay, Apollo, a hand-built sheet. The failure modes belong to retrieval tools in general, not to one vendor.

Every check below is free. Nine of the eleven defects behind them were found this way, at zero credits, after the data was already paid for.

## When to use

- A sourcing pull came back and nothing downstream has touched it yet
- Someone wants to gate or weight on a column and its trustworthiness is unestablished
- A column's values look different from the last pull
- A count or a qualify rate looks wrong for the population it came from

## When NOT to use

- Weighting, ranking or tiering the accounts -> `lead-scoring`
- Writing the prompt that produced the file -> `origami-sourcing`
- Deciding the gates themselves -> `icp-research`

## Operating principle

**Retrieval tools retrieve facts well and judge badly - and some of what looks factual is an artefact of the retrieval path.**

Measured across 8 Origami pulls on ICP-M2 (September 2026): of the 65 companies appearing in more than one pull, **60 had a derived-judgment field contradict itself between runs**. Only 5 had any factual conflict, 3 of those cosmetic. A list can be factually sound and still be unusable - because every verdict in it is noise, because its date column is a crawl timestamp, or because its rows count the same requisition twice.

## Step 1 - classify every column before checking anything

| Class | What it is | Trust |
|---|---|---|
| **Factual** | Headcount, funding, founded year, domain, HQ | High. Spot-check only |
| **Extraction** | A term lifted out of source text | Medium. Unusable without the verbatim sentence |
| **Derived judgment** | Any verdict, screen, flag, classification, fit or evidence score | None. Strip it |
| **Definition unstable** | Counts and volumes | None until role scope, domain scope and deduplication method are established |
| **Retrieval artefact** | A field the pipeline filled rather than read - dates, IDs, row counts | None until its spread is checked against the pull |

Publish the classification. It is what tells the operator which columns they may gate on.

## Step 2 - the ten checks

Run all ten. Report each as pass, fail or not applicable, with row counts.

| # | Check | Why it is on the list |
|---|---|---|
| 1 | Coverage per column - what percentage non-blank? | Revenue came back 0% twice and 37% once. A gate on a sparse column silently drops good accounts. Below ~60%, mark the column **ungateable** rather than gating and reporting survivors |
| 2 | Do values cluster at a cap boundary? | Sorting on a dimension under a result cap returns a list pinned at the ceiling. Three occurrences, including after the cap was raised |
| 3 | Does any row's verdict contradict its own fact columns? | One account was marked undecided on funding while its own `Ownership Type = PE-owned` already resolved that branch |
| 4 | Spot-check every role or category match against the body text | Two of six matched postings in one sample were front-end roles behind the title *Lead Platform Engineer*. A title is not evidence |
| 5 | Magnitude-check every volume or count against a denominator | "100M transactions/day" at 598 employees is ~36B/year. Working band for postings: ~0.5-1 per 100 employees normal, above ~5 needs verification |
| 6 | Re-run overlap - does any derived field disagree with a previous pull? | 60 of 65 did. Fastest way to establish that a judgment column is worthless |
| 7 | Duplicate units - group rows by company plus title, then compare bodies by length and hash | One company's posting appeared twice with byte-identical 8,238-character descriptions under two source IDs; another twice with near-identical bodies. **14-29% of one pull's rows carried no new requisition**, all charged. Report the duplication rate and treat rows and units as different objects |
| 8 | Date spread against the pull timestamp | `Date Posted` gave 17 dates across two months on one search type and the pull date on every row of two others. A date column whose values all equal the retrieval date is UNKNOWN, not data |
| 9 | Unit and divisor integrity | Is every count denominated in the unit the decision uses, is the divisor present, and does it reconcile against visible rows? A population in postings against a threshold in accounts resolved to three different strategic verdicts depending on a divisor nobody had requested |
| 10 | Are excluded rows accounted for, and is any exclusion driven by a blank field? | A blank screen once collapsed 59 of 60 accounts to one qualified |

Checks 5, 7 and 8 tend to fire together. When they do, look for one mechanism rather than three defects: duplicate rows inflate a per-company count, which is what a magnitude outlier is usually made of.

## Step 3 - the unrepairable call

Some columns cannot be rescued, and saying so is the deliverable.

A count or volume column that cannot produce its **role scope, domain scope and deduplication method** is unrepairable, not merely unverified - the scope cannot be reconstructed after retrieval. Recommend dropping it as UNKNOWN for all rows, not caveating it and not marking it pending. Pressed on exactly this, Origami confirmed the role list, could not establish domain scope or deduplication because only an aggregate had ever been stored, called its own values unverified aggregates and declined to estimate. That was the correct answer and it cost nothing.

The same call applies to:

- **Identity resolved on name rather than domain.** "Kraken" in one sample was Kraken Technologies (kraken.tech, energy, 2019), not the crypto exchange.
- **An extraction column without its sentence.** `oracle` on a blockchain oracle network would have put a crypto provider on an Oracle-migration list.
- **A date column equal to the pull date.** Not "approximately right" - unknown. Anything weighting recency on it is weighting nothing.
- **A stored aggregate offered in place of a count from visible rows.** Different object. Say so and count the rows.

When a defect is found in a *derived* figure that a paid figure depends on, downgrade the paid figure's confidence too. The trigger population inherited the deduplication defect of the index it was counted from.

## Step 4 - the report

Five parts, in this order:

1. **Verdict in one line.** Safe to use for X, not safe for Y.
2. **Column trust table.** Name, class, coverage percentage, gateable yes/no.
3. **Failed checks.** Which of the ten, with affected row counts and two or three named examples.
4. **Unknown bucket.** Rows held for review because a field was blank, with the field named. Never merged into the excluded set.
5. **Recommended drops.** Columns to strip before handoff, with the reason - and any confidence downgrade owed to a figure elsewhere.

Then stop. Scoring, tiering and messaging are downstream.

## Hard rules

- A blank field is UNKNOWN, not FAIL - and UNKNOWN is not zero.
- Never gate on a column whose coverage has not been reported.
- Never accept a match on a title, or a boolean without its quote.
- Never accept a count without its three scopes.
- Never accept an extracted term without its sentence.
- Never accept a date without its spread.
- Rows are not units. Report the duplication rate before anyone divides by a row count.
- Resolve identity on domain, never on name.
- Report contradictions; never resolve one by taking the more recent value.

## Provenance

Checks 1-6 and 10 are derived from the ICP-M2 Origami trial; 7, 8 and 9 were added 3 September 2026 from defects measured against the committed job-postings CSV at zero credits. Sources: `marketing/outbound/research/data/0926-origami-companies.csv` (with its `Field Conflicts` column), `marketing/outbound/research/data/0926-origami-job-postings.csv`, `handoffs/0926-origami-prompt-log.md`, `handoffs/0926-origami-300-posting-prompt-v3.md`, `handoffs/0926-handoff-origami-skill-spec.md`.
