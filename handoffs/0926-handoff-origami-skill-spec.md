# Handoff — Skill spec: `origami-sourcing`

**Owner:** Rudra · **Written:** 3 September 2026 · **Purpose:** input to `skill-creator` in a fresh chat
**Siblings:** `handoffs/0926-handoff-origami-sourcing.md` (operations) · `handoffs/0926-handoff-gtm-execution.md` (accounts)

---

## 0. Why this is a separate document

The operations handoff answers *"what do I do next with Origami."* This answers *"what should a skill do every time."* They need different shapes:

| Operations handoff | This spec |
|---|---|
| Current state, open decisions, credit budget | Trigger conditions, procedure, output contract |
| Narrative — what happened and why | Rules — what must always hold |
| Goes stale as soon as the next run lands | Stays true across runs |

Folding the second into the first makes the handoff worse at both jobs: a fresh operator has to read past skill-authoring material to find the next action, and a skill author has to reverse-engineer rules out of a narrative. **Recommendation: keep them separate, and open the skill-creation chat with this doc plus `0926-origami-prompt-log.md`.**

**Everything this spec needs is committed.** No CSV re-attachment, no reference back to the originating chat.

| File | What it is |
|---|---|
| `handoffs/0926-origami-prompt-log.md` | All 14 verbatim prompts written to Origami, in order, annotated with what each fixed and whether it worked |
| `marketing/outbound/research/data/0926-origami-companies.csv` | 120 unique companies, all fact columns merged across 8 pulls, with provenance and a `Field Conflicts` column |
| `marketing/outbound/research/data/0926-origami-job-postings.csv` | 36 job-posting rows with full descriptions, so any role-match claim can be re-audited from source |
| `marketing/outbound/research/0926-m2-pursuit-order-snapshot.md` | The 32 qualified accounts with gate evidence |

---

## 1. What the skill is

**Name:** `origami-sourcing`

**Description (drives triggering — keep it concrete):**
> Write and audit origami.chat sourcing prompts for a named ICP. Use when sourcing target accounts, building a prospect list, running a trigger search, or evaluating a CSV that Origami returned. Enforces trigger-first search, facts-only output, and the credit budget.

**Trigger phrases to cover:** "source accounts for [ICP]", "write an Origami prompt", "run a trigger search", "here's the CSV Origami gave me", "build a target list", "look-alike search", "how many credits will this cost".

**Explicitly out of scope:** scoring, tiering, cohort assignment, messaging. Those belong to `lead-scoring` and `abm-campaign`. The skill hands over facts and stops.

---

## 2. The one idea the skill exists to enforce

**Origami retrieves facts well and judges badly. Take the facts; do the judgment yourself.**

This is not a hunch. It is measured across the 8 pulls, and the evidence is in `0926-origami-companies.csv`:

> **Of the 65 companies that appeared in more than one pull, 60 had a derived-judgment field contradict itself between runs. Only 5 had any factual field conflict — and 3 of those were cosmetic** (`500` vs `495` employees, `411000000` vs `409000000` funding, `series_e` vs `SERIES_E`).

Contradictions by field:

| Field | Kind | Companies contradicted |
|---|---|---|
| `Transaction Evidence Review` | derived | **60** |
| `Transaction Volume` | derived | 7 |
| `Matching Posting Count` | factual-looking, definition unstable | 4 |
| `Database Technology Mentions` | extraction | 2 |
| `Engineering Location` | factual | 2 |
| `Employee Count` / `Total Funding` / `Funding Stage` | factual | 1 each, all cosmetic |

Same company, same source text, different run, opposite verdict. `Carta` came back `NO_EVIDENCE`, then `VERIFIED PER-PERIOD`, then `NO EVIDENCE` again.

**Rule the skill must enforce:** never request, and never accept, a column where Origami has decided something. Request the underlying text and decide locally.

---

## 3. Procedure the skill should run

### Step A — Establish the shape before spending anything

Reasoning, filtering and export are free; only data retrieval costs. So iterate on the prompt for free until the shape is settled, then pull once.

