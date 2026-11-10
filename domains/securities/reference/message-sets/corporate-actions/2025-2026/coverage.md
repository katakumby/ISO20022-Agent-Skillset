---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
set_slug: "corporate-actions"
source_ids: ["src-000079", "src-000080", "src-000081", "src-000082", "src-000083", "src-000084", "src-000085", "src-000086", "src-000087", "src-000088", "src-000089", "src-000090", "src-000091", "src-000092", "src-000093", "src-000094"]
source_editions: ["2025-2026", "February 2026"]
message_ids: ["head.001.001.02", "seev.031.001.16", "seev.032.001.09", "seev.033.001.14", "seev.034.001.16", "seev.035.001.17", "seev.036.001.17", "seev.037.001.17", "seev.038.001.09", "seev.039.001.13", "seev.040.001.13", "seev.041.001.15", "seev.042.001.14", "seev.044.001.13"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Corporate Actions extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000079 | docx | extracted-needs-review | [Evidence](documents/src-000079/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000080 | pdf | extracted-needs-review | [Evidence](documents/src-000080/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000081 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000081/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000082 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.031.001.16/structure.md) | See declaration coverage |
| src-000083 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.032.001.09/structure.md) | See declaration coverage |
| src-000084 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.033.001.14/structure.md) | See declaration coverage |
| src-000085 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.034.001.16/structure.md) | See declaration coverage |
| src-000086 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.035.001.17/structure.md) | See declaration coverage |
| src-000087 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.036.001.17/structure.md) | See declaration coverage |
| src-000088 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.037.001.17/structure.md) | See declaration coverage |
| src-000089 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.038.001.09/structure.md) | See declaration coverage |
| src-000090 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.039.001.13/structure.md) | See declaration coverage |
| src-000091 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.040.001.13/structure.md) | See declaration coverage |
| src-000092 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.041.001.15/structure.md) | See declaration coverage |
| src-000093 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.042.001.14/structure.md) | See declaration coverage |
| src-000094 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.044.001.13/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
