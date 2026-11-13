---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
set_slug: "business-application-header"
source_ids: ["src-000011", "src-000013"]
source_editions: ["Version 4 March 2024", "march-2024"]
message_ids: ["head.001.001.04"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Business Application Header extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000011 | pdf | extracted-needs-review | [Evidence](documents/src-000011/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000013 | xsd | extracted-needs-review | [Evidence](../../../messages/head.001.001.04/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../tracking/issues.md) · [Set index](index.md)
