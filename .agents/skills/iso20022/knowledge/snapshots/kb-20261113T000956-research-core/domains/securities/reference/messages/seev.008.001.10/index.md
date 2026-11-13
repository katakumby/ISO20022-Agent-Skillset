---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "seev.008.001.10"
message_family: "seev.008"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.008.001.10"
source_ids: ["src-000195"]
source_editions: []
message_name: "MeetingResultDisseminationV10"
business_area: "seev"
message_version: "10"
message_sets: ["meetings"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
---

# seev.008.001.10 — MeetingResultDisseminationV10

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `MeetingResultDisseminationV10`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | seev.008.001.10 | [src-000195](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.008.001.10.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:seev.008.001.10 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Meetings | raw-input/securities_events_general_meeting_proxy_voting/seev.008.001.10.xsd |

## References

- [Complete structure and type index](structure.md)
- [Message-set context, tables and diagrams](../../message-sets/meetings/edition-unknown-src-000188/index.md)
- [Source extraction coverage](../../message-sets/meetings/edition-unknown-src-000188/coverage.md)
- [Shared participants](../../../../../catalog/participants.md)
- [Business flows](../../../../../catalog/flows.md)
- [Source identities and original occurrences](../../../../../tracking/source-register.md)
- [Known gaps and review requirements](../../../../../tracking/issues.md)

## Review

Complete supplied schema declarations have focused pages with literal XML, qualified references and nested paths. Automated schema compilation: **pass**. Extraction is **needs-review**; this does not claim that source documentation, tables or diagrams have passed visual review.

<!-- ROLES-NAV-START -->
[Participants, sender/receiver directions and unresolved narrative roles](roles.md)
<!-- ROLES-NAV-END -->
