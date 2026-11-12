---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
set_slug: "post-trade-matching"
source_ids: ["src-000180", "src-000181", "src-000182", "src-000183", "src-000184", "src-000185", "src-000186", "src-000187"]
source_editions: ["2024-2025", "February 2025"]
message_ids: ["semt.023.001.02", "setr.027.001.05", "setr.029.001.02", "setr.030.001.03", "setr.044.001.04"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Post-Trade Matching extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000180 | docx | extracted-needs-review | [Evidence](documents/src-000180/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000181 | pdf | extracted-needs-review | [Evidence](documents/src-000181/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000182 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000182/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000183 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.023.001.02/structure.md) | See declaration coverage |
| src-000184 | xsd | extracted-needs-review | [Evidence](../../../messages/setr.027.001.05/structure.md) | See declaration coverage |
| src-000185 | xsd | extracted-needs-review | [Evidence](../../../messages/setr.029.001.02/structure.md) | See declaration coverage |
| src-000186 | xsd | extracted-needs-review | [Evidence](../../../messages/setr.030.001.03/structure.md) | See declaration coverage |
| src-000187 | xsd | extracted-needs-review | [Evidence](../../../messages/setr.044.001.04/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
