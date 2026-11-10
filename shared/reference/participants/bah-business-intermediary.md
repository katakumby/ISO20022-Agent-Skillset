---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bah-business-intermediary"
aliases: ["Business Application in the middle", "middle man that processes the Business Message"]
source_ids: ["src-000012"]
source_locations: ["file/printed page 4 §1.4; pages 9–10 §2.2"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_ids: ["head.001.001.04"]
flows: ["bah-business-message-exchange", "bah-related-message"]
limitations: ["Scoped functional role; no institutional equivalence inferred.", "Source guide diagram comparisons recorded; source/version discrepancies remain explicit."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Business application acting as intermediary

## Definition and role scope

An intermediary that performs business processing is a business application in the guide. The same application is the recipient of one Business Message and sender of a different Business Message.

## Responsibilities and actions

Processes the first Business Message, appears as its BAH recipient, then creates a different Business Message and appears as the second BAH sender. This role is distinct from forwarding alone.

## Identifiers

The guide supplies no separate institution identifier scheme for this scoped role; the BAH From/To identification fields apply to each relevant message.

## Relationships and applicability

- [bah-sending-messaging-endpoint](bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](bah-receiving-messaging-endpoint.md).
- [bah-technical-forwarder](bah-technical-forwarder.md).

The same real application or institution can occupy different roles in different exchanges. These records are scoped to BAH messaging and do not equate the roles with account owner, account servicer, bank, CSD or market infrastructure.

## Flows

- [bah-business-message-exchange](../message-sets/business-application-header/2021-11-03-v3.0/flows/business-message-exchange.md)
- [bah-related-message](../message-sets/business-application-header/2021-11-03-v3.0/flows/related-message.md)

## Evidence and limitations

- [src-000012](../../../raw-input/business_application_header/ISO_20022_BusinessApplicationHeader_MUG_v3_0.pdf), file/printed page 4 §1.4; pages 9–10 §2.2.

Source labels are scoped aliases, not identity assertions about institutions. Diagram cross-checks are recorded in the MUG visual coverage; exact-version applicability and source direction discrepancies remain needs-review. [BAH and BFH context](../concepts/business-application-header-and-business-file-header.md).

## Reviewed source diagrams

[MUG diagram/table coverage and precise visual-review evidence](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/visual-coverage.md).
