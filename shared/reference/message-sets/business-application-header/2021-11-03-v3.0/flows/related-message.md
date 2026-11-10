---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-related-message"
source_ids: ["src-000012"]
source_locations: ["MUG §2.13, file/printed pages 21–23"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint", "bah-business-intermediary"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain.", "Sender/receiver inconsistency in source p22 table."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Send a new message related to prior messages

## Purpose, trigger and preconditions

Expose the underlying business messages that triggered creation of a different business message.

A process uses multiple messages, potentially different definitions, and the recipient needs the underlying context.

Evidence: [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed pages 21–23, §2.13.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).
- [bah-business-intermediary](../../../../participants/bah-business-intermediary.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Business application creating the new message | Includes relevant prior BAH details in Related. CopyDuplicate and PossibleDuplicate are not used in this scenario. | Narrative names B as current creator; receiving endpoint is not safely resolved from the inconsistent table |
| 2 | Receiving endpoint | Distinguishes the functions of multiple related messages using their MessageDefinitionIdentifier values. | Receives related-message context |

All steps derive from [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), §2.13, file/printed pages 21–23. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

The p22 table repeats From A / To B despite the heading and narrative identifying B as sender of Business Message B. Direction is explicitly unresolved rather than guessed. Source examples include setr.047 relating to prior setr.012 and setr.010, and camt.029 relating to camt.056 and pacs.008.

## Outcomes and postconditions

The receiver can identify underlying messages and distinguish their functions. Related does not itself mean copy, duplicate, cancellation or reversal.

## Diagrams and review

- [Diagram fig-0027](../documents/src-000012/pdf-figures/fig-0027.md).
- [Diagram fig-0028](../documents/src-000012/pdf-figures/fig-0028.md).
- [Diagram fig-0029](../documents/src-000012/pdf-figures/fig-0029.md).
- [Complete table tbl-0015](../documents/src-000012/tables/tbl-0015.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).


## Source direction evidence

The diagram shows A→B for Business Message A, then B→C for Business Message B; the scenario table prints From=A and To=B while carrying Related from Message A. Issue-000003 preserves this conflict. The source also gives embedded document-reference examples, separately reconstructed without equating them with BAH Related. [§2.13 pp22–23](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf) (src-000012).
