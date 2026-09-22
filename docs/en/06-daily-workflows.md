<!-- lang: en | status: synced | source_revision: v0.1.0 | last_updated: 2026-09-22 | last_verified: 2026-09-22 -->

# 06 | Run Errands: Files, Documents, Spreadsheets, and Slides

[简体中文](../zh-CN/06-daily-workflows.md) · [Home](../../README.en.md)

## Remember this

A general workflow is not “one sentence to finished product.” It is inventory, sample, batch, verify, and deliver—with visible artifacts at every stage.

## File organization

Ask for an inventory before defining classification and naming rules. A batch rename plan should include old path, new path, reason, collision, and execution status. Start with the [file-operation preview](../../templates/en/file-operation-preview.md).

```text
Scan input and produce rename-plan.csv without changing files.
Mark name collisions, unknown items, and possible duplicates as REVIEW; never overwrite them.
Wait for my approval. If later executed, produce rollback.csv.
```

## Documents and source synthesis

Separate three layers: factual extract, structured summary, and agent inference. Keep file, section, or page pointers for important claims. If a source cannot be found, write “unverified” rather than inventing a plausible citation.

Useful intermediate artifacts include a material inventory, theme table, disagreement table, report outline, and open-question list. Approve these before drafting a long report.

## Spreadsheets

An agent can normalize columns, dates, units, and missing-value markers; merge tables; and create summaries. Verification should cover:

- input and output row counts and unique keys;
- duplicate and unmatched records;
- changes in missingness;
- units, currencies, and date formats;
- at least five recalculated samples;
- formula ranges and aggregation definitions.

Use the [spreadsheet check](../../templates/en/spreadsheet-check.md). A polished chart is not evidence that the data are correct.

## Presentations

Start with the [presentation brief](../../templates/en/presentation-brief.md): audience, duration, purpose, required evidence, template, and exclusions. Work in three passes:

1. **Storyline:** title, main message, and evidence for each slide.
2. **Content:** tables, charts, citations, and speaker notes.
3. **Visual:** fonts, overflow, overlap, alignment, color, and projector readability.

Trace important numbers back to the spreadsheet or source. A generated `.pptx` is not a visual acceptance test.

## End-to-end office workflow

```text
Source material → thematic summary → report → CSV action table → slide storyline → human review
```

See [examples/office-workflow](../../examples/office-workflow/README.en.md). Intermediate artifacts are intentional: they reveal where an error entered the chain.

## Mistakes I have made

- Moving thousands of files without preview or collision policy.
- Citing a secondary summary as the original source.
- Checking only total rows after a join, not one-to-many matches.
- Reviewing a twenty-slide deck only as thumbnails.

## Checklist

- [ ] Batch file work has a preview and recovery map.
- [ ] Facts, summaries, and inferences remain distinguishable.
- [ ] Spreadsheet review covers keys, missingness, and sample recalculation.
- [ ] Slides move from storyline to content to visual inspection.
- [ ] Final deliverables trace back to inputs and intermediate artifacts.

## Sources and verification

- [OpenAI Docs: Work with files](https://learn.chatgpt.com/docs/work-with-files)
- Shared examples and templates in this repository
- Last verified: 2026-09-22

[Previous](05-learn-to-drive.md) · [Next: Extensions](07-upgrades-and-tools.md)
