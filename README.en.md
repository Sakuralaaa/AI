# AI Agent Road Guide

[简体中文](README.md) · Chinese is the source of truth for this repository.

> Think of an agent as a vehicle. Codex, Claude Code, and PI-Desktop are different vehicles; the model is the fuel. Better fuel can unlock more speed and reliability, while ordinary fuel may be perfectly adequate for lightweight jobs such as organizing files or changing formats. Your prompt is the destination, MCP is an accessory port, and you remain responsible for the route and the final inspection.

This is a practical guide for general users, graduate students, and knowledge workers. You do not need to learn programming or install every tool before starting. The README tells the full story; follow the chapter links only when you need step-by-step operation, configuration detail, or troubleshooting.

## The short answer: a reliable starter stack

```text
Codex Desktop                              ← install one vehicle first
  └─ OpenAI sign-in or an authorized API    ← establish one verifiable fuel path
      └─ CC-Switch (optional)                ← add a selector only for multiple providers
          └─ CLIProxyAPI (optional)           ← add only for compatibility or gateway needs
              └─ MCP / Skills (advanced)      ← add accessories after the main route works
```

For your first run, install only **Codex Desktop**, retain sandboxing and approvals, and complete a small task through an official sign-in or a trusted API. CC-Switch, CLIProxyAPI—CPA in this guide—MCP, and multi-agent workflows are not prerequisites.

## Understand the vehicle, fuel, and fuel path

| Metaphor | Technical term | Responsibility | Common choices |
|---|---|---|---|
| Vehicle | Agent client or harness | Organizes context, calls tools, executes work, and presents changes | Codex, Claude Code, PI-Desktop |
| Fuel | Model | Interprets instructions, reasons, and generates content or code | Models with different capability, price, and context limits |
| Fuel station | Model provider | Supplies access, authentication, quota, and billing | Official sign-in, official API, compliant third-party provider |
| Fuel-path selector | CC-Switch | Stores and switches provider and client configuration | Useful when one client has several legitimate providers |
| Local transfer station | CLIProxyAPI | Exposes supported upstreams through compatible APIs | Useful for protocol adaptation or one local endpoint |
| Accessory port | MCP | Connects the agent to files, browsers, or specialist software | Install one at a time for a real task |
| Driver's manual | Skills / `AGENTS.md` | Stores reusable workflows and project rules | Acceptance criteria, naming rules, operation boundaries |

The metaphor creates intuition, but the distinction matters: **a stronger model does not automatically make every agent better**. The same model behaves differently when the tools, context management, permissions, and execution loop change. The same vehicle also changes in speed, accuracy, and cost when you change its fuel.

## Core installation and basic setup

This guide installs desktop tools **directly from GitHub Releases and does not use Microsoft Store or `winget ... -s msstore` as a tutorial step**. The provenance still matters: neither Codex download repository below is an official OpenAI GitHub distribution channel. We use OpenAI documentation as the reference for features, sign-in, sandboxing, and permission behavior.

### 1. Codex Desktop: preferred community mirror

