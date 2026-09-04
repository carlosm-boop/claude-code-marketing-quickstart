# latest.md — working memory

Delta cache for the WeKan marketing OS. Newest at top. Agents read this before deciding what to do; you write here after anything significant.

**What goes here:** drift reports, deltas since last cycle, metric movements, recent decisions.
**What does not:** canonical content (that's in `positioning.md`, `ICP.md`, etc.) or long-term records (that's `history.md`).

---

## 2026-09-04 (later 5) — workstream 1's 14 corrections applied; the precedence rule was backwards

**All 14 rows of `data/0926-w1-master-corrections.csv` are in.** They did not edit the master CSV — correct discipline, and the corrections now load as **an input island with its own precedence tier**, so a rebuild reproduces them instead of a hand-edit burying them. Master is **116 rows**.

**The finding that matters is about precedence, not data.** Workstream 1 caught **Alan** at `EST●` on a roster hand-read with an **empty `est_sentence`** and `est_retrieval` reading *"roster hand-read, pre-pull"* — and Alan was never in the 44-domain pull at all. They ran the pinned 9-term list against Alan's full P9 posting text, 24,714 characters dated 2026-09-02: **zero hits.** Alan is `EST○`, Tier 2 → Tier 3.

**So the build had precedence backwards.** It preferred the roster over every measurement. The rule now, written into the script and the schema doc: **a measurement with a recorded retrieval path beats a roster hand-read that carries no sentence.** The roster is the narrative record of the reasoning; **it is not a retrieval path.** Order is now w1-corrections → dated 44-pull → roster-with-a-sentence → superseded undated pull → firmographics.

**Seven cost-test accounts move from `UNSCORED` to measured `EST○ / HIR●`.** Workstream 1 ran the pinned list against committed P9 text for all 19 cost-test companies — 3.8k to 24.7k chars each — and got **zero hits across every one.** Mollie, Chrono24, Facile.it, Meilleurtaux, Origami Risk, OEC, Capital on Tap, all on postings within five days of the pull. **That is a downgrade in evidence and an upgrade in knowledge**: they were unmeasured, now they are measured-and-absent, and their ceilings rise from 35 to 55–75. This is the distinction `tier_confidence` was built to carry, arriving one build later as a live case.

**Bondora is a row now, in a `REVIEW` bucket rather than given a tier.** Funding stage returned `Public`, ownership returned `private`, total funding blank — a contradiction between two columns, which is an unresolved **gate**, not a weak score. One web-research credit settles it. A tier number here would be a guess wearing a number's clothes.

**Current state: T1 8 · T2 11 · T3 40 · REVIEW 1 · UNSCORED 56.** Evidence tiers A 14 · B 46 · C 56. Confidence `FIRM` 36 · `PROVISIONAL` 9 · `CANNOT REACH TIER 1` 14 · `UNSCOREABLE` 56 · `REVIEW` 1. **Tier 1 has not moved through any of this** — the eight are the roster's eight, and the 17 unsupported `MRG◐` marks remain the one thing that could take it to roughly 4.

**Verification is at 11 checks and two have now earned their keep.** Check 8 (a posting-derived EST with no date window) found the recency-windowed file outside `data/`. Check 5 (score equals the sum of its marks) caught Bondora being scored before its marks were set — a build-order bug, not a data problem. Two new checks: every w1 correction landed on the row it names, and no corrected signal still reads `NOT RETRIEVED`.

---

## 2026-09-04 (later 4) — the master account file exists; seven islands become one

**`data/0926-master-accounts.csv`, 115 rows, built by `scripts/build-master-accounts.py`.** Schema and rules in `0926-master-accounts-schema.md`. The CSV is now the roster a sequence gets built from; `0926-target-accounts.md` stays the narrative record of why each mark is what it is. **The script is the only writer** — a correction goes into the source island and then into a rebuild, never into the CSV by hand.

**Reconciliation is exact.** roster 31 (29 + Alan and FreedomPay shared with cost-test) · cost-test 9 (7 new) · consolidation 19 · c1-fresh-pull 56 · Vinted and ShiftKey, which had never landed in a file = **115**. Domain is the only join key. Zero duplicate domains, zero same-company-different-domain collisions. **Workstream 1's 9-vs-7 reconciliation confirmed independently by the build.**

**Tier 1 is unchanged at 8** and is exactly the roster's eight, recomputed from the marks rather than copied. **Tier 2 goes 9 → 12**: three consolidation accounts (Docplanner, Entrata, OfferUp) reach it because the 44-domain pull gave them EST and HIR the roster never scored.

**Built first against the undated pull, which over-credited.** Using `Claude outputs/0926-est-hir-results-44-dated.csv` instead — the recency-windowed version, found on disk outside `data/` — moved Tier 2 from 15 to 12 and evidence-tier A from 19 to 14. Cabify falls out on `EST⊘` (newest pain posting 2022-02-10), Teachers Pay Teachers on `EST⊗` (4 requisitions), **Vinted on `EST○` — absent across 67 requisitions.** The window is doing exactly the work it was added for, and open gap 1 is closed: the dated file was in the repo all along, in the wrong folder.

**The column that matters most is `tier_confidence`, and it is new thinking, not a port.** Every row now carries `score_ceiling` — the maximum it can still reach given what has *actually been retrieved*. A score alone presents an **unmeasured** account as a **measured-and-weak** one. That is the UNKNOWN family at the level of the whole model rather than a single field, and it is the seventh instance. Distribution: `FIRM` 36 · `PROVISIONAL` 9 · `CANNOT REACH TIER 1` 7 · **`UNSCOREABLE` 63** — ceiling below the 37.5 Tier 2 line. Sixty-three of 115 accounts are not ranked low. They are not ranked.

**`evidence_tier` is separated from account tier, deliberately.** A 19 · B 33 · C 63. Evidence tier says what an email may *claim*; account tier says how much attention the account *earns*. Different questions, different columns. Collapsing them is how a category-line account gets a named-pain email.

**MRG's provenance is settled: firmographic, not posting-derived.** `Ownership Type` / `Latest Round`, per `mrg_retrieval` on every row. So the 35-point ceiling for a no-posting account does not collapse to 15 the way workstream 1 guessed. But it is still optimistic for two other reasons: **MDB is unmeasured across the entire fresh pull** (`MDB?`, 15 points not in hand), and **MRG 20 needs a real margin event, not a funding stage.** Measured on the 56 keeps: **10 carry a `PRIVATE_EQUITY_ROUND` fact; of the 50 with no live posting, 9 do.** So today's real ceiling for those 50 is **20 for nine of them and 0 for the other 41** — not 35, not 15.

**Eight verification checks run on every build** and all pass. One found a real gap, recorded rather than papered over: **the 949-row EST/HIR corpus was never committed** — only its per-domain aggregate. So 44 rows cannot show the dates behind their EST and HIR marks, **including the recency window that moved Tier 1 from 10 to 8.** That window is currently unverifiable from the repo. Only 8 rows have real date ranges, from the 58-row committed corpus. Requested from workstream 1.

**Open gaps recorded in the schema doc:** the 949-row corpus · the 17 unsupported `MRG◐` · the 10-domain probe results not yet rows (Turno among them) · `Latest Round` blank on 13 of 56 fresh-pull rows, the **fourth** unpopulated-column instance after `Ownership Type`, `Company Screen` and `Matching Posting Count` · Bondora pending as a 10th cost-test account.

