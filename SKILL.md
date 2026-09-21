---
name: agent-prd-authoring
description: Create or upgrade a formal, engineering-ready PRD for AI agent products. Use when the user provides an agent idea, repository, implementation notes, existing PRD, or asks for a standard PRD covering end-to-end flow, node behavior, state machine, guardrails, retries/fallbacks, context/memory, permissions, evaluation, acceptance, release gates, and diagrams. Supports research agents, coding agents such as Codex/Claude Code-like products, browser/computer-use agents, workflow/action agents, data agents, support agents, multi-agent systems, and hybrids.
---

# Agent PRD Authoring

Create a formal product requirements document that engineering, design, QA, and AI/agent engineers can implement and review without guessing product behavior.

The output is a product specification, not a PM tutorial, prompt-engineering essay, or technical design document.

## 1. Operating principles

1. Define **observable product behavior** precisely.
2. Specify every product-critical threshold, retry count, timeout, termination condition, permission boundary, fallback path, and acceptance threshold with concrete values.
3. Do not leave vague phrases such as “适当重试”, “必要时压缩”, “合理控制次数”, or “尽可能避免”. Convert them into explicit conditions and values.
4. Do not prescribe implementation details unless they are themselves part of the product contract.
5. Do not write sections explaining what a PM should or should not do. Write only the product requirements.
6. When an existing implementation or repository is provided, inspect the real behavior before writing the PRD. Never infer code behavior from filenames alone.
7. When the existing implementation and user-requested target behavior differ, the user’s stated target behavior wins. Preserve the current behavior only when it is intentionally retained.
8. Every non-happy-path must terminate in an explicit product outcome: recover, retry, degrade, ask user, partial success, or fail.
9. For probabilistic agent behavior, define evaluation and end-to-end acceptance in addition to functional requirements.
10. Use diagrams to explain structure and state; use node specifications to explain behavior; use tables to lock parameters and thresholds.

## 2. Read these references selectively

Read only the references needed for the current project.

- Always read `references/prd-standard.md`.
- Always read `references/common-node-library.md`.
- Always read `references/diagram-standard.md`.
- Always read `references/acceptance-eval-standard.md`.
- Read `references/agent-archetypes.md` to classify the agent.
- For research/retrieval agents, read `references/research-agent.md`.
- For coding agents, read `references/coding-agent.md`.
- For browser/computer-use and workflow/action agents, read `references/browser-action-agents.md`.
- For data/analytics agents, read `references/data-agent.md`.
- For customer support/knowledge agents, read `references/support-agent.md`.
- For multi-agent systems, read `references/multi-agent.md`.
- For writing style and document QA, read `references/document-style.md`.

## 3. Source ingestion and project reconstruction

Before drafting the PRD, reconstruct the agent as it actually works or is intended to work.

Use this source priority:

1. Explicit user requirements in the current request.
2. Approved/declared target behavior in product documentation.
3. Current implementation behavior in code and configuration.
4. Existing README, architecture notes, realization docs, tests, prompt files, tool definitions, and eval scripts.
5. Sensible versioned defaults from this skill when the project has no explicit decision.

For an existing repository, inspect enough material to answer at minimum:

- What is the user input and user-visible output?
- What states can a run enter?
- What is the core agent loop?
- What can the model decide autonomously?
- What is enforced outside the model?
- Which tools/actions exist?
- What state is persisted during a run?
- How are context, memory, evidence, artifacts, and logs separated?
- How does the agent converge and terminate?
- What happens when model/tool/action calls fail?
- Which actions require user confirmation?
- What quality/evaluation system exists?

If documentation and code conflict, do not silently average them. Choose the target behavior using the source priority above and make the PRD internally consistent.

## 4. Classify the agent before writing

Classify the product into one or more archetypes:

- research/retrieval agent
- coding/software-engineering agent
- browser/computer-use agent
- workflow/action agent
- data/analytics agent
- support/knowledge agent
- multi-agent/orchestrator
- hybrid

Use `references/agent-archetypes.md` to select the required node modules and evaluation dimensions.

Do not force Search/Fetch/Evidence nodes into a coding-only agent. Do not force Edit/Test/Git nodes into a research-only agent.

## 5. Build a product behavior inventory

Create an internal inventory before drafting:

- entry points
- user inputs and constraints
- planning/decomposition behavior
- core loop
- tools/actions
- intermediate state
- context management
- memory/persistence
- permissions/HITL
- retries and model fallback
- action/tool fallback
- deduplication/idempotency
- convergence and hard termination
- user stop/cancel
- finalization and fallback output
- observability
- evaluation
- end-to-end acceptance

For every item, record the concrete current/target value if one exists.

## 6. Lock the global product contract first

Before writing detailed nodes, create a **Global Product Parameters & Hard Boundaries** table.

Include every product-critical value applicable to the project, such as:

