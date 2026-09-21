# Browser / Computer-Use / Workflow Action Agent Rules

Use when the agent navigates UI, fills forms, clicks buttons, or calls external systems that mutate state.

## Required modules

- task and target-system normalization
- authentication/session state
- observe current state
- action selection
- action execution
- post-action state verification
- stale/changed-state recovery
- form review
- approval for high-impact action
- idempotency / duplicate-action protection
- rate-limit/retry handling
- rollback/compensation if available
- final action receipt / outcome summary

## Observe-act-verify loop

Every state-changing action should follow:
`observe → validate preconditions → act → observe again → verify expected state`

Never infer success solely because a click/API call was sent.

## Suggested defaults

- ordinary UI action retry after stale/transient failure: max 2 additional attempts
- repeated same action after unchanged failure: stop and choose alternate route
- irreversible/external action approval timeout: 10 min unless product context requires shorter
- unauthorized irreversible/external action: 0
- post-action verification coverage for irreversible/external actions: 100%

## High-risk actions

Require explicit approval for:
- purchases/payments
- sending external messages
- deleting user/business data
- changing permissions/access
- submitting legally/financially consequential forms
- publishing/deploying externally visible changes
- account/security settings changes

Show the user:
- intended action
- important parameters/target
- expected effect
- risk/irreversibility

Reject/timeout means do not execute. Do not immediately re-request the identical denied action.

## Idempotency

For actions that may be retried, define how the product prevents duplicate creation/payment/message/send/update.

If idempotency cannot be guaranteed, require state re-check before retry.

## Stale state

When page/UI state changed:
- reacquire current state
- do not continue using old coordinates/assumptions blindly
- revalidate the target before action

## Final contract

Return verified outcome, not just attempted action.
If outcome cannot be verified, state “action attempted, final state unverified” and do not present success as certain.
