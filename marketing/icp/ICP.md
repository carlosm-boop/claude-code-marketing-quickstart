# WeKan.AI — Ideal Customer Profiles (CANONICAL)

*Replaced 2026-09-02. Source: `WeKan_Consulting_Practice_ICPs.docx` (August 2026, sales-ops-ready). This supersedes the DRAFT SKELETON seeded 2026-08-31, which was inference from `company.md` + `positioning.md` and is preserved at `ICP.draft-skeleton.bak`. This file is research-grade: firmographics, buying committees, triggers, disqualifiers and proof points come from the source document, not from inference.*

**Scope:** NA + Europe primary, APAC/India secondary. Six ICPs across three offerings.
**Refresh cadence:** quarterly, or on a positioning change.

> **Proof firewall applies to everything downstream of this file.** Proof points below are anonymised by industry. Named client/metric pairings (HoneyQuote / SNCF / Amadeus) are retired per `../brand/brand-voice.md` §0. No skill or agent assembles that pairing.

---

## The qualification framework

An ideal customer is scored on three axes: **Fit** (firmographic + technographic), **Intent** (trigger signals putting them in-market now), **Accessibility** (relationship, MongoDB/hyperscaler channel, investor network, NitroStack community).

| Dimension | Points | Breakdown |
|---|---|---|
| Fit | 40 | industry 10 · size 10 · technographic 15 · geo 5 |
| **Intent** | **30** | **active trigger ≤90d 15** · density 10 · engagement 5 |
| Accessibility | 15 | relationship 10 · channel 5 |
| Economics | 15 | deal value 10 · multi-offering 5 |

**Tier 1 = 75+** (named-account ABM) · **Tier 2 = 50–74** (persona sequences, signal monitoring) · **Tier 3 = <50** (nurture). **Disqualifiers override any score.**

Best accounts qualify for 2+ ICPs — "one partner, one continuous context" is a qualification lens, not just positioning.

**Sourcing implication:** Intent is 30 of 100 points. Firmographic-first sourcing scores zero on it by construction. Search the trigger first, filter by fit second.

---

## Offering 1 — Modernization Services · powered by WeKan Evolve

### ICP-M1 — The Legacy Estate Owner (primary)

Large enterprise running mission-critical workloads on a 10–25+ year relational estate whose cloud and AI agendas are blocked by it — under a cost, risk or transformation mandate with a deadline.

| Dimension | Definition |
|---|---|
| Industries | BFSI, travel/aviation, retail & CPG, healthcare, manufacturing/energy, logistics |
| Size | $500M–$20B revenue (sweet spot $1B–$10B), 2,500+ employees, 200+ engineers |
| Geography | NA/EU primary; India/APAC via BFSI practice |
| Technographic | Legacy core with heavy PL/SQL / T-SQL stored procedures; monolithic C++/Java/.NET coupled to the DB; on-prem or hybrid with a cloud/DC-exit deadline; $1M+ annual DB licence spend; MongoDB footprint anywhere = co-sell path |

- **Buying committee:** CIO/CTO (economic — timeline, risk) · Chief Architect / VP Platform (champion) · Head of Infra / DBA leadership (evaluator, potential blocker — engage early with an audit-ready zero-regression story) · CFO/procurement (licence-cost case) · CISO/compliance (lineage, DORA/RBI/HIPAA)
- **Pains:** 18–36-month SI programs that stall; licensing eating transformation budget; cloud blocked at the data layer; AI blocked by the estate; scarce legacy talent; zero downtime tolerance
- **Triggers:** Oracle ULA renewal / licence audit (highest intent) · cloud commitment or DC-exit deadline · new CIO/CTO/Chief Architect · cost-out program · stalled SI migration · M&A integration · modernization/MongoDB job posts · regulatory clocks (DORA, RBI, resilience rules)
- **Qualify when:** named mission-critical estate with known pain · CIO/CTO sponsor · forcing event ≤2 quarters · assessment-first accepted · real transformation appetite · written success criteria
- **Disqualify:** lowest-rate staff-aug procurement · mega-SI sole-vendor mandates · mainframe/COBOL-only (park in nurture) · no exec sponsor · estate pain under ~$250K/yr
- **Entry offer:** 1-day Modernization & AI-Readiness Review → paid 2–4-week Evolve discovery → phased factory program → app/code → infra → agentic AI
- **Proof points (anonymised):** global travel-technology provider, 25-year Oracle RMS modernized — 50% licensing-cost reduction, zero regression across 75+ end-to-end tests · 40+ workloads for a global insurer · a major UK retail bank's mobile banking modernized end to end · aggregate 50,000+ tables, 10,000+ stored procedures, 800+ dev-days saved in six weeks, ~24 → 10 months time-to-value

