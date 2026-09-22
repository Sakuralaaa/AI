# Tool map

[简体中文](tools.md) · Last verified: 2026-09-22

“Official” means the product or project maintainer's channel. “Community project” means an independent open-source project. Neither a “community mirror” nor a “community repack” is an official distribution channel.

| Tool | Source type | Role in this guide | Entry point | Check before use |
|---|---|---|---|---|
| ChatGPT desktop app / Codex | Official OpenAI | Feature, sign-in, and permission reference for the main agent workspace | [Windows documentation](https://learn.chatgpt.com/docs/windows/windows-app) | This guide installs through the community GitHub channels below; do not label them as official OpenAI releases |
| Codex App Mirror | Community mirror | Preferred GitHub-direct source in this guide; Windows MSIX and macOS DMG | [Latest Release](https://github.com/Wangnov/codex-app-mirror/releases/latest) | Not an OpenAI repository; verify architecture, SHA256, manifest, and digital signature |
| Rebuild Codex Desktop | Community repack | Portable Windows x64 ZIP fallback | [GitHub Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases) | Unpacked, patched, and repacked; Windows x64 only, with a wider supply-chain boundary than the mirror |
| Claude Code | Official Anthropic | Alternative agent vehicle | [Official documentation](https://docs.anthropic.com/en/docs/claude-code/getting-started) | Follow Anthropic for installation, sign-in, regional, and plan eligibility |
| PI-Desktop | Community project | Extensible, model-agnostic desktop agent workspace | [vastsa/PI-Desktop](https://github.com/vastsa/PI-Desktop) | It is evolving quickly; confirm downloads, permissions, and features in Releases and README |
| CC-Switch | Community project | Manage providers, MCP, Skills, and configuration across agents | [Latest Release](https://github.com/farion1231/cc-switch/releases/latest) | Prefer MSI on Windows and DMG on macOS; back up configuration before switching |
| CLIProxyAPI | Community project | Optional local compatible-API gateway | [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) | Bind locally by default; do not expose management interfaces or credentials to the public internet |
| Sub2API | Community project | Comparison point for team, user, and billing gateways | [Wei-Shaw/sub2api](https://github.com/Wei-Shaw/sub2api) | This guide does not cover commercial deployment; operators own compliance and data responsibilities |
| MCP-for-Stata | Community project | Specialist-software case study | [SepineTam/mcp-for-stata](https://github.com/SepineTam/mcp-for-stata) | Not affiliated with StataCorp; users supply Stata and a valid license |

## Update policy

- Avoid claims such as “always latest” or “official GitHub mirror.”
- When an entry point, install command, or project owner changes, update this table before the chapter text.
- If maintenance status cannot be confirmed, mark it “verification pending” rather than guessing a replacement.
