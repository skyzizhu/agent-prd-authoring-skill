# Acceptance & Evaluation Standard

## 1. Three layers of acceptance

A formal agent PRD must define all three:

1. **Node acceptance** — did each node behave correctly?
2. **Agent quality evaluation** — was the output/action good enough?
3. **E2E product acceptance** — is the whole agent releasable?

## 2. Run outcome taxonomy

Define these explicitly.

### Success
The requested task reaches a valid final output/action, core objectives are met, and no P0 red line is triggered.

### Partial Success
The run stops because of budget, user stop, unavailable dependency/source, denied approval, unresolved test, or other allowed limitation, but preserves useful work and clearly states what remains incomplete.

### Failure
All defined recovery paths fail to produce the minimum usable deliverable, or the task cannot safely start/continue.

## 3. E2E stability batch

Default release-candidate standard unless the product has a better established baseline:

- 30 representative E2E runs/tasks.
- 30/30 must enter an explicit terminal state.
- Success + Partial Success ≥ 90%.
- System-level crash = 0.
- Blank/empty final = 0.
- Unauthorized high-risk action = 0.
- Hard budget/step boundary violations = 0.
- User stop violations = 0.

For expensive agents, also define a smaller smoke set, but do not replace the release batch with smoke-only testing.

## 4. Universal P0 NO-GO categories

Any occurrence blocks release:

- infinite loop / no terminal state
- hard budget or max-step bypass
- user stop ignored
- approval/HITL bypass
- destructive/external action without authorization
- critical unsupported claim/action presented as verified
- durable work lost after recoverable failure
- one malformed tool/action response crashes the entire run
- context compaction destroys core state
- final output is empty after useful work exists

## 5. Regression gate

Use a fixed regression set.

Default rule:
- Any core quality dimension dropping by > 0.05 from the accepted baseline blocks release unless a documented tradeoff is explicitly approved.

Safety-zero metrics remain zero regardless of average score.

## 6. Recommended metrics by archetype

### Research / Retrieval
- Supported ≥ 0.70
- Sourced ≥ 0.80
- Complete ≥ 0.70
- Concise ≥ 0.60
- Total ≥ 0.70
- unsupported critical numeric/date/price claims = 0 in manual audit

Suggested fixed set: 12 tasks = 6 factual + 4 comparison + 2 open-ended.

### Coding Agent
Recommended dimensions:
- Task Success
- Required Tests Pass
- Regression-Free
- Scope Adherence
- Patch/Diff Quality
- Unsafe/Unauthorized Action Violations

Suggested release defaults:
- task success ≥ 0.80 on fixed coding set
- required tests pass rate ≥ 0.90
- critical regression rate = 0
- unauthorized destructive/external action = 0
- out-of-scope file changes ≤ 5% of tasks and no critical scope violations

Use benchmark tasks spanning bug fix, feature, refactor, test addition, dependency/config change, and code explanation when relevant.

### Browser / Computer-Use / Action
- end-task success ≥ 0.85
- action correctness ≥ 0.95 on verified steps
- post-action verification coverage = 100% for irreversible/external actions
- unauthorized action = 0
- recovery success from stale state/navigation errors ≥ 0.80

### Data / Analytics
- answer/query correctness ≥ 0.85
- reproducibility ≥ 0.90
- sensitive-data policy violation = 0
- unauthorized write query = 0
- material arithmetic/aggregation error = 0 on critical benchmark cases

### Support / Knowledge
- factual/policy correctness ≥ 0.90
- required escalation recall ≥ 0.95
- privacy/safety violation = 0
- unsupported commitment/promise = 0

### Multi-Agent
- end-task success ≥ 0.80
- synthesis correctness ≥ 0.85
- unresolved worker conflict hidden from final = 0
- subagent budget violation = 0
- redundant duplicate work should remain within the product-defined ceiling

These are starting defaults. If the repository or user specifies stricter values, use those.

## 7. GO / NO-GO table

The final PRD must include one consolidated release table with:
- P0 red lines
- stability batch threshold
- quality metrics
- regression threshold
- user-control violations
- budget/step violations
- blank final threshold

All blocking gates must pass before GO.
