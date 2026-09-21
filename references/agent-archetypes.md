# Agent Archetype Classifier

Classify the product before selecting node modules.

## 1. Research / Retrieval Agent
Signals:
- web or knowledge retrieval
- source reading
- evidence/citations
- comparison/research reports

Mandatory extra modules:
- query generation
- result dedup/reuse
- source ranking/freshness
- URL dedup
- fetch/deep-read fallback
- evidence extraction
- cross-source verification
- conflict handling
- citation/final grounding

## 2. Coding / Software Engineering Agent
Signals:
- reads/modifies a repository
- shell/terminal use
- tests/lint/typecheck
- patch/diff generation
- Git operations

Mandatory extra modules:
- workspace/repo grounding
- task-to-code-scope normalization
- code search/read
- change plan
- edit/apply patch
- command/test execution
- failure diagnosis and repair loop
- diff/scope review
- destructive command boundary
- Git/push boundary
- regression acceptance

## 3. Browser / Computer-Use Agent
Signals:
- interacts with websites/UI through screenshots/DOM/computer control
- form filling
- multi-step navigation

Mandatory extra modules:
- page/screen state capture
- navigation/action selection
- stale-state recovery
- auth/session boundary
- form review before submit
- irreversible action confirmation
- post-action verification

## 4. Workflow / Action Agent
Signals:
- calls business APIs or external services
- creates/updates/sends/deletes data
- executes transactions or workflows

Mandatory extra modules:
- identity/auth/precondition
- idempotency
- external-write classification
- approval boundary
- action execution
- post-action verification
- compensation/rollback where possible
- audit trail

## 5. Data / Analytics Agent
Signals:
- SQL/data warehouse/files/tables
- analytics questions
- chart/report generation
- possible write queries

Mandatory extra modules:
- dataset/schema discovery
- query plan
- read/write classification
- query execution
- result validation
- sensitivity/PII rules
- export/output
- reproducibility

## 6. Support / Knowledge Agent
Signals:
- customer questions
- product policy/KB retrieval
- ticket handling
- escalation

Mandatory extra modules:
- intent classification
- identity/account boundary
- KB/policy retrieval
- answer drafting
- confidence/escalation
- prohibited promises/actions
- handoff context

## 7. Multi-Agent / Orchestrator
Signals:
- manager/worker agents
- parallel delegation
- specialist subagents

Mandatory extra modules:
- decomposition
- worker scope
- budget allocation
- isolated/shared context policy
- worker result contract
- conflict/duplication handling
- synthesis
- termination

## 8. Hybrid Agent
Use multiple modules when the agent materially combines archetypes.

Examples:
- coding agent with browser testing → Coding + Browser
- research agent that sends a report by email → Research + Workflow/Action
- data research agent → Data + Research

Do not include modules that do not affect the product behavior.