**Disagreement with workstream 1 on one mark.** They asked for the probe's 4 zeros to be `EST⊗`. Per this repo's own legend `⊗` means *measured absent, single source, provisional* — searched one document, did not find it. An account with **nothing inside the window was never measured**: that is `EST?` if it has no postings at all, or `EST⊘` if postings exist but predate the window. All three score zero, so no tier moves — but the mark is the audit trail, and item 6 of the deltas file is the argument for getting it right.

---

## 2026-09-03 (later 8) — the retraction landed; both skills at v1.2

**Item 8 of the workstream-3 handover is a correction, and it was live in the skills.** Workstream 2 flagged three passages teaching the retracted sole-cause conclusion. There was a **fourth neither workstream flagged**: `origami-sourcing` Step B justified the whole one-gate shape with *"headcount, geography and capital uniquely reject nobody — every company they catch is already caught by type."* Same void reasoning, in the passage that sets the skill's shape.

**The conditioning law is now a named rule in both skills** — "the second rule" in `origami-sourcing`, a block above check 11 in `sourcing-csv-audit`, with the decision table from `lead-scoring` rule 6 and the Ola/Lazada/PhonePe pull as the worked example. Check 11 stays; it now reports a **validity verdict per filter**, and a zero on a filter the corpus was built under is labelled an artefact, not a finding.

**The shape was re-derived rather than reverted, and this is a judgment worth reviewing.** §7 of the handover said one gate plus a column list. §8 voids the basis for demoting geography and headcount specifically. Those two are in tension and neither handover reconciled them. The skill now carries **three blocks: the discriminating gate (company type, 110 sole-cause — that finding survives, since it discriminates inside an already-conditioned corpus), the enforced gates (geography, headcount band, status, founded floor — kept as hard gates, with an explicit note that near-zero discrimination is not permission to remove them), and the columns.** The ergonomic finding survives untouched: no stack of numbered filter steps. **Safe reading chosen deliberately** — the cost of wrongly keeping a gate is a narrower pull, the cost of wrongly dropping one is Ola.

**Everything else landed.** `origami-sourcing`: A0 pre-flight question (what decision, at what threshold — C1 needed 143 against a most-pessimistic 862), A1 enumerate-vs-sample purchasing table, A2 the repo grep, constraints 20-24 (absence from enumerating calls only · fresh draw on gate change · projections state their sample basis · price per row · one canonical text file), cost model repriced per row with the 3.2-vs-5.3 per-lead trap explained, `Infra/SRE Posting` moved out of the enrichment budget, four new failure entries (17 sole-cause trap, 18 gate re-scores old sample, 19 projections as counts, 20 absence from a sampling call), and the leaky-term entry now carries the 3-of-7 rate with all three variants.

**`sourcing-csv-audit`: checks 12-15** — company-set drift, type conformance, blanks clearing disqualifiers, is-the-text-in-the-repo. Plus the absence-asymmetry rule as the fourth member of the UNKNOWN family, and retrieval-path-per-value in Step 1.

**Still open, unchanged:** `lead-scoring`'s lane overlap, the 21-vs-23 skill count, `orchestration.md`'s stale ICP.md line, and no withdrawal banner inside the v3 prompt file.

---

## 2026-09-03 (later 7) — the skill's shape changed: one gate, everything else a column

**Both sourcing skills at v1.1, implementing `handoffs/0926-handover-to-workstream3.md`.** This was a shape change, not an addition to a constraint list.

**`origami-sourcing`.** The seven-step gate stack is gone, replaced by **one gate plus a column list** — filter on what the company does, read everything else. The sole-cause measurement over 296 companies is in the skill: company type 110, geography and headcount and capital **zero each**. **Rule 0 added at the top of the trigger section** — read the campaign doc first, campaign gates govern, name campaign-vs-ICP conflicts explicitly instead of inheriting whichever document the author happened to be reading. Constraint 4 strengthened past "band and stratify": no sorting inside a band either, require the returned sequence, verify non-monotonic, state sampled min/max against band bounds as a coverage percentage — and prefer dropping the cap, since headcount rejects nobody. Three new constraints: 17 ask the tool about itself but never accept its verdict, 18 never search an industry label, 19 reject the polluted universe. Four new failure entries: universe pollution, industry-taxonomy collapse, fit verdicts silently discarding qualified accounts, and the public-status two-check conflict. Two of the handover's six were already in the file (requisition double-counting, `Date Posted`) and were enriched rather than duplicated.

**Costs corrected, and this is the expensive lesson.** Pricing is now `rows × (retrieval + per-company enrichment)` with the observed spread in the skill: 1.2 credits/company for a thin tech-stack search, ~5.2/row trigger-first, **~24/qualified company** with full enrichment plus a fit verdict. **Prompt v3 is marked WITHDRAWN in the skill** — priced at 300 credits, ~1,560 at observed rates, and its shape is the gate stack the skill now rejects. Kept as provenance with the cost reason attached.

**`sourcing-csv-audit`.** Check 11, filter discriminative power, with the instruction to run it *first* when a filter set is on trial — it is the only check that retires a rule rather than flagging a row. Two hard rules added: a zero-sole-cause filter is decorative, and never accept a fit verdict because it removes rows already paid for.

**Still open from (later 5) and (later 6):** `lead-scoring`'s lane overlap, the 21-vs-23 skill count in both `CLAUDE.md` files, and `orchestration.md`'s stale "ICP.md is a draft skeleton" line. **New:** `0926-origami-300-posting-prompt-v3.md` has no withdrawal banner in the file itself — the skill marks it withdrawn, the file does not, and it reads as runnable.

---

## 2026-09-03 (later 11 · w1) — Rule 0: the campaign governs sourcing; Pantheon is anti-ICP, not suppression

**Settled with Rudra and written into the sourcing handoff as Rule 0.** When sourcing for a named campaign, use the **campaign's** numbers. `ICP.md` defines who is a good-fit customer; the campaign spec defines who enters the sequence. Cross-check for conflicts, resolve them explicitly, never silently pick one. Campaign gates live in the `WeKan Outbound Campaign Prioritization` project doc — **read it before writing a prompt for any campaign.**

**What this cost.** Ten Origami prompts were built at M2's qualification thresholds (200–2,500 employees, $100M+ raised) instead of C1's targeting thresholds (200–5,000, Series C+/$50M+) — every pull filtered at half the intended ceiling and half the funding floor. And all three tech-stack searches filtered `NOT MongoDB` while **C1 gates on Atlas / large cloud estate signals**, so they were excluding the campaign's own primary estate gate. The campaign doc was never opened by this workstream until now; "C1" was referenced throughout the handoff and taken to mean a single volume-email question.

**Conflict audit.** Only M1 and M2 have size tables in `ICP.md`. M1 and C3 agree. M2 and C1 disagree on both headcount and funding. P2, A1, P1, A2 have no size tables — no collision possible yet, none reconciled either.

