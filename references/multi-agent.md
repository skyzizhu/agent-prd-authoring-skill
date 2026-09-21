# Multi-Agent / Orchestrator Product Rules

## Required modules

- decomposition decision
- worker selection/assignment
- worker scope contract
- per-worker budget/turn limits
- isolated/shared context rules
- worker result contract
- duplicate-work control
- worker failure handling
- result conflict handling
- synthesis
- manager termination

## When to delegate

Use workers when tasks are meaningfully parallel, require isolated context, or need distinct specializations.
Do not delegate trivial sequential work merely because subagents exist.

## Worker contract

Each worker should receive:
- specific objective
- allowed tools/actions
- budget/step limit
- required output structure
- evidence/artifact expectations
- forbidden scope expansion

Workers should not recursively create subagents unless the product explicitly allows it.

## Shared state

Define what is:
- shared read-only
- shared writable
- worker-local
- manager-only

Avoid simultaneous uncontrolled writes to the same artifact/workspace.

## Duplicate work

Manager should detect overlapping worker assignments and either merge or cancel redundant work before expensive execution.

## Conflict handling

If workers disagree:
1. compare evidence/execution results
2. identify scope/version/environment differences
3. ask a targeted tie-breaker worker only if necessary
4. surface unresolved conflict in final output

## Termination

Manager must have its own max-step/budget rule independent from workers.
Worker completion does not imply overall completion; manager must validate synthesis coverage.
