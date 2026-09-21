# Common Agent Node Library

Use this as a completeness checklist, not as a fixed linear workflow.

## A. Entry and initialization

### N00 User Input / Task Creation
Specify required input, optional controls, validation, empty/invalid handling, and initial user-visible status.

### N01 Session / Preference / Prior-State Injection
Define what historical context may be reused and what must never be injected automatically.

### N02 Budget / Step / Permission Initialization
Lock budgets, max steps, risk policy, stop flag, and per-run counters.

### N03 Task Normalization
Resolve object, scope, time range, environment, constraints, expected deliverable, and ambiguous terms.

### N04 Planning / Decomposition
Define max/min subproblems or workstreams, structure validation, repair count, and minimal-plan fallback.

### N05 Checklist / Worklist Initialization
Define statuses and how completion is judged.

## B. Core loop

### N06 Turn Gate / Progress Gate
Check stop, budget, max steps, checklist, pending approval, repeated failures, and context size.

### N07 Next Action Decision
Define what the model may choose and what system rules override it.

### N08 Tool/Action Selection
Define eligible tools/actions by state and risk level.

### N09 Tool/Action Execution
Define timeout, retries, dedup/idempotency, result recording, and permission boundary.

### N10 Observation / Verification
Decide whether the result is trustworthy/complete enough to affect durable state.

### N11 Durable State Update
Update notes, artifacts, checklist, evidence, test status, or workflow state.

### N12 Progress Assessment
Classify as progress / repeated attempt / blocked / complete / partial.

### N13 Continue / Redirect / Converge
Decide whether to keep exploring, change strategy, or enter finalization.

## C. Context and state

### N14 Context Monitoring
Trigger compaction/cleanup by explicit threshold.

### N15 Context Compaction
Define required preserved state and deterministic fallback.

### N16 Long-Term Memory Update
Persist only approved stable information; define cap/TTL/merge policy if applicable.

### N17 Run/Event Logging
Define what must be replayable for debugging and audit.

## D. Control and recovery

### N18 User Stop / Cancel
Define safe-stop behavior, in-flight action handling, and partial-result behavior.

### N19 HITL / Approval
Define which actions require approval, timeout, reject semantics, and re-prompt rules.

### N20 Model Failure / Retry / Fallback
Separate transient model failure from malformed output and capability mismatch.

### N21 Tool/Action Failure / Circuit Breaker
Define consecutive failure threshold, reset condition, strategy-switch rule, and final fallback.

### N22 Dependency / Authentication / Configuration Failure
Define whether the run can continue in degraded mode or must fail early.

## E. Finalization

### N23 Completion Check
Define what is sufficient to finalize.

### N24 Final Output Generation
Define structure, grounding, unresolved items, and user-facing status.

### N25 Final Validation
Check empty output, unsupported claims, failed tests, unverified external action, or missing required sections.

### N26 Forced Final / Fallback Output
Define multi-level fallback ladder and minimum usable deliverable.

### N27 Terminal State / Persistence
Set completed/stopped/failed, stop reason, metrics, memory update, and history entry.

## Add nodes when needed

Split a common node when it contains product-significant sub-decisions. Examples:
- Search can split into query generation, provider fallback, dedup, snippet filter, URL fetch, evidence validation.
- Coding can split into file discovery, file read, edit, test, diagnose, repair, diff review.
- Browser use can split into observe, navigate, fill, review, confirm, submit, verify.

Do not merge nodes merely to make the PRD shorter if merging hides a threshold, permission boundary, or fallback.
