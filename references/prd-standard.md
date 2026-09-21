# Formal Agent PRD Standard

## Purpose

This reference defines the minimum product-specification depth for a formal AI agent PRD.

A formal PRD must be complete enough that engineering can design the implementation, QA can derive test cases, and product/design can review behavior without guessing.

## Required sections

### 0. Document control
Include product name, PRD version, status, date, change summary, and source-of-truth note.

### 1. Product definition
Include:
- product type / agent archetype
- target user and core jobs
- core product objective
- scope and non-goals
- success criteria

### 2. Global product parameters and hard boundaries
Create one authoritative table. Repeat values in node specs when relevant, but this table is the canonical location.

Typical fields:
- max steps / turns
- budget/cost tiers
- soft convergence threshold
- hard convergence / tool removal threshold
- timeouts
- model retry count/backoff
- fallback model attempts
- tool retry/circuit breaker
- approval timeout
- context-compaction threshold
- duplicate-work policy
- freshness window
- source/evidence thresholds
- edit/test cycles for coding agents
- browser action retries
- release thresholds

### 3. End-to-end flow, state machine, node map
Must show:
- user entry
- planning / normalization
- main agent loop
- tool/action loop
- state updates
- convergence
- stop / approval / failure branches
- finalization
- persistence / logs

### 4. Critical subflows
Draw only behaviorally complex subflows: branches, loops, state transitions, permissions, or multi-stage fallbacks.

### 5. Detailed node specifications
Every behaviorally meaningful node gets a stable ID.

Required node fields:
1. Node ID and name
2. Purpose
3. Entry condition
4. Inputs/state
5. Agent behavior
6. Product rules / thresholds
7. Output/state update
8. Branches / next nodes
9. Failure / fallback
10. User-visible state
11. Acceptance criteria

### 6. Cross-node behavior rules
Examples:
- deduplication / idempotency
- source or execution verification
- context/memory boundaries
- user-control semantics
- risk/approval rules
- repeated-failure behavior
- convergence rules

### 7. User experience and observability
Define user-visible progress and internal replay/debug requirements without prescribing storage or UI framework.

### 8. Failure/retry/degradation
Maintain a matrix covering every major dependency or agent subsystem.

### 9. E2E acceptance / Definition of Done
Define Success, Partial Success, Failure, P0 blockers, stability batch, quality thresholds, safety-zero thresholds, and GO/NO-GO.

### 10. Evaluation / release gate
Use archetype-specific metrics and fixed regression sets.

## Product requirement vs technical design boundary

A product requirement must specify behavior when a choice changes user experience, cost, safety, reliability, quality, or acceptance.

Specify in PRD:
- max retries
- timeout
- fallback sequence
- hard stop threshold
- user approval boundary
- what state survives compaction
- what counts as duplicate work
- acceptance thresholds
- post-action verification requirement

Do not prescribe by default:
- class/module names
- async/threading design
- DB table schema
- REST endpoint paths
- SDK-specific code
- queue implementation
- cache storage technology
- embedding/vector algorithm choice unless it is intentionally a product contract

## Precision standard

Bad:
- “必要时重试”
- “适当压缩上下文”
- “尽量避免重复请求”
- “模型判断是否结束”

Good:
- “429/5xx/timeout最多请求3次；第2/3次分别等待2s/5s；仍失败进入Backup Model 1次。”
- “prompt_tokens > 4,000触发Compaction；必须保留Goal、已验证事实、未完成Checklist、用户约束和最近6条合法消息。”
- “同一规范化URL在同一Run成功Fetch后，再次访问网络请求数=0。”
- “Budget≥95%后研究型Tools不可调用；Step=20无论Checklist状态均进入Final。”

## Formality rule

Do not write instructional commentary such as “PM should pay attention to...” inside the PRD. Convert it into product behavior.
