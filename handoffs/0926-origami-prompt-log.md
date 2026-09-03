# Origami prompt log — 14 verbatim prompts, 26 Aug – 2 Sep 2026

Every instruction written to origami.chat during the ICP-M2 sourcing trial, recovered verbatim from the session transcript and kept in order. Annotations say what each was fixing and whether it worked.

**Why this file exists:** the rules in the handoff are abstracted from these. When authoring an Origami skill, work from the prompts, not from the summary of the prompts — the phrasing is what did the work.

**Read `handoffs/0926-handoff-origami-skill-spec.md` alongside this.**

---

## P1 · Opening gate set — scale-first

Pull 2. First fully structured prompt: six numbered gates, hard exclusions, an explicit 'do not gate on revenue' clause, and hiring signal demoted to a ranking layer. **Outcome: partial failure.** Returned rows clustered at the headcount ceiling because the search sorted descending on the same dimension it capped.

```text
Build a scale-first target list for ICP-M2 (Scaled Digital Platform).

SELECTION GATES — all must hold, applied before any hiring signal:
1. Founded 2018 or earlier (MVP-era architecture requires elapsed time).
2. Total headcount 250–2,500 (ICP requires an engineering org of
   50–500; 500 total headcount caps out below that).
3. Funding: $100M+ raised total AND latest round is Series C or later,
   OR PE-owned, OR bootstrapped-and-profitable. Use latest round date
   — treat funding data older than 18 months as unverified.
4. Vertical: logistics/delivery, insurtech, fintech, marketplaces,
   vertical SaaS, travel tech.
5. Company-side transaction volume evidence: GMV, payment volume,
   order count, trips, policies, or API call volume — stated by the
   company. Customer AUM or market-size figures do NOT count.
6. Geography: US or Europe.

HARD EXCLUSIONS:
- Companies whose product is infrastructure: databases, hosting,
  PaaS, observability, log/data platforms, GPU compute.
- Companies founded 2019+ regardless of funding.
- Subsidiaries of larger public companies (buying committee is gone).

DO NOT use revenue estimates as a gate — your coverage is ~37% and
missing data would exclude qualified accounts. Report revenue where
available as a tiebreaker only, labeled as an estimate.

THEN apply hiring signal (SRE, platform, DBRE, infrastructure roles,
90-day window) as a timing/urgency layer that ranks the qualified set.
Do not use it to select into the set.

Output: for each account, list which gate evidence you found and which
you could not verify. Flag stale funding data explicitly.
```

---

## P2 · Amendments to the scale-first search

Pull 3. Raised the ceiling to 2,500 and adjusted funding logic. **Outcome: same clustering failure recurred** — proof that raising a cap does not fix a sort-under-cap problem. Banding does.

```text
AMENDMENTS to the scale-first search:

1. Raise the headcount ceiling to 2,500. The 500 cap is currently the
   dominant selection variable — the returned list is 449–499 employees,
   sorted descending. ICP requires an ENGINEERING org of 50–500, which
   at typical ratios means 250–2,500 total headcount. The current cap
   makes the top 80% of the ICP invisible.

2. Add a company-age gate: founded 2018 or earlier. "MVP-era
   architecture" is a claim about elapsed time. Vertice (founded 2021)
   passed at 479 employees.

3. Enforce the vertical list as a hard gate, not a preference. Only
   5 of 28 returned companies are in the named verticals.

4. Hard-exclude infrastructure vendors: databases, hosting, PaaS,
   developer platforms, durable execution, observability, data
   connectivity, GPU compute. Temporal, CData and Port.io are
   suppliers to this ICP, not members of it.

5. Exclude POST_IPO_EQUITY and SPAC-bound companies. Two got through.

6. Stop emitting Fit Score. It has been 100 for every row across two
   lists. Either return a differentiated score or return none — a
   saturated score reads as ranking and is not.

7. Refresh funding stage before returning. Pushpay came back as
   POST_IPO_EQUITY; it was taken private by BGH Capital and Sixth
   Street in 2023.
```

---

## P3 · Continue, do not re-search

Screening instruction over the ~478 raw matches already retrieved. Pattern worth keeping: an explicit 'do not start a new search' sentence stops the tool re-pulling and re-charging.

