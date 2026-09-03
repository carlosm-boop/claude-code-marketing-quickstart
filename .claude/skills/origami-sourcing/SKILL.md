---
name: origami-sourcing
version: '1.2'
last_updated: 2026-09-03
author: wekan
description: Write and price origami.chat retrieval prompts for one campaign or ICP and one trigger. Establishes what decision the pull serves, whether the call can establish it at all, and whether the answer is already in the repo - then composes a one-discriminating-gate-plus-column-list prompt, prices it per row at observed rates, and returns facts only. No filters on firmographics that are not enforced gates, no scores, no verdicts. Triggers - "write an Origami prompt", "source accounts on Origami", "run a trigger search", "look-alike search", "how many credits will this cost", "Origami pull", "sample the trigger population", "how big is the pool"
goal: Get facts out of origami.chat that survive an audit, at a correctly forecast per-row cost, in the unit the decision is denominated in, without letting the tool filter or judge - and without buying a number whose decision is already settled.
outcome: marketing/outbound/research/MMYY-origami-prompt-{campaign-or-icp}-{trigger}.md with the decision and threshold the pull serves, the prompt as issued, the per-row cost forecast, the campaign-vs-ICP reconciliation, and the returned facts written to marketing/outbound/research/data/.
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

Pushing anything to origami.chat is **never autonomous** (`.claude/rules/orchestration.md`). Establish the decision, forecast the cost, surface for approval, then run.

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

Ignoring it wasted most of a trial. Ten prompts were built at ICP-M2's qualification thresholds (200-2,500 employees, $100M+) instead of campaign C1's targeting thresholds (200-5,000, Series C+/$50M+), and three technographic searches filtered `NOT MongoDB` while C1 gates **on** Atlas signals. The campaign doc was not opened until hour ten.

**Where the two documents disagree, name the conflict and resolve it explicitly - never pick one silently.** C1 names five verticals and says plain "SaaS"; ICP-M2 names six including travel tech and says "vertical SaaS". Neither is wrong. Nobody had reconciled them, so every prompt inherited whichever the author happened to be reading.

## The first rule - facts yes, judgment no

**Origami retrieves facts well and judges badly. Take the facts; do the judgment here.**

Of the 65 companies appearing in more than one pull, **60 had a derived-judgment field contradict itself between runs**. Only 5 had any factual conflict, 3 of those cosmetic. Carta came back `NO_EVIDENCE`, then `VERIFIED PER-PERIOD`, then `NO EVIDENCE` again, on the same source text.

**The corollary matters as much: it is reliable about itself.** On 3 September it gave five honest, itemised, self-critical answers to direct capability questions - retiring `Matching Posting Count`, defining its own confidence scale, defining its hiring filter, explaining the Coupa mechanism, and recommending against scaling a pull with the right structural fix attached. The same day its derived columns were wrong on fit, on database extraction, on public status and on its own row counts. **Ask it about itself freely. Never accept its verdict about a company.**

## The second rule - a filter applied upstream cannot discriminate downstream

**Conditioning on a variable destroys its variance. Near-zero discriminative power means the gate is already enforced, not that it is unimportant.**

This rule exists because its violation cost a pull on 3 September. A sole-cause analysis over 296 companies showed geography and headcount uniquely rejecting **zero**, and both were demoted from gates to columns. That corpus had been sourced *under* geography and headcount filters. The next pull removed them and returned **Ola at 29,658 employees in India, Lazada 21,590 in Singapore, PhonePe 19,151, Daraz 13,487, Trendyol 11,479, Alipay, Flipkart** - **9 of the 14 companies that cleared the transaction-volume gate failed geography or headcount.**

| Was the filter a gate during sourcing? | What near-zero discrimination means | What to do |
|---|---|---|
| **Yes** | The gate is working; selection destroyed the variance | **Drop it from scoring. Never from gating.** |
| **No** | It genuinely fails to separate this population | Consider dropping, after checking the population is representative |

**A discrimination test answers "what should carry weight in the score." It never answers "what can be removed from the gates."** No test run on a population the gates produced can distinguish the two. Workstream 2 hit the same trap from inside Model B - VOL, SCL and AGE all looked like noise and all three were sourcing gates; `lead-scoring` rule 6 carries the decision table above.

To test a gate the corpus was built on, you must draw a sample **without** it, and budget for the junk that comes back.

## Step A - three questions before you spend anything

Reasoning, filtering and export are free. Only retrieval costs. Iterate for free until the shape is settled, then pull once.

