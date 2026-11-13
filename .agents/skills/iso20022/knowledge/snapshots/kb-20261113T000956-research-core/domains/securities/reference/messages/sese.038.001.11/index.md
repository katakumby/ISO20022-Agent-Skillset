---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "sese.038.001.11"
message_family: "sese.038"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.038.001.11"
source_ids: ["src-000197", "src-000229"]
source_editions: ["2025-2026", "March 2026"]
message_name: "SecuritiesSettlementTransactionModificationRequestV11"
business_area: "sese"
message_version: "11"
message_sets: ["settlement-and-reconciliation"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000197", "file_pages": [1133, 1299], "heading": "32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11"}]
---

# sese.038.001.11 — SecuritiesSettlementTransactionModificationRequestV11

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesSettlementTransactionModificationRequestV11`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | sese.038.001.11 | [src-000229](../../../../../raw-input/settlement_and_reconciliation/sese.038.001.11.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:sese.038.001.11 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Settlement and Reconciliation | raw-input/settlement_and_reconciliation/sese.038.001.11.xsd |

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

- [Modification after settlement](../../message-sets/settlement-and-reconciliation/2025-2026/flows/modification-after-settlement.md)
- [Modification before settlement with counterparty response](../../message-sets/settlement-and-reconciliation/2025-2026/flows/modification-before-settlement.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
