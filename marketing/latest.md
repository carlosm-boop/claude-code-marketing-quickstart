# latest.md — working memory

Delta cache for the WeKan marketing OS. Newest at top. Agents read this before deciding what to do; you write here after anything significant.

**What goes here:** drift reports, deltas since last cycle, metric movements, recent decisions.
**What does not:** canonical content (that's in `positioning.md`, `ICP.md`, etc.) or long-term records (that's `history.md`).

---

## 2026-09-03 (later 10 · w1) — the database-estate search was sourcing ICP-M1 inside ICP-M2's headcount band

**Refined run: 3 qualified of 30 sampled, ~10 credits each. Do not scale — and the reason is not the filter ordering.**
Survivors in `data/privatedatabaseestaterefined20260903.csv`: **Trust Payments** (UK payments acquirer, real card volume — the strong one) · **Reward** (card-linked offers on bank transaction feeds — plausible) · **BD Media | BD Logistics** (**exclude**: the pipe is two brands under one parent, and it is Belgian physical leaflet distribution, not a digital platform). ~2 real accounts from 30.

### The diagnosis

`ICP.md` gives **M1's** technographic signature as *"Legacy core with heavy **PL/SQL / T-SQL** stored procedures"*. PL/SQL is Oracle; T-SQL is Microsoft SQL Server. **Oracle + MSSQL is M1's fingerprint, verbatim.** M1's size band is **2,500+ employees**.

Every run today searched that M1 tech signature inside **M2's** headcount band (200–2,500 — which is M1's floor), behind a `private, not publicly listed` filter that excludes most large enterprises. The intersection is companies that fit neither ICP. That is why the output was persistently insurance carriers, utilities, manufacturers, logistics and professional-services firms: **the tech filter pulled toward M1 while the size and ownership filters fought it.**

The industries that kept surfacing — SECURA, Talcott, Everwise Credit Union, APG Austrian Power Grid, TMEIC, E80 Group, Exeter Finance — are BFSI, energy, manufacturing and logistics. **Those are M1's named industries.** The market was reporting where Oracle/MSSQL estates live; the filters kept discarding the answer. None of them appeared as an M1 lead only because the 2,500 cap excluded M1's population by construction.

Compounding it: M2's own monolith is *"MSSQL/**MySQL/Postgres** monolith from the founding era"*. The search covered one third of that list. MSSQL and "digital-native" are close to anti-correlated — post-2010 platforms are Postgres/MySQL/Mongo shops; MSSQL and Oracle concentrate in traditional enterprises, i.e. M1.

**Origami's vertical-first proposal is right on ordering** (scarcest filter first — the third instance today of *most selective goes first*, after never-sort-on-the-capped-dimension and trigger-before-firmographics). It is just not sufficient, because the tech filter was pointed at the wrong ICP.

### Two searches now specified

