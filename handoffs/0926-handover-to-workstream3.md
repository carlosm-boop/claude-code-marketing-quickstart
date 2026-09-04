# Handover to workstream 3 — `origami-sourcing` skill corrections, 3 September 2026

Written by workstream 1. The skill was authored this morning from the v3 prompt. **v3 is withdrawn**, and the
day produced one finding that changes the skill's core shape rather than adding to its constraint list.

---

> ## ⚠ RECONCILIATION — read this before §1 and §7
>
> **§1 and §7 below are superseded in their conclusion, not in their finding.** §1's sole-cause table and §7's
> instruction to demote geography and headcount to columns were written before §8, which voided their basis.
> Workstream 3 found a fourth affected passage neither workstream 2 nor I flagged — Step B's justification for
> the one-gate shape — which was the load-bearing one. The reconciliation is §16 at the end of this file.
>
> **What survives:** the ergonomic finding (no stack of numbered filter steps) and TYPE's dominance.
> **What does not:** "demote geography and headcount to columns" as an instruction.

## 1. The headline: one gate, everything else a column

Measured across **296 unique companies** consolidated from all 16 sourcing CSVs
(`data/0926-consolidated-graded-296-v2.csv`). Method: for each filter, count **sole-cause rejections** — the
companies it uniquely rejects, i.e. how many more would qualify if the filter were deleted.

| Filter | Rejects | Sole cause |
|---|---|---|
| **Company type / transaction-volume qualifier** | 232 | **110** |
| Public / SPAC-bound | 31 | 5 |
| Not-a-company | 101 | 4 |
| Founded year | 5 | 1 |
| Geography | 2 | **0** |
| Headcount | 6 | **0** |
| Capital (Series C+ / $50M+) | 17 | **0** |

**Company type does essentially all the work.** Headcount, geography and capital uniquely reject nobody —
every company they catch is already caught by type.

**Skill change:** the prompt template should carry **one gate and a column list**, not a gate stack. The
template's current shape — seven numbered steps each applying a filter — is what produced two days of
oscillation between over-filtering with no reasons and no filtering with raw junk.

