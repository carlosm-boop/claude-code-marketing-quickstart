---
name: origami-sourcing
version: '1.0'
last_updated: 2026-09-03
author: wekan
description: Write and price origami.chat retrieval prompts for one ICP and one trigger. Reads the ICP for gates, composes the trigger-first prompt with its draw rule, deduplication step and report block, quotes the credit cost before spending, and returns facts only - no scores, tiers or cohorts. Triggers - "write an Origami prompt", "source accounts on Origami", "run a trigger search", "look-alike search", "how many credits will this cost", "Origami pull", "sample the trigger population"
goal: Get facts out of origami.chat that survive an audit, at a known credit cost, in the unit the decision is denominated in, without letting the tool make any judgment call.
outcome: marketing/outbound/research/MMYY-origami-prompt-{icp}-{trigger}.md with the prompt as issued, the credit estimate, the free questions asked, and the returned fact columns written to marketing/outbound/research/data/.
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

Compose and price origami.chat prompts for **one ICP x one trigger x one offer**. Hand back facts and stop.

Pushing anything to origami.chat is **never autonomous** (`.claude/rules/orchestration.md`). Compose, estimate, surface for approval, then run.

## When to use

- A named ICP needs accounts sourced against a named trigger
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

## The one rule this skill exists to enforce

**Origami retrieves facts well and judges badly. Take the facts; do the judgment here.**

Measured across 8 pulls on ICP-M2 (26 Aug - 2 Sep 2026): of the 65 companies that appeared in more than one pull, **60 had a derived-judgment field contradict itself between runs**. Only 5 had any factual conflict, and 3 of those were cosmetic (`500` vs `495` employees, `411000000` vs `409000000` funding, `series_e` vs `SERIES_E`). Carta came back `NO_EVIDENCE`, then `VERIFIED PER-PERIOD`, then `NO EVIDENCE` again, on the same source text.

| Field | Kind | Companies contradicted |
|---|---|---|
| `Transaction Evidence Review` | derived | **60** |
| `Transaction Volume` | derived | 7 |
| `Matching Posting Count` | factual-looking, definition unstable | 4 |
| `Database Technology Mentions` | extraction | 2 |
| `Engineering Location` | factual | 2 |
| `Employee Count` / `Total Funding` / `Funding Stage` | factual | 1 each, all cosmetic |

Never request, and never accept, a column where Origami has decided something. Request the underlying text and decide locally.

There is a second, quieter failure class: **fields that look factual but are artefacts of the retrieval path.** `Date Posted` on Job Posting Search returns the crawl date. `Matching Posting Count` is a stored aggregate with no deduplication method. The index double-counts requisitions. Neither the tool nor the column name tells you - only a spread check or a magnitude check does.

## Step A - settle the shape before spending anything

Reasoning, filtering and export are free. Only retrieval costs. Iterate the prompt for free until the shape is settled, then pull once.

Establish, by asking the operator or by reading the ICP:

1. Which ICP, and which **single** trigger. Separate triggers get separate searches - they draw from separate universes and **add** rather than intersect.
2. Sample or census. If a sample, **what decision it has to settle** - that sets the size, not the budget.
3. **What unit the decision is denominated in.** Accounts, requisitions, postings, domains. This is the question most likely to waste a pull: a trigger population counted in postings cannot answer a threshold table denominated in accounts without a divisor, and the divisor has to be requested at retrieval time.
4. The credit ceiling.

Gates come from `marketing/icp/ICP.md` for the named ICP - lift its trigger list, qualifiers and disqualifiers rather than inventing them. If that file is marked DRAFT, say so in the output rather than presenting inference as research.

**Cite a gate, never re-derive one.** ICP.md now documents each gate's semantics as well as its value, and the semantics are what a prompt gets wrong. ICP-M2's *Founded 2018 or earlier* is defined there as a **floor with no upper bound** - the sourcing proxy for MVP-era architecture, which needs elapsed time. Read as a range it would exclude exactly the older digital platforms that carry the deepest estates. If a threshold in a prompt does not match ICP.md, ICP.md wins; if ICP.md has no note on it, ask before inventing the semantics.

**Evidence status.** This procedure is derived from one worked run, ICP-M2. The other five WeKan ICPs are untested against it. State that when applying it to a new ICP.

## Step B - the template

