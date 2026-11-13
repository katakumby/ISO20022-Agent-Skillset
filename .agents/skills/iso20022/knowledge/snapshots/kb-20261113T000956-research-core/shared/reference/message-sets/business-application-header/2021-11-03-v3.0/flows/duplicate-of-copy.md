---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-duplicate-of-copy"
source_ids: ["src-000012"]
source_locations: ["MUG §2.9, file/printed pages 18"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Send a duplicate of a prior copy

## Purpose, trigger and preconditions

Send a duplicate of a previously sent copy of a Business Message.

A prior copy Business Message exists.

Evidence: [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed pages 18, §2.9.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Uses CopyDuplicate=CODU and Related carrying relevant BAH elements of the copy Business Message. | Sending endpoint → receiving endpoint |

All steps derive from [src-000012](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), §2.9, file/printed pages 18. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

The related message is the copy referenced by this scenario. The guide defines no settlement correction semantics for this action.

## Outcomes and postconditions

The receiver is told this is a duplicate of a copy.

## Diagrams and review

- [Diagram fig-0025](../documents/src-000012/pdf-figures/fig-0025.md).
- [Complete table tbl-0011](../documents/src-000012/tables/tbl-0011.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).


## Source direction and code evidence

The diagram shows original A→B, prior copy A→C, then Message 3 (DUPL) A→C. The table prints To=B and CopyDuplicate=CODU. The general CODU usage and the drawn DUPL label are both retained; issue-000003 remains open. [§2.9 p18](../../../../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md) (src-000012).
