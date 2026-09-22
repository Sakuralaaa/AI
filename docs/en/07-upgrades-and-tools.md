<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 07 | Upgrade the Vehicle: MCP, Skills, Multi-Agent Work, and Computer Use

[简体中文](../zh-CN/07-upgrades-and-tools.md) · [Home](../../README.en.md)

## Remember this

More extensions do not automatically make a stronger system. Add MCP, a Skill, a plugin, or a second agent only when a clear problem cannot be solved by existing capability.

## MCP: the accessory port

Model Context Protocol connects an agent to external tools and context. Local Codex clients support local STDIO servers and remote HTTP servers; those transports create different process, network, and authentication boundaries.

Before installation, ask:

- Who maintains it, and where are source and releases?
- What can it read, write, or delete?
- Does it access the network, and where does data go?
- How is it authenticated, and where are secrets stored?
- How do you stop, remove, and inspect it?

After adding a server in the Codex desktop interface, save and restart as directed. Test one tool with non-sensitive data before expanding scope.

## Skills: driving playbooks

A Skill is commonly a directory containing `SKILL.md`, describing when to use a workflow, the steps, and successful completion. It may include scripts, references, and templates. It does not upgrade the model; it reduces repeated explanation and workflow drift.

Weekly reports, spreadsheet checks, and publication-export rules may become Skills. Keep one-off requests in the prompt and durable repository agreements in AGENTS.md.

## Plugins: packaged upgrade kits

On supported products, plugins may combine Skills, MCP servers, and optional UI. Treat them as software supply chain, not harmless text. Review maintainer, version, permissions, network behavior, and update history.

## Multi-agent work: a fleet, not clones

Parallelize independent outputs such as source research, spreadsheet review, and slide review. Work requiring shared state or continuous decisions is often clearer with one agent.

A practical split is producer and reviewer. Keep output directories separate and assign one integrator. Never let two agents edit the same file without coordination.

## Computer Use and browser work

Use them for real interfaces, missing APIs, or visual inspection. Keep human confirmation for sign-in, payment, publication, deletion, messaging, and final submission. Web pages and documents may contain malicious instructions aimed at the agent; page content is data, not authority.

## Try it

Choose a low-risk process repeated at least three times, such as converting meeting notes into a recap and actions. Run it as a normal prompt, write stable steps and checks, then decide whether it belongs in a template, AGENTS.md, or a Skill. Add MCP only if an external system is actually required.

## Mistakes I have made

- Installing many MCP servers without understanding their process and file access.
- Turning a temporary preference into a global rule.
- Letting parallel agents edit the same deck and losing versions.
- Allowing Computer Use to click the final submit action.

## Checklist

- [ ] Every extension has a purpose and minimum permission.
- [ ] I can distinguish MCP, Skill, plugin, and AGENTS.md.
- [ ] Parallel outputs are isolated and have an integrator.
- [ ] External and irreversible actions require human confirmation.
- [ ] I know how to disable or remove every extension.

## Sources and verification

- [OpenAI Docs: MCP](https://learn.chatgpt.com/docs/extend/mcp)
- [OpenAI Docs: Plugin architecture](https://developers.openai.com/plugins/concepts/plugins)
- [OpenAI Docs: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md)
- Last verified: 2026-09-22

[Previous](06-daily-workflows.md) · [Next: Case studies](08-case-studies.md)
