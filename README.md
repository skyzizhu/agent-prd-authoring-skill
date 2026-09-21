# agent-prd-authoring

A reusable Agent Skill for producing formal, engineering-ready PRDs for AI agent products.

It supports:
- research/retrieval agents
- coding agents (Codex/Claude Code-like)
- browser/computer-use agents
- workflow/action agents
- data/analytics agents
- support/knowledge agents
- multi-agent/orchestrator systems
- hybrid agents

## What it generates

The skill turns an agent idea, repository, implementation notes, or existing PRD into a product specification with:
- explicit end-to-end flow
- node map and detailed node behavior
- run state machine
- critical subflow diagrams
- hard product parameters
- retries/fallbacks/timeouts
- context/memory/state rules
- permissions/HITL
- convergence/termination
- final output/fallback contract
- E2E Definition of Done
- archetype-specific Eval and GO/NO-GO release gates

It intentionally avoids becoming a technical design document unless you explicitly ask for one.

## Structure

```text
agent-prd-authoring/
├── SKILL.md
├── README.md
├── references/
├── templates/
├── examples/
├── scripts/
└── agents/
```

## Codex / ChatGPT installation

Repository-local Codex skill:

```text
<repo>/.agents/skills/agent-prd-authoring/
```

Personal Codex skill:

```text
~/.agents/skills/agent-prd-authoring/
```

Invoke in Codex with the skill selector (for example `$agent-prd-authoring`) or let it trigger from the description when implicit invocation is enabled.

## Claude Code installation

Project-local:

```text
<repo>/.claude/skills/agent-prd-authoring/
```

Personal:

```text
~/.claude/skills/agent-prd-authoring/
```

Invoke with:

```text
/agent-prd-authoring
```

Claude Code can also load it automatically when the request matches the skill description.

## Recommended use

For an existing agent, give the skill the repository or project docs and ask for a **formal PRD**, not a generic template.

For a new agent, provide the target user, main task, available tools/actions, risk level, and expected output. The skill will choose concrete V1 defaults for missing non-safety values and conservative approval boundaries for high-risk actions.

## Validation

Run:

```bash
python scripts/validate_skill.py
```

This checks the skill frontmatter, file references, line budget, and required resources.
