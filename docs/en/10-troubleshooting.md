<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 10 | Roadside Assistance: Troubleshooting

[简体中文](../zh-CN/10-troubleshooting.md) · [Home](../../README.en.md)

## Remember this

Diagnose one layer at a time: workspace and direct official access first, then client configuration, local gateway, extension, and task.

## General sequence

1. Record expected result, actual result, exact error, and time.
2. Record OS, architecture, tool version, and installation source.
3. Reproduce with the smallest non-sensitive task.
4. Remove newly added layers and return to the last working baseline.
5. Inspect logs for the relevant layer after redaction.
6. Change one variable at a time and record the result.

## Installation

### Microsoft Store will not download

Check network, Store sign-in, system update, and organizational policy. Try the `winget` path in OpenAI documentation. If using a community mirror, verify architecture, SHA256, manifest, and digital signature. Contact the administrator when policy blocks sideloading.

### MSIX installation fails

Common causes include x64/ARM64 mismatch, missing App Installer, signature problems, and device policy. Do not replace it with an unknown “patched” package.

### PowerShell blocks a script

Confirm source and necessity before changing anything. Consult Microsoft's execution-policy guidance; do not permanently disable all script protection for one tool.

## Workspace and permissions

- File not found: confirm the opened directory and allowed path.
- Read but not write: inspect current permission profile and output directory.
- Git integration unavailable: confirm native Windows Git, then restart the app.
- WSL confusion: separate agent environment, terminal environment, and physical file location.

## CC-Switch and CPA

- Switch has no effect: confirm target client, configuration file, restart requirement, and actual Base URL.
- 401/403: inspect authorization scope, expiry, and system time; never post the key publicly.
- 404: inspect Base URL path and model mapping.
- Connection refused: confirm CPA process, bind address, and port.
- Port conflict: identify the owning process before stopping anything.
- Complex failure: restore direct official access. If direct access also fails, solve account or client issues first.

## MCP and specialist software

- Server missing after install: save, restart as required, then inspect the MCP list and logs.
- Tool listed but unavailable: inspect process, working directory, environment, and authorization.
- Stata will not start: verify executable path, license, compatibility, and independent launch.
- Command runs but output is absent: inspect log, output path, and working-directory statements.

## Documents, spreadsheets, and slides

- “Done” but no file: request the exact relative or absolute path, then inspect the filesystem.
- Garbled text: check encoding, fonts, and target application.
- Spreadsheet totals differ: return to join keys, filters, missingness, and units; recalculate samples.
- Slides are misaligned: open every slide in the target PowerPoint version; generation logs are not visual review.

## Help request template

```text
OS and architecture:
Tool, version, installation source:
Workspace type (Windows/WSL):
Intended result:
Actual result:
Minimal reproduction:
Full redacted error:
Last working state:
Already tried:
```

## Mistakes I have made

- Upgrading the client, CC-Switch, CPA, and model together.
- Capturing only the final error line.
- Posting full configuration and tokens for help.
- Layering fixes without restoring a baseline.

## Checklist

- [ ] The issue is reproduced or disproved by a minimal task.
- [ ] One variable changes at a time.
- [ ] Logs and screenshots are redacted.
- [ ] I can return to direct access or the last working configuration.
- [ ] The original acceptance test passes, not merely the absence of an error.

## Sources and verification

- [OpenAI Docs: Windows app](https://learn.chatgpt.com/docs/windows/windows-app)
- [OpenAI Docs: MCP](https://learn.chatgpt.com/docs/extend/mcp)
- [Tool map](../../resources/tools.en.md)
- Last verified: 2026-09-22

[Previous](09-safety-and-ethics.md) · [Home](../../README.en.md)
