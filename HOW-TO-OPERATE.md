# How to operate this system

Your workspace is built. This is how you drive it.

Fifteen minutes. No code. Seven habits, then a troubleshooting table you can come back to when something feels off.

The one idea underneath all seven: **the setup is the work.** Most people treat Claude like a smarter search box — type, read, take the first answer. That ceiling is low. The people who get real work out of it spend their effort on what Claude knows, what it can check itself against, and how much room it has to think. Then the output takes care of itself.

---

## 1. Give it a way to check its own work

**What it is.** Instead of asking for a thing, ask for a thing plus the standard it has to meet. Claude drafts, checks itself against the standard, and fixes what fails — before you ever see it.

**Why it matters.** Without a standard, you are the only quality signal. Every draft comes back to you, you spot the same three problems, you send it back. With a standard, that loop runs without you.

**In your work.** Don't say "write a competitor teardown." Say "write a competitor teardown, then check it against our teardown standard — every claim has a source, no adjectives without evidence, pricing quoted not paraphrased — and fix anything that fails." Better still, write that standard down once so you stop retyping it. A quality-check hook is this habit made automatic: it fires on every draft, every time, whether you remember or not.

**The mistake it prevents.** Being the only thing standing between a first draft and a client.

---

## 2. Make it plan before it touches anything

**What it is.** A read-only mode. Claude explores your files, works out what it would do, and shows you the plan. Nothing changes until you approve. `Shift+Tab` twice to enter it.

**Why it matters.** Editing a plan costs a minute. Undoing six wrongly-rewritten files costs an afternoon.

**In your work.** Any time a request touches more than one file — refreshing messaging across the spine, restructuring your ICP, rewriting a page and its supporting docs — plan first. Read the plan properly. If it has misread your positioning, you'll see it there, in a paragraph, instead of finding it later spread across six files. Skip planning for small, obvious edits; it's overhead on a one-line fix.

**The mistake it prevents.** Discovering halfway through a rewrite that it misunderstood the brief.

---

## 3. Send a second Claude to do the reading

**What it is.** A subagent — a separate Claude with its own memory, sent to do one job, that reports back a summary. Its reading never enters your session.

**Why it matters.** Your session has a fixed amount of room. Reading forty competitor pages fills it, and there's nothing left for the actual thinking. A subagent does that reading somewhere else and hands you back the three themes.

**In your work.** Two shapes cover most of it. **Investigation:** "Use a subagent to read every page on their site and come back with how they position against us." You get the answer, not the forty pages. **Review:** one session writes the positioning, then a fresh one reviews it — with no memory of having written it, so it reads like a stranger would. That second pair of eyes is the point; a Claude reviewing its own work talks itself into the work.

**The mistake it prevents.** Burning the whole session on research and having no room left to think.

---

## 4. Keep the session clean

**What it is.** Everything said in a session stays in it — good context and dead ends alike. Managing that is a habit, not a setting.

**Why it matters.** A session that starts sharp gets vague after a few hours. That's not the model having a bad day; it's a full, cluttered session.

**In your work.** Four moves:

- **Finished a piece of work?** Clear the session and write a fresh brief for the next one. New task, new session.
- **Continuing, but it's got long?** Compact it, and say what should survive — "keep the positioning decisions and the file list, drop the drafts."
- **It went down a wrong path?** Rewind to before the wrong turn rather than typing "that didn't work, try something else." That sentence leaves the failed attempt sitting in the session, and it keeps tripping over it.
- **Quick unrelated question mid-task?** Ask it as a side question so it doesn't get folded into the work.

**The mistake it prevents.** The 4pm session that's worse than the 9am one, and you can't work out why.

---

## 5. Connect fewer tools than you want to

**What it is.** Connections let Claude reach your other systems directly — your docs, your CRM, your analytics, your notes. Every connection also adds to the list of options it weighs before every action.

**Why it matters.** More connections make it slower to start and worse at choosing. Three well-chosen beats fifteen.

**In your work.** Start where your work actually lives — usually your docs and your notes. Add one, use it on something real, then decide if you need another. When you do add, prefer ones scoped to the project you're in over ones switched on everywhere. If something feels sluggish or it keeps reaching for the wrong source, the connection list is the first place to look.

**The mistake it prevents.** Connecting everything in week one, then wondering why it picks the wrong source.

---

## 6. Keep a private notes file

**What it is.** A file that sits beside your main context file, loads the same way, and never leaves your machine. Yours only.

**Why it matters.** Some corrections are about your taste, your habits, or feedback you personally keep getting. They belong in your workspace but not in the shared one.

**In your work.** Every time you correct the same thing twice, write it down here. "Stop using the word leverage." "Our buyer is the Head of PMM, not the CMO — stop writing to the CMO." "Always give me the numbers before the recommendation." Keep two sections: things about this project, and habits of your own you're trying to correct. Prune it every few weeks — once something is automatic, it can go.

**The mistake it prevents.** Giving the same note every week and wondering why it never lands.

---

## 7. Let it write its own rules

**What it is.** When Claude gets something wrong, end your correction with: *"Update the context file so you don't repeat this."*

**Why it matters.** This is the habit that compounds hardest. Claude is unusually good at turning its own mistake into a precise rule — better, often, than you'd write it, because it knows exactly what it misread.

**In your work.** It ships USD pricing to a UK client → correct it, then have it write the rule. It uses last quarter's positioning → correct it, then have it write the rule. Do this for a month and your context file becomes a list of every trap your work contains, written in the phrasing the model actually responds to. You stop guessing what belongs in there.

**One caution:** keep the file short. Long context files bury the rules that matter. For each line, ask — would removing this cause a mistake? If not, cut it.

**The mistake it prevents.** Correcting the same thing forever while the context file never changes.

---

## When something feels off

| What you're seeing | What's usually happening | What to do |
|---|---|---|
| It went off and did the wrong thing | It started work before you agreed on the approach | Plan mode first (§2). Read the plan, edit the plan, then approve |
| Sharp this morning, sloppy now | The session is full of old work | Clear and write a fresh brief, or compact and say what to keep (§4) |
| It keeps making the same mistake | The correction never got written down | Have it write the rule (§7); if it's personal, your private notes (§6) |
| It read a load of files and then had no room left | The reading happened in your session | Send a subagent to read and report back (§3) |
| The output looks right but you don't trust it | Nothing checked it but you | Give it the standard to check against, then make it a hook (§1) |
| It reaches for the wrong tool or source | Too many connections to choose between | Trim to the ones you actually use (§5) |
| It says it's done but you can't tell if it worked | It claimed success without evidence | Ask for the proof — the output, the file, the number. Never accept "done" on its own |

---

## The short version

☑ Give it a standard to check itself against
☑ Plan before it touches more than one file
☑ Send a subagent to do the heavy reading
☑ New task → new session; wrong turn → rewind, don't argue
☑ Three good connections, not fifteen
☑ Private notes for what you keep repeating
☑ Every correction becomes a rule

Setup is the work. Execution is verification.

---

*Some of the habits here were sharpened by Arpan Patel's "Beyond the Prompt: Claude Code" (arps18.github.io, May 2026), rewritten for marketing and GTM work.*