```text
Continue the scale-first ICP-M2 screen. Do not start a new search — screen
the ~478 raw matches still unscreened from the amended criteria.

=== FIX FIRST: SAMPLING ===

Both previous runs returned results sorted by employee count descending,
so both returned only the largest companies under the ceiling. Run 1
returned 449–499 employees against a 500 cap. Run 2 returned 1,540–2,225
against a 2,500 cap. This is the single biggest problem with the output.

Do NOT rank, sort, or order results by employee count.

Instead, screen and report in three headcount bands, separately:
  Band A:   200–600 employees
  Band B:   600–1,200 employees
  Band C: 1,200–2,500 employees

Report each band as its own group with its own qualified count and its own
raw-match count. I need to see where fit density actually sits across the
band, not just the top slice. If you must cap output, cap it per band, not
across the whole set.

=== KEEP (these worked) ===

- Founded 2018 or earlier. Keep as a hard gate and keep Founded Year as
  a returned column.
- Headcount ceiling 2,500, floor 200.
- Funding: $100M+ total raised AND latest round Series C or later, OR
  PE-owned, OR bootstrapped-and-profitable.
- Refresh funding status before returning. This caught Zuora, Litera and
  iCapital correctly.
- Exclude public and SPAC-bound companies.
- Exclude infrastructure vendors: databases, hosting, PaaS, developer
  platforms, durable execution, observability, data connectivity, GPU
  compute, log/data platforms.
- No Fit Score. Do not add any composite or overall score in its place.

=== DROP ===

Remove Annual Revenue entirely — as a gate, as a criterion, and as a
column. Coverage has been 0%, 37% and 0% across three runs. It is dead
weight and it silently excludes qualified accounts.

=== ADD: TRANSACTION VOLUME GATE (this is now the binding constraint) ===

The company's own systems must process a countable, recurring flow, stated
publicly by the company. Acceptable evidence: orders, payments processed,
bookings, policies written, claims, trips, listings, card transactions,
shipments, API call volume, or an equivalent per-period operational count.

Explicitly NOT acceptable as volume evidence:
- assets under management belonging to the company's customers
- spend under management, or contract value the platform touches
- total addressable market or industry-size figures
- number of customers, users, or employees served, on its own

Return the exact figure and the exact wording you found it in. If you
cannot find company-side volume evidence, mark the account UNVERIFIED on
this gate rather than passing it — do not substitute a customer-asset
figure. This filter matters more than any other: it is what separates a
real database estate from a company that sounds large.

=== ADD: TWO MISSED EXCLUSIONS ===

1. Portfolio and holding companies that operate independent brands or
   businesses. No single estate, no single CTO owning a margin question.
   (Run 2 returned Red Ventures, which is this.)

2. Desktop, document and productivity software whose primary deployment
   is inside Microsoft 365, Google Workspace, or on-premises. High user
   counts there do not indicate a high-volume cloud database estate.
   (Run 2 returned Litera, which is this.)

=== TIGHTEN: VERTICAL GATE ===

Verticals: logistics and delivery platforms, insurtech, fintech,
marketplaces, vertical SaaS, travel tech.

"Vertical SaaS" has been acting as a catch-all — it admitted legal tech,
digital media, parking and intranet software across the two runs. Apply it
only where the company sells software to one named industry AND passes the
transaction volume gate above. When in doubt, return the account with the
vertical marked BORDERLINE and name the industry, rather than passing or
dropping it silently.

=== ADD: ENGINEERING LOCATION (report, do not gate) ===

Return the location of the engineering organization, not just the corporate
HQ, where the company states it. Several accounts have a US headquarters
and a majority-offshore engineering org. Report it; I will decide whether
it qualifies.

=== OUTPUT COLUMNS ===

Company Name | Domain | Founded Year | Employee Count | Headcount Band |
Total Funding | Funding Stage (refreshed) | Ownership (VC / PE / bootstrapped
/ corporate) | Vertical (or BORDERLINE + industry) | Transaction Volume
Evidence (figure + source wording, or UNVERIFIED) | HQ Location |
Engineering Location | Gates Passed | Gates Unverified | Notes on stale or
conflicting data found

For every account, state which gates you verified and which you could not.
An unverified gate is information I need, not a reason to pass or drop.

=== BEFORE YOU RUN ===

Tell me the estimated credit cost for screening all ~478, and the raw-match
count in each of the three bands. If the full screen is expensive, screen 20
per band first (60 total) and report the per-band qualify rate so I can
decide whether to scale.
```

---

## P4 · Hold and fix

