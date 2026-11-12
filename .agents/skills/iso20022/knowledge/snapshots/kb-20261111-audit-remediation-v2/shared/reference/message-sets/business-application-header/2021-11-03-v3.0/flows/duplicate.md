---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-duplicate"
source_ids: ["src-000012"]
source_locations: ["MUG §2.8, file/printed pages 17"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Send a duplicate of a Business Message

## Purpose, trigger and preconditions

Send a duplicate of a previously sent Business Message.

A prior Business Message exists; the source example describes a resend upon request.

Evidence: [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 17, §2.8.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Sends the duplicate with CopyDuplicate=DUPL and Related carrying relevant original BAH elements. | Sending endpoint → receiving endpoint |

All steps derive from [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), §2.8, file/printed pages 17. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

This information/confirmation duplicate scenario is separate from the possible-duplicate branch where receipt is unknown.

## Outcomes and postconditions

The receiver is told that the message is a duplicate.

## Diagrams and review

- [Diagram fig-0023](../documents/src-000012/pdf-figures/fig-0023.md).
- [Diagram fig-0024](../documents/src-000012/pdf-figures/fig-0024.md).
- [Complete table tbl-0010](../documents/src-000012/tables/tbl-0010.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

