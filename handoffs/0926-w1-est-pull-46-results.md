# Workstream 1 → Workstream 2: the 46-domain EST pull, and a retraction

**Written:** 4 September 2026 · **Workstream 1: Origami sourcing** · **Mode 3 (Centaur)**
**Data:** `marketing/outbound/research/data/0926-w1-est-marks-46-domains.csv` — 46 rows, join on `domain`
**Source:** `infrastructurejobevidence20260904.csv`, 452 rows / 441 postings / 46 domains, 12-month window

---

## 0 · Retraction first: the boolean IS a false-negative generator

I told you the probe vindicated the `Infra/SRE Posting` boolean — 0 false negatives of 10 — and that HIR was
settled at fail for the fresh-pull cohort, don't re-buy it. **That was wrong, and this pull is the evidence.**

The 6 boolean-`true` domains are emburse, filevine, fresha, kyriba, snapsheetclaims, softheon. All 6 have a
live infra-titled posting inside 90 days, so the boolean has no false *positives*. But **15 of the 40
boolean-`false` domains in this pull also have one:**

`arbitersports · arisglobal · curvedental · dealersocket · ecp123 · fireblocks · mambu · medius · pcmicorp ·
podium · promise-pay · roofr · socure · stampli · storable`

**False-negative rate 15/40 = 37.5%**, measured on 40 domains rather than 10. Under the pre-committed rule
(≥3 of 10 → the boolean is a false-negative generator) this fires decisively — in the opposite direction to
what I reported yesterday.

### Why the probe got it wrong

Not a bad draw. A bad query. P(0 of 10 | p=0.375) = 0.91%, which is possible but unlikely; the retrieval
density is the real tell:

| pull | domains | postings | per domain |
|---|---|---|---|
| 10-domain probe | 10 | 8 | 0.8 |
| this 46-domain pull | 46 | 441 | 9.6 |

Same tool, one day apart, overlapping population, **12× difference**. The probe asked for
"infrastructure, platform, SRE, DBRE, database reliability or devops"; this pull asked for
"infrastructure, platform, SRE, DBRE, **database**, devops **or backend**". I widened the role filter between
pricing the probe and running the pull, and then read the probe's thin return as a population fact.

**The lesson, for the skill:** a negative result from a retrieval is only as strong as that retrieval's
recall, and recall is unknown unless you measure it. An absence is a claim about the world only when the
retrieval that produced it has been shown to find things. Mine hadn't. This is the ninth instance of the
UNKNOWN family and the first where the defect is in the *instrument's sensitivity* rather than in a field.

Your `tier_confidence` column already models this correctly. `UNSCOREABLE` was the right call and I argued
against it on the strength of a measurement that could not support the argument.

---

## 1 · What the pull actually returned

Origami **left both extraction columns empty** — `Keyword Quotes` and `Database Quotes` are blank on all 441
rows. Taken at face value that reads as "zero estate language in 441 engineering postings", which is not
credible. It shipped the full posting text in `Raw Data` as JSON with a populated `description` field
(1,453–10,786 chars, median 4,866), so the pull is fully rescuable and I ran your pinned terms myself.

**Do not read a blank extraction column as a measured absence.** Tenth instance of the family.

### Marks

| mark | count |
|---|---|
| `EST●` | 5 |
| `EST○` measured absent across full description text | 30 |
| `EST?` no postings retrieved in 12m, never measured | 11 |
| `HIR●` live infra-titled posting ≤90d | 21 |
| `HIR○` infra postings but none live | 14 |
| `HIR?` no postings at all | 11 |
| `MDB●` | 1 |
| `MDB?` named as a requirement only | 3 |
| `MDB○` | 42 |

`EST?` (11): birchstreetsystems · fieldpulse · kenect · owner.app · porteiro · softgamings · suvoda ·
tabit.cloud · tispayments · tyfone · wibmo.

---

## 2 · The five `EST●`, in order of strength

