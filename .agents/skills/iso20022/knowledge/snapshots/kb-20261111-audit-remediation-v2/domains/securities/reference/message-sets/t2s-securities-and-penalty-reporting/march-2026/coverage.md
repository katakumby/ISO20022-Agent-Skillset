---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
set_slug: "t2s-securities-and-penalty-reporting"
source_ids: ["src-000308", "src-000309", "src-000310", "src-000318", "src-000319", "src-000374", "src-000375", "src-000376"]
source_editions: ["march-2026"]
message_ids: ["semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.040.001.01", "semt.044.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S SecuritiesAndPenaltyReporting extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000308 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.025.001.01/structure.md) | See declaration coverage |
| src-000309 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.026.001.01/structure.md) | See declaration coverage |
| src-000310 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.027.001.01/structure.md) | See declaration coverage |
| src-000318 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.040.001.01/structure.md) | See declaration coverage |
| src-000319 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.044.001.01/structure.md) | See declaration coverage |
| src-000374 | docx | extracted-needs-review | [Evidence](documents/src-000374/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000375 | pdf | extracted-needs-review | [Evidence](documents/src-000375/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000376 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000376/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
