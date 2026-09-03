# Handoff — Workstream 2: GTM execution on the qualified 32

**Owner:** Rudra · **Written:** 2 September 2026 · **Scope:** the marketing repo, its skills and agents, applied to accounts already sourced
**Companion handoffs:** `handoffs/0926-handoff-origami-sourcing.md` (workstream 1 — sourcing) · `handoffs/0926-handoff-origami-skill-spec.md` (workstream 3 — authoring the `origami-sourcing` skill)

---

## 0. What this chat is for

Turning 32 qualified ICP-M2 accounts into sequenced, on-brand outbound using the skills and agents in the `claude-code-marketing-quickstart` repo.

**In scope:** ABM plans · outreach copy · scoring and tiering · messaging and positioning work · repo file maintenance · the skills and agents themselves.

**Out of scope — belongs to workstream 1:** Origami prompts, CSV evaluation, credit spend, the volume-vs-ABM population test. If this chat needs more accounts or tech-stack data, it writes a request and hands it over.

**Mode:** Mode 3 (Centaur) for strategy and scoring. Anything with a client name or a metric in it drops to **Mode 2 at most** — see §3.

---

## 1. The repo

**Path on Rudra's machine:** `C:\Users\c4mun\Documents\GitHub Repos\claude-code-marketing-quickstart`

Governed by nested `CLAUDE.md` files — one at root, one per folder. Read the folder's `CLAUDE.md` before writing into it. `pulse-analytics-example/` is a worked example, not WeKan data; never read it as fact.

### Read these first, in this order

1. `marketing/rules/escalation.md` — what you may do autonomously and what you may not. Non-negotiable.
2. `marketing/brand/brand-voice.md` — especially **§0, the proof firewall**.
3. `marketing/company/company.md` — canonical facts and numbers. Wins over anything in `positioning/`.
4. `marketing/icp/ICP.md` — the scoring framework and all six ICPs.
5. `marketing/messaging/messaging.md` — §6 is the approved proof-point pool, §7 the words-to-avoid list.
6. `marketing/latest.md` — most recent entry is 2026-09-02 at the top, covering all the work below.

### Skills and agents available

**Agents:** `context-refresh` · `gtm-engineer` · `product-marketer` · `content-marketer` · `aeo-specialist`
**Skills most relevant here:** `abm-campaign` · `lead-scoring` · `outreach-emails` · `icp-research` · `funnel-strategy` · `product-messaging` · `positioning` · `tov-guidelines` · `brand-kit`

---

## 2. Canonical facts you will need constantly

From `company.md` — use these exact figures, do not round or revert to approximations:

- **100+ full-time engineers · 40+ enterprise clients · 160+ projects delivered · 50+ studio startups co-built**
- One of only **SIX** boutique MongoDB systems-integrator partners globally (canonical = 6; correct any doc saying "five")
- **"MongoDB-native but not MongoDB-limited"** — frame the MongoDB investment as a mark of trust and technical depth, never as the boundary of what WeKan does
- Three engines: **Evolve** (transform & modernize) → **Helix** (build & engineer) → **NitroStack** (operationalize intelligence)
- **"Build Mode" is retired.** It is on the words-to-avoid list; Helix is the external name.
- Modernization speed: **~50% faster** is the standard claim; 60% only as a stated best case
- Live wedge worth leading with: **Realm end-of-life modernization**

From `messaging.md` §7, avoid: "database modernization partner" · "staff augmentation" · MongoDB-only framing · "Build Mode".

---

## 3. Hard guardrails — read before writing any asset

### The proof firewall (`brand-voice.md` §0)

> **Client names and performance metrics must NEVER appear together, in any asset.**

- **Pool A** = client names only, no metrics.
- **Pool B** = metrics anonymised by industry (`messaging.md` §6).

> *"Adding a named customer is a human act. If WeKan wants to name a customer against an outcome, Rudra adds those details himself after clearing them. No skill or agent ever proposes the pairing, infers it, or asks for permission to make it."*

Note the last clause: an agent must not even *ask*. Do not surface a name-plus-metric pairing as a question. (This was over-read once in the prior session — internal working docs and discussion may name clients freely; the firewall governs *assets*.)

### From `escalation.md`

