# WeKan — ICP-M2 target accounts (0926)

*Written 2026-09-02 by `/lead-scoring` Model B. Reads `../../icp/ICP.md` (ICP-M2), `../../positioning/positioning.md`, `../../messaging/messaging.md`, `../../company/company.md`. Every score cites the evidence that produced it; no evidence, no points.*

**Provenance.** Derived from the September 2026 ICP-M2 sourcing trial: 120 unique companies screened across eight Origami pulls yielding 17 CSVs — two firmographic screens, one amended screen, one banded stratified sample, a transaction-evidence audit, a correction test and a trigger-first SRE sample. **31 qualified + 1 disqualified** (Pantheon, reclassified anti-ICP 2026-09-03). 400 credits. (Canonical tally, settled 2026-09-02; the 120 is a clean domain dedupe across all 17 source files and supersedes the earlier 119 and 124.) Full per-account reasoning is maintained as the ICP-M2 Pursuit Order artifact; this file is the canonical extract every downstream outbound skill reads.

> **Proof firewall.** Anonymised proof only. Use `messaging.md` §6 Pool B wording. Named clients are added by Rudra by hand; no skill assembles the pairing.

## Scoring model — Model B (ICP-M2)

| Signal | Weight |
|---|---|
| Named estate or database pain | 25 |
| Margin-scrutiny trigger | 20 |
| Live infra / SRE / DBRE hiring | 15 |
| MongoDB or Atlas presence | 15 |
| Company-side transaction volume, per-period | 10 |
| Founded 2018 or earlier | 10 |
| Scale: $100M+ at Series C+, OR PE-owned, OR bootstrapped-profitable; 200–2,500 employees | 5 |
| **Anti-ICP hit** (infra vendor · holding company · public/SPAC · founded 2019+ · confirmed refusal of production access) | **−40** |

Partial evidence scores half. **Tier 1 = 75+ · Tier 2 = 50–74 · Tier 3 = <50**, per `ICP.md`.

### Calibration note — one weighting error found by running it

The first pass treated a *predicted* production-access difficulty as an anti-ICP hit at −40. That crashed Signifyd from Tier 1 to Tier 3 on an inference, which is the mirror image of the mistake the skill's own guardrail forbids: never infer a signal to move a number, and equally never infer a *disqualifier*. The ICP's wording is "no production access **will be granted**" — a confirmed refusal, not an anticipated obstacle.

**Corrected:** the anti-ICP hit fires only on structural exclusions (infrastructure vendor, holding company, publicly listed or SPAC-bound, founded 2019 or later) or a confirmed refusal. Access difficulty is carried as a flag in the ACC column and resolved in discovery. That restores Signifyd to Tier 1 and leaves Pantheon correctly at −40 as a managed-PaaS vendor.

### Where the model disagrees with hand ranking — worth reading

- **Close scores 80 (Tier 1) against a hand rank of 29.** It has MongoDB in production, a live platform req and a 2013 founding; it was hand-ranked low only because its scale is unverified, and the model does not punish that hard (scale is worth 5). The model is arguably right that it deserves attention — it was originally filtered out of sourcing entirely because its funding row reads "seed / $250K", which is wrong for a thirteen-year-old profitable CRM. **Resolve scale and it is a genuine Tier 1.**
- **Alan scores 65 (Tier 2) against a hand rank of 4.** It has the best estate evidence on the list — a self-described Postgres monolith in a daily-deploy monorepo — but no margin-pressure trigger at all, and margin trigger is worth 20. The model is right to hold it at Tier 2. Its pain reads as velocity and data governance, not cost, which also means the entry offer's savings framing is the weaker angle for it.
- Both disagreements are informative rather than errors. Keep the score for triage and the pursuit order for sequencing judgment.

## Evidence key

`VER` industry · `AGE` founded ≤2018 · `SCL` scale · `VOL` per-period transaction volume · `EST` named estate pain · `MRG` margin trigger · `HIR` live infra hiring · `ACC` production access grantable · `MDB` MongoDB present

`●` evidence in hand · `◐` partial evidence · `○` confirmed absent · `?` **UNKNOWN — no evidence either way, scores zero** (rule 4) · `✕` known obstacle (flag, not a disqualifier) · `⊘` signal present but **direction disqualifies it** (rule 5) · `◑` signal present on a **weaker evidence tier**, half credit

`MDB●` confirmed present, direction acceptable · `MDB○` confirmed absent (a primary database was detected, MongoDB was not among it) · `MDB?` detector returned no primary database at all — absence of evidence, not evidence of absence · `MDB⊘` present but a migration *away* from MongoDB is named in the target's own words · `MDB◑` present on **job-advert slug evidence only** — the product-stack detector returned nothing, the source carries no sentences, and direction is therefore unknowable from it at any price

`●` evidence in hand · `◐` partial or inferred · `○` no evidence · `✕` known obstacle (flag, not a disqualifier)

## Scores corrected 2026-09-03 — read this before the tables

Two rules were approved and applied today, and together they moved **nine accounts down a tier**. Tier 1 went from four accounts to **one**.

- **Rule 4 — UNKNOWN scores zero.** `◐` is partial evidence, never absent evidence. Gates now carry `?` where the source field was blank, held a status word instead of a value, or carried a value the tool itself labelled unverified.
- **Rule 5 — direction-check the MongoDB weight.** Presence is not alignment. `MDB⊘` marks an account migrating *away* from MongoDB; the 15-point co-sell weight scores zero there.

**What the audit found.** `Founded Year` is blank for 14 of 32 accounts, and AGE had been paying **the full 10 points** on eleven of those blanks. `Transaction Volume` contains **no volume figures at all** across the whole roster — 20 blank, 9 `UNVERIFIED`, 3 `VERIFIED` — with the substance sitting in `Transaction Evidence Review`: **3 accounts verified per-period, 5 cumulative-only, 3 no-evidence, 1 implausible, 20 blank.** VOL is a 10-point signal evidenced for **3 of 32 accounts** (ID.me, Weee!, Zūm). MongoDB had been scoring blanks at zero correctly all along, which is why the defect read as inconsistency across signals rather than one wrong constant.

**The ranking held better than the scores.** Sensor Tower stays rank 1 under every correction. Its heavy signals are real: `EST●` from a live requisition, `HIR●` from a P1 posting with a genuine date, `MDB●` now confirmed and direction-checked. What it lost was 15 points resting on two empty columns. Sequencing judgment survives; **the numbers should not be quoted anywhere outside this repo until the verification set in open item 10 is closed.**

## Scores corrected 2026-09-03 — read this before the tables

Three passes landed today. Together they moved eleven accounts down a tier and took Tier 1 from four accounts to **one**.

- **Rule 4 — UNKNOWN scores zero.** `◐` is partial evidence, never absent evidence. Gates carry `?` where the source field was blank, held a status word instead of a value, or carried a value the tool itself labelled unverified.
- **Rule 5 — direction-check the MongoDB weight.** Presence is not alignment. `MDB⊘` marks an account migrating *away* from MongoDB; the 15-point co-sell weight scores zero there.
- **VOL is dead across the entire roster, and evidence tiers now apply to MDB.** Both below.

### VOL scores zero for all 32 accounts, and that makes it a dead signal

`Transaction Volume` holds no volume figures anywhere on the roster — 20 blank, 9 `UNVERIFIED`, 3 `VERIFIED`. The three `VERIFIED PER-PERIOD` values in `Transaction Evidence Review` were briefly credited at 10 points each. **They should not have been.** Per §7 of `handoffs/0926-handoff-origami-sourcing.md`, that column is the output of a classifier that failed three ways, the third being **fabrication: 20 of 21 rows marked "verified per-period volume" had no period phrase anywhere in the source text.** It is the canonical example behind `lead-scoring` rule 2 — *never accept a derived judgment column from the sourcing tool.* A ~95% fabrication rate cannot carry 10 points.

**VOL therefore scores 0 for every account on the list.** ID.me −10 (Tier 2 → Tier 3, which also resolves the Cohort-D-in-Tier-2 contradiction on evidence rather than by rule override), Zūm −10, Weee! −10.

**A signal that discriminates between zero accounts is not a signal.** Workstream 1 already concluded *"retire VOL as a gate"* and moved it to a discovery question on the call, which is the right home for it. Consequence for the model: **maximum achievable is now 90, not 100** (EST 25 + MRG 20 + HIR 15 + MDB 15 + AGE 10 + SCL 5). The tier thresholds were calibrated for 100, so **T1 ≥75 has silently become 83% of achievable rather than 75%.** Renormalising to the original intent (75% and 50% of 90 → thresholds 67 and 45) moves exactly one account: Metropolis Technologies 47 from Tier 3 to Tier 2. Left unrenormalised for now because the effect is one account and the tighter bar is defensible — flagged so it is a choice rather than a drift.

### MDB now has two evidence tiers, and the lower one cannot ever satisfy rule 5

Relayed from workstream 1 and verified here. `MongoDB Evidence` reads **`job postings only`** for Workrise, iCapital and — in the new cohort — OEC. For all three the product-stack detector (`Database Mentions Found`) **returned nothing**. Their MongoDB comes entirely from `Job Posting Tech Stack`, a slug aggregate of **314, 317 and 374 entries** scraped across every job advert the company has posted.

That is a materially weaker tier, for three reasons:

1. **A slug list has no sentences, so direction is unknowable by construction.** Rule 5 can never be satisfied from this source at any price.
2. **It is a hiring corpus, not an estate.** iCapital's list contains twelve database technologies — `mongodb`, `mongodb-atlas`, `mysql`, `microsoft-sql-server`, `azure-sql`, `oracle`, `amazon-dynamodb`, `postgresql`, `amazon-rds-for-mysql`, `google-bigquery`, `databricks`, `snowflake`. A "nice to have", a system being retired, a different team or a different product line all produce the same slug as a core production dependency.
3. **This is the failure the repo has already catalogued twice** — Lighthouse's `Role Match = true` on a title alone, and Chainlink Labs returning `Database Technology Mentions = oracle` because Chainlink *is* an oracle network. The standing rule is *require the verbatim sentence, not the extracted term.* A slug is an extracted term with no sentence behind it.

**Applied: `MDB◑`, half credit (7.5 of 15).** Workrise −7.5, iCapital −7.5 → **iCapital falls out of Tier 2.** `◑` rather than `?` because the slug is real data — MongoDB genuinely appears in their hiring corpus — but it cannot establish a production dependency. That is the definition of partial evidence, which is what half credit is for; rule 4 bars `◐` for *absent* evidence, not for weak evidence. The stricter reading (`?`, zero) costs Workrise and iCapital 7.5 more each and moves no further tiers.

**iCapital's co-presence flag is Tier B as well** — its `Legacy Relational: MSSQL;MySQL` comes from the same slug list. Its entire MongoDB-plus-legacy story rests on a 317-entry hiring corpus, so it should not drive a campaign without a real requisition.

**The ranking held better than the scores.** Sensor Tower stays rank 1 under every correction; its heavy signals are real — `EST●` from a live requisition, `HIR●` from a P1 posting with a genuine date, `MDB●` from product-stack detection and direction-checked. **The scores must not be quoted outside this repo until open item 10 closes.**

