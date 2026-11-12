---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "camt.080.001.02"
message_family: "camt.080"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.080.001.02"
source_ids: ["src-000233", "src-000253", "src-000360"]
source_editions: ["August 2026", "march-2024"]
message_name: "IntraBalanceMovementModificationQueryV02"
business_area: "camt"
message_version: "02"
message_sets: ["t2s", "t2s-intra-balance-movement"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [423, 435], "heading": "18 camt.080.001.02 IntraBalanceMovementModificationQueryV02"}, {"source_id": "src-000360", "file_pages": [232, 244], "heading": "11 camt.080.001.02 IntraBalanceMovementModificationQueryV02"}]
---

# camt.080.001.02 — IntraBalanceMovementModificationQueryV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `IntraBalanceMovementModificationQueryV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | camt.080.001.02 | [src-000253](../../../../../raw-input/target2securities_t2s/camt.080.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:camt.080.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S IntraBalanceMovement | raw-input/target2securities_t2s/camt.080.001.02.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/t2s-intra-balance-movement/march-2024/index.md)
- [Source extraction coverage](../../message-sets/t2s-intra-balance-movement/march-2024/coverage.md)
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


<!-- INTRABALANCE-FIG-13-START -->
[Push modification and cancellation reporting activity](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p200-push-mode.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-13-END -->

<!-- INTRABALANCE-FIG-14-START -->
[Pull modification and cancellation reporting activity](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p204-pull-mode.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-14-END -->

<!-- INTRABALANCE-FIG-21-START -->
[Modification query and report exchange](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p269-requesting-an-intra-balance-modification-query.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-21-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
