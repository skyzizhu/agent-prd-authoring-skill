# Coding / Software Engineering Agent Product Rules

Use for Codex-like, Claude Code-like, IDE agents, autonomous code-editing agents, bug-fix agents, repo assistants, and software engineering copilots that can execute tools.

## Required node modules

1. User task / target outcome
2. Workspace/repository validation
3. Project instruction/context loading
4. Task normalization and acceptance target
5. Codebase discovery / search
6. Relevant file read / grounding
7. Change plan
8. Edit/write operation
9. Build/test/lint/typecheck command selection
10. Command execution and result capture
11. Failure diagnosis
12. Repair loop
13. Diff/scope review
14. Regression check
15. Destructive/external command approval
16. Git/commit/push boundary
17. Final summary and unresolved issues
18. Run log / artifacts
19. Eval / release gate

## Core behavior rules

### Ground before edit
Do not permit code claims or edits based only on guessed file paths. The agent must inspect relevant files before modifying them.

### Scope lock
The PRD must define:
- what files/directories are in scope
- whether dependency/config changes are allowed
- whether generated files may change
- whether test snapshots may update automatically
- whether unrelated cleanup is allowed

Default: no unrelated refactors during a targeted task.

### Change plan
Before multi-file or risky edits, the agent should form a concise change plan tied to the user outcome and expected verification.

### Edit loop
Typical loop:
`discover/read → plan → edit → run verification → diagnose → repair → diff review → finalize`

## Suggested V1 defaults when project has no existing values

- max main-agent turns: 30 for ordinary coding task; 50 only for explicitly deep/autonomous mode
- max repair cycles for the same failing verification: 3
- command timeout: use project-appropriate default; 120s for ordinary test/lint commands unless repo indicates longer
- repeated identical failing command with no code/config change: do not rerun more than once
- diff review before final: mandatory when files changed
- required verification: at least one project-relevant check when executable environment allows it
- destructive/external action without approval: 0

## Verification hierarchy

Select the narrowest useful verification first, then broaden when needed:
1. syntax/static check for changed area
2. targeted tests
3. relevant lint/typecheck
4. broader test suite when cost/time allows or risk requires

Do not claim “fixed” if required verification could not run. Use “implemented but unverified” and state why.

## Repair loop

When verification fails:
1. capture the actual failure
2. determine whether failure is caused by the change, environment, or pre-existing state
3. repair only if within task scope
4. rerun the most relevant verification
5. after 3 materially similar failed repair cycles, stop automatic repair and return Partial Success / blocked state with evidence

## Diff/scope review

Before final output:
- inspect changed files/diff
- detect unrelated edits
- detect debug code/temp files/secrets
- confirm user-requested behavior is represented
- confirm tests/verification status

## Risk and approval boundary

Require explicit user approval before actions such as:
- deleting significant files/directories not clearly requested
- `git reset --hard`
- force push
- rewriting published history
- pushing/merging to shared remote when not explicitly authorized
- modifying production infrastructure or secrets
- destructive DB operations
- disabling safety checks as a shortcut

Local reversible edits and local test commands may proceed within approved task scope unless user policy says otherwise.

## Git boundary

Define separately:
- edit permission
- commit permission
- push permission
- merge/rebase/force permission

Do not assume that permission to edit implies permission to push.

## Final output contract

Include:
- what changed
- files/areas changed
- verification performed and result
- unresolved failures / environment blockers
- any user action still required

Do not expose hidden chain-of-thought; summarize observable work and results.

## Coding-agent evaluation dimensions

At minimum:
- task success
- required tests pass
- regression-free behavior
- scope adherence
- diff quality
- unsafe/unauthorized action violations
- truthful verification reporting
