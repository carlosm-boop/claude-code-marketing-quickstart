# Origami 300-posting sample — prompt v3

**Written:** 3 September 2026 · **Workstream 1: Origami sourcing** · **Mode 3 (Centaur)**
**Supersedes:** the prompt in §9 item 1 of `0926-handoff-origami-sourcing.md`
**Cost:** 300 credits. Every amendment below is prompt text — none requires additional retrieval.

Five amendments. Two are analytical gaps in the v1 prompt; three are data defects measured from
`marketing/outbound/research/data/0926-origami-job-postings.csv` on 3 September, at zero credits.

---

## A1 · Unit mismatch — the divisor was missing

Trigger population is **7,377 postings**. The §2 threshold table is denominated in **accounts**. The v1
REPORT block asked for "companies qualified after Step 2" but never for *unique companies represented in
the 300* — so there is no postings-per-company divisor, and 7,377 converts to anything:

| If 300 rows map to | Rows/company | Trigger pop. in companies | At ~7% qualify | Verdict |
|---|---|---|---|---|
| 25 companies | 12 | ~615 | ~43 | ABM only |
| 60 companies | 5 | ~1,475 | ~103 | Hybrid |
| 200 companies | 1.5 | ~4,900 | ~344 | Volume viable |

Same qualify rate, all three rows of the table. The divisor *is* the decision.

The divisor must be **counted from the returned rows by domain**, not taken from an Origami-supplied
figure. §9 item 3 established that `Matching Posting Count` is an unauditable stored aggregate. A count
reconcilable against visible rows is a different object from one that is not.

## A2 · The one-row-per-posting instruction had been dropped

P11 item 3 established *"OUTPUT IS ONE ROW PER JOB POSTING, not per company."* The v1 item-1 prompt lost
it. Collapsing to one row per company destroys the divisor **and** the MongoDB grouping fidelity P11 was
written to protect — a company may name MongoDB in one posting and Postgres in another.

## A3 · Sort-under-cap, in a new dimension

§6 rule 1: never sort on the dimension you are capping. This sample caps on **postings**. A draw sorted
by company, size, posting count or recency biases the divisor — a recency-sorted 300 out of 7,377 covers
roughly the most recent four days and would badly understate the 90-day company universe. Same failure
that broke pulls 2, 3 and 5, wearing a different hat.

## A4 · MEASURED DEFECT: the posting index double-counts requisitions

Proven from the committed CSV, not inferred:

**Alan, pull P7.** Two rows. Same title (*Senior Platform Engineer (x/f/m) - Data Retention*), same date,
two LinkedIn job IDs (`4461283739`, `4462180441`) — and the job descriptions are **byte-identical**:
8,238 characters, SHA1 `2dcfb33b902b` on both. One requisition, retrieved and charged twice.

**Lighthouse, pulls P7 and P8.** Two rows, same title (*Lead Platform Engineer*), same date, two IDs
(`4452600278`, `4452601242`), descriptions 7,458 vs 7,563 characters — near-identical, not identical.
Most likely one role posted to two locations. Ambiguous from the data.

**Rate in the trigger-first pulls:** of P7's 7 rows, 1 is a proven byte-identical duplicate and a 2nd is
a probable one. **14–29% of rows carry no new requisition.** Origami charges 1 credit per row, so a
300-row pull buys roughly 215–260 distinct requisitions.

**Consequence for the numerator.** This is the same defect that retired `Matching Posting Count` — Origami
could not state its deduplication method, and here we can see why: there isn't one. 7,377 is an aggregate
over the same index. So **the numerator of the C1 calculation is as unverified as the column that was
struck from Model B.** §2 labels 7,377 confidence "Sourced"; that is too generous.

**The saving grace, and the question that resolves it.** If 7,377 counts rows the same way the sample
does, the duplication cancels in `7,377 × (unique companies ÷ rows)`. If 7,377 is deduplicated while the
sample rows are not, using rows as the denominator understates the company universe. **Which it is, is a
free question.** Ask it.

## A5 · MEASURED DEFECT: `Date Posted` is the retrieval date on trigger-first pulls

| Pull | Search type | `Date Posted` values |
|---|---|---|
| P1 | Company Search | 17 distinct dates, 2026-07-06 → 2026-09-01 — real spread |
| P7 | Job Posting Search | `2026-09-02` on all 7 rows |
| P8 | Job Posting Search | `2026-09-02` on all 6 rows |

2026-09-02 is the **pull date**. Every trigger-first posting claims to have been posted the day it was
retrieved. Likely mechanism: LinkedIn renders relative dates ("2 days ago") and Origami records the crawl
date when it cannot parse an absolute one.

