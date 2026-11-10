---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-business-message-exchange"
source_ids: ["src-000012"]
source_locations: ["MUG §2.2, file/printed pages 9–11"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint", "bah-business-intermediary", "bah-technical-forwarder"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Send a Business Message

## Purpose, trigger and preconditions

A sending business application creates and sends a Business Message to its receiving business application.

A business message is to be exchanged. The guide does not supply further process-specific preconditions.

Evidence: [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 9–11, §2.2.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).
- [bah-business-intermediary](../../../../participants/bah-business-intermediary.md).
- [bah-technical-forwarder](../../../../participants/bah-technical-forwarder.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Creates the BAH and message; populates From, To, BusinessMessageIdentifier, MessageDefinitionIdentifier and CreationDate. | Sending endpoint → receiving endpoint |
| 2 | Technical forwarder, if present | Forwards without business processing. Only the transport header changes. | Business sender and receiver remain the same |
| 3 | Business intermediary, if present | Processes the first Business Message and creates a different Business Message; it is recipient on the first and sender on the second. | Distinct first and second exchanges |

All steps derive from [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), §2.2, file/printed pages 9–11. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

Forwarding and business processing are different branches. The source notes implementation challenges when non-ISO network headers cannot carry required business information without BAH.

## Outcomes and postconditions

The intended receiving business application receives the business message. No settlement, accounting or payment outcome is specified.

## Diagrams and review

- [Diagram fig-0001](../documents/src-000012/pdf-figures/fig-0001.md).
- [Diagram fig-0002](../documents/src-000012/pdf-figures/fig-0002.md).
- [Diagram fig-0003](../documents/src-000012/pdf-figures/fig-0003.md).
- [Diagram fig-0004](../documents/src-000012/pdf-figures/fig-0004.md).
- [Diagram fig-0010](../documents/src-000012/pdf-figures/fig-0010.md).
- [Diagram fig-0011](../documents/src-000012/pdf-figures/fig-0011.md).
- [Diagram fig-0012](../documents/src-000012/pdf-figures/fig-0012.md).
- [Diagram fig-0013](../documents/src-000012/pdf-figures/fig-0013.md).
- [Complete table tbl-0001](../documents/src-000012/tables/tbl-0001.md).
- [Complete table tbl-0002](../documents/src-000012/tables/tbl-0002.md).
- [Complete table tbl-0003](../documents/src-000012/tables/tbl-0003.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