## Model B v2 — four signals. Approved and applied 2026-09-03.

**EST 25 · MRG 20 · HIR 15 · MDB 15. Maximum 75. Tier 1 ≥ 56.25 · Tier 2 ≥ 37.5.**

**AGE, SCL and VOL are now gates only and no longer score.** They were always gates; scoring them a second time was double-counting a decision already made upstream, and the sole-cause test below shows it bought 25 points of noise. **Removing them from scoring is not permission to relax them as gates** — `lead-scoring` rule 6, and the reason it exists.

**Tier changes: 5** — Close T2→T1, Zuora T2→T3, Carta T2→T3, Metropolis Technologies T2→T3, NexHealth T3→T2.

**Coupling condition, recorded at workstream 1's request.** The surviving four put **55 of 75 points on data workstream 1 sources** — EST from posting text, HIR from postings, MDB from tech enrichment. The model is sharper *and* more coupled to sourcing quality. Firmographic padding used to absorb a thin pull; it no longer will, so a weak run now yields empty scores rather than mediocre ones. Watch for it.

### EST is unmeasured on 22 of 31 accounts — read before using the tiers below

Workstream 1 asked whether EST's zeros are a measured absence or an unmeasured blank. **Measured 2026-09-03: unmeasured, on 22 of 31.** EST is the heaviest signal in v2 at **25 of 75 points — 33% of the model** — and it rests on evidence for **9 accounts (29%)**.

| EST provenance | Accounts | Detail |
|---|---|---|
| Positive **and traceable** | 6 | Sensor Tower · Close · Owner.com · Signifyd · Alan · NexHealth — each has a requisition in `data/0926-origami-job-postings.csv` |
| Positive but **untraceable** | 1 | **Metropolis Technologies** `EST◐`, 12.5 pts, **0 posting rows and a blank `Database Technology Mentions`** — the source of its "partial estate signal" is not recorded anywhere |
| **Measured absence** — text read, no estate pain found | 2 | FreedomPay · Lighthouse |
| **UNMEASURED, scored 0** | **22** | No posting text and no database column. Never searched. |

**The error is asymmetric and that is what makes it serious.** Those 22 are scored as though we know they have no estate pain. We do not know that — we never looked. Any one of them could carry `EST●` and gain 25 points, which in a 75-point model is a tier and a half.

**Exposure, computed:** of the 22, **3 would reach Tier 1** (Zuora, Carta, Pushpay — all 35 → 60) and **10 more would reach Tier 2** on a single unmade measurement. **Tier 1 currently holds 2 accounts. Three more could enter it without anything about those companies changing.**

**Verdict: Model B v2 ranks soundly over the 9 accounts where EST is measured, and does not rank the other 22 at all — it merely fails to score them.** v2 is not the cause: v1 carried the identical gap and simply diluted it, since EST was 25 of 100 there against 25 of 75 here. **v2 makes the exposure proportionally worse, so the model change raises the priority of fixing it rather than creating the problem.** No revert; a measurement.

**This is the fourth instance today of a blank masquerading as a value** — after AGE credit on blank founding years, VOL credit on a fabricating classifier, and a blank `Ownership Type` clearing a −40 disqualifier. The pattern is now well enough evidenced to be the thing the system is actually for.

**Consequence for the credit spend — the priority inverts.** The proposed ~150 credits went to the 19 new consolidation accounts. **The 22 unmeasured roster accounts are the better buy:** they are already gate-qualified and evidenced on MRG, HIR and MDB, so one measurement completes them, and it directly changes who gets ABM. The 19 are unevidenced on everything and would land in Tier 3 regardless. Revised order in open item 15.

## Roster re-measured against the 4 September EST pull

**949 postings across 44 domains, 689 distinct requisitions, all 44 domains returned including 9 with no postings.** The pull resolved the signal that had been blocking every decision. Full audit and the pinned term list are in the section below the tables.

**Tier 1 goes from 2 accounts to 10.** The gate was never gating on estate pain — it was gating on which nine accounts happened to have been measured. With 23 of 44 domains measured positive, it gates on the thing it names.

## Roster — EST measured, dated, and recency-windowed (4 September)

**Tier 1 is 8 accounts.** The number moved three times in two days: 4 → 2 when unearned points came out, 2 → 10 when the estate signal was finally measured, 10 → 8 when a 12-month recency window was applied to that measurement. Every move was the same discipline.

**`EST⊘` — stale.** A new mark for pain language that exists but predates the window. Four roster accounts hold it: **Zuora** (newest estate posting 2022-05-24), **Back Market** (2022-02-21), **Netradyne** (2024-03-27), **Blockchain.com** (2024-08-24, zero inside the year against 43 requisitions). It scores zero like `○` and `⊗`, and the mark records *why* — a 2022 advert saying "we are modernizing our monolith" is as likely to mean they finished as that they are still in it. Same inversion as Owner.com migrating *off* MongoDB.

## Roster — EST measured, dated, and hand-verified (4 September)

**Tier 1 is 8 accounts.** The count moved four times in two days: 4 → 2 when unearned points came out · 2 → 10 when the estate signal was finally measured · 10 → 8 when a 12-month recency window was applied · and held at 8 through a hand-read of all 15 qualifying sentences. Every move was the same discipline.

## Tier 1 — score ≥56.25  (8 accounts)

Named-account ABM. Each holds estate language dated inside the last 12 months.

| Account | Score /75 | prev | Gates | Trigger evidence | Cohort |
|---|---|---|---|---|---|
| **Sensor Tower** · `sensortower.com` | 75 | — | `VER◐ AGE? SCL◐ VOL? EST● MRG● HIR● ACC● MDB●` | **MongoDB present**; named estate pain in an open req; margin/sponsor trigger confirmed; live infra hiring; MongoDB confirmed — direction checked, neutral; `AGE?` Founded Year blank | B — sponsor mandate |
| **Pushpay** · `pushpay.com` | 75 | — | `VER◐ AGE? SCL● VOL? EST● MRG● HIR● ACC● MDB●` | margin/sponsor trigger confirmed; **legacy relational co-present**; MongoDB confirmed — **direction unverified, no requisition on file**; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | B — sponsor mandate |
| **Close** · `close.com` | 65 | — | `VER◐ AGE? SCL○ VOL? EST● MRG◐ HIR● ACC● MDB●` | **MongoDB present**; named estate pain in an open req; live infra hiring; MongoDB confirmed — direction checked, neutral; `AGE?` Founded Year blank | A — hiring trigger |
| **ID.me** · `id.me` | 65 | — | `VER◐ AGE● SCL● VOL? EST● MRG◐ HIR● ACC✕ MDB●` | access obstacle flagged; **legacy relational co-present**; MongoDB confirmed — **direction unverified, no requisition on file** · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **ezCater** · `ezcater.com` | 65 | — | `VER● AGE● SCL● VOL? EST● MRG◐ HIR● ACC● MDB●` | firmographics only — no trigger; MongoDB confirmed — **direction unverified, no requisition on file** · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Cover Genius** · `covergenius.com` | 65 | — | `VER● AGE● SCL● VOL? EST● MRG◐ HIR● ACC● MDB●` | firmographics only — no trigger; MongoDB confirmed — **direction unverified, no requisition on file** · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Metropolis Technologies** · `metropolis.io` | 60 | — | `VER○ AGE● SCL● VOL? EST● MRG● HIR● ACC● MDB○` | partial estate signal; margin/sponsor trigger confirmed; **`EST?` — the `EST◐` mark was dropped 2026-09-03: 0 posting rows, blank `Database Technology Mentions`, source untraceable. 12.5 pts removed. In the 44-domain pull.** · **re-measured by the 04-09 pull** | B — post-acquisition integration |
| **Cambridge Mobile Telematics** · `cmtelematics.com` | 60 | — | `VER● AGE? SCL● VOL? EST● MRG● HIR● ACC● MDB?` | margin/sponsor trigger confirmed; **MongoDB UNKNOWN — detector returned no primary database**; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | B — sponsor mandate |

## Tier 2 — score 37.5–56.24  (9 accounts)

| Account | Score /75 | prev | Gates | Trigger evidence | Cohort |
|---|---|---|---|---|---|
| **Zuora** · `zuora.com` | 50 | — | `VER◐ AGE● SCL● VOL? EST⊘ MRG● HIR● ACC● MDB●` | margin/sponsor trigger confirmed; **legacy relational co-present**; MongoDB confirmed — **direction unverified, no requisition on file** · **`EST⊘` stale — estate language exists but predates the 12-month window** | C — re-score as M1 |
| **Owner.com** · `owner.com` | 50 | — | `VER● AGE● SCL● VOL? EST● MRG◐ HIR● ACC● MDB⊘` | **MongoDB present**; named estate pain in an open req; live infra hiring; **`MDB⊘` — migration *away* from MongoDB named in its own requisition, co-sell weight zeroed (rule 5)** | A — hiring trigger |
| **Signifyd** · `signifyd.com` | 50 | — | `VER● AGE● SCL● VOL? EST● MRG◐ HIR● ACC✕ MDB○` | named estate pain in an open req; live infra hiring; access obstacle flagged | A — hiring trigger |
| **Carta** · `carta.com` | 50 | — | `VER● AGE● SCL● VOL? EST○ MRG● HIR● ACC● MDB●` | margin/sponsor trigger confirmed; MongoDB confirmed — **direction unverified, no requisition on file** · **re-measured by the 04-09 pull** | E — efficiency reset |
| **Housecall Pro** · `housecallpro.com` | 50 | — | `VER● AGE● SCL● VOL? EST● MRG◐ HIR● ACC● MDB○` | firmographics only — no trigger · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Wallapop** · `wallapop.com` | 50 | — | `VER● AGE? SCL● VOL? EST● MRG◐ HIR● ACC● MDB○` | firmographics only — no trigger; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Netradyne** · `netradyne.com` | 40 | — | `VER◐ AGE● SCL● VOL? EST⊘ MRG◐ HIR● ACC● MDB●` | firmographics only — no trigger; **legacy relational co-present**; MongoDB confirmed — **direction unverified, no requisition on file** · **`EST⊘` stale — estate language exists but predates the 12-month window** | D — watchlist, no trigger |
| **Alan** · `alan.com` | 40 | — | `VER● AGE● SCL● VOL? EST● MRG○ HIR● ACC◐ MDB○` | named estate pain in an open req; live infra hiring | A — hiring trigger |
| **NexHealth** · `nexhealth.com` | 37.5 | — | `VER◐ AGE? SCL✕ VOL? EST◐ MRG◐ HIR● ACC● MDB○` | partial estate signal; live infra hiring; `AGE?` Founded Year blank | A — hiring trigger |

## Tier 3 — score <37.5  (14 accounts)

