<!-- lang: en | status: synced | source_revision: v0.1.1 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 02 | Choose and Install: Codex as the Main Route

[简体中文](../zh-CN/02-choose-and-install.md) · [Home](../../README.en.md)

## Remember this

Install one reliable vehicle before changing fuel or adding accessories. This guide installs Codex Desktop from GitHub Releases and does not use Microsoft Store as an operational step.

## Why one main route matters

When several agents, providers, and gateways arrive at once, a failure is difficult to assign to the client, account, model, or network layer. First complete one accepted task in Codex; that gives you a baseline for later comparisons with Claude Code or PI-Desktop.

| Agent | Good fit | Character | Watch for |
|---|---|---|---|
| Codex | Users who want a desktop workspace for files, tasks, and review | Native Windows workflow, projects, sandbox, MCP, Skills, review | Main route here; use OpenAI documentation for feature and permission behavior |
| Claude Code | Terminal-first users or Anthropic-oriented workflows | Terminal-centric project execution and extensions | Follow Anthropic for installation and account eligibility |
| PI-Desktop | Users who want an independent desktop workspace for projects, models, and plugins | Local-first, model-agnostic community desktop | It evolves quickly; verify the current README and Releases |

PI-Desktop is an optional vehicle, not a dependency of this guide.

## Before installation

- On Windows, confirm OS version and x64 versus ARM64; on macOS, confirm Intel versus Apple Silicon.
- Determine whether the device is managed by a school or employer; policy may block sideloaded MSIX packages.
- Prepare a normal practice folder, not raw research data or a synchronized-drive root.
- If you have used Codex before, back up `%USERPROFILE%\.codex`.
- Git helps with review and rollback. Install Node, Python, or .NET only when your work requires them.

Check Windows architecture in PowerShell:

```powershell
Get-CimInstance Win32_OperatingSystem | Select-Object OSArchitecture
```

## Codex Desktop: preferred GitHub community mirror

Open the [latest Wangnov/codex-app-mirror release](https://github.com/Wangnov/codex-app-mirror/releases/latest). This is a community mirror, not an official OpenAI GitHub repository. The repository says it mirrors upstream installers without modification and includes checksums and a manifest with each release.

| System | Asset to choose |
|---|---|
| Windows x64 | The `.Msix` whose name contains `x64` |
| Windows ARM64 | The `.Msix` whose name contains `arm64` |
| Apple Silicon Mac | `Codex-mac-arm64.dmg` |
| Intel Mac | `Codex-mac-x64.dmg` |

### Windows: verify and install the MSIX

Download the installer, `SHA256SUMS.txt`, and the release manifest to one temporary directory. The path and filename below are placeholders; do not copy the version literally:

```powershell
Get-FileHash -Algorithm SHA256 -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
Get-AuthenticodeSignature -LiteralPath "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

Compare the first output exactly with the corresponding line in `SHA256SUMS.txt`, and confirm that the signature is not unexpected. Then install:

```powershell
Add-AppxPackage -Path "C:\Downloads\OpenAI.Codex_<version>_x64__2p2nqsd0c76g0.Msix"
```

You can also double-click the MSIX and use Windows App Installer. If Windows reports an administrator block, prohibited sideloading, or a disabled deployment service, contact the administrator on a managed device. Do not change policy or download a cracked build to work around the restriction.

### macOS: install the DMG

Download the DMG matching the processor, open it, and drag the app to `Applications`. If the first launch shows a security warning, verify provenance and file integrity before changing protection settings.

OpenAI's [official Windows documentation](https://learn.chatgpt.com/docs/windows/windows-app) remains authoritative for features, sign-in, sandboxing, and runtime behavior. Its current download path differs from the GitHub-direct route selected by this guide.

## Windows x64 portable fallback

[WSGsety/rebuild-codex-desktop Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases) publishes a portable Windows x64 ZIP:

1. Download `Codex-win-x64-<version>.zip` and `SHA256SUMS.txt`.
2. Verify the ZIP with `Get-FileHash`.
3. Extract it completely to an ordinary folder; do not run it from an archive preview.
4. Launch `ChatGPT.exe` in the extracted directory.

This project unpacks the upstream MSIX, patches `app.asar`, and rebuilds it. It is therefore an **unofficial community repack**, not a plain mirror or an official OpenAI portable edition. It currently supports Windows x64 only. Its supply-chain boundary is wider, so use it only when MSIX installation cannot work and you understand the distinction.

## CC-Switch: install from GitHub Releases

Install CC-Switch only when you need to manage several providers or client configurations. Open the [latest farion1231/cc-switch release](https://github.com/farion1231/cc-switch/releases/latest):

- On Windows, prefer the `.msi`; choose `Windows-Portable.zip` for a portable copy.
- On macOS, choose the `.dmg` and drag the app to `Applications`.
- On ARM64, select an artifact explicitly marked `arm64`.

On Windows, double-click the MSI or install it with a placeholder path:

```powershell
msiexec.exe /i "C:\Downloads\CC-Switch-<version>-Windows.msi"
```

Do not synchronize every setting on the first launch. Back up Codex configuration, add one independently verifiable provider, restart the client after switching if required, and complete a small non-sensitive task. See [Chapter 04](04-routing-and-proxy.md) for fields, restoration, and CPA integration.

## Try it: a safe first launch

1. Start Codex and sign in with your own authorized account, or configure an API you are entitled to use.
2. Inspect the agent environment, terminal, sandbox, and approval settings.
3. Keep default sandboxing and action approval.
4. Create and open a practice folder.
5. Prompt: “List the current directory without creating, changing, or deleting any file.”
6. Compare the output with the folder and record app version, installation source, architecture, and date.
7. Only when multiple providers are genuinely needed, install CC-Switch and practice one switch, verification, and restoration cycle.

## Mistakes I have made

- Installing an ARM64 package on x64, or the reverse.
- Calling a community mirror or repack an “official GitHub build.”
- Installing a third-party artifact without checking hash, manifest, and signature.
- Running a portable app inside the archive viewer, so resource files appear missing.
- Running the entire app permanently as administrator to fix one script.
- Configuring CC-Switch, CPA, and several models before direct access works.

## Expected result

Codex opens the practice folder and lists its files accurately without writing anything. You know the package source, device architecture, app version, and configuration directory. If CC-Switch is installed, you can restore the original direct configuration.

## Checklist

- [ ] The asset matches the device architecture.
- [ ] The community mirror was checked against SHA256, manifest, and digital signature.
- [ ] The portable fallback is correctly identified as a Windows x64 community repack.
- [ ] Codex completes a read-only directory inventory.
- [ ] Sandbox and approvals remain enabled by default.
- [ ] No managed-device policy was bypassed.
- [ ] If CC-Switch is in use, the original configuration is backed up and restorable.

## Sources and verification

- [OpenAI Docs: Windows app](https://learn.chatgpt.com/docs/windows/windows-app)
- [Wangnov/codex-app-mirror Releases](https://github.com/Wangnov/codex-app-mirror/releases/latest) (community mirror)
- [WSGsety/rebuild-codex-desktop Releases](https://github.com/WSGsety/rebuild-codex-desktop/releases) (community repack)
- [CC-Switch Releases](https://github.com/farion1231/cc-switch/releases/latest) (community project)
- [Anthropic: Claude Code setup](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- [PI-Desktop](https://github.com/vastsa/PI-Desktop) (community project)
- Last verified: 2026-09-22

[Previous](01-know-your-agent.md) · [Next: Models and providers](03-models-and-providers.md)
