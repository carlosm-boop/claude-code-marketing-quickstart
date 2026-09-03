#!/usr/bin/env node
/**
 * SessionStart hook — inject the marketing OS working memory.
 *
 * Reads marketing/latest.md and hands it to Claude as additionalContext, so
 * open conflicts and recent drift are visible BEFORE anything gets decided.
 * This is what stops stale context propagating silently.
 *
 * Read-only. Never blocks. Always exits 0, even on error — a session must
 * never fail to start because of this file.
 */
'use strict';

const fs = require('fs');
const path = require('path');

const MAX_CHARS = 6000;

try {
  const root = process.env.CLAUDE_PROJECT_DIR || process.cwd();
  const latest = path.join(root, 'marketing', 'latest.md');

  if (!fs.existsSync(latest)) process.exit(0);

  let body = fs.readFileSync(latest, 'utf8').replace(/\r\n/g, '\n').trim();
  if (!body) process.exit(0);

  if (body.length > MAX_CHARS) {
    body = body.slice(0, MAX_CHARS) + '\n\n[...truncated — read marketing/latest.md in full]';
  }

  const context =
    'WORKING MEMORY — marketing/latest.md (auto-loaded at session start).\n' +
    'Anything listed here as an open conflict or a DRAFT file must be treated as\n' +
    'unresolved. Do not let a downstream skill consume it as settled truth.\n\n' +
    body;

  process.stdout.write(JSON.stringify({
    hookSpecificOutput: {
      hookEventName: 'SessionStart',
      additionalContext: context
    }
  }) + '\n');
} catch (_) {
  // Deliberately silent. A broken hook must not be a broken session.
}
process.exit(0);