| Account | Score /75 | prev | Gates | Trigger evidence | Cohort |
|---|---|---|---|---|---|
| **Civitatis** · `civitatis.com` | 35 | — | `VER● AGE? SCL● VOL? EST○ MRG● HIR● ACC● MDB○` | margin/sponsor trigger confirmed; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | B — sponsor mandate |
| **iCapital** · `icapital.com` | 27.5 | — | `VER● AGE● SCL● VOL? EST○ MRG● HIR○ ACC◐ MDB◑` | margin/sponsor trigger confirmed; **legacy relational co-present**; *job-posting evidence only*; **`MDB◑` — MongoDB appears only as one slug in a 317-entry job-advert aggregate; the product-stack detector returned nothing. Half credit, and direction is unknowable from this source** · **re-measured by the 04-09 pull** | C — re-score as M1 |
| **FreedomPay** · `freedompay.com` | 27.5 | — | `VER● AGE● SCL◐ VOL? EST○ MRG● HIR◐ ACC◐ MDB?` | margin/sponsor trigger confirmed; **MongoDB UNKNOWN — detector returned no primary database** | B — sponsor mandate |
| **Workrise (now RigUp)** · `workrise.com` | 27.5 | — | `VER◐ AGE? SCL● VOL? EST○ MRG● HIR○ ACC● MDB◑` | margin/sponsor trigger confirmed; *job-posting evidence only*; `AGE?` Founded Year blank; **`MDB◑` — MongoDB appears only as one slug in a 314-entry job-advert aggregate; the product-stack detector returned nothing. Half credit, and direction is unknowable from this source** · **re-measured by the 04-09 pull** | E — efficiency mandate |
| **Zeta** · `zeta.tech` | 25 | 50 | `VER● AGE● SCL● VOL? EST○ MRG◐ HIR○ ACC● MDB●` | firmographics only — no trigger; **legacy relational co-present**; MongoDB confirmed — **direction unverified, no requisition on file** · **`EST○` — the sole match was *"entrepreneurial legacy & excellence"*: heritage, not a legacy system. Spurious, dropped 2026-09-04** | D — watchlist, no trigger |
| **Back Market** · `backmarket.com` | 25 | — | `VER● AGE● SCL● VOL? EST⊘ MRG◐ HIR● ACC● MDB○` | firmographics only — no trigger · **`EST⊘` stale — estate language exists but predates the 12-month window** | D — watchlist, no trigger |
| **Blockchain.com** · `blockchain.com` | 25 | — | `VER● AGE● SCL● VOL? EST⊘ MRG◐ HIR● ACC◐ MDB○` | firmographics only — no trigger · **`EST⊘` stale — estate language exists but predates the 12-month window** | D — watchlist, no trigger |
| **Fleetio** · `fleetio.com` | 25 | — | `VER◐ AGE? SCL● VOL? EST○ MRG◐ HIR● ACC● MDB○` | firmographics only — no trigger; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Zūm** · `ridezum.com` | 20 | — | `VER◐ AGE● SCL● VOL? EST? MRG● HIR? ACC● MDB○` | margin/sponsor trigger confirmed · **re-measured by the 04-09 pull** | B — sponsor mandate |
| **Weee!** · `sayweee.com` | 10 | — | `VER● AGE● SCL● VOL? EST? MRG◐ HIR? ACC● MDB○` | firmographics only — no trigger · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Engine (formerly Hotel Engine)** · `hotelengine.com` | 10 | — | `VER● AGE? SCL● VOL? EST○ MRG◐ HIR○ ACC● MDB○` | firmographics only — no trigger; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Sure** · `sureapp.com` | 10 | — | `VER● AGE? SCL● VOL? EST? MRG◐ HIR? ACC● MDB?` | firmographics only — no trigger; **MongoDB UNKNOWN — detector returned no primary database**; `AGE?` Founded Year blank · **re-measured by the 04-09 pull** | D — watchlist, no trigger |
| **Lighthouse** · `mylighthouse.com` | 0 | — | `VER● AGE● SCL● VOL? EST○ MRG○ HIR○ ACC● MDB?` | firmographics only — no trigger; **MongoDB UNKNOWN — detector returned no primary database** | D — watchlist, no trigger |
| **FarEye** · `fareye.com` | 0 | — | `VER● AGE● SCL● VOL? EST○ MRG○ HIR○ ACC◐ MDB?` | firmographics only — no trigger; **MongoDB UNKNOWN — detector returned no primary database** · **re-measured by the 04-09 pull** | D — watchlist, no trigger |

## Hand-read of the 15 sentences — one spurious, and a distinction nobody had named

Workstream 1 read the qualifying sentences and found what no regex catches. **Zeta's sole match was *"founded in 2015 by two visionary leaders … whose entrepreneurial legacy & excellence has put us on top of the global fintech."* `legacy` as heritage, not a legacy system.** Dropped — Zeta 50 → 25, Tier 2 → Tier 3. Their three "thin" calls also hold: ShiftKey's is an AWS region move, EIS Group's is generic Azure CloudOps, Wallapop's is mobile-app modularisation.

### The distinction: evidence about the *candidate* is not evidence about the *company*

Reading all 15 surfaces a category the term list cannot separate. **"Experience managing technical transitions such as monolith-to-microservices" describes the person being hired. "Our .NET Framework 4.8 monolith processing billions in giving" describes the estate.** Only the second is EST evidence. The regex matches both identically.

Graded on that test:

**Company's own estate, quotable** — Pushpay *".NET Framework 4.8 monolith processing billions in giving"* · Housecall Pro *"our transition from a monolithic Ruby on Rails application toward a modern, distributed, event-driven, domain-oriented architecture"* · ezCater *"we're actively replatforming search"* · Metropolis *"driving infrastructure modernization and legacy system integrations"* · Docplanner *"help modernize our architecture"* · OfferUp *"lead platform migrations end-to-end"* · RELEX *"in 2026, this includes … gradually migrating existing deployments into the new structure"*.

**Candidate requirement, not company estate — and two are in Tier 1.** **Cambridge Mobile Telematics** (60, Tier 1): *"Experience managing technical transitions such as monolith-to-microservices, cloud migration, or major data store rearchitecture"* — a hiring specification. **Cover Genius** (65, Tier 1): its single dated sentence is *"Assist application teams to optimize queries, migrations and perform other datastore performance tuning"* — a duties list. **This qualifies workstream 1's reassurance that Tier 1 survived the hand-read untouched: six of the eight do, two rest on job-requirement language rather than a stated estate fact.** Neither is disqualifying on its own, and both hold real `MRG` and `HIR` evidence — but the first email to either cannot open on an estate claim the posting does not actually make.

## Depth grading — dropped, and the mandatory sentence replaces it

This workstream proposed grading EST by depth so a named migration would outrank a keyword hit. **Withdrawn. Workstream 1's counter-argument is better on all three counts**, and the third is decisive: **a human already reads this evidence at the right moment.** C3 requires a human-approved first touch per account, and the difference between Owner.com's named MongoDB-to-Postgres migration and a bare keyword match matters in *what the first email says* — not in a score. Grading it turns a solved workflow problem into an unsolvable scoring one. Their other two: a gate is a threshold test and must stay binary, and a hand-assigned depth grade is a **derived judgment**, the exact class this trial spent two days learning never to encode.

**Adopted instead: the quoted, dated sentence is a mandatory field on every `EST●`.**

**And the field is not only documentation — it is the detection mechanism for exactly the error above.** Zeta's heritage match and CMT's hiring-specification match are invisible behind a `●` and obvious the moment the sentence sits next to it. Had the field been mandatory from the start, both would have been caught on sight rather than by a hand-read three days later. It is the cheapest guard the roster has: it costs one column and it makes every false positive self-announcing.

## MRG provenance audit — run 4 September. 59% of its points trace to nothing, and workstream 1 was right.

**Correction to the section below, which was written yesterday and is wrong on its central claim.** It reported MRG prevalence at 35% and concluded the conditioning law did not apply. **That measured `MRG●` only. Counting any MRG credit, 28 of 31 accounts carry it — 90% prevalence.** That is the near-constant signature. **Workstream 1's conditioning hypothesis was correct; this workstream measured the wrong denominator**, which is the same error as the inverted depth metric two sections up.

### What the 28 marks rest on

| Provenance | Accounts | Points |
|---|---|---|
| A PE or sponsor fact in the committed CSV | 8 | 160 |
| The cohort assignment only, no recorded fact | 3 | 60 |
| **No traceable evidence of any kind** | **17** | **170** |
| | **28** | **390** |

**230 of 390 MRG points — 59% — rest on something other than a recorded fact.**

**And the 17 with nothing are all `MRG◐` at 10 points, every one of them a Series C, D, E or G company.** The mark was awarded for being late-stage VC-backed. **But "Series C+ or $100M+ or PE-owned" was a *sourcing gate* — every account on the roster passed it by construction.** So `MRG◐` is the capital gate re-scored under a different name, which is precisely the VOL / SCL / AGE pattern: **a filter applied upstream, paid for a second time downstream.** Sixth instance of the family.

The 8 with real provenance are genuine: `private_equity` or `PRIVATE_EQUITY_ROUND` or `POST_IPO_EQUITY` in the source data — Sensor Tower, Pushpay, Cambridge Mobile Telematics, Zuora, Civitatis, iCapital, FreedomPay, Zūm. A take-private or a sponsor round is a real margin-scrutiny event.

### The decision this forces, and its size

**Zeroing the 17 unsupported `MRG◐` marks would take Tier 1 from 8 accounts to roughly 4** — Close, ID.me, ezCater and Cover Genius all fall to 55 and out of Tier 1, and Owner.com, Signifyd, Housecall Pro and Wallapop each lose 10. **That is the second-largest tier movement of the trial and it is unresolved.** It is not applied here, because unlike the earlier corrections it is not a defect with one right answer: a late-stage VC company under board efficiency pressure genuinely *is* an M2 margin target, and `ICP.md` lists *"efficiency mandate after a funding round, layoff or profitability pivot"* as a trigger. What is missing is not the concept but the evidence that any specific account has it.

**So the fix is retrieval, not arithmetic, and it belongs to workstream 1:** for the 17, is there an actual margin event on record — an earnings-call commitment, an announced layoff, a stated profitability pivot, a public retrenchment? That is a real sourcing question. Until it is answered, `MRG◐` on those 17 should be read as **`MRG?`** — unknown, not partial — and the roster's Tier 1 count treated as an upper bound.

**Note the shape of this one, because it is the first of its kind in the trial:** every earlier defect was a blank scored as a value. This is a *sourcing gate scored as a trigger* — a real fact, correctly recorded, counted in the wrong column. Rule 6 catches it only if someone thinks to ask whether the signal was a gate. It is the argument for making that question mandatory rather than advisory.

## MRG — the sole-cause reading, from 3 September (superseded above on prevalence)

Workstream 1 flagged MRG as the next candidate for retirement: 20 points, 2 sole-cause tier changes, the profile VOL, SCL and AGE had. **Checked, and it is a different problem with a different fix.**

**Their conditioning hypothesis does not hold.** PE-ownership is both a capital gate and the sponsor-mandate trigger, so there is partial overlap — but MRG sits at **35% prevalence**, nowhere near the near-constant signature that killed the other three. VOL had *zero* variance; SCL was identical on 28 of 32; AGE's entire spread was missing data. MRG has real variance.