Ask the operator, or infer from the ICP:
1. Which ICP, and which single trigger? (One ICP × one trigger × one offer — separate triggers get separate searches, because they draw from separate universes and **add** rather than intersect.)
2. Sample or census?
3. Credit ceiling for this pull.

### Step B — Compose the prompt from the working template

`P10` in the prompt log is the template that worked. Its skeleton:

```
STEP 1 — SEARCH ON THE TRIGGER.       (the observable event, 90-day window)
STEP 2 — NARROW BY ICP FIT.           (gates + hard exclusions)
STEP 3 — SPLIT THE OUTPUT ON <SIGNAL>. (verbatim quotes, grouped)
STEP 4 — RETURN FACTS ONLY.           (named columns, then the refusals)
```

Step 4 must end with an explicit refusal list. The line that made the difference:

> *No transaction-volume column, no screening flags, no derived scores.*

And must request the denominator:

> *Report the trigger population before narrowing and the qualified count after, split by headcount band.*

### Step C — Apply the standing constraints

Every prompt, no exceptions:

1. **Trigger first, firmographics second.** Intent is 30 of 100 points in WeKan's scoring model; a firmographic-first search scores zero on it by construction.
2. **A blank field is UNKNOWN, not FAIL.** State it in the prompt. Unknowns go to a review bucket.
3. **Facts only.** No fit scores, evidence classifications, pass/fail screens, or public-status determinations.
4. **Never sort on the dimension you cap.** Band and stratify instead.
5. **Do not gate on revenue** (0% coverage in two of three runs, 37% in the third) **or transaction volume** (unverifiable).
6. **Require an exclusion reason per excluded row**, and ask for the excluded rows as a file, not a count.
7. **Reset context explicitly** when changing search shape — Origami carries state between runs.
8. **Pause after the first sample** when running a multi-stage plan, so a correction costs one sample rather than the whole pull.
9. **Ignore Fit Score.** It is a platform default, not a data defect, and prompting against it wastes instructions.
10. **Close every prompt with the refusal clause:** *"If anything above cannot be established without a further retrieval, say so rather than estimating."* This is the highest-yield single line in the corpus. It turned the same tool that once marked 21 companies "verified" with no supporting text into one that returned a clean, itemised "I cannot determine this" — and that answer retired a bad signal for zero credits.
11. **Require scope with every count.** Any per-company count must arrive with its role scope, domain scope and deduplication method. A count missing any of the three is UNKNOWN, not a number, and the scope cannot be recovered after the fact.

### Step D — Audit the returned CSV before anyone uses it

The skill should run this checklist and report failures, not just hand the file on:

| Check | Why |
|---|---|
| Do the row values cluster at a cap boundary? | The sort-under-cap failure — happened three times |
| Coverage per column: what % non-blank? | Revenue came back 0% twice. A gate on a sparse column silently drops good accounts |
| Does any row's verdict contradict its own fact columns? | FreedomPay was marked undecided on funding while its own `Ownership Type = PE-owned` resolved the branch |
| Spot-check every `Role Match = true` against the job description | Two of four "qualified" postings in the corrected sample were frontend roles |
| Magnitude-check any volume figure against headcount | FarEye's "100M transactions/day" at 598 employees ≈ 36B/year |
| Re-run overlap: does any company's derived field disagree with a previous pull? | 60 of 65 did |
| Are excluded rows accounted for, and is any exclusion driven by a blank field? | The audit that cleared this was the single most reassuring result of the trial |

### Step E — Hand over

Account names plus sourced fact columns. No tiers, no scores, no cohorts.

---

## 4. Failure catalogue — use these as the skill's worked examples

Each is real, each is reproducible from the committed data.

**1 · Sort-under-cap.** Sorting headcount-descending with a 60-result cap returns 60 companies pinned at the ceiling. Occurred in pulls 2 and 3; `P2` in the prompt log raised the ceiling and it recurred, which is the proof that banding — not a bigger cap — is the fix.

**2 · Blank read as FAIL.** A blank `Company Screen` collapsed 59 of 60 accounts to one qualified. See `P7` in the prompt log for the correction, which works by naming three accounts whose own rows contradicted the verdict.