| Work | Rule |
|---|---|
| Cold email sequences, social posts, website copy, blog | **Escalate always** |
| Any asset containing a client name | **Hard stop. Never autonomous.** |
| Any metric not in `messaging.md` §6 or `company.md` | **Hard stop** |
| Overwriting a canonical file (`ICP.md`, `positioning.md`, `messaging.md`, `company.md`, `brand-*.md`) | **Escalate always** |
| Research and strategy files | Autonomous |
| Buying-committee names | **Public sources only. No scraped personal contact data.** |

---

## 4. What has already been written

| File | State |
|---|---|
| `marketing/icp/ICP.md` | **Replaced** the 57-line draft skeleton with 196 lines from `WeKan_Consulting_Practice_ICPs.docx`. Backup at `ICP.draft-skeleton.bak`. Rudra confirmed: "ICP.md looks good." |
| `.claude/skills/lead-scoring/SKILL.md` | **Model B added** for ICP-M2 alongside relabelled Model A (M1). Backup at `SKILL.md.bak`. Also added the M2 anti-ICP hard filter, the "blank = UNKNOWN not FAIL" rule, the "never accept a derived judgment column" rule, and real Origami call costs. |
| `marketing/outbound/research/0926-target-accounts.md` | Canonical scored output. 14,889 bytes / 153 lines. Scoring model, calibration note, model-vs-hand-ranking disagreements, evidence key, three tier tables, entry point, disqualified section, open items. |
| `marketing/outbound/research/0926-m2-pursuit-order-snapshot.md` | Full per-account snapshot derived from the Pursuit Order artifact — gate evidence, near misses, removed-with-reasons. Committed so the artifact's content survives session loss. |
| `marketing/outbound/strategy/0926-abm-alan.md` | 105 lines. Sources, trigger, buying committee, 5 beliefs, entry point, touch plan, assets, disqualifiers. **Belief 5 marked `[UNAVAILABLE]` and escalated** — see §7. |
| `marketing/outbound/strategy/0926-abm-owner-com.md` | 112 lines. Same structure, plus a dedicated section on the MongoDB conflict-of-interest objection. |
| `marketing/latest.md` | New 2026-09-02 entry at the top (line 10) documenting all of the above and the escalation. |

**Source data, committed — nothing needs re-attaching:**

| Path | What it is |
|---|---|
| `marketing/outbound/research/data/0926-origami-companies.csv` | All 120 screened companies with merged fact columns, provenance, and a `Field Conflicts` column |
| `marketing/outbound/research/data/0926-origami-job-postings.csv` | 36 job-posting rows with full descriptions — the evidence behind every HIR gate |
| `handoffs/0926-origami-prompt-log.md` | The 14 verbatim Origami prompts |
| `handoffs/0926-handoff-origami-skill-spec.md` | Skill spec for `origami-sourcing` (workstream 3) |

