# ABM plan — Alan (alan.com)

*Written 2026-09-02 by `/abm-campaign`. Reads `../research/0926-target-accounts.md`, `../../icp/ICP.md` (ICP-M2), `../../positioning/positioning.md`, `../../messaging/messaging.md`, `../../company/company.md`.*

**ICP-M2 · Model B score 65 (Tier 2) · Cohort A, hiring trigger · Motion C1**

> **Proof firewall.** Every proof point below is drawn verbatim-in-substance from `messaging.md` §6 Pool B, anonymised by industry. No WeKan client is named anywhere in this plan or its assets.

---

## Account snapshot — what's true, with sources

| Fact | Source |
|---|---|
| Health insurance and prevention platform; France, Belgium, Spain, expanding to Canada | Own job posting, 2026-09-02 |
| Founded 2016 · Series F · $1.357B raised total | Origami SRE-trigger run |
| €800M+ ARR · 40,000+ companies · 1M+ members | Own job posting |
| 1,542 employees (Origami) vs "team of 800+" (own posting) | **Discrepancy — resolve before first touch.** Origami's figure may include contractors or be stale. |
| **Stack, self-disclosed: "Python/Flask/React and PostgreSQL at the core, in a monorepo we deploy daily."** Wider platform AWS/GCP, Kubernetes, Terraform, Datadog. | Own job posting — the single most valuable line in this file |
| Organised into "areas" with a Tech Foundations group and a Data Foundations crew inside it | Own job posting |
| Open role: Senior Platform Engineer — Data Retention & Privacy, hiring above level E | LinkedIn, posted 2026-09-02 |

**Why this account is unusual.** Almost every other account on the M2 list has an *inferred* estate. Alan published theirs. A ten-year-old licensed insurer running its full book on a single Postgres core inside a daily-deploy monorepo is the founding-era-architecture condition described in the ICP, stated by the target in its own words.

## Trigger — why now

Live infrastructure hiring: a senior platform role, posted within the 90-day window, owning a platform that "15+ areas and 1M+ members depend on." The posting says the platform "no longer depends on one person" is the goal — a stated single-point-of-failure in a system handling personal health data across three jurisdictions.

**Read the trigger honestly:** this is a *velocity and governance* trigger, not a margin trigger. Nothing public suggests Alan is under cost pressure. Model B scores it 65 rather than Tier 1 precisely because the margin-scrutiny signal is absent, and that shapes the entry framing below.

## Buying committee

| Role in the deal | Who | What they care about | Likely objection |
|---|---|---|---|
| Economic buyer | CTO or VP Engineering — **identify from public sources before first touch; do not guess** | Velocity, reliability, the infra line on the P&L | "We have 800 engineers. Why would we need you?" |
| Champion | Head of Tech Foundations / Data Foundations crew lead | Getting the platform off one person's shoulders; production-safe execution | "Will an outside partner actually understand our monorepo?" |
| Technical validator | Principal or staff engineer on Tech Foundations | Architecture credibility, no hand-waving | "Have you done this on a monorepo that deploys daily?" |
| Financial gatekeeper | CFO | Savings validated, not promised | Weakest lever here — there is no visible cost mandate |
| **Blocker — and the real one** | DPO / CISO | GDPR, data residency, member data | "You are not getting production access." |

Names are deliberately absent. `abm-campaign` guardrail: public sources only, no scraped contact data. Fill the committee from LinkedIn and their engineering blog before the first touch, not from inference.

## Belief shift — the beliefs, each with the proof that moves it

**1. "A daily-deploy monorepo on a single Postgres core is a scaling ceiling, not a virtue."**
They present the stack as a strength, and at their stage it was. The belief to move is that the same design that made them fast is what will slow them down next.
→ **Proof:** US homeowner's-insurance platform — 90% faster launch (2 weeks → 5 minutes), 3× query performance, 2× developer velocity. Same industry, same architectural starting point.

**2. "This can be done in production, at insurer scale, without downtime."**
→ **Proof:** global on-demand delivery platform — zero downtime; plus aggregate: zero regression during migration, 50,000+ database tables transformed, 10,000+ stored procedures modernized.

**3. "A modernization program is the on-ramp to what we want next, not a detour from it."**
Alan is visibly an AI-forward company. The belief to move is that the foundation work is the precondition, not a competing priority.
→ **Proof:** the arc — Evolve → Helix → NitroStack, one partner and one continuous context; and the US homeowner's-insurance platform raised $100M on the modernized platform, showing modernization as a growth enabler rather than a cost exercise.

