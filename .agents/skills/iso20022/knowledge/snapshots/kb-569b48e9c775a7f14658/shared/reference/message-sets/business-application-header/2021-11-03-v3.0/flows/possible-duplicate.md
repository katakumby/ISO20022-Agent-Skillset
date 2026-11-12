---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-possible-duplicate"
source_ids: ["src-000012", "src-000011"]
source_locations: ["MUG §2.10, file/printed pages 19"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03", "Version 4 March 2024"]
---

# Resend when original receipt is uncertain

## Purpose, trigger and preconditions

Recover when the sender suspects that the receiver did not receive the Business Message.

The sender has received no reply because of technical or other problems.

Evidence: [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 19, §2.10.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Resends the same Business Message, marks PossibleDuplicate YES, and copies relevant original header elements into Related. | Sending endpoint → receiving endpoint |
| 2 | Receiving endpoint | Checks whether the original identified in Related was received. | Decision at receiving endpoint |
| 3 | Receiving endpoint | If original was received, ignores this business message; if not received, treats it as the original. | Alternative branches at receiving endpoint |

All steps derive from [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), §2.10, file/printed pages 19. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

The received-original and missing-original branches are mutually exclusive. This is application-level resend, not network retransmission (also src-000011 pp5–6 and p15 §2.4.11).

## Outcomes and postconditions

Avoid repeated business processing when the original was already received; otherwise process as original.

## Diagrams and review

- [Diagram fig-0026](../documents/src-000012/pdf-figures/fig-0026.md).
- [Complete table tbl-0012](../documents/src-000012/tables/tbl-0012.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