**Two consequences.**

1. A3's verification mechanism does not work as written — asking for the posting-date distribution would
   return 300 identical dates and prove nothing. v3 therefore requires the *verbatim* date from the source
   posting, and an explicit refusal where only relative recency is available.
2. Bigger: **the recency half of the trigger is currently unverified.** "Live infrastructure hiring" is 15
   points in Model B. If posting dates are unusable on exactly the pull type that sources the trigger, the
   freshness of that signal cannot be checked from returned data — and the 90-day window behind the 7,377
   figure rests on the same logic. Whether the window filter itself ran is a question for Origami, and it
   is free.

Note that P1 proves Origami *can* return real posting dates. This is a defect in the Job Posting Search
path, not a capability gap.

---

## The prompt — paste as one block

```text
STEP 1 — SEARCH ON THE TRIGGER.
Companies with open roles matching: SRE, Site Reliability, DBRE,
Database Reliability, Infrastructure Engineer, or Platform Engineering
WHERE THE PLATFORM IS INFRASTRUCTURE, NOT FRONT-END. Exclude any
posting whose body is about UI, web front-end, design systems or
client-side frameworks, even when the title says "Platform Engineer" —
that exact title returned an Ember/React/TypeScript role last time.
Posted in the last 90 days. Retrieve 300 postings. Do not exceed 300.

DRAW RULE. The 300 must be a spread across the full 90-day window and
across companies, not a top slice. Do not sort or rank the draw by
company, employee count, funding, posting count, or recency. Three
previous searches returned only their largest companies under a cap
because they sorted descending on the dimension they were capping; a
draw concentrated on a handful of high-volume posters would break the
exact measurement this sample exists to make.

STEP 2 — NARROW BY ICP-M2 FIT.
  - Founded 2018 or earlier
  - 200-2,500 employees
  - $100M+ raised with latest round Series C or later, OR PE-owned,
    OR bootstrapped and profitable
  - Private: not publicly listed, not SPAC-bound
  - US or Europe
  - Digital-native with real transaction volume, typically logistics &
    delivery, insurtech, fintech, marketplaces, vertical SaaS, travel
    tech. Treat that list as indicative of the type, not exhaustive —
    an adjacent-industry digital platform with genuine transaction
    volume qualifies; flag it ADJACENT and name the industry.
  - EXCLUDE companies whose own product is infrastructure: databases,
    hosting, PaaS, developer platforms, observability, data
    connectivity, GPU compute, workflow orchestration.
  - EXCLUDE portfolio and holding companies operating independent
    brands.

STEP 3 — ROLE-FILTER AUDIT. Applies to all 300 postings, whether or
not they pass Step 2. For each posting return the verbatim job title
and quote the one sentence from the posting body that establishes
whether infrastructure, platform, database or reliability work is the
core of the role. Do not return a role-match boolean without that
quote. In the last sample two of six matched postings were front-end
platform roles (Ember/React/TypeScript) under the title "Lead Platform
Engineer", so I need the false-positive rate of the filter itself, not
your verdict on it.

STEP 4 — SPLIT ON DATABASE TECHNOLOGY. Quote verbatim every database
or data-infrastructure technology named in each posting, with the
sentence it appears in, then group:
  GROUP 1 — names MongoDB or MongoDB Atlas
  GROUP 2 — names MySQL, Postgres, MSSQL or a named monolith
  GROUP 3 — names other data infrastructure
  GROUP 4 — none named
Quote the sentence, not just the term: a previous run returned
"oracle" for Chainlink Labs, which is a blockchain oracle network.

STEP 5 — DEDUPLICATE TO DISTINCT REQUISITIONS, AND SHOW YOUR WORK.
Your index double-counts requisitions and I can prove it. In the last
sample, Alan's "Senior Platform Engineer (x/f/m) - Data Retention"
came back twice, at LinkedIn IDs 4461283739 and 4462180441, with
byte-identical 8,238-character descriptions. Lighthouse's "Lead
Platform Engineer" came back twice at IDs 4452600278 and 4452601242.

So: for every group of rows sharing the same company and the same job
title, state whether the job descriptions are identical, near-
identical, or materially different. Assign each row a REQUISITION ID:
rows with identical or near-identical descriptions at the same company
share one requisition ID. Keep every row — do not silently drop the
duplicates; I want to see them and I want the rate.

STEP 6 — POSTING DATES, VERBATIM.
Return the date the posting states it was published, as the source
states it. Do NOT substitute the retrieval date. In the last two
trigger-first pulls every row came back dated the day of the pull —
all 7 rows of one pull and all 6 of the next dated 2026-09-02 — which
makes the 90-day window unverifiable from the output. If a source
shows only relative recency ("2 weeks ago"), return that relative
string verbatim and mark the absolute date UNKNOWN. Never fill the
field with today's date.

STEP 7 — RETURN FACTS ONLY, ONE ROW PER JOB POSTING.
One row per posting, NOT per company. A company with three open infra
roles gets three rows. Do not collapse to a "most relevant posting".

Columns: requisition ID · company · domain · founded year · employee
count · total funding · funding stage · ownership type · HQ location ·
engineering location where stated · verbatim job title · posting date
as stated (or relative string + UNKNOWN) · posting URL · verbatim
technology mentions · industry (or ADJACENT + industry).

No transaction-volume column, no fit scores, no screening flags, no
role-match boolean without its quote. A blank field is UNKNOWN, not
FAIL — return the row with the field marked unknown.

REPORT — three levels of count, kept distinct:
  a. Trigger population before narrowing, with the window. State
     whether that figure counts ROWS AS RETURNED or DISTINCT
     REQUISITIONS. This is the single most important line in the
     report: I am dividing by a sample ratio and multiplying by that
     number, so if the two are counted differently the answer is
     wrong. If you cannot determine which it counts, say so.
  b. Rows retrieved.
  c. DISTINCT REQUISITIONS among those rows, per Step 5, and the
     duplication rate.
  d. UNIQUE COMPANIES represented — count distinct domains in the rows
     themselves and state that number. It must reconcile against the
     rows I can see. Do not substitute a stored aggregate from your
     index; if that is the only figure you have, say so and return the
     rows so I can count them myself.
  e. Distribution of requisitions per company: how many companies
     contributed 1, 2, 3-5, 6-10, 11+. I need the concentration, not
     the mean.
  f. Rows and requisitions passing the role audit.
  g. Companies qualified after Step 2, as UNIQUE COMPANIES, plus the
     requisitions they account for.
  h. The excluded rows as a table with one reason each.

WHY a, c, d AND e MATTER, so they do not get optimised away: the
trigger population is denominated in postings and my decision is
denominated in companies. Without the requisitions-per-company ratio
and a statement of what the population figure counts, I cannot convert
one into the other and this retrieval buys me nothing. All of it is
derivable from data you are already retrieving. None of it requires an
additional retrieval.

TWO FREE QUESTIONS, answer before or alongside the run:
  1. Does the 90-day window filter run against the posting's actual
     publication date, or against the date your index first saw it?
     These give different answers and I need to know which one the
     7,377 figure reflects.
  2. Is 7,377 a count of index rows or of distinct requisitions?

COUNTS: if you report any per-company posting count, state its role
scope, its domain scope, and its deduplication method alongside it. A
count without all three is to be returned as UNKNOWN, not as a number.

If anything above cannot be established without a further retrieval,
say so rather than estimating.
```

