# Cost-test pull — graded accounts, handover to workstream 2

**Graded:** 3 September 2026 · **Source:** `srepostingscosttestrawdata20260903.csv` (22 rows)
**Grading:** applied against ICP-M2 gates per §8 of `0926-handoff-origami-sourcing.md`. Gate evidence only —
no Model B scoring, no tiering, no cohort assignment, per §10.

## Row-to-company reconciliation

22 rows → **19 unique companies.** Alan appears 3× (one requisition, byte-identical 8,238-char description,
three LinkedIn IDs) and Kraken 2× (two distinct descriptions). **Count companies, not rows** — the row count
overstates leads by ~16%.

## Qualified — 9 companies, 7 new

| Company | Domain | Founded | Emp | Funding | Ownership | HQ | Gate evidence |
|---|---|---|---|---|---|---|---|
| Mollie | mollie.com | 2004 | 1,165 | $909.5M series_c | PE-owned | Netherlands | Payments processor. Transaction volume is the product. |
| Chrono24 | chrono24.com | 2003 | 400 | $187.1M (stage undisclosed) | VC/private | Germany | Luxury watch marketplace. Stage UNKNOWN, amount clears $100M. |
| Facile.it | facile.it | 2011 | 1,333 | PE-owned | PE-owned | Italy | Loan & insurance comparison marketplace. |
| Meilleurtaux | meilleurtaux.com | 1999 | 1,613 | series_unknown | PE-owned | France | Mortgage & insurance broker platform. |
| Alan | alan.com | 2016 | 1,542 | $1.357B series_f | VC/private | France | Insurtech. Already on roster (Tier 2). |
| FreedomPay | freedompay.com | 2000 | 595 | $32.5M | PE-owned | US | Commerce payments platform. Qualifies via PE branch, not amount. Already on roster. |
| Origami Risk | origamirisk.com | 2009 | 991 | PE-owned | PE-owned | US | Insurance risk & claims platform. Volume = customers' claims through its systems. |
| OEC | oeconnection.com | 2000 | 1,879 | PE-owned | PE-owned | US | Automotive parts commerce platform. Parts-order volume. |
| Capital on Tap | capitalontap.com | 2012 | 1,122 | $611.1M debt_financing | private | UK | SMB business credit cards. **CAPITAL-PATH: DEBT** — see rule below. |

**New to the roster (7):** Mollie · Chrono24 · Facile.it · Meilleurtaux · Origami Risk · OEC · Capital on Tap.
Alan and FreedomPay were already on the qualified 32.

**Rule set 3 September — debt financing satisfies the funding gate for lenders.** Capital on Tap raised $611M
with debt financing as the latest round, which is not a "Series C or later" and so fails the gate as literally
written. Decided: for lenders and balance-sheet fintechs, debt *is* the growth capital and they lend it out;
the gate's job is to test scale and capital access, and $611M passes both. Flag the branch as
`CAPITAL-PATH: DEBT` so it stays visible. Rejecting this rule systematically excludes the lending half of
fintech, which is where M2-shaped database estates concentrate. **This will recur — Bondora is the next case.**

## Excluded — 9 companies, with reason

| Company | Reason |
|---|---|
| Kraken (kraken.tech) | Founded 2019, fails age gate. Also Octopus Energy's platform arm → subsidiary rule. Two independent reasons. Note: this is Kraken Technologies (energy), not Kraken the exchange. |
| Indicium AI | Business consulting and services. No transaction estate of its own. |
| Strategic Link Consulting | Consultancy. Same reason. |
| OnBoard | Board-meeting and document software. Clears every firmographic gate; hits the productivity-software exclusion (P3) — user counts are not transaction volume. |
| Hack The Box | $69.5M series_b fails both the $100M amount and the Series C stage. Also security tooling. |
| Atticus | Seed stage. Fails funding gate outright. |
| Everbridge | `post_ipo_debt`, ownership Public. **Fifth consecutive pull where the public-status filter has missed a listed company.** May also be stale — Thoma Bravo took Everbridge private in 2024, same error class as Pushpay in P2. |
| Lantern | $31M secondary_market. Fails funding gate. |
| Smartcat | $28.9M series_c. Amount fails. |

## Pending — 1

**Bondora** (bondora.group, 2008, 224 emp, Estonia, P2P lending marketplace). Funding stage returned `Public`
while Ownership Type returned `private`, and Total Funding is blank. Per the standing rule a blank field is
UNKNOWN not FAIL, so it goes to the review bucket rather than being dropped. Costs 1 web-research credit to
settle. Strong ICP type fit if it resolves private.

## Data defects in this pull

1. **Kraken's funding stage disagrees between its own two rows** — `Late-stage growth / First standalone
   investment round` vs `Series D`. Derived-field self-contradiction, consistent with the measured pattern
   (60 of 65 multi-pull companies had a derived field contradict itself).
2. **Bondora's stage and ownership contradict each other** (see above).
3. **Everbridge leaked through the public filter** — fifth occurrence.
4. **Date spread is 3 days, not 90.** All 22 rows fall between 2026-08-31 and 2026-09-02 for a search
   nominally over a 90-day window. See the recency finding in `latest.md` (3 Sep, later 5).

## Model B input coverage — read before scoring these nine

Per `latest.md` (3 Sep, later 6): Model B converts blank fields to `◐` and half credit, so absent evidence
earns points. That finding applies directly here.

| Model B input | Coverage on these 9 | Detail |
|---|---|---|
| AGE (10 pts) | **9/9 populated** | 1999–2016. All clear of the 2018 boundary. Better than the roster's 14/32 blank. |
| MongoDB (15 pts) | **0/9 named** | Alan `PostgreSQL` · Meilleurtaux `BigQuery` · Facile.it the bare word `database` · six named nothing. |
| VOL (10 pts) | **0/9** | No volume column requested, by design — VOL retired as a gate (§7). |
| SCL (5 pts) | 5/9 have a funding figure | Origami Risk, Facile.it, OEC, Meilleurtaux resolve on `PE-owned` only. |

**25 of 100 points are absent — not partial — on every one of these nine.** Under the current conversion each
would collect ~12 points of `◐` for evidence that does not exist. **Do not score these until the proposed
fourth rule (UNKNOWN scores zero) is settled.** This file carries gate evidence only and no scores by design.

**The MongoDB gap is buyable and it is the cheapest high-value spend available.** `Enrich Tech Stack` at
2.5 credits/company: **~23 credits for these nine**, ~103 credits for the full 41-account roster. Converts a
15-point inference into data. For comparison, the withdrawn v3 sample would have cost ~1,560.