### ICP-M2 — The Scaled Digital Platform (secondary)

A growth-stage technology platform or ISV whose MVP-era architecture and sprawling cloud estate are now taxing margins and velocity — infrastructure spend growing faster than revenue, releases slowing, and a board now asking about efficiency.

| Dimension | Definition |
|---|---|
| Industries | Logistics & delivery platforms, insurtech, fintech, marketplaces, vertical SaaS, travel tech — **digital-native companies with real transaction volume** |
| Size | $50M–$1B revenue or $100M+ raised (Series C through pre-IPO); **engineering org of 50–500** |
| Geography | US and Europe primary (matches the delivery-platform and insurtech case studies) |
| Ownership | VC-backed late stage, PE-owned, or newly profitable — all under margin scrutiny |
| Engagement shape | 2-week paid infrastructure & estate assessment with savings quantified → optimization/modernization program → embedded platform-engineering pod |

**The industry list is indicative of the type, not a closed set.** The operative test is the qualifier: digital-native with real *company-side* transaction volume — orders, payments, bookings, policies, trips, listings, card transactions. Customer assets-under-management and market-size figures are not transaction volume.

**Technographic & estate markers**

- Estate sprawl: large cloud database estates (e.g. 100+ MongoDB Atlas clusters), conservative provisioning, <20% average utilization, premium tiers everywhere
- MVP-era core: MSSQL/MySQL/Postgres monolith from the founding era now throttling releases
- Ops markers: legacy database versions in production, missing auto-scaling, index debt, analytics and transactional workloads mixed
- Team shape: thin platform/SRE function relative to product engineering; a CTO who owns the margin question personally

**Buying committee**

| Role | Titles | What they care about |
|---|---|---|
| Economic buyer | CTO, VP Engineering | Velocity, reliability, and the infra line on the P&L; looking for a senior partner, not a body shop |
| Champion | Head of Platform / Infrastructure, Principal Engineer | Getting out of firefighting; credibility of production-safe execution |
| Financial gatekeeper | CFO, COO | Path-to-profitability math; savings validated, not promised |

- **Pains:** infra spend growing faster than revenue, cloud bill a standing board topic · monolith-era architecture slowing releases exactly when the market demands iteration · reliability incidents with direct revenue impact · platform team too small to run optimization and roadmap simultaneously
- **Triggers:** efficiency mandate after a funding round, layoff or profitability pivot · IPO preparation (margin story construction) · public incident or visible outage · cloud-spend milestones or contract renewals (Atlas, AWS/GCP/Azure commits) · hiring signals: SRE, platform engineering, DBRE roles
- **Qualify when:** cloud database/infra spend of $1M+ annually, or a core monolith with named scaling pain · CTO/VP Engineering engaged directly · willingness to grant production telemetry access · openness to an ongoing partnership after the optimization win
- **Disqualify:** shopping for one-off hourly tuning · no production access will be granted (assessment-by-hearsay fails) · pre-revenue or sub-scale estates where savings cannot fund the engagement
- **Also exclude (derived, 2026-09-02):** companies whose own product is infrastructure (databases, hosting, PaaS, developer platforms, observability, data connectivity, GPU compute, workflow orchestration) — deepest in-house benches, lowest winnability · portfolio/holding companies operating independent brands — no single estate, no single margin owner · publicly listed and SPAC-bound companies — ICP stops at pre-IPO
- **Entry offer — the only one:** fixed-fee **2-week estate assessment** that quantifies savings against real workload data (self-funding: identified savings routinely exceed program cost by an order of magnitude). Expansion: optimization program → application modernization (monolith → microservices) → embedded pod → agentic surfaces via NitroStack (ICP-A2 overlap).
- **Proof points to lead with (anonymised — use exactly two):**
  1. **Estate cost & sprawl.** Global on-demand delivery platform (Series E, $12B valuation): 100+ clusters optimized, $1M+ annual savings, 30–90% per-cluster reduction, zero downtime. *Lead with this where the pain is estate cost or sprawl.*
  2. **Velocity & monolith.** US insurtech: MSSQL monolith re-engineered to cloud-native microservices — product launch time from 2 weeks to 5 minutes, 3× query performance, 2× dev velocity. *Lead with this where the pain is release velocity or a founding-era monolith.*
