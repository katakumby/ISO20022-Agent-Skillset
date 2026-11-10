---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-market-practice"
source_ids: ["src-000012"]
source_locations: ["MUG §2.5, file/printed pages 13–14"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Identify an implementation specification

## Purpose, trigger and preconditions

Indicate the market-practice specification with which the message complies.

Parties have agreed a business context. A market practice restricts the underlying message and may extend it through extensions or supplementary data.

Evidence: [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed pages 13–14, §2.5.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Supplies MarketPractice Registry and Identification identifying the specification within that registry. | Sending endpoint → receiving endpoint |

All steps derive from [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), §2.5, file/printed pages 13–14. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

Identification can include a URN, version or date; the examples are source examples, not prescribed universal registry values.

## Outcomes and postconditions

The recipient can identify the referenced implementation specification; compliance checking is not specified as an ordered workflow.

## Diagrams and review

- [Diagram fig-0020](../documents/src-000012/pdf-figures/fig-0020.md).
- [Complete table tbl-0007](../documents/src-000012/tables/tbl-0007.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