Steps 3, 5 and 6 apply when the trigger is a job posting or another repeating document. A firmographic census pull collapses to steps 1, 2, 4 and 7 - the shorter shape in `P10`.

```
STEP 1 - SEARCH ON THE TRIGGER.
  <the observable event>, within the last 90 days.
  Trigger first, then narrow. No firmographic filters here.
  Qualify any role or keyword term known to leak, by name, with the
  false positive it produced last time.
  Retrieve <N>. Do not exceed <N>.

  DRAW RULE. The <N> must be a spread across the full window and
  across companies, not a top slice. Do not sort or rank the draw by
  company, size, funding, volume or recency. <name the bias this
  would introduce in this specific pull>.

STEP 2 - NARROW BY <ICP> FIT.
  Gates: <lift from ICP.md, as bands never as sort keys>
  Resolve identity on domain, never on name.
  Where an adjacent-industry company qualifies on substance, flag it
  ADJACENT and name the industry rather than dropping it.
  EXCLUDE, by category: <categories, not examples>
  A blank field is UNKNOWN, not FAIL - return the row with the field
  marked unknown.
  Return the excluded rows as a table, one reason each.

STEP 3 - <SIGNAL> AUDIT. Applies to all <N>, whether or not they
  pass Step 2. Return the verbatim title or label, and quote the one
  sentence establishing that the thing you are matching on is the
  core of the document. No boolean without its quote - I need the
  false-positive rate of the filter, not your verdict on it.

STEP 4 - SPLIT ON <SIGNAL>. Quote verbatim every instance and the
  sentence it appears in, then group. Name the priority group.
  Quote the sentence, not just the term.

STEP 5 - DEDUPLICATE TO DISTINCT <UNIT>, AND SHOW YOUR WORK.
  For every group of rows sharing the same company and the same
  title, state whether the bodies are identical, near-identical or
  materially different. Assign a <UNIT> ID; rows with identical or
  near-identical bodies at the same company share one ID.
  Keep every row - do not silently drop duplicates. I want the rate.

STEP 6 - DATES, VERBATIM.
  Return the date the source states, as it states it. Do NOT
  substitute the retrieval date. Where only relative recency is
  shown, return the relative string verbatim and mark the absolute
  date UNKNOWN. Never fill the field with today's date.

STEP 7 - RETURN FACTS ONLY, ONE ROW PER <UNIT>.
  One row per <unit>, NOT per company. Do not collapse to a "most
  relevant" row.
  Columns: <unit ID, company, domain, the gate facts, verbatim title,
  date as stated, source URL, verbatim signal mentions, industry>
  No volume column, no fit scores, no screening flags, no derived
  scores, no evidence classifications, no pass/fail verdicts, no
  public-status determinations, no boolean without its quote.

  REPORT - keep the levels distinct:
    a. Trigger population before narrowing, with the window, AND
       whether that figure counts ROWS AS RETURNED or DISTINCT
       <UNIT>S. If you cannot determine which, say so.
    b. Rows retrieved.
    c. Distinct <unit>s among them, and the duplication rate.
    d. Unique companies represented - counted from distinct domains
       in the returned rows, reconcilable against the rows I can
       see. Do not substitute a stored aggregate.
    e. Concentration: how many companies contributed 1, 2, 3-5,
       6-10, 11+. Not the mean.
    f. Rows and <unit>s passing the Step 3 audit.
    g. Companies qualified after Step 2, as unique companies, plus
       the <unit>s they account for.
    h. Excluded rows, one reason each.

  WHY a, c, d AND e MATTER, so they are not optimised away: <state
  the unit conversion the decision needs>. All of it is derivable
  from data already being retrieved; none needs another retrieval.

  FREE QUESTIONS, answer before or alongside the run:
    <questions about how the tool's own filters and aggregates are
    computed - these cost nothing and have repeatedly changed the
    interpretation of a paid figure>

  COUNTS: any per-company count must state its role scope, its
  domain scope and its deduplication method. A count without all
  three is to be returned as UNKNOWN, not as a number.

  If anything above cannot be established without a further
  retrieval, say so rather than estimating.
```

The closing line is the highest-yield sentence in the corpus. It turned the same tool that once marked 21 companies "verified" with no supporting text into one that returned a clean, itemised "I cannot determine this" - and that answer retired a bad signal for zero credits. Never omit it.