Issued when the transaction-evidence classifier began contradicting itself. Stops work mid-run rather than letting a broken classifier write 60 rows. The template for interrupting a bad run.

```text
Hold the full screen. The transaction-evidence classifier is producing
contradictory output and I don't want it applied at scale.

Evidence of the problem, from your own two tables in this run:
- Five of ten companies got different labels in the audit table vs the
  band tables: FarEye (NO_EVIDENCE -> VERIFIED PER-PERIOD), Vanta
  (VERIFIED -> NO EVIDENCE), Netradyne (CUMULATIVE_ONLY -> VERIFIED
  PER-PERIOD), ezCater (NO_EVIDENCE -> CUMULATIVE ONLY), iCapital
  (CUMULATIVE_ONLY -> NO EVIDENCE).
- Labels contradict their own values: Netradyne's value literally says
  "(cumulative)" and is labelled VERIFIED PER-PERIOD. Weee!'s "1 million
  orders per month" and ezCater's "millions of orders a year" are both
  labelled CUMULATIVE ONLY.
- No magnitude check: Zeta is VERIFIED on "300+ Transactions per year"
  for a platform with 25M+ cards issued. Blockchain.com returned
  "1500+ transactions processed" for a crypto exchange.

Fixes required before scaling:
1. Classify from the extracted value itself. If the value contains a
   period word (per day/month/year, daily, annually), it is PER-PERIOD.
   If it says cumulative, since inception, or to date, it is CUMULATIVE.
   Never label a value "per-period" when the value says cumulative.
2. Add a magnitude sanity check. Flag IMPLAUSIBLE rather than VERIFIED
   when the figure is inconsistent with headcount and business model
   (300 transactions/year at 2,225 employees).
3. Return one label per company across all tables. Reconcile the audit
   and band tables before delivering.
4. Drop Fit Score. In the audit table all ten Fit Score 100 rows are
   exactly the ten VERIFIED rows — it is a copy of the evidence column,
   not a second signal.
5. Fix the public-company filter. ACV Auctions (NASDAQ: ACVA) came
   through as SERIES_E, and the "Handy HQ / angi.com" row is Angi
   (NASDAQ: ANGI) with Handy's pre-acquisition funding — the same
   name/domain mismatch you flagged for Whatfix and HiBob, unflagged.

Then re-run the 10 qualified accounts as a test. When all three tables
agree and no public companies appear, screen the 325.

Separately: your raw-pool figure moved from ~478 last run to 325 (195 +
85 + 45) this run. Which is correct, and what changed?
```

---

## P5 · Scope pin

Disambiguates which table an instruction applies to when several are in play. Origami will otherwise apply a correction to the wrong artifact.

```text
Scope: this is about the BANDED SEARCH and the rules behind it — the
Transaction Evidence Audit table (60 rows) and the Band A / Band B /
Band C tables (10 qualified). Do not touch the original 23-company
hiring-led table; that one is a separate request below.

Apply fixes 1, 2, 3 and 5 to the SAVED ACCOUNT-SCREENING RULES, not
just to rows in the audit table. Relabelling 60 rows leaves the same
defects in place for the 325-company screen. The public-company filter
in particular has now failed in three consecutive runs across three
different tables (WeRide and PlusAI in the amended run, ACV Auctions
and Angi in the banded run) — that is a rules-level defect.

Then reconcile the existing audit and band tables so they agree, and
re-run only the 10 qualified accounts as a test. Screen the 325 once
all tables agree and no public companies appear.
```

---

## P6 · Conditional approval

Approves a next step subject to two conditions and one change. Shows the shape: never approve a plan wholesale, itemise what must hold.

```text
Good work on the reconciliation and the 478/325 answer. Two things
before I approve the 325 screen, and one change to how it runs.

1. Send me the per-account results of the 10-account test: for each
   company, the extracted figure, its verbatim source wording, and
   which of the four buckets it landed in. Four aggregate counts do
   not let me review nine rejections. I specifically need Weee!
   ("1 million orders per month") and ezCater ("millions of orders a
   year") — if the corrected classifier still calls those anything
   other than verified per-period, the fix is incomplete.

2. Test the public-company filter against known positives. The clean
   pass on the 10 band accounts is a null result — none of them was
   public. Run the filter against ACV Auctions (NASDAQ: ACVA) and the
   "Handy HQ / angi.com" row (Angi, NASDAQ: ANGI), both of which it
   previously passed as private. Report whether it now catches them.

3. CHANGE TO THE 325 SCREEN: transaction volume is no longer a
   qualifying gate. It yielded 1 of 60, which rejects on whether a
   company publishes a per-period number rather than on fit.

   Qualify on: founded 2018 or earlier; vertical on the ICP list;
   $100M+ raised with latest round Series C or later, OR PE-owned, OR
   bootstrapped-and-profitable; private (not public, not SPAC-bound);
   not an infrastructure or developer-platform vendor; not a portfolio
   holding company; 200-2,500 employees.

   Then RETURN transaction volume as three reported columns —
   figure, verbatim source wording, bucket (per-period / cumulative /
   none / implausible) — and use it to rank the qualified set, not to
   filter it. No account is dropped for lacking a published figure.

   Report qualified counts per band so I can see where density sits.

Once 1 and 2 come back clean, run the 325 under those rules.
```

