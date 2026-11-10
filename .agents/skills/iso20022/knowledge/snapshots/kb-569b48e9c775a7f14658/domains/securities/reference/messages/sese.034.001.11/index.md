---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "sese.034.001.11"
message_family: "sese.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:sese.034.001.11"
source_ids: ["src-000197", "src-000225"]
source_editions: ["2025-2026", "March 2026"]
message_name: "SecuritiesFinancingStatusAdviceV11"
business_area: "sese"
message_version: "11"
message_sets: ["settlement-and-reconciliation"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000197", "file_pages": [951, 993], "heading": "28 sese.034.001.11 SecuritiesFinancingStatusAdviceV11"}]
---

# sese.034.001.11 — SecuritiesFinancingStatusAdviceV11

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `SecuritiesFinancingStatusAdviceV11`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | sese.034.001.11 | [src-000225](../../../../../raw-input/settlement_and_reconciliation/sese.034.001.11.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:sese.034.001.11 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Settlement and Reconciliation | raw-input/settlement_and_reconciliation/sese.034.001.11.xsd |

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

- [Securities financing — three parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-three-parties.md)
- [Securities financing — two parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-instruction-two-parties.md)
- [Financing modification without position change — three parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-three-parties.md)
- [Financing modification without position change — two parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-modification-two-parties.md)
- [Financing substitution — three parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-three-parties.md)
- [Financing substitution — two parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-substitution-two-parties.md)
- [Financing top-up — three parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-three-parties.md)
- [Financing top-up — two parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-top-up-two-parties.md)
- [Financing withdrawal — three parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-three-parties.md)
- [Financing withdrawal — two parties](../../message-sets/settlement-and-reconciliation/2025-2026/flows/financing-withdrawal-two-parties.md)
<!-- SETTLEMENT-FLOW-LINKS-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
