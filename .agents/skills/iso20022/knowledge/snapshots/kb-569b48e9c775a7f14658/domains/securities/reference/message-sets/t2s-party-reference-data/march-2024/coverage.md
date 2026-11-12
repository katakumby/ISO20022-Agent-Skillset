---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S PartyReferenceData"
set_slug: "t2s-party-reference-data"
source_ids: ["src-000269", "src-000270", "src-000271", "src-000272", "src-000277", "src-000286", "src-000296", "src-000297", "src-000298", "src-000368", "src-000369", "src-000370"]
source_editions: ["march-2024"]
message_ids: ["reda.014.001.02", "reda.015.001.01", "reda.016.001.01", "reda.017.001.02", "reda.022.001.02", "reda.031.001.01", "reda.041.001.02", "reda.042.001.01", "reda.043.001.02"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S PartyReferenceData extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000269 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.014.001.02/structure.md) | See declaration coverage |
| src-000270 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.015.001.01/structure.md) | See declaration coverage |
| src-000271 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.016.001.01/structure.md) | See declaration coverage |
| src-000272 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.017.001.02/structure.md) | See declaration coverage |
| src-000277 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.022.001.02/structure.md) | See declaration coverage |
| src-000286 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.031.001.01/structure.md) | See declaration coverage |
| src-000296 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.041.001.02/structure.md) | See declaration coverage |
| src-000297 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.042.001.01/structure.md) | See declaration coverage |
| src-000298 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.043.001.02/structure.md) | See declaration coverage |
| src-000368 | docx | extracted-needs-review | [Evidence](documents/src-000368/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000369 | pdf | extracted-needs-review | [Evidence](documents/src-000369/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000370 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000370/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
