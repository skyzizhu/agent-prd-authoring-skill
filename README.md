# agent-prd-authoring

一个可复用的 Agent Skill，用于为 AI Agent 产品产出正式的、可直接交付工程实现的 PRD。

支持的 Agent 类型：
- 研究/检索类 Agent
- 编程类 Agent（类似 Codex / Claude Code）
- 浏览器/电脑操作类 Agent
- 工作流/执行动作类 Agent
- 数据/分析类 Agent
- 客服/知识类 Agent
- 多 Agent/编排调度系统
- 混合型 Agent

## 生成内容

本 skill 将 Agent 创意、代码仓库、实现笔记或已有 PRD 转化为包含以下内容的产品规格说明：
- 明确的端到端流程
- 节点地图与详细节点行为
- 运行状态机
- 关键子流程图
- 硬性产品参数
- 重试/降级/超时策略
- 上下文/记忆/状态规则
- 权限控制与人机协同（HITL）
- 收敛与终止条件
- 最终输出/降级兜底契约
- 端到端完成的定义（E2E Definition of Done）
- 按原型类型定制的 Eval 评估与 GO/NO-GO 发布门槛

除非你明确要求，本 skill 有意不产出技术设计文档。

## 目录结构

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

## Codex / ChatGPT 安装

仓库级 Codex skill：

```text
<repo>/.agents/skills/agent-prd-authoring/
```

个人级 Codex skill：

```text
~/.agents/skills/agent-prd-authoring/
```

在 Codex 中通过 skill 选择器调用（例如 `$agent-prd-authoring`），或在开启隐式触发时由 description 自动触发。

## Claude Code 安装

项目级：

```text
<repo>/.claude/skills/agent-prd-authoring/
```

个人级：

```text
~/.claude/skills/agent-prd-authoring/
```

调用方式：

```text
/agent-prd-authoring
```

当请求匹配 skill 描述时，Claude Code 也可以自动加载它。

## 推荐用法

针对已有 Agent：把代码仓库或项目文档交给本 skill，并要求产出**正式 PRD**，而不是通用模板。

针对全新 Agent：提供目标用户、核心任务、可用的工具/动作、风险等级和期望输出。对于缺失的非安全类取值，skill 会自行选定具体的 V1 默认值；对于高风险动作，会采用保守的审批边界。

## 校验

运行：

```bash
python scripts/validate_skill.py
```

该脚本会检查 skill 的 frontmatter、文件引用、行数预算和必需资源。
