<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 08 | Case Studies: Run the Method End to End

[简体中文](../zh-CN/08-case-studies.md) · [Home](../../README.en.md)

## Remember this

The value of a case study is not the final file. It is the visible chain of inputs, transformations, checks, and human decisions.

## Case A: source material to briefing

The goal is an auditable briefing pack:

```text
Material inventory
→ sourced thematic summary
→ report draft
→ CSV action table
→ 12–15 slide storyline
→ factual and visual review
```

Keep sources separate from summaries, retain a pointer for every important claim, approve the report before designing slides, and trace slide numbers back to CSV or source. See [office-workflow](../../examples/office-workflow/README.en.md).

A useful opening prompt is:

```text
Inventory input first; do not draft the report.
Produce a material list, citation boundaries, missing information, and a processing plan.
Every factual claim needs a source file pointer. Mark your inference separately.
```

## Case B: Stata-MCP

Stata demonstrates how MCP connects specialist software. It is not the guide's main track. The example uses synthetic panel data and no real personal records.

1. Prepare a valid Stata installation and license.
2. Follow current [MCP-for-Stata](https://github.com/SepineTam/mcp-for-stata) instructions to register it with Codex.
3. Restart the client and use the project's current test to confirm the connection.
4. Import [synthetic_panel.csv](../../examples/stata-mcp/synthetic_panel.csv).
5. Ask the agent to audit variables, missingness, unique keys, and descriptive statistics first.
6. Run [analysis.do](../../examples/stata-mcp/analysis.do), saving logs, tables, and figures to a separate output directory.
7. Use the [verification checklist](../../examples/stata-mcp/verification.en.md) for sample size, model specification, coefficients, and standard errors.
8. Draft prose or a slide storyline only after verification.

Do not translate statistical significance automatically into causality, and do not repeatedly vary samples and models solely to obtain significance. The method transfers to R, Python, or SPSS: replace the specialist tool, keep the audit, reproducible script, and human review.

## Case C: batch file organization

The shared folder includes [manifest-before.csv](../../examples/file-organization/manifest-before.csv) and an illustrative [rename-plan.csv](../../examples/file-organization/rename-plan.csv). Practice in three passes: plan without editing, review collisions and unknowns, then execute on copies and produce `rollback.csv`.

Never apply the sample paths directly to real material. Generate a new mapping from the actual inventory.

## Mistakes I have made

- Keeping only the final deck and losing the origin of a number.
- Accepting an interpretation because a Stata command ran without opening the log.
- Treating conclusions from synthetic data as research findings.
- Executing a rename plan that still contained collisions.

## Checklist

- [ ] Each case has input, plan, intermediate artifact, output, and review.
- [ ] Claims in the office case trace to source material.
- [ ] The Stata case preserves scripts and logs and receives human statistical review.
- [ ] The file case runs on copies and produces a recovery map.
- [ ] No case contains real credentials or sensitive data.

## Sources and verification

- [MCP-for-Stata](https://github.com/SepineTam/mcp-for-stata)
- Synthetic and demonstration material under `examples/`
- Last verified: 2026-09-22

[Previous](07-upgrades-and-tools.md) · [Next: Safety](09-safety-and-ethics.md)
