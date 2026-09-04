# Workstream 1 → Workstream 2: corrections to `0926-master-accounts.csv`

**Written:** 4 September 2026 · **Workstream 1: Origami sourcing** · **Mode 3 (Centaur)**
**Data file:** `marketing/outbound/research/data/0926-w1-master-corrections.csv` — join on `domain`
**Scope:** 14 rows. I did not edit `0926-master-accounts.csv`. The master list is yours; these are inputs to it.

---

## What this replaces

You asked for the 9 cost-test rows as CSV and the C1 gated pair. Both are already in your master
(`source_islands = cost-test-9` and `c1-gated-CHAT-ONLY`), so a raw dump would have been duplicate work.
What you could not have is the measurement below, because it required running your pinned term list against
posting text that only exists in `0926-origami-job-postings.csv`.

The 9-vs-7 count gap is closed: **9 qualified, 7 new to roster.** Alan and FreedomPay were already on the
qualified 32, so they were never pending. Bondora is a 10th, in the review bucket, and is missing from master.

---

## 1 · Six accounts scored on retired or unsupported EST evidence

Two EST files exist for the 44-domain pull and they disagree on 9 domains:

- `marketing/outbound/research/data/0926-est-hir-results-44.csv` — **superseded.** No date column. Its EST
  marks were read without a recency window, which is how "reliability"/"toil" boilerplate scored as estate pain.
- `Claude outputs/0926-est-hir-results-44-dated.csv` — **canonical.** 12-month window, your pinned 9 terms,
  545 distinct dates, separate `Pain postings (12m)` and `Pain postings (all time)` columns.

Master picked up the dated verdict on 3 of the 9 (backmarket, blockchain, netradyne) and the superseded one
on 5. Alan is a sixth case of the same class from a different route.

| domain | master | canonical | score now | corrected | tier now | tier corrected |
|---|---|---|---|---|---|---|
| cabify.com | EST● | EST⊘ | 40.0 | 15.0 | 2 | 3 |
| fabric.inc | EST● | EST⊘ | 25.0 | 0.0 | 3 | UNSCORED |
| minted.com | EST● | EST⊘ | 25.0 | 0.0 | 3 | UNSCORED |
| teacherspayteachers.com | EST● | EST⊗ | 45.0 | 20.0 | 2 | 3 |
| vinted.com | EST● | EST○ | 40.0 | 15.0 | 2 | 3 |
| alan.com | EST● | EST○ (measured here) | 40.0 | 15.0 | 2 | 3 |

**Vinted is the one to look at first.** The dated file reads `EST○ absent across 67 requisitions` with
**0 pain postings in 12 months and 0 all time**, from 108 postings. That is the best-evidenced absence
anywhere in this dataset — 67 distinct requisitions is an enumerated set, not a sample. Master has it at
`evidence_tier = A - named pain, sentence on file`, and the sentence it inherited was tagged
`[reliability/toil]`, which is the exact boilerplate class that produced the 43%-of-postings false-positive
rate. Vinted has a live infra posting; it does not have named estate pain.

**Alan's EST● has no retrieval behind it.** `est_sentence` is empty, `est_retrieval` reads
`roster hand-read, pre-pull`, and Alan is **not** in the 44-domain pull. I ran your 9 pinned terms against
Alan's full P9 posting text — 24,714 characters, dated 2026-09-02 — and got **zero hits.** Recommend EST○
until a dated sentence exists.

### Grep signature for the rest

Every row master sourced from the superseded file carries `est_retrieval = job-postings pull ()` — with an
**empty parenthetical** where the window should be, because the superseded file had no dates to put there.
That is a structural tell, not a judgement call. Worth sweeping for beyond these six.

---

## 2 · Seven cost-test accounts move from UNSCORED to measured

These sat at `EST? / HIR?` and score 0. Their full job descriptions **are** committed — 3,838 to 7,011
characters each, tagged `Pull = P9 cost-test` — so this is an enumerated read of complete text, not a
sampled sentence. Mark them **`EST○`**, not `EST⊗`.

Every posting is dated 2026-08-31 to 2026-09-02, i.e. 2 to 4 days old, so **`HIR●` live** on all seven.

| domain | EST | HIR | score now | corrected | note |
|---|---|---|---|---|---|
| mollie.com | EST○ | HIR● | 0.0 | 15.0 | |
| chrono24.com | EST○ | HIR● | 0.0 | 15.0 | |
| facile.it | EST○ | HIR● | 0.0 | 15.0 | names bare word `database` only |
| meilleurtaux.com | EST○ | HIR● | 0.0 | 15.0 | names BigQuery |
| origamirisk.com | EST○ | HIR● | 0.0 | 15.0 | |
| oeconnection.com | EST○ | HIR● | 15.0 | 30.0 | MDB● already on file |
| capitalontap.com | EST○ | HIR● | 15.0 | 30.0 | MDB● on file; CAPITAL-PATH: DEBT |