**C1's volume question was already answered in the campaign doc.** C1 is priority 1, week 1, "lead volume campaign", calibrated over the **first 500 sends** with the rule *scale +50% if positive ≥2%, rework if <0.5%*. The threshold table in §2 of the sourcing handoff was re-deriving a decision the plan had already made. Useful arithmetic instead: 500 sends ÷ ~3.5 contacts per committee ≈ **143 accounts** to complete the first calibration window. The roster is 39 — about one week of C1 at its own 25–40 contacts/day. Sourcing is needed to feed calibration, not to decide whether to run it.

### ESCALATION to workstream 2 — Pantheon, and it changes the count

**Pantheon (`pantheon.io`) is not a suppression case. It is an anti-ICP disqualification.** Rudra confirms WeKan has never worked with them, so the client/relationship suppression check does not apply. But the reason it was held was never a relationship — it was recorded as *"check against the C1 competitor suppression list"* and *"running customer databases is their product"*. Those are two different mechanisms and the repo conflated them.

The correct read: Pantheon is a managed hosting/PaaS platform, which is an explicit **ICP-M2 anti-ICP exclusion** — *"companies whose own product is infrastructure (databases, hosting, PaaS, developer platforms, observability, data connectivity, GPU compute, workflow orchestration)"*, worth −40 in Model B. Its own row already carries `ACC✕` and *"anti-ICP: infrastructure vendor"* at 35 points, Tier 3. It is also not plausibly a WeKan competitor: WeKan sells database modernization consulting, Pantheon sells WordPress and Drupal hosting. They do not compete for the same work.

**So: drop it from the roster as anti-ICP, do not hold it pending a suppression check.** Per §10 this workstream does not edit roster files, so this is an escalation, not an edit.

**Count consequence — three places carry the tally.** The cohort table reads `A 5 · B 7 · C 2 · D 15 · E 2 · suppression 1 = 32`, and Pantheon is that `suppression 1`. Reclassified, the roster is **31 qualified + 1 disqualified**, and the 39-account enrichment set becomes 38. `0926-target-accounts.md`, `0926-m2-pursuit-order-snapshot.md` and the published exec brief all need the change. Minor side note: the tech-stack enrichment spent ~2.5 credits on pantheon.io.

**Still missing and it blocks sends, not sourcing:** the C1 suppression list itself does not exist in the repo. Four files instruct a check against it; no file is it. The categories are in the campaign doc — current clients, active opportunities, Labs and design partners (lending bank, Medora, CoE universities), active MongoDB co-sell accounts, competitors — but the account names are presumably in HubSpot.

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

## 2026-09-04 (later 3) — MRG audited: 59% of its points trace to nothing, and yesterday's diagnosis was wrong

**Run here, from committed data, at zero cost.** 28 accounts carry `MRG●` or `MRG◐`, worth 390 points. **8 accounts (160 pts) trace to a PE or sponsor fact in the CSV. 3 (60 pts) rest on the cohort assignment alone. 17 (170 pts) have no traceable evidence of any kind.** 230 of 390 points — **59%** — rest on something other than a recorded fact.

**I had the diagnosis wrong yesterday.** `(later 2)` reported MRG at 35% prevalence and concluded the conditioning law did not apply. **That counted `MRG●` only. Counting any MRG credit it is 28 of 31 — 90%.** Near-constant. **Workstream 1's conditioning hypothesis was right and this workstream measured the wrong denominator** — the same error as the inverted depth metric, two days running.

**The mechanism, and it is a new shape.** All 17 unsupported marks are `MRG◐` at 10 points, and every one is a Series C, D, E or G company. The mark was awarded for being late-stage VC-backed — **but "Series C+ or $100M+ or PE-owned" was a sourcing gate that every roster account passed by construction.** So `MRG◐` is the capital gate re-scored under another name: a filter applied upstream, paid for twice. **Sixth instance of the family, and the first that is not a blank scored as a value — it is a real fact, correctly recorded, counted in the wrong column.** Rule 6 only catches it if someone thinks to ask whether the signal was a gate, which argues for making that question mandatory rather than advisory.

**Size of the unresolved decision: zeroing the 17 would take Tier 1 from 8 to roughly 4.** Close, ID.me, ezCater and Cover Genius all fall to 55 and out; Owner.com, Signifyd, Housecall Pro and Wallapop each lose 10. **Second-largest tier movement of the trial.** Not applied, because unlike the earlier corrections there is no single right answer — a late-stage company under board efficiency pressure genuinely is an M2 target, and `ICP.md` names *"efficiency mandate after a funding round, layoff or profitability pivot"* as a trigger. What is missing is evidence that any specific account has it.

**So the fix is retrieval and it is workstream 1's:** for those 17, is there an actual margin event on record — an earnings commitment, an announced layoff, a stated profitability pivot? Until answered, `MRG◐` on the 17 reads as **`MRG?`**, and **Tier 1 at 8 is an upper bound.**

**The 8 sound ones:** Sensor Tower, Pushpay, Cambridge Mobile Telematics, Zuora, Civitatis, iCapital, FreedomPay, Zūm — all carrying `private_equity`, `PRIVATE_EQUITY_ROUND` or `POST_IPO_EQUITY` in source data. A take-private or sponsor round is a real margin event.

**Consequence for the Pursuit Order artifact: do not rebuild it yet.** Tier 1 could move 8 → 4 on this question alone, and the 28 pending accounts will restructure the roster again. A superseded banner pointing at this file is the right holding action.

---

## 2026-09-04 (later 2) — Zeta dropped; depth grading withdrawn; MRG is collinear, not idle

**Zeta's `EST●` was spurious and is dropped.** Its sole dated match: *"founded in 2015 by two visionary leaders … whose entrepreneurial legacy & excellence."* `legacy` as heritage. Zeta 50 → 25, Tier 2 → Tier 3. **Tiers: T1 8 · T2 9 · T3 14.** Workstream 1's three "thin" calls also verified — ShiftKey is an AWS region move, EIS Group generic Azure CloudOps, Wallapop mobile-app modularisation.

### The distinction the term list cannot make, and it touches two Tier 1 seats

**Evidence about the candidate is not evidence about the company.** *"Experience managing technical transitions such as monolith-to-microservices"* describes the hire. *"Our .NET Framework 4.8 monolith processing billions in giving"* describes the estate. The regex matches both identically.

**Two Tier 1 accounts rest on the first kind.** **Cambridge Mobile Telematics** (60) — *"Experience managing technical transitions such as monolith-to-microservices…"*, a hiring specification. **Cover Genius** (65) — its only dated sentence is *"assist application teams to optimize queries, migrations and perform other datastore performance tuning"*, a duties list. **This qualifies workstream 1's reassurance that Tier 1 came through the hand-read clean: six of eight did.** Neither is disqualifying — both hold real MRG and HIR evidence — but the first email to either cannot open on an estate claim the posting does not make.

### Depth grading withdrawn — their argument is better

This workstream proposed grading EST depth. **Dropped.** Their decisive reason: **a human already reads this evidence at the right moment.** C3 requires human-approved first touch, and Owner.com's named migration versus a keyword match matters in *what the email says*, not in a score. Grading it converts a solved workflow problem into an unsolvable scoring one. Plus: a gate is a threshold test and must stay binary, and a hand-assigned depth grade is a **derived judgment** — the class this trial spent two days learning never to encode.

