# Document Style Standard

## Tone

- Clear, concise, neutral, formal.
- Avoid motivational or tutorial language.
- Avoid explaining the role of a PM inside the PRD.
- Avoid filler such as “为了更好地”, “需要注意的是”, unless it changes a requirement.

## Requirement language

Prefer:
- “必须” for hard requirements.
- “允许” for permitted behavior.
- “禁止/不得” for prohibited behavior.
- “默认” for versioned defaults.
- “当…时” for triggers.
- “否则” for fallback.

## Numbering

Recommended:
- Sections: 0, 1, 2...
- Nodes: N00, N01...
- Figures: 图 1, 图 2...
- Rules: R-01, R-02... when many cross-node rules exist.
- Acceptance: AC-01... if traceability is useful.

## Tables

Use tables for:
- global parameters
- node overview
- state definitions
- retry/fallback matrix
- risk/approval matrix
- verification rules
- acceptance gates
- evaluation metrics

Avoid giant prose tables where a node specification is clearer.

## Page/layout guidance for Word/PDF

- A4 portrait by default.
- Use landscape only for a single wide matrix when necessary.
- Do not split a single node’s key rule table awkwardly across pages.
- Repeat table headers across pages.
- Keep figures on one page whenever possible.
- If a diagram becomes unreadable, split it into main flow + subflow.
- Use consistent caption format.
- Use one Chinese sans-serif font family consistently when possible.

## Figure captions

Format:
`图 5  Search / Fetch / JS Fallback 子流程（对应 N08–N16）`

## Cross-reference style

Use explicit references:
- “详见图 8。”
- “本规则同时适用于 N06、N20、N27。”
- “最终验收以 9.1 为准。”

## Avoid

- placeholder text such as “待研发确认” unless the business decision truly cannot be made
- raw code snippets in product requirements
- API/DB schema dumps
- duplicated explanations across many nodes
- vague adjectives without acceptance criteria