- **Approved first-line hooks (verbatim):**
  - "We found a $12B delivery platform $1M+ a year in its Atlas estate — without touching customer experience. A 2-week assessment would tell you what's hiding in yours."
  - "Your infra bill is growing faster than your revenue. That's not a scaling law — it's provisioning debt, and it's fixable in production, with zero downtime."
- **Why WeKan wins here:** this ICP buys proof-per-dollar — documented, production-safe wins at scale; modernization + growth in one partner; investor-backed, BSI-tier MongoDB mastery the client's generalist cloud partner does not have

---

## Offering 2 — Product Engineering · powered by Helix

### ICP-P1 — The Enterprise Product Builder (primary)

Product/digital/innovation leader with a named initiative and a P&L attached who cannot get it built at mandate speed with internal teams consumed by run-the-business.

- **Firmographics:** the modernization verticals + enterprise software divisions; $500M+ revenue (upper mid-market $250M+); NA/EU. Buying centre often BU/digital P&L, outside central IT procurement
- **Buyers:** CPO/CDO/BU GM (economic) · VP Product / Head of Digital (champion) · CTO/CIO/EA (gatekeeper — architecture, security, maintainability) · BU finance (stage-gated spend)
- **Pains:** 6–8-week discovery burns the window · agencies ship output not outcomes · initiatives ship then die (no instrumentation) · AI codegen = speed without direction · governance requirements agencies can't pass
- **Triggers:** announced digital initiative / digital-revenue target · new CPO/CDO (first 180 days) · innovation-unit or venture-build launch · competitor launch · PE value-creation plan · a modernization program reaching "now build on it"
- **Qualify when:** named initiative with owner and funded budget · start ≤90 days · blueprint-first discovery accepted · enterprise-grade requirements that favour WeKan · stakeholder access during discovery
- **Disqualify:** staff-aug/rate-card RFPs · design-only or prototype theatre · cheapest-offshore runs · no client-side product owner
- **Entry offer:** Helix discovery sprint (5–7 days, fixed fee, fundable blueprint out) → build pod → embedded team → agentic product surfaces

### ICP-P2 — The Funded Founder & Scale-up (secondary, distinct tier)

Funded teams converting capital into traction on a deadline: (a) pre-MVP founders (Seed–A, $2M–$15M); (b) post-MVP stuck pre-PMF (A–B); (c) scale-ups re-platforming (B–E) — the latter overlaps ICP-M2 and often enters through modernization.

- **Firmographics:** fintech/insurtech, healthtech, vertical SaaS, marketplaces; US-heavy + UK/EU hubs. Channels: VCs, accelerators, PE operating partners, venture studios, MongoDB startup ecosystem
- **Buyers:** founder/CEO, CTO — direct access, no intermediaries; investors as channel
- **Pains:** burn vs runway · senior hiring takes 6+ months · MVP built wrong · no instrumentation, opinion-driven iteration
- **Triggers:** fresh round announced (highest intent) · first VP Eng posting · demo days · visible dev-shop failure · PE platform acquisitions
- **Qualify when:** ~$1.5M+ raised or revenue-backed · founder bought into clarity-first · multi-quarter horizon · decision-maker in the room
- **Disqualify:** unfunded idea-stage (route exceptional teams to WeKan Labs) · "just build my spec" · body rental at freelance rates · reputational-risk categories
- **Entry offer:** ideation & blueprint sprint (founder-friendly fixed fee) → MVP build → embedded team → PMF (Helix Grow) → agentic; feeder for ICP-A2

---

## Offering 3 — Agentic AI Implementation · powered by NitroStack + Agentic SE

### ICP-A1 — The Stalled Enterprise AI Program (primary)

12–24 months into GenAI: pilots and chatbots everywhere, nothing governed in production. A Head of AI now owns the gap; the board wants ROI, not experiments.

