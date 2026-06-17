# Rule — PII redaction (mask before model, store, or share)

When handling sales-call or meeting transcripts (e.g., `/win-loss-analysis`) or any record carrying customer PII, mask the identifiers before the model sees them, before you store the artifact, and before you share it. Keep the signal — roles, company, deal context — that the analysis actually runs on.

If the data carries no PII (public company research, your own strategy docs), this rule is silent.

## The three gates — model, store, share

1. **Before model.** Redact identifiers before pasting a transcript into a session. The model doesn't need the end-customer's name or account number to find win/loss patterns — it needs the words, roles, and deal shape.
2. **Before store.** A saved artifact keeps the redacted form, not the raw PII.
3. **Before share.** Anything going to a doc, Slack, or email is redacted first. External surfaces get cached and indexed — a name you remove later may already be cached.

## What to mask

| PII type | Mask to |
|---|---|
| End-customer / consumer names | `[CLIENT]`, `[CLIENT-2]` (stable per person within a doc) |
| Email addresses | `[EMAIL]` |
| Phone numbers | `[PHONE]` |
| Account / policy / reference numbers | `[ACCOUNT]` |
| Card / IBAN / sort codes | `[CARD]` |
| Home addresses, postcodes | `[ADDRESS]` |

## What NOT to over-redact — keep the signal

Don't strip what the analysis runs on. **Keep:** the rep's / seller's name and role, the prospect *company* (for B2B), job titles, deal stage, product and competitor names, the actual spoken words, and timestamps. Over-redaction destroys the signal and is its own failure. The target is *identity*, not *context*.

## How to check

Run a regex pass before bulk processing; named-person redaction still needs a judgment pass:

```
email      :  [A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}
phone      :  (\+?\d[\d\s().-]{7,}\d)
card (16d) :  \b(?:\d[ -]*?){13,16}\b
```

If you can't run the regex on a bulk transcript, redact by hand before processing — don't process raw and "clean later."

## Owner

Whoever owns the win-loss / transcript work (named in [`quarterly-maintenance.md`](./quarterly-maintenance.md)).

## Refresh cadence

Reviewed each quarterly maintenance pass.
