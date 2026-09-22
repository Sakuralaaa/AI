# Glossary

[简体中文](glossary.md) · Last verified: 2026-09-22

| Term | Vehicle metaphor | Precise meaning |
|---|---|---|
| Agent framework / harness | Vehicle | Software that organizes the model, context, tool calls, execution loop, and user interface |
| Model | Fuel | The model that interprets input, reasons, and generates output; capability, speed, and cost vary |
| Provider | Fuel station | A service supplying model access, authentication, billing, and availability |
| Prompt | Destination and directions | The goal, context, constraints, and acceptance criteria supplied by the user |
| Context | Current map and cargo | Conversation, files, instructions, and tool results visible to the task |
| Token | Fuel-consumption unit | A unit used to meter model input and output; it is not the same as a word or a currency unit |
| API Key / OAuth | Fuel card or key | Authentication material that must be treated as secret |
| Base URL | Station entrance | The base address to which a compatible client sends API requests |
| CC-Switch | Fuel-path selector | A manager for provider, MCP, Skills, and related configuration across agent clients |
| CLIProxyAPI (CPA) | Local gateway | An independent community project exposing supported upstream access through compatible APIs; it is not a file format |
| MCP | Accessory port | A protocol and integration pattern connecting agents to external tools, services, and context |
| Skill | Driving playbook or mode | Reusable workflow guidance that may include scripts, templates, and references |
| Plugin | Upgrade kit | An installable package that may bundle Skills, MCP, UI, or other extensions; exact definitions vary by product |
| Sandbox | Guardrail | An execution boundary limiting commands, filesystem access, or network access |
| Approval | Human checkpoint | A request for user confirmation before a particular action |
| Failover | Alternate route | Trying another available service after the current one fails according to policy |

The metaphor builds intuition. For configuration and security decisions, rely on the precise definition and upstream documentation.
