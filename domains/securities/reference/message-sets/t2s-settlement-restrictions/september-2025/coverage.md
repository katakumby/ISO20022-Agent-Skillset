---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
set_slug: "t2s-settlement-restrictions"
source_ids: ["src-000311", "src-000312", "src-000313", "src-000314", "src-000315", "src-000316", "src-000317", "src-000380", "src-000381", "src-000382"]
source_editions: ["september-2025"]
message_ids: ["semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S SettlementRestrictions extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000311 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.028.001.01/structure.md) | See declaration coverage |
| src-000312 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.029.001.01/structure.md) | See declaration coverage |
| src-000313 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.030.001.01/structure.md) | See declaration coverage |
| src-000314 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.031.001.01/structure.md) | See declaration coverage |
| src-000315 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.032.001.01/structure.md) | See declaration coverage |
| src-000316 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.033.001.01/structure.md) | See declaration coverage |
| src-000317 | xsd | extracted-needs-review | [Evidence](../../../messages/semt.034.001.01/structure.md) | See declaration coverage |
| src-000380 | docx | extracted-needs-review | [Evidence](documents/src-000380/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000381 | pdf | extracted-needs-review | [Evidence](documents/src-000381/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000382 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000382/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)

<!-- SETTLEMENT-RESTRICTIONS-REVIEW-START -->
[Source diagrams, flows and table review](settlement-restrictions-review.md)
<!-- SETTLEMENT-RESTRICTIONS-REVIEW-END -->