**What the 2 tier changes actually mean.** Renormalising the thresholds when a signal is deleted measures whether it changes the *ordering*. MRG barely does, because it is broadly distributed across the accounts that already rank highly — **72% overlap with HIR, 45% with EST**. But with thresholds held fixed, deleting MRG moves **12 accounts, including all 8 in Tier 1.** It is not idle; it is collinear.

| Signal | Weight | Prevalence | Sole-cause changes | Reading |
|---|---|---|---|---|
| EST | 25 | 42% | 14 | Independent and decisive |
| MDB | 15 | 32% | 6 | Independent, punches above its weight |
| HIR | 15 | 68% | 3 | Broad; overlaps MRG at 72% |
| MRG | 20 | 35% | 2 | **Collinear with HIR, not absent** |

**So the sole-cause test answers "does this change the ranking", never "is this doing work."** A collinear signal scores low on it while carrying points every top account depends on. Worth adding to `lead-scoring` rule 6 as the test's stated limit — it is the same shape as the rule itself, one level in.

**The real open question on MRG is provenance, not weight.** Twenty-eight accounts carry `MRG●` or `MRG◐` and the recorded evidence for most is the phrase *"margin/sponsor trigger confirmed."* That is the same unrecorded provenance flagged against Sensor Tower on 3 September and never resolved. **Before re-weighting MRG, establish what those 28 marks rest on** — it is a 20-point signal whose evidence has never been audited, and the trial's entire yield says that is where the next defect will be.

## The recency rule — a window must match the half-life of the claim

Workstream 1's finding, 4 September, and it is the most transferable rule the trial has produced.

**A recency window must match the half-life of the claim the signal makes.**

| Signal | What it claims | Window |
|---|---|---|
| `HIR` | hiring **now** | 90 days |
| `EST` | **current** architecture | 12 months |
| `MDB` | **current** stack | 12 months |
| `AGE` | a historical fact | none |

**Different signals take different windows from the same pull.** One window was inherited across a whole model, which is how a 2022 job advert ended up qualifying an account in 2026.

**Why 12 months and not 24 or 90.** At 24 months the only account added is Blockchain.com, whose newest estate posting is August 2024 with zero inside the year against 43 requisitions — precisely the case the window exists to catch. At 90 days it drops Zeta, ShiftKey and ESW, all recent enough that the architecture cannot plausibly have changed.

**Effect: EST● falls from 22 to 15 across the 44 domains, and Tier 1 from 10 to 8.** Four roster accounts move to the new `EST⊘` mark.

### Our two counts differed by one account, and the one account was a Tier 1 seat

Workstream 1 measured 16, this workstream 15. **The entire difference is the `cost optimisation` term**, and it decides **Zuora** — which sat at 75 in Tier 1.

With the term in, Zuora has 6 recent qualifying postings on lines like *"drive initiatives for cost optimization, performance tuning, and system hardening."* With it out, Zuora has **zero** inside the window and its newest genuine estate language is from **May 2022**.

**The term stays out, and the reason settles it independently of taste: Zuora already holds `MRG●` at 20 points for exactly this evidence.** ICP-M2 separates the two explicitly — the estate marker is *"MVP-era core: MSSQL/MySQL/Postgres monolith from the founding era now throttling releases"*; the margin trigger is *"infra spend growing faster than revenue, cloud bill a standing board topic."* Cloud FinOps is the second one. Counting it in EST as well pays 45 points for one piece of evidence, which is the double-count the four-signal rebuild exists to prevent. Same for Zinnia and Entrata, the other two domains the term would have added.

## The EST pull — audit, and the term list pinned

**Delivered 4 September: 958 rows, 949 postings, 44 of 44 domains returned, 9 with an explicit no-posting row.** Every audit claim from workstream 1 was independently reproduced here.

| Check | Result |
|---|---|
| Date field | **Fixed — first time in the trial.** 545 distinct dates spanning 2019-11-07 to 2026-09-03. The retrieval-date defect is absent. |
| Requisition duplication | **27.4%** — 949 rows, 689 distinct requisitions. Confirms the single Alan case was not an outlier. |
| Role filter | **2.7% leaky**, down from 43%. The AI-platform and data-platform exclusions worked. |
| MongoDB, free second source | Named in posting text on 6 domains — Workrise, ESW, Cover Genius, Docplanner, Housecall Pro, Zinnia. |

### The pull returned four years of history, not live openings — and HIR had to change

**Only 111 of 949 postings fall inside 90 days.** "Has posted an infrastructure role" and "is hiring one now" are different facts, and ICP-M2 defines the trigger as *live* hiring, posted ≤90 days.

**19 domains have live infra hiring · 16 have history but nothing current · 9 have none.** Scoring HIR on any retrieved posting would have credited 16 accounts with 15 points they have not earned — iCapital, Workrise, Zeta, Engine and FarEye among them. **HIR is now computed from recent postings only.** EST is unaffected: architecture described in 2024 is still evidence about the estate.

### The definition of "named estate pain", pinned as an exact term list

Three independent measurements disagreed by up to 12×, entirely on wording. Reconciled by measuring prevalence of every candidate term across all 949 postings and discarding anything that cannot discriminate:

**Discarded as boilerplate** — `reliability` 67% of postings · `observability` 38% · `on-call` 31% · `incident` 23%. A term present in two-thirds of a corpus is standard SRE vocabulary, not a company describing its estate. Same rule that retired the headcount rejection rate.

**Discarded as belonging to another signal** — `cost optimisation`. It is the **margin** trigger, not the estate signal. Leaving it in had EST double-counting MRG, which is the redundancy the sole-cause work exists to remove. Costs two domains.

**The pinned list, nine terms:** `migrat*` · `monolith*` · `legacy` · `technical debt` / `tech debt` · `re-architect*` · `replatform*` / `re-platform*` · `moderni[sz]*` · `decompos*` · `shard*`

**Result: EST● on 23 of 44 domains.** Once the term lists were aligned the three measurements landed at 22, 23 and 25 — within two domains. **Workstream 1's structural argument settled the design question and it was right: requiring a named database inside EST collapses EST into MDB**, which already carries 15 points on its own detection path.

### Frequency is not evidence — a metric built here inverted its own ranking

A first attempt graded EST depth by *what share of a company's postings mention estate work.* It ranked **Vinted "thin" at 3%** — on the strength of *"Scaling database clusters (Vitess, MySQL) by introducing new sharding strategies,"* which is the single most specific estate sentence in the entire corpus — while grading a company "substantive" at 90% on *"our platform saw only 6 minutes of downtime."*

**Rate measures how infrastructure-flavoured a hiring corpus is, not how strong the estate evidence is.** A large employer names its monolith in 3 of 67 adverts; a small one repeats a reliability line in 9 of 9. The repo's own rule — *the verbatim sentence, never the extracted count* — applies to metrics built here just as much as to columns arriving from the tool. Third time in two days the rule has caught its own author.

**Consequence: EST carries no depth grading, and it should.** Owner.com's `EST●` is a named MongoDB-to-Postgres migration in a senior requisition read by a human. Several new Tier 1 entrants hold a single keyword match in a long corpus. **Both score 25.** MDB already grades its positives by source (`MDB●` product-stack versus `MDB◑` job-advert slug); EST needs the same treatment, graded on the specificity of the strongest sentence rather than the frequency of any. **Proposed, not applied** — it needs a human pass over 23 sentences, which is cheap but is not a regex.

### Sole-cause test re-run on the measured roster

Workstream 1's caveat was that if Tier 1 landed above ~8 the weight should be revisited. It landed at 10. **The test says the weight is not the problem.**

| Signal | Weight | Prevalence of `●` | Sole-cause tier changes |
|---|---|---|---|
| **EST** | 25 | 58% | **9** — still the strongest discriminator on the roster |
| MDB | 15 | 32% | 7 |
| HIR | 15 | 68% | 3 |
| **MRG** | 20 | 35% | **2** |

**EST survives its own test.** The weaker signal is now **MRG at 20 points for 2 tier changes** — the next candidate for the treatment VOL, SCL and AGE received, and the thing to watch as the 28 pending accounts are gated.

### Cohort still overrides tier for sequencing

**MongoDB presence is a Fit signal, not an Intent signal.** `ICP.md` is explicit that Intent is 30 of 100 and that firmographic-first sourcing scores zero on it by construction. **After today's corrections no Cohort D account remains in Tier 2** — ID.me was the last one and fell to Tier 3 on the VOL correction, which is the better outcome: resolved on evidence rather than by overriding the tier.

**Rule, unchanged: cohort governs motion, tier governs attention.** The tier tables are a triage ranking, not a send list. Zuora and iCapital remain Cohort C and route to the M1 re-score — and their MongoDB-plus-legacy co-presence is a stronger M1 shape than M2, with the caveat that iCapital's rests on slug evidence only.

## MongoDB enrichment — arrived and audited 2026-09-03

**Source:** `0926-enrich-targets-enriched-raw.csv` (39 rows, 9 columns) and `0926-mongodb-status-39-accounts.csv`. Covers the 32 plus 7 net-new accounts from workstream 1's cost test. This closes open item 2 — the ~80-credit Enrich Tech Stack pull described there as "highest value per credit available".

**Result: 13 of 32 confirmed MongoDB present, 14 confirmed absent, 5 UNKNOWN.** The three accounts this file already claimed MongoDB for — Sensor Tower, Owner.com and Close — are all **confirmed**. The top of the list was right.

**Zero accounts entered Tier 1.** Eight promoted Tier 3 → Tier 2. The highest-weighted unscored signal in Model B, filled in across the whole roster, did not change who gets named-account ABM.

### Four audit findings — read before using the column

**1 · Five "no" values are UNKNOWN, not no.** The detector returned **no primary OLTP database whatsoever** for Cambridge Mobile Telematics (only `Databricks`), Lighthouse (only `Elasticsearch`), FreedomPay (`Redis;Snowflake`), Sure (empty) and FarEye (empty). No operating company has no database. Four of the five show `Database Mentions Found` empty — the detector produced nothing, which is a null result, not a negative. Recorded as `MDB?`. **The score is unaffected either way** — absent and absent-evidence both score zero — but the provenance record must not say "no MongoDB" as a fact.

**2 · `Mid-Migration` is inference, not detection, and its name asserts a direction the data cannot support.** The flag is derived: MongoDB detected AND legacy relational detected. Six accounts in the 32 — Pushpay, Zeta, iCapital, Zuora, ID.me, Netradyne. But MongoDB alongside MySQL is **polyglot persistence**, the normal state of any ten-year-old platform. It is equally consistent with a migration in flight, a migration that stalled, a migration that finished and left legacy running, or two teams that never spoke. Per the standing rule against derived judgment columns, the flag is **renamed to co-presence** in the tables above: `legacy relational co-present`. The signal is real and valuable — ICP-M2's technographic marker is a founding-era relational core *plus* a MongoDB footprint, and co-presence hits both — but it needs the direction established before it drives a campaign.