- budget tiers or cost limits
- max agent steps/turns
- progress self-check threshold
- soft convergence threshold
- hard tool-removal threshold
- request timeout
- model retry count and backoff
- backup-model attempts
- tool/action retry limits
- circuit-breaker threshold
- deduplication window/threshold
- context-compaction threshold
- retained recent messages/items
- approval timeout
- source verification rules
- file/edit/test retry cycles for coding agents
- browser action retries and post-action verification
- external-write confirmation rules
- evaluation thresholds
- release gates

If a non-safety value is unspecified, select a concrete V1 default using the closest archetype reference and keep it internally consistent.

For destructive, financial, privacy-sensitive, externally visible, permission-changing, or hard-to-reverse actions, use a conservative default: explicit user approval before execution.

## 7. Construct the node map

Give every node a stable ID: `N00`, `N01`, ...

Start at user input and continue through final output and persistence. Include small but behaviorally important nodes; do not collapse them merely to reduce page count.

Each node specification must contain:

- **Node name**
- **Purpose**
- **Entry condition**
- **Inputs / required state**
- **Agent behavior**
- **Product rules and numeric thresholds**
- **Output / state update**
- **Branches and next nodes**
- **Failure / fallback**
- **User-visible status** when relevant
- **Acceptance criteria**

Do not add implementation fields such as class names, API endpoint names, thread models, database schemas, or SDK calls unless the user explicitly requests technical design.

## 8. Define state machines explicitly

Every formal PRD must define run states and terminal states.

At minimum distinguish:

- created/queued
- planning/preparing
- executing/researching/working
- waiting for approval or user input
- compacting/recovering when applicable
- finalizing/verifying
- completed
- stopped/cancelled with partial result
- failed

Define legal transitions and what causes each transition.

Do not treat `stop_reason` as the same thing as run status. A run may stop early and still produce a valid partial result.

## 9. Design the core loop and termination behavior

Every autonomous agent needs a clearly documented loop:

`gate/check → decide next action → execute action/tool → observe result → update state → assess progress → continue/change direction/finalize`

Specify:

- what the gate checks each turn
- what counts as progress
- what counts as repeated/non-productive behavior
- when the agent may broaden the task
- when it must stop broadening
- soft convergence behavior
- hard convergence behavior
- max step/turn cutoff
- what happens at the final allowed step
- user stop behavior
- circuit breaker behavior

Never rely only on a prompt instruction for a hard safety or cost boundary. The PRD must state that the capability becomes unavailable or the run transitions state when the hard boundary is reached.

## 10. Specify model-call failure policy

For every LLM-powered node, specify:

- request timeout
- retryable errors
- max primary-model attempts
- retry delays/backoff
- backup/fallback model use if applicable
- capability requirements for the fallback model
- node-specific fallback when all model calls fail

Do not use one generic fallback for all nodes. Planning, extraction, main-agent reasoning, compaction, finalization, and memory may require different degradation behavior.

## 11. Specify tool/action behavior

For each tool/action category, define product behavior, not SDK schemas.

Document:

- when the agent should use it
- when it should reuse prior results instead
- deduplication/idempotency rule
- timeout
- retry/fallback
- failure counter behavior
- permission/risk level
- what state is updated after success/failure
- whether the result must be verified before being treated as success

For externally visible or irreversible actions, define pre-action confirmation and post-action verification.

## 12. Specify context, memory, and durable state separately

Do not use “context” and “memory” interchangeably.

Define, as applicable:

- active context: what the model sees this turn
- task/work notes: facts/progress for this run
- evidence/artifacts: source-backed or execution-backed results
- long-term memory/preferences: stable information allowed to persist across sessions
- event/run log: observable execution history

If context compaction exists, define:

- exact trigger
- information that must survive compaction
- number/range of recent messages/items retained
- failure fallback if compaction fails
- whether compaction cost counts toward budget
- protocol integrity rules for tool-call/result pairs

## 13. Specify verification rules by agent archetype

Use the archetype-specific reference.

Examples:

- Research agent: source hierarchy, URL/query dedup, cross-source verification, freshness, conflicts, citations.
- Coding agent: repository grounding, edit scope, test/lint/typecheck, diff review, regression handling, destructive command boundary.
- Browser/action agent: page state verification, stale-state recovery, confirmation before irreversible actions, post-action confirmation.
- Data agent: schema grounding, query validation, read/write separation, result checks, sensitive data handling.
- Support agent: policy grounding, customer identity boundary, escalation triggers, forbidden unsupported promises.
- Multi-agent: worker scope, shared state, merge/conflict resolution, subagent budget, orchestration termination.

## 14. Add diagrams as first-class PRD content

Follow `references/diagram-standard.md`.

A formal agent PRD should normally include:

1. End-to-end user/system flow.
2. Run state machine.
3. Core agent loop.
4. Context/state/data-asset relationship diagram.
5. Convergence/termination decision flow.
6. Failure/retry/fallback flow.
7. Finalization/fallback flow.
8. Archetype-specific critical subflows.

