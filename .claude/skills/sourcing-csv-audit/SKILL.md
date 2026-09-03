---
name: sourcing-csv-audit
version: '1.2'
last_updated: 2026-09-03
author: wekan
description: Audit a sourced account or posting list before anything downstream touches it. Classifies every column by trust class, type conformance and retrieval path, then runs fifteen checks - coverage, cap-boundary clustering, self-contradicting rows, role match against body text, magnitude, cross-pull contradiction, duplicate units, date spread, unit and divisor integrity, exclusion accounting, filter discriminative power with its conditioning caveat, company-set drift, type conformance, blanks clearing disqualifiers, and whether the evidence text is in the repo. Reports failures and recommends drops; never scores or tiers.
goal: Establish which columns of a sourced list are safe to gate on and which must be dropped, before anyone scores or sequences it.
outcome: marketing/outbound/research/MMYY-{source}-list-audit.md with a column trust table, the fifteen check results, the sole-cause table with its validity verdict, the unknown bucket and recommended drops.
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

### Absence is not symmetric with presence

**Evidence of presence and evidence of absence do not cost the same, and the operative property is whether the source enumerates or samples.** An enumerating source supports an absence; a sampling source never does. One estate-pain sentence establishes a positive; no quantity of *one posting* establishes a negative.

**Mark an absence from a sampling source as provisional, distinctly from an absence from an enumerating source, even though both score zero.** Worked both ways: estate evidence read from job postings is broken, because a job advert samples an estate — nine accounts held a single-source absence scored identically to a thorough search. The MongoDB detector shows what good looks like: it returns a populated list of primary databases, so absence from it is sound, and where it returned nothing the mark stayed unknown rather than absent.

Fourth member of the family: blank is UNKNOWN not FAIL · a derived judgment column is never evidence · a date equal to the pull timestamp is UNKNOWN not data · **an absence from a sampling source is provisional.**

## Step 1 - classify every column before checking anything

| Class | What it is | Trust |
|---|---|---|
| **Factual** | Headcount, funding, founded year, domain, HQ | High. Spot-check only |
| **Extraction** | A term lifted out of source text | Medium. Unusable without the verbatim sentence |
| **Derived judgment** | Any verdict, screen, flag, classification, fit or evidence score | None. Strip it |
| **Definition unstable** | Counts and volumes | None until role scope, domain scope and deduplication method are established |
| **Retrieval artefact** | A field the pipeline filled rather than read - dates, IDs, row counts | None until its spread is checked against the pull |

Then two further passes over the same columns, because trust class alone misses both:

