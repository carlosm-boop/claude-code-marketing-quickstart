# EST + HIR posting pull — domain list

*Assembled 44 domains, 3 September 2026, for workstream 1's Job Posting Search (call 1 of 2).*

**Paste the block below into the prompt.** One row per domain required, including domains with no matching posting — that absence is the data being bought.

## The 44

```
zuora.com
carta.com
pushpay.com
metropolis.io
icapital.com
workrise.com
id.me
zeta.tech
ezcater.com
covergenius.com
netradyne.com
ridezum.com
cmtelematics.com
civitatis.com
sayweee.com
housecallpro.com
backmarket.com
blockchain.com
fleetio.com
wallapop.com
hotelengine.com
sureapp.com
fareye.com
amberstudent.com
csiweb.com
cabify.com
docplanner.com
eisgroup.com
esw.com
entrata.com
itilite.com
jobandtalent.com
minted.com
offerup.com
peopleperhour.com
relexsolutions.com
rgigroup.com
sitly.nl
teacherspayteachers.com
zinnia.com
fabric.inc
italki.com
vinted.com
shiftkey.com
```

## Composition

- **23** roster accounts with no committed posting text — the 22 unmeasured plus Metropolis Technologies, whose untraceable `EST◐` was dropped 2026-09-03 and must be re-measured. **Zuora, Carta and Pushpay are in this group and each reaches Tier 1 if EST comes back positive.**
- **19** consolidation accounts from `data/0926-new-accounts-for-roster.csv` — blank on EST, HIR and MDB.
- **2** C1-cleared accounts — Vinted and ShiftKey carry `Infra Posting = true` so HIR is known, but neither has posting text, so EST is unmeasured.

## The 7 cost-test accounts are OUT — resolved 2026-09-03

Struck. Workstream 1 merged the cost-test posting text into `data/0926-origami-job-postings.csv` as `Pull = P9 cost-test` (36 rows → 58, commit `37b10cf`), rather than committing a second text-bearing file. **That is the better fix and the reasoning matters:** committing a second file preserves the evidence but breaks the premise that made the one-grep check work — *"the postings CSV is the only file holding posting text."* The next person greps the canonical file, finds nothing, and buys a pull they did not need. Third time today that same premise error would have fired.

**EST and HIR for the seven were then measured here at zero cost — see `0926-target-accounts.md`.**

**This file now contains exactly 44 domains.**

## Not in the pull

The 29 companies that already have committed posting text in `data/0926-origami-job-postings.csv`, and the 15 Cohort D accounts are included only because they are on the roster — a measured EST absence for them is still worth having, since it converts a blank into a fact.
