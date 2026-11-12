---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "semt.034.001.01"
message_family: "semt.034"
namespace: "urn:iso:std:iso:20022:tech:xsd:semt.034.001.01"
source_ids: ["src-000233", "src-000317", "src-000381"]
source_editions: ["August 2026", "september-2025"]
message_name: "IntraPositionMovementPendingReportV01"
business_area: "semt"
message_version: "01"
message_sets: ["t2s", "t2s-settlement-restrictions"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
mdr_definitions: [{"source_id": "src-000233", "file_pages": [2724, 2747], "heading": "79 semt.034.001.01 IntraPositionMovementPendingReportV01"}, {"source_id": "src-000381", "file_pages": [169, 192], "heading": "8 semt.034.001.01 IntraPositionMovementPendingReportV01"}]
participant_ids: ["participant-src-000380-account-owner", "participant-src-000380-central-securities-depositories-csd", "participant-src-000380-direct-connected-participant-dcp", "participant-src-000380-executing-servicing-party", "participant-src-000380-instructing-party", "participant-src-000380-t2s"]
flow_ids: ["flow-src-000380-p263-push-mode", "flow-src-000380-p308-intra-position-movement-pending-report-semt-034", "flow-src-000380-p91-intra-position-movement-query-response-and-pending-report"]
---

# semt.034.001.01 — IntraPositionMovementPendingReportV01

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `IntraPositionMovementPendingReportV01`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | semt.034.001.01 | [src-000317](../../../../../raw-input/target2securities_t2s/semt.034.001.01.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:semt.034.001.01 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | T2S SettlementRestrictions | raw-input/target2securities_t2s/semt.034.001.01.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/t2s-settlement-restrictions/september-2025/index.md)
- [Source extraction coverage](../../message-sets/t2s-settlement-restrictions/september-2025/coverage.md)
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


<!-- SETTLEMENT-RESTRICTIONS-BUSINESS-START -->
[Purpose, roles, full/status query conditions, report rules and flows (September2025)](business-settlement-restrictions.md)
<!-- SETTLEMENT-RESTRICTIONS-BUSINESS-END -->

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
