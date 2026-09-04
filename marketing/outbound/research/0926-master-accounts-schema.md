# The master account file — schema and rules

**File:** `data/0926-master-accounts.csv` · **Built by:** `scripts/build-master-accounts.py` · **Rows:** 115 · **Built:** 2026-09-04

This replaces the seven islands as the single place a sequence gets built from. It does
not replace `0926-target-accounts.md`, which stays the narrative record of *why* each
mark is what it is. **The CSV is the roster; the markdown is the reasoning.**

Rebuild it by re-running the script. Never hand-edit the CSV — the script is the only
writer, so a correction goes into the source island and then into a rebuild.

---

## Reconciliation — where the 115 come from

| Island | Rows | Overlap |
|---|---|---|
| `roster-31` | 31 | 2 also in cost-test (Alan, FreedomPay) |
| `cost-test-9` | 9 | 7 new, 2 already on roster |
| `consolidation-19` | 19 | none |
| `c1-fresh-pull-56` | 56 | none |
| `c1-gated-CHAT-ONLY` | 2 | Vinted, ShiftKey — never landed in a file |

29 + 2 + 7 + 19 + 56 + 2 = **115**. Domain is the only join key, normalised once
(lowercased, scheme and `www.` stripped). Zero duplicate domains; zero same-company
different-domain collisions.

---

## The three columns that make this different from a lead list

**`est_sentence`** — the verbatim qualifying sentence. Mandatory wherever EST scores.
This is the detection mechanism for the two defects no regex catches: `legacy` used as
heritage (Zeta), and a candidate requirement read as an estate fact (CMT, Cover Genius).
19 rows carry a sentence. **Read it before writing the email.**

**`est_window` / `hir_window`** — the date range of the rows the mark rests on. A mark
without a window is a claim without a vintage. 44 rows currently read
`DATES NOT IN REPO` — see the open gap below.

**`score_ceiling` + `tier_confidence`** — the maximum the account can still reach given
what has actually been retrieved, and what that does to the tier's meaning:

| `tier_confidence` | Rows | Meaning |
|---|---|---|
| `FIRM` | 36 | All four signals retrieved. The tier is a measurement. |
| `PROVISIONAL` | 9 | Can still reach Tier 1; one signal unretrieved. |
| `CANNOT REACH TIER 1` | 7 | Ceiling 40–55. Tier 2 is its permanent home under this model. |
| `UNSCOREABLE` | 63 | Ceiling below 37.5 — the Tier 2 line. **Not a low score. No score.** |

This column exists because a score alone presents an *unmeasured* account as a
*measured-and-weak* one. That is the UNKNOWN family at the level of the whole model,
and it is the single most load-bearing thing in this file.

**Ceiling distribution:** 75 → 36 rows · 60 → 9 · 55 → 4 · 40 → 3 · 35 → 43 · 15 → 20.

---

## `evidence_tier` — what class of email a row can carry

| Tier | Rows | What it can say |
|---|---|---|
| **A** — named pain, sentence on file | 19 | A first line quoting the target's own words about its own estate. |
| **B** — estate measured, no qualifying sentence | 33 | Category line. The estate *was* searched and the pain is not there. |
| **C** — estate never retrieved | 63 | Category line only, and the file says so rather than implying weakness. |

A ≠ Tier 1. Evidence tier says what the email may claim; account tier says how much
attention the account earns. They are different questions and they get different columns.

---

## Signals — weight, retrieval path, and what a mark means

Model B v2: **EST 25 · MRG 20 · HIR 15 · MDB 15**, max 75. T1 ≥ 56.25, T2 ≥ 37.5.
`AGE`, `SCL`, `VER`, `VOL` are **gates only** and do not score — each was applied during
sourcing, so the surviving population is near-constant on all of them.

| Signal | Retrieval path | Recency window |
|---|---|---|
| `EST` | job-postings pull | 12 months |
| `HIR` | job-postings pull, or Origami search-time boolean | 90 days |
| `MDB` | MongoDB product-stack detector, or job-advert slug (half credit) | 12 months |
| `MRG` | **Origami firmographics — `Ownership Type` / `Latest Round`. Not posting text.** | none |

**Marks:** `●` evidence in hand (full credit) · `◐` partial evidence (half) ·
`◑` weaker evidence tier (half) · `○` confirmed absent across an adequate sample (zero) ·
`⊗` measured absent, single source, provisional (zero) · `⊘` present but direction
disqualifies, or stale (zero) · `?` **UNKNOWN — never retrieved (zero, and lowers the
ceiling)** · `✕` known obstacle, a flag not a disqualifier.

**`MRG?` vs `MRG◐`.** 17 rows carry `MRG◐` awarded for being late-stage VC-backed —
but "Series C+ or $100M+ or PE-owned" was a *sourcing gate* every roster account passed
by construction. That is the capital gate re-scored as a trigger. Those 17 should read
`MRG?` pending a margin-event check. **Until that lands, treat Tier 1 = 8 as an upper
bound; the floor is roughly 4.** The `mrg_retrieval` column names which of the two any
given row rests on, verbatim.

---

## Open gaps, recorded rather than hidden

1. **The 949-row EST/HIR corpus is not in the repo.** Only its per-domain aggregate is,
   so 44 rows cannot show the dates behind their EST and HIR marks — including the
   recency window that moved Tier 1 from 10 to 8. That window is currently
   unverifiable from the repo. **Request `0926-est-hir-results-44-dated.csv`.**
   Only 8 rows have real date ranges, from the 58-row committed corpus.
2. **The 17 unsupported `MRG◐` marks.** See above. Retrieval question, not arithmetic.
3. **The 10-domain probe results are not in this file.** Turno and the other nine
   need adding, with the 4 zeros marked correctly — `EST?` if there were no postings
   at all, `EST⊘` if postings exist but predate the 12-month window. `EST⊗` means
   *searched one document and did not find it*, which is a third thing.
4. **`Latest Round` is blank on 13 of the 56 fresh-pull rows** (23%), so MRG and the
   scale gate have no retrieval path for those. Fourth instance of the
   unpopulated-column pattern, after `Ownership Type`, `Company Screen` and
   `Matching Posting Count`.
5. **Bondora** is pending as a 10th cost-test account and is not yet a row.

---

## Verification that runs on every build

Row count against island membership · duplicate domains · same company on two domains ·
**credit awarded where the retrieval path reads `NOT RETRIEVED`** · score equals the sum
of its marks · tier equals the threshold applied to the score · every evidence-tier-A
row has a non-empty sentence · every posting-derived EST has a window or an explicit
flag. All eight pass as of this build.
