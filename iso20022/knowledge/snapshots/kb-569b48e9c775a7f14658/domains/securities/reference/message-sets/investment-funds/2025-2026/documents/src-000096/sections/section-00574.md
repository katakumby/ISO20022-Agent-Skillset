---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["31 sese.008.001.09 ReversalOfTransferInConfirmationV09"]
file_pages: [778]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.008.001.09"]
---

# 31 sese.008.001.09 ReversalOfTransferInConfirmationV09

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 778 to 778.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 778

```text
31 sese.008.001.09
ReversalOfTransferInConfirmationV09
31.1 MessageDefinition Functionality
Scope
The ReversalOfTransferInConfirmation message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or its authorised representative, to
cancel a previously sent transfer in confirmation.
Usage
The ReversalOfTransferInConfirmation message is used to reverse a previously sent transfer in
confirmation.
To request the reversal of a transfer in confirmation, the transfer reference of the transfer in instruction,
as specified in the original TransferInInstruction message, is specified in the transfer reference element.
The executing party's reference for the execution of the transfer may also be specified in the
TransferConfirmationReference element.
The message identification of the original TransferInConfirmation message may also be quoted in
PreviousReference but this is not recommended.
Outline
The ReversalOfTransferInConfirmationV09 MessageDefinition is composed of 9
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
F. Function
Function of the transfer-in, that is, whether the message is used as a reversal of a previously sent
confirmation or as a reversal of a previously sent advice. The absence of Function indicates the
message is a reversal of a previously sent confirmation.
G. ReversalReferences
Reference of the transfer confirmation to be reversed.
Approved by the Securities SEG on 27 January 2026 sese.008.001.09
ReversalOfTransferInConfirmationV09
Investment Funds - Maintenance 2025 - 2026 778 May 2026
```

