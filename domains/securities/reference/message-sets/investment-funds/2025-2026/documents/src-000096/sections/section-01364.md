---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "43.1 MessageDefinition Functionality"]
file_pages: [1892, 1893]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.003.001.05"]
---

# 43.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1892 to 1893.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1892

```text
43 setr.003.001.05
RedemptionBulkOrderConfirmationV05
43.1 MessageDefinition Functionality
Scope
The RedemptionBulkOrderConfirmation message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
confirm the details of execution for a previously received RedemptionBulkOrder message.
Usage
The RedemptionBulkOrderConfirmation message is used to confirm the execution of all individual
orders included in a previously sent RedemptionBulkOrder message.
There is usually one bulk confirmation message for one bulk order message.
Each individual order confirmation specified is identified in DealReference. The reference of the original
individual order is specified in OrderReference. The message identification of the RedemptionBulkOrder
message in which the individual order was conveyed may also be quoted in RelatedReference, but this
is not recommended.
A RedemptionBulkOrder must in all cases be responded to by a RedemptionBulkOrderConfirmation
and in no circumstances by a RedemptionOrderConfirmation.
If the executing party needs to confirm a RedemptionOrder instruction, then the
RedemptionOrderConfirmation must be used.
When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be
present with the value 'true' or '1'. When this is the case, the message must only contain a confirmation
amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.
Outline
The RedemptionBulkOrderConfirmationV05 MessageDefinition is composed of 7
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. BulkExecutionDetails
General information related to the execution of the orders.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1892 May 2026
```

## File page 1893

```text
F. CopyDetails
Information provided when the message is a copy of a previous message.
G. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.003.001.05
RedemptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 1893 May 2026
```

