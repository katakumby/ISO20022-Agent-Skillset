---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "41.1 MessageDefinition Functionality"]
file_pages: [1685]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.001.001.05"]
---

# 41.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1685 to 1685.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1685

```text
41 setr.001.001.05
RedemptionBulkOrderV05
41.1 MessageDefinition Functionality
Scope
The RedemptionBulkOrder message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
instruct a redemption from a financial instrument for two or more accounts.
Usage
The RedemptionBulkOrder message is used to bulk several individual orders into one bulk order. The
individual orders come from different instructing parties, that is, account owners, but are for the same
financial instrument. The RedemptionBulkOrder can result in one single bulk cash settlement or several
individual cash settlements.
This message will be typically used by a party collecting orders, that is, a concentrator, bulking these
individual orders into one bulk order before sending it to an executing party.
For a single redemption order, the RedemptionOrder message, not the RedemptionBulkOrder
message, must be used.
If there are redemption orders for different financial instruments but for the same account, then the
RedemptionOrder must be used.
Outline
The RedemptionBulkOrderV05 MessageDefinition is composed of 6 MessageBuildingBlocks:
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
Approved by the Securities SEG on 27 January 2026 setr.001.001.05 RedemptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 1685 May 2026
```

