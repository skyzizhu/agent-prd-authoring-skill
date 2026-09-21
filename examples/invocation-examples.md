# Invocation Examples

## Existing research agent repository

“Use agent-prd-authoring on this repository and create a formal engineering-ready PRD. Read the implementation and docs first. Preserve current behavior where intentional, make all retry/timeout/convergence/evidence rules explicit, add diagrams, and include E2E acceptance and release gates.”

## Codex/Claude Code-like coding agent

“Use agent-prd-authoring to write the PRD for a coding agent that can inspect a repository, edit files, run shell commands and tests, and optionally commit changes. Define workspace scope, edit/test/repair loops, destructive command boundaries, Git permissions, context handling, final diff review, eval, and release gates.”

## Browser purchasing/workflow agent

“Use agent-prd-authoring to create a PRD for a browser agent that fills multi-step forms. Include page-state verification, stale-state recovery, idempotency, user confirmation before irreversible submission, post-action verification, retry policies, and Partial Success behavior.”

## Data agent

“Use agent-prd-authoring for an analytics agent that queries a warehouse and generates reports. Define schema grounding, read/write boundaries, query retries, result validation, PII rules, reproducibility, and evaluation.”

## PRD upgrade/audit

“Use agent-prd-authoring to upgrade this existing PRD. Do not turn it into a template. Find every ambiguous threshold or fallback, add missing node/subflow diagrams, lock E2E acceptance, and return the revised formal document.”