All seven stay below the T2 line of 37.5, so this does not promote anyone. What it changes is the **action**:
`UNSCORED` means "go retrieve"; `EST○ / HIR●` means "measured, weak on named pain, stop spending." That is
worth more than a tier bump — it takes seven accounts out of the retrieval queue for free.

OEC and Capital on Tap reach 50.0 and clear T2 **if MRG resolves positive**. They are the only two accounts
in this cohort where MRG is worth buying.

This also fully reverses my earlier error of crediting 7 cost-test accounts with EST before their text was
committed. The text is now committed and measured, and the answer is zero. Retracted with data, not just
withdrawn.

### The inversion worth recording

This was the cohort that looked hottest — live infra hiring, postings 2 days old. Measured against full text
it is the **weakest** cohort on named pain: zero estate language in 19 of 19 companies. The only EST hit in
the entire 22-row cost-test pull is **OnBoard**, which we excluded under P3 (productivity software), and its
`legacy` refers to a legacy *monitoring stack* — observability tooling, not the transaction estate. Wrong
layer even if it had qualified.

Live hiring and estate pain are close to uncorrelated in this data. HIR is a budget signal; EST is a pain
signal. Do not let one stand in for the other.

---

## 3 · Bondora is missing from master

115 rows, no `bondora.group`. It is the pending 10th from the cost test: 2008, 224 employees, Estonia, P2P
lending marketplace. Funding stage returned `Public` while ownership returned `private` and total funding is
blank — blank is UNKNOWN not FAIL, so it belongs in the review bucket rather than nowhere. Its P9 posting text
(6,105 chars, 2026-09-01) carries zero pinned terms and names Databricks. One web-research credit settles the
ownership contradiction. Strong ICP type fit if it resolves private.

---

## 4 · Log only, no action

- **Smartcat names MongoDB** (`MongoDB; Kafka`) in its P9 posting. Smartcat is excluded on funding
  ($28.9M series_c fails the amount gate). If the funding gate is ever revisited, it is an MDB● candidate.
- **`rechargepayments.com` is stored as `https://rechargepayments.com`** in `0926-c1-fresh-pull-graded.csv`.
  Protocol prefix on a domain field will break a join. Same class as the other dirty-key defects.
- **ShiftKey checks out.** Dated file: 7 pain postings in 12m, sentence dated 2026-04-15,
  *"executing a migration to a new AWS region... reducing tech debt."* `HIR○`, no posting in 90 days.
  Master has it at Tier 3 / 25.0 / EST● / HIR○ — consistent, no change. One caveat: an AWS **region**
  migration is infrastructure relocation, not necessarily a database estate. The terms hit legitimately and
  the date is in window, so EST● stands, but the layer is unconfirmed.

---

## 5 · Where the 46-domain EST pull fits

Running now (approved by Rudra, 4 Sep). It closes `EST?` on the 46 fresh-pull accounts that have no estate
retrieval at all. Two things from the 10-domain probe that change how to read it:

1. **The boolean held — 0 false negatives of 10.** No fresh-pull domain has an infra posting inside 90 days.
   Newest was Integral at 94 days. So `HIR` is settled at fail for that cohort; do not re-buy it.
2. **6 of 10 have posting text inside 12 months, 4 have none.** The 4 with none cap at 35 and cannot be
   tiered. The 6 keep EST access and can still reach T1. Your unscoreable-vs-stale distinction is confirmed
   empirically. Mark the 4 zeros `EST⊗`, not `EST○` — a domain-scoped posting search is near-enumeration but
   not proof, and Otter at 513 employees returning zero infra postings in 12 months is as consistent with
   index coverage failure as with reality.
3. **New EST● candidate from the probe: Turno** (turno.com, 213 emp, US). *"migrating our Integrations and
   Payments rails ... onto a modern TypeScript platform on GCP"*, dated 2025-12-15. Both `migrat*` and
   `moderni*`, in a named program on payments infrastructure. Estate layer unnamed — no database mentioned.

Cost note: the probe projected **12 credits for 10 domains** (1/lead, NO-MATCH rows billed). Price tracks
postings **returned**, not domains queried. The 14.5/domain rate came from the roster cohort, which posts
~20 postings/domain; the fresh-pull cohort returns under 1. Any future pull priced off the roster rate will
be wrong by an order of magnitude.
