# Example: Coding Agent Node Map

A Codex/Claude Code-like product may resolve into:

- N00 用户任务与目标结果
- N01 Workspace / Repo Validity
- N02 Project Instructions / Session Context
- N03 Task Normalization / Acceptance Target
- N04 Work Plan
- N05 Repo Search / Symbol Discovery
- N06 Relevant File Read / Grounding
- N07 Change Scope Lock
- N08 Edit Plan
- N09 File Edit / Patch
- N10 Command Selection
- N11 Test / Lint / Typecheck Execution
- N12 Verification Result Classification
- N13 Failure Diagnosis
- N14 Repair Loop
- N15 Diff / Scope Review
- N16 Regression Check
- N17 Context Compaction / State Recovery
- N18 Model/Tool Retry & Circuit Breaker
- N19 User Stop
- N20 Destructive Command / HITL
- N21 Git Commit / Push Boundary
- N22 Final Verification
- N23 Final Change Summary
- N24 Partial Success / Blocked Output
- N25 Run Log / Artifacts
- N26 Eval / Release Gate

Typical mandatory diagrams:
- End-to-End Coding Flow
- Run State Machine
- Read/Edit/Test/Repair Loop
- Risky Command & Git Approval Flow
- Context/Artifacts/Workspace State
- Failure/Fallback Flow
- Final Verification & Partial Success Flow