**Adopted: the quoted, dated sentence is a mandatory field on every `EST●`.** One addition from here — **the field is also the detection mechanism for the error they just found by hand.** Zeta's heritage match and CMT's hiring-spec match are invisible behind a `●` and obvious the moment the sentence sits beside it. Mandatory from the start, both would have been caught on sight rather than three days later. Cheapest guard on the roster: one column, and every false positive self-announces.

### MRG is collinear, not idle — and the sole-cause test has a stated blind spot

**Their conditioning hypothesis does not hold.** PE-ownership is both a capital gate and the sponsor trigger, so partial overlap exists, but MRG sits at **35% prevalence** — nowhere near the near-constant signature that killed VOL (zero variance), SCL (28 of 32 identical) or AGE (spread entirely missing data).

**What the 2 changes mean: renormalising thresholds measures whether a signal changes the *ordering*.** MRG barely does — **72% overlap with HIR, 45% with EST**. But with thresholds fixed, deleting MRG moves **12 accounts including all 8 in Tier 1.** It is carrying points every top account depends on.

**So the sole-cause test answers "does this change the ranking", never "is this doing work."** A collinear signal scores low while being load-bearing. Proposed as a stated limit on `lead-scoring` rule 6 — the same shape as the rule itself, one level in.

**The real MRG question is provenance.** Twenty-eight accounts carry `MRG●` or `MRG◐` and the recorded evidence for most is *"margin/sponsor trigger confirmed."* Same unrecorded provenance flagged against Sensor Tower on 3 September and never resolved. **Audit what those 28 marks rest on before touching the weight** — a 20-point signal whose evidence has never been checked is exactly where this trial says the next defect lives.

---

## 2026-09-04 (later) — the recency rule: Tier 1 settles at 8, and a Tier 1 seat turned on one term

**Workstream 1's recency finding is the most transferable rule of the trial, and it is right.** A 2022 advert saying *"we are modernizing our monolith"* is as likely to mean they finished as that they are still in it — the same inversion as Owner.com migrating *off* MongoDB. Stale evidence does not merely fail to help; it can point the wrong way.

**The rule: a recency window must match the half-life of the claim the signal makes.** `HIR` claims hiring now → 90 days. `EST` claims current architecture → 12 months. `MDB` claims current stack → 12 months. `AGE` is a historical fact → no window. **Different signals take different windows from the same pull.** One window inherited across a whole model is how a four-year-old job ad qualified an account.

**12 months justified against both boundaries:** at 24 months the only addition is Blockchain.com, whose newest estate posting is August 2024 with zero inside the year against 43 requisitions — exactly the case the window exists to catch. At 90 days it drops Zeta, ShiftKey and ESW, all recent enough that the architecture cannot have changed.

**Applied: EST● falls 22 → 15 across the 44 domains. Tier 1 falls 10 → 8.** New mark **`EST⊘` stale** — pain language exists but predates the window; scores zero like `○` and `⊗`, and records why. Four roster accounts hold it: **Zuora** (newest 2022-05-24) · **Back Market** (2022-02-21) · **Netradyne** (2024-03-27) · **Blockchain.com** (2024-08-24).

**Tier 1 (8):** Sensor Tower 75 · Pushpay 75 · Close 65 · ID.me 65 · ezCater 65 · Cover Genius 65 · Metropolis 60 · Cambridge Mobile Telematics 60. **T2 10 · T3 13.**

### The one-account disagreement, and why it resolved without appeal to taste

They measured 16, this workstream 15. **The whole difference is the `cost optimisation` term, and it decided Zuora's Tier 1 seat.** With it in, Zuora has 6 recent qualifying postings on lines like *"drive initiatives for cost optimization, performance tuning, and system hardening."* Without it, zero inside the window and nothing genuine since May 2022.

**It stays out, and the deciding argument is structural rather than editorial: Zuora already holds `MRG●` at 20 points for exactly that evidence.** `ICP.md` separates them — the estate marker is a founding-era monolith throttling releases; the margin trigger is *"infra spend growing faster than revenue, cloud bill a standing board topic."* Cloud FinOps is the margin signal. Scoring it in EST too pays 45 points for one observation, which is the double-count the four-signal rebuild exists to prevent. Zinnia and Entrata are the same case.

**Eight is also where workstream 1's own threshold sat** — they flagged that above ~8 the gate would have stopped gating and the 25-point weight should get another look. It landed at 8 without anyone tuning toward it, which is the most reassuring thing about the number.

### Their fourth error of one shape, and the check that catches all four

Workstream 1 catalogued it themselves: sole-cause on a corpus already conditioned on the filters under test · sole-cause used as a marginal statistic for a joint decision · estate pain read from boilerplate (`reliability` in 67% of postings) · estate pain read from four-year-old postings. **All four are computing on everything returned rather than on what is valid.**

**The audit check: before computing any signal, state the retrieval path and the date range of the rows it rests on.** The retrieval-path half was already in `sourcing-csv-audit`; the date half is new. This workstream's own inverted depth metric — grading Vinted "thin" at 3% on a frequency rate — is a fifth instance of the same family, so the check earns its place from both sides. (The "corpus's single best estate sentence" this line used to claim for Vinted was a paraphrase in no data file; corrected 2026-09-04.)

---

## 2026-09-04 — the EST pull lands: Tier 1 goes from 2 to 10, and a metric built here inverted its own ranking

**949 postings across 44 domains, 689 distinct requisitions, every domain returned including 9 empty.** Every audit claim reproduced independently: date field **fixed for the first time in the trial** (545 distinct dates, 2019–2026) · duplication **27.4%** · role filter **2.7% leaky**, down from 43% · MongoDB named in posting text on 6 domains as a free second source.

**Two corrections that changed the scoring.**

**1 · The pull returned four years of history, not live openings — only 111 of 949 postings are inside 90 days.** ICP-M2 defines the trigger as *live* hiring. **19 domains hiring now · 16 with history only · 9 with none.** Scoring HIR on any retrieved posting would have credited 16 accounts with 15 unearned points. Workstream 1 caught this and it is right. EST is unaffected — architecture described in 2024 still describes the estate.

**2 · "Named estate pain" pinned to an exact nine-term list.** Three measurements disagreed by up to 12×, entirely on wording. Reconciled by measuring every candidate term's prevalence across all 949 postings: **`reliability` appears in 67%, `observability` 38%, `on-call` 31%, `incident` 23%** — a term in two-thirds of a corpus cannot discriminate. Also removed **`cost optimisation`**, which is the *margin* signal: leaving it in had EST double-counting MRG. **Workstream 1's structural argument decided the design and was right — requiring a named database inside EST collapses EST into MDB.** Final list: `migrat* · monolith* · legacy · technical debt · re-architect* · replatform* · moderni[sz]* · decompos* · shard*`. **EST● on 23 of 44.** Aligned, the three measurements land at 22, 23 and 25.

**Tier 1 goes from 2 accounts to 10** — Sensor Tower 75 · Zuora 75 · Pushpay 75 · Close 65 · ID.me 65 · ezCater 65 · Cover Genius 65 · Netradyne 65 · Metropolis 60 · Cambridge Mobile Telematics 60. T2 10 · T3 11. **The gate was never gating on estate pain; it was gating on which nine accounts had been measured.** Ten is also right-sized for C3's own cadence of 10–15 named accounts a week.