**4. "WeKan is a senior partner, not a body shop."** The ICP is explicit that this buyer is "looking for a senior partner, not a body shop."
→ **Proof:** MongoDB strategic investor · one of six boutique systems-integrator partners globally · Fortune 500 delivery across NA, Europe and APAC · 40%+ of engineering on WeKan's own platform IP.

**5. "Finding out what this would take costs me one call, and I stay in control of what I share."**
The belief the deal turns on is not *"can you assess us blind"* — nobody grants an outsider production access on a first call, and WeKan does not ask for it. It is that the discovery path is staged and low-risk.
→ **Proof:** the path is intro call → technical working session with WeKan's pre-sales solutions architect and chief architect → production access only if both sides want to proceed. Between those steps the architects work from what Alan chooses to share — schema shape, stack, volumes, pain points — and come back with what could be done and in what timeframe. WeKan's CEO is in these conversations, which is itself the senior-partner signal belief 4 is making.
→ **Supporting proof (Pool B, anonymised):** the US homeowner's-insurance platform — 90% faster launch (2 weeks → 5 minutes), 2× developer velocity, 3× query performance. A regulated insurance estate, same shape as Alan's, no client named.

## Entry point

**Champion first, not the economic buyer.** Head of Tech Foundations or the Data Foundations lead, on the platform-single-point-of-failure framing their own posting supplies.

Rationale: at 800+ engineers a cold CTO approach reads as vendor noise, and the champion has the pain in writing. But the ICP's qualification checklist requires the CTO or VP Engineering engaged directly — so **the champion conversation exists to earn the CTO conversation, and the account does not qualify for the assessment until the CTO is in the room.**

**Pillar:** `messaging.md` §2 pillar 1 — *Modernize the foundation*. **Audience framing:** §5, VP Engineering / Platform — architecture-first, faster cycles, no lost context. Not the ROI framing; there is no cost mandate to attach it to.

## Touch plan

| # | Channel | Purpose | Asset needed | Owner |
|---|---|---|---|---|
| 1 | Email to champion | Name the single-point-of-failure they described, in their words. No pitch. | Sequence step 1 — `/outreach-emails` | Rudra (copy escalation) |
| 2 | LinkedIn connect, no message | Presence before the second email | — | Rudra |
| 3 | Email, +4 days | The velocity proof: same-industry monolith, launch time collapse | Sequence step 2 | Rudra |
| 4 | Email, +5 days | The offer: 2-week estate assessment, savings and velocity quantified against real workload data. Pre-empt the access objection by scoping to metrics, query plans and slow-query logs. | Sequence step 3 + one-page assessment scope | Rudra |
| 5 | Exit or route | No reply → Cohort D watchlist, re-enter on a new trigger. Reply → CTO introduction is the goal of the first call, not a proposal. | — | Rudra |

Three touches plus LinkedIn over roughly twelve days, per the C1 campaign spec. **`escalation.md`: cold email sequence drafted → Escalate, always.** No copy ships without Rudra's review.

## Assets to produce

| Asset | Skill | Status |
|---|---|---|
| 3-step email sequence, Alan-specific angle | `/outreach-emails` | Not started |
| Landing page for the M2 assessment offer | `/website-copy` | Not started — C1 spec calls for one landing page per ICP |
| "Provisioning debt" article for credibility ahead of touch 3 | `/aeo-content` | Optional |
| Prospect deck, if it reaches a first call | `wekan-client-deck` | On demand |
| Staged-discovery framing for belief 5 | Written into this plan | Resolved 3 Sep — no new proof point needed |

## Disqualifiers — what tells us to stop

- Production access refused outright **after the technical working session** — i.e. they will not grant it at any point, not merely not on call one. That is the explicit ICP-M2 disqualifier. Declining access early is normal and is not a disqualifier.
- No CTO or VP Engineering engagement after the champion conversation — the ICP requires a short chain to the economic buyer.
- They want a contractor to fill the open role rather than a partner to run a program. That is staff augmentation, on the global negative-ICP list.
- Estate turns out to be smaller than the ARR implies and identified savings cannot fund the engagement.

## Open items

1. Resolve the 1,542 vs 800+ headcount discrepancy.
2. Identify the CTO / VP Engineering and Tech Foundations lead from public sources.
3. ~~Escalate belief 5.~~ Resolved 3 Sep — the premise was wrong, not the proof library. See belief 5.
4. Run Origami Enrich Tech Stack (2.5 credits) to confirm whether anything beyond Postgres sits in the estate.
