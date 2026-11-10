---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
set_slug: "t2s-administration"
source_ids: ["src-000237", "src-000238", "src-000239", "src-000343", "src-000344", "src-000345"]
source_editions: ["march-2024"]
message_ids: ["admi.005.001.02", "admi.006.001.01", "admi.007.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S Administration extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000237 | xsd | extracted-needs-review | [Evidence](../../../messages/admi.005.001.02/structure.md) | See declaration coverage |
| src-000238 | xsd | extracted-needs-review | [Evidence](../../../messages/admi.006.001.01/structure.md) | See declaration coverage |
| src-000239 | xsd | extracted-needs-review | [Evidence](../../../messages/admi.007.001.01/structure.md) | See declaration coverage |
| src-000343 | docx | extracted-needs-review | [Evidence](documents/src-000343/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000344 | pdf | extracted-needs-review | [Evidence](documents/src-000344/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000345 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000345/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../tracking/issues.md) · [Set index](index.md)
