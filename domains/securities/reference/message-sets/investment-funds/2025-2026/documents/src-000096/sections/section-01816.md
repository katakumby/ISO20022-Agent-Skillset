---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05"]
file_pages: [2523]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47 setr.007.001.05 SubscriptionBulkOrderV05

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2523 to 2523.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2523

```text
47 setr.007.001.05
SubscriptionBulkOrderV05
47.1 MessageDefinition Functionality
Scope
The SubscriptionBulkOrder message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
instruct a subscription to a financial instrument for two or more accounts.
Usage
The SubscriptionBulkOrder message is used to bulk several individual orders into one bulk order. The
individual orders come from different instructing parties, that is, account owners, but are for the same
financial instrument. This message will typically be used by a party collecting orders and bulking these
individual orders into one bulk order before sending it to another party.
For a single subscription order, the SubscriptionOrder message, not the SubscriptionBulkOrder
message, must be used.
Outline
The SubscriptionBulkOrderV05 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. BulkOrderDetails
General information related to the orders.
E. CopyDetails
Information provided when the message is a copy of a previous message.
F. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2523 May 2026
```

