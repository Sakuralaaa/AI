# AI Agent Road Guide

[简体中文](README.md) · Chinese is the source of truth for this repository.

> Think of an agent as a vehicle. Codex, Claude Code, and PI-Desktop are different vehicles, while the model is the fuel. Premium fuel can unlock stronger performance; ordinary fuel may still be ideal for lightweight work such as sorting files or changing formats. Your prompt is the destination, MCP is an accessory port, and you remain responsible for the route and the final inspection.

This is a practical guide for general users, graduate students, and knowledge workers. You do not need to learn programming first. Starting with Codex, the guide explains installation, models, providers, routing, permissions, files, spreadsheets, presentations, and connections to specialist software such as Stata.

## Pick a route

- **Brand new to agents:** Start with [Before you drive](docs/en/00-before-driving.md) and complete the ten-minute read-only exercise.
- **Codex is already installed:** Go to [Learn to drive](docs/en/05-learn-to-drive.md), then try the [daily workflows](docs/en/06-daily-workflows.md).
- **Interested in multiple providers or a local gateway:** Read [Models and providers](docs/en/03-models-and-providers.md) before [CC-Switch and CLIProxyAPI](docs/en/04-routing-and-proxy.md).
- **Only interested in research software:** Stata is a self-contained example in the [case studies](docs/en/08-case-studies.md).

## The map in one picture

```text
You (choose the destination and inspect the result)
│
├─ Codex / Claude Code / PI-Desktop     ← vehicle
│  ├─ files, terminal, browser           ← built-in capabilities
│  ├─ MCP / Skills                      ← accessory ports and playbooks
│  └─ permissions, sandbox, approvals    ← guardrails
│
└─ model configuration                   ← fuel path
   ├─ official sign-in or official API   ← official station
   ├─ CC-Switch                         ← configuration selector
   └─ CLIProxyAPI (optional)             ← local gateway
```

The metaphor is only an entry map. Technically, the agent harness organizes context, tools, and the execution loop; the model interprets and generates; the provider supplies access and billing.

## Chapters

1. [Before you drive](docs/en/00-before-driving.md)
2. [Know your agent](docs/en/01-know-your-agent.md)
3. [Choose and install](docs/en/02-choose-and-install.md)
4. [Models, providers, and cost](docs/en/03-models-and-providers.md)
5. [CC-Switch and CLIProxyAPI](docs/en/04-routing-and-proxy.md)
6. [Learn to drive Codex](docs/en/05-learn-to-drive.md)
7. [Everyday workflows](docs/en/06-daily-workflows.md)
8. [MCP, Skills, multi-agent work, and Computer Use](docs/en/07-upgrades-and-tools.md)
9. [Case studies](docs/en/08-case-studies.md)
10. [Safety, privacy, and academic integrity](docs/en/09-safety-and-ethics.md)
11. [Troubleshooting](docs/en/10-troubleshooting.md)

## Three rules

1. **Inspect before editing.** Ask the agent to inventory and plan before it changes an unfamiliar folder.
2. **Verify important results.** Recalculate samples, return to original sources, and inspect every slide. “Done” is not evidence.
3. **Use the narrowest sufficient permission.** Keep the sandbox and approvals by default; broaden access only when the need, trust boundary, and recovery path are clear.

The [tool map](resources/tools.en.md) marks each link as official, community-maintained, or a community mirror and records the verification date. This repository does not teach credential extraction, account sharing, payment workarounds, or geographic-restriction bypasses.

## Examples and templates

- [Shared examples](examples/): file organization, an office workflow, and Stata-MCP.
- [中文模板](templates/zh-CN/) / [English templates](templates/en/).
- [Glossary](resources/glossary.en.md): bilingual terminology, the vehicle metaphor, and precise definitions.

## V0.1 status

V0.1 includes the complete bilingual guide, templates, examples, and translation checks. Screenshots will be added from verified interfaces later; the current release is usable without them. See the [changelog](CHANGELOG.md).

## Disclaimer

This repository records personal learning and usage experience. It is not official support or academic, legal, investment, or payment advice. Review upstream documentation before acting. Confirm institutional and provider policies before handling sensitive data, installing extensions, or connecting gateways. See the [disclaimer](DISCLAIMER.en.md) and [security guide](SECURITY.en.md).