---

## How to read the result

1. **Company qualify rate** = unique qualified companies ÷ unique companies in sample. Not rows ÷ rows.
2. **Trigger population in companies** = 7,377 × (unique companies ÷ *the matching denominator*) — rows if
   7,377 counts rows, distinct requisitions if it counts requisitions. Report (a) decides which.
3. **In-market qualified accounts** = (1) × (2) → read off the §2 threshold table. Do not re-argue it.

**Apply the magnitude rule before computing anything.** Working band from `lead-scoring`: ~0.5–1 matching
posting per 100 employees is normal, above ~5 per 100 needs verification. Any company in the sample above
that band gets its requisitions audited by hand before it enters the divisor — otherwise one Alan-shaped
row inflates the mean and shrinks the apparent company universe.

**Use the median, not the mean**, if the concentration distribution in (e) has a long tail.

**Secondary check:** does the sample surface qualified companies the 120-company firmographic pool never
contained? If yes, the 40–150 stock estimate was too low.

**Expect ~215–260 distinct requisitions from 300 rows** at the measured 14–29% duplication rate. That is a
modest precision loss (±3 → ±3.3 points) and does not justify raising the spend.

---

## Corrections owed to other files

- **§2 of `0926-handoff-origami-sourcing.md`:** downgrade the 7,377 confidence from "Sourced" to
  "Unverified aggregate — deduplication unknown, same defect that retired `Matching Posting Count`".
- **§9 of the same file:** two items are numbered 4, and the lines following item 3 are an orphaned tail of
  the retired `Matching Posting Count` prompt, including a dangling code fence.
- **`lead-scoring`:** the magnitude-check rule now has a second instance behind it — Alan's duplicate pair
  is the mechanism that produced the 25.7-per-100 figure, not just evidence that it was wrong.
