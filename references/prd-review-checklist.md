# Final PRD Review Checklist

## Structure
- [ ] Product goal, scope, and non-goals are explicit.
- [ ] Global product parameter table exists.
- [ ] End-to-end flow exists.
- [ ] State machine exists.
- [ ] Node overview and detailed node specs use stable IDs.
- [ ] Critical subflows are diagrammed.

## Agent behavior
- [ ] Core loop is explicit.
- [ ] Model autonomy vs hard system boundaries is unambiguous.
- [ ] Soft convergence has a trigger and behavior.
- [ ] Hard convergence has a trigger and behavior.
- [ ] Max steps/turns is explicit.
- [ ] User stop behavior is explicit.
- [ ] Partial success is defined.

## Failure handling
- [ ] Model timeout/retry/fallback is explicit.
- [ ] Tool/action failure and circuit breaker are explicit.
- [ ] Dependency/auth failure is explicit.
- [ ] Context-compaction failure is explicit.
- [ ] Final-output failure has a fallback ladder.
- [ ] No useful work can silently disappear after failure.

## State/context
- [ ] Active context, task notes, evidence/artifacts, memory, and logs are separated.
- [ ] Context-compaction trigger is numeric/explicit.
- [ ] Required retained state is explicit.
- [ ] Tool/action protocol integrity is protected.

## Risk/control
- [ ] High-risk actions are classified.
- [ ] Approval timeout and reject semantics are explicit.
- [ ] Repeated denied action behavior is explicit.
- [ ] Irreversible/external actions have post-action verification where applicable.

## Archetype-specific
- [ ] Research: dedup, URL reuse, freshness, source hierarchy, cross-validation, conflicts, citations.
- [ ] Coding: repo grounding, edit scope, tests, repair loop, diff review, destructive commands, Git boundary.
- [ ] Browser/action: stale state, submit confirmation, post-action verification.
- [ ] Data: schema grounding, read/write boundary, data sensitivity, result validation.
- [ ] Support: policy grounding, escalation, privacy.
- [ ] Multi-agent: worker scope, budget, merge/conflicts, termination.

## Acceptance/Eval
- [ ] Success/Partial Success/Failure are defined.
- [ ] E2E stability batch is defined.
- [ ] P0 NO-GO items are listed.
- [ ] Quality metrics have numeric thresholds.
- [ ] Regression threshold exists.
- [ ] Safety-zero metrics are zero.
- [ ] GO/NO-GO table exists.

## Writing/format
- [ ] No “PM should...” teaching sections.
- [ ] No vague “适当/必要时/尽量” without concrete conditions.
- [ ] No unnecessary technical implementation prescription.
- [ ] Figures are readable and cross-referenced.
- [ ] Tables are not clipped or awkwardly split.
- [ ] Terminology is consistent.
