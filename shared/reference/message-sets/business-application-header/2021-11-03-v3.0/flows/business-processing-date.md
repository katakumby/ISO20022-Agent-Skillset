---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-business-processing-date"
source_ids: ["src-000012"]
source_locations: ["MUG §2.6, file/printed pages 14–15"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Indicate the business processing date

## Purpose, trigger and preconditions

Tell the receiver which business processing date the message refers to.

Market practice or bilateral agreement should define use of this field.

Evidence: [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed pages 14–15, §2.6.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Supplies BusinessProcessingDate for the receiver and sends the message. | Sending endpoint → receiving endpoint |

All steps derive from [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), §2.6, file/printed pages 14–15. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

BusinessProcessingDate may differ from CreationDate. Source examples cover after-hours processing, legal business-date differences, time zones, and forward-dated requests; no particular calendar rule is universal.

## Outcomes and postconditions

The intended business processing date is communicated. Source-defined settlement or processing success is not guaranteed by this header.

## Diagrams and review

- [Diagram fig-0021](../documents/src-000012/pdf-figures/fig-0021.md).
- [Complete table tbl-0008](../documents/src-000012/tables/tbl-0008.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