**Published artifacts** — living deliverables, republish to the same URL:
- **ICP-M2 Pursuit Order** — `claude.ai/code/artifact/aefe4ddd-5bfe-4920-bae3-57dde74a158d`
- **What the M2 Sourcing Trial Bought** (exec brief for Rudra's boss) — `claude.ai/code/artifact/19952fa8-f0dc-4472-b449-409e53d61ea3`

> **Mechanics:** the session scratchpad that held the HTML sources is gone. To edit either artifact, first `Artifact action:"read"` its URL to recover the live version, then republish to the same URL. Publishing without the `url` creates a second artifact instead of updating.

---

## 5. Model B — the ICP-M2 scoring model

**Gates:** VER (industry) · AGE (founded ≤2018) · SCL (late-stage / PE scale) · VOL (company-side per-period transaction volume) · EST (named estate or DB pain) · MRG (margin-scrutiny trigger) · HIR (live infra hiring) · ACC (production access grantable)

**Weights:** EST 25 · MRG 20 · HIR 15 · MongoDB signal 15 · VOL 10 · AGE 10 · SCL 5 · **anti-ICP −40**
**Tiers:** T1 ≥75 · T2 50–74 · T3 <50

### Calibration note — read this before trusting a score

The first pass applied the −40 anti-ICP penalty to a **predicted** production-access difficulty. That crashed Signifyd from rank 1 to Tier 3 on an inference rather than a fact.

**Corrected rule:** anti-ICP fires **only** on a structural exclusion (infrastructure vendor, public company, wrong vertical, holding company) or a **confirmed** access refusal. Predicted access difficulty is a *flag*, not a penalty. Signifyd restored to Tier 1 at 75. Pantheon stays at −40 — it is a managed-PaaS vendor, a structural exclusion.

### Two open disagreements between the model and hand ranking

Recorded, not resolved. Both are informative.

- **Close: model 80 (T1) vs hand rank 29.** The model rewards a clean estate signal; the hand ranking discounted Close on scale. One of the two is wrong, and the model is at least legible.
- **Alan: model 65 (T2) vs hand rank 4.** **Closed 3 September. The model was right; the hand ranking was leaning on a number that does not exist.** Alan's apparent strength was trigger density — 396 matching infrastructure postings vs FreedomPay's 3. Origami has since confirmed it cannot establish the domain scope or the deduplication method behind those counts: they are unverified aggregates, and the breakdown was never stored, so they cannot be repaired. **`Matching Posting Count` is UNKNOWN for all 32 accounts and is struck from Model B inputs.** HIR stays at 15. Alan stays Tier 2 on its gate evidence — which is independently sound: a real posting held in `data/0926-origami-job-postings.csv`, *Senior Platform Engineer, Data Retention & Privacy*, PostgreSQL named in the body.

---

## 6. The roster — 32 accounts

| # | Account | Score | Tier | Cohort / motion | Industry |
|---|---|---|---|---|---|
| 1 | Sensor Tower | 92 | T1 | B · sponsor mandate | Vertical SaaS · digital intel |
| 2 | Owner.com | 85 | T1 | A · hiring trigger | Marketplace · restaurant |
| 3 | Close | 80 | T1 | A · hiring trigger | Vertical SaaS · CRM |
| 4 | Signifyd | 75 | T1 | A · hiring trigger | Fintech · payments |
| 5 | Alan | 65 | T2 | A · hiring trigger | Insurtech |
| 6 | Metropolis Technologies | 52 | T2 | B · post-acquisition integration | Mobility · payments |
| 7 | NexHealth | 52 | T2 | A · hiring trigger | Vertical SaaS · health |
| 8 | FreedomPay | 50 | T2 | B · sponsor mandate | Fintech · payments |
| 9 | Pushpay | 45 | T3 | B · sponsor mandate | Payments |
| 10 | Zuora | 45 | T3 | C · re-score as M1 | Subscription billing |
| 11 | iCapital | 45 | T3 | C · re-score as M1 | Fintech · alternatives |
| 12 | Cambridge Mobile Telematics | 40 | T3 | B · sponsor mandate | Insurtech |
| 13 | Carta | 40 | T3 | E · efficiency reset | Fintech · private markets |
| 14 | Workrise (RigUp) | 40 | T3 | E · efficiency mandate | Energy marketplace |
| 15 | Zūm | 40 | T3 | B · sponsor mandate | Student transportation |
| 16 | Civitatis | 35 | T3 | B · sponsor mandate | Travel tech · marketplace |
| 17 | Fleetio | 35 | T3 | D · watchlist | Fleet · logistics-adjacent |
| 18 | Housecall Pro | 35 | T3 | D · watchlist | Vertical SaaS · home services |
| 19 | ID.me | 35 | T3 | D · watchlist | Identity · fintech-adjacent |
| 20 | **Pantheon** | 35 | T3 | **Suppression check first** | Managed PaaS |
| 21 | Wallapop | 35 | T3 | D · watchlist | Marketplace |
| 22 | Weee! | 35 | T3 | D · watchlist | Grocery delivery · marketplace |
| 23 | Zeta | 35 | T3 | D · watchlist | Fintech · issuer processing |
| 24 | ezCater | 35 | T3 | D · watchlist | Food marketplace |
| 25 | Back Market | 30 | T3 | D · watchlist | Marketplace |
| 26 | Blockchain.com | 30 | T3 | D · watchlist | Fintech · exchange |
| 27 | Cover Genius | 30 | T3 | D · watchlist | Insurtech · embedded |
| 28 | Engine (Hotel Engine) | 30 | T3 | D · watchlist | Travel tech |
| 29 | Netradyne | 30 | T3 | D · watchlist | Fleet safety · vision |
| 30 | Sure | 30 | T3 | D · watchlist | Insurtech |
| 31 | Lighthouse | 20 | T3 | D · watchlist | Travel tech · hospitality |
| 32 | FarEye | 15 | T3 | D · watchlist | Logistics & delivery |

**Cohort key** (per the one ICP × one trigger × one offer rule — accounts split by *what put them in-market*, not by attractiveness). Every account carries the same entry offer: **the fixed-fee 2-week estate assessment.**

- **A · hiring** → C1, email-led to CTO. The only cohort matching C1 as approved.
- **B · sponsor** → C3 pattern: LinkedIn-led, human-approved first touch, CFO savings framing.
- **C · reclassify** → ICP-M1 shaped. Route to the existing C3 estate-triggers track.
- **D · watchlist** → not a sequence. Monitor for a trigger; promote into A or B when one fires.
- **E · efficiency** → assessment with a margin-story framing.

**Cohort D being the largest group is the finding, restated:** most accounts that fit the profile are not in-market today. Hold and watch, do not email.

**FarEye caveat:** demoted to T3 after a magnitude check. Its claimed 100M transactions/day against 598 employees works out to ~36B/year — implausible. Origami also flagged it. Do not restore without a verified figure.

---

## 7. The escalation that wasn't — resolved 3 September

**This section is kept as a record of a mistake, because the mistake is instructive.**

I escalated to Rudra that `messaging.md` §6 had no proof point for *"delivering an assessment under restricted production-data access,"* marked belief 5 of the Alan plan `[UNAVAILABLE]`, and said four accounts were blocked on it.

**The premise was wrong.** WeKan's motion is: intro call → one or two follow-ups → production access if we're in. Nobody expects access on a first call and WeKan does not ask for it. Between those steps the pre-sales solutions architect, chief architect and CEO gather whatever technical detail the prospect is willing to share and come back with what could be done and in what timeframe. There was never a gap in the proof library — there was a gap in my model of the sales motion.

**How it was fixed.** Belief 5 in `0926-abm-alan.md` is now *"Finding out what this would take costs me one call, and I stay in control of what I share,"* proved by the staged discovery path itself plus the existing Pool B insurance proof point. Nothing new was needed. The disqualifier in both plans was also re-worded: refusing access *after* the technical working session is the disqualifier; declining it early is normal.

**The lesson, worth carrying into the other workstreams.** The guardrail worked exactly as designed — it stopped an invented proof point from being written. But a guardrail firing is not the same as a real gap. Before escalating a missing proof point, check whether the belief it supports is one the buyer would actually hold at that stage of the motion. Escalating a non-problem costs a day and a decision-maker's attention.

## 8. Open work, in order

1. ~~Resolve §7.~~ **Done 3 September — it was a false alarm.** Both ABM plans are unblocked and carry no `[UNAVAILABLE]` markers.
2. **Run `context-refresh`.** Item 5 of the original five-point plan, never executed. It re-reads the canonical files and flags what the last two days made stale.
3. **Pantheon suppression / competitor check.** Managed PaaS — likely a competitor, not a prospect. Resolve before it appears in any list that leaves the building.
4. ~~Reconcile the count discrepancies.~~ **Done 2 September.** Canonical figures: **120 companies screened · 32 qualified · 8 Origami pulls · 17 CSVs · 400 credits.** The 120 is a clean domain dedupe across all 17 source files and supersedes the earlier 119 and 124. Exec brief republished with corrected tally and cohort table; `latest.md` corrected. Use these numbers in any asset.
5. **ABM plans for Sensor Tower and Close** — the two remaining Tier 1s without one.
6. **Re-score Zuora and iCapital as ICP-M1** (Cohort C) rather than leaving them in an M2 list at T3.
7. **Two verifications:** Owner.com's founding year (sits on the 2018 boundary; affects AGE) and Signifyd's two-vintage figures.
8. **Add both handoffs and `0926-target-accounts.md` to the Claude project by hand.** `project_write` returns HTTP 403 in this environment; reads work fine.

---

## 9. Interface with workstream 1

**Requests to send that way:**
- `Enrich Tech Stack` on the 32 (~80 credits) — converts the MongoDB gate from inference to data.
- The `Matching Posting Count` column query — settles whether HIR is underweighted in Model B (§5).
- The 300-posting sample result, which determines whether Cohort A runs as volume email or stays ABM.

**Accept from that way:** account names plus sourced fact columns only. Scoring, tiering and cohort assignment happen here, against Model B — never accept a tier or fit score computed by the sourcing tool.

---

## 10. Two process notes worth keeping

- **The `.md` companion drifted two revisions behind the artifact.** The fix was a Python parser that reads the artifact HTML and regenerates the markdown, so the two cannot diverge. That script lived in the session scratchpad and is gone — if the companion needs regenerating, rewrite it rather than hand-editing both.
- **Running the model found an error reading it never would have.** Model B's anti-ICP bug (§5) only surfaced when scores were actually computed and Signifyd came out wrong. Compute before trusting.
