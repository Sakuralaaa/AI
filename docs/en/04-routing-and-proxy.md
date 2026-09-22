<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 04 | Switch the Fuel Path: CC-Switch and CLIProxyAPI

[简体中文](../zh-CN/04-routing-and-proxy.md) · [Home](../../README.en.md)

## Remember this

CC-Switch mainly manages client configuration; CLIProxyAPI mainly provides a local compatible gateway. Make the official direct path work before adding layers.

## Why this matters

With several agents or providers, manually editing JSON, TOML, and environment variables is error-prone. CC-Switch provides visual configuration management. CLIProxyAPI—abbreviated CPA in this guide—can expose supported upstream access through compatible APIs. They can work together or separately.

```text
Agent clients
   ↓ read configuration
CC-Switch (store, switch, and synchronize configuration)
   ↓ optional Base URL
CLIProxyAPI (local compatible-API gateway)
   ↓
Upstream services you are authorized to use
```

CPA here is a project abbreviation, not a `.cpa` file format.

## Safe CC-Switch onboarding

1. Download from channels declared by [farion1231/cc-switch](https://github.com/farion1231/cc-switch).
2. Back up client configuration before the first switch.
3. Add one provider you can verify independently.
4. Learn the shape using placeholders:

```text
Name: My Provider
Base URL: https://example.invalid/v1
API Key: YOUR_API_KEY
Model: YOUR_MODEL_NAME
```

5. Restart the client if required and run a short, non-sensitive connectivity task.
6. Record which files changed and practice restoring the original configuration.

CC-Switch can also manage MCP, Skills, and prompts. Start with one client instead of synchronizing everything at once.

## Safe CLIProxyAPI principles

- Read the current documentation and Releases at [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI).
- Bind to loopback, such as `127.0.0.1`, for the first setup; do not publish it directly.
- Use a dedicated local client key and keep upstream authentication out of tutorials, logs, and screenshots.
- Identify configuration, logs, model mappings, shutdown, upgrade, and rollback before enabling it.
- Connect only accounts or APIs you are authorized to use under their terms.

This repository does not cover credential extraction, account sharing, or restriction bypasses. Follow current upstream configuration documentation because formats change.

## Where Sub2API fits

[Sub2API](https://github.com/Wei-Shaw/sub2api) focuses more on multi-user access, key distribution, billing, and operations. A local personal workflow does not need databases and a public service merely because they offer more features. This guide compares the concept but does not teach commercial deployment.

## Try it: add one layer at a time

1. Confirm an official sign-in or official API can complete a short task without CC-Switch or CPA.
2. Add only CC-Switch, switch once, then restore.
3. Add local CPA only if you have a concrete need; keep loopback binding.
4. Record request path, configuration file, and log location after each layer.

## Mistakes I have made

- Debugging CC-Switch, CPA, and model mapping before direct access worked.
- Adding or omitting a Base URL path segment and receiving a 404.
- Exposing a local management port to the public internet.
- Forgetting how to restore the client's direct configuration.

## Checklist

- [ ] I can draw my request path.
- [ ] I know which client files CC-Switch changes.
- [ ] CPA is local or on a controlled network; management is not public.
- [ ] I can restore direct access.
- [ ] Samples and logs contain no real credentials.

## Sources and verification

- [CC-Switch](https://github.com/farion1231/cc-switch)
- [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI)
- [Sub2API](https://github.com/Wei-Shaw/sub2api)
- Last verified: 2026-09-22

[Previous](03-models-and-providers.md) · [Next: Learn to drive](05-learn-to-drive.md)