---

## P7 · The blank-field collapse correction

The single most expensive lesson. A blank `Company Screen` field was being read as FAIL, collapsing 59 of 60 accounts to one qualified. This prompt names three accounts whose own rows contradicted the verdict.

```text
The qualified count of 1 is wrong. Three accounts in the band tables
carry VERIFIED PER-PERIOD status: Weee! (Band B), Zūm (Band A) and
ID.me (Band B). Only Weee! was counted because it is the only one of
the three whose Company Screen field is populated. That field is blank
on 28 of 38 band rows, and blank is being treated as a failure.

Fix that first: either populate Company Screen for every row, or treat
blank as "not yet screened" rather than "failed". Then re-report the
qualified counts per band.

Three other items from the last request are not done:

1. Labels are not normalised. The audit table contains seven distinct
   strings for four buckets: NO_EVIDENCE and NO EVIDENCE,
   CUMULATIVE_ONLY and CUMULATIVE ONLY, VERIFIED and VERIFIED
   PER-PERIOD. Pick one string per bucket and rewrite every row.

2. Reconciliation covers 38, not 60. The audit table has 60 companies;
   the band tables have 16 + 17 + 5 = 38. Which 22 are missing and why?
   Zūm and ID.me also still disagree between tables.

3. Fit Score was not dropped — it is now 100 for all audit rows and 75
   for the band rows, so one company carries two scores. Remove the
   column.

4. The public-company filter is still untested. ACV Auctions
   (NASDAQ: ACVA, tagged SERIES_E) and the "Handy HQ / angi.com" row
   are both still marked VERIFIED in the audit table and appear in no
   band table. Run the filter against those two specifically and tell
   me whether it catches them.

5. ezCater is still CUMULATIVE ONLY on "millions of orders a year".
   "A year" is a period. Check why that case still fails.

Do not run the 325 screen yet. When you do, apply the gate change I
sent: transaction volume becomes three reported columns (figure,
verbatim source wording, bucket) used to RANK the qualified set — not
to filter it. Qualify on age, vertical, funding/ownership, private
status, not-a-vendor, not-a-holding-company, 200-2,500 employees.
```

---

## P8 · Retire the classifier

Ends three attempts at transaction-volume classification after three distinct failure modes. Names the exact reason, so the tool does not re-propose it.

```text
Stop work on the transaction-evidence classifier. Three attempts have
produced three different failure modes and this batch is the worst:

- 20 of the 21 rows marked VERIFIED PER-PERIOD contain no period phrase
  in their source text. EliseAI's entire description is "Fixing housing
  and healthcare with agentic AI to improve how we live" — no digits —
  and it is marked verified.
- Tines, whose text actually says "thousands of mission-critical
  workflows per day", is marked NO EVIDENCE.
- The audit and band tables disagree on 15 of 33 shared companies.
- The figures and source wording were removed and replaced with a bare
  VERIFIED/UNVERIFIED flag, so the column cannot be audited.

Remove the transaction-evidence column entirely. Do not attempt a
fourth pass.

Run the 325-company screen on FACTUAL criteria only, which have been
reliable throughout:
  founded 2018 or earlier · 200-2,500 employees · $100M+ raised with
  latest round Series C or later, OR PE-owned · private (not public,
  not SPAC-bound) · US or Europe · vertical on the ICP list

Return only: company, domain, founded year, employee count, headcount
band, total funding, funding stage, ownership, HQ location, engineering
location where stated. No fit score, no evidence column, no screen flag.
Report counts per headcount band.

Two data corrections to make first, both outstanding since the last
three requests:
1. ACV Auctions is NASDAQ:ACVA and the "Handy HQ / angi.com" row is
   Angi, NASDAQ:ANGI. Both are public. Remove them and tell me the
   public-company filter now catches them.
2. Drop Fit Score. It has been a constant 100 for three runs.
```

