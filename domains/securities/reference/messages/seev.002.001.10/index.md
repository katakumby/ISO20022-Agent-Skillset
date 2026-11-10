---
template: false
document_kind: "message-index"
review_status: "needs-review"
domain: "securities"
message_id: "seev.002.001.10"
message_family: "seev.002"
namespace: "urn:iso:std:iso:20022:tech:xsd:seev.002.001.10"
source_ids: ["src-000189"]
source_editions: []
message_name: "MeetingCancellationV10"
business_area: "seev"
message_version: "10"
message_sets: ["meetings"]
limitations: ["MDR business content is reviewed independently.", "Source tables and figures are not reconciled by schema extraction."]
---

# seev.002.001.10 — MeetingCancellationV10

## Purpose, usage and actors

The supplied XSD establishes XML structure. Its message type name is `MeetingCancellationV10`. Business purpose, sender/receiver responsibilities, conditions and related flows require the independently supplied MDR evidence linked below. Schema membership alone does not identify a sending institution or business role.

## Identification

| Fact | Value | Evidence |
| --- | --- | --- |
| Exact definition | seev.002.001.10 | [src-000189](../../../../../raw-input/securities_events_general_meeting_proxy_voting/seev.002.001.10.xsd); targetNamespace |
| Namespace | urn:iso:std:iso:20022:tech:xsd:seev.002.001.10 | /xs:schema/@targetNamespace |
| Root(s) | Document | /xs:schema/xs:element |
| Collection | Meetings | raw-input/securities_events_general_meeting_proxy_voting/seev.002.001.10.xsd |

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