**3 · Classifier fabrication.** 20 of 21 rows marked "verified per-period volume" had no period phrase in the source. EliseAI's entire company description is one sentence containing no digits. Three attempts, three distinct failure modes: inverted labels → blank-field gating → fabrication.

**4 · Neutral title, wrong role.** Lighthouse's posting is titled *Lead Platform Engineer* and was marked `Role Match = true`. Its description names **Ember, React, TypeScript and Frontend** — it is a front-end platform role. Verifiable in `0926-origami-job-postings.csv`. **Never accept a role match on the title alone.**

**5 · Keyword match in the wrong sense.** Chainlink Labs came back with `Database Technology Mentions = oracle`. Chainlink is a blockchain **oracle** network; the word has nothing to do with Oracle Database. A technographic gate on that string would have put a crypto oracle provider on an Oracle-migration list. **Require the verbatim sentence, not the extracted term.**

**6 · A defined column can still be unusable — and the tool may not know it.** `Matching Posting Count` had a clean definition, supplied on request. It still failed twice over. **Across pulls it changed meaning** (Alan 15,398 → 396, Kraken 1,231 → 10, Lighthouse 1,119 → 9, FreedomPay 393 → 3). **And within a pull the values failed a magnitude check** — per 100 employees: FreedomPay 0.5, Kraken 0.5, Lighthouse 0.7, Chainlink 9.7, Alan 25.7. Pressed on it, Origami could confirm the role list but **could not establish domain scope or deduplication**, because only an aggregate was ever stored; it then called its own values unverified aggregates and declined to estimate. **The column was unrepairable, not merely unverified.** Lesson for the skill: a definition is necessary and not sufficient; normalise every count against a denominator you trust, and require role scope, domain scope and deduplication method *at retrieval time*, because they cannot be recovered afterwards.

**7 · Name collision.** "Kraken" in the SRE sample is Kraken Technologies (kraken.tech, energy, founded 2019), not the crypto exchange. Resolve on domain, never on name.

**8 · Wrong-shape entities leaking through.** Infrastructure vendors and public companies recurred across runs (ACV Auctions, Angi, Temporal, WEKA, Tines). Exclusions must be named categorically in the prompt and reported with reasons.

---

## 5. Costs the skill must know

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

The skill should quote an estimate before any pull and refuse to run one that exceeds the stated ceiling without confirmation.

**Sample-size guidance to encode:** a 30-posting sample gave a qualify rate of ~7% with a confidence interval of roughly 1%–22% — useless for a decision. A 300-posting sample costs 300 credits and narrows it to about ±3 points. When a sample has to settle a threshold question, size it against the decision, not against the budget.

---

## 6. Evaluation cases for `skill-creator`

Should trigger:
- "Write me an Origami prompt to find insurtech companies hiring SREs"
- "Here's the CSV Origami returned — does it look right?"
- "How many credits for a 200-company tech-stack enrichment?"
- "Run a look-alike search on our 32 qualified accounts"

Should NOT trigger:
- "Score these accounts" → `lead-scoring`
- "Write the first email for Alan" → `outreach-emails`
- "Who should we target?" → `icp-research`

Behaviours to assert:
- Given an ICP and a trigger, produces a four-step prompt whose Step 4 contains an explicit refusal list.
- Given a CSV with a column at 0% coverage, flags it rather than gating on it.
- Given a row where a verdict contradicts its own fact columns, reports the contradiction.
- Given a request to gate on transaction volume, refuses and explains why.
- Never emits a tier, score or cohort.

---

## 7. Open question for Rudra before authoring

The trial ran entirely against ICP-M2. The gate vocabulary in the working template (founded year, headcount band, funding-or-PE, private status, geography, digital-native qualifier) is M2-shaped.

**Should the skill be ICP-generic — reading gates from `marketing/icp/ICP.md` for whichever ICP is named — or M2-specific for now and generalised once a second ICP has been sourced?**

Generic is the better long-term shape and is what `ICP.md` now supports, since all six ICPs are in it with their triggers and disqualifiers. The risk is encoding a general procedure from a single worked example. My read: **build it generic, but ship it with the M2 run as the only worked example, and mark the other five ICPs untested.** That is honest about the evidence and still usable on day one.