**3 · Direction is not academic. Owner.com is migrating *off* MongoDB.** From its own Staff Database Engineer requisition, already committed in `data/0926-origami-job-postings.csv`: *"Deep expertise with a major relational engine (**Postgres strongly preferred**) in high-volume production; experience migrating workloads (e.g., **MongoDB → Postgres**) a strong plus"*, alongside *"Lead the migration of product workloads"* and *"zero-downtime migrations on large, live tables"*. **This is a Model B design flaw, not a data error.** The MongoDB signal is worth 15 points as a co-sell path, but it is direction-agnostic: it pays the same whether an account is adopting MongoDB or retiring it. Owner.com collects 15 points for a footprint it is actively shrinking, at the account where WeKan's MongoDB credential is the *weakest* opening rather than the strongest. The ABM plan already frames the requisition correctly; the score does not. **Proposed: MDB scores 15 only where direction is toward MongoDB or neutral, and 0 where a named migration away from it exists.** Zero credits to check — the requisition text is already in the repo for every account in the postings CSV.

**5 · Direction check run across all 13 MongoDB accounts — coverage is 3 of 13, and it found exactly one reversal.** The committed postings CSV holds requisition text for only three of the thirteen, because the other ten were sourced from the scale-led and firmographic pulls rather than the hiring-led one. Result: **Owner.com — migration away, confirmed** (`MDB⊘`, −15). **Sensor Tower — MongoDB named in its Platform Engineer req, no migration sentence → neutral, keeps 15.** **Close — MongoDB named in its Senior Backend Engineer req, no migration sentence → neutral, keeps 15.** The remaining ten have **no requisition on file, so direction is unverified** and they keep their presence score per rule 5's scope note. The check was worth running for free — it converted two accounts from assumed-neutral to checked-neutral — but it cannot reach the ten that matter most for the co-presence story. **Request to workstream 1: a Job Posting Search for the ten (Workrise, Pushpay, Zeta, iCapital, Carta, Zuora, Cover Genius, ID.me, Netradyne, ezCater), 1 credit per posting.**

**The direction check on the co-presence accounts is not free — measured, 2026-09-03.** Workstream 1 relayed that the text is in the repo. It is not, for these accounts. Verified against both source files: **none of the six co-presence accounts (Pushpay, Zeta, iCapital, Zuora, ID.me, Netradyne) has a row in `data/0926-origami-job-postings.csv`**, and five of the six have a **blank** `Job Posting Tech Stack` in the enrichment file as well — so there is no job-posting data of any kind for them, prose or slug. iCapital has only the 317-slug aggregate, which contains no sentences. The 36 rows of full requisition text in the postings CSV all belong to the hiring-led pulls; every co-presence account came from the scale-led and firmographic pulls, which carry no postings. **Direction for this set costs credits. The zero-cost check is already exhausted at 3 of 13.** The Owner.com case shows a false positive here is worth 15 points on a hostile signal.

**4 · The detector has measurable false negatives.** `Databases Detected` for Owner.com is `MongoDB;Snowflake` — Snowflake is a warehouse, so the entire detected OLTP estate is MongoDB. Yet Postgres is named verbatim in Owner.com's own open requisition as the preferred engine. **The detector missed a database the company advertises.** That downgrades confidence in every `MDB○` and in every blank `Legacy Relational`, including the six co-presence calls above: some of the fourteen "confirmed absent" may be the same miss in the other direction.

### The seven net-new accounts are not scored

Origami Risk · Facile.it · Chrono24 · Mollie · OEC · Meilleurtaux · Capital on Tap. Two carry MongoDB — **OEC** (`MSSQL;MySQL` co-present, job-posting evidence only) and **Capital on Tap**. None has been through the M2 gates: no VER, AGE, SCL, VOL, EST, MRG or HIR evidence exists for any of them. Per the workstream interface rule, account names plus sourced fact columns are accepted from sourcing and **scoring happens here** — so these seven enter as candidates for a gate pass, not as roster additions. OEC is the one worth looking at first on co-presence.

## Entry point — identical for every account

**Fixed-fee 2-week estate assessment**, savings quantified against real workload data. M2 has exactly one entry offer; everything past it is expansion. Proof point selection is per account, from two only:

- **Estate cost & sprawl** → `messaging.md` §6: global on-demand delivery platform (logistics) — $1M annual infrastructure savings, 30–90% cost reduction per cluster, zero downtime
- **Velocity & monolith** → `messaging.md` §6: US homeowner's-insurance platform — 90% faster launch (2 weeks → 5 minutes), 2× developer velocity, 3× query performance

Second proof point applies to: Owner.com · Alan · Sure · Cover Genius · NexHealth · Cambridge Mobile Telematics · Housecall Pro. First applies to the rest.

**Audience framing** from `messaging.md` §5 — CTO/CIO: de-risked modernization, one accountable partner, measurable ROI. VP Engineering / Platform: architecture-first, faster cycles, no lost context.

**Avoid** (`messaging.md` §7): "database modernization partner", MongoDB-only framing, generic digital transformation. MongoDB mastery is a differentiator inside a broader story, never the story.

## Disqualified — anti-ICP hits and structural exclusions

Eighty-nine of the 120 screened companies were excluded — 88 at screening plus Pantheon, reclassified 2026-09-03. Reasons cluster, and each cluster is a filter the next sourcing run should apply rather than a judgment to repeat by hand.

**Infrastructure vendors — suppliers, not prospects** — Temporal · CData · Port.io · Hydrolix · Fluidstack · Skyflow · CloudLinux · Tines · WEKA · AntemetA · Chainlink Labs · InterSystems · Supabase · Collibra · Movu Robotics · ACS

Their customers are ICP-M2. Deepest in-house platform benches, lowest winnability, and in some cases competitors.

**Pantheon — reclassified 2026-09-03 from "suppression check first" to a straight anti-ICP disqualification, and removed from the roster.** Rudra confirms WeKan has never worked with them, so relationship suppression does not apply. The recorded reason had been competitor status, which does not hold either: Pantheon sells managed WordPress and Drupal hosting, WeKan sells database modernization consulting, and they do not compete for the same work. What Pantheon **is** is hosting and PaaS — an explicit M2 anti-ICP exclusion at −40. It scored 55 on signals before the penalty, 15 after. **Do not hold it pending a suppression check that will never resolve.** Its former row: `VER○ AGE? SCL● VOL? EST● MRG◐ HIR● ACC✕ MDB○`, cohort "suppression check first" — that cohort is now empty.

**No single estate, no single margin owner** — Red Ventures · Telia Cygate · E.ON Software Development · HCLTech Germany · Neotalent Conclusion · Commerzbank Digital Technology Centre Bulgaria

Portfolio and holding companies operating independent brands, and subsidiaries whose buying committee sits at the parent.

**Wrong deployment model** — Litera

Document software deployed inside Microsoft 365 and Google Workspace. High user counts there do not indicate a cloud database estate.

**No buying committee** — Weights & Biases

Acquired by CoreWeave (~$1.7B, closed). Selling cloud-cost optimisation into a cloud provider's subsidiary runs backwards.

**Publicly listed or SPAC-bound** — WeRide · PlusAI · ACV Auctions · Angi

The ICP stops at pre-IPO.

**No MVP era to modernise — founded 2019 or later** — Vertice · Hebbia · Wispr Flow · Rillet · Accrete · Ambient.ai · David AI · Unify · Labelbox · Vanta · osapiens · Atlan · Hadrian · K2 Space

"MVP-era architecture now taxing margins" is a claim about elapsed time. Greenfield infrastructure has nothing to unwind.

**Production access is a non-starter** — Peregrine

Government and public-safety data platform. Assessment-by-hearsay fails — an explicit ICP disqualifier, distinct from the access *flags* carried in Tier 1.

**Estate too small or wrong shape** — Brainly · First Due · Kantata · Envoy · LumApps · Uberall · Trackforce · Luminance · onXmaps · Laravel · Vimeo · Intercom · Showpad · Salsify · Fullstory · Mural · Simpplr · Accela · H1 · FSP

Records-management and workplace software at low write volume, consultancies, or read-heavy content platforms where per-cluster savings cannot fund a program.

## C1 is not blocked by the model — and it is not addressable at 40 either

Workstream 1's point, 3 September, and it is the most useful thing said all day: **the four-signal model produces T1 2 · T2 4 · T3 25. It is not ranking the roster, it is picking about six accounts.** That is a legitimate output and the right instrument for **C3** — trigger-gated ABM, 10–15 named accounts a week, human-approved first touches. **It is not the instrument for C1.**

**C1 is a volume campaign: 25–40 contacts a day, email-led to CTO/VP Eng, autonomous sends, calibrated over the first 500 sends. It sends to a cohort, not to a tier.** Tier order is not how a volume sequence chooses who to email. So the four-signal decision unblocks this workstream's gating queue; **it was never what blocked C1.**

### But the addressable number is 23, not 40

Workstream 1 counts 40 gate-qualified accounts and calls it "more than a week of sending." **Gate-qualified is not in-market**, and C1's own gates say *"SRE hiring OR efficiency signals."*

| Cohort | Count | C1-eligible? |
|---|---|---|
| **A** — hiring trigger | 5 | Yes — SRE hiring |
| **B** — sponsor mandate | 7 | Yes — efficiency signal |
| **E** — efficiency mandate | 2 | Yes — efficiency signal |
| C — reclassify as ICP-M1 | 2 | **No** — wrong ICP |
| **D** — watchlist, no trigger | **15** | **No** — no trigger of any kind |

**All 15 Cohort D accounts carry `HIR○ MRG◐ EST○`.** Not one has a live trigger; `MRG◐` is inferred margin pressure, which is why they were put on a watchlist rather than in a sequence. Adding the 2 C1-cleared accounts and the 7 cost-test accounts — both groups sourced from infra-posting pulls, so both carry the trigger by construction — gives **14 + 9 = 23 C1-addressable accounts today.**

**Emailing the 40 would put 15 no-trigger accounts into an autonomous volume send** on the strength of firmographic fit alone. That is the activation rule broken (one ICP × one trigger × one offer), and it is the same error in a third costume: absent evidence treated as a green light.

At 25–40 contacts a day, 23 accounts at two to three contacts each is **roughly one to two days of sending, not a week.** Enough to start. Not enough to reach the 500 sends the calibration window needs, which is an argument for continuing to source — not for emailing the watchlist.

### Suppression is not a blocker — checked 2026-09-03, and the "HubSpot export" framing was wrong

**Correction.** Workstream 1's handover said the suppression names were *"presumably in HubSpot"*; that hedge was dropped in transit and the export was written up here as C1's critical path. **WeKan does not use HubSpot** (Rudra, 3 September), so the critical path never existed.

**A suppression list effectively already exists: `messaging.md` §6 Pool A**, the ten cleared client names. Cross-checked against all 40 candidate accounts — the 31 roster plus Vinted, ShiftKey and the seven cost-test accounts:

**Zero matches, and the overlap is structurally impossible.** Pool A is Royal Caribbean · Cox Automotive · Amadeus · 7-Eleven · Davita Clinics · Allianz · Cathay Pacific · Standard Bank · Kaiser Permanente · Stanley Black & Decker — Fortune 500 enterprises across cruise, automotive, aviation, retail, dialysis, insurance, airline, banking, healthcare and power tools. **That is an ICP-M1 population: large legacy estate owners.** The roster is ICP-M2: growth-stage digital platforms, $50M–$1B, 200–5,000 employees, VC- or PE-backed. **The two ICPs cannot overlap by construction**, which is why the check returns nothing and would keep returning nothing as the roster grows.

**Consequence: C1 has no remaining blocker.** Not the model, not the credit spend, not suppression. Workstream 1's point lands in full — *"two days sourcing for a campaign that had enough accounts to start on day one"* — and the accounts were there on day one. **C1 is addressable at 23 today.**

**Residual hygiene, not a blocker.** Four repo files instruct a check against a suppression file that does not exist. The fix is to point them at `messaging.md` §6 Pool A plus the campaign doc's categories, or to write a thin file that does so — one pass, no external dependency. Worth doing before an autonomous send runs, because an instruction pointing at nothing reads as an unperformed check.

**The one number that would settle the volume-versus-ABM question is still a reply rate nobody has measured.** Every estimate in this file — the 40-to-800 interval, the ~900–1,000 projection — is a population estimate. None of them says whether the message works. The first 500 sends produce that number and no amount of scoring will.

## Sole-cause test on Model B — run 2026-09-03, and three of seven signals are noise

Requested by workstream 1, which had measured sole-cause rejections across 296 companies and found that **headcount, geography and capital uniquely rejected nobody** — company type did essentially all the discriminating. Their question: does the same hold inside Model B, where SCL is 5 points and AGE is 10?

**Method note, because the naive version of this test is misleading.** Deleting a signal lowers every score, so with thresholds held fixed a heavy signal looks important merely by being heavy. The test below deletes each signal *and* renormalises the tier thresholds to the same proportion of the new achievable maximum (75% and 50%), which isolates discrimination from weight. Both versions are recorded; the renormalised one is the answer.

| Deleted signal | Weight | Modal value | Accounts off the mode | Sole-cause tier changes |
|---|---|---|---|---|
| **EST** named estate pain | 25 | 0 on 24/32 | 8 | **14** |
| **MRG** margin trigger | 20 | 10 on 18/32 | 14 | **7** |
| **HIR** live infra hiring | 15 | 0 on 24/32 | 8 | **7** |
| **MDB** MongoDB, direction-checked | 15 | 0 on 20/32 | 12 | **6** |
| AGE founded ≤2018 | 10 | 10 on 20/32 | 12 | 3 |
| SCL scale | 5 | **5 on 28/32** | 4 | **1** |
| VOL transaction volume | 10 | **0 on 32/32** | **0** | **0** |

> ### Read this before acting on the table above
>
> **Near-zero variance means "already enforced", not "unimportant."** Every signal below that fails to discriminate does so *because a gate upstream already removed the accounts that would have varied on it.* The table says what should carry weight in the **score**. It says nothing about what can be relaxed in the **gates**, and no discrimination test ever can, because the test runs on a population the gates produced.
>
> **Worked example, from workstream 1 the same day, at the cost of a pull.** Their sole-cause analysis over 296 sourced companies showed geography and headcount uniquely rejecting **zero**, and the recommendation was to demote both to columns. That corpus had been sourced *under* those filters. The next pull removed them and returned **Ola at 29,658 employees, Lazada 21,590, PhonePe 19,151, Daraz 13,487, Trendyol 11,479, Alipay, Flipkart** — **9 of the 14 companies that cleared the transaction-volume gate failed geography or headcount.** The filters looked powerless precisely because they were working.
>
> The proposal below is safe **only because it keeps AGE, SCL and VOL as gates while dropping them from scoring.** Those are two different operations. Now written into `lead-scoring` as rule 6.

### The answer: workstream 1 was right about SCL and VOL, wrong about AGE — and then more right than their own test showed

- **VOL is provably noise.** Zero variance: every account scores 0. A signal with one value cannot separate anything. Already established from the evidence side; this confirms it from the model side.
- **SCL is very nearly noise.** **28 of 32 accounts score the identical 5 points.** One sole-cause tier change in the whole roster (Close). At 88% modal it is a constant with rounding error attached.
- **AGE looks like it discriminates, and it does not.** Three sole-cause tier changes, 12 accounts off the mode — but **all 12 are `AGE?`, blank `Founded Year`. Not one is a genuine 2019-or-later account**, because founded-2019+ is an anti-ICP exclusion and was filtered out at sourcing. **AGE's entire spread is data coverage, not age.** Verify the 12 blanks and every account resolves to ≤2018, AGE becomes a constant 10, and its variance goes to zero alongside SCL and VOL.

### The generalisation, which is the part worth keeping

**Every one of the three dead signals was also a sourcing gate.** VOL was the company-side-volume qualifier. SCL was the 200–2,500 / $100M+ / Series C+ gate. AGE was the founded-≤2018 gate. The filtering happened upstream, so the surviving population is near-constant on all three by construction — **Model B is re-scoring decisions already made, and paying 25 of 100 points for it.**

The four signals that do discriminate — EST, MRG, HIR, MDB — are precisely the four that were **not** gates. They are trigger and technographic evidence discovered *after* the population was fixed. That is the same shape as workstream 1's finding one level up: the filter that did the most damage did the least work.