- **Firmographics:** regulated first (BFSI, healthcare) + travel, logistics, retail, manufacturing ops. $250M+ revenue, sweet spot $1B+; AI CoE or named AI budget exists. NA/EU; India/APAC via BFSI (RBI-ready)
- **Technographic:** LLM spend in place (Azure OpenAI / Bedrock / Anthropic); LangChain/LangGraph/CrewAI experiments; no MCP layer, no agent identity, no evals/observability, no durable orchestration; data platform present or modernization path accepted (bridge to M1)
- **Buying committee:** CIO/CTO/CDO (economic) · Head of AI / CoE lead (champion) · CISO/risk (blocker-turned-ally — lead with governance) · COO/BU ops (use-case owner) · enterprise architect (evaluator — framework-agnosticism)
- **Pains:** pilot purgatory · chatbots bolted on legacy · three-vendor trap · security blocks every deploy · cost/latency unmanaged · earnings-call pressure
- **Triggers:** Head of AI hire (first 90 days) · earnings-call AI commitments with dates · AI pilot vendor churn · MCP/agents/AI-governance job posts · EU AI Act / DORA / RBI clocks · hyperscaler commit renewals with unspent AI credits · industry AI incidents
- **Qualify when:** one named workflow with measurable value · sponsor + use-case owner · production intent · data access grantable · foundation adequate or modernization accepted
- **Disqualify:** demo-chatbot / innovation theatre · frontier-model research asks · strategy-only with no build · security excluded from the room · estate can't feed AI and won't modernize
- **Entry offer:** AI-readiness review / 2-week agentic readiness assessment → 4–8-week production pilot on one governed workflow → multi-agent program → enablement; upstream modernization routed to M1

### ICP-A2 — The Agent-Native ISV & the Installed Base (secondary)

(a) B2B SaaS ($10M–$500M ARR, public API) needing their product in the agent ecosystem before competitors; (b) WeKan's installed base, whose AI-ready foundations make agentic the natural next engagement.

- **Buyers:** CPO/CTO (ISV) · VP Platform / Head of Integrations (champion) · existing executive sponsor (installed base)
- **Pains:** customers asking "can your product talk to our agents?" · no roadmap capacity · API-exposure security fear · (installed base) foundation built, no intelligence-layer plan
- **Triggers:** competitor ships MCP server / ChatGPT-Claude app · platform/marketplace announcements · enterprise RFP requiring agent access · NitroStack community entries from target accounts · modernization final phase = the QBR moment
- **Entry offer:** MCP server sprint (2–4 weeks fixed scope) or agentic pilot inside the account rhythm → embedded agentic surfaces → NitroCloud hosting → full A1 program
- **Note:** installed base is a **warm QBR motion — never cold-automate it.**

---

## Negative ICP — global disqualifiers

Rate-card staff augmentation · no executive sponsor · mega-SI-only RFPs · AI theatre · unfunded startups (exceptional → WeKan Labs) · pure lift-and-shift · hostile commercial terms (liability/IP beyond boutique capacity).

---

## Signal library — top signals → play

| Signal | Where it shows up | ICP | Play |
|---|---|---|---|
| Oracle ULA renewal / licence audit | Procurement chatter, job posts, filings | M1 | Estate-review offer |
| New CIO/CTO/Chief Architect | LinkedIn, press | M1 / A1 | "First 90 days" POV |
| Cloud / DC-exit deadline | Earnings, press, job posts | M1 | Estate review |
| Cost-out / efficiency program; margin pressure | Earnings calls, press | M1 / M2 | Savings-quantified assessment |
| Stalled SI migration | Network, job posts | M1 | Second opinion |
| **MongoDB / Postgres adoption signals** | **Job posts, tech blogs, MongoDB field team (co-sell)** | **M1 / M2** | **Joint motion with MongoDB; BSI credential leads** |
| **SRE / platform / DBRE hiring** | **Job boards** | **M2** | **Savings-quantified assessment** |
| Funding round | Crunchbase feed | P2 | Blueprint offer |
| First VP Eng posting | Job boards | P2 | Blueprint offer |
| New CPO/CDO or digital initiative | LinkedIn, press | P1 | Discovery sprint |
| Head of AI hire | LinkedIn | A1 | Readiness assessment |
| MCP / agents in job posts | Job boards | A1 | Governance-led |
| EU AI Act / DORA / RBI clocks | Regulatory calendar | A1 / M1 | Readiness + modernization |
| Competitor ships MCP server | Product news | A2 | MCP sprint |
| M&A | Press | M1 / P1 | Integration play |

---

## Standardized entry offers

All paid, bounded, high-certainty first steps.

| Offer | ICP | Shape |
|---|---|---|
| Modernization & AI-Readiness Review | M1 / A1 | 1 day |
| **Estate & Infra Assessment, savings-quantified** | **M2** | **2 weeks, fixed fee** |
| Helix Discovery Sprint | P1 / P2 | 5–7 days, fixed fee |
| Agentic Readiness Assessment + Production Pilot | A1 | 2 weeks + 4–8 weeks |
| MCP Server Sprint | A2 | 2–4 weeks |

---

## Activation rule

**One campaign = one ICP × one trigger × one offer.** One segmented list per ICP; landing page per ICP; M1 + A1 signal feeds first; named owner; quarterly closed-loop review of reply/meeting/win rates per ICP.
