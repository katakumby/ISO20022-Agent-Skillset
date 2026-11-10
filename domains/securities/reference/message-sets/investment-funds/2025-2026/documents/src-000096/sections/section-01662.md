---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "46.1 MessageDefinition Functionality"]
file_pages: [2310, 2311]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.006.001.06"]
---

# 46.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2310 to 2311.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2310

```text
46 setr.006.001.06
RedemptionOrderConfirmationV06
46.1 MessageDefinition Functionality
Scope
The RedemptionOrderConfirmation message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
confirm the details of execution for a previously received RedemptionOrder message.
Usage
The RedemptionOrderConfirmation message is used to confirm the execution of one or more individual
orders.
A RedemptionOrder message containing more than one individual order may be responded to by more
than one RedemptionOrderConfirmation message, as the valuation cycle of the financial instruments in
each individual order may be different. When a RedemptionOrderConfirmation message contains fewer
confirmations that originally instructed in the original RedemptionOrder message, there is no
specification indication in the confirmation for this. Reconciliation must be based on the references.
Each individual order confirmation specified is identified in DealReference. The reference of the original
individual order is specified in OrderReference. The message identification of the RedemptionOrder
message in which the individual order was conveyed may also be quoted in RelatedReference but this
is not recommended.
A RedemptionOrder must in all cases be responded to by a RedemptionOrderConfirmation message
and in no circumstances by a RedemptionBulkOrderConfirmation message.
If the executing party needs to confirm one or more redemption orders for the same financial instrument
then a RedemptionBulkOrderConfirmation message must be used.
When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be
present with the value 'true' or '1'. When this is the case, the message must only contain a confirmation
amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.
Outline
The RedemptionOrderConfirmationV06 MessageDefinition is composed of 7 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2310 May 2026
```

## File page 2311

```text
E. MultipleExecutionDetails
General information related to the execution of investment fund orders.
F. CopyDetails
Information provided when the message is a copy of a previous message.
G. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.006.001.06 RedemptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 2311 May 2026
```