**Proposed revision, not applied — this is a model change and needs Rudra.** Reduce Model B to the four discriminating signals (EST 25 · MRG 20 · HIR 15 · MDB 15, max 75, thresholds 56.25 / 37.5) and treat AGE, SCL and VOL as **gates only**, which is what they already are. On the current 31-account roster that moves five accounts: **Close 65 → Tier 1** (which finally settles the model-versus-hand-ranking disagreement recorded above, in the model's favour), NexHealth into Tier 2, and Zuora, Carta and Metropolis down to Tier 3. Tiers become T1 2 · T2 4 · T3 25.

**Condition to record if the four-signal model is approved (workstream 1, 3 September).** The surviving four put **55 of 75 points on data workstream 1 sources** — EST from posting text, HIR from postings, MDB from tech enrichment. **The model gets sharper and simultaneously more coupled to sourcing quality.** Firmographic padding used to absorb a thin pull; it no longer will, so a weak sourcing run now degrades scoring directly. That is a fair trade and it must be written down, because the failure mode changes shape: under the old model a thin pull produced mediocre scores, under the new one it produces empty ones.

**Do this before gating the 28 pending accounts, not after** — but re-tiering churn is the lesser reason. **The real blocker is evidence coverage, and workstream 1 supplied it.** Three of the four surviving signals are sourced by that workstream, and the 19 consolidation accounts have none of them:

| Signal | Wt | Source | Coverage on the 19 |
|---|---|---|---|
| EST | 25 | job-posting text | **none** — sourced by Company Search, no postings retrieved |
| MRG | 20 | funding and ownership events | partial |
| HIR | 15 | job postings | **none** — Origami left `Infra/SRE Posting` blank on all 30 rows and declined to guess |
| MDB | 15 | `Enrich Tech Stack` | **none** — never enriched |

**The 19 are blank on 55 of the proposed 75 points.** Gating them today puts every one in Tier 3 on absent evidence — rule 4's failure mode arriving from the opposite direction, and the reason rule 4 exists.

**Sequencing, agreed with workstream 1:** settle the four-signal model → authorise ~150 credits (~48 for `Enrich Tech Stack` across the 19, the rest a posting pull against those domains for HIR and EST) → *then* gate. Workstream 1 will not spend it without the model decision, because the spend only makes sense once the four signals are locked.

## Private-status provenance audit — run 2026-09-03, and the defect is the opposite shape

Requested by workstream 1 after Origami supplied the mechanism behind the seven-occurrence public-status failure: *"'Latest Round' only checked whether a value existed; it did not penalize `POST_IPO_EQUITY`. The business check then accepted the later private-equity acquisition."* Two checks disagreed and the permissive one won. Their conclusion: any account whose private status came from an Origami column rather than a verification carries the defect.

**Measured across all 31 roster accounts, the finding is worse than that and a different shape. `Ownership Type` is blank for 27 of 31.** For those accounts the private status did not come from an Origami column at all — **it came from nothing.** The anti-ICP exclusion "publicly listed or SPAC-bound", worth −40, was never evaluated against a populated field for 87% of the roster.

This is the anti-ICP mirror of the blank-credit bug closed earlier today. There, a blank field earned scoring credit. Here, a blank field earns a **clean bill of health on a disqualifier**. Same root cause: absent evidence treated as a settled answer.

### Graded, so the exposure is legible rather than alarming

| Provenance tier | Accounts | Status |
|---|---|---|
| `Ownership Type` populated | 3 — Alan (`VC/private`), FreedomPay (`PE-owned`), Lighthouse (`VC/private`) | Sourced |
| Positive post-IPO marker | 1 — **Pushpay** (`POST_IPO_EQUITY`) | **Verified 2026-09-03** |
| No evidence of any kind | 1 — **Engine** (Ownership Type, Funding Stage *and* Total Funding all blank) | **Verified 2026-09-03** |
| Indirect only: a private-market `Funding Stage` | 26 | Inference, not verification |

**Both accounts carrying real risk are now verified private.**

- **Engine** — the only roster account with no provenance whatsoever. Crunchbase: **private, Series C, Permira lead**, three rounds, Denver. Clean.
- **Pushpay** — the known case, and the field that should have caught it is the one that didn't. Verified: listed on the **NZX in 2014**, on the **ASX from 12 October 2016 as `PPH`**, and **delisted from both in May 2023** on acquisition by Sixth Street Partners and BGH Capital. Private since. The conclusion on the roster was right; the check that produced it was not. Its `MRG●` sponsor-mandate trigger *is* that take-private, so the account is internally consistent.

**Net: no roster account is currently public.** The gate's conclusions hold; its enforcement does not. The 26 inference-only accounts are low risk — a company closing a Series E or a private-equity round is not listed — but that is reasoning from a different field than the gate names, and it should be recorded as inference rather than passed off as a check.

**Recommended, cheap:** stop treating a blank `Ownership Type` as a pass. Require either a populated ownership field or a verification before an account clears the public/SPAC exclusion, and mark the rest `OWN?` the way `AGE?` and `VOL?` are marked now. That is rule 4 applied to the anti-ICP side, where it currently does not reach.

**And it is cheap, because the field can be populated — confirmed by workstream 1 the same evening.** Their transaction-volume pull returned `PUBLIC_COMPANY` correctly and **unprompted on 14 of 30 rows** (Shopify, Booking Holdings, Jumia, Sea, Lightspeed, BILL, PAR Technology, NCR Voyix, WEX, Thryv, GoTo, Intellect, Aurionpro, Nucleus). **`OWN?` is a per-pull coverage failure, not a capability gap** — any re-pull can fill it, so this closes with a re-pull rather than 27 hand verifications.

## EST is not a weight in v2 — it is a hidden gate on Tier 1

Workstream 1 cautioned that EST is heavy for a signal read from one job posting. **The arithmetic is worse than that: no account can reach Tier 1 without `EST●`, whatever else it scores.**

Maximum reachable without EST is **MRG 20 + HIR 15 + MDB 15 = 50**, against a Tier 1 cut of **56.25**. So an account perfect on every other signal — confirmed margin trigger, live infra hiring, MongoDB present and direction-checked — **tops out in Tier 2.** Both current Tier 1 members carry `EST●`, and that is not a coincidence; it is the only way in.

**EST would have to fall to 15 points before a non-EST account could reach Tier 1** (max 65, cut 48.75, versus 50 available). That would demote below HIR and MDB the signal `ICP.md` calls *"the core qualifier, and the only one that ever came from the target's own words."* **Breaking the gate is worse than owning it.**

**Recommendation: own it, fix the depth, leave the weight — and declare the gate *after* the pull, not before.**

**The sequencing amendment is workstream 1's and it is right.** `EST●` is held by **6 accounts**; 22 are unmeasured and 9 more are single-source absences. **So the gate does not currently gate on estate pain — it gates on having been measured favourably once.** Declaring it today would write measurement luck into the model as policy. The 44-domain pull settles which it is: surface estate pain at 15 of 44 and the `EST●` population triples and the gate becomes a real qualifier; surface two more and the gate is confirmed as a sampling artifact and the weight question reopens on evidence. **Same decision, one step later, made against a measured population instead of a six-account accident.**

1. **Declare it.** Tier 1 requires `EST●`. Written as a rule it is defensible and legible; left as an emergent property of the arithmetic it is a trap for whoever reads the tier table next.
2. **Stop treating one posting as a settled absence.** A company can carry a twenty-year estate and never mention it in one SRE req. *"No estate pain in the single posting we hold"* is a much weaker claim than *"this company has no estate pain"*, and today it produces the same `EST○` and the same zero.

### The general rule underneath, because it is not about EST

**Evidence of presence and evidence of absence do not cost the same.** One estate-pain sentence is sufficient to establish `EST●`. No amount of *one posting* is sufficient to establish `EST○`. Positives are cheap and sound; negatives are expensive and weak. **A model that scores them symmetrically will systematically under-score**, and that is precisely what has been happening.

**Sharpening, because "single-source" is not quite the operative property: an absence is only as strong as the *completeness* of the source it is drawn from.** A source that **enumerates** supports an absence. A source that **samples** does not. Count of sources is a proxy; completeness is the thing.

**MDB is the worked counter-example, and it shows the system already got this right once.** `MDB○` rests on a detector that returned a populated list of primary databases with MongoDB not among them — an **enumerating** source, so the absence is sound. The five `MDB?` are exactly the cases where the detector returned nothing, and they are already marked unknown rather than absent. **MDB's absence handling is correct; EST's is not — because a job advert samples an estate, it does not enumerate one.**

Note the mirror: for MDB the **positive** already carries its provenance (`MDB●` product-stack detection versus `MDB◑` job-advert slug, half credit). For EST the **absence** now needs to. Same principle either side of the ledger — **a mark should carry the quality of the source that produced it.**

**Fourth member of the family this trial has produced:** a blank field is UNKNOWN not FAIL · a derived judgment column is never evidence · a date column equal to the pull timestamp is UNKNOWN not data · **an absence from a sampling source is provisional, not absent.**

**New mark: `EST⊗` — measured absent, single source, provisional.** Distinct from `EST○`, measured absent across every posting the company has. Both score 0; only `⊗` carries a note that the measurement is one document deep. **The 44-domain pull returns one row per posting and every posting per domain, so a multi-source EST is possible for the first time** — which means the distinction is about to become measurable rather than theoretical.

**Current holders of a single-source absence:** FreedomPay and Lighthouse on the roster, plus the seven cost-test accounts measured today. **All nine are structurally capped at 50 of 75 — Tier 2 at best — on one requisition each.**

**The pull is safe to run now.** The weight question does not change the pull's design: workstream 1's prompt already returns one row per posting and demands a row for every domain including the empty ones. Run it, then decide the weight against real multi-posting data rather than ahead of it.

## EST and HIR measured for the 7 cost-test accounts — free, 2026-09-03

Workstream 1 merged the cost-test posting text into `data/0926-origami-job-postings.csv` as `Pull = P9 cost-test` (36 → 58 rows, commit `37b10cf`) instead of committing a second text-bearing file — the better fix, because a second file preserves evidence while breaking the premise that made the one-grep check work. **With the text in the canonical file, both signals were measurable for free.**

**EST: measured absence on all seven.** No estate-pain sentence in any of the seven postings, and one database named across all of them (BigQuery, Meilleurtaux). These are now **measured zeros rather than blanks** — the distinction the whole audit turned on. Origami Risk 7,011 chars · Meilleurtaux 6,848 · Facile.it 5,232 · Capital on Tap 4,911 · Mollie 4,870 · OEC 4,398 · Chrono24 3,838.

**HIR: 4 of 7, not 7 of 7 — the leaky role term fired again.** Judged on description text, not titles:

| Account | Posting | Infra terms | Non-infra terms | HIR |
|---|---|---|---|---|
| Capital on Tap | Site Reliability Engineer | 3 | 0 | **●** |
| Origami Risk | Site Reliability Engineer | 3 | 0 | **●** |
| Mollie | Platform Engineer II — Build | 4 | 1 | **●** |
| OEC | Senior Platform Engineer (Cloud & AI) | 7 | 3 | **●** |
| Facile.it | Platform Engineer — DevEx & Cloud Platform | 3 | 4 (`react`, `typescript`, `llm`, DevEx) | **○ leaky** |
| Meilleurtaux | AI Platform Engineer — AZURE | 2 | 2 (`genai`, `llm`) | **○ leaky** |
| Chrono24 | (Senior) AI Platform Engineer | **0** | 0 | **○ leaky** |

**Second confirmed instance of the leaky "Platform Engineering" term**, after Lighthouse's Ember/React/TypeScript *Lead Platform Engineer*. It now has a measured rate on a fresh pull: **3 of 7**. The new variant is AI-platform roles rather than front-end ones — same term, different false positive.

**Method note worth keeping.** A first pass over these seven judged 2 of 7 infra **from the titles alone** and was wrong; the description scan corrected it to 4. That is the repo's own rule — *never accept a role match on the title alone* — catching its author. The check costs one pass over text already held.

**And the roster survives the same scrutiny: 0 of 6 HIR marks fail.** Sensor Tower, Close, Owner.com, Signifyd, Alan and FreedomPay all show 4–9 infra terms against 0–3 non-infra; NexHealth reads ambiguous at 2/0 but is not leaky. **The leaky term is hitting the newer pulls, not the P1 infra-hiring pull the roster was built from** — P1 used the tighter role list. Roster HIR evidence stands.

## Credit spend — revised priority, 2026-09-03

Workstream 1's counts, corrected by them: **21 accounts need MDB** (the 19 consolidation accounts plus Vinted and ShiftKey, added after the 39-account enrichment) and **19 need HIR** (Vinted and ShiftKey already carry `Infra Posting = true` from the C1 pull). The original 31 and the 7 cost-test accounts already have both. **What nobody had counted: 22 roster accounts need EST.**

Ordered by decision value per credit, not by cohort:

| # | Buy | Accounts | Method | Cost | Why here |
|---|---|---|---|---|---|
| 1 | **HIR** | 19 | boolean via company lookup @0.5 | **~10** | Best value density on the list — a 15-point signal for ten credits. |
| 2 | **EST on the roster** | **22** | posting pull @1/posting + enrichment | **~45–115** | Highest decision value. 33% of the model, currently unmeasured on 71% of the roster, and it decides Tier 1 membership. |
| 3 | **MDB** | 21 | `Enrich Tech Stack` @2.5 | **~53** | Fills the last gap on the new accounts and on Vinted/ShiftKey. |
| 4 | **EST on the 19** | 19 | posting pull, unpriced | ~40–100 | Last. These accounts are unevidenced on every signal, so EST alone will not tier them. |

**Restructured 2026-09-03 — workstream 1's packaging beats the four line items above. Two calls, not four.**

One **Job Posting Search** across the affected domains buys **EST (25) and HIR (15) together — 40 of the 75 points** — because the posting text is the only source EST has, and a domain returning no matching posting is a *measured absence* rather than a blank. That distinction is the entire point of the audit. `Enrich Tech Stack` stays a separate call for MDB, because posting rows carry database mentions on only 10 of 36 rows (~28%), which is not good enough for a 15-point gate.

| Call | Buys | Domains | Cost |
|---|---|---|---|
| 1 · Job Posting Search | **EST only** — HIR now arrives free at search time, since the gated pull populates `Infra/SRE Posting` on every row | **44** | ~30–60 |
| 2 · Enrich Tech Stack | MDB | 21 | ~53 |
| | | | **~85–115** — inside the authorised 150, covering 44 accounts rather than 19 |

**The 44:** the **23** roster accounts with no posting text (the 22 unmeasured plus Metropolis, whose mark is now dropped and which must be re-measured) · the **19** consolidation accounts · **Vinted and ShiftKey**, which have HIR from the C1 pull but no EST. Zuora, Carta and Pushpay — the three that would reach Tier 1 on this measurement — are all in the 23.

**Correction to the 44, found here: the 7 cost-test accounts are not covered either.** Workstream 1's table credits them with EST and HIR because they were sourced from a job-posting pull. HIR is genuinely known — a posting existed. **But EST needs the posting text, and `srepostingscosttestrawdata20260903.csv` was never committed to the repo.** Checked: none of Origami Risk, Facile.it, Chrono24, Mollie, OEC, Meilleurtaux or Capital on Tap appears in `data/0926-origami-job-postings.csv`, the only file holding posting text.

**So the pull is 51 domains, or 44 if that CSV is committed first.** Committing it is strictly better — it costs nothing, it saves 7 domains of pull, and it preserves the evidence the way every other pull has been preserved. **Recommendation: commit the file, keep the pull at 44.** This is the same "the text is in the repo" premise error that cost a round-trip earlier today, running in the opposite direction — worth noting that the check took one grep both times.

**Items 1 and 2 are the ones that change decisions.** Item 2 is the one that could move three accounts into Tier 1.

## Open items

1. ~~**The campaign-motion question.**~~ **Closed 2026-09-03 in the direction of "sufficient." Stop measuring the pool.** Origami's own answer: all three figures — 2,723 → 1,506 → 862 — are projections off the same stale 30-row sample, each recomputed from a draw whose 16 non-US/EU rows can never pass the gates, with the caveat *"neither number should be treated as an exact TAM for campaign sizing."* **The decision no longer needs the number. C1's first calibration window needs 143. The most pessimistic projection is 862 — wrong by four times over and still enough.** The fresh gated draw is still owed and is now nice-to-know, not a blocker. This question consumed most of 3 September; the answer was available from the ratio the whole time. Superseded detail: The old framing: ~7,400 job postings over 90 days, 2 of 30 sampled qualifying strictly, an interval consistent with 40 to 800 qualified companies. **Workstream 1's transaction-volume-first pull is the first sourcing configuration that worked**, and Origami projects **~2,723 qualified in a ~3,000 pool at 3.2 credits each**; 5 of 14 cleared geography and headcount, implying roughly **900–1,000 in-band qualified accounts**. **Treat that as order of magnitude only — n=14, and the 2,723 is Origami's own projection, not a count.** Even discounted heavily it changes the shape of the question: against the 143 accounts the first 500-send calibration window needs, **the population was never the constraint — the filter order was.** Searching the trigger first and filtering fit second is what `ICP.md` already says ("Intent is 30 of 100 points; firmographic-first sourcing scores zero on it by construction") and what took three days to demonstrate. A volume motion is viable on these numbers; ABM-only would leave the pool untouched. **Still open** because the projection needs a real count behind it before it drives a spend.
2. ~~**MongoDB presence is unknown for 29 of 32 accounts.**~~ **Closed 2026-09-03 by the Enrich Tech Stack pull.** 13 confirmed present · 14 confirmed absent · 5 UNKNOWN. It resolved the highest-weighted unscored signal on the roster and **moved zero accounts into Tier 1.** See the enrichment section for the four audit findings and the direction check.
3. ~~**Signifyd's figures carry two vintages.**~~ **Closed 2026-09-03 — immaterial confirmed, not assumed.** The `Field Conflicts` column records the drift as `Employee Count=500 | 495 ;; Total Funding=411000000 | 409000000 ;; Funding Stage=series_e | SERIES_E`. Note the conflicted figure is **total funding, not revenue.** Independent check: a round-by-round public record sums to ~$390M (seed $2M late 2012 · A $7M · B $20M 2016 · C $56M 2017 · D $100M 2018 · E $205M April 2021 at a $1.34B valuation). Every one of the three figures clears the SCL threshold of $100M+ at Series C+ by roughly 4×, so the drift cannot move the gate. Employees: Signifyd's own about page states **500+**, which contains both point estimates — record `500+ (company-stated)` and drop 495 and 500. Founded **2011**, confirming `AGE●` on evidence rather than on a blank field. **SCL rests on public funding data; the CSV's `Annual Revenue: 150M` is an unattributed vendor estimate and is not used.**
4. **Two ICP interpretation calls are settled** and applied here: the industry list is indicative of "digital-native with real transaction volume" rather than closed, and US/Europe describes proof transferability rather than engineering location.

5. ~~**Owner.com's founding year.**~~ **Closed 2026-09-03 — 2018 approved, `AGE●` applied (+5).** Owner.com then lost 15 to the direction rule and sits at 65, Tier 2 — it fell on MongoDB, not on age. Reasoning kept because the anti-ICP call turned on it: `Founded Year` is **blank** in both committed CSVs, so `AGE◐` (5 of 10) was awarded on no evidence at all. Two sourced readings now exist. **2018** — the ProfitBoss founding (FOX Business, 11 Dec 2020), corroborated by Owner's own Series C memo: *"Building for restaurants for over 7 years"* (memo ~May 2025). **2020** — the Wikipedia infobox value, echoed by Owner's own job description in `data/0926-origami-job-postings.csv`: *"Since 2020, we've generated tens of millions"*. The rebrand to Owner.com came in 2021 (Business Insider, Sept 2021). **The gate turns on which reading holds: 2018 → `AGE●`, score 85 → 90. 2020 → `AGE○` plus the founded-2019-or-later anti-ICP hit at −40 → score 40, Tier 3, and `../strategy/0926-abm-owner-com.md` is void.** Recommendation: **2018, `AGE●`, score 90, no anti-ICP hit.** The company's own claim is the strongest source available; the 2018 ProfitBoss codebase *is* the MVP era; and the exclusion's stated purpose — "greenfield infrastructure has nothing to unwind" — is contradicted directly by a live Staff Database Engineer req naming a MongoDB-to-Postgres migration. Firing a −40 structural exclusion against direct estate evidence is the Signifyd calibration error in a mirror. **Not applied. Escalated.**

6. **Sensor Tower's two size figures are stale, and it is rank 1 with an ABM plan pending.** The CSV carries `Annual Revenue: 35.6M` and `Total Funding: 46000000` — both **below** ICP-M2's size floor of "$50M–$1B revenue or $100M+ raised". `SCL◐` currently stands on the `private_equity` ownership limb, which is sound, but the size limb fails on the data in hand. Both figures read as pre-transaction: the $45M Series B predates the private-equity acquisition and the subsequent combination with data.ai. `Founded Year` is blank for Sensor Tower too. **Verify current revenue, headcount and ownership before writing the ABM plan, not after.**

7. **Close's SCL is scored `○` on a funding row this file already calls wrong.** The CSV reads `Total Funding: 250000 / Funding Stage: seed / Employee Count: 214` for a thirteen-year-old CRM. Model B's SCL carries a **bootstrapped-profitable** limb. If Close qualifies under it, SCL moves `○ → ●`, the score moves 80 → 85, and the model-versus-hand-ranking disagreement above resolves in the model's favour. One verification closes it and unblocks the second Tier 1 ABM plan.

8. ~~**Blanks are earning credit.**~~ **Closed 2026-09-03 — approved and applied as `lead-scoring` rules 4 and 5** (`SKILL.md` v1.2, backup at `SKILL.md.pre-rules-45`). Nine accounts moved down a tier; Tier 1 went from four accounts to one. Superseded detail: Coverage across the 32 qualified rows in `data/0926-origami-companies.csv`: `Founded Year` blank **14/32** (AGE, 10 pts) · `Database Technology Mentions` blank **29/32** (MongoDB signal, 15 pts) · `Transaction Volume` blank **20/32** (VOL, 10 pts) · `Matching Posting Count` blank 29/32 (already retired). That is **35 of 100 points** resting largely on inference. The mechanism is a category slip: `lead-scoring` rule 1 (*"a blank field is UNKNOWN, not FAIL"*) and its corollary (*"UNKNOWN is not zero"*) were both written about **ranking** — don't sort a blank below a real value. Model B applies them as **scoring**, where "partial evidence scores half" turns every blank into `◐` and 5 points. **Proposed fourth rule: UNKNOWN scores zero — neither penalty nor credit. `◐` is for partial evidence, never for absent evidence.** Editing `lead-scoring/SKILL.md` is an escalation, so this is proposed, not applied.


9. **Applied 2026-09-03 — kept as the record of what the correction cost.** Audited against the source CSV: **AGE credit was awarded on a blank `Founded Year` for 14 of 32 accounts**, and not at half — Sensor Tower, Close, Signifyd and eleven others took the **full 10 points** on an empty field. **VOL credit was awarded on a blank `Transaction Volume` for 20 of 32.** All four Tier 1 accounts are blank on **both** columns. **No Tier 1 account has a verified founding year or a verified transaction volume**; of the 18 accounts that do have a real `Founded Year`, none is Tier 1. That is selection, not coincidence — generous marks were assigned where evidence was absent, and accounts with populated rows were graded against actual values.

   Applying the proposed rule (open item 8: UNKNOWN scores zero) to AGE and VOL only, and crediting the two founding years verified 2026-09-03:

   | Account | Now | Blank-sourced points | Corrected | Tier |
   |---|---|---|---|---|
   | Owner.com | 85 | VOL 10 (AGE now **verified 2018**, +5) | **80** | T1 |
   | Sensor Tower | 92 | AGE 10 + VOL 5 | **77** | T1 |
   | Close | 80 | AGE 10 + VOL 5 | **65** | T2 |
   | Signifyd | 75 | VOL 10 (AGE **verified 2011**) | **65** | T2 |

   **Tier 1 goes from four accounts to two, and Owner.com becomes rank 1** — not because it improved, but because its founding year is the only one verified. **The ranking is more robust than the scores.** Tier 1's heavy signals are genuinely evidenced: EST from real requisitions, HIR from real P1 postings with real dates, MDB now confirmed — 55 of Sensor Tower's 92 rests on evidence. It is the last 17.5 that rests on two empty columns and a stale ownership figure. Sequencing judgment survives; the numbers should not be quoted.

10. **Sensor Tower is rank 1 and the least-evidenced account on the roster.** Blank `Founded Year`, blank `Transaction Volume`, `Annual Revenue: 35.6M` and `Total Funding: 46000000` both below the M2 size floor and both pre-acquisition, `SCL◐` standing only on the `private_equity` limb, and `MRG●` at 20 points whose provenance is recorded only as "margin/sponsor trigger confirmed". **17.5 of its 92 traces to blank or stale source fields.** Its estate, hiring and MongoDB evidence is sound. Verify founding year, headcount, ownership and the margin trigger's source before the ABM plan, not after — one of those four either earns the rank or moves it.

11. ~~**Direction check on the 13 MongoDB accounts.**~~ **Run 2026-09-03. Coverage 3 of 13.** One reversal (Owner.com, `MDB⊘`), two confirmed neutral (Sensor Tower, Close), ten with no requisition on file. **Open remainder: a 10-account Job Posting Search request sits with workstream 1** — see enrichment finding 5. Until it returns, ten accounts hold 15 points each on unverified direction; Owner.com is the proof that some of them may not deserve it.

12. **`Legacy Relational` needs a second pass against requisition text, not the detector.** Finding 4 shows the detector missed Postgres at Owner.com. Every blank `Legacy Relational` is therefore suspect, which means the co-presence set may be larger than six. Same free source as item 11.

13. **Nine accounts from the cost-test pull can now be scored — the block on them has lifted.** `handoffs/0926-costtest-graded-accounts.md` carries gate evidence for 19 companies from the SRE-postings cost test, 9 qualified, **7 new to the roster** (Mollie · Chrono24 · Facile.it · Meilleurtaux · Origami Risk · OEC · Capital on Tap). That file states *"do not score these until the proposed fourth rule (UNKNOWN scores zero) is settled"* — **it was settled and applied today**, so scoring is unblocked. Their AGE coverage is **9/9 populated (1999–2016)**, far better than this roster's 14/32 blank; MongoDB is named for 0 of 9 in the pull itself, though the enrichment separately resolves OEC (`MDB◑`, slug tier, co-presence) and Capital on Tap (`MDB●`, product stack). Also carries a **new rule from 3 September: debt financing satisfies the funding gate for lenders** (`CAPITAL-PATH: DEBT`, Capital on Tap at $611M) — the gate tests scale and capital access, and rejecting debt would systematically exclude the lending half of fintech.

14. **Stale public/private status is a recurring anti-ICP risk on this roster.** The cost-test file records Everbridge leaking through the public-status filter as the **fifth consecutive occurrence**, and names Pushpay in P2 as the same error class. Anti-ICP fires at −40 on "publicly listed or SPAC-bound", so a stale ownership field is worth 40 points in either direction. Several roster accounts have changed status recently by take-private — Pushpay and Zuora among them, where the take-private is simultaneously the `MRG●` trigger. **Cheap pass worth running: re-check current listing status for every roster account carrying `MRG●` on a sponsor mandate.**

## Refresh

Quarterly, or when a Cohort D account's trigger fires. Cohort D is a watchlist, not a sequence — monitored for infra hiring, a funding or ownership event, or a public incident, and promoted into Cohort A or B when one appears.