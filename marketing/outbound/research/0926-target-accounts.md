# WeKan — ICP-M2 target accounts (0926)

*Written 2026-09-02 by `/lead-scoring` Model B. Reads `../../icp/ICP.md` (ICP-M2), `../../positioning/positioning.md`, `../../messaging/messaging.md`, `../../company/company.md`. Every score cites the evidence that produced it; no evidence, no points.*

**Provenance.** Derived from the September 2026 ICP-M2 sourcing trial: 120 unique companies screened across eight Origami pulls yielding 17 CSVs — two firmographic screens, one amended screen, one banded stratified sample, a transaction-evidence audit, a correction test and a trigger-first SRE sample. 32 qualified. 400 credits. (Canonical tally, settled 2026-09-02; the 120 is a clean domain dedupe across all 17 source files and supersedes the earlier 119 and 124.) Full per-account reasoning is maintained as the ICP-M2 Pursuit Order artifact; this file is the canonical extract every downstream outbound skill reads.

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

`VER` industry · `AGE` founded ≤2018 · `SCL` scale · `VOL` per-period transaction volume · `EST` named estate pain · `MRG` margin trigger · `HIR` live infra hiring · `ACC` production access grantable

`●` evidence in hand · `◐` partial or inferred · `○` no evidence · `✕` known obstacle (flag, not a disqualifier)

## Tier 1 — score 75+  (4 accounts)

Named-account ABM. Run `/abm-campaign` per account.

| Account | Score | Gates | Trigger evidence | Cohort |
|---|---|---|---|---|
| **Sensor Tower** · `sensortower.com` | 92 | `VER◐ AGE● SCL◐ VOL◐ EST● MRG● HIR● ACC●` | **MongoDB present**; named estate pain in an open req; margin/sponsor trigger confirmed; live infra hiring | B — sponsor mandate |
| **Owner.com** · `owner.com` | 85 | `VER● AGE◐ SCL● VOL● EST● MRG◐ HIR● ACC●` | **MongoDB present**; named estate pain in an open req; live infra hiring | A — hiring trigger |
| **Close** · `close.com` | 80 | `VER◐ AGE● SCL○ VOL◐ EST● MRG◐ HIR● ACC●` | **MongoDB present**; named estate pain in an open req; live infra hiring | A — hiring trigger |
| **Signifyd** · `signifyd.com` | 75 | `VER● AGE● SCL● VOL● EST● MRG◐ HIR● ACC✕` | named estate pain in an open req; live infra hiring; access obstacle flagged | A — hiring trigger |

## Tier 2 — score 50–74  (4 accounts)

One unknown each. Resolve, then promote or drop.

| Account | Score | Gates | Trigger evidence | Cohort |
|---|---|---|---|---|
| **Alan** · `alan.com` | 65 | `VER● AGE● SCL● VOL● EST● MRG○ HIR● ACC◐` | named estate pain in an open req; live infra hiring | A — hiring trigger |
| **Metropolis Technologies** · `metropolis.io` | 52 | `VER○ AGE◐ SCL● VOL● EST◐ MRG● HIR○ ACC●` | partial estate signal; margin/sponsor trigger confirmed | B — post-acquisition integration |
| **NexHealth** · `nexhealth.com` | 52 | `VER◐ AGE● SCL✕ VOL◐ EST◐ MRG◐ HIR● ACC●` | partial estate signal; live infra hiring | A — hiring trigger |
| **FreedomPay** · `freedompay.com` | 50 | `VER● AGE● SCL◐ VOL● EST○ MRG● HIR◐ ACC◐` | margin/sponsor trigger confirmed | B — sponsor mandate |

## Tier 3 — score <50  (24 accounts)

Nurture and trigger-monitoring only. Not sequence-eligible.

