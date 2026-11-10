---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-character-set"
source_ids: ["src-000012"]
source_locations: ["MUG §2.3, file/printed pages 11–12"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Declare additional character sets

## Purpose, trigger and preconditions

Inform the receiving application that relevant text elements may contain non-Basic-Latin characters.

Text may contain additional character sets.

Evidence: [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed pages 11–12, §2.3.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Lists each additional character set in CharacterSet, separated by semicolons, and sends the message. | Sending endpoint → receiving endpoint |
| 2 | Receiving endpoint | Interprets relevant text within the stated character sets. | Receives business message |

All steps derive from [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), §2.3, file/printed pages 11–12. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

More constrained text datatypes retain their own constraints; the BAH character-set statement does not override them.

## Outcomes and postconditions

The receiver can identify declared character sets; no further processing postcondition is specified.

## Diagrams and review

- [Complete table tbl-0005](../documents/src-000012/tables/tbl-0005.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).

