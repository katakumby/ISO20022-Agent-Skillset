---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S LinkReferenceData"
set_slug: "t2s-link-reference-data"
source_ids: ["src-000300", "src-000301", "src-000302", "src-000303", "src-000304", "src-000305", "src-000365", "src-000366", "src-000367"]
source_editions: ["december-2024"]
message_ids: ["reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S LinkReferenceData extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000300 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.045.001.01/structure.md) | See declaration coverage |
| src-000301 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.046.001.01/structure.md) | See declaration coverage |
| src-000302 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.047.001.01/structure.md) | See declaration coverage |
| src-000303 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.049.001.01/structure.md) | See declaration coverage |
| src-000304 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.050.001.01/structure.md) | See declaration coverage |
| src-000305 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.051.001.01/structure.md) | See declaration coverage |
| src-000365 | docx | extracted-needs-review | [Evidence](documents/src-000365/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000366 | pdf | extracted-needs-review | [Evidence](documents/src-000366/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000367 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000367/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
