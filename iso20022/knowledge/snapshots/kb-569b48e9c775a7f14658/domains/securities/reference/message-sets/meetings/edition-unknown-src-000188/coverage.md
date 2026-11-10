---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "Meetings"
set_slug: "meetings"
source_ids: ["src-000188", "src-000189", "src-000190", "src-000191", "src-000192", "src-000193", "src-000194", "src-000195"]
source_editions: []
message_ids: ["seev.001.001.13", "seev.002.001.10", "seev.003.001.10", "seev.004.001.11", "seev.005.001.10", "seev.006.001.12", "seev.007.001.12", "seev.008.001.10"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed.", "No MDR narrative documentation is supplied for this collection; business purpose, participants and flows cannot be established from XSD alone."]
collection_kind: "message-set"
---

# Meetings extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000188 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.001.001.13/structure.md) | See declaration coverage |
| src-000189 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.002.001.10/structure.md) | See declaration coverage |
| src-000190 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.003.001.10/structure.md) | See declaration coverage |
| src-000191 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.004.001.11/structure.md) | See declaration coverage |
| src-000192 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.005.001.10/structure.md) | See declaration coverage |
| src-000193 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.006.001.12/structure.md) | See declaration coverage |
| src-000194 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.007.001.12/structure.md) | See declaration coverage |
| src-000195 | xsd | extracted-needs-review | [Evidence](../../../messages/seev.008.001.10/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
