# Handover to workstream 2 — consolidated queue, 3 September 2026

Written by workstream 1 (Origami sourcing). Per §10 of `0926-handoff-origami-sourcing.md` this workstream
produces account names plus sourced facts and does not score, tier, assign cohorts, or edit roster files
and artifacts. Everything below needs workstream 2 to act.

---

## 1. Two new accounts — the first two Rule 0 unlocked

Sourced 3 September by the first C1-gated search (`data/c1scaleddigitalplatforms20260903.csv`).

| Field | Vinted | ShiftKey |
|---|---|---|
| Domain | vinted.com | shiftkey.com |
| Founded | 2008 | 2016 |
| Employees | **4,035** | **3,884** |
| Ownership | PRIVATELY_HELD | PRIVATELY_HELD |
| Total funding | $2,016,385,308 | $300,000,000 |
| Latest round | SECONDARY_MARKET | PRIVATE_EQUITY_ROUND |
| HQ | Vilnius, Lithuania | Irving, Texas, US |
| Business | Second-hand fashion marketplace | Healthcare workforce marketplace |
| Infra posting live | yes | yes |
| Origami Fit Score | 100 | 100 |

**Gate evidence — both clear every C1 gate.** Founded ≤2018 · 200–5,000 employees · Series C-or-later
equivalent capital · private, not SPAC-bound · Europe / US · marketplace with genuine company-side
transaction volume (listings and sales; shift bookings).

**Both sit at 3,884 and 4,035 employees — above `ICP.md`'s 2,500 ceiling and inside C1's 5,000.** They are
therefore the first two accounts admitted by Rule 0, and **every previous pull would have rejected them on
headcount alone.** That is the correction validating itself immediately.

**Not yet known: MongoDB / Atlas status.** Neither has been through `Enrich Tech Stack`. C1 gates on
Atlas / large cloud estate signals, so this is a gate, not just a Model B input. ~5 credits for the pair.

**No scoring attached, by design.** Note that Model B's blank-credit exposure applies: MDB, VOL and any
blank AGE must score zero under your proposed rules 4–5, not half.

---

## 2. Pantheon — reclassification, and it moves the count

**Pantheon (`pantheon.io`) is an anti-ICP disqualification, not a suppression case.** Rudra confirms WeKan
has never worked with them, so relationship suppression does not apply. The recorded reason was competitor
status — but Pantheon sells managed WordPress and Drupal hosting, and WeKan sells database modernization
consulting; they do not compete for the same work. What Pantheon *is*, is **hosting and PaaS**, an explicit
M2 anti-ICP exclusion worth −40. Its own row already carries `ACC✕` and *"anti-ICP: infrastructure vendor"*
at 35 points, Tier 3.

**Drop it as anti-ICP. Do not hold it pending a suppression check that will never resolve.**

**Count consequence — three files carry the tally.** The cohort table reads
`A 5 · B 7 · C 2 · D 15 · E 2 · suppression 1 = 32`, and Pantheon is that `suppression 1`.

| Figure | Was | Becomes |
|---|---|---|
| Qualified roster | 32 | **31** + 1 disqualified |
| Roster + cost-test new accounts | 39 | **38** |
| With Vinted + ShiftKey | — | **40** |

Files to correct: `0926-target-accounts.md` · `0926-m2-pursuit-order-snapshot.md` · the published exec brief
(recover its source with `Artifact action:"read"` first — the scratchpad that held the HTML is gone).

---

## 3. Rule 0 — and the re-screen you do NOT need to run

**Settled 3 September: when sourcing for a named campaign, the campaign's numbers govern.** `ICP.md` defines
a good-fit customer; the campaign spec defines who enters the sequence. Full statement in §"Rule 0" of
`0926-handoff-origami-sourcing.md`. Campaign gates live in the `WeKan Outbound Campaign Prioritization`
project doc.

C1's targeting gates: **200–5,000 employees · Series C+ OR $50M+ raised OR PE-owned OR
bootstrapped-profitable · private · US/EU · logistics & delivery, insurtech, fintech, marketplaces, SaaS ·
gate on Atlas / large cloud estate signals · SRE hiring OR efficiency signals.**

