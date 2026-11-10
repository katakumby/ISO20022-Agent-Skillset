---
template: false
review_status: "needs-review"
domain: "shared"
document_kind: "participant"
participant_id: "bah-technical-forwarder"
aliases: ["technical middle man"]
source_ids: ["src-000012"]
source_locations: ["file/printed page 4 §1.4; pages 9–10 §2.2"]
domains: ["shared"]
message_sets: ["business-application-header"]
message_ids: ["head.001.001.04"]
flows: ["bah-business-message-exchange"]
limitations: ["Scoped functional role; no institutional equivalence inferred.", "Source guide diagram comparisons recorded; source/version discrepancies remain explicit."]
source_editions: ["Version 3.0 2021-11-03"]
---

# Technical intermediary that forwards a Business Message

## Definition and role scope

A transport intermediary that performs no business function on the message. This is a functional transport role and is not identified as a BAH business sender or receiver solely because it forwards the message.

## Responsibilities and actions

Forwards to the correct business application without opening or changing the Business Message. Only transport headers change in the forwarding scenario. The guide warns that connecting networks with incompatible non-ISO header mechanisms can lose business information when BAH is omitted.

## Identifiers

No BAH identity is assigned merely because of technical forwarding. The source does not define a transport-address scheme.

## Relationships and applicability

- [bah-sending-messaging-endpoint](bah-sending-messaging-endpoint.md).
- [bah-receiving-messaging-endpoint](bah-receiving-messaging-endpoint.md).
- [bah-business-intermediary](bah-business-intermediary.md).

The same real application or institution can occupy different roles in different exchanges. These records are scoped to BAH messaging and do not equate the roles with account owner, account servicer, bank, CSD or market infrastructure.

## Flows

- [bah-business-message-exchange](../message-sets/business-application-header/2021-11-03-v3.0/flows/business-message-exchange.md)

## Evidence and limitations

- [src-000012](../../../evidence/omitted/2bef0f7d99f68f11e72a140f.md), file/printed page 4 §1.4; pages 9–10 §2.2.

Source labels are scoped aliases, not identity assertions about institutions. Diagram cross-checks are recorded in the MUG visual coverage; exact-version applicability and source direction discrepancies remain needs-review. [BAH and BFH context](../concepts/business-application-header-and-business-file-header.md).

## Reviewed source diagrams

[MUG diagram/table coverage and precise visual-review evidence](../message-sets/business-application-header/2021-11-03-v3.0/documents/src-000012/visual-coverage.md).
