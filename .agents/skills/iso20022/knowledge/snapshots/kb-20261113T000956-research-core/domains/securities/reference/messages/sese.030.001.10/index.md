---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "sese.030.001.10"
message_family: "sese.030"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.030.001.10"
source_ids: ["src-000197", "src-000221"]
source_editions: ["2025-2026", "March 2026"]
message_name: "SecuritiesSettlementConditionsModificationRequestV10"
business_area: "sese"
message_version: "10"
message_sets: ["settlement-and-reconciliation"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000197", "file_pages": [783, 801], "heading": "24 sese.030.001.10 SecuritiesSettlementConditionsModificationRequestV10"}]
---

# sese.030.001.10 — SecuritiesSettlementConditionsModificationRequestV10

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesSettlementConditionsModificationRequestV10`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | sese.030.001.10 | [src-000221](../../../../../raw-input/settlement_and_reconciliation/sese.030.001.10.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:sese.030.001.10 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Settlement and Reconciliation | raw-input/settlement_and_reconciliation/sese.030.001.10.xsd |

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

- [Release an instruction originally on hold](../../message-sets/settlement-and-reconciliation/2025-2026/flows/hold-release.md)
- [Processing change for two transactions](../../message-sets/settlement-and-reconciliation/2025-2026/flows/processing-change-multiple-transactions.md)
- [Processing change for one transaction](../../message-sets/settlement-and-reconciliation/2025-2026/flows/processing-change-one-transaction.md)
- [Hold then release an instruction](../../message-sets/settlement-and-reconciliation/2025-2026/flows/released-held-released.md)
- [Unilateral splitting](../../message-sets/settlement-and-reconciliation/2025-2026/flows/unilateral-splitting.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
