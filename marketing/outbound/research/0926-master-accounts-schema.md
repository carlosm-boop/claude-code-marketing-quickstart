# The master account file — schema and rules

**File:** `data/0926-master-accounts.csv` · **Built by:** `scripts/build-master-accounts.py` · **Rows:** 116 · **Built:** 2026-09-04

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
| `w1-corrections` | 13 | Overrides from `data/0926-w1-master-corrections.csv` |
| `w1-corrections-review` | 1 | Bondora — a row that was missing entirely |

29 + 2 + 7 + 19 + 56 + 2 + 1 = **116**. Domain is the only join key, normalised once
(lowercased, scheme and `www.` stripped). Zero duplicate domains; zero same-company
different-domain collisions.

## Precedence — which source wins

1. **`w1-corrections`** — a measurement with a recorded retrieval path.
2. **The dated 44-domain pull** (`0926-est-hir-results-44-dated.csv`), recency-windowed.
3. **The roster** (`0926-target-accounts.md`) — but only where it carries a sentence.
4. **The undated 44-domain pull** — superseded; retained only for `Databases Named`.
5. **Firmographic columns** from the four sourcing CSVs, first non-empty wins.

**A measurement with a retrieval path beats a roster hand-read that carries no
sentence.** This rule was added on workstream 1's Alan finding: the roster had Alan at
`EST●` from a hand-read with an empty `est_sentence` and `est_retrieval` reading
*"roster hand-read, pre-pull"*. Running the pinned 9-term list against Alan's full P9
posting text — 24,714 characters, dated 2026-09-02 — returned **zero hits**. Alan is
`EST○`, and drops from Tier 2 to Tier 3. The roster is the narrative record of the
reasoning; **it is not a retrieval path**, and the first version of this build had the
precedence backwards.

---

## The three columns that make this different from a lead list

**`est_sentence`** — the verbatim qualifying sentence. Mandatory wherever EST scores.
This is the detection mechanism for the two defects no regex catches: `legacy` used as
heritage (Zeta), and a candidate requirement read as an estate fact (CMT, Cover Genius).
19 rows carry a sentence. **Read it before writing the email.**

**`est_window` / `hir_window`** — the vintage of the mark: the ISO date of the qualifying
posting, plus how many pain postings fell inside the 12-month window against all-time.
A mark without a window is a claim without a vintage. `est_pain_postings_12m` next to
`est_pain_postings_alltime` is the stale-vs-current test, mechanically: Cabify reads
0 of 3 and is `EST⊘`.

**`score_ceiling` + `tier_confidence`** — the maximum the account can still reach given
what has actually been retrieved, and what that does to the tier's meaning:

| `tier_confidence` | Rows | Meaning |
|---|---|---|
| `FIRM` | 36 | All four signals retrieved. The tier is a measurement. |
| `PROVISIONAL` | 9 | Can still reach Tier 1; one signal unretrieved. |
| `CANNOT REACH TIER 1` | 14 | Ceiling 40–55. Tier 2 is its permanent home under this model. |
| `UNSCOREABLE` | 56 | Ceiling below 37.5 — the Tier 2 line. **Not a low score. No score.** |
| `REVIEW BUCKET` | 1 | Bondora — an unresolved gate, not a score. See below. |

This column exists because a score alone presents an *unmeasured* account as a
*measured-and-weak* one. That is the UNKNOWN family at the level of the whole model,
and it is the single most load-bearing thing in this file.

**Ceiling distribution:** 75 → 36 rows · 60 → 9 · 55 → 11 · 40 → 4 · 35 → 43 · 15 → 13.

---

## `evidence_tier` — what class of email a row can carry

| Tier | Rows | What it can say |
|---|---|---|
| **A** — named pain, sentence on file | 14 | A first line quoting the target's own words about its own estate. |
| **B** — estate measured, no qualifying sentence | 46 | Category line. The estate *was* searched and the pain is not there. |
| **C** — estate never retrieved | 56 | Category line only, and the file says so rather than implying weakness. |

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

1. ~~The 949-row EST/HIR corpus is not in the repo.~~ **Closed 2026-09-04.** The
   verification check for a missing date window found the dated file *was* in the repo
   all along — as `Claude outputs/0926-est-hir-results-44-dated.csv`, outside `data/`.
   Copied to `data/` and now the authoritative EST/HIR source. Every one of the 14
   evidence-tier-A rows carries an ISO date for its qualifying posting plus the
   12-month and all-time pain-posting counts. **The underlying 949 posting rows are
   still uncommitted** — only the per-domain aggregate is here — so a re-read of any
   individual posting is not possible from the repo. That is a smaller gap than it was
   and it is the remaining half.
2. **The 17 unsupported `MRG◐` marks.** See above. Retrieval question, not arithmetic.
3. **The 10-domain probe results are not in this file.** Turno and the other nine
   need adding, with the 4 zeros marked correctly — `EST?` if there were no postings
   at all, `EST⊘` if postings exist but predate the 12-month window. `EST⊗` means
   *searched one document and did not find it*, which is a third thing. All three
   score zero, so no tier moves either way; the mark is the audit trail.
4. **`Latest Round` is blank on 13 of the 56 fresh-pull rows** (23%), so MRG and the
   scale gate have no retrieval path for those. Fourth instance of the
   unpopulated-column pattern, after `Ownership Type`, `Company Screen` and
   `Matching Posting Count`.
5. **Bondora** is now a row, in the `REVIEW` bucket rather than given a tier. Its
   funding stage returned `Public` while ownership returned `private` and total funding
   is blank — a contradiction between two columns, which is an unresolved *gate*, not a
   weak score. Blank is UNKNOWN, not FAIL. Its P9 posting text (6,105 chars, dated
   2026-09-01) returns zero pinned terms and names Databricks. **One web-research
   credit settles the ownership question**, and until it is settled a tier number would
   be a guess wearing a number's clothes.

6. **Seven cost-test accounts now read `EST○` on measurement, reversing an earlier
   credit.** Workstream 1 ran the pinned 9-term list against the committed P9 posting
   text for all 19 cost-test companies — full descriptions, 3.8k to 24.7k characters —
   and found **zero hits across every one**. Mollie, Chrono24, Facile.it, Meilleurtaux,
   Origami Risk, OEC and Capital on Tap move from `UNSCORED` to measured `EST○` with
   `HIR●` live, all on postings dated within five days of the pull. That is a real
   downgrade in evidence and an upgrade in *knowledge*: they were unmeasured, now they
   are measured-and-absent, and their ceilings rise from 35 to 55 or 75 accordingly.

---

## Verification that runs on every build

Row count against island membership · duplicate domains · same company on two domains ·
**credit awarded where the retrieval path reads `NOT RETRIEVED`** · score equals the sum
of its marks · tier equals the threshold applied to the score · every evidence-tier-A
row has a non-empty sentence · every posting-derived EST has a window · every
evidence-tier-A row's window contains an ISO date · **every workstream-1 correction
actually landed on the row it names** · no corrected signal still reads
`NOT RETRIEVED`. **All eleven pass as of this build.**

Two of these checks have already earned their place. Check 8 found the recency-windowed
EST/HIR file sitting outside `data/`, which closed gap 1 and moved Tier 2 from 15 to 12.
Check 5 caught the Bondora row being scored before its marks were set — a bug in the
build order, not in the data.
