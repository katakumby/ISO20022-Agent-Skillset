---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["51 setr.011.001.05 SubscriptionOrderCancellationRequestV05", "52.1 MessageDefinition Functionality"]
file_pages: [3248, 3249]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.012.001.06"]
---

# 52.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 3248 to 3249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3248

```text
52 setr.012.001.06
SubscriptionOrderConfirmationV06
52.1 MessageDefinition Functionality
Scope
The SubscriptionOrderConfirmation message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
confirm the details of the execution of a SubscriptionOrder instruction.
Usage
The SubscriptionOrderConfirmation message is used to confirm the execution of one or more individual
orders.
A SubscriptionOrder message containing more than one individual order may be responded to by more
than one SubscriptionOrderConfirmation message, as the valuation cycle of the financial instruments in
each individual order may be different. When a SubscriptionOrderConfirmation message contains fewer
confirmations that originally instructed in the original SubscriptionOrder message, there is no
specification indication in the confirmation for this. Reconciliation must be based on the references.
Each individual order confirmation specified is identified in DealReference. The reference of the original
individual order is specified in OrderReference. The message identification of the SubscriptionOrder
message in which the individual orders was conveyed may also be quoted in RelatedReference but this
is not recommended.
A SubscriptionOrder must in all cases be responded to by a SubscriptionOrderConfirmation message
and in no circumstances by a SubscriptionBulkOrderConfirmation message.
If the executing party needs to confirm one or more subscription orders for the same financial
instrument, then a SubscriptionBulkOrderConfirmation message must be used.
When the message is used to convey a confirmation amendment/s, the AmendmentIndicator must be
present with the value 'true' or '1'. When this is the case, the message must only contain a confirmation
amendment/s and not contain both a confirmation amendment/s and a 'new' confirmation/s.
Outline
The SubscriptionOrderConfirmationV06 MessageDefinition is composed of 7 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3248 May 2026
```

## File page 3249

```text
E. MultipleExecutionDetails
General information related to the execution of the orders.
F. CopyDetails
Information provided when the message is a copy of a previous message.
G. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 setr.012.001.06 SubscriptionOrderConfirmationV06
Investment Funds - Maintenance 2025 - 2026 3249 May 2026
```

