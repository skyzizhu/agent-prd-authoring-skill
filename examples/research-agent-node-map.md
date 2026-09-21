# Example: Research Agent Node Map

A typical formal research-agent PRD may resolve into:

- N00 用户输入与启动校验
- N01 Session / Preferences 注入
- N02 Budget / Step / Safety 初始化
- N03 问题理解与边界归一
- N04 Research Plan
- N05 Dynamic Checklist
- N06 Progress / Convergence Gate
- N07 Next Action Decision
- N08 Query Generation
- N09 Search Provider / Fallback
- N10 Search Dedup / Reuse
- N11 Result Triage / Snippet-First
- N12 Source Priority / Freshness
- N13 URL Dedup / Cache Reuse
- N14 Static Fetch / JS Fallback
- N15 Domain Failure Reroute
- N16 Page Extraction
- N17 Evidence / Notes
- N18 Cross-Source Verification
- N19 Conflict Handling
- N20 Checklist Update
- N21 Context Monitor
- N22 Context Compaction
- N23 LLM Retry / Model Fallback
- N24 Tool Failure / Circuit Breaker
- N25 User Stop
- N26 HITL
- N27 Hard Convergence / Max Step
- N28 Final Report
- N29 Final Fallback
- N30 Memory / Session Persistence
- N31 Run Log / Observability
- N32 Eval / Release Gate

This is a reference shape, not a fixed requirement. Merge or split nodes according to actual product behavior, but do not hide product-critical decisions.
