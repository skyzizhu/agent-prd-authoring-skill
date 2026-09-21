# Diagram Standard for Agent PRDs

## Core rule

Use diagrams to explain structure, state, loops, and decisions. Use node text to explain exact behavior and acceptance.

## Mandatory diagrams for a non-trivial agent

1. **End-to-End Flow**
   - User input to final output.
   - Show the core loop as a loop, not a fake linear sequence.
   - Show convergence/termination and finalization.

2. **Run State Machine**
   - Include transient states and terminal states.
   - Label transitions with conditions.
   - Distinguish `stopped` from `failed`.

3. **Core Agent Loop**
   - gate/check → decide → act/tool → observe → update → assess → continue/finalize.

4. **Context / State / Memory Relationship**
   - Clarify what is ephemeral, task-scoped, durable, source-backed, and audit-only.

5. **Convergence / Termination Decision Flow**
   - Show soft convergence, hard convergence, max-step cutoff, budget/cost cutoff, user stop, and circuit breaker.

6. **Failure / Retry / Fallback Flow**
   - Model failures, tool/action failures, context failures, dependency failures, finalization failures.

7. **Finalization / Fallback Flow**
   - normal final → forced final → durable-state fallback → explicit failure.

## Archetype-specific diagrams

### Research
- search/dedup/snippet/fetch/JS fallback
- evidence verification/conflict handling

### Coding
- repo grounding → search/read → edit → test → diagnose/repair → diff review
- risky command / Git boundary

### Browser / Action
- observe → navigate → act → verify
- form review / confirm / submit / post-action verification

### Data
- schema discovery → query plan → execution → validation → answer/export

### Multi-agent
- manager → decomposition → workers → result contracts → conflict resolution → synthesis

## When a node needs its own subflow

Create a node-level diagram if any apply:
- 2+ decision branches
- a loop/back-edge
- multiple states
- permission/HITL branch
- multi-stage fallback
- a product-critical retry sequence

Do not diagram a node that is a single deterministic transformation.

## Visual conventions

- Rounded rectangle: action/state.
- Diamond: decision.
- Oval: terminal state.
- Dashed/neutral box: cached/reused/optional behavior.
- Red: failure/blocked path.
- Yellow: risk/decision/approval/convergence.
- Green: verified/success/final.
- Keep labels short; detailed rules belong in the node spec.

## Layout rules

- Prefer portrait-friendly top-to-bottom flow for Word/PDF.
- Use left-to-right only for compact state machines.
- Keep each diagram to roughly 6–12 visible nodes when possible.
- Split large flows instead of shrinking labels.
- Ensure all decision edges have labels such as Yes/No, Success/Fail, Enough/Not enough.
- Put figure number and title directly below or above the image.
- Add “对应 Nxx–Nyy” mapping.

## Cross-reference rules

Every complex diagram should point to node IDs. Every detailed node with a diagram should reference the figure number.

Example:
- 图 5 Search / Fetch / JS Fallback（对应 N08–N16）
- N14 网页抓取：内部流程见图 5。