**Sole-cause re-run answers the weight question: EST survives.** 25 points, 58% prevalence, **9 sole-cause tier changes — still the strongest discriminator.** The weak signal is now **MRG: 20 points for 2 tier changes**, and it is the next candidate for what VOL, SCL and AGE got.

### The finding worth keeping: frequency is not evidence, and the rule caught its author again

A depth metric built here graded EST by *what share of a company's postings mention estate work.* It ranked **Vinted "thin" at 3%** and another company **"substantive" at 90%** on *"our platform saw only 6 minutes of downtime."* **Rate measures how infrastructure-flavoured a hiring corpus is, not how strong the evidence is.** Third time in two days the repo's own rule — the verbatim sentence, never the extracted count — has caught the person applying it.

**Corrected 2026-09-04: the Vitess/sharding quote this entry carried was a paraphrase presented as a quotation and is in no data file.** Vinted is `EST○`, absent across 67 requisitions. Full correction in the roster and in ADDENDUM 2 item 4.

**Consequence: EST needs depth grading and does not have it.** Owner.com's `EST●` is a named MongoDB-to-Postgres migration in a senior req; several new Tier 1 entrants hold one keyword in a long corpus. Both score 25. MDB already grades positives by source; EST should too, on the specificity of the strongest sentence. Proposed, not applied — it is a human pass over 23 sentences, not a regex.

### Billing — flagged, unresolved

Workstream 1 priced this pull at **~30–60 credits** and it retrieved **949 postings**. At 1 credit per posting that is potentially **~949 credits against an authorisation given for ~150**. They disclosed it unprompted. **Confirm the actual charge on the dashboard before the next pull.** This is the second outstanding billing question and it is why the exec brief now carries a recommendation to keep a running credit total — per-pull costs are recorded, no cumulative figure is.

---

## 2026-09-03 (later 18) — gate declared after the pull; the asymmetry rule, sharpened

**Workstream 1's sequencing amendment accepted, and it is the better call.** `EST●` is held by 6 accounts against 22 unmeasured and 9 single-source absences — **so the gate does not currently gate on estate pain, it gates on having been measured favourably once.** Declaring it today would write measurement luck into the model as policy. The 44-domain pull settles it: estate pain at 15 of 44 and the gate becomes a real qualifier; two more and it is a confirmed sampling artifact and the weight question reopens on evidence. **Same decision, one step later, against a measured population instead of a six-account accident.**

### The general rule, with one sharpening

Theirs: **evidence of presence and evidence of absence do not cost the same.** One estate-pain sentence establishes `EST●`; no amount of one posting establishes `EST○`. Positives cheap and sound, negatives expensive and weak — and a model scoring them symmetrically under-scores systematically.

**Sharpening: "single-source" is a proxy. The operative property is whether the source *enumerates* or *samples*.** An enumerating source supports an absence; a sampling source does not.

**MDB is the counter-example that proves it, and shows the system already got this right once.** `MDB○` rests on a detector that returned a populated list of primary databases with MongoDB absent from it — enumeration, so the absence is sound. The five `MDB?` are where the detector returned nothing, already marked unknown. **MDB's absence handling is correct. EST's is not, because a job advert samples an estate rather than enumerating one.**

And the mirror is neat: for MDB the **positive** already carries its provenance (`MDB●` product-stack versus `MDB◑` slug, half credit); for EST the **absence** now needs to. **A mark should carry the quality of the source that produced it** — either side of the ledger.

**Fourth member of the family:** blank is UNKNOWN not FAIL · a derived judgment column is never evidence · a date equal to the pull timestamp is UNKNOWN not data · **an absence from a sampling source is provisional, not absent.**

### Sequence agreed

1. **Run the EST pull** — `handoffs/0926-est-pull-prompt.md` against the 44. Nothing blocks it and it is what every remaining decision needs.
2. **Then declare `EST● required for Tier 1`**, or reopen the weight if the pull shows the gate was an artifact.
3. **Then `Enrich Tech Stack` on the 21** for MDB.

Workstream 1 will log the asymmetry rule and the decision-threshold habit once the pull returns, so both go into `sourcing-csv-audit` with real numbers attached rather than as another pair of principles. **Their instinct to wait for the numbers is the same instinct as the amendment above, applied to their own work.**

---

## 2026-09-03 (later 17) — EST is a hidden Tier 1 gate; pool question closed

**Workstream 1 cautioned that 25 points is heavy for a signal read from one job posting. The arithmetic is worse: `EST●` is a necessary condition for Tier 1.**

Max reachable without EST is **MRG 20 + HIR 15 + MDB 15 = 50** against a Tier 1 cut of **56.25**. An account perfect on every other signal — margin trigger confirmed, live infra hiring, MongoDB present and direction-checked — **cannot leave Tier 2.** Both current Tier 1 members carry `EST●` because it is the only way in. **EST would have to drop to 15 points to break the gate**, demoting below HIR and MDB the signal `ICP.md` calls the core qualifier. **Breaking it is worse than owning it.**

**Recommendation: declare the gate, fix the depth, leave the weight.**

- **Declare it** — "Tier 1 requires `EST●`" as a stated rule rather than an emergent property of the arithmetic, which is a trap for the next reader of the tier table.
- **New mark `EST⊗`** — measured absent, **single source, provisional** — distinct from `EST○`, measured absent across every posting a company has. Both score 0; `⊗` records that the measurement is one document deep. A company can carry a twenty-year estate and never mention it in one SRE req, and today that produces the same zero as a thorough search.
- **Nine accounts currently hold a single-source absence** — FreedomPay, Lighthouse, and the seven cost-test accounts measured today — **all structurally capped at 50 of 75 on one requisition each.**

**The pull is safe to run now and should not wait on this.** Workstream 1's prompt already returns one row per posting and demands a row for every domain including empty ones, so multi-source EST becomes measurable for the first time. Run it, then decide the weight against real data rather than ahead of it. Prompt committed at `handoffs/0926-est-pull-prompt.md` (`b5eb2b5`) with the leaky-term exclusions and the infra-versus-non-infra term counts this workstream's measurement argued for.

### Open item 1 closed — stop measuring the pool

Origami's answer: **all three figures (2,723 → 1,506 → 862) are projections off the same stale 30-row sample**, each recomputed from a draw whose 16 non-US/EU rows can never pass the gates, with its own caveat that neither should be treated as a TAM for campaign sizing. **The decision does not need the number.** C1's first calibration window needs **143**. The most pessimistic projection is **862** — wrong by four times over and still sufficient. The fresh gated draw is nice-to-know, not a blocker.

**This question consumed most of 3 September and the answer was available from the ratio the whole time.** Worth remembering the next time a number is chased: ask first what decision it changes, and at what threshold it would change it.

---

## 2026-09-03 (later 16) — the 7 measured free; leaky role term confirmed at 3 of 7; roster HIR clean

**Workstream 1's fix beats the one proposed here.** They merged the cost-test posting text into `data/0926-origami-job-postings.csv` as `Pull = P9 cost-test` (36 → 58 rows, commit `37b10cf`) rather than committing a second text-bearing file. **Committing a second file preserves the evidence but breaks the premise that made the one-grep check work** — *the postings CSV is the only file holding posting text* — so the next person greps the canonical file, finds nothing, and buys a pull they did not need. Third time today that premise error would have fired. Their call, and it was right.