**1 · ECP (`ecp123.com`) — the best-qualified account in the dataset.** 2026-08-27, eight days old.

> "We're migrating off a ColdFusion legacy platform, and the two will coexist for a while."
> "SQL Server and PostgreSQL, a mix of monolith and services, adopting domain-driven design and an
> event-driven architecture, all on AWS."

First person, present tense, named legacy platform, named relational estate, a monolith, and an explicit
coexistence period. That last clause *is* provisioning debt stated by the company. Also worth flagging for
ICP routing: SQL Server is M1's technographic signature sitting inside an M2-band company.

**2 · Fresha (`fresha.com`).** 2026-08-15.

> "We are in the process of switching away from our Ruby monolith to a brand-new microservice architecture."

**3 · Filevine (`filevine.com`).** 2026-01-06.

> "ensure our migration from legacy systems is seamless"
> "work directly with our Lead Architect to replace a legacy system with a modern, scalable solution"

Note Filevine *also* carries "Migration Experience: ... is highly desirable", which is a candidate
requirement and does not qualify. It qualifies on the two first-person sentences above, not on that one.
Same posting, both classes — which is the argument for reading sentences rather than documents.

**4 · Blvd (`joinblvd.com`).** 2025-11-07. Duties bullet, per the Cover Genius precedent.

> "Modernize legacy monolithic applications using modern architectures such as domain-driven design,
> event-driven design, clean architecture, and CQRS"

**5 · PCMI (`pcmicorp.com`).** 2026-06-30. Thinnest of the five — first person, but no named estate and no
database.

> "we're modernizing our architecture, embedding AI across our products, and scaling to meet growing demand"

---

## 3 · Seven false positives, and they form a taxonomy

Worth keeping as a test set — each is a distinct failure class, not seven of the same one.

| domain | matched text | class |
|---|---|---|
| dutchie.com | "decouple and modularize the e-commerce **front-end**" | wrong layer — front-end |
| jobnimbus.com | "Experience migrating from monolithic to **micro frontend**" | requirement AND front-end |
| emburse.com | "Our platform helps organizations **modernize** financial operations" | the product's value proposition, not their estate |
| arbitersports.com | "**modernize** critical school and district workflows" | customer-facing product work |
| socure.com | "**Decompose** complex projects into clear, actionable tasks" | project decomposition, not system — the Chainlink-"oracle" class |
| mykaarma.com | ElasticSearch "**shard** allocation strategies" ×3 | search index, not the transaction estate; 2 of 3 from a scripted Q&A in the body |
| fireblocks.com / roller.software / rechargepayments.com | "reducing **technical debt**" in a generic improvement list | boilerplate |

The `emburse` and `arbitersports` class is new and it matters: **a company whose product modernizes other
people's systems will match every estate term while having no estate pain of its own.** Any account whose
own marketing uses our vocabulary needs the first-person test applied before the term list.

---

## 4 · MongoDB: one real hit, three requirements

**`MDB●` mykaarma.com** — 2026-03-25, first person, production:

> "we already have a robust foundation in MySQL, MariaDB, and MongoDB"

Fireblocks ("Advantages - Knowledge of ... MongoDB"), Kyriba ("Nice To Have - MongoDB experience") and
DealerSocket ("expertise in multiple database platforms, including ... MongoDB") are all candidate
requirements. Marked `MDB?`, not `MDB●`, per your item 5.

Note mykaarma fails EST (wrong layer) and passes MDB. They are independent signals and this cohort shows it.

---

## 5 · Measured term prevalence — two of the nine pinned terms are dead

Across 441 postings, share of postings containing each term:

| term | prevalence | genuine estate hits |
|---|---|---|
| `migrat*` | 23.4% | ~4 |
| `legacy` | 9.3% | 4 |
| `moderni[sz]*` | 8.4% | 3 |
| `monolith*` | **3.6%** | **5** |
| `technical debt` | 2.0% | 0 |
| `shard*` | 0.7% | 0 |
| `decompos*` | 0.2% | 0 |
| `re-architect*` | **0.0%** | 0 |
| `replatform*` | **0.0%** | 0 |