The roster was built at `ICP.md`'s tighter thresholds (200–2,500 and $100M+ AND Series C+).

**Checked, so you don't have to: the correction is forward-looking only.** Re-screening all 88 rejected
companies in `0926-origami-companies.csv` against C1's gates returns **6 candidates, and all 6 still fail on
other grounds** — Fluidstack and CloudLinux are infrastructure vendors, Aurora Energy Research is Research
Services, Accrete and Sonatus are outside C1's verticals, Rillet fails the age gate. **Zero** rejections sit
in the 2,500–5,000 band, because no pull ever retrieved above 2,500. **No re-screen required.**

---

## 4. MongoDB status — done for 39, with an evidence tier you must not flatten

`data/0926-mongodb-status-39-accounts.csv`. **15 of 39 present, 24 a sourced negative.** Coverage moved from
3-of-32 named to 39-of-39 determined.

**Two caveats before scoring:**

1. **Three of the 15 rest on job-posting text only** — Workrise, iCapital, OEC — not on a detected product
   stack. The `MongoDB Evidence` column carries the distinction. **Two of your eight Tier 2 promotions
   (Workrise, iCapital) rest on that softer tier**, and the promotion note treats all thirteen as equivalent.
2. **`Mid-Migration` was renamed `Co-Presence (direction UNKNOWN)`** after your Owner.com finding. MongoDB
   beside MySQL is polyglot persistence, not a migration in flight, and the direction can run either way.
   The original label was a derived judgment shipped inside a data file — my error, corrected.

Seven accounts show co-presence: iCapital, OEC, Pushpay, Zeta, Zuora, ID.me, Netradyne. Your open item 11
(the free direction check against requisition text) is the right next step on all of them.

---

## 5. Seven cost-test accounts awaiting your gates

From `handoffs/0926-costtest-graded-accounts.md`: **Origami Risk · Facile.it · Chrono24 · Mollie · OEC ·
Meilleurtaux · Capital on Tap.** Gate evidence attached per account, no scoring. Your `(later 7)` entry
correctly records these as gate-pass candidates rather than roster additions.

One rule was set to admit Capital on Tap and will recur: **for lenders and balance-sheet fintechs, a debt
round satisfies the funding gate when the amount clears the threshold** ($611M raised, latest round
`debt_financing`, which is not a "series"). Debt is a lender's growth capital. Flagged `CAPITAL-PATH: DEBT`.
Rejecting the rule systematically excludes the lending half of fintech. **Bondora is the next case** and
needs one web-research credit to settle a `Public` / `private` contradiction.

---

## 6. The public-status filter — seventh failure, and now we have the cause

Origami supplied the mechanism on 3 September, which no previous occurrence produced:

> *"Coupa scored 100 because 'Latest Round' only checked whether a value existed; it did not penalize
> `POST_IPO_EQUITY`. The business check then accepted the later private-equity acquisition."*

**Two checks disagreed and the permissive one won.** That explains the whole series — WeRide, PlusAI,
ACV Auctions, Angi, Everbridge, Monolithic Power Systems (`NASDAQ: MPWR` returned as `Private`), and Coupa.
Origami has added an explicit current-status conflict check to its saved rules.

**Consequence for the roster:** any account whose private status was taken from an Origami column rather than
verified is carrying that defect. **Pushpay** is the known live case — it came back `POST_IPO_EQUITY` and was
taken private by BGH Capital and Sixth Street in 2023, so the *conclusion* is right but the *provenance* is
the failing check. Worth a spot audit of private-status provenance across the roster.

---

## 7. Not sourcing's problem, but it blocks sends

**The C1 suppression list does not exist in the repo.** Four files instruct a check against it; no file is
it. Categories are in the campaign doc — current clients, active opportunities, Labs and design partners
(lending bank, Medora, CoE universities), active MongoDB co-sell accounts, competitors — but the account
names are presumably in HubSpot. C1's guardrail requires suppression before any send.
