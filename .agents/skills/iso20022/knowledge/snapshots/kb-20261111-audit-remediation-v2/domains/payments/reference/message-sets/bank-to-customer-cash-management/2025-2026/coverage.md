---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
set_slug: "bank-to-customer-cash-management"
source_ids: ["src-000004", "src-000005", "src-000006", "src-000007", "src-000008", "src-000009", "src-000010"]
source_editions: ["2025-2026", "March 2026"]
message_ids: ["camt.052.001.14", "camt.053.001.14", "camt.054.001.14", "camt.060.001.07"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Bank-to-Customer Cash Management extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000004 | docx | extracted-needs-review | [Evidence](documents/src-000004/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000005 | pdf | extracted-needs-review | [Evidence](documents/src-000005/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000006 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000006/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000007 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.052.001.14/structure.md) | See declaration coverage |
| src-000008 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.053.001.14/structure.md) | See declaration coverage |
| src-000009 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.054.001.14/structure.md) | See declaration coverage |
| src-000010 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.060.001.07/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