---

## P9 · Context reset

'Ignore the previous searches — this is a different shape and I don't want contamination.' Origami carries state between runs; a new search shape needs an explicit reset.

```text
New search. Ignore the previous scale-first and banded searches — this
is a different shape and I don't want criteria carried over.

We're sourcing for ONE ICP, ONE TRIGGER, ONE OFFER.

ICP: WeKan ICP-M2, The Scaled Digital Platform.
TRIGGER: active infrastructure hiring — open roles for SRE, Site
Reliability, Platform Engineering, DBRE, Database Reliability, or
Infrastructure Engineer, posted within the last 90 days.
OFFER: 2-week savings-quantified estate assessment.

STEP 1 — SEARCH ON THE TRIGGER FIRST.
Find companies with those roles open in the last 90 days. The trigger
is the primary selector, not a filter applied afterwards. I want the
trigger population, then narrowed.

STEP 2 — NARROW BY ICP FIT.
  - Founded 2018 or earlier
  - 200-2,500 employees
  - $100M+ raised with latest round Series C or later, OR PE-owned,
    OR bootstrapped and profitable
  - Private: not publicly listed, not SPAC-bound
  - US or Europe
  - Industry: logistics or delivery platforms, insurtech, fintech,
    marketplaces, or vertical SaaS. These five only — not travel,
    not media, not HR, not compliance or security tooling.
  - EXCLUDE companies whose own product is infrastructure: databases,
    hosting, PaaS, developer platforms, observability, data
    connectivity, GPU compute, workflow orchestration.
  - EXCLUDE portfolio and holding companies operating independent
    brands.

STEP 3 — RETURN FACTS ONLY.
Company · domain · founded year · employee count · total funding ·
funding stage · ownership type · HQ location · engineering location
where stated · the exact job titles found and their posting dates ·
job posting URLs · any database or infrastructure technologies named
in those postings, quoted verbatim.

No transaction-volume column. No screening flags. No derived scores.
I only want facts and the verbatim job-post text.

Report the trigger population size before narrowing, and the qualified
count after, split by headcount band (200-600 / 600-1,200 /
1,200-2,500).

SEPARATE QUESTION, answer before running: can you source technographic
signals — specifically companies with MongoDB or MongoDB Atlas in their
stack? That is both a trigger and a channel for us, so if you can
source it, it becomes the next search.
```

---

## P10 · **The trigger-first template — the one that works**

Pull 7. Four numbered steps: search the trigger, narrow by fit, split on database technology, return facts only. Note the last line of Step 4: *no transaction-volume column, no screening flags, no derived scores.* This is the prompt any new sourcing skill should be built from.

```text
STEP 1 — SEARCH ON THE TRIGGER.
Companies with open roles for SRE, Site Reliability, Platform
Engineering, DBRE, Database Reliability or Infrastructure Engineer,
posted in the last 90 days. Trigger first, then narrow.

STEP 2 — NARROW BY ICP-M2 FIT.
  - Founded 2018 or earlier
  - 200-2,500 employees
  - $100M+ raised with latest round Series C or later, OR PE-owned,
    OR bootstrapped and profitable
  - Private: not publicly listed, not SPAC-bound
  - US or Europe
  - Digital-native companies with real transaction volume, typically in:
    logistics & delivery platforms, insurtech, fintech, marketplaces,
    vertical SaaS, travel tech. Treat that list as indicative of the
    type, not exhaustive — a digital-native platform with genuine
    transaction volume in an adjacent industry qualifies; flag it as
    ADJACENT and name the industry so I can judge.
  - EXCLUDE companies whose own product is infrastructure: databases,
    hosting, PaaS, developer platforms, observability, data
    connectivity, GPU compute, workflow orchestration.
  - EXCLUDE portfolio and holding companies operating independent brands.

STEP 3 — SPLIT THE OUTPUT ON DATABASE TECHNOLOGY.
Quote verbatim every database or data-infrastructure technology named
in each job posting, then group the qualified accounts:
  GROUP 1 — posting names MongoDB or MongoDB Atlas
  GROUP 2 — posting names MySQL, Postgres, MSSQL or a named monolith
  GROUP 3 — posting names other data infrastructure
  GROUP 4 — no database technology named
Group 1 is the priority set.

STEP 4 — RETURN FACTS ONLY.
Company · domain · founded year · employee count · total funding ·
funding stage · ownership type · HQ location · engineering location
where stated · exact job titles and posting dates · job posting URLs ·
verbatim technology mentions · industry (or ADJACENT + industry).

No transaction-volume column, no screening flags, no derived scores.
Report the trigger population before narrowing and the qualified count
after, split by headcount band (200-600 / 600-1,200 / 1,200-2,500).
```