**Both signals then measured for the seven at zero cost.**

- **EST: measured absence on all seven.** No estate-pain sentence anywhere, one database named across seven postings. **Measured zeros, not blanks** — which is the distinction the entire audit turned on, and it now holds for 16 of 38 candidate accounts instead of 9 of 31.
- **HIR: 4 of 7, not 7 of 7.** Capital on Tap, Origami Risk, Mollie and OEC are genuine infra roles on the description text. **Facile.it, Meilleurtaux and Chrono24 are leaky matches** — DevEx and AI-platform roles carrying `react`, `typescript`, `llm`, `genai`; Chrono24's description contains **zero** infrastructure terms.

**Second confirmed instance of the leaky "Platform Engineering" term**, after Lighthouse's Ember/React/TypeScript req — and now with a rate on a fresh pull: **3 of 7**. The new false positive is AI-platform roles rather than front-end ones. Same term, new costume.

**A first pass here judged 2 of 7 from titles alone and was wrong** — the description scan corrected it to 4. The repo's own rule, *never accept a role match on the title alone*, catching its author. Cost: one pass over text already held.

**Roster HIR survives the same check: 0 of 6 marks fail.** Sensor Tower, Close, Owner.com, Signifyd, Alan and FreedomPay all read 4–9 infra terms against 0–3 non-infra; NexHealth is ambiguous at 2/0 but not leaky. **The leaky term hits the newer pulls, not the P1 infra-hiring pull the roster was built from.** Roster HIR evidence stands.

**Call 1 is now EST-only** — HIR arrives free at search time, since the gated pull populates `Infra/SRE Posting` on every row. A 15-point signal now attaches to every new account at no marginal cost.

**`handoffs/0926-est-hir-pull-domains.md` corrected to exactly 44** — the conditional 7-account block is struck.

---

## 2026-09-03 (later 15) — two calls not four; domain list built; Metropolis mark dropped

**Workstream 1's packaging beats the four line items in `(later 14)`, and the reasoning is right.** One **Job Posting Search** buys **EST (25) and HIR (15) together — 40 of the 75 points** — because the posting text is EST's only source, and a domain returning no matching posting is a **measured absence** rather than a blank. That distinction is the whole point of the audit: after this pull, no account is scored 0 on EST as though we looked when we did not, whichever way the numbers move. `Enrich Tech Stack` stays separate for MDB, because posting rows carry database mentions on only 10 of 36 (~28%) — not good enough for a 15-point gate.

| Call | Buys | Domains | Cost |
|---|---|---|---|
| 1 · Job Posting Search | EST + HIR | **44** | ~30–60 |
| 2 · Enrich Tech Stack | MDB | 21 | ~53 |
| | | | **~85–115**, inside the authorised 150, covering 44 accounts instead of 19 |

**Domain list assembled and committed: `handoffs/0926-est-hir-pull-domains.md`.** Independently arrives at **44** — 23 roster accounts with no committed posting text, the 19 consolidation accounts, plus Vinted and ShiftKey. Ready to paste; workstream 1 does not need to assemble it.

**Correction found here: the 7 cost-test accounts are not covered either.** Workstream 1's table credits them with EST and HIR because they came from a job-posting pull. **HIR is genuinely known — a posting existed. EST needs the text, and `srepostingscosttestrawdata20260903.csv` was never committed.** Verified: none of Origami Risk, Facile.it, Chrono24, Mollie, OEC, Meilleurtaux or Capital on Tap appears in `data/0926-origami-job-postings.csv`, the only file holding posting text. **So the pull is 51 domains, or 44 if that CSV is committed first — and committing it is strictly better: zero cost, 7 fewer domains, and the evidence preserved as every other pull has been.** The seven are listed separately in the domain file as a conditional block.

This is the **"the text is in the repo" premise error running in the opposite direction** — the same one that cost a round-trip this morning. Both times the check was one grep. Worth making that grep a step in `sourcing-csv-audit` rather than a thing someone remembers to do.

**Metropolis Technologies: `EST◐` dropped, applied.** 12.5 points on a mark with zero posting rows and a blank database column. Score **32.5 → 20**, still Tier 3, gate now `EST?`, and it is in the 44. Workstream 1 was right that an untraceable positive is worse than a marked unknown — a blank at least announces itself.

---

## 2026-09-03 (later 14) — EST is unmeasured on 22 of 31. Fourth blank-as-value instance, and the heaviest one.

**Workstream 1 asked the right question: are EST's zeros a measured absence or an unmeasured blank? Measured: unmeasured, on 22 of 31 accounts.**

EST is the heaviest signal in the v2 model just applied — **25 of 75 points, 33% of the model** — and it rests on evidence for **9 accounts (29%)**. Six positive and traceable to a requisition in the postings CSV (Sensor Tower, Close, Owner.com, Signifyd, Alan, NexHealth) · two measured absences where the text was read and no estate pain found (FreedomPay, Lighthouse) · **one positive mark with no traceable source at all — Metropolis Technologies `EST◐`, 12.5 points, zero posting rows and a blank database column** · and **22 never searched.**

**The error is asymmetric, which is what makes it serious.** The 22 are scored as though we know they have no estate pain. We never looked. **Computed exposure: 3 of them would reach Tier 1 on a single unmade measurement** — Zuora, Carta and Pushpay, all 35 → 60 — **and 10 more would reach Tier 2. Tier 1 currently holds 2 accounts.**

**Verdict: v2 ranks soundly over the 9 measured accounts and does not rank the other 22 at all.** It does not merely score them low; it fails to score them. **v1 carried the identical gap** — EST was 25 of 100 there against 25 of 75 here — so v2 dilutes it less rather than creating it. **No revert. A measurement.** The model change raises the priority of the fix instead of causing the problem.

**Fourth instance today of a blank masquerading as a value**, after AGE credit on blank founding years, VOL credit from a fabricating classifier, and a blank `Ownership Type` clearing a −40 disqualifier. Four in one day across two workstreams is no longer a run of bad luck; it is the failure mode this system produces by default, and rule 4 only catches it where someone has already thought to mark the field.

**Credit priority inverts.** Workstream 1's corrected counts: 21 need MDB (the 19 plus Vinted and ShiftKey — their own miss, disclosed), 19 need HIR. **Nobody had counted the 22 roster accounts needing EST.** Revised order by decision value per credit: **HIR for the 19 at ~10 credits** (best density on the list, a 15-point signal for ten credits) → **EST for the 22 roster accounts at ~45–115** (the only spend that can change Tier 1) → MDB for the 21 at ~53 → EST for the 19 last, since those are unevidenced on every signal and EST alone will not tier them. Table in `0926-target-accounts.md`.

---

## 2026-09-03 (later 13) — Model B v2 applied; suppression is not a blocker; C1 has none left

**All three approved by Rudra.** Four-signal model, rule 6 ratified, ~150 credits authorised. He also settled the meta-question: **relaying workstream 1's message counts as approval**, so future relays do not need a second round-trip.

### Model B v2 is live

**EST 25 · MRG 20 · HIR 15 · MDB 15. Max 75. T1 ≥56.25 · T2 ≥37.5.** AGE, SCL and VOL are gates only and no longer score. Backup at `_backups/0926-target-accounts.md.pre-4signal`.

