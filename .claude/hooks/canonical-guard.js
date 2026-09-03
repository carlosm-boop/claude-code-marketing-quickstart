#!/usr/bin/env node
/**
 * PreToolUse hook — guard the canonical context files.
 *
 * marketing/rules/escalation.md says overwriting a canonical file always
 * escalates to Rudra. Canonical files are the compounding axis: every
 * downstream output inherits them, so a silent edit propagates everywhere.
 * This makes that rule mechanical instead of remembered.
 *
 * MODE controls behaviour:
 *   'warn'  (default) — allows the write, tells Claude and Rudra it happened.
 *                       Zero friction, no clash with agents doing approved work.
 *   'block'           — denies the write outright. Switch to this once you
 *                       trust the file list and want a hard gate.
 *
 * Always exits 0. A guard that crashes the session is worse than no guard.
 */
'use strict';

const MODE = 'warn'; // <- change to 'block' for a hard gate

const CANONICAL = [
  'marketing/company/company.md',
  'marketing/positioning/positioning.md',
  'marketing/messaging/messaging.md',
  'marketing/icp/ICP.md',
  'marketing/brand/brand-kit.md',
  'marketing/brand/brand-voice.md',
  'marketing/rules/escalation.md',
  'marketing/rules/gate-rules.md'
];

let raw = '';
process.stdin.on('data', (c) => { raw += c; });
process.stdin.on('end', () => {
  try {
    const ev = JSON.parse(raw || '{}');
    const input = ev.tool_input || {};
    const target = String(input.file_path || input.path || '').replace(/\\/g, '/');
    if (!target) return process.exit(0);

    const hit = CANONICAL.find((c) => target.endsWith(c));
    if (!hit) return process.exit(0);

    const reason =
      'CANONICAL FILE: ' + hit + '\n' +
      'marketing/rules/escalation.md requires Rudra to approve any overwrite of a ' +
      'canonical context file. Every downstream skill reads this file, so an ' +
      'unreviewed change propagates to every future output.\n' +
      'Confirm with Rudra before proceeding, and log the change in marketing/history.md.';

    if (MODE === 'block') {
      process.stdout.write(JSON.stringify({
        hookSpecificOutput: {
          hookEventName: 'PreToolUse',
          permissionDecision: 'deny',
          permissionDecisionReason: reason
        }
      }) + '\n');
    } else {
      process.stdout.write(JSON.stringify({
        hookSpecificOutput: {
          hookEventName: 'PreToolUse',
          additionalContext: reason
        },
        systemMessage: 'Canonical file being edited: ' + hit + ' — confirm this was approved, and log it in marketing/history.md.'
      }) + '\n');
    }
  } catch (_) {
    // Silent by design.
  }
  process.exit(0);
});
process.stdin.on('error', () => process.exit(0));
