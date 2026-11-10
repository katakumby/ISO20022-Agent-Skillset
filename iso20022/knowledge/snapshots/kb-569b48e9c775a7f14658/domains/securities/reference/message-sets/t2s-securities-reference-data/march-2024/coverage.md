---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
set_slug: "t2s-securities-reference-data"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: ["reda.006.001.01", "reda.007.001.01", "reda.008.001.01", "reda.009.001.01", "reda.010.001.01", "reda.012.001.01", "reda.013.001.01", "reda.029.001.01", "reda.030.001.01", "reda.033.001.01", "reda.034.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# T2S SecuritiesReferenceData extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000378 | pdf | extracted-needs-review | [Evidence](documents/src-000378/index.md) | See item-level review evidence and remaining source-wide limitations |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
