---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05"]
file_pages: [3243]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.011.001.05"]
---

# 51 setr.011.001.05 SubscriptionOrderCancellationRequestV05

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3243 to 3243.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3243

```text
51 setr.011.001.05
SubscriptionOrderCancellationRequestV05
51.1 MessageDefinition Functionality
Scope
The SubscriptionOrderCancellationRequest message is sent by an instructing party, for example, an
investment manager or its authorised representative, to the executing party, for example, a transfer
agent, to request the cancellation of a previously sent SubscriptionOrder.
Usage
The SubscriptionOrderCancellationRequest message is used to request the cancellation of one or more
individual orders.
There is no amendment, but a cancellation and re-instruct policy.
To request the cancellation of one or more individual orders, the order reference of each individual
order listed in the original SubscriptionOrder message is specified in the order reference element. The
message identification of the SubscriptionOrder message which contains the individual orders to be
cancelled may also be quoted in PreviousReference but this is not recommended.
The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).
This cancellation message is a cancellation request. There is no automatic acceptance of the
cancellation.
The rejection or acceptance of a SubscriptionOrderCancellationRequest is made using an
OrderCancellationStatusReport message.
Outline
The SubscriptionOrderCancellationRequestV05 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. MasterReference
Reference assigned to a set of orders or trades in order to link them together.
E. OrderReferences
Identification of the individual order to be cancelled.
F. CopyDetails
Information provided when the message is a copy of a previous message.
Approved by the Securities SEG on 27 January 2026 setr.011.001.05
SubscriptionOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 3243 May 2026
```

