---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "44.1 MessageDefinition Functionality"]
file_pages: [2101]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.004.001.05"]
---

# 44.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2101 to 2101.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2101

```text
44 setr.004.001.05
RedemptionOrderV05
44.1 MessageDefinition Functionality
Scope
The RedemptionOrder message is sent by an instructing party, for example, an investment manager or
its authorised representative, to the executing party, for example, a transfer agent, to instruct the
redemption of one or more financial instruments for one investment fund account.
Usage
The RedemptionOrder message is used to instruct single redemption orders, that is, a message
containing one order for one financial instrument and related to one investment account. The
RedemptionOrder message may also be used for multiple orders, that is, a message containing several
orders related to the same investment account for different financial instruments.
For a single redemption order, the RedemptionOrder message, not the RedemptionBulkOrder
message, must be used.
If there are redemption orders for the same financial instrument but for different accounts that are to be
communicated in a single message, then the RedemptionBulkOrder message must be used.
Outline
The RedemptionOrderV05 MessageDefinition is composed of 6 MessageBuildingBlocks:
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
Approved by the Securities SEG on 27 January 2026 setr.004.001.05 RedemptionOrderV05
Investment Funds - Maintenance 2025 - 2026 2101 May 2026
```

