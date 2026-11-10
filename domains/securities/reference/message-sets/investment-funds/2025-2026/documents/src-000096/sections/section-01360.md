---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "42.1 MessageDefinition Functionality"]
file_pages: [1887]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.002.001.05"]
---

# 42.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1887 to 1887.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1887

```text
42 setr.002.001.05
RedemptionBulkOrderCancellationRequestV0
5
42.1 MessageDefinition Functionality
Scope
The RedemptionBulkOrderCancellationRequest message is sent by an instructing party, for example,
an investment manager or its authorised representative, to the executing party, for example, a transfer
agent, to request the cancellation of a previously sent RedemptionBulkOrder.
Usage
The RedemptionBulkOrderCancellationRequest message is used to request the cancellation of one or
more individual orders.
There is no amendment, but a cancellation and re-instruct policy.
To request the cancellation of one or more individual orders, the order reference of each individual
order listed in the original RedemptionBulkOrder message is specified in the order reference element.
The message identification of the RedemptionBulkOrder message which contains the individual orders
to be cancelled may also be quoted in PreviousReference but this is not recommended.
The deadline and acceptance of a cancellation request is subject to a service level agreement (SLA).
This cancellation message is a cancellation request. There is no automatic acceptance of the
cancellation.
The rejection or acceptance of a RedemptionBulkOrderCancellationRequest is made using an
OrderCancellationStatusReport message.
Outline
The RedemptionBulkOrderCancellationRequestV05 MessageDefinition is composed of 6
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
Approved by the Securities SEG on 27 January 2026 setr.002.001.05
RedemptionBulkOrderCancellationRequestV05
Investment Funds - Maintenance 2025 - 2026 1887 May 2026
```

