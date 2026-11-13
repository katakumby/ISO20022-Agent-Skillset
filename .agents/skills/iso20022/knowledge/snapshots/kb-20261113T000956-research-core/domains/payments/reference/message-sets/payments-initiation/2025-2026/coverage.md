---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
set_slug: "payments-initiation"
source_ids: ["src-000173", "src-000174", "src-000175", "src-000176", "src-000177", "src-000178", "src-000179"]
source_editions: ["2025-2026", "March 2026"]
message_ids: ["pain.001.001.13", "pain.002.001.15", "pain.007.001.13", "pain.008.001.12"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Payments Initiation extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000173 | docx | extracted-needs-review | [Evidence](documents/src-000173/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000174 | pdf | extracted-needs-review | [Evidence](documents/src-000174/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000175 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000175/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000176 | xsd | extracted-needs-review | [Evidence](../../../messages/pain.001.001.13/structure.md) | See declaration coverage |
| src-000177 | xsd | extracted-needs-review | [Evidence](../../../messages/pain.002.001.15/structure.md) | See declaration coverage |
| src-000178 | xsd | extracted-needs-review | [Evidence](../../../messages/pain.007.001.13/structure.md) | See declaration coverage |
| src-000179 | xsd | extracted-needs-review | [Evidence](../../../messages/pain.008.001.12/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
