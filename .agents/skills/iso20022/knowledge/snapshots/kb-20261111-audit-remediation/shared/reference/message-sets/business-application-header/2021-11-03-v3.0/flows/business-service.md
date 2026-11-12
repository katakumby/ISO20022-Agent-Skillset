---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-business-service"
source_ids: ["src-000012"]
source_locations: ["MUG §2.4, file/printed pages 12"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Identify the business service

## Purpose, trigger and preconditions

Let the receiver relate the Business Message unambiguously to the service in which it is used.

Normally used when a business message can be used in multiple services. Service may be provider-defined or bilaterally/multilaterally agreed.

Evidence: [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 12, §2.4.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Populates BusinessService with the service identification and sends the message. | Sending endpoint → receiving endpoint |
| 2 | Receiving endpoint | Relates the message to the identified business service. | Receives business message |

All steps derive from [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), §2.4, file/printed pages 12. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

The guide does not define service identifiers or alternative failure paths.

## Outcomes and postconditions

Business-service context is identified.

## Diagrams and review

- [Complete table tbl-0006](../documents/src-000012/tables/tbl-0006.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

