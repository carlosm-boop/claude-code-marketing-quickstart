# EST pull — final prompt. 44 domains, EST-only.

**Domains:** `handoffs/0926-est-hir-pull-domains.md` (44, cost-test block struck after the P9 merge).
**Cost:** ~30–60 credits, 1/posting retrieved. **Buys:** EST (25 pts). HIR now arrives free at search time.
**Role exclusions updated 3 Sep:** *AI Platform* and *Data Platform* added — workstream 2 measured the leaky
"Platform Engineering" term at **3 of 7 on P9** (Facile.it DevEx, Meilleurtaux AI-Azure, Chrono24 zero infra
terms). Second confirmed instance after Lighthouse's Ember/React req; the new variant is AI-platform, not
front-end. Same term, new costume.

```text
Job posting pull against a specific domain list. I am not searching for
new companies — I want the posting text for accounts I already have.

DOMAINS — 44. Return a row for EVERY domain, including ones with no
matching posting. That absence is data I am paying for; a domain that
silently does not appear is useless to me.

[paste the 44 domains]

ROLES: SRE, Site Reliability, DBRE, Database Reliability, Infrastructure
Engineer, Platform Engineering — INFRASTRUCTURE ONLY.

EXCLUDE these role variants explicitly. All three have already produced
false positives on this exact term:
  - front-end or web platform roles, even titled "Platform Engineer" —
    one came back as an Ember-to-React migration
  - AI Platform / ML Platform roles — measured at 3 of 7 on the last
    pull; an AI platform is not a database estate
  - Data Platform or analytics-platform roles where the work is
    pipelines and warehousing rather than production transactional
    databases
  - engineering-leadership reqs (Head of, VP, Director)

For each posting, count infrastructure terms versus non-infrastructure
terms in the BODY and return both counts. Do not judge the role from its
title — the title has been wrong every time it has been tested.

RETURN, one row per posting, not per company:
  domain · company · verbatim job title · posting date AS THE SOURCE
  STATES IT (never today's date — two previous trigger pulls returned
  the pull date on every row) · posting URL · THE FULL POSTING TEXT ·
  infra term count · non-infra term count · every database or
  data-infrastructure technology named, quoted in the sentence it
  appears in.

For a domain with no matching current posting, return one row marked
NO CURRENT MATCHING POSTING. Do not omit it.

DEDUPLICATE TO REQUISITIONS. For rows sharing a company and title, say
whether the descriptions are identical, near-identical or different, and
assign a requisition ID. Keep every row; show me the rate. Last time
Alan's "Senior Platform Engineer" came back twice at two LinkedIn IDs
with byte-identical 8,238-character descriptions.

No fit verdict, no fit score, no estate-pain assessment. I read the text
and make that call myself.

Quote the sentence for every technology, not the extracted term — a
previous run returned "oracle" for Chainlink Labs, which is a blockchain
oracle network.

REPORT: domains queried · domains with at least one matching posting ·
postings retrieved · distinct requisitions · cost per posting.

If anything above cannot be established without a further retrieval, say
so rather than estimating.
```

## Caution on EST as a signal, for whoever finalises the weights

Workstream 2 measured EST as a **measured absence on all 7** cost-test accounts — no estate-pain sentence, one
database named across all seven. That is a real improvement over a blank. But note what the measurement rests
on: **one job posting per company.**

A company can carry an enormous legacy estate and not mention it in a single SRE requisition. So "measured
absence from one posting" is materially weaker than "this company has no estate pain," and EST is the heaviest
signal in the four-signal model at 25 of 75.

Two consequences worth deciding before the weights lock:

1. **The 7 are structurally capped at 50 of 75** — Tier 2 at best — on the strength of one req each. If that
   is not intended, EST should be measured across *all* of a company's infra postings rather than the first
   one returned, which is what this pull's per-domain multi-row return makes possible.
2. **Consider whether 25 points is the right weight for a signal read from a single posting.** The six roster
   positives came from P1, the same source type, so the measurement is at least consistent — but consistency
   is not the same as depth.

Not this workstream's call. Raised because the pull about to run is what the weight rests on.

## Pool sizing — Origami's own answer, and why to stop chasing it

Origami, asked directly: **1,506 was a projection from the original 30-company sample, not a count.** Current
projection ~862 with ~6,435 raw companies unfetched, and its own caveat that *"neither number should be
treated as an exact TAM for campaign sizing."*

So all three figures — 2,723, 1,506, 862 — are projections off the **same stale 30-row sample**, 16 rows of
which are in Asia, South America or Africa and can never pass the gates. A fresh gated draw is still owed.

**But the decision no longer needs the number.** C1's first calibration window needs **143** accounts. The
most pessimistic projection is **862**. Even wrong by 4× that is enough. The pool question consumed most of
3 September and is now answered in the direction of "sufficient" — treat any further precision as
nice-to-know, not blocking.
