---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
set_slug: "fitrr"
source_ids: ["src-000320", "src-000321", "src-000322", "src-000323", "src-000324", "src-000325", "src-000326", "src-000327", "src-000328", "src-000329", "src-000330", "src-000331", "src-000332", "src-000333", "src-000334", "src-000335", "src-000336", "src-000337", "src-000338", "src-000339", "src-000340", "src-000341", "src-000342"]
source_editions: ["2025", "July 2025"]
message_ids: ["auth.016.001.03", "auth.017.001.02", "auth.031.001.01", "auth.032.001.01", "auth.033.001.03", "auth.035.001.01", "auth.036.001.03", "auth.039.001.01", "auth.040.001.01", "auth.041.001.01", "auth.042.001.02", "auth.043.001.01", "auth.044.001.03", "auth.045.001.03", "auth.047.001.01", "auth.048.001.01", "auth.049.001.02", "auth.050.001.01", "auth.053.001.01", "auth.102.001.01"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# Transactions and Financial Instruments Data Reporting extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000320 | docx | extracted-needs-review | [Evidence](documents/src-000320/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000321 | pdf | extracted-needs-review | [Evidence](documents/src-000321/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000322 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000322/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000323 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.016.001.03/structure.md) | See declaration coverage |
| src-000324 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.017.001.02/structure.md) | See declaration coverage |
| src-000325 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.031.001.01/structure.md) | See declaration coverage |
| src-000326 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.032.001.01/structure.md) | See declaration coverage |
| src-000327 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.033.001.03/structure.md) | See declaration coverage |
| src-000328 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.035.001.01/structure.md) | See declaration coverage |
| src-000329 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.036.001.03/structure.md) | See declaration coverage |
| src-000330 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.039.001.01/structure.md) | See declaration coverage |
| src-000331 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.040.001.01/structure.md) | See declaration coverage |
| src-000332 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.041.001.01/structure.md) | See declaration coverage |
| src-000333 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.042.001.02/structure.md) | See declaration coverage |
| src-000334 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.043.001.01/structure.md) | See declaration coverage |
| src-000335 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.044.001.03/structure.md) | See declaration coverage |
| src-000336 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.045.001.03/structure.md) | See declaration coverage |
| src-000337 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.047.001.01/structure.md) | See declaration coverage |
| src-000338 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.048.001.01/structure.md) | See declaration coverage |
| src-000339 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.049.001.02/structure.md) | See declaration coverage |
| src-000340 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.050.001.01/structure.md) | See declaration coverage |
| src-000341 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.053.001.01/structure.md) | See declaration coverage |
| src-000342 | xsd | extracted-needs-review | [Evidence](../../../messages/auth.102.001.01/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