**Search A — ICP-M1, the primary ICP, never sourced once.** Same tech filter, band corrected: Oracle or MSSQL high-confidence · **2,500+ employees** · NA/EU · BFSI, travel/aviation, retail & CPG, healthcare, manufacturing/energy, logistics · **drop the private-only filter** — M1 is mostly listed companies · keep consultancies and captive service centres excluded, but manufacturers, utilities and traditional insurers are **in scope** for M1, not out. Recommended first: primary ICP, stronger entry offer and proof points (the 25-year Oracle RMS modernization is M1's), and today's accidental evidence says the population is reachable.

**Search B — ICP-M2, vertical-first.** As Origami proposed, plus **MySQL and Postgres added** to the database filter, and **no `vertical SaaS` search term** — it is not a real taxonomy value and it acted as a catch-all in P3, admitting legal tech, digital media, parking and intranet software. Ask Origami for its filterable industry values first; that question is free.

### Systematic defect across all three tech-search runs

**`Ownership Type` returned the literal string `Private` on every row** — no PE / VC / bootstrapped sub-type. M2's funding gate (`$100M+ with latest round Series C or later, OR PE-owned, OR bootstrapped and profitable`) has therefore been **unevaluable on every account these searches produced**, including all three survivors. Free question: can Origami return the ownership sub-type? If not, that gate stays permanently open on tech-search output and must be closed by hand or by a second call.

Also recurring: `Founded Year` blank on 2 of 3 (11 of 30 in the sampled set, flagged not failed — correct behaviour). **Trust Payments illustrates why the proxy is weak**: a 2019/2020 rebrand of a much older business, so the entity reads young while the estate is old. Consistent with the `(later 9)` finding that founding year is a proxy for estate age, not the thing itself.

---

## 2026-09-03 (later 6) — skills now cite ICP.md for gate semantics, not just gate values

**`origami-sourcing` updated** after the age proxy landed in `ICP.md`. Four changes: a *cite-a-gate-never-re-derive-one* rule in Step A naming the floor-not-a-range semantics; the worked-example commentary re-anchored on `ICP.md` ICP-M2; constraint 16 (lift gates verbatim with their stated semantics — a floor is not a range, a band is not a sort key, a qualifier is not optional); and failure case 12, the law-firm-founded-1748 result, which is the evidence that **the digital-native qualifier, not the age gate, is what excludes pre-digital companies.**

**Three of the four items flagged in (later 5) are now closed** — the 7,377 confidence downgrade, §9's numbering, and the commit backlog (all three commits landed). Still open: `lead-scoring`'s lane overlap with `origami-sourcing`, the 21-vs-23 skill count in both `CLAUDE.md` files, and the stale *"ICP.md is a draft skeleton today"* line in `orchestration.md` — which is now conspicuously wrong, since ICP.md is the file the skills cite for gate semantics.

---

## 2026-09-03 (later 9 · w1) — the age gate was never in the ICP, and the qualifier was carrying it

**Tech-stack search validated as a capability; the query was wrong and the error was mine.** Origami *can* search by technology (0.5/result, combinable with size, country, ownership, confidence and a hiring boolean). First run — `data/privatedatabaseestate20260903.csv`, 25 companies at **1.2 credits per company against the 24 the trigger path had reached**, MongoDB exclusion clean, thin table honoured, 24 of 25 high-confidence on MSSQL, ~418 more projected.

**Origami reported an 83% qualification rate. Against real ICP-M2 it is 4 of 25.** The prompt I supplied carried the firmographic filters and **omitted the industry qualifier and every exclusion** — cut while shortening the prompt after two long ones failed. Origami hit the filters it was given, correctly. The 21 failures: 7 consultancies and professional-services firms (including Osborne Clarke, a law firm founded **1748**) · 2 infrastructure vendors (Flexential, AMAX) · 3 hardware manufacturers · 3 captives of public parents · 1 state-owned utility · 1 asset manager · 3 traditional non-digital-native financial institutions · 2 compliance/gov software. Worth a look: Continental Finance, Exeter Finance, AMCS Group, Giacom.

**Resolves the long-vs-short prompt argument.** Shorten by dropping what Origami already has saved — the firmographic gates. Never by dropping what it repeatedly gets wrong — industry type and exclusions. The long prompts were not verbose; they carried eight pulls of accumulated exclusions. I cut the load-bearing half.

### The finding: `ICP.md` never contained an age gate

Searched the file. **"Founded 2018 or earlier" does not appear in it, and never did.** What `ICP.md` states is *MVP-era architecture* and *"MSSQL/MySQL/Postgres monolith from the founding era"* — a condition about the **estate**, not the company's founding date. The 2018 threshold was invented in **P1** as a way to make an architectural condition searchable by a tool that cannot inspect an estate, and it has propagated through all 14 prompts, the handoff, and both sourcing skills without ever being written into the canonical ICP.

**Why nobody noticed it is one-sided.** The threshold is a floor: it rejects companies too young to have a founding-era monolith. It has no ceiling. Pre-digital companies were being excluded by the **digital-native / transaction-volume qualifier**, not by age — so the age gate never had to hold that line. Drop the qualifier, as my prompt did, and the age gate admits an 18th-century law firm and a 1931 credit union.

**A ceiling is the wrong fix.** An older company genuinely running a digital platform typically has the *deepest* legacy estate and is the stronger target. So the correction is documentation and direction, not a new threshold.

**Applied to `marketing/icp/ICP.md`** (canonical — the guard will flag it):
1. A `Company age` row in the M2 dimension table, recording the 2018 proxy, what it stands in for, and that it is a minimum with deliberately no upper bound.
2. A note stating that age never excludes a pre-digital company, the qualifier does, with the 1748/1931 evidence — so the next person writing a prompt knows the qualifier cannot be trimmed.
3. Five exclusion categories the ICP never named, all surfaced empirically by this search: professional-services firms · hardware and industrial manufacturers · traditional non-digital-native financial institutions · captive shared-service centres and country subsidiaries of public parents · state-owned utilities and public bodies. Each with its reason, per the standing rule.

**Note for whoever owns the source document:** `ICP.md` now diverges from `WeKan_Consulting_Practice_ICPs.docx`. Three additions, all dated and marked derived. They should be pushed back upstream.

**Public-status filter has now failed in six consecutive pulls.** This one is the starkest yet: **Monolithic Power Systems (NASDAQ: MPWR)** returned with `Ownership Type = Private`. Also `Founded Year` blank on **14 of 25**, so the age filter provably did not run on those rows — the same unenforced-gate failure as Lighthouse in P7. And `Ownership Type` is the literal string `Private` on all 25, with no PE/VC/bootstrapped distinction, so the funding-ownership gate is unevaluable from this output.

**Method, confirmed twice more.** Origami answered two direct capability questions honestly: confidence is job-posting evidence strength and *"not a guarantee that the technology is deployed throughout production"*; and the hiring filter is a boolean "at least one current matching posting", not the retired aggregate. Consistent with the standing read — **reliable about itself, unreliable when judging companies.** Note the consequence for scoring: tech detection is posting-derived, so a stack hit is a hiring signal, never "estate confirmed".

---

## 2026-09-03 (later 8 · w1) — MongoDB is now data on all 39 accounts, and 7 are mid-migration

**The 15-point MongoDB input is resolved across the whole roster.** `Enrich Tech Stack` run on the 39 accounts in `outbound/research/data/0926-enrich-targets.csv`. Result: **15 of 39 run MongoDB, 24 do not** — and "do not" is now a sourced negative rather than a blank. Clean output at `outbound/research/data/0926-mongodb-status-39-accounts.csv`; Origami's raw return preserved at `0926-enrich-targets-enriched-raw.csv`.

Coverage went from 3/32 named (29 blank) to **39/39 determined**. Cost was one enrichment pass.

**The extraction column was wrong on three accounts, and the standing rule caught it.** `Database Mentions Found` reported MongoDB at 12 companies. Parsing the raw `Tech Stack` and `Job Posting Tech Stack` text directly gives **15**. The three it missed — **Workrise, iCapital, OEC** — each have zero mongo hits in `Tech Stack` and 1-2 in `Job Posting Tech Stack`. **Origami's extractor scans one field and not the other.** iCapital's is explicit: `mongodb-atlas`, the managed service, which is the co-sell channel itself.

This is the twelfth catalogued instance of *never accept a derived judgment column from the sourcing tool; take the facts and do the extraction here.* Cost: zero credits, one parse.

**Checked before trusting it.** The three upgrades rest on `Job Posting Tech Stack`, and the tokens `dbt`, `gitHub-copilot`, `mongodb` appear in that order at all three companies, which looked like boilerplate. It is not: across the 10 accounts carrying that field, no pair exceeds Jaccard 0.5 and only **five** tools are common to all ten (AWS, Python, JavaScript, Salesforce, HubSpot). `mongodb` is not among them. The lists are company-specific.

**Evidence-strength note for scoring.** 12 of the 15 are MongoDB in the detected product stack; **3 are job-postings-only** (Workrise, iCapital, OEC). A hiring-derived mention is softer than an observed production stack — a team is working with it, which is arguably the better *timing* signal but the weaker *estate* signal. The clean CSV carries `MongoDB Evidence` so the two are never conflated. Recommend they score as present-but-flagged, not as equal to a detected stack.

**The most commercially interesting cut is new: 7 accounts run MongoDB alongside a legacy relational engine.**

| Account | Legacy engine present |
|---|---|
| iCapital | MSSQL + MySQL |
| OEC | MSSQL + MySQL |
| Pushpay | MySQL |
| Zeta | MySQL |
| Zuora | MySQL |
| ID.me | MySQL |
| Netradyne | MySQL |

These are mid-migration: the destination is already in the building and the thing being migrated off is still running. Both halves of the WeKan story observable in one account, and it maps straight onto the `Oracle replace with MongoDB & WeKan` narrative. **This should drive pursuit order** — it is a sharper discriminator than the MongoDB flag alone, which 15 accounts now share. Postgres was deliberately excluded from "legacy" here: Postgres + MongoDB is a common modern pairing and does not imply a migration.

**Group distribution across the 39:** Group 1 (MongoDB) 15 · Group 2 (relational, no MongoDB) 16 · Group 3 (other data infra only) 5 · Group 4 (nothing named) 3. Group 4 is Sure, FarEye and Facile.it — three accounts where enrichment returned a stack with no database in it at all, which is a coverage gap rather than a finding.

**Consequence for w2's blank-scoring finding.** `(later 6)` measured MongoDB blank on 29 of 32 and 35 of 100 points resting on inference. **15 of those points are now sourced for every account on the roster.** The remaining exposure is AGE (14/32 blank) and VOL (20/32 blank) — and VOL was retired as a gate in §7, so whether it should score at all is the open question, not whether to fill it.

---

## 2026-09-03 (later 9) — VOL is dead across the whole roster; MDB gains an evidence tier

**Two items relayed from workstream 1. One confirmed and applied, one wrong on its premise, and chasing the first invalidated something applied an hour earlier.**

### VOL scores zero for all 32 accounts — the three `VERIFIED` values came from the fabricating classifier

Tracking the evidence-tier question into `handoffs/0926-handoff-origami-sourcing.md` §7 turned up the source of `Transaction Evidence Review`: **a classifier that failed three ways, the third being fabrication — 20 of 21 rows marked "verified per-period volume" had no period phrase anywhere in the source text.** It is the canonical example behind `lead-scoring` rule 2. **The three `VERIFIED PER-PERIOD` values credited at 10 points each in `(later 8)` are withdrawn.** ID.me −10 (Tier 2 → Tier 3), Zūm −10, Weee! −10.

**VOL now scores zero for every account on the roster, which makes it a dead signal** — it discriminates between nobody. Workstream 1 had already concluded *"retire VOL as a gate"* and moved it to a discovery question on the call; this is the same conclusion reached from the scoring side. **Model consequence: maximum achievable is 90, not 100**, so `T1 ≥75` has silently become 83% of achievable rather than 75%. Renormalising to the original intent (67 / 45) moves exactly one account — Metropolis Technologies 47 into Tier 2. Left unrenormalised, flagged so it is a choice and not a drift. **Rudra's call.**

Silver lining: ID.me falling to Tier 3 resolves the Cohort-D-in-Tier-2 contradiction from `(later 8)` **on evidence rather than by overriding the tier.** No Cohort D account remains in Tier 2.

### MDB now has two evidence tiers — confirmed from workstream 1, verified here

`MongoDB Evidence` reads `job postings only` for **Workrise, iCapital** and, in the new cohort, **OEC**. For all three the product-stack detector returned **nothing**; MongoDB comes solely from `Job Posting Tech Stack`, a slug aggregate of **314 / 317 / 374 entries** scraped across every advert the company has posted. iCapital's contains **twelve database technologies**. That is a hiring corpus, not an estate — and a slug has no sentence behind it, so **rule 5 can never be satisfied from this source at any price.** Third instance of the same failure after Lighthouse's title-only role match and Chainlink's `oracle`.

**Applied `MDB◑`, half credit.** Workrise −7.5, iCapital −7.5 → **iCapital falls out of Tier 2.** `◑` not `?` because the slug is real but cannot establish a production dependency — partial evidence, which is what half credit is for. **iCapital's co-presence flag is Tier B too** (its `MSSQL;MySQL` comes from the same list), so its entire MongoDB-plus-legacy story rests on slugs and must not drive a campaign.

### The direction check on the co-presence accounts is not free

Workstream 1 relayed that the text is in the repo. **Measured: it is not, for these accounts.** None of the six co-presence accounts has a row in `data/0926-origami-job-postings.csv`; five of six have a **blank** `Job Posting Tech Stack` as well, so there is no job-posting data of any kind for them. The 36 rows of requisition prose all belong to the hiring-led pulls — every co-presence account came from the scale-led and firmographic pulls. **The zero-cost check is exhausted at 3 of 13** (done in `later 8`: Owner.com reversed, Sensor Tower and Close neutral). Direction for the remaining ten costs a Job Posting Search, ~1 credit per posting. Request stands with workstream 1; the premise correction goes back the same way.

| | 09-02 | after rules 4/5 | now |
|---|---|---|---|
| Tier 1 | 4 | 1 | **1** — Sensor Tower 77 |
| Tier 2 | 12 | 8 | **6** — Owner.com 65 · Close 65 · Signifyd 65 · Alan 55 · Zuora 50 · Carta 50 |
| Tier 3 | 16 | 23 | **25** |

### Also picked up from the cost-test handoff — two new open items

`handoffs/0926-costtest-graded-accounts.md` appeared today and had not been read here. **Its block has lifted:** it says *"do not score these until the proposed fourth rule is settled"*, and that rule was settled and applied today, so **the 7 new accounts are scoreable** (Mollie · Chrono24 · Facile.it · Meilleurtaux · Origami Risk · OEC · Capital on Tap) — AGE coverage 9/9 populated, far better than this roster's 14/32 blank. New open items 13 and 14 in `0926-target-accounts.md`. Item 14 is the one worth acting on: **stale public/private status is now a five-occurrence defect**, and anti-ICP fires at −40 on "publicly listed", so a stale ownership field is worth 40 points either way. Cheap pass — re-check listing status for every roster account carrying `MRG●` on a sponsor mandate.

---

## 2026-09-03 (later 8) — rules 4 and 5 approved and applied: Tier 1 is one account

**Both rules approved by Rudra and written into `.claude/skills/lead-scoring/SKILL.md` (now v1.2, backup at `SKILL.md.pre-rules-45`).** The stale "119 companies / six runs" provenance in that file is corrected in the same pass, closing a `(later 6)` escalation.

- **Rule 4 — UNKNOWN scores ZERO,** neither penalty nor credit. `◐` is partial *evidence*, never absent evidence. Rules 1 and 3's corollary were written about **ranking**; Model B was applying them as **scoring**. Corollary added: wrong-shape evidence is not partial evidence — a cumulative lifetime total against a per-period definition scores 0, not 5.
- **Rule 5 — direction-check every technographic co-sell signal.** Presence is not alignment. A MongoDB footprint an account is retiring is worse than absence: it makes the partnership credential the weakest available opening.

### The cost, and it is not small

**Nine accounts moved down a tier. Tier 1 went from four accounts to one.**

| | 09-02 | Corrected |
|---|---|---|
| Tier 1 | 4 | **1** — Sensor Tower 77 |
| Tier 2 | 12 | **8** — Owner.com 65 · Close 65 · Signifyd 65 · Alan 55 · Zuora 50 · iCapital 50 · Carta 50 · ID.me 50 |
| Tier 3 | 16 | **23** |

**`Transaction Volume` contains no volume figures anywhere on the roster.** 20 blank, 9 `UNVERIFIED`, 3 `VERIFIED` — a status word, not a measurement. The substance is in `Transaction Evidence Review`: **3 verified per-period · 5 cumulative-only · 3 no-evidence · 1 implausible · 20 blank.** A 10-point signal evidenced for **3 of 32 accounts** (ID.me, Weee!, Zūm). AGE was paying the full 10 on a blank `Founded Year` for eleven accounts. MongoDB had been scoring blanks at zero correctly all along — hence the defect reading as inconsistency across signals rather than one wrong constant.

**The ranking held better than the scores.** Sensor Tower is rank 1 under every correction; 55 of its old 92 was real evidence — `EST●` from a live requisition, `HIR●` from a P1 posting with a genuine date, `MDB●` confirmed and now direction-checked. It lost 15 points resting on two empty columns. **Sequencing judgment survives. The scores must not be quoted outside this repo until open item 10 closes** — Sensor Tower is simultaneously rank 1 and the least-evidenced account on the list.

**Owner.com fell out of Tier 1 on MongoDB, not on age.** Its founding year was approved at 2018 (`AGE●`, +5) and it still dropped 85 → 65, because its own Staff Database Engineer requisition names *"migrating workloads (e.g., MongoDB → Postgres)"* and asks for *"deep expertise with a major relational engine (Postgres strongly preferred)"*. Best estate evidence on the roster and a MongoDB disqualifier in one document. **The signals are separable and both readings are right:** `EST●` holds at 25 because the pain is real and named; `MDB⊘` scores 0 because the direction is away. **It is still a good prospect — the M2 entry offer never required MongoDB — so what changes is the opening, not the fit. `0926-abm-owner-com.md` must not lead with the partnership credential.**

### Direction check: run, coverage 3 of 13

The committed postings CSV holds requisition text for only **3 of the 13** MongoDB-positive accounts; the other ten came from scale-led and firmographic pulls, which carry no postings. Owner.com — **reversal confirmed**. Sensor Tower and Close — MongoDB named, **no migration sentence, neutral, keep 15**. The remaining ten keep their presence score per rule 5's scope note, on **unverified direction**.

**Open, and it is the live one:** rules 4 and 5 pull against each other on exactly those ten. Rule 4 says UNKNOWN scores zero; rule 5 says direction is a disqualifier tested only on positive evidence, so no requisition means no disqualifier. I have applied rule 5's reading and flagged it rather than silently choosing — **the tighter reading would take Tier 2 from 8 accounts to 4** (Zuora, iCapital, Carta and ID.me all fall to Tier 3). **Reconciled by Rudra 2026-09-03 in favour of rule 5's reading** — zeroing a detector-confirmed signal because a second, different question is unanswered would be a penalty for absence of evidence, which rule 4 itself forbids. No rescore needed; the applied tables stand. **Request queued for workstream 1: Job Posting Search on the ten, 1 credit per posting** — Owner.com is the proof that a false positive here is worth 15 points on a hostile signal.

### Owner.com's ABM plan reframed — and it needed less than the rescore implied

**The plan called the direction problem on 2 September, before the score did.** It already carries a section titled *"The objection to handle before anything else"* stating that WeKan is MongoDB-backed while Owner.com is migrating off MongoDB, and instructing *"do not lead with MongoDB mastery."* What was wrong was the 15-point score, not the strategy. Updated: header rescored 85 → 65 with a note that **cohort governs motion** so the account stays sequence-eligible on its Cohort A hiring trigger; founding year resolved to 2018 in the snapshot and the age disqualifier struck; Series D lead (Goldman Sachs Asset Management) added, which strengthens the CFO efficiency angle; open items 1 and 4 closed. Backup at `0926-abm-owner-com.md.pre-0903`.

**One real gap found, and deliberately not escalated as a blocker.** The plan predicts the technical validator will ask *"Have you done Mongo-to-Postgres, or only the other direction?"* — and checked against `messaging.md` §6, **the proof library has no answer.** Every named migration in Pool B runs *off* a relational engine (the aviation licensing reduction, the insurance MSSQL-to-microservices re-engineering) or optimises a MongoDB estate in place (the logistics cluster work). The 50,000-table / 10,000-stored-procedure aggregate is relational-origin by construction — stored procedures are a PL/SQL and T-SQL artefact. **No proof point describes a migration off MongoDB.**

So belief 4 is an argument from **architecture, not track record**: the factory's seven agents operate on schema, code and data-model analysis, none of it engine-specific, so the direction of this pair is new but the surface area is not. Honest, defensible with a CTO, and weaker than a named analogue — it must not be dressed as one. **Not escalated as a blocker**, because the technical validator appears at the working-session stage and not in email 1 — the same reasoning that retired the false escalation earlier today. Written into the plan as a stated limit with a three-step handling order, and a note that only Rudra may add a named engagement if one exists.

**Also recorded:** the Enrich Tech Stack pull returned *less* for Owner.com than its own advert already gives us — detected estate `MongoDB;Snowflake`, with **Postgres missed entirely** despite being named as the preferred engine in the requisition. For this account the requisition beats any enrichment, which is the general lesson too.

**Items closed in `0926-target-accounts.md`:** 2 (MongoDB unknown), 5 (Owner.com founding year), 8 (blank credit), 11 (direction check, partial). **Still open:** 1 (campaign motion), 6 and 7 (Sensor Tower and Close size checks), 10 (Sensor Tower's four verifications), 12 (`Legacy Relational` second pass).

---

## 2026-09-03 (later 7) — MongoDB resolved: 13 of 32, zero new Tier 1s, and the signal can fire backwards

**Open item 2 is closed.** The ~80-credit Enrich Tech Stack pull landed: `data/0926-enrich-targets-enriched-raw.csv` (39 rows) and `data/0926-mongodb-status-39-accounts.csv`, both committed so nothing needs re-attaching. **13 of 32 confirmed MongoDB present · 14 confirmed absent · 5 UNKNOWN.** The three accounts already claimed — Sensor Tower, Owner.com, Close — are all confirmed. The top of the list was right.

**The headline is what it did not buy. Zero accounts entered Tier 1.** Eight promoted Tier 3 → Tier 2: Pushpay 60 · Zuora 60 · iCapital 60 · Workrise 55 · Carta 55 · ID.me 50 · Zeta 50 · ezCater 50. Tier 2 grows 4 → 12, Tier 1 stays at 4, Tier 3 falls 24 → 16. The highest-weighted unscored signal in Model B, filled in across the whole roster, changed nobody's motion at the top. Second time this trial that closing the biggest data gap left the pursuit order intact — the constraint on this list was never coverage.

**Two of the eight promotions are Cohort C.** Zuora and iCapital both promote on MongoDB *plus* co-present MSSQL/MySQL, which is an ICP-M1 shape, not M2. This strengthens §8.6 (re-score them as M1) rather than adding them to M2 sequences.

### The finding that matters: the MDB signal is direction-agnostic

**Owner.com is migrating off MongoDB.** From its own committed requisition: *"Deep expertise with a major relational engine (**Postgres strongly preferred**) in high-volume production; experience migrating workloads (e.g., **MongoDB → Postgres**) a strong plus."* Model B pays Owner.com 15 points for a MongoDB footprint it is actively shrinking — at the one account where WeKan's MongoDB credential is the weakest opening rather than the strongest. Design flaw, not data error. **Proposed: MDB scores 15 where direction is toward MongoDB or neutral, 0 where a named migration away from it exists.** Zero credits to check; requisition text is already in the repo.

Three more audit findings, all in `0926-target-accounts.md` under the enrichment section: five "no" values are **UNKNOWN** (the detector returned no primary database at all for CMT, Lighthouse, FreedomPay, Sure, FarEye — score unaffected, provenance record corrected) · **`Mid-Migration` is inference** and renamed to *co-presence*, because MongoDB beside MySQL is polyglot persistence, not a migration in flight · **the detector has measurable false negatives** — it missed Postgres at Owner.com, a database named verbatim in their own advert, which downgrades confidence in all fourteen `MDB○` calls and every blank `Legacy Relational`.

### And the blank-credit exposure is worse than reported this morning

The `(later 6)` entry said blanks earn half credit. Audited properly against the source CSV, it is not half: **AGE took the full 10 points on a blank `Founded Year` for eleven accounts, including Sensor Tower, Close and Signifyd.** Totals: AGE credit on a blank `Founded Year` for **14 of 32**, VOL credit on a blank `Transaction Volume` for **20 of 32**. Correction to that entry: the MongoDB signal scored blanks at **zero**, correctly — so the model is *inconsistent across signals*, not uniformly generous. AGE is the worst offender, VOL the widest.

**All four Tier 1 accounts are blank on both columns, and of the 18 accounts with a real `Founded Year`, none is Tier 1.** Selection, not coincidence. Applying the proposed rule to AGE and VOL, with the two founding years verified today: Owner.com **80** (T1, and rank 1) · Sensor Tower **77** (T1) · Close **65** (T2) · Signifyd **65** (T2). **Tier 1 goes from four to two.**

**The ranking is more robust than the scores.** 55 of Sensor Tower's 92 rests on real evidence — EST from a live requisition, HIR from a P1 posting with a real date, MDB now confirmed. It is the last 17.5 that rests on two empty columns and a stale ownership figure. Sequencing judgment survives. The numbers should not be quoted in anything that leaves the building.

**Sensor Tower is rank 1 and the least-evidenced account on the roster** — blank founding year, blank transaction volume, revenue and funding both below the M2 size floor and both pre-acquisition, `SCL◐` on the PE limb alone, and `MRG●` at 20 points whose provenance is recorded only as "margin/sponsor trigger confirmed". Its ABM plan should wait on four verifications, not proceed and be patched.

**New open items 9–12** in `0926-target-accounts.md`: the blank-credit tier scenario · Sensor Tower's verification set · the free direction check on all 13 MongoDB accounts · a second pass on `Legacy Relational` against requisition text rather than the detector. **Seven net-new accounts** arrived with the enrichment (Origami Risk, Facile.it, Chrono24, Mollie, OEC, Meilleurtaux, Capital on Tap) — none has been through the M2 gates, so they enter as gate-pass candidates, not roster additions. OEC carries co-presence and is worth looking at first.

---

## 2026-09-03 (later 6) — the repo is uncommitted; context-refresh run; two verifications

**Session opened from `handoffs/0926-handoff-gtm-execution.md`.** §8 item 2 executed, §8 item 4 finished properly, §8 item 7 closed on one of two and escalated on the other. Mode 3 confirmed for scoring and strategy; Mode 2 on anything carrying a client name or a metric.

### The finding that outranks both verifications

**Blanks are earning half credit in Model B.** Coverage across the 32 qualified rows in `outbound/research/data/0926-origami-companies.csv`: `Founded Year` blank **14/32** (AGE, 10 pts) · `Database Technology Mentions` blank **29/32** (MongoDB, 15 pts) · `Transaction Volume` blank **20/32** (VOL, 10 pts). **35 of 100 points rest largely on inference.**

The mechanism is a category slip, not a typo. `lead-scoring` rule 1 (*"a blank field is UNKNOWN, not FAIL"*) and its corollary (*"UNKNOWN is not zero"*) were both written about **ranking** — don't sort a blank below a real value. Model B applies them as **scoring**, where "partial evidence scores half" converts every blank to `◐` and 5 points. **Proposed fourth rule: UNKNOWN scores zero — neither penalty nor credit. `◐` is for partial evidence, never for absent evidence.** Skill edit, so proposed not applied. Same family as the anti-ICP calibration bug and the `Matching Posting Count` retirement: the model was being fed inference and paying for it.

### Verifications (§8.7)

**Signifyd — closed. Immaterial confirmed, not assumed.** The conflicted figure is **total funding, not revenue**: `Employee Count=500 | 495 ;; Total Funding=411000000 | 409000000`. A round-by-round public record sums to ~$390M (seed $2M late 2012 · A $7M · B $20M 2016 · C $56M 2017 · D $100M 2018 · E $205M April 2021, $1.34B valuation). All three figures clear the SCL threshold by ~4×, so the drift cannot move the gate. Employees → `500+ (company-stated)`, which contains both point estimates. Founded **2011**, so `AGE●` now rests on evidence rather than a blank. The CSV's `Annual Revenue: 150M` is an unattributed vendor estimate and is not used.

**Owner.com — verified, escalated, not applied.** `Founded Year` is blank in both CSVs, so `AGE◐` was awarded on nothing. Two sourced readings: **2018** (ProfitBoss founding, FOX Business 11 Dec 2020; corroborated by Owner's own Series C memo, *"Building for restaurants for over 7 years"*, ~May 2025) and **2020** (Wikipedia infobox; echoed by Owner's own job description, *"Since 2020, we've generated tens of millions"*). Rebrand to Owner.com was 2021. **2018 → `AGE●`, 85 → 90. 2020 → `AGE○` plus the founded-2019-or-later anti-ICP hit at −40 → 40, Tier 3, and `outbound/strategy/0926-abm-owner-com.md` is void.** Recommending 2018: the company's own claim is the strongest source, the ProfitBoss codebase *is* the MVP era, and "greenfield infrastructure has nothing to unwind" is contradicted by a live Staff Database Engineer req naming a MongoDB-to-Postgres migration. Also found: `Funding Stage: series_b` is two rounds stale (Series C May 2025, $120M at $1B; a Series D led by Goldman Sachs Asset Management since). A fresh round is itself an M2 trigger — candidate MRG upgrade, needs the round date.

**Two more accounts need a size check before their ABM plans, both recorded as open items 6 and 7 in `0926-target-accounts.md`.** Sensor Tower — rank 1, plan pending — carries `Annual Revenue: 35.6M` and `Total Funding: 46000000`, both *below* the M2 size floor; `SCL◐` stands only on the `private_equity` limb, and both figures read as pre-acquisition, pre-data.ai. Close carries `seed / $250K` for a thirteen-year-old CRM and scores `SCL○` on it; if the bootstrapped-profitable limb applies, 80 → 85 and the model-vs-hand disagreement resolves for the model.

### Blocking

0. **Nothing from the last three days is committed to git. Fix this first.** `git log` ends at `e0c4f74`, the upstream quickstart setup. **Every WeKan file is untracked** — `company.md`, `messaging.md`, `positioning.md`, `brand-voice.md`, `escalation.md`, `ICP.md`, `goals.md`, `latest.md`, `history.md`, both ABM plans, `0926-target-accounts.md`, the pursuit-order snapshot, both source CSVs, all four handoffs, and the three new skills (`lead-scoring` Model B, `origami-sourcing`, `sourcing-csv-audit`). The handoff describes the snapshot as "committed so the artifact's content survives session loss"; git disagrees. Working-tree only, on one machine, with three sessions writing to it concurrently. One `git add -A && git commit` closes the largest single risk in the repo.

0b. **Three sessions are writing this repo at once, and it already cost an entry.** Mtimes between 07:02 and 07:11 UTC show workstream 1 and workstream 3 writing `orchestration.md`, `origami-sourcing/SKILL.md`, `sourcing-csv-audit/SKILL.md`, `history.md`, `handoff-origami-sourcing.md` and prompt v3 while this session was writing. **Two entries below were both numbered `(later 4)`** — this one is renumbered `(later 6)` and moved to the top to restore ordering. Convention worth adopting: number by wall-clock at write time, or append the workstream, e.g. `(w2)`. Nothing was lost, but a session that read `latest.md` before another's write and saved after it would silently drop an entry.

1. **`ICP.md` is canonical since 2026-09-02 but still declared DRAFT in five live places.** Any agent reading them will disclaim research-grade content as inference. `marketing/CLAUDE.md:24` · `.claude/rules/orchestration.md:30` · `.claude/agents/gtm-engineer.md:13` and `:26` · `.claude/agents/product-marketer.md:32` · `.claude/agents/context-refresh.md:17`. Four are agent or rule files — escalation.
2. **Count drift — fixed where autonomous.** `0926-target-accounts.md:5,110` → 120 screened / 8 pulls / 17 CSVs / 32 qualified. `0926-abm-owner-com.md:22` → 120. `0926-m2-pursuit-order-snapshot.md` given a superseded banner (body untouched; it is programmatically generated). **Still open: `.claude/skills/lead-scoring/SKILL.md:72,131` says "119 companies across six Origami runs"** — skill file, escalation.
3. **A conflict closed 2026-08-31 is still recorded open, and is gating a skill.** `positioning.md:68` says "Helix vs Build Mode naming unresolved"; `product-launch/SKILL.md:50` lists it under *when not to run this skill*. `company.md:82` is the resolution of record. Canonical + skill, so both escalation.
4. **`positioning.md` carries five differentiators; `company.md` carries six** — #6 "Products, not just projects, 40%+ of engineering on internal IP" is missing. `company.md` wins on conflict by its own rule and `positioning.md` agrees, so positioning is wrong by its own rule. `marketing/CLAUDE.md:11` propagates "the five differentiators".
5. **The only API-credit escalation gate is denominated in a retired tool.** `rules/escalation.md:28` — "~200 Exa queries in one run". Exa is explicitly not wired. 400 origami credits already spent with no threshold in force and a 300-credit sample queued. Re-denominate in origami credits.
6. **Exa is still declared in 19 of 21 SKILL.md frontmatters** as `optional_mcps: - exa`, against `.claude/connections.md:170` ("Do not reference them in skills or agents").

### Overdue

- `.claude/rules/quarterly-maintenance.md` — populated 2026-05-18, **108 days against a 90-day ritual, overdue 18**, and its Rule 1 ownership table is 22 rows of `{Name}` placeholders. It is step one of the ritual `context-refresh` defers to, and it is unrunnable.
- **Eight upstream skills untouched 107 days** (`last_updated: 2026-05-19`): brand-kit, competitor-aggregate, competitor-research, funnel-strategy, icp-research, positioning, product-messaging, tov-guidelines. All eight also carry the stale `- exa` — one pass fixes both.
- `lead-scoring/SKILL.md` frontmatter still reads `last_updated: 2026-08-31`; it gained Model B on 09-02 and rule 3 on 09-03. The date is wrong, so nothing will flag it again.
- Three `.claude/rules/*.md` state a cadence with **no last-refreshed date**, so they can never compute as overdue: `one-page-rule.md:38`, `pii-redaction.md:44`, `evidence-bound-outputs.md:37`. `marketing/rules/gate-rules.md` has **no cadence at all**.

### Missing

`competitors/` (`/competitor-research` ×3-4 → `/competitor-aggregate`; candidates named at `positioning.md:66`) · `funnel/` (`/funnel-strategy`, unblocked since `ICP.md` landed) · **`win-loss/` (`/win-loss-analysis` — not blocked, the Drive connector is live; highest-leverage run available, it converts every asserted differentiator into evidence)** · `expert-pov/` (`/expert-pov` on the CEO tech-vision memo) · `goals.md` baselines (**11 live `[UNAVAILABLE]` markers, all in `goals.md`** — no lane strategy is evaluable without them; hand-author) · `gate-rules.md` Rules 4+ (the Manager Prompt; its own closing line: "agents are enforcing three rules and guessing at the rest").

### Hygiene

**Broken relative links: zero** across 93 files scanned. **One-page rule: clean** — largest `CLAUDE.md` is 46 lines against 80. Remaining: ~15 slash commands referenced with no skill directory, mostly upstream boilerplate, plus `/paid-*` and `/lifecycle-*` in two out-of-scope lane `CLAUDE.md`s that should just say "not built yet" · `lead-scoring/SKILL.md.bak` sits inside the skills tree where a glob finds it · `env` still lists four retired API keys 20 lines above the line retiring them · `README.md` still onboards a new operator onto Exa in six places, contradicting `connections.md:149` · `.claude/CLAUDE.md:27` points at `README.md` for an owner name the README does not contain.

### Converging with the other two workstreams

Read `(later 4)` and `(later 5)` below alongside this entry — three sessions landed on one conclusion from three directions.

- **Workstream 1 named a third member of the family; this entry says the first member is being misapplied.** It added *"a date column where every value equals the retrieval date is UNKNOWN, not data,"* siblings to *"a blank field is UNKNOWN, not FAIL"* and *"never accept a derived judgment column."* The finding above is that the founding rule of that family was written about **ranking** and Model B applies it as **scoring**, so blanks earn 5 points. Fixing the family's members without fixing that conversion leaves the leak open.
- **`Date Posted` is the retrieval date on Job Posting Search pulls (P7/P8: `2026-09-02` on all 13 rows), which puts HIR's recency half in question — but not for Tier 1.** HIR is 15 points and is scored on *live* hiring. Checked: Sensor Tower, Owner.com, Close and Signifyd all carry `Seen In Pulls: P1`, and P1 returned 17 distinct dates spanning 2026-07-06 → 2026-09-01. Owner.com's requisition is dated 2026-07-31. **Tier 1 and Tier 2 HIR evidence holds; the defect bites the 300-posting sample and any future trigger-first pull.**
- **`sourcing-csv-audit` is now a gate upstream of `lead-scoring`** (`orchestration.md`: `icp-research → origami-sourcing → sourcing-csv-audit → lead-scoring → abm-campaign → outreach-emails`). The blank-coverage table above — AGE 14/32, MongoDB 29/32, VOL 20/32 — is exactly what that gate should refuse to pass. Worth checking whether its ten checks already cover column coverage, and adding it if not.

### Still open from §8.8

**`project_write` still returns HTTP 403.** Re-tested this session: `project_info` and `project_search` work, doc creation is rejected upstream. The handoffs and `0926-target-accounts.md` still have to be added to the Claude project by hand.

**`pulse-analytics-example/` — do not delete yet.** Root `CLAUDE.md:39` says delete when no longer needed, but 26 links across 15 `CLAUDE.md` files, 4 `SKILL.md` files and the README point into it, and it is the only format reference for the four empty canonical slots. Fill those first, then delete and strip the pointers in one pass.

---

## 2026-09-03 (later 5) — two sourcing skills built; the spec's template was already superseded

**`origami-sourcing` and `sourcing-csv-audit` written to `.claude/skills/`, both `status: draft`.** The skill-spec handoff proposed one skill. Split into two because the halves trigger on different inputs — *"write me a prompt"* vs *"here's what came back"* — and the audit half is tool-agnostic: nothing in it depends on Origami, so it works against TheirStack, Clay or a hand-built sheet.

**The spec's template was out of date by the time it was implemented.** It generalises `P10`'s four steps. Prompt v3, written later the same day, has seven — and the three new ones (role-filter audit, requisition dedup, verbatim dates) exist because of defects measured *after* the spec was written. `origami-sourcing` now carries the v3 shape as its template with `P10` as the census variant. Constraints 12–15 encode the date-spread rule this file asked for, plus one-row-per-unit, unit-and-divisor discipline, and no-boolean-without-its-quote. **Constraints 10 and 11 keep their numbers** — they are referenced from here.

**The audit checklist went from seven checks to ten.** New: 7 duplicate units (rows are not requisitions), 8 date spread against the pull timestamp, 9 unit and divisor integrity. All three are free checks against data already paid for, which is how nine of the eleven catalogued defects were found.

**Registered in `.claude/rules/orchestration.md`** under `gtm-engineer`, with the dependency note `icp-research → origami-sourcing → sourcing-csv-audit → lead-scoring`. No account list reaches `lead-scoring` without passing the audit.

**Open, both needing Rudra:**

1. **Lane overlap.** `lead-scoring`'s description still says it "sources accounts via origami.chat" and triggers on *"build a prospect list"* and *"target account list"*. With `origami-sourcing` in place that is two skills claiming one job. Editing a skill is non-autonomous, so the wording is proposed, not applied.
2. **Skill count stale in two canonical files.** `CLAUDE.md` and `.claude/CLAUDE.md` both say 21 skills; it is 23. Canonical, so untouched.

**Stale line found:** `orchestration.md` says `marketing/icp/ICP.md` "is a draft skeleton today". It is not — ICP.md is 18KB covering all six ICPs, and the skeleton sits in `ICP.draft-skeleton.bak`. The no-skill-runs-against-DRAFT rule still stands; only its example is stale.

---

## 2026-09-03 (later 7 · w1) — the best result came from a platform button, not a prompt; and the index may only reach back days

**The single most important correction of the day: the cost test was not a prompt.** It was an Origami platform option offering to reduce cost per lead. It produced a **42% company-level qualify rate — 6× the best prompt-driven result of the whole trial** (strict read 2 of 30). Three turns were spent authoring prompt amendments while the thing that actually worked was a UI affordance. **Find that option and characterise it before writing another prompt.** Open question: is it re-runnable, and what did it change — the search shape, the enrichment depth, or the draw?

**Prompt engineering is not the binding lever it was assumed to be.** The prompt log's 14 entries record real fixes to real failures, but none of them moved the qualify rate the way one platform setting did. Weight future effort accordingly.

**Cost model corrected — the handoff was wrong by ~5×.** The handoff priced the 300-posting sample at 300 credits from the "1 credit per job posting" line. Observed rate is **~5.2 credits per returned row**, because Origami also charges firmographic enrichment per company and the v3 prompt demanded it on every row. A 300-row pull is therefore **~1,560 credits, not 300** — 16% of budget for a population estimate. v3 is withdrawn as written. Rudra caught this from cost data; credit where due.

**Cost per qualified account is the better decision variable.** ~114 credits for 9 qualified companies ≈ **13 credits per qualified account**. Reaching the 200-account volume threshold ≈ 2,800 credits. That is a measurable, self-calibrating number available from every pull, and it replaces the population-sizing exercise that had been gating the C1 decision on two unverified aggregates.

**RECENCY FINDING — the index may only reach back a few days, not 90.** Three consistent data points:
1. Cost test: all 22 rows dated 2026-08-31 → 09-02, a **3-day span** for a nominal 90-day search.
2. P7 and P8: all 13 rows stamped with the pull date.
3. A pull instructed to *exclude* 31 Aug – 2 Sep and go further back returned **one row**.

Reading: the trigger search reaches recent postings and cannot be steered to a historical window. **If confirmed, the "7,377 postings over 90 days" flow figure is not samplable** — you cannot sample a window the tool cannot see — which is a deeper problem than the deduplication defect logged in later 4. Free question now pending with Origami: how far back does the job-posting index reach.

**Strategic consequence, and it is a good one.** If the tool surfaces only fresh postings, the right motion is **a small recurring weekly pull, not a one-shot top-up.** Harvest the flow as it arrives: freshest possible trigger, no date gymnastics, spend spread over time, and it suits an ongoing C1 sequence better than a single blast. This reframes C1 from "size the universe, then decide" to "run the harvest, decide by observation at 60 accounts and again at 200."

**Also learned: a short labelled-example prompt underperformed.** "Here are the excellent / good / poor ones, find 10 more like the good" plus a date exclusion returned 1 lead. Most likely the date exclusion starved it (see recency finding) rather than the brevity. Asking straight for 20 more, with no date constraint, is the live test.

**Handover written:** `handoffs/0926-costtest-graded-accounts.md` — 9 qualified (7 new: Mollie, Chrono24, Facile.it, Meilleurtaux, Origami Risk, OEC, Capital on Tap), 9 excluded with reasons, Bondora pending one web-research credit. Gate evidence only, no scoring, per §10.

**New rule — debt financing satisfies the funding gate for lenders.** Capital on Tap: $611M raised, latest round debt_financing, which is not a series and fails the gate as literally written. Decided qualified — debt is a lender's growth capital and the gate exists to test scale and capital access. Flagged `CAPITAL-PATH: DEBT`. Rejecting the rule would systematically exclude the lending half of fintech. Bondora is the next case.

**Counting discipline: rows are not leads.** The 22-row cost test is 19 companies (Alan ×3, one byte-identical requisition; Kraken ×2). After removing the poorly-graded companies Origami left a 12-row table — that is **10 companies**, not 12 leads. Any cost-per-lead figure computed on rows overstates by ~16-20%.

**Public-status filter has now failed in five consecutive pulls** (WeRide, PlusAI, ACV Auctions, Angi, and now Everbridge). It is a rules-level defect that no prompt has fixed. Everbridge may additionally be stale — Thoma Bravo took it private in 2024, same error class as Pushpay.

---

### Consequences for the other two workstreams

**Workstream 3: `origami-sourcing` is carrying a withdrawn template.** `(later 5)` adopted prompt v3's seven-step shape as the skill's template. **v3 is withdrawn as written** — it prices at ~1,560 credits, not 300, because it demands firmographic enrichment on every row at ~5.2 credits each. Keep constraints 12 and 15 (date spread, no-boolean-without-its-quote) and the audit's checks 7-9; they are what found the defects. **Re-open constraint 14 (unit-and-divisor discipline):** it was written to convert a posting population into a company population, and the recency finding above suggests that population is not samplable at all. It is sound method for a tool that can reach a historical window; it may be unusable against this one. `P10` should go back to being the template until the platform option in this entry is characterised.

**Workstream 2: my handover has the exact blank profile your Model B finding warns about.** Coverage on the 9 newly graded accounts in `handoffs/0926-costtest-graded-accounts.md`:

| Model B input | Coverage | Note |
|---|---|---|
| AGE (10 pts) | **9/9 populated** | 1999-2016, all clear of the 2018 boundary. Better than the roster's 14/32 blank. |
| MongoDB (15 pts) | **0/9 named** | Alan PostgreSQL · Meilleurtaux BigQuery · Facile.it the bare word "database" · six named nothing. |
| VOL (10 pts) | **0/9** | No volume column was requested, by design — VOL was retired as a gate. |
| SCL (5 pts) | 5/9 have a funding figure | Origami Risk, Facile.it, OEC, Meilleurtaux resolve on `PE-owned` only. |

**So 25 of 100 points are absent, not partial, on every one of these nine.** Under the current "partial evidence scores half" conversion they would each collect ~12 points of `◐` for evidence that does not exist — which is your proposed fourth rule (*UNKNOWN scores zero*) applied to a fresh cohort before it enters the model. **Do not score these nine until that rule is settled.** The handover file states gate evidence only and deliberately carries no scores.

**The MongoDB gap is buyable, and it is the cheapest high-value spend on the table.** `Enrich Tech Stack` at 2.5 credits/company → **~23 credits for all nine**, or ~103 credits for the full 41-account roster. That converts a 15-point inference into data across the board and is 1.5% of what v3 would have cost. It is now the highest-ROI credit spend identified in this workstream.

**Agreed on git.** Three sessions, one uncommitted tree, and this entry nearly lost a neighbour to a label collision. Renumbering to `(later 7 · w1)` per your convention and adopting the workstream suffix.

---

## 2026-09-03 (later 4) — the trigger numerator has the same defect as the column we just retired

**Two data defects measured from the committed job-postings CSV at zero credits.** Both hit the 300-posting sample, which is still the open blocker on the C1 volume-vs-ABM question.

**1 · The posting index double-counts requisitions.** Alan's *Senior Platform Engineer (x/f/m) - Data Retention* came back twice in pull P7 — two LinkedIn IDs (`4461283739`, `4462180441`), same date, and **byte-identical descriptions**: 8,238 characters, SHA1 `2dcfb33b902b` on both. One requisition, charged twice. Lighthouse's *Lead Platform Engineer* came back twice as well (`4452600278`, `4452601242`, 7,458 vs 7,563 chars — near-identical, probably one role in two locations). **Rate: 14–29% of P7's rows carry no new requisition.**

**This is why Origami could not state its deduplication method — there isn't one.** And 7,377 is an aggregate over the same index, so **the numerator of the C1 calculation is exactly as unverified as `Matching Posting Count`, which was struck from Model B yesterday.** The handoff's §2 table labels 7,377 confidence "Sourced". Downgrade it. The duplication cancels in `7,377 × (unique companies ÷ rows)` *only if* 7,377 counts rows the same way the sample does — which is a free question, now in the prompt.

**Also: Alan's 25.7 postings per 100 employees now has a mechanism, not just a verdict.** The magnitude-check rule caught the symptom; duplicate requisitions are the cause. Second instance behind the rule.

**2 · `Date Posted` is the retrieval date on trigger-first pulls.** P1 (Company Search) returned 17 distinct dates spanning 2026-07-06 → 2026-09-01. P7 and P8 (Job Posting Search) returned **`2026-09-02` on all 13 rows** — the pull date. Likely cause: LinkedIn renders relative dates and Origami records the crawl date when it cannot parse an absolute one.

**Consequence: the recency half of the trigger is unverified.** "Live infrastructure hiring" is 15 points in Model B, and posting dates are unusable on exactly the pull type that sources it. Whether the 90-day window filter runs against real publication dates or against index-first-seen dates is now a free question in the prompt. P1 proves Origami *can* return real dates — this is a Job Posting Search defect, not a capability gap.

**New standing constraint for `origami-sourcing`:** never accept a date field without checking its spread against the pull timestamp. A date column where every value equals the retrieval date is UNKNOWN, not data. Same shape as "a blank field is UNKNOWN, not FAIL" and "never accept a derived judgment column" — the third member of that family.

**Prompt v3 written:** `handoffs/0926-origami-300-posting-prompt-v3.md`. Five amendments over the handoff's §9 item 1, all prompt text, zero extra credits: one-row-per-posting restored (it had been dropped from P11), unique-companies divisor added (the v1 report block asked for postings and the threshold table is in accounts — a unit mismatch that would have made 300 credits buy nothing), a draw rule against sort-under-cap, requisition-level dedup with visible working, and verbatim posting dates. Awaiting Rudra's run.

## 2026-09-03 (later 3) — Matching Posting Count retired; role filter has one leaky term

**Origami verified as far as it could and stopped.** Role list confirmed and sound (SRE · Site Reliability · Platform Engineering · DBRE · Database Reliability · Infrastructure Engineer). **Domain scope and deduplication method: cannot be determined** — only an aggregate was ever stored. Its own words: *"396 for Alan and 66 for Chainlink Labs should be treated as unverified aggregate counts, not reliable company-specific posting counts."* It declined to estimate and saved itself a rule that future counts must show role scope, domain scope and deduplication method.

**`Matching Posting Count` is struck from Model B inputs — UNKNOWN for all 32 accounts, not a pending verification.** The breakdown was never stored, so the values are unrepairable rather than unconfirmed. HIR stays at 15. Alan stays Tier 2 on its gate evidence, which is independently sound.

**Better news than expected on the filter.** The role list being correct means it is not broadly over-matching — **one term is leaky.** "Platform Engineering" catches front-end platform roles; Lighthouse's *Lead Platform Engineer* is Ember/React/TypeScript. The 300-posting prompt now qualifies that term explicitly and requires the three count disclosures. So the earlier 2-of-30 qualify rate was depressed by one bad term, not a broken filter.

**Method finding worth generalising.** The clause *"if anything cannot be established without a further retrieval, say so rather than estimating"* produced a clean itemised refusal from the same tool that once fabricated verification for 20 of 21 companies. It is now standing constraint #10 in the `origami-sourcing` skill spec, and it retired a bad signal for zero credits.

---

## 2026-09-03 (later 2) — the restricted-access escalation was a false alarm

**Withdrawn.** I escalated that `messaging.md` §6 had no proof point for delivering an assessment under restricted production-data access, and marked belief 5 of the Alan plan `[UNAVAILABLE]`. **The premise was wrong.** WeKan's motion is intro call → one or two follow-ups → production access if we're in; nobody expects access on call one and WeKan does not ask for it. In between, the pre-sales SA, chief architect and CEO work from whatever the prospect chooses to share and come back with scope and timeframe.

**Belief 5 rewritten** to *"Finding out what this would take costs me one call, and I stay in control of what I share"* — proved by the staged discovery path plus the existing Pool B insurance proof point. No new proof point required, no gap in the proof library. `[UNAVAILABLE]` markers cleared from `0926-abm-alan.md`; both plans are unblocked.

**Disqualifier re-worded in both plans:** refusing production access *after the technical working session* is the ICP-M2 disqualifier. Declining it early is normal and is not one.

**Process note.** The `abm-campaign` guardrail worked — it stopped an invented proof point from being written. But a guardrail firing is not evidence of a real gap. Check that the belief is one the buyer would hold *at that stage of the motion* before escalating.

---

## 2026-09-03 (later) — Matching Posting Count defined; HIR stays at 15

**Origami answered.** `Matching Posting Count` = infrastructure/SRE postings at the same domain, inside the same 90-day window, **postings not companies**, not limited to the rows shown, **UNKNOWN when the domain lookup fails**, ranking signal not a gate.

**The definition did not survive contact with the data.** Normalised per 100 employees: FreedomPay 0.5 · Kraken 0.5 · Lighthouse 0.7 · Chainlink Labs 9.7 · **Alan 25.7**. Alan's 396 infrastructure postings against 1,542 employees would be a quarter of the company hired as SREs in one quarter. Not credible.

**Decision: do not re-weight HIR in Model B.** The proposal to raise it rested on Alan's 396 vs FreedomPay's 3, and Alan's number is the one that fails. Alan stays Tier 2 on its gate evidence. The model was right; the hand ranking was leaning on a bad number.

**New rule in `lead-scoring` (now three, not two):** magnitude-check every count against a denominator before it ranks anything — *a clean definition is necessary and not sufficient*. Working band: ~0.5–1 matching posting per 100 employees is normal, above ~5 per 100 needs verification. Corollary added: **UNKNOWN is not zero** — Origami returns UNKNOWN on a failed domain lookup, so a blank must not rank below a 3.

**Open, cheap:** pull 20 of Alan's matching postings (20 credits) and read the titles. If they are not infrastructure roles the role list over-matches; if they are not Alan's, the domain lookup does.

---

## 2026-09-03 — sourcing data consolidated, third workstream added

**The 17 raw Origami CSVs are superseded.** Everything is now in the repo, so no chat ever needs them re-attached:

- `outbound/research/data/0926-origami-companies.csv` — all **120** unique companies, fact columns merged across the 8 pulls, with `Seen In Pulls`, `Pull Count`, `On Qualified Roster` and a `Field Conflicts` column.
- `outbound/research/data/0926-origami-job-postings.csv` — 36 job-posting rows with full descriptions and URLs, so any role-match claim can be re-audited from source.
- `handoffs/0926-origami-prompt-log.md` — all **14 verbatim prompts** written to Origami, annotated.

**The capability map is now measured, not asserted.** Of the 65 companies appearing in more than one pull, **60 had a derived-judgment field contradict itself between runs; only 5 had any factual conflict, and 3 of those were cosmetic.** `Transaction Evidence Review` alone contradicted itself on 60 companies. This is the empirical backing for the `lead-scoring` rule "never accept a derived judgment column from the sourcing tool."

**Three new failure findings, all reproducible from the committed data:**
1. Lighthouse's posting is titled *Lead Platform Engineer* and was marked `Role Match = true`; its description names Ember, React and TypeScript. **Never accept a role match on the title alone.**
2. Chainlink Labs returned `Database Technology Mentions = oracle` — Chainlink is a blockchain *oracle* network. **Require the verbatim sentence, not the extracted term.**
3. `Matching Posting Count` changed meaning between pulls (Alan 15,398 → 396; Lighthouse 1,119 → 9). Valid within a pull, meaningless across pulls. **The proposal to re-weight HIR in Model B on this column is on hold until Origami defines it.**

**Third workstream.** `handoffs/0926-handoff-origami-skill-spec.md` — spec for an `origami-sourcing` skill: trigger conditions, the four-step prompt template that worked, standing constraints, a CSV audit checklist, an eight-case failure catalogue and eval cases. Kept separate from the operations handoff on purpose; the two answer different questions.

---

## 2026-09-02 (later) — work split into two chats

Context limits forced a split. Two handoff docs now live in `handoffs/`:

- **`handoffs/0926-handoff-origami-sourcing.md`** — workstream 1. Origami prompts, CSV evaluation, credit spend, the trigger-first sourcing spec, and the pre-registered threshold test for whether campaign C1 can run as a volume email motion. Owns the source CSVs.
- **`handoffs/0926-handoff-gtm-execution.md`** — workstream 2. This repo, its skills and agents, applied to the 32 already-qualified accounts. Owns Model B, the ABM plans, and everything under `marketing/`.

**Boundary:** workstream 1 hands over account names plus sourced fact columns only. Scoring, tiering and cohort assignment happen in workstream 2. Neither chat writes into the other's territory.

**New file:** `outbound/research/0926-m2-pursuit-order-snapshot.md` — the full per-account snapshot from the Pursuit Order artifact, committed so the evidence survives session loss.

**Counts settled.** Re-derived from all 17 source CSVs by domain dedupe: **120 unique companies screened** (120 distinct names, 120 distinct domains, one-to-one) across **8 Origami pulls**, **32 qualified**, 400 credits. This supersedes the 124 written below and the 119 that was in the exec brief. The brief has been republished with corrected tally strip and cohort table (A 5 · B 7 · C 2 · D 15 · E 2 · suppression 1 = 32).

---

## 2026-09-02 — ICP.md replaced, M2 outbound seeded, lead-scoring gains a second model

**`ICP.md` is no longer a draft.** Replaced from `WeKan_Consulting_Practice_ICPs.docx` (August 2026, sales-ops-ready): the three-axis Fit/Intent/Accessibility framework and 100-point scoring, all six ICPs with buying committees, triggers, qualifiers and disqualifiers, the negative ICP, the full signal library and the standardized entry offers. Draft skeleton preserved at `icp/ICP.draft-skeleton.bak`. **This closes the longest-standing open item — `gtm-engineer`, `lead-scoring`, `abm-campaign` and `outreach-emails` are all unblocked.**

**`/lead-scoring` now has two models.** Model A is the existing M1 weighting (legacy estate, EOL pressure). **Model B is new, for ICP-M2:** named estate pain 25 · margin trigger 20 · live infra hiring 15 · MongoDB presence 15 · per-period transaction volume 10 · founded ≤2018 10 · scale 5 · anti-ICP −40. Derived from a 120-company sourcing trial and validated against hand ranking.

**Two rules added to `lead-scoring` that cost real credits to learn:**
1. A blank field is UNKNOWN, not FAIL. Dropping rows for missing data once reported 59 of 60 accounts as failing on a column that had never been populated.
2. Never accept a derived judgment column from the sourcing tool. Take facts; do the scoring here. A transaction-volume classifier failed three times in three different ways — the third marking 21 companies "verified" when 20 had no supporting text.

**Origami's real capability, corrected.** It *does* handle technographics — Enrich Tech Stack at 2.5 credits/company is the MongoDB signal Model B weights at 15. Job Posting Search is 1 credit/result, which caps trigger pulls. **Reasoning, filtering and export are free; only new data costs.** TheirStack is still the deeper option once wired, but it is not a prerequisite.

**Outbound seeded.** `outbound/research/0926-target-accounts.md` — 32 scored accounts, 120 screened, 400 credits, with the full disqualified section. `outbound/strategy/0926-abm-alan.md` and `0926-abm-owner-com.md` — two Tier 1/Cohort A plans.

**One escalation, blocking.** `messaging.md` §6 has **no proof point for delivering an assessment under restricted production-data access.** Four M2 accounts turn on that belief (Alan, Signifyd, iCapital, ID.me). Marked `[UNAVAILABLE]` in the Alan plan per the `abm-campaign` guardrail rather than improvised. **Rudra: does an anonymisable account of a metrics-only assessment exist?** If yes it belongs in §6; if no, that is a real gap in the M2 proof library.

**Still open:** no competitor research · no win-loss evidence · `goals.md` has no baselines · the ICP-M2 campaign motion question (volume email vs ABM) is unresolved pending a 300-posting Origami sample.

---

## 2026-08-31 (2) — Conflicts resolved, stack corrected, hooks live

**All three open conflicts are closed. Nothing in this workspace is provisional any more.**

1. **Proof firewall — confirmed as policy.** Anonymization always. The older positioning foundation's named proof points (HoneyQuote / SNCF / Amadeus) are retired. If WeKan wants to name a customer against an outcome, **Rudra adds those details by hand after clearing them** — no skill or agent ever assembles the pairing or asks to.
2. **Helix**, not Build Mode. "Build Mode" is in the words-to-avoid list.
3. **Counts locked:** 100+ engineers · 40+ clients · 160+ projects. The "+" absorbs the doc discrepancy — undershooting is fine, overstating is not.

**Stack corrected to reality.** Exa, Granola, Gong, Notion, Linear, Ahrefs, Firecrawl and GA4 were upstream assumptions, not the WeKan stack. All removed from skills, agents and config.

- **In use:** origami.chat (lead sourcing), Google Workspace, Slack, Google Meet
- **Planned:** TheirStack, HubSpot Smart CRM, SmartLead, HeyReach, Customer.io — none have an MCP connector; all go through an n8n / Make webhook bridge with the review gate in front
- **Research now runs on Claude Code's built-in WebSearch / WebFetch** — every skill was rewired, so **zero wiring is required to start working today**

**Correction worth acting on: you do have transcripts.** Google Meet saves transcripts to the organiser's Google Drive, and the Drive connector is already connected. `/win-loss-analysis` is not blocked — it only needs Meet transcription to have been switched on. This is the highest-leverage run available.

**Hooks are live.** `session-context.js` injects this file at session start; `canonical-guard.js` flags writes to canonical files (warn mode — one line switches it to block). Written in Node so they run on Windows without a POSIX shell.

**Still open:** no competitor research, no win-loss evidence, `ICP.md` still a DRAFT skeleton, `goals.md` has no baselines. Every differentiator in `positioning.md` remains internally asserted.

---

## 2026-08-31 (1) — Workspace seeded

Four-layer setup run against this repo. Layer 1 seeded for WeKan.AI from the `wekan-client-deck` skill references; Layers 2-4 built out (10 new skills, 5 agents, integrations mapped). Upstream bugs fixed: invalid YAML in `competitor-research` frontmatter, two broken relative links, and a `.gitattributes` for the CRLF phantom diff.

---
