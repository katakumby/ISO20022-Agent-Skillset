---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "camt.067.001.02"
message_family: "camt.067"
namespace: "urn:iso:std:iso:20022:tech:xsd:camt.067.001.02"
source_ids: ["src-000233", "src-000243", "src-000360"]
source_editions: ["August 2026", "march-2024"]
message_name: "IntraBalanceMovementStatusAdviceV02"
business_area: "camt"
message_version: "02"
message_sets: ["t2s", "t2s-intra-balance-movement"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [114, 132], "heading": "8 camt.067.001.02 IntraBalanceMovementStatusAdviceV02"}, {"source_id": "src-000360", "file_pages": [31, 49], "heading": "3 camt.067.001.02 IntraBalanceMovementStatusAdviceV02"}]
---

# camt.067.001.02 — IntraBalanceMovementStatusAdviceV02

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `IntraBalanceMovementStatusAdviceV02`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | camt.067.001.02 | [src-000243](../../../../../raw-input/target2securities_t2s/camt.067.001.02.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:camt.067.001.02 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S IntraBalanceMovement | raw-input/target2securities_t2s/camt.067.001.02.xsd |

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


<!-- INTRABALANCE-FIG-10-START -->
[External intra-balance movement activity](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p189-external-scenario.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-10-END -->

<!-- INTRABALANCE-FIG-11-START -->
[Internal intra-balance movement activity](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p193-internal-scenario.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-11-END -->

<!-- INTRABALANCE-FIG-17-START -->
[External cash settlement restriction creation](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p219-in-external-scenario.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-17-END -->

<!-- INTRABALANCE-FIG-18-START -->
[Internal cash settlement restriction creation](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p230-in-internal-scenario.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-18-END -->

<!-- INTRABALANCE-FIG-19-START -->
[Modification and cancellation transaction exchange](../../message-sets/t2s-intra-balance-movement/march-2024/flows/flow-src-000359-p238-modification-and-cancellation-process.md) — source359 roles, conditions and message directions.
<!-- INTRABALANCE-FIG-19-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
