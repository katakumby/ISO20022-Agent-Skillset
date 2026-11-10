---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09"]
file_pages: [602]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.004.001.09"]
---

# 27 sese.004.001.09 ReversalOfTransferOutConfirmationV09

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 602 to 602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 602

```text
27 sese.004.001.09
ReversalOfTransferOutConfirmationV09
27.1 MessageDefinition Functionality
Scope
The ReversalOfTransferOutConfirmation message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
cancel a previously sent transfer out confirmation.
Usage
The ReversalOfTransferOutConfirmation message is used to reverse a previously sent transfer out
confirmation.
To request the reversal of a transfer out confirmation, the transfer reference of the transfer out
instruction, as specified in the original TransferOutInstruction message, is specified in the transfer
reference element. The executing party's reference for the execution of the transfer may also be
specified in the TransferConfirmationReference element.
The message identification of the original TransferOutConfirmation message may also be quoted in
PreviousReference but this is not recommended.
Outline
The ReversalOfTransferOutConfirmationV09 MessageDefinition is composed of 8
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
F. ReversalReferences
Reference of the transfer confirmation to be reversed.
G. MarketPracticeVersion
Identifies the market practice to which the message conforms.
H. CopyDetails
Approved by the Securities SEG on 27 January 2026 sese.004.001.09
ReversalOfTransferOutConfirmationV09
Investment Funds - Maintenance 2025 - 2026 602 May 2026
```