**New audit-checklist check (#11): filter discriminative power.** Before trusting any filter set, compute
sole-cause rejections. A filter with zero sole-cause is decorative and should be demoted to a column. This is
free — it runs on data already paid for — and it is the single highest-leverage check in the catalogue.

## 2. Rule 0 belongs in the skill's trigger section

**When sourcing for a named campaign, the campaign's numbers govern; `ICP.md` defines a good-fit customer,
the campaign spec defines who enters the sequence.** Full statement in `0926-handoff-origami-sourcing.md`.
Campaign gates live in the `WeKan Outbound Campaign Prioritization` project doc.

**The skill must instruct: read the campaign doc before writing a prompt.** Ten prompts in this trial were
built at M2's qualification thresholds (200–2,500 employees, $100M+) instead of C1's targeting thresholds
(200–5,000, Series C+/$50M+), and three tech searches filtered `NOT MongoDB` while C1 gates *on* Atlas
signals. The campaign doc was never opened by this workstream until hour ten.

Also: **where the two documents disagree, say so and resolve it explicitly.** C1 names five verticals and
says plain "SaaS"; ICP-M2 names six including travel tech and says "vertical SaaS". Neither is wrong; nobody
had reconciled them.

## 3. Sort-under-cap: banding is NOT sufficient — fifth recurrence

Constraint 6 currently says band and stratify. **That is not enough.** On 3 September the output was banded
into 200–1,000, 1,000–2,500 and 2,500–5,000, and the descending sort was applied *inside each band*:

| Band | Actually sampled | Coverage |
|---|---|---|
| 200–1,000 | 982–1,000 | **2.2%** |
| 1,000–2,500 | 2,320–2,500 | 12% |
| 2,500–5,000 | 4,219–4,853 | 25% |

All three monotonic descending. Any fit-density conclusion drawn from a banded sample is void until
within-band ordering is checked.

**Strengthen the constraint to:** *never sort or rank on any dimension you are capping or banding, including
inside a band. Require the returned sequence and verify it is not monotonic. State the sampled min and max
against the band's min and max, as a coverage percentage.*

**And the better fix, per §1: remove the headcount cap entirely.** With no cap there is nothing to cluster
against, and the filter has zero discriminative power anyway.

## 4. Failure catalogue — six new entries, all reproducible from committed data

1. **The universe is polluted.** Origami's company search runs over LinkedIn company pages. A facts-only pull
   returned personal profiles ("Women Developer", 2,187 employees; "Account Manager", 1,242), freelancers
   (a Russian consultant, "Профессия liberale (auto-entrepreneur)" at 3,927 employees), the City of Hamburg
   (hamburg.de), a US defence agency, and a furniture trade newspaper. **Employee counts on those rows are
   meaningless.** New check: reject rows whose description is under ~25 characters or whose ownership is
   `SELF_EMPLOYED` / `PARTNERSHIP` / `GOVERNMENT_AGENCY`.
2. **The industry taxonomy collapses.** 28 of 30 rows returned `software development`; zero returned
   logistics, insurtech, fintech or marketplace. **Never search on an industry label; search on the company
   description and keywords, and require the description as a column.** "Vertical SaaS" is not a taxonomy
   value at all and acted as a catch-all in P3.
3. **`Date Posted` is the retrieval date on Job Posting Search.** P1 (Company Search) returned 17 distinct
   dates spanning 2026-07-06 → 09-01. P7 and P8 returned `2026-09-02` on all 13 rows — the pull date. New
   constraint: *a date column where every value equals the pull timestamp is UNKNOWN, not data.*
4. **The posting index double-counts requisitions.** Alan's *Senior Platform Engineer* returned twice at two
   LinkedIn IDs with **byte-identical** 8,238-character descriptions (SHA1 `2dcfb33b902b`). 14–29% of rows in
   the trigger-first pulls carried no new requisition. Require content-hash dedup and report rows versus
   distinct requisitions separately.
5. **A fit verdict silently discards qualified accounts.** `Fit Check` rejected 27 of 30 with no reason. The
   rejects contained three insurance platforms (Zinnia, EIS, RGI) and three marketplaces (italki, Sitly,
   Teachers Pay Teachers). This is the most expensive form of the standing rule, because it removes rather
   than adds. **Never request a fit verdict. Request facts plus the description and grade locally.**
6. **Public-status: the mechanism, after seven occurrences.** Origami's own explanation: *"Latest Round only
   checked whether a value existed; it did not penalize POST_IPO_EQUITY. The business check then accepted the
   later private-equity acquisition."* Two checks disagreed and the permissive one won. Require an explicit
   current-status conflict check. Note that manual review still caught three more (Fiverr, ACV Auctions, OLX).

## 5. Method finding worth its own constraint

**Origami is reliable about itself and unreliable when judging companies.** Five times on 3 September it gave
an honest, itemised, self-critical answer to a direct capability question — the `Matching Posting Count`
retirement, the confidence-scale definition, the hiring-filter definition, the Coupa mechanism, and the
"don't scale this" recommendation with the right structural fix attached. In the same day its derived columns
were wrong on fit, on database extraction, on public status, and on its own row counts.

**Constraint:** ask the tool capability questions freely and trust the answers; never accept a verdict about a
company. Always close with *"if anything above cannot be established without a further retrieval, say so
rather than estimating"* — that clause produced every one of the five honest answers.

## 6. Costs, corrected

| Call | Rate |
|---|---|
| Company Search | 0.5 / result |
| Job Posting Search | 1 / result |
| Enrich Tech Stack | 2.5 / company · website variant 1 / domain |
| Web Research | 1 / call |
| Verified Email | 3 · Verified Phone | 15 |

**Observed rates are higher than the list price because enrichment is charged per company on top of
retrieval.** The trigger-first pulls ran at **~5.2 credits per returned row**, and a pull whose fit checks
discarded most rows reached **~24 per qualified company**. The v3 prompt was priced in the handoff at 300
credits for 300 postings; at observed rates it was **~1,560**. **Skill change: price a prompt by
`rows × (retrieval + per-company enrichment)`, and warn when the enrichment column list is long.**

The cheapest configuration measured all day: tech-stack Company Search returning a thin table, **1.2 credits
per company**. The most expensive: trigger-first with full enrichment and a fit verdict, ~24.

## 7. What the skill's template should now be

Replace the v3 seven-step shape with:

1. **One gate** — what the company does, judged from description and keywords, with the transaction-volume
   qualifier as the operative test and the exclusion categories named with a required reason per excluded row.
2. **A column list** — everything else, explicitly not a filter: founded year, headcount, ownership and
   sub-type, funding and latest round, HQ, industry label, infra-posting boolean, detected technologies with
   confidence.
3. **Blank = UNKNOWN, not FAIL**, stated in the prompt.
4. **No sort, no rank, on anything.** Report the returned sequence.
5. **A cost question**: cost per returned company, broken down by call type.
6. **The refusal clause**, verbatim, last.

`P10` remains the reference for a trigger-first pull. The v3 block is provenance only — keep it, marked
withdrawn, with the cost reason attached.

---

# ADDENDUM 2 — late 3 September. Read item 8 first; it corrects a check I gave you this morning.

## 8. CORRECTION — audit check #11 is unsafe as I wrote it

This morning I proposed **check #11: filter discriminative power via sole-cause rejections.** Compute, for each
filter, how many companies it uniquely rejects; zero sole-cause means the filter is decorative.

**As written, that check will mislead you, and it misled me the same day.**

I ran it on 296 companies and found geography and headcount uniquely rejected **zero**. I told Rudra to demote
both from gates to columns. That corpus had been sourced *under* geography and headcount filters, so their
variance had already been destroyed by conditioning. The next pull removed them and returned **Ola at 29,658
employees in India, Lazada 21,590 Singapore, PhonePe 19,151 India, Alipay China** — 9 of 14 qualified
companies failing geography or headcount.

**Amended check #11:**

> Compute sole-cause rejections for each filter. **Then ask, for every filter showing near-zero sole-cause:
> was this filter applied during the sourcing of this corpus?** If yes, the result is void — conditioning on a
> variable destroys its variance, and near-zero sole-cause means *already enforced*, not *unimportant*. The
> check is only valid for filters the corpus was NOT filtered by. To test a filter the corpus was built on,
> you must draw a sample without it.

Workstream 2 hit the identical trap from inside Model B — VOL, SCL and AGE all looked like noise and all three
were sourcing gates. Their `lead-scoring` rule 6 carries both worked examples. **This skill needs the same
rule, because this skill is where the check lives.**

## 9. The enumerate/sample rule — a purchasing rule, not just a scoring one

Refined by workstream 2 from a weaker version of mine. The operative property of a source is **whether it
enumerates or samples.**

| Origami call | Behaviour | Can establish presence | Can establish absence |
|---|---|---|---|
| `Enrich Tech Stack` | enumerates the detected stack | yes | **yes** — a populated list with X absent is sound |
| Company Search | enumerates firmographics | yes | yes, when the field is populated |
| Job Posting Search | **samples** whatever reqs exist | yes | **never** |
| Web Research | samples | yes | never |

**Prompt-authoring rule: if the deliverable is an absence, buy from an enumerating call. A sampling call can
only ever establish presence.** No quantity of job adverts enumerates a database estate.

Corollary for marks: **an absence from a sampling source is provisional, not absent.** Fourth member of the
family, after blank-is-UNKNOWN, derived-columns-are-not-evidence, and a date column equal to the pull
timestamp is UNKNOWN.

## 10. New failure mode — adding a gate re-scores the old sample

Asked to add two gates, Origami produced a "fresh gated table" that contained the **identical 30 companies**,
byte-for-byte the same set, re-scored. Qualification fell 47% → 13%, which read as a collapse and was actually
attrition on a sample drawn before the gates existed — 16 of its 30 rows in Asia, South America or Africa.

**Prompt requirement: when adding or changing a gate, state explicitly "draw a NEW sample under all gates; do
not re-use or re-score the previous table."** And an audit check: compare the company set against the previous
pull before interpreting any rate change.

## 11. Pool projections are not counts

Three figures came out of one stale 30-row sample: **2,723 → 1,506 → 862**, each recomputed as gates were
added, with Origami's own caveat that *"neither number should be treated as an exact TAM for campaign
sizing."*

**Rule: any projected pool figure must state its sample basis and the gates that sample was drawn under. A
projection from a sample drawn under different gates is void.**

## 12. Pre-flight question that would have saved most of a day

Workstream 2's phrasing, and it is the best process finding of the day:

> **Ask first what decision the number changes, and at what threshold it would change it.**

C1's calibration window needs **143** accounts. Every configuration all day projected hundreds. The threshold
was never in doubt; roughly ten hours went into refining a number whose decision had already been made. **Add
this as the first question in the skill's trigger section, before any sizing or population pull.**

## 13. The leaky role term now has a rate and a taxonomy

"Platform Engineering" false-positives measured at **3 of 7** on pull P9. Three confirmed variants:

1. **front-end / web platform** — Lighthouse, an Ember-to-React migration under "Lead Platform Engineer"
2. **AI / ML platform** — Meilleurtaux "AI Platform Engineer – AZURE", Chrono24 "(Senior) AI Platform Engineer"
   with **zero** infrastructure terms in the body
3. **data / analytics platform** — Facile.it "Platform Engineer – DevEx & Cloud", 3 infra terms against 4
   non-infra

**All three belong in the template's exclusion list by name.** And the stronger fix: **require an
infra-term-versus-non-infra-term count in the posting body for every row, and never judge the role from its
title.** Workstream 2's own first pass judged 3 of 7 from titles and was wrong — the text check said 4 of 7
clean. The title has been wrong every time it has been tested.

## 14. Cost model, refined again

**Origami's "credits per lead" is a derived figure that moves with your gate strictness, not with price.** It
reported 3.2/lead on the ungated sample and 5.3/lead on the gated one — same cost, fewer qualified rows.

**Rule: price a pull in credits per ROW retrieved. Credits per qualified lead is an output of the gates, not a
property of the tool, and it will look worse every time you correctly tighten a filter.**

Observed per-row rates: **1.2** (thin tech-stack Company Search, no enrichment) · **~1.5** (facts-first with
description) · **~5.2** (trigger-first with per-company enrichment) · **~24 per qualified** (trigger-first with
a fit verdict discarding most rows).

**Also: HIR is now free at search time.** The gated pull populated `Infra/SRE Posting` on all 30 rows, having
returned it blank on all 30 the pull before. A 15-point signal now attaches to every sourced account at zero
marginal cost — so it comes out of the enrichment budget entirely.

## 15. The canonical-text premise, and why it is load-bearing

Workstream 2's one-grep check — *"is the posting text actually in the repo?"* — depends on there being exactly
**one** file that holds posting text. It caught a real error twice today in opposite directions.

When the cost-test CSV turned out to hold text for seven accounts, the fix was **not** to commit a second
text-bearing file: that preserves the evidence and breaks the premise, so the next grep fails. Its 22 rows
were merged into `0926-origami-job-postings.csv` (36 → 58, tagged `Pull = P9 cost-test`) with the raw file
committed alongside for provenance.

**Two rules:** posting text lives in exactly one canonical file, and *"is the text in the repo"* is a step in
`sourcing-csv-audit`, not something someone remembers.


---

# §16 — RECONCILIATION, and the measurement that settles it

## The dispute

- **My §1/§7:** geography and headcount uniquely reject nobody across 296 companies → demote to columns.
- **My §8:** that corpus was conditioned on both, so the result is void → the Ola pull proved they have power.
- **Workstream 3:** re-derived into discriminating gate / enforced gates / columns, keeping all four as hard
  prompt gates. *"Wrongly keeping a gate costs a narrower pull, wrongly dropping one costs Ola."*
- **Workstream 2:** the tension is *where* enforcement happens, not gate-versus-column. Enforce locally after
  retrieval and both survive — and it is the only way a gate can ever be measured again. **A gate in the
  prompt is a gate you can never measure.** Their counter-example: Vinted (4,035) and ShiftKey (3,884) clear
  every C1 gate and would have been rejected by every prior pull on headcount alone.

## The fresh pull is the first unconditioned corpus this trial has produced

`data/0926-c1-fresh-pull-graded.csv` / the 405-row gated table retains **rejected rows as well as accepted
ones**, and Origami is already retrieving outside both gates and filtering locally:

- **239 of 405 rows (59%)** are outside the 200–5,000 headcount band
- **125 of 405 rows (31%)** are outside US/Europe

So workstream 2's proposal is not a change to how sourcing works — **it is a description of what the current
configuration already does.** The removal counts they asked for are already computable from the returned
table. And check 11 is valid on this corpus.

## Check 11, run properly

| Filter | Rejects | Sole cause | Drop it → |
|---|---|---|---|
| **TYPE** | 321 | **19** | +19 qualify |
| FOUNDED | 67 | 7 | +7 |
| PUBLIC | 42 | 6 | +6 |
| GEO | 125 | **1** | +1 |
| HEADCOUNT | 239 | **0** | +0 |

**Joint test — the one nobody ran:** dropping **both** geography and headcount admits **1** additional
company. Zero companies are rejected by that pair jointly and by neither alone. On this corpus, 124 of the 125
geographically-excluded companies also fail TYPE.

## So the answer is neither "keep" nor "drop"

On the 30-row sample, 9 of 14 TYPE-passing companies failed geography or headcount — Ola, Lazada, PhonePe,
Alipay. On this 405-row sample, dropping both costs one company. **Same two gates, opposite verdicts, because
the samples differ.**

The difference is TYPE's specificity. With the exclusion categories fully named, TYPE catches nearly
everything geography would; with a loose TYPE gate it does not, and geography is load-bearing.

**Therefore: the value of a gate is sample-dependent, so it cannot be settled once.** That is the argument for
workstream 2's split, and it is stronger than the argument they made for it — local enforcement is not merely
*safer*, it is the only configuration under which the recurring measurement is possible at all.

**Adopting workstream 2's split as written:** geography and status stay prompt gates (settled values).
Headcount band and founded floor are retrieved above and filtered locally with the removal count reported
(contested values — Rule 0 exists *because* C1 and `ICP.md` disagree on headcount). Their ~64% waste estimate
on the headcount dimension matches the measured 59%.

## Amendment owed to check 11 — my error, and it is a second caveat

§8 added the conditioning caveat. It needs one more:

> **Sole-cause is a marginal statistic. It measures redundancy, not dispensability.** Two filters with
> overlapping coverage each show near-zero sole-cause while the pair is load-bearing. Always run the joint
> test — drop each candidate *set*, not each filter — and never remove more than one near-zero filter without
> re-measuring after the first removal.

Here the marginal and joint results agreed (+0 and +1 respectively), so the original conclusion happened to
survive on this corpus. That was luck. I used a marginal statistic to justify a joint decision, which is the
error underneath the conditioning error.

## Workstream 3's shape call: endorsed, with the split applied

Re-deriving rather than reverting was right, and catching Step B was the better find — a skill whose
*structure* rests on voided reasoning is worse than one whose instructions do. The three-block shape stands.
Apply workstream 2's split inside the enforced-gates block and the file needs no further change from me.

---

# §17 — Cost model, corrected again with settlement data (4 September)

## Billing behaves in two stages, and only the second one counts

Origami **quotes a temporary gross charge, then settles.** Measured on the three zero-yield company pulls:

| Pull | Quoted | Settlement refund | Net |
|---|---|---|---|
| 1 (244 candidates) | 125.00 | −125.00 | **0** |
| 2 (389 candidates) | 199.50 | −199.50 | **0** |
| 3 (497 candidates) | 319.96 | −319.96 | **0** |
| | **644.46** | **−644.46** | **0** |

So *"you were only charged for the qualified companies you got"* is literally true — zero qualified, zero net
cost. **Rule: never record a quoted figure as spend. Read the balance after settlement.** Every per-lead and
per-row figure in this file derived from a quote rather than a settled balance is an upper bound.

## Job Posting Search rate — my figure was wrong in both directions

I priced the 44-domain EST pull at **1 credit per posting, 30–60 credits total.** Actuals:

- **Rate is 0.5 credits per candidate returned**, not 1.0 per posting → my rate was **2× too high**
- **1,277 candidates returned**, 949 retained after filtering → billing is on **candidates returned, not rows
  retained** (0.67 per retained posting)
- Gross calculated at **638.5 credits**; execution record shows **0 debited** and the balance is unchanged at
  6,507.92, so settlement may still be pending — **treat as unconfirmed, not free**

The volume error dwarfs the rate error. I estimated one or two postings per domain. Reality: **Vinted 108,
Housecall Pro 106, ID.me 85, Blockchain.com 64, Pushpay 61, Zuora 52** — median 20 per domain across 35
domains with any postings.

**Two rules for the skill:**

1. **Estimate a posting pull as `domains × expected postings per domain`, and assume ~20, not 1.** A
   domain-list pull against 44 known accounts is a ~1,000-row retrieval, not a ~50-row one.
2. **Require a quote before retrieval.** Origami quotes before executing, so the prompt should end with:
   *"Before retrieving anything, tell me the candidate count and the quoted credit cost, and wait for my
   go-ahead."* That converts a 20× estimation error into a question.

## Postings are historical, not live — a distinction the date fix revealed

The verbatim-date requirement worked for the first time (545 distinct dates, 2019–2026). It also exposed that
a posting pull returns **history, not current openings**: only **114 of 949** postings are inside 90 days.

**Consequence: "has a posting" and "is hiring now" are different facts.** 35 of 44 domains have some posting;
only **19** have one inside 90 days. HIR is a *live* signal and must be computed from the recent subset —
counting all 35 over-states it by 16 accounts. EST is unaffected: architecture described in a 2024
requisition is still evidence of the estate.

**Audit check: bucket posting dates by age before computing any hiring signal.**

---

# §18 — Recency windows. Raised by Rudra, and it was my fourth provenance error of the day.

## What happened

The 44-domain pull returned **four years of posting history**. I filtered HIR to 90 days and then measured
EST across **all 949 postings regardless of age.** Rudra caught it: *"I'm seeing job postings as far back as
2021, I hope that's getting contemplated."*

**Effect: EST● 22 → 16 on a 12-month window.** Six domains were qualifying on stale evidence:

| Domain | Newest pain posting | Pain postings, all time | in last 12m |
|---|---|---|---|
| Cabify | **2022-02-10** | 3 | 0 |
| Back Market | **2022-02-21** | 2 | 0 |
| fabric.inc | 2023-03-25 | 1 | 0 |
| Netradyne | 2024-03-27 | 1 | 0 |
| Minted | 2024-08-25 | 5 | 0 |
| Blockchain.com | 2024-12-02 | 4 | 0 |

**And a stale positive can invert.** A 2022 posting saying *"modernising our monolith"* is as likely to mean
the work finished as that it is ongoing — the same direction problem as Owner.com migrating *off* MongoDB.
Age does not merely weaken this signal, it can reverse it.

## The rule

> **A recency window must match the half-life of the claim the signal makes.**
>
> | Signal | Claims | Window |
> |---|---|---|
> | HIR — live infra hiring | a company is hiring **now** | **90 days** |
> | EST — named estate pain | current **architecture** | **12 months** |
> | MDB — MongoDB present | current **stack** | 12 months |
> | AGE / founding year | a historical fact | none — never expires |
>
> Different signals take different windows from the same pull. Never inherit one window across a scoring model.

12 months chosen over 24: the only domain 24 months adds is Blockchain.com, whose newest pain posting is
December 2024 with **zero** inside the year — precisely the stale case the window exists to exclude. 90 days
was rejected as too tight: it drops Zinnia, Zeta, ShiftKey and Entrata, all recent enough that the
architecture cannot have changed.

**New mark `EST⊘` — stale: pain language exists but predates the window.** Distinct from `EST○` (measured
absent across an enumerated set) and `EST⊗` (absent, thin evidence). Six accounts hold it. All three score
zero; the marks record *why*, which is the whole point of the family.

## The pattern in my four errors today

All four were the same shape: **computing on everything returned rather than on what is valid.**

1. Sole-cause on a corpus already conditioned on the filters being tested
2. Sole-cause as a marginal statistic used for a joint decision
3. Estate pain read from boilerplate — "reliability" is in 67% of postings
4. Estate pain read from four-year-old postings

**Audit check: before computing any signal, state the retrieval path AND the date range of the rows it rests
on.** Both belong in Step 1 of `sourcing-csv-audit` next to retrieval-path-per-value. The date half is new.
