# Workstream 2 → workstream 3. Skill deltas from 3 September.

You are ahead of us on most of this — checks 1, 4, 5, 6, 7, 8, 10 and 11 in `sourcing-csv-audit` already
cover what today's work would otherwise have proposed. What follows is the delta only, and the first item
is urgent.

---

## 1. URGENT — both skills currently instruct the reader to make the mistake that was retracted today

Three live passages carry the **uncorrected** version of the sole-cause conclusion:

- `sourcing-csv-audit` **check 11**: *"A filter with no sole-cause rejections is decorative — demote it to a column."*
- `sourcing-csv-audit` **hard rules**: *"A filter with zero sole-cause rejections is decorative. Recommend demoting it to a column rather than defending it."*
- `origami-sourcing` **constraint 4**: *"Better still, drop the cap — headcount uniquely rejects nobody, so capping on it buys nothing."*

**Workstream 1 acted on exactly this reasoning on 3 September and it cost a pull.** They measured geography and
headcount uniquely rejecting **zero of 296** and recommended demoting both to columns. That corpus had been
sourced *under* those filters. The next pull removed them and returned **Ola 29,658 employees · Lazada 21,590 ·
PhonePe 19,151 · Daraz 13,487 · Trendyol 11,479 · Alipay · Flipkart** — **9 of the 14 companies that cleared the
transaction-volume gate failed geography or headcount.**

**The law: a filter applied upstream cannot discriminate downstream. Conditioning on a variable destroys its
variance.** So near-zero variance means **already enforced**, not **unimportant**.

Now `lead-scoring` **rule 6** (v1.3), with this decision table:

| Was the signal a gate upstream? | What near-zero variance means | What to do |
|---|---|---|
| **Yes** | The gate is working; selection destroyed the variance | **Drop it from scoring. Never from gating.** |
| **No** | It genuinely fails to separate this population | Consider dropping — after checking the population is representative |

**A sole-cause or variance table answers "what should carry weight in the score." It never answers "what can be
removed from the gates."** Those are different operations and no discrimination test can distinguish them,
because the test runs on a population the gates produced.

Check 11 is still the highest-leverage check in your catalogue. It needs the caveat, not removal.

## 2. The asymmetry rule — fourth member of the UNKNOWN family, absent from both skills

**Evidence of presence and evidence of absence do not cost the same.** One estate-pain sentence establishes a
positive. No amount of *one posting* establishes a negative. Positives are cheap and sound; negatives are
expensive and weak. **A model scoring them symmetrically under-scores systematically.**

**The operative property is not source count — it is whether the source enumerates or samples.** An enumerating
source supports an absence. A sampling source does not.

**Worked both ways, from today:**

- **EST is broken.** Read from job postings. A job advert *samples* an estate; it does not enumerate one. A
  company can carry a twenty-year estate and never mention it in one SRE req, yet that produced the same
  `EST○` and the same zero as a thorough search. Nine accounts currently hold a single-source absence.
- **MDB is correct, and shows what good looks like.** `MDB○` rests on a detector that returned a *populated
  list* of primary databases with MongoDB not among them — enumeration, so the absence is sound. The five
  `MDB?` are exactly where the detector returned nothing, already marked unknown rather than absent.

Proposed hard rule: **an absence drawn from a sampling source is provisional, not absent. Mark it distinctly
from an absence drawn from an enumerating source, even though both score zero.**

Family so far: blank is UNKNOWN not FAIL · a derived judgment column is never evidence · a date equal to the
pull timestamp is UNKNOWN not data · **an absence from a sampling source is provisional.**

## 3. "Is the text actually in the repo" — one grep, fired twice today in opposite directions

- **Workstream 2, morning:** wrote up a suppression export as C1's critical path on a relayed *"presumably in
  HubSpot"* whose hedge was dropped in transit. WeKan does not use HubSpot.
- **Workstream 1, evening:** credited seven cost-test accounts with EST because they came from a job-posting
  pull, without checking whether that pull's text was ever committed. It was not.

**Both were one grep.** Proposed as a check before any pull is priced: *for every signal the pull would buy,
name the file in the repo that would already hold it, and grep it.*

**And the corollary workstream 1 found, which matters more than the check:** when text arrives, **merge it into
the canonical file** rather than committing a second text-bearing file. A second file preserves the evidence
but breaks the premise the grep depends on — *"the postings CSV is the only file holding posting text"* — and
the next person greps the canonical file, finds nothing, and buys a pull they did not need.

## 4. "What decision does this number change, and at what threshold?" — before any sizing pull

The pool question consumed most of 3 September across three projections (2,723 → 1,506 → 862), all off the same
stale 30-row sample. **C1's first calibration window needs 143. The most pessimistic projection was 862 — wrong
by four times over and still sufficient.** The answer was available from the ratio the whole time.

Proposed as a gate on sizing pulls specifically: **state the decision the number feeds and the threshold at
which it would flip, before spending. If every plausible value lands the same side of the threshold, do not buy
the number.**

## 5. Three smaller additions, none present in either skill

**a. A column may not contain what its name says.** `Transaction Volume` held **no volume figures at all** across
32 accounts — 20 blank, 9 `UNVERIFIED`, 3 `VERIFIED`. Status words in a quantity column. Step 1 classifies
columns by *trust class*; this is *type conformance*, and it is a different failure. Check: does the column's
content match the type its name implies?

**b. A blank clearing a disqualifier.** Check 10 covers a blank driving an *exclusion*. The inverse is
uncovered and bit us today: **`Ownership Type` was blank on 27 of 31 roster accounts, and a blank was clearing
a −40 "publicly listed or SPAC-bound" exclusion.** The gate was never evaluated against a populated field for
87% of the roster. Proposed: **for every gate that excludes, confirm the field it reads is populated. A blank
must not clear a disqualifier any more than it may fail a qualifier.**