Preferred download: [latest Wangnov/codex-app-mirror release](https://github.com/Wangnov/codex-app-mirror/releases/latest)

Choose the asset for your machine:

- Windows x64: the `.Msix` whose name contains `x64`.
- Windows ARM64: the `.Msix` whose name contains `arm64`.
- Apple Silicon Mac: `Codex-mac-arm64.dmg`.
- Intel Mac: `Codex-mac-x64.dmg`.

On Windows, check the architecture in PowerShell first:

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object OSArchitecture
```

Download `SHA256SUMS.txt` from the same release and verify the package. The path and version below are placeholders:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
Get-AuthenticodeSignature -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

After the hash matches the release and the signature is not unexpected, install it:

```powershell
Add-AppxPackage -Path "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

On macOS, open the matching DMG and drag the application to `Applications`. Do not obtain a supposed “patched” copy from an unknown download site.

> This is a **community mirror**. The repository says it mirrors upstream installers without modifying them and publishes checksums and a manifest. You should still verify the file yourself. If a school or employer blocks sideloaded MSIX packages, contact the administrator instead of bypassing policy.

### 2. Codex Desktop: Windows x64 portable fallback

Fallback: [WSGsety/rebuild-codex-desktop Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases)

This project publishes a portable Windows x64 ZIP. Download `Codex-win-x64-<version>.zip` and `SHA256SUMS.txt`, compare the hash, extract the archive, and run `ChatGPT.exe` from the extracted directory.

The difference from the preferred mirror is important: this is an **unofficial repack**, produced by unpacking the upstream MSIX, patching `app.asar`, and building a portable ZIP. It currently supports neither Windows ARM64 nor macOS. Its supply-chain boundary is wider, so treat it as a fallback when MSIX installation cannot work—not as an “official portable build.”

### 3. Keep first-run configuration minimal

1. Sign in with your own authorized account or configure an API you are entitled to use.
2. Create a practice folder; do not begin with raw research data, financial files, or a sync-drive root.
3. Keep sandboxing and action approval enabled. Do not use full access permanently to save one confirmation.
4. Choose a familiar terminal; PowerShell is a reasonable default for Windows beginners.
5. Ask Codex to **list the directory without making changes** and confirm that workspace access behaves as expected.

See [Choose and install](docs/en/02-choose-and-install.md) for architecture checks, installation, hash verification, portable-build tradeoffs, and the complete first-run checklist.

### 4. CC-Switch: install only when you need several fuel paths

Download: [latest farion1231/cc-switch release](https://github.com/farion1231/cc-switch/releases/latest)

- Windows: prefer the `.msi`; choose `Windows-Portable.zip` if you need the portable build.
- macOS: download the `.dmg` and drag the app to `Applications`.
- On ARM64, select an asset explicitly marked `arm64`.

On Windows, double-click the MSI or use this placeholder path:

```powershell
msiexec.exe /i "C:\Downloads\CC-Switch-<version>-Windows.msi"
```

Before the first switch, back up `%USERPROFILE%\.codex` and the target client's configuration. Add only one independently verifiable provider and learn the field shape with placeholders:

```text
Name: My Provider
Base URL: https://example.invalid/v1
API Key: YOUR_API_KEY
Model: YOUR_MODEL_NAME
```

Restart the client if needed, run a small non-sensitive task, and then practice restoring the original direct configuration. Do not synchronize every MCP server, Skill, and prompt on the first attempt. See [Switch the fuel path](docs/en/04-routing-and-proxy.md) for the full request path and the distinctions among CC-Switch, CPA, and Sub2API.

### Four common installation problems

| Symptom | Check first | Do not |
|---|---|---|
| MSIX will not install | x64 versus ARM64, App Installer, signature, device policy | Download an unknown modified package |
| Administrator-blocked message | Whether the device is managed and sideloading is prohibited | Bypass organizational policy |
| Portable build will not start | Full extraction, x64 hardware, and the exact security alert | Disable all endpoint protection |
| CC-Switch change has no effect | Target client, file changed, Base URL, restart requirement | Change the gateway, model, and several configs together |

Continue with [Troubleshooting](docs/en/10-troubleshooting.md) when the quick checks are not enough.

## Choose fuel: models and providers

Ask three questions first: how hard is the task, how costly is an error, and may the provider receive this data?

- Renaming files, reformatting, and initial classification: an ordinary model is often enough; permissions and recovery matter more.
- Cross-file reasoning, complex spreadsheets, and long-document synthesis: a more reliable model and larger context may help, but sampling and recalculation remain mandatory.
- Research conclusions, public figures, contracts, or high-risk decisions: the model is only an assistant; return to the source, formulas, and human review.

Chat subscriptions, API quotas, and third-party resale are usually separate billing systems. Do not assume that a chat subscription includes every API. Establish an official sign-in or official API baseline before adding CC-Switch or CPA, so failures can be assigned to the correct layer. See [Models, providers, and cost](docs/en/03-models-and-providers.md).

## The actual workflow: from request to accepted result

Using an agent is not “send one sentence, then believe it.” A stable workflow has six stages:

```text
choose workspace → write task brief → ask for an inventory → approve plan and permissions
                 → execute in small steps and inspect changes → verify against acceptance criteria
```

Copy this minimal task brief to start:

```text
Goal: Organize the files in the practice folder into type-based subfolders.
Input: The current directory only; do not access anything outside it.
Output: First provide a dry-run list and old-to-new path mapping. Wait before execution.
Constraints: Do not delete or overwrite. Stop and report filename collisions.
Acceptance: File count is unchanged, every old path has a new path, and a rollback map exists.
Authorization: This turn permits reading and planning only; do not move files yet.
```

Begin with a read-only inventory or dry run. Once the plan is correct, grant explicit execution permission; afterward, inspect the diff, file counts, and recovery path. See [Learn to drive](docs/en/05-learn-to-drive.md) for planning, project memory, and handoffs, or copy an [English template](templates/en/).

## What agents can do in daily work

| Scenario | Good agent work | Your acceptance work |
|---|---|---|
| File organization | Inventory, classification proposal, rename dry run, rollback map | Count, collisions, omissions, recoverability |
| Reports | Outline, consistent formatting, source summaries, draft synthesis | Return citations to originals and verify facts |
| Spreadsheets | Cleaning plan, formula drafts, joins, anomaly checks | Units, keys, missingness, sampled recalculation |
| Presentations | Narrative, slide brief, asset list, first draft | Visual inspection, figures, fonts, speaking logic |
| Specialist software | Invoke authorized workflows through MCP | Software version, logs, parameters, result review |

Stata-MCP is one example of connecting specialist software, not a dependency of the guide. The [case studies](docs/en/08-case-studies.md) cover a source-to-report/spreadsheet/presentation flow, bulk file organization, and Stata-MCP on synthetic data.

## When to add MCP, Skills, and multiple agents

- **MCP:** Install only when a real task needs the external tool; inspect permissions, maintenance, logs, and removal first.
- **Skills:** When a workflow repeats, capture the steps and acceptance criteria as a reusable driver's manual.
- **Multiple agents:** Parallelize only when the work has clean boundaries and mergeable outputs; coordination can otherwise cost more than it saves.
- **Computer Use:** Useful for interfaces without APIs, but it requires more state confirmation, visual evidence, and human review.

See [Upgrade the vehicle](docs/en/07-upgrades-and-tools.md) for details.

## Choose your route

- **Brand new to agents:** Complete the [ten-minute read-only exercise](docs/en/00-before-driving.md), then follow the installation path on this page.
- **Codex already works:** Continue with [Learn to drive](docs/en/05-learn-to-drive.md), then try the [daily workflows](docs/en/06-daily-workflows.md).
- **You need multiple models:** Read [Models and providers](docs/en/03-models-and-providers.md) for billing and data boundaries before configuring [CC-Switch or CPA](docs/en/04-routing-and-proxy.md).
- **Something failed:** Do not stack fixes; use [Troubleshooting](docs/en/10-troubleshooting.md) and isolate one layer at a time.
- **You only care about research software:** Go directly to the Stata-MCP entry in the [case studies](docs/en/08-case-studies.md); it does not run through the rest of the guide.

## Detailed chapters

1. [Before you drive](docs/en/00-before-driving.md)
2. [Know your agent](docs/en/01-know-your-agent.md)
3. [Choose and install Codex, the portable fallback, and CC-Switch](docs/en/02-choose-and-install.md)
4. [Models, providers, and cost](docs/en/03-models-and-providers.md)
5. [CC-Switch and CLIProxyAPI](docs/en/04-routing-and-proxy.md)
6. [Learn to drive Codex](docs/en/05-learn-to-drive.md)
7. [Everyday workflows](docs/en/06-daily-workflows.md)
8. [MCP, Skills, multi-agent work, and Computer Use](docs/en/07-upgrades-and-tools.md)
9. [Case studies](docs/en/08-case-studies.md)
10. [Safety, privacy, and academic integrity](docs/en/09-safety-and-ethics.md)
11. [Troubleshooting](docs/en/10-troubleshooting.md)

## Three boundaries

1. **Inspect before editing.** Inventory and plan before changing an unfamiliar folder in bulk.
2. **Verify important results.** Recalculate samples, return citations to original sources, and inspect every slide. “Done” is not evidence.
3. **Use the narrowest sufficient permission.** Keep sandboxing and approvals; broaden access only when the need, trust boundary, and recovery path are clear.

## Source labels and scope

- **Official:** Documentation and downloads published by the product or project maintainer.
- **Community project:** Independently maintained open-source software, without implied support from OpenAI, Anthropic, or StataCorp.
- **Community mirror:** A third-party copy of upstream installers; signatures, hashes, and manifests still require verification.
- **Community repack:** An artifact redistributed after unpacking and modification; its supply-chain boundary is wider than a mirror's.

The [tool map](resources/tools.en.md) records every entry point, source type, and verification date. This repository does not teach credential extraction, account sharing, payment workarounds, or geographic-restriction bypasses.

## Examples, templates, and release status

- [Shared examples](examples/): file organization, source-to-presentation work, and Stata-MCP.
- [中文模板](templates/zh-CN/) / [English templates](templates/en/): task briefs, acceptance sheets, presentation briefs, and more.
- [Glossary](resources/glossary.en.md): bilingual terminology, vehicle metaphors, and precise definitions.
- [Security guide](SECURITY.en.md) / [disclaimer](DISCLAIMER.en.md).

V0.1 includes the complete bilingual guide, templates, examples, and translation checks. Screenshots will be added after their real interfaces are verified; the current guide is complete without them. See the [changelog](CHANGELOG.md).

This repository records personal learning and usage experience. It is not official support or academic, legal, investment, or payment advice. Tools change quickly, so verify upstream documentation and applicable school, employer, and provider policies before acting.
