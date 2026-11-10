---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "Collateral Management"
set_slug: "collateral-management"
source_ids: ["src-000065", "src-000066", "src-000067", "src-000068", "src-000069", "src-000070", "src-000071", "src-000072", "src-000073", "src-000074", "src-000075", "src-000076", "src-000077", "src-000078"]
source_editions: []
message_ids: ["colr.003.001.05", "colr.004.001.05", "colr.005.001.06", "colr.006.001.05", "colr.007.001.06", "colr.008.001.06", "colr.009.001.05", "colr.010.001.05", "colr.011.001.05", "colr.012.001.05", "colr.013.001.05", "colr.014.001.05", "colr.015.001.05", "colr.016.001.05"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed.", "No MDR narrative documentation is supplied for this collection; business purpose, participants and flows cannot be established from XSD alone."]
collection_kind: "message-set"
---

# Collateral Management extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000065 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.003.001.05/structure.md) | See declaration coverage |
| src-000066 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.004.001.05/structure.md) | See declaration coverage |
| src-000067 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.005.001.06/structure.md) | See declaration coverage |
| src-000068 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.006.001.05/structure.md) | See declaration coverage |
| src-000069 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.007.001.06/structure.md) | See declaration coverage |
| src-000070 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.008.001.06/structure.md) | See declaration coverage |
| src-000071 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.009.001.05/structure.md) | See declaration coverage |
| src-000072 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.010.001.05/structure.md) | See declaration coverage |
| src-000073 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.011.001.05/structure.md) | See declaration coverage |
| src-000074 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.012.001.05/structure.md) | See declaration coverage |
| src-000075 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.013.001.05/structure.md) | See declaration coverage |
| src-000076 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.014.001.05/structure.md) | See declaration coverage |
| src-000077 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.015.001.05/structure.md) | See declaration coverage |
| src-000078 | xsd | extracted-needs-review | [Evidence](../../../messages/colr.016.001.05/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
