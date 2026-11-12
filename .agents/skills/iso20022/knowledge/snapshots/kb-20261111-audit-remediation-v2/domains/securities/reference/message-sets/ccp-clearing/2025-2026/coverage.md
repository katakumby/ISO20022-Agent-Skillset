---
template: false
document_kind: "extraction-coverage"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
set_slug: "ccp-clearing"
source_ids: ["src-000052", "src-000053", "src-000054", "src-000055", "src-000056", "src-000057", "src-000058", "src-000059", "src-000060", "src-000061", "src-000062", "src-000063", "src-000064"]
source_editions: ["2025-2026", "March 2026", "March 2026; Standards MX November 2026 release"]
message_ids: ["secl.001.001.05", "secl.002.001.05", "secl.003.001.05", "secl.004.001.04", "secl.005.001.02", "secl.006.001.02", "secl.007.001.03", "secl.008.001.03", "secl.009.001.03", "secl.010.001.04"]
limitations: ["All source tables and figures require recorded visual reconciliation before this set can be reviewed."]
collection_kind: "message-set"
---

# CCP Clearing extraction coverage

| Source | Format | Disposition | Destination | Review |
| --- | --- | --- | --- | --- |
| src-000052 | docx | extracted-needs-review | [Evidence](documents/src-000052/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000053 | pdf | extracted-needs-review | [Evidence](documents/src-000053/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000054 | xlsx | extracted-needs-review | [Evidence](workbooks/src-000054/index.md) | See item-level review evidence and remaining source-wide limitations |
| src-000055 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.001.001.05/structure.md) | See declaration coverage |
| src-000056 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.002.001.05/structure.md) | See declaration coverage |
| src-000057 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.003.001.05/structure.md) | See declaration coverage |
| src-000058 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.004.001.04/structure.md) | See declaration coverage |
| src-000059 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.005.001.02/structure.md) | See declaration coverage |
| src-000060 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.006.001.02/structure.md) | See declaration coverage |
| src-000061 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.007.001.03/structure.md) | See declaration coverage |
| src-000062 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.008.001.03/structure.md) | See declaration coverage |
| src-000063 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.009.001.03/structure.md) | See declaration coverage |
| src-000064 | xsd | extracted-needs-review | [Evidence](../../../messages/secl.010.001.04/structure.md) | See declaration coverage |

## Boundaries and pending checks

Each extracted document and workbook has its own item inventory. These inventories retain table parts, drawing occurrences, exact page/paragraph/cell locators and limitations. PDF candidate detection does not establish a complete visual table/diagram inventory. No set is marked reviewed solely because text or cells were extracted.

- Reconcile every source table and figure with its complete rendered original.
- Review participant definitions, activity order and message direction against the source.
- Render Mermaid reconstructions and compare their labels and relationships.
- Resolve document edition conflicts before combining business statements.

[Open issues](../../../../../../tracking/issues.md) · [Set index](index.md)
