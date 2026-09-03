# Handoff — Workstream 1: Origami sourcing

**Owner:** Rudra · **Written:** 2 September 2026 · **Scope:** ICP-M2 account sourcing via origami.chat
**Companion handoffs:** `handoffs/0926-handoff-gtm-execution.md` (workstream 2 — the accounts already sourced) · `handoffs/0926-handoff-origami-skill-spec.md` (workstream 3 — authoring the `origami-sourcing` skill)

---

## 0. What this chat is for

Sourcing ICP-M2 accounts through Origami: writing and correcting its prompts, evaluating its CSV output, and settling whether campaign C1 can run as a volume email motion.

**In scope:** Origami prompt authoring · CSV evaluation · credit budgeting · sourcing-shape diagnosis · the volume-vs-ABM test.

**Out of scope — belongs to workstream 2:** the 32 accounts already qualified, the marketing repo, ABM plans, messaging, Model B scoring, anything under `marketing/`. If a sourcing run adds accounts, this chat hands over a clean list; it does not write to the repo.

**Mode:** Mode 3 (Centaur). Rudra owns the calls on what to spend credits on and how to read the ICP; the assistant executes prompts, audits output, and argues.

---

## 1. Where things stand

Eight Origami pulls between 26 August and 2 September producing 17 CSVs, 400 credits (~4% of budget), 120 unique companies screened, 32 accounts qualified against ICP-M2. Every screen so far searched **firmographics first** and hoped a trigger was present. That is backwards — Intent is 30 of 100 points in WeKan's own scoring model, and firmographic-first sourcing scores zero on it by construction.

The correction is in flight: **trigger-first** searching (find the job posting, then filter by fit). The first two samples of that approach have landed and the qualify rate is **not yet settled**.

---

## 2. The live decision — is C1 a volume motion?

### Stock vs flow (the framing that unlocked this)

- A **firmographic screen** measures a *stock*: how many companies fit the profile right now. Banded sampling put that at roughly **40–150 accounts** across US + Europe, densest in the 600–1,200 employee band.
- A **trigger search** measures a *flow*: how many fitting companies enter the market each quarter by posting an infra role. Flow can be several times the stock, because accounts cycle in and out as they hire.
- **C1's viability depends on the flow, not the stock.** Every "the M2 universe is tiny" conclusion drawn from the firmographic runs is measuring the wrong quantity.

### Numbers on the table

