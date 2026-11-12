---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "semt.017.001.14"
message_family: "semt.017"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.017.001.14"
source_ids: ["src-000197", "src-000205"]
source_editions: ["2025-2026", "March 2026"]
message_name: "SecuritiesTransactionPostingReportV14"
business_area: "semt"
message_version: "14"
message_sets: ["settlement-and-reconciliation"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000197", "file_pages": [198, 272], "heading": "8 semt.017.001.14 SecuritiesTransactionPostingReportV14"}]
---

# semt.017.001.14 — SecuritiesTransactionPostingReportV14

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesTransactionPostingReportV14`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | semt.017.001.14 | [src-000205](../../../../../raw-input/settlement_and_reconciliation/semt.017.001.14.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:semt.017.001.14 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Settlement and Reconciliation | raw-input/settlement_and_reconciliation/semt.017.001.14.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/settlement-and-reconciliation/2025-2026/index.md)
- [Source extraction coverage](../../message-sets/settlement-and-reconciliation/2025-2026/coverage.md)
- [Shared participants](../../../../../catalog/participants.md)
- [Business flows](../../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.



<!-- MDR-NAV-START -->
## Supplied business evidence

[Purpose, usage, actors and detailed MDR evidence](mdr-evidence.md)
<!-- MDR-NAV-END -->

<!-- SETTLEMENT-FLOW-LINKS-START -->
## Source-scoped settlement flows

- [Reporting pull mode with third party](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-pull.md)
- [Reporting push mode with third party](../../message-sets/settlement-and-reconciliation/2025-2026/flows/reporting-push.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