| Account | Score | Gates | Trigger evidence | Cohort |
|---|---|---|---|---|
| **Pushpay** · `pushpay.com` | 45 | `VER◐ AGE● SCL● VOL● EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | B — sponsor mandate |
| **Zuora** · `zuora.com` | 45 | `VER◐ AGE● SCL● VOL● EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | C — re-score as M1 |
| **iCapital** · `icapital.com` | 45 | `VER● AGE● SCL● VOL● EST○ MRG● HIR○ ACC◐` | margin/sponsor trigger confirmed | C — re-score as M1 |
| **Cambridge Mobile Telematics** · `cmtelematics.com` | 40 | `VER● AGE◐ SCL● VOL● EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | B — sponsor mandate |
| **Carta** · `carta.com` | 40 | `VER● AGE● SCL● VOL◐ EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | E — efficiency reset |
| **Workrise (now RigUp)** · `workrise.com` | 40 | `VER◐ AGE● SCL● VOL◐ EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | E — efficiency mandate |
| **Zūm** · `ridezum.com` | 40 | `VER◐ AGE● SCL● VOL◐ EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | B — sponsor mandate |
| **Civitatis** · `civitatis.com` | 35 | `VER● AGE◐ SCL● VOL◐ EST○ MRG● HIR○ ACC●` | margin/sponsor trigger confirmed | B — sponsor mandate |
| **Fleetio** · `fleetio.com` | 35 | `VER◐ AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Housecall Pro** · `housecallpro.com` | 35 | `VER● AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **ID.me** · `id.me` | 35 | `VER◐ AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC✕` | access obstacle flagged | D — watchlist, no trigger |
| **Pantheon** · `pantheon.io` | 35 | `VER○ AGE● SCL● VOL● EST● MRG◐ HIR● ACC✕` | named estate pain in an open req; live infra hiring; **anti-ICP: infrastructure vendor**; access obstacle flagged | Suppression check first |
| **Wallapop** · `wallapop.com` | 35 | `VER● AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Weee!** · `sayweee.com` | 35 | `VER● AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Zeta** · `zeta.tech` | 35 | `VER● AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **ezCater** · `ezcater.com` | 35 | `VER● AGE● SCL● VOL● EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Back Market** · `backmarket.com` | 30 | `VER● AGE● SCL● VOL◐ EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Blockchain.com** · `blockchain.com` | 30 | `VER● AGE● SCL● VOL◐ EST○ MRG◐ HIR○ ACC◐` | firmographics only — no trigger | D — watchlist, no trigger |
| **Cover Genius** · `covergenius.com` | 30 | `VER● AGE● SCL● VOL◐ EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Engine (formerly Hotel Engine)** · `hotelengine.com` | 30 | `VER● AGE● SCL● VOL◐ EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Netradyne** · `netradyne.com` | 30 | `VER◐ AGE● SCL● VOL◐ EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Sure** · `sureapp.com` | 30 | `VER● AGE● SCL● VOL◐ EST○ MRG◐ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **Lighthouse** · `mylighthouse.com` | 20 | `VER● AGE● SCL● VOL◐ EST○ MRG○ HIR○ ACC●` | firmographics only — no trigger | D — watchlist, no trigger |
| **FarEye** · `fareye.com` | 15 | `VER● AGE● SCL● VOL✕ EST○ MRG○ HIR○ ACC◐` | firmographics only — no trigger | D — watchlist, no trigger |

## Entry point — identical for every account

**Fixed-fee 2-week estate assessment**, savings quantified against real workload data. M2 has exactly one entry offer; everything past it is expansion. Proof point selection is per account, from two only:

- **Estate cost & sprawl** → `messaging.md` §6: global on-demand delivery platform (logistics) — $1M annual infrastructure savings, 30–90% cost reduction per cluster, zero downtime
- **Velocity & monolith** → `messaging.md` §6: US homeowner's-insurance platform — 90% faster launch (2 weeks → 5 minutes), 2× developer velocity, 3× query performance

Second proof point applies to: Owner.com · Alan · Sure · Cover Genius · NexHealth · Cambridge Mobile Telematics · Housecall Pro. First applies to the rest.

**Audience framing** from `messaging.md` §5 — CTO/CIO: de-risked modernization, one accountable partner, measurable ROI. VP Engineering / Platform: architecture-first, faster cycles, no lost context.

**Avoid** (`messaging.md` §7): "database modernization partner", MongoDB-only framing, generic digital transformation. MongoDB mastery is a differentiator inside a broader story, never the story.

## Disqualified — anti-ICP hits and structural exclusions

Eighty-eight of the 120 screened companies were excluded. Reasons cluster, and each cluster is a filter the next sourcing run should apply rather than a judgment to repeat by hand.

**Infrastructure vendors — suppliers, not prospects** — Temporal · CData · Port.io · Hydrolix · Fluidstack · Skyflow · CloudLinux · Tines · WEKA · AntemetA · Chainlink Labs · InterSystems · Supabase · Collibra · Movu Robotics · ACS

Their customers are ICP-M2. Deepest in-house platform benches, lowest winnability, and in some cases competitors. Pantheon scores 75 on signals and is held at −40 for the same reason.

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

## Open items

1. **The campaign-motion question is unresolved.** The trigger pool is ~7,400 job postings over 90 days, but only 2 of 30 sampled postings qualify strictly — a confidence interval consistent with anywhere between 40 and 800 qualified companies. A 300-posting sample (300 credits at 1 credit/posting) narrows it enough to decide volume-email versus ABM.
2. **MongoDB presence is unknown for 29 of 32 accounts.** Origami's Enrich Tech Stack costs 2.5 credits per company — ~80 credits fills the highest-weighted unscored signal across the whole list. Highest value per credit available.
3. ~~**Signifyd's figures carry two vintages.**~~ **Closed 2026-09-03 — immaterial confirmed, not assumed.** The `Field Conflicts` column records the drift as `Employee Count=500 | 495 ;; Total Funding=411000000 | 409000000 ;; Funding Stage=series_e | SERIES_E`. Note the conflicted figure is **total funding, not revenue.** Independent check: a round-by-round public record sums to ~$390M (seed $2M late 2012 · A $7M · B $20M 2016 · C $56M 2017 · D $100M 2018 · E $205M April 2021 at a $1.34B valuation). Every one of the three figures clears the SCL threshold of $100M+ at Series C+ by roughly 4×, so the drift cannot move the gate. Employees: Signifyd's own about page states **500+**, which contains both point estimates — record `500+ (company-stated)` and drop 495 and 500. Founded **2011**, confirming `AGE●` on evidence rather than on a blank field. **SCL rests on public funding data; the CSV's `Annual Revenue: 150M` is an unattributed vendor estimate and is not used.**
4. **Two ICP interpretation calls are settled** and applied here: the industry list is indicative of "digital-native with real transaction volume" rather than closed, and US/Europe describes proof transferability rather than engineering location.

5. **Owner.com's founding year — verified, and the AGE call is Rudra's.** `Founded Year` is **blank** in both committed CSVs, so `AGE◐` (5 of 10) was awarded on no evidence at all. Two sourced readings now exist. **2018** — the ProfitBoss founding (FOX Business, 11 Dec 2020), corroborated by Owner's own Series C memo: *"Building for restaurants for over 7 years"* (memo ~May 2025). **2020** — the Wikipedia infobox value, echoed by Owner's own job description in `data/0926-origami-job-postings.csv`: *"Since 2020, we've generated tens of millions"*. The rebrand to Owner.com came in 2021 (Business Insider, Sept 2021). **The gate turns on which reading holds: 2018 → `AGE●`, score 85 → 90. 2020 → `AGE○` plus the founded-2019-or-later anti-ICP hit at −40 → score 40, Tier 3, and `../strategy/0926-abm-owner-com.md` is void.** Recommendation: **2018, `AGE●`, score 90, no anti-ICP hit.** The company's own claim is the strongest source available; the 2018 ProfitBoss codebase *is* the MVP era; and the exclusion's stated purpose — "greenfield infrastructure has nothing to unwind" — is contradicted directly by a live Staff Database Engineer req naming a MongoDB-to-Postgres migration. Firing a −40 structural exclusion against direct estate evidence is the Signifyd calibration error in a mirror. **Not applied. Escalated.**

6. **Sensor Tower's two size figures are stale, and it is rank 1 with an ABM plan pending.** The CSV carries `Annual Revenue: 35.6M` and `Total Funding: 46000000` — both **below** ICP-M2's size floor of "$50M–$1B revenue or $100M+ raised". `SCL◐` currently stands on the `private_equity` ownership limb, which is sound, but the size limb fails on the data in hand. Both figures read as pre-transaction: the $45M Series B predates the private-equity acquisition and the subsequent combination with data.ai. `Founded Year` is blank for Sensor Tower too. **Verify current revenue, headcount and ownership before writing the ABM plan, not after.**

7. **Close's SCL is scored `○` on a funding row this file already calls wrong.** The CSV reads `Total Funding: 250000 / Funding Stage: seed / Employee Count: 214` for a thirteen-year-old CRM. Model B's SCL carries a **bootstrapped-profitable** limb. If Close qualifies under it, SCL moves `○ → ●`, the score moves 80 → 85, and the model-versus-hand-ranking disagreement above resolves in the model's favour. One verification closes it and unblocks the second Tier 1 ABM plan.

8. **Three of Model B's eight signals are largely scored without data — and blanks are quietly earning half credit.** Coverage across the 32 qualified rows in `data/0926-origami-companies.csv`: `Founded Year` blank **14/32** (AGE, 10 pts) · `Database Technology Mentions` blank **29/32** (MongoDB signal, 15 pts) · `Transaction Volume` blank **20/32** (VOL, 10 pts) · `Matching Posting Count` blank 29/32 (already retired). That is **35 of 100 points** resting largely on inference. The mechanism is a category slip: `lead-scoring` rule 1 (*"a blank field is UNKNOWN, not FAIL"*) and its corollary (*"UNKNOWN is not zero"*) were both written about **ranking** — don't sort a blank below a real value. Model B applies them as **scoring**, where "partial evidence scores half" turns every blank into `◐` and 5 points. **Proposed fourth rule: UNKNOWN scores zero — neither penalty nor credit. `◐` is for partial evidence, never for absent evidence.** Editing `lead-scoring/SKILL.md` is an escalation, so this is proposed, not applied.

## Refresh

Quarterly, or when a Cohort D account's trigger fires. Cohort D is a watchlist, not a sequence — monitored for infra hiring, a funding or ownership event, or a public incident, and promoted into Cohort A or B when one appears.