## Worked examples

Both are verbatim and committed. Read the one whose shape matches the pull.

| Example | Shape | Where |
|---|---|---|
| `P10` | Census qualify pull, four steps. The only prompt in the corpus that worked on first return | `handoffs/0926-origami-prompt-log.md` §P10 |
| Prompt v3 | 300-posting sample, seven steps. Adds draw rule, role-filter audit, requisition dedup, verbatim dates, the a-h report block and two free questions | `handoffs/0926-origami-300-posting-prompt-v3.md` |

`P10` is the shape to copy when the decision is *which accounts*. v3 is the shape to copy when the decision is *how many*, because that is when units, divisors and duplication start deciding the answer. Note what v3's gates do: the age gate is a **floor** and headcount a **band** - never sort keys, and never a range (see `ICP.md` ICP-M2, *"The age test is a floor, not a range"*). Funding is a three-way OR, so a profitable bootstrapper is not lost to a funding filter. The ADJACENT flag converts an exclusion into a judgment call routed back to the operator.

## Step C - standing constraints

Every prompt, no exceptions. Numbering is referenced from `marketing/latest.md` - do not renumber 10 or 11.

1. **Trigger first, firmographics second.** Intent is 30 of 100 points in the `lead-scoring` model; a firmographic-first search scores zero on it by construction.
2. **A blank field is UNKNOWN, not FAIL** - and UNKNOWN is not zero. It must not rank below a real low value downstream.
3. **Facts only.** No fit scores, evidence classifications, pass/fail screens, or public-status determinations.
4. **Never sort on the dimension you cap.** Band and stratify, and write an explicit DRAW RULE naming the bias. A bigger cap does not fix this - it recurred after the cap was raised.
5. **Do not gate on revenue** (0% coverage in two of three runs, 37% in the third) **or on transaction volume** (unverifiable).
6. **Require an exclusion reason per excluded row**, as a table, not a count.
7. **Reset context explicitly** when changing search shape. Origami carries state between runs.
8. **Pause after the first sample** in a multi-stage plan, so a correction costs one sample rather than the whole pull.
9. **Ignore Fit Score.** A platform default, not a data defect; prompting against it wastes instructions.
10. **Close every prompt with the refusal clause:** *"If anything above cannot be established without a further retrieval, say so rather than estimating."*
11. **Require scope with every count.** Role scope, domain scope, deduplication method. A count missing any of the three is UNKNOWN, not a number - the scope cannot be recovered after the fact.
12. **Never accept a date field without checking its spread against the pull timestamp.** A date column where every value equals the retrieval date is UNKNOWN, not data. Third member of the family with 2 and 3.
13. **One row per unit, never per company, and deduplicate to distinct units with visible working.** Rows are not requisitions. The index double-counts; 14-29% of one pull's rows carried no new requisition, all charged.
14. **Denominate the report in the unit the decision uses, and request the divisor.** Ask what the population figure itself counts. A population in postings against a threshold table in accounts converts to anything until the ratio is known.
15. **No boolean without its verbatim quote**, and name every known leaky term with the false positive it produced.
16. **Lift gates from `ICP.md` verbatim, with their stated semantics.** A floor is not a range, a band is not a sort key, and a qualifier is not optional. Never restate a threshold from memory.

## Step D - cost and sizing

> Only data costs credits. The thinking is free.

| Call | Cost |
|---|---|
| Company Search | 0.5 / result |
| Job Posting Search | 1 / result |
| Enrich Tech Stack | 2.5 / company |
| Enrich Tech Stack (Website) | 1 / domain |
| Web Research | 1 / call |
| Verified Email | 3 / email |
| Verified Phone | 15 / phone |
| Browser Automation | 5 / session |

Quote an estimate before any pull. Refuse to run one that exceeds the stated ceiling without explicit confirmation.

**Charge is per row, not per distinct unit.** At the measured 14-29% duplication rate a 300-row posting pull buys roughly 215-260 distinct requisitions. Quote the effective count, not the row count.

**Size the sample against the decision, not the budget.** A 30-posting sample gave a ~7% qualify rate with a confidence interval of roughly 1%-22% - useless for a threshold decision. 300 rows narrow it to about +/-3 points, +/-3.3 after duplication. Say what interval the operator is buying before spending.