- **Type conformance (check 13).** Does the content match the type the name implies? A quantity column holding status words is a different failure from an untrustworthy column.
- **Retrieval path per value (check 15's sibling).** Where one column's values come from more than one path, **the path is part of the value.** `MongoDB Evidence` returned product-stack detection for twelve accounts and a job-advert slug aggregate for three - one account's "list" held twelve database technologies, which is a hiring corpus, not an estate. Mark them distinctly even where they score alike.

Publish the classification. It is what tells the operator which columns they may gate on.

## Step 2 - the fifteen checks

Run all fifteen. Report each as pass, fail or not applicable, with row counts.

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
| 11 | **Filter discriminative power, with the conditioning test** — count sole-cause rejections per filter, **then for every filter showing near-zero, ask: was this filter applied during the sourcing of this corpus?** If yes, that filter's result is **void** | Measured over 296 companies: company type **110** sole-cause; geography, headcount and capital **zero** each. The zeros were void — that corpus was sourced under those filters. Acting on them returned Ola at 29,658 employees in India. See the conditioning law below |
| 12 | **Company-set drift** — before interpreting any rate change between pulls, diff the company sets | A "fresh gated table" contained the identical 30 companies re-scored. Qualification read as 47% → 13%, which was attrition on a pre-gate draw, not a collapse |
| 13 | **Type conformance** — does each column contain what its name implies? | `Transaction Volume` held **no volume figures at all** across 32 accounts: 20 blank, 9 `UNVERIFIED`, 3 `VERIFIED`. Status words in a quantity column. Distinct from trust class — a trusted column can still be the wrong type |
| 14 | **Blanks clearing disqualifiers** — for every gate that excludes, confirm the field it reads is populated | `Ownership Type` was blank on **27 of 31** roster accounts while a blank cleared a −40 "publicly listed or SPAC-bound" exclusion. The gate was never evaluated against a populated field for 87% of the roster. Check 10 catches blanks *driving* exclusions; this is the inverse |
| 15 | **Is the evidence text in the repo?** — for every signal a row claims, name the canonical file that would hold its text, and grep it | Fired twice in one day in opposite directions: seven accounts credited with estate evidence from a pull whose text was never committed, and a critical path built on a relayed "presumably in HubSpot" for a tool WeKan does not use |

### The conditioning law — read before running check 11

**A filter applied upstream cannot discriminate downstream. Conditioning on a variable destroys its variance, so near-zero discrimination means the gate is *already enforced*, not that it is *unimportant*.**

| Was the filter a gate during sourcing? | What near-zero means | What to do |
|---|---|---|
| **Yes** | The gate is working; selection destroyed the variance | **Drop it from scoring. Never from gating.** |
| **No** | It genuinely fails to separate this population | Consider dropping, after checking the population is representative |

**A sole-cause table answers "what should carry weight in the score." It never answers "what can be removed from the gates."** No test run on a population the gates produced can tell the two apart. Report the table *with its validity verdict per filter* — a zero on a filter the corpus was built under is not a finding, it is an artefact. To test such a gate you must draw a sample without it. `lead-scoring` rule 6 carries the same table; workstream 2 hit this trap from inside Model B, where VOL, SCL and AGE all looked like noise and all three were sourcing gates.

**Run check 11 first when a filter set is on trial** — it is the only check that can retire a rule rather than flag a row, and it runs on data already paid for. Method: build the full row set, apply every filter independently, count the rows each rejects that no other filter rejects, then apply the conditioning test above to every near-zero result.

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
3. **Failed checks.** Which of the fifteen, with affected row counts and two or three named examples. For check 11, the sole-cause table **with a validity verdict per filter**.
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
- An absence from a sampling source is provisional, not absent.
- A blank must not clear a disqualifier any more than it may fail a qualifier.
- Never interpret a rate change without diffing the company sets first.
- Posting text lives in exactly one canonical file. When new text arrives it is merged in, never committed as a second text-bearing file - a second file preserves the evidence and breaks check 15's premise.
- Report contradictions; never resolve one by taking the more recent value.
- A filter with zero sole-cause rejections in a corpus sourced under that filter is **already enforced, not decorative.** Never recommend removing a gate on the strength of a discrimination test; recommend dropping it from *scoring* only.
- Never accept a fit verdict, screen or pass/fail column. It removes rows already paid for, and in one pull it discarded 27 of 30 with no reason — six of them qualified on inspection.

## Provenance

Checks 1-6 and 10 are derived from the ICP-M2 Origami trial; 7, 8 and 9 were added 3 September 2026 from defects measured against the committed job-postings CSV at zero credits; 11 comes from the 296-company consolidation the same day, **as corrected by §8 of the same handover** - the uncorrected form of that check cost a pull; 12-15 come from `handoffs/0926-handover-to-workstream3.md` §10 and §15 and `handoffs/0926-w2-to-w3-skill-deltas.md` §3 and §5. Sources: `marketing/outbound/research/data/0926-origami-companies.csv` (with its `Field Conflicts` column), `marketing/outbound/research/data/0926-origami-job-postings.csv`, `handoffs/0926-origami-prompt-log.md`, `handoffs/0926-origami-300-posting-prompt-v3.md`, `handoffs/0926-handoff-origami-skill-spec.md`, `handoffs/0926-handover-to-workstream3.md`, `marketing/outbound/research/data/0926-consolidated-graded-296-v2.csv`.
