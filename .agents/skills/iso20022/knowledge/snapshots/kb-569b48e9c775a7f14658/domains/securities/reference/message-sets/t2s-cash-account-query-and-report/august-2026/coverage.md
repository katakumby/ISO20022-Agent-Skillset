---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
set_slug: "t2s-cash-account-query-and-report"
source_ids: ["src-000235", "src-000236", "src-000293", "src-000294", "src-000295", "src-000350", "src-000351", "src-000352"]
source_editions: ["august-2026"]
message_ids: ["acmt.025.001.02", "acmt.026.001.02", "reda.038.001.01", "reda.039.001.01", "reda.040.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S CashAccountQueryAndReport extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000235 | xsd | extracted-needs-review | [Evidence](../../../messages/acmt.025.001.02/structure.md) | See declaration coverage |
| src-000236 | xsd | extracted-needs-review | [Evidence](../../../messages/acmt.026.001.02/structure.md) | See declaration coverage |
| src-000293 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.038.001.01/structure.md) | See declaration coverage |
| src-000294 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.039.001.01/structure.md) | See declaration coverage |
| src-000295 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.040.001.01/structure.md) | See declaration coverage |
| src-000350 | docx | extracted-needs-review | [Evidence](documents/src-000350/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000351 | pdf | extracted-needs-review | [Evidence](documents/src-000351/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000352 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000352/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