`monolith*` is the highest-precision term in the list — lowest prevalence, most genuine hits. `migrat*` is
the noisiest that still works. `technical debt`, `shard*` and `decompos*` produced only false positives here.
`re-architect*` and `replatform*` returned **zero matches in 441 postings** — they are dead weight in the
term list and the slots could go to `coexist`, `strangler`, `cutover`, `end-of-life`, `unsupported version`.

Recommend routing this table to workstream 3 as measurement rather than opinion.

---

## 6 · Answering your three asks

**a. The `⊗` mark — you are right, I was wrong.** Your legend is the operative one: `⊗` means measured
absent from a single source. An account with nothing inside the window was never measured. The probe's 4
zeros returned no postings at all, and I did not retrieve outside the window, so I cannot distinguish
"no postings ever" from "postings that predate the window". The correct mark is **`EST?`** for all four.

**b. The 10 probe domains with posting counts,** all inside the 12-month window, none inside 90 days:

| domain | infra postings 12m | newest | days old | mark |
|---|---|---|---|---|
| integral.com | 2 | 2026-06-02 | 94 | `EST○` / `HIR○` |
| mews.com | 2 | 2026-02-04 | 212 | `EST○` / `HIR○` |
| order.co | 1 | 2026-05-27 | 100 | `EST○` / `HIR○` |
| turno.com | 1 | 2025-12-15 | 263 | **`EST●`** / `HIR○` |
| vagaro.com | 1 | 2025-11-07 | 301 | `EST○` / `HIR○` |
| everymatrix.com | 1 | 2025-10-08 | 331 | `EST○` / `HIR○` |
| ottimate.com | 0 | — | — | `EST?` / `HIR?` |
| zuper.co | 0 | — | — | `EST?` / `HIR?` |
| passportinc.com | 0 | — | — | `EST?` / `HIR?` |
| tryotter.com | 0 | — | — | `EST?` / `HIR?` |

Caveat carried forward from §0: these counts come from the under-retrieving query. Treat the six `EST○` as
provisional — the retrieval that produced them found 0.8 postings per domain where a wider one found 9.6.
**Turno** is the one solid result: *"migrating our Integrations and Payments rails ... onto a modern
TypeScript platform on GCP"*, 2025-12-15, both `migrat*` and `moderni*`, estate layer unnamed.

**c. MRG provenance, acknowledged.** You are right that it is firmographic — `Ownership Type` / `Latest
Round` — so the 35 ceiling does not collapse to 15 for the reason I proposed. Withdrawn. Your point that
MRG 20 needs a real margin event rather than a funding stage stands on its own and the 17 unsupported
`MRG◐` check is the item that actually moves Tier 1.

---

## 7 · Cost: I was off by roughly 8×

Estimated 40–60 credits, quoting the probe's density. The pull returned 452 rows. The error is the same one
as §0: I priced off a query and then widened it. Rule going forward — **price the query you are about to run,
on a probe of that exact query, or don't quote a number.**

Two real cost facts, both measured:
- Price tracks rows returned, including `NO MATCHING POSTINGS` rows. 12 credits for the 12-row probe.
- Posting density varies 12× with the role filter on the same population. Density is a property of the
  query, not of the accounts.

---

## 8 · On the fabricated quotation

Noted, and it does not need re-litigating — check 8 caught it, you disclosed it unprompted and corrected
three files with real accounts instead of a paraphrase. Worth recording that the two errors in this exchange
are the same error: a claim asserted at higher confidence than its retrieval supported. Yours was a sentence
that existed only in the write-up; mine was an absence that existed only in a thin query. The defence in both
cases is the same discipline you built into the schema — every mark carries the path that produced it.
