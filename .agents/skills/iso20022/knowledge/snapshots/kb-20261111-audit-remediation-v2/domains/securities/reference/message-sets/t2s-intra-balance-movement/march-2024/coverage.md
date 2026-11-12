---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
set_slug: "t2s-intra-balance-movement"
source_ids: ["src-000242", "src-000243", "src-000244", "src-000245", "src-000246", "src-000247", "src-000248", "src-000251", "src-000252", "src-000253", "src-000254", "src-000255", "src-000256", "src-000257", "src-000258", "src-000359", "src-000360", "src-000361"]
source_editions: ["march-2024"]
message_ids: ["camt.066.001.02", "camt.067.001.02", "camt.068.001.02", "camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02", "camt.078.001.02", "camt.079.001.02", "camt.080.001.02", "camt.081.001.02", "camt.082.001.02", "camt.083.001.02", "camt.084.001.02", "camt.085.001.02"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S IntraBalanceMovement extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000242 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.066.001.02/structure.md) | See declaration coverage |
| src-000243 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.067.001.02/structure.md) | See declaration coverage |
| src-000244 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.068.001.02/structure.md) | See declaration coverage |
| src-000245 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.072.001.02/structure.md) | See declaration coverage |
| src-000246 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.073.001.02/structure.md) | See declaration coverage |
| src-000247 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.074.001.02/structure.md) | See declaration coverage |
| src-000248 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.075.001.02/structure.md) | See declaration coverage |
| src-000251 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.078.001.02/structure.md) | See declaration coverage |
| src-000252 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.079.001.02/structure.md) | See declaration coverage |
| src-000253 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.080.001.02/structure.md) | See declaration coverage |
| src-000254 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.081.001.02/structure.md) | See declaration coverage |
| src-000255 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.082.001.02/structure.md) | See declaration coverage |
| src-000256 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.083.001.02/structure.md) | See declaration coverage |
| src-000257 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.084.001.02/structure.md) | See declaration coverage |
| src-000258 | xsd | extracted-needs-review | [Evidence](../../../messages/camt.085.001.02/structure.md) | See declaration coverage |
| src-000359 | docx | extracted-needs-review | [Evidence](documents/src-000359/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000360 | pdf | extracted-needs-review | [Evidence](documents/src-000360/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000361 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000361/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)

<!-- INTRABALANCE-REVIEW-START -->
[Source359 diagram, flow and table review](intrabalance-review.md)
<!-- INTRABALANCE-REVIEW-END -->