| Quantity | Value | Confidence |
|---|---|---|
| Trigger population | ~7,400 individual job postings / 90-day window (Origami reported 7,377) | **Unverified aggregate.** Postings, not companies — and the index double-counts requisitions (proven 3 Sep: Alan's posting returned twice with byte-identical text). Deduplication method unknown, i.e. the same defect that retired `Matching Posting Count`. See `0926-origami-300-posting-prompt-v3.md` §A4. |
| Firmographic pool for comparison | 325 companies | Sourced, but not directly comparable to the above |
| Qualify rate, sample 2 | Origami said 4 of 30. Strict read: **2 of 30 (~7%)** | Weak — n=30 gives a CI of roughly 1%–22% |
| Converted to qualified companies | somewhere between **40 and 800** | Straddles the entire decision table |

Origami reported 4 qualified of 30 postings. Two of those four are **front-end platform roles** (both Lighthouse postings are "Engineering, Frontend Platform", Ember→React) that the role filter was meant to exclude, yet were marked `Role Match = true`. A third turns on an unresolved founding year. Strict read is 2 of 30.

**The filter is no longer the binding constraint — sample size is.**

### The threshold table (pre-registered; do not re-argue after the data lands)

M2's buying committee is 3–4 contactable people per account (CTO or VP Eng, Head of Platform, CFO). C1 targets one qualified meeting per 60–80 contacts.

| In-market qualified accounts | Contacts available | Verdict on C1 |
|---|---|---|
| 200+ | ~700+ | Volume motion viable — ~10 qualified meetings per cycle |
| 60–200 | ~200–700 | Hybrid: low-volume email on the cohort, ABM on the top accounts |
| under 60 | ~200 | ABM only. Under three meetings per cycle does not justify warming domains |

### The decisive experiment

**300-posting sample = 300 credits** (Origami charges 1 credit per job posting retrieved). Narrows the interval to roughly ±3 points — enough to land in one row of the table instead of across all three. Cheaper than what the trial has already spent. **This is the single highest-value next spend.**

Read two numbers off it: **trigger population before narrowing** × **qualify rate**. Their product is the answer.

Secondary check: does the sample surface qualified companies the firmographic pool never contained? If yes, the 40–150 stock estimate was too low.

---

## 3. Origami capability map

Hard-won across eight pulls. This is the most reusable output of the whole trial — it applies to every ICP, not just M2.

**Now measured, not asserted.** Of the 65 companies that appeared in more than one pull, **60 had a derived-judgment field contradict itself between runs; only 5 had any factual conflict, and 3 of those were cosmetic** (`500` vs `495` employees, `series_e` vs `SERIES_E`). `Transaction Evidence Review` alone contradicted itself on 60 companies — Carta came back `NO_EVIDENCE`, then `VERIFIED PER-PERIOD`, then `NO EVIDENCE`. Reproduce it from the `Field Conflicts` column of `0926-origami-companies.csv`.

**Reliable (sourced facts):**
founding year · headcount / headcount band · funding total · funding stage · ownership type · private-vs-public status · industry · HQ · job-posting text · tech-stack enrichment · exclusion logic for infra vendors and holding companies.

**Does not exist / unusable:**
- **Revenue estimates** — 0% coverage in two of three runs, 37% in the third.
- **Published transaction volume** — unverifiable. Three classifier attempts, three failure modes (§6).

**Unreliable (derived judgment — never accept as a column):**
fit score · inferred evidence classification · "Company Screen" pass/fail · public-status determination · role-match booleans.

> **Standing rule:** never accept a derived judgment column from the sourcing tool. Ask for the underlying facts and do the judgment here. Every collapse in this trial traces to trusting a column Origami computed rather than retrieved.

**Note:** Origami *does* handle technographics — `Enrich Tech Stack` at 2.5 credits/company, or 1 credit/domain for the website-only variant. Earlier guidance in this project that said otherwise was wrong. TheirStack is planned for deeper hiring + technographic work but is not a reason to skip Origami here.

---

## 4. Origami pricing (from platform screenshots, 2 Sep 2026)

> *"Only data costs credits. The thinking is free."*

| Call | Cost |
|---|---|
| Company Search | 0.5 / result |
| Job Posting Search | 1 / result |
| Enrich Tech Stack | 2.5 / company |
| Enrich Tech Stack (Website) | 1 / domain |
| Web Research | 1 / call |
| Verified Email | 3 / email |
| Verified Phone | 15 / phone |
| Browser Automation | 5 / session |

Planning consequence: iterating on prompts is free. Only pull data once the shape of the request is settled.

**Also note:** Fit Score is a platform default. It is not a data defect and it is not worth prompting against — disregard it in analysis. (Three instructions were burned learning this.)

---

## 5. Run log — 8 pulls, 17 CSVs, 333 data rows, 120 unique companies

Verified 2 September by reading all 17 files. The three audit batches share identical filenames with different contents — keep them apart by timestamp.

| # | Time | Pull | CSVs | Rows | Result |
|---|---|---|---|---|---|
| 1 | 10:37 | Infrastructure-hiring screen | `infrastructurehiringaccounts20260902.csv` | 23 | First candidate pool; independent assessment named 11 T1 / 5 T2 |
| 2 | 10:55 | Scale-first firmographic screen | `scalefirstplatformaccounts20260902.csv` | 28 | Headcount-descending under a cap → all rows clustered at the ceiling |
| 3 | 11:17 | Amended scale-first screen | `scalefirstplatformaccountsamended20260902.csv` | 8 | Same clustering failure recurred |
| 4 | 12:56–57 | Transaction audit + banded sample, v1 | `transactionevidenceaudit` + bands a/b/c | 60 + 2/5/3 | Classifier fabricated evidence (§7). Band files carry only the *qualified* rows, not the full band |
| 5 | 13:32 | Transaction audit + banded sample, v2 (post rule-fix) | same four filenames | 60 + 16/17/5 | Blank-field fix applied; bands re-populated |
| 6 | 17:10 | Transaction audit + banded sample, v3 | same four filenames | 60 + 11/11/11 | Balanced 11-per-band re-run. Source of the 40–150 stock estimate |
| 7 | 18:09 | Trigger-first SRE sample | `srejobpostings20260902.csv` | 7 | 7,377-posting flow figure. **7 rows shown + 23 hidden exclusions = the 30-posting sample** |
| 8 | 19:02 | Trigger-first SRE corrected re-sample | `srepostingscorrectedsample20260902.csv` | 6 | Role-match and funding-branch corrections; exclusion audit came back clean |

**Important:** the CSVs contain the returned/qualified subset, never the full sample. The "30 postings" and "23 exclusions" figures come from Origami's prose report and reconcile exactly against the 7-row CSV. Any future sample should ask for the excluded rows as a file, not a count.

## 6. Four sourcing-shape failures, and the rules that fix them

**1 · Headcount-descending sort under a result cap** (happened three times)
Sorting by headcount descending with a 60-result cap returns 60 companies all pinned at the ceiling — it samples *around* the target band rather than *into* it. **Rule:** never sort by the same dimension you are capping on. Use banded stratified sampling: fix a band, sample within it, repeat.

**2 · Revenue field unusable** (0% coverage twice, 37% once)
**Rule:** do not gate on revenue. Use funding total + stage + ownership type as the scale proxy.

**3 · Infra vendors and public companies leaking through** (repeatedly — ACV Auctions, Angi, Temporal, WEKA, Tines)
Exclusion needs to be explicit and structural, not left to Origami's judgment. **Rule:** name the exclusion categories in the prompt and require the *reason* for each exclusion as a column.
The final exclusion audit came back mutually exclusive and complete: vendor 6 · holding company or subsidiary 4 · founded after 2018 3 · private status 2 · industry 2 · capital path 5 · non-commercial 1 = 23. **None** of the 23 was driven by a blank field. The filter is not quietly discarding good accounts — that was the main risk and it is cleared.

**4 · Blank field read as FAIL**
A blank `Company Screen` collapsed 59 of 60 accounts. **Rule:** *a blank field is UNKNOWN, not FAIL.* State this explicitly in every prompt. Unknowns go to a review bucket; they do not fail the gate.

---

## 7. The transaction-volume classifier — three attempts, three distinct failure modes

1. **Inverted labels** — pass/fail applied backwards.
2. **Blank-field gating** — the failure in §6.4.
3. **Fabrication** — 20 of 21 rows marked "verified per-period volume" had no period phrase anywhere in the source text. EliseAI's entire company description is a single sentence containing no digits.

**Conclusion: retire VOL as a gate.** Transaction volume is now a *ranking input* (10 points in Model B) and a *discovery question* on the call. Do not spend more credits trying to source it. If a future run needs it, require the verbatim source sentence as a column and audit it by hand.

---

## 8. Prompting constraints that now hold

Carry these into every Origami prompt for ICP-M2:

1. One ICP × one trigger × one offer per search. Separate searches per trigger **add** rather than intersect — the combined pool is larger than any single firmographic screen produced.
2. Trigger first, firmographics second.
3. Blank = UNKNOWN, never FAIL.
4. Return facts, not judgments. No fit scores, no evidence classifications, no pass/fail screens.
5. Require an explicit exclusion reason per excluded row.
6. Never sort on the capped dimension. Band and stratify.
7. Do not gate on revenue or transaction volume.
8. **Lead with the MongoDB signal.** A company hiring an SRE *and* naming MongoDB in the posting hits Intent and Accessibility in the scoring model simultaneously — the trigger and the co-sell channel in the same account. The ICP's own signal library already lists job posts as a source for it.

### Rule 0 — the campaign governs, not the ICP (settled 3 September)

**When sourcing for a named campaign, use the campaign's numbers.** `ICP.md` defines who is a good-fit *customer*; the campaign spec defines who goes into the *sequence*. Those are different jobs and cold outbound deliberately targets wider than it qualifies. Cross-check the campaign gates against the ICP to surface conflicts, resolve any conflict explicitly, and never silently pick one.

Source of campaign gates: `WeKan Outbound Campaign Prioritization` (Claude project doc, August 2026). **Read it before writing a prompt for any campaign.**

**C1 (M2) targeting gates — these govern M2 sourcing:** 200–5,000 employees · US/EU · latest round Series C or later OR $50M+ raised OR PE-owned OR bootstrapped-profitable · private, not SPAC-bound · logistics & delivery, insurtech, fintech, marketplaces, SaaS · **gate on Atlas / large cloud estate signals** · SRE hiring *or* efficiency signals.

**Why this is Rule 0.** Ten prompts in this trial were built at M2's *qualification* thresholds — 200–2,500 employees and $100M+ raised — instead of C1's *targeting* thresholds of 200–5,000 and Series C+/$50M+. Every pull was filtered at roughly half the intended headcount ceiling and half the funding floor, which under-filled the funnel by construction. Worse, three tech-stack searches filtered `NOT MongoDB` while C1 gates *on* Atlas signals — the searches were excluding the campaign's own primary estate gate.

**Conflict audit, 3 September.** Only M1 and M2 carry size tables in `ICP.md`. M1 and C3 agree. M2 and C1 disagree on both headcount and funding. P2, A1, P1 and A2 have no size tables, so no collision is possible there yet — but none has been reconciled either, so the same conflict will appear if those tables are ever written.

**Calibration consequence.** C1's baselines (reply 4–8%, positive 1.5–3%, ≥1 meeting per 60–80 contacts) assume C1's targeting gates. Sourcing at the tighter ICP thresholds feeds the sequence a higher-fit list than the baseline expects, so reply rate would beat baseline for reasons unrelated to the copy and the 30-day review would draw the wrong conclusion.

### ICP interpretation settled with Rudra (apply, don't relitigate)

- **Industries.** M2 names six sectors (logistics & delivery, insurtech, fintech, marketplaces, vertical SaaS, travel tech) followed by "digital-native companies with real transaction volume." The **qualifier is the gate**; the six sectors are where that type is typically found. Consequence: Workrise and Metropolis qualify; Brainly does not (its volume is read traffic, not transactions).
- **Geography.** "US and Europe primary" describes whether the **proof transfers**, not where engineers sit. US-headquartered platforms with Indian engineering orgs stay in scope — where WeKan's India presence is an advantage. Unblocks Zeta and FarEye.
- **Source of truth** for the ICP is `WeKan_Consulting_Practice_ICPs.docx`, not the condensed project `.md`. The condensed version drops travel tech.

---

## 9. Open items — in priority order

1. **Run the 300-posting sample (300 credits), with the role-filter audit built in.** Settles the C1 volume question against the §2 threshold table, and simultaneously measures how often the role filter is wrong — which is what item 3 is really about.

   > **Use the v3 prompt in `0926-origami-300-posting-prompt-v3.md`, not the block below.** v3 corrects five
   > defects in this one: the missing unique-companies divisor (this prompt reports postings while the §2 table
   > is denominated in accounts), the dropped one-row-per-posting instruction from P11, sort-under-cap on the
   > posting draw, requisition-level double-counting, and `Date Posted` returning the retrieval date. The block
   > below is kept for provenance.

```text
STEP 1 — SEARCH ON THE TRIGGER.
Companies with open roles matching: SRE, Site Reliability, DBRE,
Database Reliability, Infrastructure Engineer, or Platform Engineering
WHERE THE PLATFORM IS INFRASTRUCTURE, NOT FRONT-END. Exclude any
posting whose body is about UI, web front-end, design systems or
client-side frameworks, even when the title says "Platform Engineer" —
that exact title returned an Ember/React/TypeScript role last time.
Posted in the last 90 days. Retrieve 300 postings. Do not exceed 300.

STEP 2 — NARROW BY ICP-M2 FIT.
  - Founded 2018 or earlier
  - 200-2,500 employees
  - $100M+ raised with latest round Series C or later, OR PE-owned,
    OR bootstrapped and profitable
  - Private: not publicly listed, not SPAC-bound
  - US or Europe
  - Digital-native with real transaction volume, typically logistics &
    delivery, insurtech, fintech, marketplaces, vertical SaaS, travel
    tech. Treat that list as indicative of the type, not exhaustive —
    an adjacent-industry digital platform with genuine transaction
    volume qualifies; flag it ADJACENT and name the industry.
  - EXCLUDE companies whose own product is infrastructure: databases,
    hosting, PaaS, developer platforms, observability, data
    connectivity, GPU compute, workflow orchestration.
  - EXCLUDE portfolio and holding companies operating independent
    brands.

STEP 3 — ROLE-FILTER AUDIT. This applies to all 300 postings, whether
or not they pass Step 2. For each posting return the verbatim job title
and quote the one sentence from the posting body that establishes
whether infrastructure, platform, database or reliability work is the
core of the role. Do not return a role-match boolean without that
quote. In the last sample two of six matched postings were front-end
platform roles (Ember/React/TypeScript) sitting under the title "Lead
Platform Engineer", so I need the false-positive rate of the filter
itself, not your verdict on it.

STEP 4 — SPLIT ON DATABASE TECHNOLOGY. Quote verbatim every database
or data-infrastructure technology named in each posting, with the
sentence it appears in, then group:
  GROUP 1 — names MongoDB or MongoDB Atlas
  GROUP 2 — names MySQL, Postgres, MSSQL or a named monolith
  GROUP 3 — names other data infrastructure
  GROUP 4 — none named
Quote the sentence, not just the term: a previous run returned
"oracle" for Chainlink Labs, which is a blockchain oracle network.

STEP 5 — RETURN FACTS ONLY.
Company · domain · founded year · employee count · total funding ·
funding stage · ownership type · HQ location · engineering location
where stated · verbatim job title · posting date · posting URL ·
verbatim technology mentions · industry (or ADJACENT + industry).

No transaction-volume column, no fit scores, no screening flags, no
role-match boolean without its quote. A blank field is UNKNOWN, not
FAIL — return the row with the field marked unknown.

REPORT: trigger population before narrowing; postings retrieved;
postings passing the role audit; companies qualified after Step 2; and
the excluded rows as a table with one reason each.

COUNTS: if you report any per-company posting count, state its role
scope, its domain scope, and its deduplication method alongside it. A
count without all three is to be returned as UNKNOWN, not as a number.

If anything above cannot be established without a further retrieval,
say so rather than estimating.
```
2. **`Enrich Tech Stack` on the 32 accounts (~80 credits).** Turns the MongoDB gate from inference into data at 2.5/company. Hand the result to workstream 2.
3. **`Matching Posting Count` — retired, not deferred. Resolved 3 September; no further spend.** Origami answered the free question honestly and completely:

   - **Role list confirmed** and it is sound: SRE · Site Reliability · Platform Engineering · DBRE · Database Reliability · Infrastructure Engineer.
   - **Domain scope: cannot be determined.** The stored value is an aggregate count with no domain-by-domain breakdown.
   - **Deduplication: cannot be determined.** Unknown whether one requisition posted to several boards, or one role open in several locations, counted once or many times.
   - Origami's own conclusion: *"396 for Alan and 66 for Chainlink Labs should be treated as unverified aggregate counts, not reliable company-specific posting counts."* It declined to estimate and saved itself a rule that future counts must show role scope, domain scope and deduplication method.

   **Consequence: the column is UNKNOWN for all 32 accounts, not a pending verification.** It cannot be repaired retroactively — the breakdown was never stored. Strike it from Model B inputs. It can be rehabilitated on future pulls only if the three disclosures come with it, which item 1's prompt now requires.

   **The role list being sound changes the read on the false positives.** The filter is not broadly over-matching; one term is leaky. *"Platform Engineering"* catches front-end platform roles — Lighthouse's *Lead Platform Engineer* is Ember/React/TypeScript. Item 1's Step 1 now qualifies that term explicitly. This is better news than feared for the 300-posting sample: the earlier 2-of-30 read was depressed by one bad term, not a broken filter.

   **Method note worth keeping.** The clause *"if any of these cannot be answered without a new retrieval, say so rather than estimating"* is what produced a clean refusal from the same tool that once marked 21 companies "verified" with no supporting text. Put it at the end of every prompt.
4. **Review the 23 hidden exclusions.** Origami offers this in suggested next actions. Low cost, closes the audit.
5. **Consider a look-alike search** on the qualified 32 as an alternative sourcing path. Rudra raised it; not yet evaluated against trigger-first.
6. **Confirm two firmographics:** Owner.com's founding year (sits right on the 2018 boundary) and Signifyd's two-vintage figures.

---

## 10. Interface with workstream 2

- **This chat produces:** new qualified accounts with sourced firmographics, plus tech-stack enrichment.
- **Hand over as:** a plain list of account names + the sourced fact columns. No scoring, no tiering, no cohort assignment — that happens in workstream 2 against Model B.
- **Do not touch** the marketing repo or either published artifact from this chat.
- **Escalate to workstream 2** if a run changes the account count, since two artifacts and one repo file all carry the tally.

---

## 11. Files and sources — all committed, nothing to re-attach

Everything this chat needs is in the repo. Do not ask Rudra to re-upload CSVs.

| Path | What it is |
|---|---|
| `marketing/outbound/research/data/0926-origami-companies.csv` | **All 120 unique companies**, every fact column merged across the 8 pulls. Columns `Seen In Pulls`, `Pull Count`, `On Qualified Roster` give provenance; `Field Conflicts` lists every field where two pulls disagreed. This replaces all 17 raw CSVs for company-level work. |
| `marketing/outbound/research/data/0926-origami-job-postings.csv` | **36 job-posting rows** with full descriptions and posting URLs, from pulls P1, P7 and P8. Any role-match claim can be re-audited from source here. |
| `handoffs/0926-origami-prompt-log.md` | **All 14 verbatim prompts** written to Origami, in order, annotated with what each fixed and whether it worked. |
| `handoffs/0926-handoff-origami-skill-spec.md` | Skill-authoring spec derived from the above — trigger conditions, procedure, failure catalogue, eval cases. |
| `marketing/outbound/research/0926-m2-pursuit-order-snapshot.md` | The 32 qualified accounts with gate evidence. |
| `marketing/icp/ICP.md` | All six ICPs, in-repo, replacing the docx as the working reference. |

The 17 raw CSVs are superseded by the two consolidated files and are not needed. If a future run has to be reconciled against a specific pull, the `Seen In Pulls` column identifies which.

**Published artifacts** (read-only reference for this chat):
- ICP-M2 Pursuit Order — `claude.ai/code/artifact/aefe4ddd-5bfe-4920-bae3-57dde74a158d`
- What the M2 Sourcing Trial Bought — `claude.ai/code/artifact/19952fa8-f0dc-4472-b449-409e53d61ea3`

## 12. Counts — settled 2 September

Both discrepancies are resolved. **Use these figures.**

| Figure | Value | How derived |
|---|---|---|
| Unique companies screened | **120** | Domain dedupe across all 17 CSVs. 120 distinct names map one-to-one onto 120 distinct domains, no blank domains, no name with two domains — so the count is clean, not an estimate. Supersedes the earlier 119 and 124. |
| Qualified accounts | **32** | The Pursuit Order roster |
| Origami pulls | **8** | CSV timestamps, §5 |
| Total CSV data rows | 333 | Across 17 files, with overlap between runs |
| Credits | 400 (~4% of budget) | Rudra's figure |

The exec brief was republished 2 September with all of these corrected, including its cohort table (A 5 · B 7 · C 2 · D 15 · E 2 · suppression 1 = 32) and a 3%/4% wobble in the body. It had been carrying 119 / 31 in the tally strip and 29 / 114 in the body. `marketing/latest.md` said 124 and has been corrected.

Editing either artifact requires recovering its source first: the session scratchpad that held the HTML is gone, so use `Artifact action:"read"` on the URL before republishing to the same URL.
