---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "business-flow"
flow_id: "bah-signed-message"
source_ids: ["src-000012"]
source_locations: ["MUG §2.12, file/printed pages 21"]
source_edition: "Version 3.0, 2021-11-03"
domains: ["shared"]
message_sets: ["business-application-header"]
message_families: ["head.001"]
message_ids: []
participants: ["bah-sending-messaging-endpoint", "bah-receiving-messaging-endpoint"]
limitations: ["MUG-to-exact-schema-version applicability unresolved.", "Source figures have explicit review evidence; contextual/version limitations remain."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Send a signed Business Message

## Purpose, trigger and preconditions

Send a Business Message containing the sending business entity signature.

Signature must follow the W3C XML Signature specification and additional service, market-practice or business-area constraints.

Evidence: [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed pages 21, §2.12.

## Participants

- [bah-sending-messaging-endpoint](../../../../participants/bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](../../../../participants/bah-receiving-messaging-endpoint.md).

## Ordered activities and message direction

| Step | Responsible participant | Activity or decision | Sender / receiver |
| --- | --- | --- | --- |
| 1 | Sending endpoint | Includes Signature in the BAH and sends the Business Message. | Sending endpoint → receiving endpoint |

All steps derive from [src-000012](../../../../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), §2.12, file/printed pages 21. The exchanged object is a Business Message with BAH (head.001 family); a particular document-message identifier is not generally specified by this scenario.

## Alternatives and exceptions

The detailed signing and verification paths, including failure decisions, are preserved in the linked Annex A flow references. Figure 4’s connector discrepancy remains issue-000017.

## Outcomes and postconditions

A signed Business Message is delivered; successful signature validation is not implied merely by presence of the field.

## Diagrams and review

- [Diagram fig-0031](../documents/src-000012/pdf-figures/fig-0031.md).
- [Diagram fig-0032](../documents/src-000012/pdf-figures/fig-0032.md).
- [Diagram fig-0033](../documents/src-000012/pdf-figures/fig-0033.md).
- [Diagram fig-0034](../documents/src-000012/pdf-figures/fig-0034.md).
- [Complete table tbl-0014](../documents/src-000012/tables/tbl-0014.md).
- [Complete table tbl-0020](../documents/src-000012/tables/tbl-0020.md).

[Full MUG visual-coverage and limitations](../documents/src-000012/visual-coverage.md). Source diagrams have Mermaid 12.3.0 rendering and visual-comparison records. Scenarios with no separate source graph use their complete usage table and narrative.

The MUG is Version 3.0 dated 2021-11-03; its packaging example uses head.001.001.03. The supplied schema is head.001.001.04. These source scenarios are retained as guide-level business context; exact profile applicability to V04 is not silently assumed. [Header comparison and limitations](../../../../concepts/business-application-header-and-business-file-header.md).


## Reusable detailed processes

[Construct and sign](signing-business-message.md) · [Verify signature](verifying-signature.md) · [Signature rules and contexts](../../../../concepts/bah-signature-guidelines.md).