**A0. What decision does this number change, and at what threshold would it change it?**

If every plausible value lands on the same side of the threshold, **do not buy the number.** C1's first calibration window needs **143** accounts. Three successive pool projections gave 2,723 -> 1,506 -> 862, all off one stale 30-row sample; the most pessimistic was wrong by four times over and *still sufficient*. Roughly ten hours went into refining a figure whose decision had already been made. The answer was in the ratio the whole time. Ask this before any sizing or population pull.

**A1. Can the call you are about to buy establish what you need at all?**

The operative property of a source is whether it **enumerates** or **samples**.

| Origami call | Behaviour | Can establish presence | Can establish absence |
|---|---|---|---|
| `Enrich Tech Stack` | enumerates the detected stack | yes | **yes** - a populated list with X absent is sound |
| Company Search | enumerates firmographics | yes | yes, where the field is populated |
| Job Posting Search | **samples** whatever reqs exist | yes | **never** |
| Web Research | samples | yes | never |

**If the deliverable is an absence, buy it from an enumerating call.** A sampling call can only ever establish presence. No quantity of job adverts enumerates a database estate.

**A2. Is the answer already in the repo?**

For every signal the pull would buy, name the file that would already hold it, and grep it. One grep fired twice on 3 September in opposite directions: once crediting seven accounts with estate evidence from a posting pull whose text had never been committed, once building a critical path on a relayed "presumably in HubSpot" for a tool WeKan does not use.

Then settle:

1. **Campaign or ICP?** If a campaign, read its spec first (Rule 0) and record the reconciliation against `ICP.md`.
2. Which **single** trigger. Separate triggers get separate searches - they draw from separate universes and **add** rather than intersect.
3. Sample or census. If a sample, what decision it settles - that sets the size, not the budget.
4. **What unit the decision is denominated in.** A trigger population counted in postings cannot answer a threshold table in accounts without a divisor, and the divisor must be requested at retrieval time.
5. The credit ceiling, against the **observed per-row** rate in Step D, not the list price.

Gates come from the campaign spec, then `marketing/icp/ICP.md`. Lift the trigger list, qualifiers and disqualifiers rather than inventing them. If a source file is marked DRAFT, say so rather than presenting inference as research.

**Cite a gate, never re-derive one.** ICP.md documents each gate's semantics as well as its value, and the semantics are what a prompt gets wrong. ICP-M2's *Founded 2018 or earlier* is defined there as a **floor with no upper bound** - the proxy for MVP-era architecture, which needs elapsed time. Read as a range it would exclude exactly the older digital platforms that carry the deepest estates. If a threshold disagrees with its source, the source wins.

**Evidence status.** Derived from one worked trial, ICP-M2 / campaign C1. The other five WeKan ICPs are untested against it.

## Step B - the template: one discriminating gate, the enforced gates, everything else a column

Three blocks, not a stack of numbered filter steps. **The stack is the shape that failed** - seven numbered steps each applying a filter produced two days of oscillation between over-filtering with no reasons and no filtering with raw junk.

What each block is for:

- **The discriminating gate** is the one that does the work. Measured over 296 companies, company type / the transaction-volume qualifier had **110 sole-cause rejections** - it uniquely rejects more than every other filter combined. That finding stands, because it discriminates *within* a corpus already conditioned on the other filters.
- **The enforced gates** are geography, headcount band and public/private status. They show near-zero discrimination in any corpus sourced under them, and per the second rule **that is not permission to remove them.** They are what keeps the universe clean; the Ola pull is what happens without them.
- **Columns** are everything else: read, never filtered, never ranked.

