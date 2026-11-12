---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
set_slug: "t2s-securities-reference-data"
source_ids: ["src-000262", "src-000263", "src-000264", "src-000265", "src-000266", "src-000267", "src-000268", "src-000284", "src-000285", "src-000288", "src-000289", "src-000377", "src-000379"]
source_editions: ["june-2021"]
message_ids: ["reda.006.001.01", "reda.007.001.01", "reda.008.001.01", "reda.009.001.01", "reda.010.001.01", "reda.012.001.01", "reda.013.001.01", "reda.029.001.01", "reda.030.001.01", "reda.033.001.01", "reda.034.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S SecuritiesReferenceData extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000262 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.006.001.01/structure.md) | See declaration coverage |
| src-000263 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.007.001.01/structure.md) | See declaration coverage |
| src-000264 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.008.001.01/structure.md) | See declaration coverage |
| src-000265 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.009.001.01/structure.md) | See declaration coverage |
| src-000266 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.010.001.01/structure.md) | See declaration coverage |
| src-000267 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.012.001.01/structure.md) | See declaration coverage |
| src-000268 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.013.001.01/structure.md) | See declaration coverage |
| src-000284 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.029.001.01/structure.md) | See declaration coverage |
| src-000285 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.030.001.01/structure.md) | See declaration coverage |
| src-000288 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.033.001.01/structure.md) | See declaration coverage |
| src-000289 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.034.001.01/structure.md) | See declaration coverage |
| src-000377 | docx | extracted-needs-review | [Evidence](documents/src-000377/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000379 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000379/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)

<!-- SECURITIES-REFERENCE-REVIEW-START -->
[Source diagrams, flows and table review](securities-reference-review.md)
<!-- SECURITIES-REFERENCE-REVIEW-END -->
