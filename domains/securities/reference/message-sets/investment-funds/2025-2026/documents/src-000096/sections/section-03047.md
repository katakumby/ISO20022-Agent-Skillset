---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03"]
file_pages: [4259]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.049.001.03"]
---

# 60 setr.049.001.03 SubscriptionBulkOrderConfirmationCancellationInstructionV03

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4259 to 4259.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4259

```text
60 setr.049.001.03
SubscriptionBulkOrderConfirmationCancellat
ionInstructionV03
60.1 MessageDefinition Functionality
Scope
The SubscriptionBulkOrderConfirmationCancellationInstruction message is sent by an executing party,
for example, a transfer agent, to the instructing party, for example, an investment manager or its
authorised representative, to cancel a previously sent SubscriptionBulkOrderConfirmation.
Usage
To request the cancellation of one or more individual order executions, the order reference and deal
reference of each individual order execution in the original SubscriptionBulkOrderConfirmation are
specified in the order reference and deal reference elements respectively. The message identification of
the SubscriptionBulkOrderConfirmation message in which the individual order execution was conveyed
may also be quoted in PreviousReference but this is not recommended. The AmendmentIndicator is
used to specify whether the subscription bulk order confirmation cancellation is to be followed by an
amendment An amendment of a subscription bulk order confirmation is carried out by sending a
SubscriptionBulkOrderConfirmation message in which the AmendmentIndicator contains the value
'true'.
Outline
The SubscriptionBulkOrderConfirmationCancellationInstructionV03 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. AmendmentIndicator
Indicates whether a confirmation amendment message will follow the confirmation cancellation
instruction or not.
F. MasterReference
Reference assigned to a set of orders or trades in order to link them together.
G. OrderReferences
Identification of the individual order confirmation to be cancelled.
Approved by the Securities SEG on 27 January 2026 setr.049.001.03
SubscriptionBulkOrderConfirmationCancellationInstr
uctionV03
Investment Funds - Maintenance 2025 - 2026 4259 May 2026
```