```
THE GATE - WHAT THE COMPANY DOES.
  <the operative test, judged from the company's own description and
  keywords - never from an industry label>
  e.g. ICP-M2: a digital-native platform with real transaction
  volume. The transaction-volume qualifier is the operative test.

  EXCLUDE, by named category: companies whose own product is
  infrastructure - databases, hosting, PaaS, developer platforms,
  observability, data connectivity, GPU compute, workflow
  orchestration; portfolio and holding companies operating
  independent brands.

  NOT-A-COMPANY REJECT: description under ~25 characters, or
  ownership SELF_EMPLOYED / PARTNERSHIP / GOVERNMENT_AGENCY.

  Return every excluded row with its reason, as a table. A row
  excluded with no reason is a defect, not an exclusion.
  Resolve identity on domain, never on name.
  Where an adjacent-industry company qualifies on substance, flag it
  ADJACENT and name the industry rather than dropping it.

THE ENFORCED GATES - short, hard, stated as gates.
  Geography: <from the campaign spec>
  Headcount band: <from the campaign spec>
  Status: not publicly listed, not SPAC-bound. Read current status,
    and where two internal checks disagree, report the conflict
    rather than resolving it.
  Founded: <the floor, with no upper bound>

COLUMNS - EVERYTHING ELSE, EXPLICITLY NOT A FILTER.
  company · domain · description (verbatim, required) · founded year ·
  headcount · ownership type and sub-type · total funding · latest
  round · current public/private status · HQ · industry label as
  returned · infra-posting boolean · detected technologies with
  confidence · <trigger-specific facts>
  Do not filter, gate, screen, rank or score on any column above.
  No fit verdict, no evidence classification, no pass/fail screen.
  Where a column's values come from more than one retrieval path,
  name the path per value - the path is part of the value.

BLANKS. A blank field is UNKNOWN, not FAIL. Return the row with the
  field marked unknown. A blank must not clear an exclusion any more
  than it may fail a qualifier.

NO SORT, NO RANK, ON ANYTHING. Report the sequence as returned. Do
  not order the output by any column, and do not order within any
  group or band.

FRESH DRAW. Draw a NEW sample under all gates. Do not re-use or
  re-score the previous table.

COST. Report cost per row retrieved, broken down by call type.

If anything above cannot be established without a further retrieval,
say so rather than estimating.
```

The closing line is the highest-yield sentence in the corpus, and it produced all five honest self-diagnoses. Never omit it.

**Role and signal terms.** Where the trigger is a role, qualify every term known to leak, by name, and require the tool to count infrastructure versus non-infrastructure terms in each posting body. "Platform Engineering" false-positives at a measured **3 of 7**, in three confirmed variants - front-end/web platform, **AI/ML platform**, and data/analytics platform. All three go in the exclusion list by name. A first pass judging from titles got 3 of 7 wrong where the body-text count got it right; the title has been wrong every time it has been tested.

**When the pull is trigger-first**, the trigger search precedes the gate and is not itself a company filter - see `P10`. Add what a repeating-document pull needs: a signal audit quoting the sentence that establishes the match rather than a boolean, content-hash deduplication to distinct requisitions with the rate reported, verbatim source dates, one row per document, and a report block keeping rows, requisitions and unique companies distinct.

## Worked examples

| Example | Status | Where |
|---|---|---|
| `P10` | **Current reference for a trigger-first pull.** Worked on first return | `handoffs/0926-origami-prompt-log.md` §P10 |
| EST pull prompt | Current reference for the role exclusions and infra-term counts | `handoffs/0926-est-pull-prompt.md` |
| Prompt v3 | **WITHDRAWN 3 Sep 2026.** Provenance only - do not run | `handoffs/0926-origami-300-posting-prompt-v3.md` |

**Why v3 was withdrawn.** Priced in its handoff at 300 credits for 300 postings; **~1,560 at observed rates**, because enrichment is charged per company on top of retrieval. And its shape is the numbered gate stack this skill rejects. Its individual amendments are sound and folded into the constraints; the prompt block is not to be reused.

## Step C - standing constraints

Numbering is referenced from `marketing/latest.md` - do not renumber 10 or 11.

**Above all of them: Rule 0, the second rule, and the three questions in Step A.**

