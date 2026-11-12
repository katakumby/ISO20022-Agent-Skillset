---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
set_slug: "t2s"
source_ids: ["src-000232", "src-000233", "src-000234"]
source_editions: ["August 2026", "august-2026"]
message_ids: ["acmt.025.001.02", "acmt.026.001.02", "admi.005.001.02", "admi.006.001.01", "admi.007.001.01", "camt.064.001.01", "camt.065.001.01", "camt.066.001.02", "camt.067.001.02", "camt.068.001.02", "camt.072.001.02", "camt.073.001.02", "camt.074.001.02", "camt.075.001.02", "camt.076.001.01", "camt.077.001.01", "camt.078.001.02", "camt.079.001.02", "camt.080.001.02", "camt.081.001.02", "camt.082.001.02", "camt.083.001.02", "camt.084.001.02", "camt.085.001.02", "colr.001.001.02", "colr.002.001.02", "head.002.001.01", "reda.006.001.01", "reda.007.001.01", "reda.008.001.01", "reda.009.001.01", "reda.010.001.01", "reda.012.001.01", "reda.013.001.01", "reda.014.001.02", "reda.015.001.01", "reda.016.001.01", "reda.017.001.02", "reda.018.001.01", "reda.019.001.01", "reda.020.001.01", "reda.021.001.01", "reda.022.001.02", "reda.023.001.01", "reda.024.001.01", "reda.025.001.01", "reda.026.001.01", "reda.027.001.01", "reda.028.001.01", "reda.029.001.01", "reda.030.001.01", "reda.031.001.01", "reda.032.001.01", "reda.033.001.01", "reda.034.001.01", "reda.035.001.01", "reda.036.001.01", "reda.037.001.01", "reda.038.001.01", "reda.039.001.01", "reda.040.001.01", "reda.041.001.02", "reda.042.001.01", "reda.043.001.02", "reda.044.001.01", "reda.045.001.01", "reda.046.001.01", "reda.047.001.01", "reda.049.001.01", "reda.050.001.01", "reda.051.001.01", "reda.075.001.01", "reda.077.001.01", "semt.025.001.01", "semt.026.001.01", "semt.027.001.01", "semt.028.001.01", "semt.029.001.01", "semt.030.001.01", "semt.031.001.01", "semt.032.001.01", "semt.033.001.01", "semt.034.001.01", "semt.040.001.01", "semt.044.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "t2s-aggregation"
---

# TARGET2-Securities extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000232 | docx | processed-with-source-limitations | [Evidence](documents/src-000232/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000233 | pdf | extracted-needs-review | [Evidence](documents/src-000233/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000234 | zip | inventory-complete | [Evidence](../../../../../../catalog/sources.json) | See publication reference |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
