---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05"]
file_pages: [3001]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50 setr.010.001.05 SubscriptionOrderV05

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3001 to 3001.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3001

```text
50 setr.010.001.05
SubscriptionOrderV05
50.1 MessageDefinition Functionality
Scope
The SubscriptionOrder message is sent by an instructing party, for example, an investment manager or
its authorised representative, to the executing party, for example, a transfer agent, to instruct the
subscription of one or more financial instruments for one investment fund account.
Usage
The SubscriptionOrder message is used to instruct single subscription orders, that is, a message
containing one order for one financial instrument for one investment account. The SubscriptionOrder
message may also be used for multiple orders, that is, a message containing several orders for the
same investment account for different financial instruments.
For a single subscription order, the SubscriptionOrder message, not the SubscriptionBulkOrder
message, must be used.
If there are subscription orders for the same financial instrument but for different accounts that are to be
communicated in a single message, then the SubscriptionBulkOrder message must be used.
Outline
The SubscriptionOrderV05 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. MultipleOrderDetails
General information related to the orders.
E. CopyDetails
Information provided when the message is a copy of a previous message.
F. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3001 May 2026
```