1. **Trigger first, firmographics second.** Intent is 30 of 100 points in the `lead-scoring` model; a firmographic-first search scores zero on it by construction.
2. **A blank field is UNKNOWN, not FAIL** - and UNKNOWN is not zero. A blank must not clear a disqualifier either.
3. **Facts only.** No fit scores, evidence classifications, pass/fail screens, or public-status determinations.
4. **Never sort or rank on any dimension you cap or band - including inside a band.** Fifth recurrence on 3 September: output banded 200-1,000 / 1,000-2,500 / 2,500-5,000 and sorted descending *within each band*, sampling **2.2%, 12% and 25%**, all monotonic. Banding alone is not the fix. Require the returned sequence, verify it is not monotonic, and state sampled min and max against each band's bounds as a coverage percentage. Any fit-density conclusion from a banded sample is void until within-band ordering is checked. **Do not respond to this by removing the cap** - see the second rule.
5. **Do not gate on revenue** (0% coverage in two of three runs) **or on transaction volume** (unverifiable).
6. **Require an exclusion reason per excluded row**, as a table, not a count.
7. **Reset context explicitly** when changing search shape. Origami carries state between runs.
8. **Pause after the first sample** in a multi-stage plan, so a correction costs one sample rather than the whole pull.
9. **Ignore Fit Score.** A platform default, not a data defect.
10. **Close every prompt with the refusal clause:** *"If anything above cannot be established without a further retrieval, say so rather than estimating."*
11. **Require scope with every count.** Role scope, domain scope, deduplication method. A count missing any of the three is UNKNOWN, not a number.
12. **Never accept a date field without checking its spread against the pull timestamp.** A date column where every value equals the retrieval date is UNKNOWN, not data.
13. **One row per unit, never per company; deduplicate to distinct units by content hash with visible working.** Rows are not requisitions. 14-29% of one pull's rows carried no new requisition, all charged.
14. **Denominate the report in the unit the decision uses, and request the divisor.**
15. **No boolean without its verbatim quote, and no role match without a body-text term count.** Name every known leaky term with the false positive it produced.
16. **Lift gates from the campaign spec and `ICP.md` verbatim, with their stated semantics.** A floor is not a range, a band is not a sort key, a qualifier is not optional.
17. **Ask the tool about itself; never accept its verdict about a company.**
18. **Never search on an industry label.** Search the description and keywords, and require the description as a column.
19. **Reject the polluted universe explicitly** with the not-a-company test. The index is LinkedIn company pages; it contains people.
20. **Buy an absence only from an enumerating call.** An absence from a sampling source is **provisional, not absent**, and must be marked distinctly even though both score zero. Fourth member of the family with 2, 3 and 12.
21. **When adding or changing a gate, demand a new draw.** State it in the prompt: *draw a NEW sample under all gates; do not re-use or re-score the previous table.*
22. **Any projected pool figure states its sample basis and the gates that sample was drawn under.** A projection from a sample drawn under different gates is void.
23. **Price per row retrieved, never per qualified lead.**
24. **Posting text lives in exactly one canonical file.** Merge new text into it; never commit a second text-bearing file.

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

**List price is not the price you pay. Enrichment is charged per company on top of retrieval.** Forecast every pull as `rows × (retrieval + per-company enrichment)` and warn when the enrichment column list is long.

**Price in credits per ROW.** Origami's own "credits per lead" is a derived figure that moves with gate strictness, not with price - it reported 3.2/lead ungated and 5.3/lead gated for the same cost and fewer qualified rows. **A per-lead figure looks worse every time you correctly tighten a filter**, which makes it useless for budgeting and actively misleading as a quality signal.

| Configuration | Observed per row |
|---|---|
| Thin tech-stack Company Search, no enrichment | **1.2** - cheapest measured |
| Facts-first with description | **~1.5** |
| Trigger-first with per-company enrichment | **~5.2** |
| Trigger-first with a fit verdict discarding most rows | **~24 per qualified** |

The 20x spread is mostly the fit verdict, which constraint 3 already forbids - it discards rows you have paid for. **A prompt that asks for a verdict pays twice: once in credits, once in lost accounts.**

**`Infra/SRE Posting` is now free at search time.** The gated pull populated it on all 30 rows, having returned it blank on all 30 the pull before. A 15-point signal now attaches to every sourced account at zero marginal cost - take it out of the enrichment budget entirely.

Quote a forecast before any pull and refuse to exceed the stated ceiling without confirmation. Ask the tool for cost per returned row broken down by call type; it answers that honestly, and it is how these rates were established.

## Step E - hand over

Facts written to `marketing/outbound/research/data/`, with the decision and threshold from A0, the prompt as issued, the campaign-vs-ICP reconciliation, the per-row forecast against actual, and the answers to any capability questions. Posting text merges into the canonical postings CSV. No tiers, no scores, no cohorts.

Route the file through `sourcing-csv-audit` before `lead-scoring` touches it.

## Failure catalogue

All measured and reproducible from the committed corpus.

