---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
set_slug: "t2s-billing"
source_ids: ["src-000249", "src-000250", "src-000346", "src-000347", "src-000348"]
source_editions: ["december-2025"]
message_ids: ["camt.076.001.01", "camt.077.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S Billing extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000249 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.076.001.01/structure.md) | See declaration coverage |
| src-000250 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.077.001.01/structure.md) | See declaration coverage |
| src-000346 | pdf | extracted-needs-review | [Evidence](documents/src-000346/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000347 | docx | extracted-needs-review | [Evidence](documents/src-000347/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000348 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000348/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
