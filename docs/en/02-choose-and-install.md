<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 02 | Choose and Install: Codex as the Main Route

[简体中文](../zh-CN/02-choose-and-install.md) · [Home](../../README.en.md)

## Remember this

Choose one vehicle that can get on the road reliably. This guide uses Codex; Claude Code and PI-Desktop are alternatives for genuinely different needs, not mandatory parallel installations.

## Three common choices

| Agent | Good fit | Character | Watch for |
|---|---|---|---|
| Codex | Users who want a desktop workspace for files, tasks, and review | Native Windows workflow, workspaces, sandbox, MCP, Skills, review | Use OpenAI documentation for current features and entry points |
| Claude Code | Terminal-first users or Anthropic-oriented workflows | Terminal-centric project execution and extensions | Follow Anthropic for installation and account eligibility |
| PI-Desktop | Users who want an independent desktop workspace for projects, models, and plugins | Local-first, model-agnostic, community-maintained desktop | It evolves quickly; verify installation, permissions, and features in the current README and Releases |

PI-Desktop is optional. It suits users comfortable following an early, fast-moving community project.

## Before installation

- Confirm Windows version and system type: x64 or ARM64.
- Determine whether the device is managed by a school or employer.
- Prepare a normal practice folder, not raw research data or a synchronized-drive root.
- Back up existing Codex state if applicable; the Windows-native default is `%USERPROFILE%\.codex`.
- Git helps with review and rollback. Install Node, Python, or .NET only when your work requires them.

## Official Codex installation

OpenAI's Windows documentation points to Microsoft Store and provides this command-line route:

```powershell
winget install --id 9PLM9XGG6VKS -s msstore
```

After sign-in, review the agent environment, terminal, sandbox, and approval settings. Keep the defaults for your first exercise.

## When Microsoft Store is unavailable

[Wangnov/codex-app-mirror](https://github.com/Wangnov/codex-app-mirror/releases) is a **community mirror, not an official OpenAI GitHub repository**. If you choose it:

1. Confirm x64 versus ARM64.
2. Download only from Releases or endpoints explicitly listed by the repository.
3. Compare the attached SHA256 list and manifest.
4. Inspect the Windows digital signature; stop if the origin or signature is unexpected.
5. If device policy blocks sideloading, contact the administrator rather than bypassing policy.

A mirror changes the download path. It does not bypass OS policy, sign-in, or product eligibility.

## Try it

Open a practice directory, use an approval-based permission setting, ask Codex for a read-only inventory, inspect the file view, and record the version, source, and date for future troubleshooting.

## Mistakes I have made

- Installing an ARM64 package on x64, or the reverse.
- Calling a community mirror an “official GitHub build.”
- Running the entire app permanently as administrator to fix one script.
- Assuming native Windows and WSL automatically share every configuration and session.

## Checklist

- [ ] Codex opens the practice folder and lists it correctly.
- [ ] I know my architecture, installation source, and state directory.
- [ ] Sandbox and approvals remain enabled by default.
- [ ] If I used a mirror, I checked hash, manifest, and digital signature.
- [ ] I did not bypass managed-device policy.

## Sources and verification

- [OpenAI Docs: Windows app](https://learn.chatgpt.com/docs/windows/windows-app)
- [Anthropic: Claude Code setup](https://docs.anthropic.com/en/docs/claude-code/getting-started)
- [PI-Desktop](https://github.com/vastsa/PI-Desktop)
- Last verified: 2026-09-22

[Previous](01-know-your-agent.md) · [Next: Models and providers](03-models-and-providers.md)
