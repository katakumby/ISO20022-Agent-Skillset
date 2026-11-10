---
template: true
document_kind: extracted-table
review_status: template
domain: "{{domain}}"
message_ids: []
table_id: "{{table_id}}"
source_ids: []
source_editions: []
---

# {{table_id}} — {{source_table_title}}

> TEMPLATE ONLY: replace the placeholder table with every substantive source row, column, header, value, unit, and note.

## Source occurrences

| Source ID | Precise page / heading / table or worksheet range | Source title / caption | Canonical or duplicate occurrence |
| --- | --- | --- | --- |

Record all occurrences when deduplicating. For XLSX, include worksheet name and exact range. For PDF, record file page and printed page label when different.

## Context and representation

{{Explain how to read the table, including units, merged/multirow headers, blank-value meaning, and relevant number/date formats. Preserve codes and leading zeros.}}

{{If formulas matter, identify the source formulas and distinguish them from cached/displayed values. Flag missing or suspect cached values.}}

## Complete table

| {{source_column_heading}} | {{source_column_heading}} |
| --- | --- |
| {{source_value}} | {{source_value}} |

Replace the placeholder columns and row with the full table. Escape literal pipes, preserve multiline meaning, and do not summarize away rows.

## Source notes and footnotes

{{Preserve all notes and identify which rows, columns, or cells they qualify.}}

## Split-table continuity

{{For large tables, give part number, total parts, original row/range coverage, and previous/next links. Repeat headers and ensure no gap or overlap. Otherwise mark this section inapplicable.}}

## Review evidence

| Check | Result | Evidence / date |
| --- | --- | --- |
| Row and column coverage reconciled | {{result}} | {{evidence}} |
| Headers, values, units, and notes compared | {{result}} | {{evidence}} |
| Split boundaries or duplicate occurrences checked | {{result}} | {{evidence}} |

- Owning reference index: {{index_link}}
- Coverage item: {{coverage_link_and_item_id}}
- Original source / optional table crop: {{source_links}}
- Open issues: {{issue_links_or_reviewed_none}}

[Template guide](README.md)
