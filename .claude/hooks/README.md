# hooks/ — orchestration triggers (ACTIVE)

*Rev. 2026-08-31. Both hooks are wired in [`../settings.json`](../settings.json) and running.*

Written in **Node**, not bash. Claude Code is itself a Node CLI, so `node` is guaranteed present wherever Claude Code runs — which sidesteps the Windows/POSIX-shell problem entirely. Both scripts use only `fs`, `path`, and stdin, so they behave identically on Windows, macOS, and Linux.

## Hook 1 — `session-context.js` (SessionStart)

Injects `marketing/latest.md` into context when a session starts, so open conflicts and DRAFT files are visible before anything gets decided.

This is the highest-value hook in the system. The failure mode it prevents is the one the source article warns about: stale context compounds, because the same drift propagates everywhere the agents reach, faster than a human would catch it.

- **Fires on:** `startup`, `resume`, `clear`
- **Reads:** `marketing/latest.md` (first 6000 chars)
- **Writes:** nothing. Read-only.
- **On error:** silent, exits 0. A broken hook must never be a broken session.

## Hook 2 — `canonical-guard.js` (PreToolUse on Write|Edit)

`marketing/rules/escalation.md` says overwriting a canonical file always escalates. Canonical files are the compounding axis — every downstream skill reads them, so a silent edit propagates to every future output. This hook makes the rule mechanical instead of remembered.

**Ships in `warn` mode.** It allows the write and flags it to both Claude and you. To make it a hard gate, change one line at the top of the script:

```js
const MODE = 'block';   // was 'warn'
```

Warn mode is the default deliberately: a `deny` hook that misfires is genuinely irritating, and you should watch which files it actually catches for a week before letting it block anything.

**Guarded paths:**

`company.md` · `positioning.md` · `messaging.md` · `ICP.md` · `brand-kit.md` · `brand-voice.md` · `escalation.md` · `gate-rules.md`

Edit the `CANONICAL` array in the script to change the list.

## Do these clash with the agents?

No — and the design is deliberate about it.

| | Hook 1 | Hook 2 |
|---|---|---|
| **What it touches** | Adds context at session start | Observes Write/Edit calls |
| **Blocks an agent?** | Never | Not in `warn` mode |
| **Overlaps agent logic?** | No — agents are *told* to read `latest.md`; the hook guarantees it happens even when a session skips the instruction | No — it enforces a rule the agents already carry, from outside them |

The one place they interact is `context-refresh`, which writes findings **to** `marketing/latest.md` — the file hook 1 reads. That's the loop working as intended: the agent writes the delta, the hook surfaces it next session. `latest.md` is not in the guarded list, so the refresh agent is never blocked.

**If you switch hook 2 to `block`:** agents will be denied on canonical writes, which is exactly what `escalation.md` asks for — but you'll then need to approve those writes explicitly. That's the trade. Warn mode until the file list has proven itself.

## Verifying they work

```bash
# Hook 1 — should print JSON containing your latest.md
CLAUDE_PROJECT_DIR="$PWD" node .claude/hooks/session-context.js

# Hook 2 — should print a canonical-file warning
echo '{"tool_input":{"file_path":"marketing/positioning/positioning.md"}}' | node .claude/hooks/canonical-guard.js

# Hook 2 — should print nothing (non-canonical path)
echo '{"tool_input":{"file_path":"marketing/outbound/research/x.md"}}' | node .claude/hooks/canonical-guard.js
```

Both were verified against Node v22 before shipping.

## Turning them off

Delete the relevant block from [`../settings.json`](../settings.json), or delete that file entirely. The scripts are inert on their own.

## Owner

Rudra.