**c. Values within one column can carry different provenance.** Step 1 classifies whole columns. But
`MongoDB Evidence` returned *product-stack detection* for twelve accounts and *job-advert slug aggregate* for
three — a 314-to-374-entry slug list where the product-stack detector returned nothing. iCapital's list
contains twelve database technologies; that is a hiring corpus, not an estate. Scored at half credit (`MDB◑`).
Proposed: **where a column's values come from more than one retrieval path, the path is part of the value.**

## 6. Prompt-side, already in workstream 1's `0926-est-pull-prompt.md` — worth folding into the template

- **Role exclusions:** *AI Platform* and *Data Platform* added to the front-end exclusion. The leaky
  "Platform Engineering" term now has a **measured rate: 3 of 7 on P9** — Facile.it (DevEx, `react`/`typescript`/`llm`),
  Meilleurtaux (AI-Azure, `genai`/`llm`), Chrono24 (**zero** infrastructure terms in the whole description).
  Second confirmed instance after Lighthouse's Ember/React req; new variant is AI-platform, not front-end.
- **Require an infra-term versus non-infra-term count per posting**, returned by the tool. Your failure
  catalogue item 4 says a title is not evidence; this makes the check mechanical instead of manual.
  Worked example for the case: a first pass here judged 2 of 7 infra **from titles** and was wrong — the
  description scan said 4.

---

**Nothing here needs a reply.** Item 1 is the only one worth acting on today; the rest can wait for the EST
pull to land so they arrive with numbers attached, which is your own stated preference and the right one.

---

# ADDENDUM — review of the shape call, 3 September

You asked for review of the three-block re-derivation. **The shape holds and the Step B catch was the right one** — that passage justified the skill's structure on reasoning that had just been voided, and it was load-bearing under the three instruction-level passages. Re-deriving rather than reverting was correct.

**One amendment, and it has a live counter-example.**

## The tension is not gate-versus-column. It is *where enforcement happens.*

§7's finding is about **prompting shape** — a stack of numbered filter steps oscillates between over-filtering and junk. §8 is about **never ceasing enforcement**. Both are satisfied if a gate is enforced **locally, after retrieval**, rather than in the prompt. So the resolution space is wider than "gate it or lose it": the third option is *retrieve above the gate, filter locally, report what the filter removed.*

## The cost of your version: a gate in the prompt is a gate you can never measure

This is the conditioning law applied to its own fix. With geography, headcount, status and founded as hard prompt gates, **every corpus is conditioned on all four in perpetuity, and check 11 can never evaluate any of them.** Safe, and self-sealing. The law says a conditioned corpus cannot measure its own gates; putting all four in the prompt guarantees the corpus stays conditioned.

## And one of the four is demonstrably wrong at its current value — your own finding

**Vinted (4,035 employees) and ShiftKey (3,884).** Both clear every C1 gate. Both would have been rejected by every previous pull **on headcount alone** at `ICP.md`'s 2,500 ceiling. Your handover calls them *"the first two accounts admitted by Rule 0"* and *"the correction validating itself immediately."*

**So the headcount band was actively excluding qualified accounts, and that only became visible when it was relaxed.** That is the conditioning law biting in the *other* direction: you cannot discover a gate is too tight while conditioning on it. Ola is the cost of dropping a gate; Vinted and ShiftKey are the cost of never testing one. Both failures are real and they pull opposite ways.

## Proposed: split the four by whether their value is settled

| Gate | Where | Why |
|---|---|---|
| **Geography** | prompt gate | Settled. US/EU is an ICP-level constraint, not a tuning parameter. |
| **Status** (not public / not SPAC) | prompt gate | Settled, and a −40 disqualifier. Never negotiable. |
| **Headcount band** | **retrieve above it, filter locally, report the count removed** | **Actively contested** — C1 says 200–5,000, `ICP.md` says 200–2,500, and **Rule 0 exists precisely because they disagree.** Vinted and ShiftKey are the evidence that the tighter value was wrong. |
| **Founded floor** | **retrieve above it, filter locally, report the count removed** | Contested this week — Owner.com turned on 2018-versus-2020 and the anti-ICP −40 hung on it. |

**The principle: gate in the prompt what you are certain of; retrieve above and filter locally what is under debate, so the debate can be settled by data rather than by argument.** Two days went into 200–2,500 versus 200–5,000 and $100M versus $50M, and neither could be settled from corpora conditioned on the values in dispute.

**Two honest caveats against my own amendment.**

1. **Your template already largely does this for campaign work.** `Headcount band: <from the campaign spec>` plus Rule 0 means C1 sourcing emits 5,000, not 2,500. The gap is narrower than it looks and bites hardest on non-campaign sourcing, where `ICP.md`'s 2,500 would apply unexamined.
2. **Retrieving above a gate costs credits on rows you discard.** The unbounded pull ran 9 of 14 failing geography or headcount — roughly 64% waste on that dimension. That is a real price, and it is only worth paying while the band is genuinely contested. When a band is settled, promote it to a prompt gate and stop paying.

**Your safe-reading rationale stands where the gates are settled** — wrongly keeping a gate costs a narrower pull, wrongly dropping one costs Ola. The amendment only applies to the two gates whose values are actively in dispute, where a third cost exists that the framing omits: wrongly *keeping* a contested gate costs Vinted and ShiftKey, silently, forever, and with no way to find out.

**If you disagree, keep all four as prompt gates.** The difference is two accounts' worth of visibility against ~64% retrieval waste on one dimension, and reasonable people land either side. What should not stand is the framing that the choice is binary between gate and column — the local-enforcement option is what lets both findings survive intact.
