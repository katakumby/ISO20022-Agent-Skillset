---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
set_slug: "t2s-collateral-reporting"
source_ids: ["src-000259", "src-000260", "src-000356", "src-000357", "src-000358"]
source_editions: ["march-2024"]
message_ids: ["colr.001.001.02", "colr.002.001.02"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S CollateralReporting extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000259 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.001.001.02/structure.md) | See declaration coverage |
| src-000260 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.002.001.02/structure.md) | See declaration coverage |
| src-000356 | docx | extracted-needs-review | [Evidence](documents/src-000356/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000357 | pdf | extracted-needs-review | [Evidence](documents/src-000357/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000358 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000358/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
