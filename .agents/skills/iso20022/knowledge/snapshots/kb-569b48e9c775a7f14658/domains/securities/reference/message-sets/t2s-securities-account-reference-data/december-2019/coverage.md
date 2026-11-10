---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
set_slug: "t2s-securities-account-reference-data"
source_ids: ["src-000273", "src-000274", "src-000275", "src-000276", "src-000278", "src-000287", "src-000290", "src-000291", "src-000292", "src-000371", "src-000372", "src-000373"]
source_editions: ["december-2019"]
message_ids: ["reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.023.001.01", "reda.032.001.01", "reda.035.001.01", "reda.036.001.01", "reda.037.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S SecuritiesAccountReferenceData extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000273 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.018.001.01/structure.md) | See declaration coverage |
| src-000274 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.019.001.01/structure.md) | See declaration coverage |
| src-000275 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.020.001.01/structure.md) | See declaration coverage |
| src-000276 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.021.001.01/structure.md) | See declaration coverage |
| src-000278 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.023.001.01/structure.md) | See declaration coverage |
| src-000287 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.032.001.01/structure.md) | See declaration coverage |
| src-000290 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.035.001.01/structure.md) | See declaration coverage |
| src-000291 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.036.001.01/structure.md) | See declaration coverage |
| src-000292 | xsd | extracted-needs-review | [Evidence](../../../messages/reda.037.001.01/structure.md) | See declaration coverage |
| src-000371 | docx | extracted-needs-review | [Evidence](documents/src-000371/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000372 | pdf | extracted-needs-review | [Evidence](documents/src-000372/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000373 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000373/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