---

## P11 · Staged execution with a checkpoint

'Run it as one prompt, pausing after the first sample.' Buys a correction point before the tool spends credits at scale. Also carries three pre-emptive corrections.

```text
Yes, run it as one prompt, pausing after the first sample. Three
corrections first.

1. THERE IS NO TRANSACTION-VOLUME GATE. Do not apply one, visibly or
   invisibly. My phrase "digital-native companies with real transaction
   volume" was describing the company TYPE, quoted from our ICP
   document — it was not an instruction to test volume. Delete it as a
   criterion.

   Your transaction-evidence classifier has failed three times: it
   inverted per-period and cumulative labels, then rejected 59 of 60
   accounts because a screening field was blank, then marked 21
   companies "verified per-period" when 20 of them had no period
   phrase anywhere in their source text. Running that logic where I
   cannot see it is worse than running it visibly. Do not run it.

   Also remove it from the SRE-triggered rules you just saved to the
   scaled digital-platform profile, or the error persists into every
   future search.

2. NO INTERNAL FIT CHECK BEYOND THE FACTUAL FILTERS. Enforce exactly
   these, all of which are objective and checkable:
     founded 2018 or earlier · 200-2,500 employees · $100M+ raised with
     latest round Series C or later, OR PE-owned, OR bootstrapped and
     profitable · not publicly listed, not SPAC-bound · US or Europe ·
     industry is one of: logistics & delivery platforms, insurtech,
     fintech, marketplaces, vertical SaaS, travel tech
   Plus the two exclusions: companies whose own product is
   infrastructure (databases, hosting, PaaS, developer platforms,
   observability, data connectivity, GPU compute, workflow
   orchestration), and portfolio or holding companies operating
   independent brands.

   Nothing else. No scoring, no inferred fit, no hidden screen. If a
   company clears those filters it goes on the list and I decide.

   Where an industry is adjacent rather than exactly on the list,
   include it and mark it ADJACENT with the industry named. Do not
   drop it and do not decide for me.

3. OUTPUT IS ONE ROW PER JOB POSTING, not per company. The MongoDB
   grouping depends on what each posting says — a company with three
   open infra roles may name MongoDB in one and Postgres in another,
   and collapsing to "most relevant posting" loses the mention that
   puts it in Group 1. Add a company-level column for the total count
   of matching postings; the number of open infra roles is signal in
   itself.

SAMPLE SIZE: 15 companies per headcount band, 45 total. Do not rank or
sort by employee count — the previous searches each returned only their
largest companies under the ceiling, so I need a spread across each
band, not the top of it.

Report the trigger population before narrowing and the qualified count
after, per band. Then pause.
```

---

## P12 · Demand the exclusions

Asks for the rows the account rules removed, not just the count. The resulting audit is what proved no exclusion was driven by a blank field.

```text
Yes — show me the 23 postings the account rules excluded. That is the
next thing I need, because four of the seven that passed should not
have:

- Kraken: founded 2019, fails the "2018 or earlier" gate. It also has
  no funding total and no funding stage, so that gate did not run.
- Aurora Energy Research: industry is "Research Services", and the
  role is Head of Software Engineering — a leadership hire, not an SRE,
  platform, DBRE or infrastructure req.
- Lighthouse: Founded Year and Industry are both BLANK, so neither gate
  ran. The role is "Lead Platform Engineer, Frontend Platform" — an
  Ember-to-React migration. Frontend platform is not the trigger.
- FreedomPay: industry is "IT Services and IT Consulting". It does
  qualify, but via PE ownership, not the industry rule.

Also: Ownership Type is blank on all 7 rows, and Matching Posting Count
returned 1,119 / 15,398 / 393 — those look like global corpus counts,
not per-company posting counts. I asked for the number of matching
postings for that company.

So: keep the filter strict, but make it actually run. Specifically —
  - Populate Founded Year and Industry for every row, and reject rows
    where either is unknown rather than passing them through.
  - Populate Ownership Type.
  - Enforce the role list. Accept only SRE, Site Reliability, Platform
    Engineering, DBRE, Database Reliability, Infrastructure Engineer.
    Exclude frontend platform roles and engineering-leadership roles.
  - Fix Matching Posting Count to be per company.

Two questions before the next batch:
1. Is 7,377 a count of postings or of companies, and over what window?
   That number decides whether this campaign runs as volume outbound or
   as named-account ABM, so I need to know exactly what it counts.
2. Of the 23 exclusions, how many were excluded for each reason —
   industry, age, funding, ownership, private status, vendor exclusion,
   holding company? A breakdown by reason tells me whether the filter
   is loose, tight, or just inconsistent.

Do not scale to the full pool yet.
```

