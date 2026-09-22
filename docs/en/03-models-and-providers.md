<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 03 | Fuel the Vehicle: Models, Providers, and Cost

[简体中文](../zh-CN/03-models-and-providers.md) · [Home](../../README.en.md)

## Remember this

Not every trip needs the most expensive fuel. Difficulty, cost of error, latency, and budget should jointly determine the model.

## Why this matters

One agent may use several models, and the same model name may be offered by different providers. Looking only at the model label while ignoring quota, context, compatibility, and billing leads to confusing failures and expensive rework.

## Match fuel to the task

- **Light work:** classify files, normalize formatting, extract fields, draft an outline. Favor speed and cost.
- **Normal work:** synthesize documents, build spreadsheet formulas, design a presentation narrative. Balance capability, latency, and context.
- **Complex or high-stakes work:** research design, long execution chains, critical data interpretation. Favor reliable reasoning and add independent review.

A stronger model is not a trusted source. Numbers, citations, and policy claims still require evidence.

## Four access patterns

1. **Official account sign-in:** A straightforward way to start; current limits and features belong to the account page.
2. **Official API:** Metered under provider rules and suitable for programmatic or compatible-client access.
3. **Third-party API:** Convenient, but adds questions about data flow, logging, pricing, and continuity.
4. **Local model:** More direct control over data, with hardware, model-management, and evaluation costs.

A consumer subscription and an API are distinct products. Signing into an app does not imply API quota for arbitrary clients.

## Manage context and tokens

- Provide only material relevant to the current task.
- Store stable background in README, task brief, and handoff files.
- Let the agent inspect an index before opening everything.
- Start a new thread after a task instead of carrying permanent irrelevant history.
- Count failed retries and human rework; cheap requests can become an expensive workflow.

## Try it: build a task-tier table

Use the cost template to record task, input size, cost of error, candidate model, elapsed time, rework, and final cost. Build your own rule from repeated observations rather than copying a public leaderboard.

## Payment and subscription boundary

Regional availability, payment methods, currency conversion, tax, and renewal terms change. Prefer provider-supported channels. This repository does not teach account sharing, unknown keys, crypto funding, virtual-card workarounds, or geographic-restriction bypasses.

## Mistakes I have made

- Comparing request price without measuring rework.
- Assuming the same model label means an identical service across providers.
- Exposing a real key in a screenshot, issue, or sample.
- Switching sensitive work to an unknown provider without reviewing data flow.

## Checklist

- [ ] I know which access pattern I am using.
- [ ] I know where data is sent and how access is billed.
- [ ] Tasks are tiered by difficulty and cost of error.
- [ ] Samples contain placeholders only.
- [ ] Stronger models do not remove the review requirement.

## Sources and verification

- [OpenAI Docs: Best practices](https://learn.chatgpt.com/guides/best-practices)
- [Tool map](../../resources/tools.en.md)
- Last verified: 2026-09-22. Prices and account limits are deliberately not frozen here.

[Previous](02-choose-and-install.md) · [Next: Routing and gateways](04-routing-and-proxy.md)
