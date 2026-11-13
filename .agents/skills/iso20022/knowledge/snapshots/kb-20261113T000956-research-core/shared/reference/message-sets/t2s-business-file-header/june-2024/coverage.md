---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "shared"
message_set: "T2S BusinessFileHeader"
set_slug: "t2s-business-file-header"
source_ids: ["src-000261", "src-000349"]
source_editions: ["june-2024"]
message_ids: ["head.002.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S BusinessFileHeader extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000261 | xsd | extracted-needs-review | [Evidence](../../../messages/head.002.001.01/structure.md) | See declaration coverage |
| src-000349 | pdf | extracted-needs-review | [Evidence](documents/src-000349/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../tracking/issues.md) · [Set index](index.md)
