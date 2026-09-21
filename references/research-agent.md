# Research / Retrieval Agent Product Rules

Use for deep-research, web research, RAG-style investigation, market research, comparison, due-diligence, and evidence-backed answer agents.

## Required node modules

1. Task normalization
2. Research plan / decomposition
3. Dynamic checklist
4. Progress/convergence gate
5. Query generation
6. Search provider/fallback
7. Query dedup/reuse
8. Result triage / snippet-first
9. Source priority / freshness
10. URL normalization/dedup
11. Static fetch
12. JS/browser fetch fallback when applicable
13. Domain/source failure rerouting
14. Page trimming/extraction
15. Evidence/notes write
16. Cross-source verification
17. Conflict handling
18. Context monitoring/compaction
19. Stop/budget/circuit breaker
20. Final report / citation validation
21. Final fallback
22. Eval/release gate

## Suggested V1 defaults when project has no existing values

Use only as starting points; existing product decisions override them.

- max research steps: 20
- progress self-check: step ≥4 or budget ≥50%
- soft convergence: budget ≥80%
- hard tool removal: budget ≥95%
- hard finalization: budget ≥100% or step=20
- search result candidates: 5
- similar-query reuse threshold: 0.75 when a numeric similarity mechanism exists
- same-run successful normalized URL: network re-fetch = 0
- static fetch timeout: 15s
- JS/browser fetch timeout: 30s
- static body too-short trigger: <150 chars
- JS body minimum: 100 chars
- long-page extraction trigger: >800 chars
- tool-return page text ceiling: about 4,000 chars
- same-domain failure reroute: ≥2 cumulative failures
- critical fact verification: 1 current first-party source OR ≥2 independent secondary sources
- max distinct search angles for one unresolved critical fact: 3
- current/fresh secondary source target: ≤90 days when “current/latest” matters
- context compaction trigger: prompt_tokens > 4,000
- recent valid messages retained after compaction: 6
- HITL timeout for risky action: 10 min
- consecutive tool failures before circuit breaker: 4
- max circuit-breaker activations: 2; next equivalent failure chain finalizes partially

## Query/search dedup

- Exact query match: reuse; no new network search.
- Highly similar query: reuse previous results and require a materially different angle before searching again.
- Similar wording alone does not count as a new angle.

## URL reuse

Normalize URL identity before duplicate decisions. Product behavior should ignore tracking fragments/parameters when they do not change content identity.

Same run:
- successful fetch already exists → use cached content; network request=0.

Later session/turn:
- static fact → reuse if still valid.
- current/latest/price/version query → allow refresh after the product-defined freshness window.

## Snippet-first

Allow search snippets to become evidence when they directly contain an unambiguous fact from a trustworthy source and the missing page context cannot materially change the meaning.

Require page deep-read when:
- price/limits/terms need qualifiers
- feature/version differences matter
- tables or surrounding conditions matter
- snippet/title conflict
- comparison claim requires nuance

## Evidence grading

### A-level critical fact
Examples: price, quota, date, product spec, policy/compliance fact, key comparison conclusion.

Verified if:
- 1 current first-party/official source, or
- no first-party source exists and ≥2 independent secondary sources agree.

Same organization/domain should normally count as one independent source, even across multiple URLs.

### B-level descriptive fact
One credible source may be enough when impact is low and no conflicting evidence exists.

### User/community sentiment
Do not convert anecdote into objective truth. Require at least 2 independent discussion/user sources before describing a recurring trend, and label as user feedback.

## Conflict handling

When evidence conflicts:
1. compare source authority
2. compare date/version
3. compare applicability/scope
4. prefer direct first-party evidence when current and applicable
5. if unresolved, report the disagreement and both sources

Do not average incompatible claims.

## Final report contract

Recommended structure:
- executive summary
- findings by research sub-question
- key facts/numbers with citations
- conflicts / uncertainty
- unverified or unavailable items
- references
- partial-result note when stopped early

Critical claims must not exceed the evidence pool.