**Five tier changes.** Close T2→**T1** · NexHealth T3→T2 · Zuora, Carta, Metropolis T2→T3. **T1 2 · T2 4 · T3 25.**

**Close reaching Tier 1 closes the oldest open disagreement in the file.** On 2 September the model scored it 80 against a hand rank of 29, and the note read *"one of the two is wrong, and the model is at least legible."* **The model was right.** Close was hand-ranked down on unverified scale — and scale is one of the three signals now proven not to discriminate. `SCL○` costs it nothing under v2; what remains is MongoDB confirmed on product-stack detection and direction-checked, named estate pain in an open req, and live infra hiring from a P1 posting with a real date.

**Coupling condition recorded in the file:** 55 of the 75 points now rest on workstream-1-sourced data. Sharper and more coupled at once — a thin pull now yields empty scores rather than mediocre ones.

### Suppression: my error, and the blocker dissolves

`(later 12)` called a HubSpot export C1's critical path. **Wrong on both counts.** Workstream 1's handover said the names were *"presumably in HubSpot"* and the hedge was dropped in transit; **WeKan does not use HubSpot.** Lesson worth keeping: a relayed inference loses its hedge unless the hedge is carried explicitly.

**Checked instead of assumed.** `messaging.md` §6 Pool A is effectively the suppression list. Cross-referenced against all 40 candidate accounts: **zero matches, and the overlap is structurally impossible.** Pool A is Fortune 500 enterprises across cruise, automotive, aviation, retail, dialysis, insurance, airline, banking, healthcare and power tools — an **ICP-M1** population. The roster is **ICP-M2**, growth-stage digital platforms at 200–5,000 employees. The two ICPs cannot overlap by construction, so the check returns nothing now and will keep returning nothing as the roster grows.

**So C1 has no remaining blocker** — not the model, not the credits, not suppression — and it is addressable at 23 accounts today (Cohorts A 5 + B 7 + E 2, plus Vinted, ShiftKey and the 7 cost-test accounts; the 15 Cohort D accounts stay out, all carrying `HIR○ MRG◐ EST○`).

**Residual hygiene:** four repo files still instruct a check against a suppression file that does not exist. Point them at Pool A plus the campaign-doc categories, or write a thin file that does. One pass, no external dependency — worth doing before an autonomous send, because an instruction pointing at nothing reads as an unperformed check.

---

## 2026-09-03 (later 12) — C1 was never blocked by the model *(superseded in part — see later 13)*

Workstream 1 recommends approving the four-signal model, ratifying rule 6 and authorising ~150 credits, **and made the point nobody had made: none of it blocks C1.** Those three are Rudra's calls and are with him; the C1 analysis is recorded here because it stands independently.

**Their argument, and it is right.** The four-signal model produces T1 2 · T2 4 · T3 25 — it is not ranking the roster, it is picking about six accounts. That is the correct instrument for **C3** (trigger-gated ABM, 10–15 named accounts a week, human-approved first touches) and the wrong one for **C1**, which is a volume campaign at 25–40 contacts a day with autonomous sends calibrated over 500 sends. **A volume sequence sends to a cohort, not to a tier.**

**Their number is wrong, and the error matters.** They count 40 gate-qualified accounts and call it a week of sending. Gate-qualified is not in-market, and C1's own gates read *"SRE hiring OR efficiency signals."* Cohorts on the current 31: **A 5 · B 7 · E 2 = 14 C1-eligible · C 2 and D 15 not eligible.** **All 15 Cohort D accounts carry `HIR○ MRG◐ EST○` — not one has a live trigger.** With the 2 C1-cleared and 7 cost-test accounts (both from infra-posting pulls, so both carry the trigger by construction), **C1-addressable today is 23, not 40** — one to two days of sending, not a week. **Emailing the 40 would put 15 no-trigger accounts into an autonomous send**, breaking the activation rule and repeating today's recurring error in a third costume: absent evidence read as a green light.

**What actually blocks C1: the suppression list still does not exist.** Four files instruct a check against it, no file is it, the names live in HubSpot, and C1's own guardrail requires suppression before any send. So the critical path to C1 is a HubSpot export that has sat untouched for three days. Their sting — *"two days sourcing for a campaign that had enough accounts to start on day one"* — is fair in direction, and sharper stated precisely: **C1 could not have started on day one either, for the same missing reason, and nothing in the model decision changes that.**

**And the number that would settle volume-versus-ABM is a reply rate nobody has measured.** Every figure in `0926-target-accounts.md` is a population estimate. None says whether the message works. The first 500 sends produce that and no amount of scoring will.

**Coupling condition recorded** against the four-signal proposal: the surviving four put **55 of 75 points on workstream-1-sourced data**. The model gets sharper and more coupled at once — firmographic padding used to absorb a thin pull and no longer will, so a weak run now produces empty scores rather than mediocre ones.

---

## 2026-09-03 (later 11) — variance is not importance; and the 28 are blocked on evidence, not on churn

Workstream 1's reply, `handoffs/0926-w1-reply-to-w2.md` (commit `4753069`). Three corrections inward, all accepted.

### The caution, and it is the important one — now `lead-scoring` rule 6

The sole-cause table in `(later 10)` invites a mistake workstream 1 made two hours earlier **at the cost of a pull**. They read near-zero variance as near-zero importance and recommended demoting geography and headcount from gates to columns, on evidence that both uniquely rejected **zero of 296** companies. That corpus had been sourced *under* those filters. The next pull removed them and returned **Ola at 29,658 employees, Lazada 21,590, PhonePe 19,151, Daraz 13,487, Trendyol 11,479, Alipay, Flipkart** — **9 of 14 companies clearing the transaction-volume gate failed geography or headcount.** The filters looked powerless precisely because they were working.

**The law, stated properly: a filter applied upstream cannot discriminate downstream. Conditioning on a variable destroys its variance.** So near-zero variance means *already enforced*, not *unimportant*. A discrimination test answers "what should carry weight in the score" and can never answer "what can be relaxed in the gates", because it runs on a population the gates produced.

**Written into `.claude/skills/lead-scoring/SKILL.md` as rule 6** (now v1.3, backup at `_backups/lead-scoring-SKILL.md.pre-rule6`), with the decision table — *was this signal a gate upstream? yes → drop from scoring, never from gating; no → consider dropping, after checking the population is representative* — and both worked examples. **Also written as a blockquote directly above the sole-cause table in `0926-target-accounts.md`**, because that table is where a future reader meets the trap. Skill edits normally escalate; this one tightens a guardrail and corrects a hazard introduced by today's own analysis, so it is applied and flagged for ratification rather than held.

The four-signal proposal is safe **only because it keeps AGE, SCL and VOL as gates while dropping them from scoring.** Two different operations.

### The 28 are blocked on evidence coverage, not on re-tiering churn

Workstream 1's reason is better than the one recorded in `(later 10)`. **Three of the four surviving signals are sourced by their workstream**, and the 19 consolidation accounts have none of them: EST (25) needs job-posting text — none retrieved, sourced by Company Search; HIR (15) needs postings — Origami left `Infra/SRE Posting` blank on all 30 rows and declined to guess; MDB (15) needs `Enrich Tech Stack` — never run. MRG (20) is partial.