## Step E - hand over

Facts written to `marketing/outbound/research/data/`, with the prompt as issued and the answers to the free questions alongside. No tiers, no scores, no cohorts.

Route the file through `sourcing-csv-audit` before `lead-scoring` touches it.

## Failure catalogue - write against these

All are measured and reproducible from the committed corpus.

1. **Sort-under-cap.** Headcount-descending under a 60-result cap returned 60 companies pinned at the ceiling. Recurred after the cap was raised (`P2`) - proof that banding is the fix. Reappeared in a new dimension when a 300-row draw risked covering only the most recent four days.
2. **Blank read as FAIL.** A blank `Company Screen` collapsed 59 of 60 accounts to one qualified. The correction (`P7`) named three accounts whose own rows contradicted the verdict.
3. **Classifier fabrication.** 20 of 21 rows marked "verified per-period volume" had no period phrase in the source; one company's whole description was a single sentence with no digits. Three attempts, three failure modes: inverted labels, blank-field gating, fabrication. Retired in `P8`.
4. **Neutral title, wrong role.** *Lead Platform Engineer* marked `Role Match = true`; its description named Ember, React, TypeScript and Frontend. "Platform Engineering" is the one leaky term in an otherwise sound role list - qualify it in Step 1, and never accept a match on the title alone.
5. **Keyword match in the wrong sense.** Chainlink Labs returned `Database Technology Mentions = oracle`. Chainlink is a blockchain **oracle** network. Require the sentence, not the term.
6. **A defined column can still be unusable.** `Matching Posting Count` had a clean definition and failed twice: it changed meaning across pulls (15,398 -> 396; 1,231 -> 10; 1,119 -> 9) and failed a magnitude check within a pull (0.5 to 25.7 per 100 employees). Pressed, Origami confirmed the role list but could not establish domain scope or deduplication - only an aggregate had ever been stored. Struck from Model B as UNKNOWN, not pending. A definition is necessary and not sufficient.
7. **Name collision.** "Kraken" in the SRE sample was Kraken Technologies (kraken.tech, energy, founded 2019), not the crypto exchange. Resolve on domain.
8. **Wrong-shape entities leaking through.** Infrastructure vendors and public companies recurred across runs. Name exclusions categorically and require reasons.
9. **The index double-counts requisitions.** One company's posting returned twice with byte-identical 8,238-character descriptions under two source IDs; another twice with near-identical bodies. 14-29% of a pull's rows carried no new requisition. This is also the mechanism behind failure 6's magnitude outlier - the count was not merely wrong, it was counting the same requisition repeatedly.
10. **A date field that is really a timestamp.** `Date Posted` returned 17 distinct dates spanning two months on Company Search, and the pull date on every single row of two Job Posting Searches. The recency half of the trigger - 15 points in Model B - is unverifiable from that output. Company Search proves the tool can return real dates, so this is a path defect, not a capability gap.
11. **Unit mismatch.** A population in postings and a threshold table in accounts. Same qualify rate resolved to "ABM only", "hybrid" or "volume viable" depending on a divisor that had not been requested. The divisor is the decision.

12. **A floor gate without its qualifier admits anything old.** *Founded 2018 or earlier* has no upper bound by design, so the **digital-native qualifier is load-bearing** - it, not the age gate, is what excludes pre-digital companies. Dropped from a real search on 3 September 2026, the age gate happily returned a law firm founded in 1748 and a credit union founded in 1931. Age never excludes; the qualifier does. Carry it in every prompt.

## Provenance

- `handoffs/0926-origami-prompt-log.md` - 14 verbatim prompts, annotated
- `handoffs/0926-origami-300-posting-prompt-v3.md` - the current sampling template and the five amendments behind it
- `handoffs/0926-handoff-origami-skill-spec.md` - the spec this skill implements
- `handoffs/0926-handoff-origami-sourcing.md` - workstream 1 operations, owns the source CSVs
- `marketing/outbound/research/data/0926-origami-companies.csv` - 120 companies, merged fact columns, `Field Conflicts`
- `marketing/outbound/research/data/0926-origami-job-postings.csv` - 36 postings with full descriptions
- `marketing/outbound/research/0926-m2-pursuit-order-snapshot.md` - the 32 qualified accounts with gate evidence
