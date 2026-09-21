# Support / Knowledge Agent Product Rules

## Required modules

- intent/task classification
- identity/account context boundary
- policy/KB retrieval
- answer/action eligibility
- confidence/coverage check
- answer drafting
- escalation/handoff
- ticket/state update if applicable
- final customer-facing response

## Grounding
Product/policy claims must be grounded in current approved knowledge sources when available.

## Identity/account boundary
Do not reveal or act on account-specific information without the product-defined authentication/authorization state.

## Escalation
Define explicit triggers, such as:
- policy ambiguity
- unsupported exception request
- high financial impact
- security/privacy concern
- required human judgment
- repeated failed self-service attempt

## Unsupported promises
The agent must not promise refunds, credits, timelines, policy exceptions, or account changes beyond its authorized action set.

## Handoff
When escalating, preserve:
- customer intent
- relevant facts
- actions already attempted
- retrieved policy references
- unresolved question

## Evaluation
At minimum:
- factual/policy correctness
- resolution completeness
- escalation accuracy
- privacy/safety
- unsupported commitment rate