**The 19 are blank on 55 of the proposed 75 points.** Gate them today and every one lands in Tier 3 on absent evidence — rule 4's failure mode arriving from the opposite direction.

**Agreed sequencing:** settle the four-signal model → authorise **~150 credits** (~48 for `Enrich Tech Stack` across the 19, the rest a posting pull against those domains) → then gate. Workstream 1 holds the spend until the model decision, because it only makes sense once the four signals are locked.

### `OWN?` is cheap to close — a coverage failure, not a capability gap

Workstream 1 accepts the provenance diagnosis (blank on 27 of 31, came from nothing rather than from a column) as superseding theirs and is amending their handover item 6. **Confirming evidence: their pull the same evening returned `PUBLIC_COMPANY` correctly and unprompted on 14 of 30 rows** — Shopify, Booking Holdings, Jumia, Sea, Lightspeed, BILL, PAR Technology, NCR Voyix, WEX, Thryv, GoTo, Intellect, Aurionpro, Nucleus. So the field populates when the pull asks for it. **`OWN?` closes with a re-pull, not with 27 hand verifications.**

### The campaign-motion question moved, and open item 1 is rewritten

Their transaction-volume-first pull is **the first sourcing configuration that worked.** Origami projects ~2,723 qualified in a ~3,000 pool at 3.2 credits each; 5 of 14 cleared geography and headcount, implying roughly **900–1,000 in-band qualified accounts. Order of magnitude only — n=14, and the 2,723 is a projection, not a count.** Even heavily discounted it reframes the question: against the 143 the first 500-send calibration window needs, **the population was never the constraint — the filter order was.** Which is what `ICP.md` already said — *Intent is 30 of 100; firmographic-first sourcing scores zero on it by construction* — and what took three days to demonstrate. A volume motion is viable on these numbers; ABM-only leaves the pool untouched. Open item 1 rewritten, still open pending a real count.

---

## 2026-09-03 (later 10) — sole-cause test run: three of Model B's seven signals are noise

Workstream 1's consolidated handover (`handoffs/0926-handover-to-workstream2.md`) landed with three asks. Two are done; the third is deliberately held.

### 1. Sole-cause test on Model B — their hypothesis was half right, and then more right than their own test showed

They measured sole-cause rejections across 296 companies: **headcount, geography and capital uniquely rejected nobody**, company type did all the discriminating. Their question was whether SCL (5 pts) and AGE (10 pts) are the same inside Model B.

**Method note.** Deleting a signal lowers every score, so with fixed thresholds a heavy signal looks important merely by being heavy. The test deletes each signal *and* renormalises the tier cuts to the same proportion of the new achievable max. Both versions are in `0926-target-accounts.md`; the renormalised one is the answer.

| Signal | Wt | Modal value | Sole-cause tier changes |
|---|---|---|---|
| EST | 25 | 0 on 24/32 | **14** |
| MRG | 20 | 10 on 18/32 | **7** |
| HIR | 15 | 0 on 24/32 | **7** |
| MDB | 15 | 0 on 20/32 | **6** |
| AGE | 10 | 10 on 20/32 | 3 |
| SCL | 5 | **5 on 28/32** | **1** |
| VOL | 10 | **0 on 32/32** | **0** |

- **VOL — provably noise.** Zero variance. Confirms from the model side what the evidence side found this morning.
- **SCL — very nearly noise.** 28 of 32 score the identical 5 points. One sole-cause tier change on the whole roster.
- **AGE — looks like it discriminates, and does not.** 12 accounts sit off the mode, and **all 12 are `AGE?`, blank `Founded Year`. Not one is genuinely 2019-or-later**, because that is an anti-ICP exclusion filtered out at sourcing. AGE's entire spread is data coverage, not age. Verify the 12 blanks and it becomes a constant 10.

**The generalisation is the keeper: every dead signal was also a sourcing gate.** VOL was the volume qualifier, SCL the 200–2,500 / $100M+ gate, AGE the founded-≤2018 gate. The population was already filtered on all three, so it is near-constant on all three by construction — **Model B is re-scoring decisions made upstream and paying 25 of 100 points for it.** The four that discriminate — EST, MRG, HIR, MDB — are exactly the four that were never gates: trigger and technographic evidence found *after* the population was fixed. Same shape as workstream 1's finding one level up.

**Proposed and not applied — needs Rudra.** Reduce Model B to those four (EST 25 · MRG 20 · HIR 15 · MDB 15, max 75, cuts 56.25 / 37.5); AGE, SCL and VOL stay gates, which is what they already are. Moves five accounts: **Close → Tier 1**, settling the model-versus-hand-ranking disagreement in the model's favour; NexHealth → Tier 2; Zuora, Carta, Metropolis → Tier 3. Tiers become T1 2 · T2 4 · T3 25.

### 2. Private-status provenance audit — the defect is the opposite shape to the one predicted

**`Ownership Type` is blank for 27 of 31 roster accounts.** Their private status did not come from an Origami column; it came from nothing. The −40 "publicly listed or SPAC-bound" exclusion was never evaluated against a populated field for 87% of the roster. **This is the anti-ICP mirror of the blank-credit bug** — there a blank earned scoring credit, here a blank earns a clean bill of health on a disqualifier.

Graded: 3 accounts have a populated ownership field · 26 rest on an indirect private-market `Funding Stage` (inference, not verification) · **2 carried real risk and both are now verified private.** **Engine** — the only account with Ownership Type, Funding Stage *and* Total Funding all blank — is private, Series C, Permira lead. **Pushpay** — the one positive `POST_IPO_EQUITY` marker — was NZX-listed 2014, ASX `PPH` from 12 Oct 2016, **delisted from both May 2023** on the Sixth Street / BGH Capital take-private. Its conclusion on the roster was right; the check that produced it was not, and that take-private is its `MRG●` trigger.

**Net: no roster account is currently public.** Conclusions hold, enforcement does not. Recommended: stop treating a blank `Ownership Type` as a pass — mark it `OWN?` the way `AGE?` and `VOL?` are marked, which is rule 4 applied to the anti-ICP side where it currently does not reach.

### 3. Gating the 28 pending accounts — held, deliberately

19 consolidation + 7 cost-test + 2 C1-cleared. **Held pending the model decision above.** Tiering 28 new accounts on a model carrying 25 points of known noise means re-tiering all 59 afterwards. Workstream 1 said the sole-cause test was worth running *before* rules 4 and 5 were finalised; the same logic applies harder here.

### Roster arithmetic corrected in two of three files

**Pantheon reclassified from "suppression check first" to a straight anti-ICP disqualification and removed from the roster** — hosting and PaaS is an explicit M2 exclusion, WeKan has never worked with them so suppression does not apply, and it does not compete with WeKan for the same work. Roster **32 → 31 + 1 disqualified**; Tier 3 25 → 24; disqualified count 88 → 89. Corrected in `0926-target-accounts.md` and the `0926-m2-pursuit-order-snapshot.md` banner, which now also carries the full arithmetic: **31 scored + 2 C1-cleared + 7 cost-test + 19 consolidation = 59 potential, 28 pending gates.**

**Third file still stale: the published exec brief** (`claude.ai/code/artifact/19952fa8-…`). Deliberately not republished yet — the roster is mid-revision pending the four-signal decision, and republishing twice for one tally is waste. One pass once the model is settled.

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