1. **Sort-under-cap.** Headcount-descending under a 60-result cap returned 60 companies pinned at the ceiling. Recurred after the cap was raised, and again *inside* bands - five occurrences.
2. **Blank read as FAIL.** A blank `Company Screen` collapsed 59 of 60 accounts to one qualified.
3. **Classifier fabrication.** 20 of 21 rows marked "verified per-period volume" had no period phrase in the source.
4. **Neutral title, wrong role - measured at 3 of 7.** Three confirmed variants of the leaky "Platform Engineering" term: front-end/web (an Ember-to-React migration titled *Lead Platform Engineer*), **AI/ML platform** (one description with **zero** infrastructure terms), and data/analytics platform (3 infra terms against 4 non-infra). Require the body-text count; the title has been wrong every time it has been tested.
5. **Keyword match in the wrong sense.** `Database Technology Mentions = oracle` for a blockchain **oracle** network.
6. **A defined column can still be unusable.** `Matching Posting Count` changed meaning across pulls (15,398 -> 396) and failed a magnitude check within one (0.5 to 25.7 per 100 employees). Retired as UNKNOWN.
7. **Name collision.** "Kraken" was Kraken Technologies (kraken.tech, energy, 2019), not the exchange. Resolve on domain.
8. **Wrong-shape entities leaking through.** Infrastructure vendors and public companies recurred across runs.
9. **The posting index double-counts requisitions.** One posting twice under two IDs with **byte-identical** 8,238-character descriptions (SHA1 `2dcfb33b902b`); 14-29% of trigger-first rows carried no new requisition.
10. **A date field that is really a timestamp.** Company Search gave 17 dates across two months; two Job Posting Searches gave the pull date on all 13 rows.
11. **Unit mismatch.** A population in postings against a threshold table in accounts. The same qualify rate resolved to three different strategic verdicts depending on a divisor nobody had requested.
12. **A floor gate without its qualifier admits anything old.** The age floor has no upper bound by design, so the digital-native qualifier is load-bearing - dropped, the gate returned a law firm founded in 1748 and a credit union founded in 1931.
13. **The universe is polluted.** Company search runs over LinkedIn company pages: personal profiles ("Women Developer", 2,187 employees; "Account Manager", 1,242), a freelance consultant at 3,927, the City of Hamburg, a US defence agency, a furniture trade newspaper. Employee counts on those rows are meaningless.
14. **The industry taxonomy collapses.** 28 of 30 rows returned `software development`; **zero** returned logistics, insurtech, fintech or marketplace. "Vertical SaaS" is not a taxonomy value and behaved as a catch-all.
15. **A fit verdict silently discards qualified accounts.** `Fit Check` rejected 27 of 30 with no reason; the rejects held three insurance platforms (Zinnia, EIS, RGI) and three marketplaces (italki, Sitly, Teachers Pay Teachers). The most expensive form of the standing rule, because it removes rather than adds - and you have paid for every row it throws away.
16. **Public status, and the mechanism.** Seven occurrences before Origami explained it: *"Latest Round only checked whether a value existed; it did not penalize POST_IPO_EQUITY. The business check then accepted the later private-equity acquisition."* Two internal checks disagreed and the permissive one won. Manual review caught three more afterwards (Fiverr, ACV Auctions, OLX).
17. **The sole-cause trap.** A discrimination test run on a corpus its own gates produced said geography and headcount were decorative. Acting on it returned Ola at 29,658 employees in India. See the second rule - this is the most expensive failure in the catalogue, because it removes a gate rather than admitting one bad row.
18. **Adding a gate re-scored the old sample.** Asked to add two gates, Origami produced a "fresh gated table" containing the **identical 30 companies**, byte-for-byte, re-scored. Qualification read as collapsing 47% -> 13%; it was attrition on a draw made before the gates existed, 16 of 30 rows in Asia, South America or Africa. Demand a new draw and diff the company set before interpreting any rate change.
19. **Pool projections mistaken for counts.** 2,723 -> 1,506 -> 862 off one stale 30-row sample, with the tool's own caveat that none should be treated as a campaign-sizing TAM.
20. **An absence bought from a sampling call.** Estate evidence read from job postings: a job advert *samples* an estate and never enumerates one, so a company with a twenty-year estate that does not mention it in one SRE req scores the same zero as a thorough search. Nine accounts held a single-source absence. The counter-example shows what good looks like - the MongoDB detector returns a *populated list* of primary databases, so absence from it is sound, and where it returned nothing the mark stayed unknown rather than absent.

## Provenance

- `handoffs/0926-handover-to-workstream3.md` - items 1-15, including the §8 correction this version implements
- `handoffs/0926-w2-to-w3-skill-deltas.md` - workstream 2's deltas
- `handoffs/0926-handoff-origami-sourcing.md` - workstream 1 operations, owns the source CSVs and the full Rule 0 statement
- `handoffs/0926-origami-prompt-log.md` §P10 · `handoffs/0926-est-pull-prompt.md` · `handoffs/0926-origami-300-posting-prompt-v3.md` (**withdrawn**)
- `marketing/outbound/research/data/0926-consolidated-graded-296-v2.csv` · `0926-origami-companies.csv` · `0926-origami-job-postings.csv` (canonical posting text)
