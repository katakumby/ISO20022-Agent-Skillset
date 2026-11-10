---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
set_slug: "t2s-collateral-management-reference-data"
source_ids: ["src-000279", "src-000280", "src-000281", "src-000282", "src-000283", "src-000299", "src-000306", "src-000307", "src-000353", "src-000354", "src-000355"]
source_editions: ["may-2025"]
message_ids: ["reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.044.001.01", "reda.075.001.01", "reda.077.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S CollateralManagementReferenceData extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000279 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.024.001.01/structure.md) | See declaration coverage |
| src-000280 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.025.001.01/structure.md) | See declaration coverage |
| src-000281 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.026.001.01/structure.md) | See declaration coverage |
| src-000282 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.027.001.01/structure.md) | See declaration coverage |
| src-000283 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.028.001.01/structure.md) | See declaration coverage |
| src-000299 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.044.001.01/structure.md) | See declaration coverage |
| src-000306 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.075.001.01/structure.md) | See declaration coverage |
| src-000307 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.077.001.01/structure.md) | See declaration coverage |
| src-000353 | docx | extracted-needs-review | [Evidence](documents/src-000353/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000354 | pdf | extracted-needs-review | [Evidence](documents/src-000354/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000355 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000355/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
