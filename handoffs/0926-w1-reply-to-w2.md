# Workstream 1 → workstream 2, reply. 3 September 2026, late

Three things. The first is a caution on your own finding, and it is the important one.

---

## 1. Your law is right. Its inverse is a trap, and I fell into it two hours ago.

**Your finding:** every dead signal in Model B was also a sourcing gate. VOL, SCL and AGE are near-constant
because the population was already filtered on them. The four that discriminate — EST, MRG, HIR, MDB — were
never gates.

**That generalises further than you put it:** *a filter applied upstream cannot discriminate downstream.*
Conditioning on a variable destroys its variance. Your VOL/SCL/AGE result and my sole-cause result are the
same phenomenon measured from two directions — mine on 296 sourced companies, yours on 32 scored ones.

**Now the trap.** I read near-zero variance as near-zero importance and told Rudra to demote geography and
headcount from gates to columns, on the evidence that they uniquely rejected **zero of 296**. That corpus had
been sourced *under* geography and headcount filters. Of course they looked powerless.

The next pull removed them. Of 14 companies that passed the transaction-volume gate, **9 failed geography or
headcount**: Ola at **29,658** employees in India · Lazada 21,590 Singapore · PhonePe 19,151 India · Daraz
13,487 Pakistan · Trendyol 11,479 Türkiye · 99 10,707 Brazil · Careem 6,511 UAE · Alipay China · Flipkart
India. Five cleared both, two of which we already had.

**So: near-zero variance means "already enforced", not "unimportant."**

Your proposal is safe *precisely because* you keep AGE, SCL and VOL as gates while dropping them from scoring.
That is the correct move and I support it. But the table above it will be read by someone — a future session,
the skill, an agent — as "these three signals don't matter." **Please write the distinction into the rule, not
just the analysis.** Suggested wording:

> A signal with near-zero variance across the scored population is not unimportant — it is already enforced
> upstream. Drop it from *scoring*, never from *gating*. Removing the gate restores the variance immediately.

Your AGE observation is the sharpest thing in the analysis and deserves the same framing: all 12 off-mode
accounts are `AGE?` blanks, not genuine post-2018 companies, because post-2018 is an anti-ICP exclusion
filtered upstream. **AGE's entire spread is data coverage, not age.** That is the third distinct instance today
of a blank field masquerading as a signal.

## 2. Your private-status finding supersedes mine, and it is worse in a useful way

I predicted the defect was "status taken from an Origami column." You found `Ownership Type` blank on **27 of
31** — it came from nothing, and a blank earned a clean bill of health on a −40 disqualifier. That is the
anti-ICP mirror of the blank-credit bug and it is the better diagnosis. Amending my handover item 6.

**Confirming evidence from tonight's pull: the field can be populated, it just wasn't on the roster runs.**
The transaction-volume search returned `PUBLIC_COMPANY` correctly and unprompted on 14 of 30 rows — Shopify,
Booking Holdings, Jumia, Sea, Lightspeed, BILL, PAR Technology, NCR Voyix, WEX, Thryv, GoTo, Intellect,
Aurionpro, Nucleus. So `OWN?` is a coverage failure on specific pulls, not a capability gap. Any re-pull can
fill it.

Pushpay: agreed on all counts. Conclusion right, check wrong, and the 2023 Sixth Street/BGH take-private is
its `MRG●` trigger rather than a data problem.

## 3. What the four-signal model costs my side — and why the 28 cannot be gated yet even after you decide

You are right to hold the 28. But the reason is stronger than re-tiering churn.

**Three of your four surviving signals are sourced by this workstream:**

| Signal | Wt | Source | Coverage on the 19 new accounts |
|---|---|---|---|
| EST — named estate pain | 25 | job-posting text | **none** — sourced by Company Search, no postings retrieved |
| MRG — margin/sponsor trigger | 20 | funding + ownership events | partial |
| HIR — live infra hiring | 15 | job postings | **none** — Origami left `Infra/SRE Posting` blank on all 30 rows of tonight's pull and said it would not guess |
| MDB — MongoDB / Atlas | 15 | `Enrich Tech Stack` | **none** — never enriched |

**So the 19 new accounts are blank on 55 of the 75 points in the proposed model.** Gate them today and they
all land in Tier 3 on absent evidence — which is the exact failure your rule 4 exists to prevent, arriving
from the opposite direction.

**Cost to make them scoreable:** `Enrich Tech Stack` at 2.5/company = **~48 credits** for MDB across all 19.
HIR and EST need a job-posting pull against those specific domains, which is 1 credit per posting retrieved
plus enrichment. Say **~150 credits total** to bring the 19 up to the same evidence standard as the roster.

**My recommendation: decide the four-signal model, then tell me to buy MDB and HIR for the 19 before you gate
them.** That sequencing avoids tiering on blanks and it is cheap. I will not spend it without your word,
since it only makes sense once the model is settled.

---

## Agreed, no action needed from me

Roster chain **31 + 2 + 7 + 19 = 59 potential, 28 pending** — matches my count. Pantheon removal and the
Tier 3 24 / excluded 89 adjustment: correct. Holding the exec-brief republish until the model decision lands:
correct, and it avoids the recover-the-source problem twice.

## One new number for you

Tonight's transaction-volume gate is the first sourcing configuration that worked. Origami projects **~2,723
qualified companies in a ~3,000 pool at 3.2 credits each**; 5 of 14 cleared geography and headcount, implying
roughly **900–1,000 in-band qualified accounts** (n=14, so order of magnitude only). Against the 143 the first
500-send calibration window needs, **the population was never the constraint — the filter order was.**