Add a node-level subflow when the node contains branching, looping, state transitions, permission decisions, or multi-stage fallback.

Do not create a diagram for every trivial node.

Each figure must have a figure number, title, and reference to the node IDs it explains.

When generating a Word/PDF artifact, render diagrams as legible images. Prefer portrait-friendly layouts; split a diagram rather than shrinking text below comfortable reading size.

## 15. Define user-visible progress and observability

Specify which product states/actions are visible to the user and which are internal.

At minimum define:

- run started/planning
- current high-level activity
- progress/checklist when useful
- waiting for approval/user input
- recovering/retrying when user-visible delay is material
- finalizing
- completed/stopped/failed

Define what must be available for internal run replay/debugging without prescribing the storage technology.

## 16. Define output contract and final fallback

Specify the final output structure for the archetype.

Also define a fallback ladder. Example pattern:

`normal final → no-tools/no-actions forced final → durable notes/artifacts fallback → explicit failure with preserved partial results`

Define what counts as an invalid/empty final result.

Partial success must be a first-class product outcome when an agent can stop because of budget, user cancellation, unavailable sources, failed tests, denied permissions, or external-service failures.

## 17. Define end-to-end acceptance and release gate

Follow `references/acceptance-eval-standard.md`.

The PRD must include a product-level Definition of Done that answers:

- What is Success?
- What is Partial Success?
- What is Failure?
- What P0 conditions are automatic NO-GO?
- How many E2E runs/tasks are required for stability testing?
- Which quality metrics have hard thresholds?
- What regression from baseline blocks release?
- Which safety/permission violations require a threshold of exactly zero?

Node-level acceptance does not replace product-level E2E acceptance.

## 18. Define evaluation by archetype

Do not use a single universal quality rubric for all agent types.

Use archetype-appropriate dimensions and explicit minimum thresholds.

Examples:

- Research: Supported, Sourced, Complete, Concise, freshness/conflict handling.
- Coding: task success, tests pass, regression-free behavior, scope adherence, diff quality, unsafe action violations.
- Browser/action: task completion, action accuracy, post-action verification, recovery, unauthorized action violations.
- Data: answer/query correctness, reproducibility, sensitivity compliance, write-safety.
- Support: factual/policy correctness, resolution quality, escalation accuracy, privacy/safety compliance.
- Multi-agent: end-task success, worker redundancy, synthesis correctness, budget adherence, conflict resolution.

For stochastic systems, use a fixed regression set plus repeated-run stability testing.

## 19. Document structure

Default formal PRD structure:

0. Document Control
1. Product Definition, Goals, Users, Scope, Non-goals
2. Global Product Parameters & Hard Boundaries
3. End-to-End Flow, State Machine, Node Map
4. Critical Subflows & Decision Diagrams
5. Detailed Node Specifications
6. Cross-Node Behavior Rules / Guardrails / Edge Cases
7. User Experience, Progress, Output, Observability
8. Failure, Retry, Degradation, Stop, HITL
9. Overall E2E Acceptance / Definition of Done
10. Evaluation & Release Gate
11. Change Log / Explicit Open Decisions only if truly unresolved

Avoid separate tutorial sections about product management methodology.

## 20. Writing standard

Write concise, direct, implementation-readable Chinese unless the user requests another language.

Rules:

- One requirement = one clear behavior.
- Use tables for parameters and matrices.
- Use diagrams for branching and loops.
- Use prose for rationale only when it changes behavior.
- Keep terminology consistent.
- Use stable IDs for nodes, figures, rules, and acceptance items.
- Cross-reference related node IDs and figure numbers.
- Never bury hard thresholds only in prose; repeat them in the global parameter table.
- Do not add source code unless explicitly requested.

## 21. Artifact requirements

If the user asks for a formal document artifact and document-generation tools are available:

- Produce `.docx` as the primary editable deliverable.
- Produce PDF only if requested or useful for review.
- Embed all diagrams in the document.
- Use a consistent heading hierarchy, table style, figure captions, page margins, fonts, and page numbers.
- Prevent table rows and node specifications from breaking awkwardly across pages.
- Ensure every diagram is legible at 100% zoom.
- Perform a final rendered-page QA pass before delivery.

Use `templates/formal-prd-outline.md` as the drafting skeleton, not as visible boilerplate.

## 22. Final quality gate before delivery

Read `references/prd-review-checklist.md` and verify every applicable item.

The PRD is not ready if any of these remain ambiguous:

- loop termination
- retry count
- fallback path
- user stop behavior
- permission boundary
- context-compaction behavior
- duplicate work/idempotency behavior
- partial success definition
- overall acceptance gate
- evaluation threshold
- any P0 safety boundary

Deliver the PRD only after these are explicit.
