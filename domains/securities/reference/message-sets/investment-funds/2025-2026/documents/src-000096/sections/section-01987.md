---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "49.1 MessageDefinition Functionality"]
file_pages: [2766, 2767]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.009.001.05"]
---

# 49.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 2766 to 2767.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2766

```text
49 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
49.1 MessageDefinition Functionality
Scope
The SubscriptionBulkOrderConfirmation message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
confirm the details of the execution of a SubscriptionBulkOrder instruction.
Usage
The SubscriptionBulkOrderConfirmation message is used to confirm the execution of all individual
orders.
There is usually one bulk confirmation message for one bulk order message.
Each individual order confirmation specified is identified in DealReference. The reference of the original
individual order is specified in OrderReference. The message identification of the
SubscriptionBulkOrder message in which the individual order was conveyed may also be quoted in
RelatedReference.
A SubscriptionBulkOrder must in all cases be responded to by a SubscriptionBulkOrderConfirmation
and in no circumstances by a SubscriptionOrderConfirmation.
If the executing party needs to confirm a SubscriptionOrder instruction, then the
SubscriptionOrderConfirmation must be used.
When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be
present with the value 'true' or '1'. When this is the case, the message must only contain a confirmation
amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.
Outline
The SubscriptionBulkOrderConfirmationV05 MessageDefinition is composed of 7
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
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2766 May 2026
```

## File page 2767

```text
F. CopyDetails
Information provided when the message is a copy of a previous message.
G. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.009.001.05
SubscriptionBulkOrderConfirmationV05
Investment Funds - Maintenance 2025 - 2026 2767 May 2026
```

