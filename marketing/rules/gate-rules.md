# WeKan.AI — gate rules (review checklist per output type)

*Seeded 2026-08-31. Rules 1–3 are extracted from existing WeKan constraints and are firm. Rules 4+ are placeholders — fill them by running the Manager Prompt on yourself.*

---

## Rule 1 — The proof firewall holds

**The rule:** No asset pairs a client name with a metric, outcome, or specific.

**Why:** Case-study material is anonymized for contractual reasons; joining the pools re-identifies clients.

**Violation pattern:** "We saved Amadeus 50% on licensing." · "SNCF went live ahead of Paris 2024." · A logo strip beside a stats band on the same fold.

**Fix template:** Split them. Names → "companies we've worked with," no numbers. Metrics → "a global travel-technology provider," no name.

**Exception:** None. This is the only rule in the repo with no exception.

## Rule 2 — Every number traces to a source

**The rule:** A figure appears only if it is in `messaging.md` §6, `company.md`, or a cited external source.

**Why:** Invented specificity is the fastest way to lose a technical buyer, and unrecoverable once caught.

**Violation pattern:** Round numbers that appear nowhere upstream. "Up to 60% faster" used as standard when `company.md` says ~50%.

**Fix template:** Replace with the sourced figure, or write `[UNAVAILABLE]` and escalate.

**Exception:** Clearly-labelled illustrative examples, marked as such in the copy itself.

## Rule 3 — Positioning is never narrowed

**The rule:** No asset positions WeKan as a point solution — a database shop, a migration vendor, a MongoDB partner, a staff-aug supplier.

**Why:** The whole differentiation is owning the arc. Narrowing it in one asset undercuts every other asset.

**Violation pattern:** A page whose H1 names only modernization. Cold email that opens with MongoDB. Anything using "digital transformation."

**Fix template:** Reframe the fragment as the on-ramp: "modernization is where it starts, not where it stops."

**Exception:** Deliberately targeted campaigns (e.g. the Realm EOL wedge) may lead with the fragment — but must land the arc before the CTA.

---

## Rules 4+ — to extract

Run the **Manager Prompt** on yourself and convert the answers into rules in the format above:

1. What are the 3–5 things you ALWAYS check first when reviewing a piece of WeKan content?
2. What red flags make you immediately skeptical of a draft?
3. What context do you wish people gave you upfront but rarely do?
4. Describe a recent draft that surprised you positively. What did it do?
5. Describe a recent draft that missed. What was missing?

Until this is done, agents are enforcing three rules and guessing at the rest.

## Owner

Rudra.
