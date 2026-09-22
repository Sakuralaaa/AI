<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 01 | Know Your Agent: Vehicle, Fuel, and Driver

[简体中文](../zh-CN/01-know-your-agent.md) · [Home](../../README.en.md)

## Remember this

The agent framework or desktop workspace is the vehicle, the model is the fuel, and the prompt is the destination. You still own the route and the final inspection.

## Why this matters

Many configuration mistakes come from confusing the vehicle with the fuel. Changing a model does not replace the interface and tools; changing an agent does not automatically transfer subscriptions. Separating the layers tells you whether to change the model, client, context, tool, provider, or permission.

## Four roles

1. **Agent framework:** Codex, Claude Code, and PI-Desktop organize sessions, tools, files, execution loops, and interfaces.
2. **Model:** Interprets, reasons, and generates. Harder or higher-stakes tasks may benefit from stronger models, but simple work often does not.
3. **Provider:** Supplies authentication, model access, billing, limits, and availability. A consumer subscription and an API product are not automatically interchangeable.
4. **User:** Selects the workspace, defines the objective, grants permission, and verifies the outcome.

## Important components

| Concept | Purpose | Common misconception |
|---|---|---|
| Context | Conversation, files, and tool results visible now | More context is always better |
| Token | A model metering unit | It maps directly to words or currency |
| MCP | Connects external tools and context | Installed means trusted |
| Skill | Reusable workflow guidance | It increases the model's inherent ability |
| Sandbox | Limits local execution | It should be disabled whenever something fails |
| Approval | Human checkpoint | It is safe to approve without reading |

## Try it: locate the failing layer

When “the agent is bad,” ask in order:

1. Is the destination clear, including format and acceptance criteria?
2. Does the agent have the right files and background?
3. Is the selected model suitable for the difficulty?
4. Are the tool, MCP server, and local application actually available?
5. Are permissions too narrow—or unnecessarily broad?
6. Is the provider returning authentication, quota, or network errors?

Layering the diagnosis works better than blindly rewriting the prompt.

## Mistakes I have made

- Confusing an articulate answer with verified truth.
- Assuming a consumer subscription includes API access in any client.
- Abbreviating CLIProxyAPI as CPA, then treating CPA as a `.cpa` file format.
- Switching providers without recording model mappings or result differences.

## A normal result and checklist

You can state which client is executing, which model is reasoning, which provider carries the request, which tools and permissions are active, and who verifies the result.

- [ ] I can distinguish agent, model, and provider.
- [ ] I know subscription and API access are separate products.
- [ ] I know MCP connects tools while Skills encode workflows.
- [ ] I know CLIProxyAPI is a project, not a file format.
- [ ] Important results still require human review.

## Sources and verification

- [OpenAI Docs: Best practices](https://learn.chatgpt.com/guides/best-practices)
- [OpenAI Docs: MCP](https://learn.chatgpt.com/docs/extend/mcp)
- [Glossary](../../resources/glossary.en.md)
- Last verified: 2026-09-22

[Previous](00-before-driving.md) · [Next: Choose and install](02-choose-and-install.md)