---

## P13 · Sequencing under a budget

'Option 4, in that order... do not scale.' Orders three requested actions and refuses the tool's offer to scale the sample before the cheap checks are done.

```text
Option 4, in that order — exclusions first, then the 7,377 definition,
then the corrected sample. Do not scale past a small sample.

One correction on the corrected table: do not make the checks
stricter. The problem is not that the filter is too loose — it is that
it is not running. Four of the seven passing rows had blank or wrong
gate fields: Lighthouse had no Founded Year and no Industry at all,
Ownership Type was blank on all seven rows, and Kraken had no funding
total or stage.

Tightening thresholds on top of unpopulated fields will reject rows
for missing data rather than for real disqualification. That already
happened in the banded run, where a blank Company Screen field caused
59 of 60 accounts to be reported as failing.

So for the corrected table:
  - POPULATE Founded Year, Industry, Ownership Type and Funding Stage
    for every row.
  - Then apply the existing rules unchanged — same thresholds.
  - A blank field is UNKNOWN, not FAIL. Return the row with the field
    marked UNKNOWN and let me judge it. Never drop a row for missing
    data.
  - Enforce the role list, which was not applied: SRE, Site
    Reliability, Platform Engineering, DBRE, Database Reliability,
    Infrastructure Engineer only. Exclude frontend-platform roles and
    engineering-leadership roles.

On the exclusion audit, I want the breakdown by reason — how many of
the 23 were excluded for industry, age, funding, ownership, private
status, vendor exclusion, holding company, and how many for a missing
or unknown field. That last count is the one I care about most.

On the 7,377: is it postings or companies, and over what time window?
```

---

## P14 · Acceptance and next step

Accepts a clean audit explicitly, so the tool does not re-litigate it, and names what comes next.

```text
Good audit — the exclusion breakdown is what I needed, and "none
excluded solely for a blank field" answers the main question. 7,377 as
postings over 90 days is clear.

Three corrections to the corrected sample, then one request.

1. The role filter did not run. Both Lighthouse postings are marked
   Role Match = true and counted as qualified. Their own text says
   "Engineering, Frontend Platform" and describes an Ember-to-React
   migration. That is the category the filter was meant to exclude, and
   it is half your qualified set. Exclude both.

2. FreedomPay is qualified, not undecided. The rule is "$100M+ raised
   OR PE-owned". Your own Ownership Type column says PE-owned, so the
   OR branch resolves it. Mark it qualified.

3. Chainlink Labs should be excluded, not undecided. You excluded it
   from the original 23 as an infrastructure-product company, and
   vendor exclusion is a hard filter that fires before funding. Also,
   its Database Technology Mentions field reads "oracle" — that is
   Chainlink's own product, decentralized oracle networks, not Oracle
   the database. Worth checking whether that pattern is producing other
   false positives.

   Kraken stays undecided, not qualified — you flagged the 2019 vs 2016
   founding discrepancy and then passed it anyway. Undecided is right
   until the entity's founding date is settled.

So the strict read is 2 of 30 qualified: Alan and FreedomPay.

THE REQUEST: pull a 300-posting sample, same rules, same 90-day
window. At 1 credit per posting that is 300 credits, and it is the only
thing that will settle the campaign question — 2 of 30 gives a
confidence interval wide enough to be consistent with anywhere between
40 and 800 qualified companies, which is not a decision.

For the 300: report qualified postings, qualified unique companies, and
postings-per-qualified-company. That last ratio is the one I am missing
— Alan shows 396 matching postings and FreedomPay shows 3, and I need
to know whether that column is per-company or something else.
```

---
