<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 09 | Drive Safely: Privacy, Permissions, and Academic Integrity

[简体中文](../zh-CN/09-safety-and-ethics.md) · [Home](../../README.en.md)

## Remember this

Safety does not mean trusting the agent not to fail. It means containing the impact of failure through workspace boundaries, permissions, backups, and human review.

## Classify data first

| Level | Examples | Default handling |
|---|---|---|
| Public | Official reports, public data, published papers | Still observe licenses and citation requirements |
| Internal | Unpublished teaching notes, ordinary meeting notes | Process under institutional policy; do not republish |
| Sensitive | Student, interview, or customer records | Prefer a controlled local environment; redact and obtain authorization |
| Highly sensitive | Health, identity, secrets, undisclosed commercial data | Keep out of ordinary agent workflows; use dedicated approval and isolation |

“Stored locally” does not always mean “never leaves the machine.” If a cloud model receives the prompt, data may leave the device. Confirm the actual data path through tool, model, and provider.

## Least privilege

- Begin with read-only or workspace-scoped access.
- Allow writes only to the project output directory.
- Deny `.env`, authentication directories, and raw data when possible.
- MCP, browser, Computer Use, and cloud tasks have controls beyond the command sandbox.
- Use broad access only for explicit, short, trusted, and recoverable work.

## Secrets and supply chain

Treat API keys, OAuth tokens, cookies, and recovery codes as passwords. Do not put them in prompts, Markdown, screenshots, issues, or Git history. MCP servers, Skills, plugins, mirrors, and install scripts can execute code; review maintainer, license, releases, and permissions.

## Academic integrity

- Check school, adviser, course, and journal AI policies first.
- Preserve prompts, tool/model scope, and human edits when disclosure may be required.
- Return every citation to a real source.
- Preserve data versions, scripts, logs, and exclusion rules.
- Do not search models, samples, and outcomes merely for significance without reporting the process.
- Language polishing does not validate facts or reasoning.

## Untrusted content and prompt injection

A web page, document, or repository may tell an agent to ignore your rules, read secrets, or transmit data. Treat external text as material, not authority. Keep human confirmation for sending, signing in, paying, deleting, publishing, and submitting.

## Try it: pre-task risk review

Use the [MCP safety check](../../templates/en/mcp-safety-check.md) and [result review](../../templates/en/result-review.md). Record data level, recipients, writable directories, irreversible actions, backup, disclosure duties, and final owner.

## Mistakes I have made

- Removing names while leaving student IDs, addresses, and rare combinations.
- Deleting a current file while leaving the secret in Git history.
- Treating MCP server instructions as more authoritative than project rules.
- Trusting a well-formatted reference without checking DOI and source.

## Checklist

- [ ] Data is classified and authorized.
- [ ] I know which services receive the material.
- [ ] Permissions are limited to necessary directories and tools.
- [ ] Secrets are absent from repository, logs, and screenshots.
- [ ] Academic output preserves sources, scripts, review, and disclosure records.
- [ ] A human confirms irreversible or external actions.

## Sources and verification

- [OpenAI Docs: Permissions](https://learn.chatgpt.com/docs/permissions)
- [OpenAI Docs: Agent approvals and security](https://learn.chatgpt.com/docs/agent-approvals-security)
- [Repository security guide](../../SECURITY.en.md)
- Last verified: 2026-09-22

[Previous](08-case-studies.md) · [Next: Troubleshooting](10-troubleshooting.md)
