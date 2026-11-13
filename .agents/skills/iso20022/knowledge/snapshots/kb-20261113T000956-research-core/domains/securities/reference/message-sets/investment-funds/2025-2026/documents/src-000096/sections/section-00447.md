---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.1 MessageDefinition Functionality"]
file_pages: [608, 609]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 608 to 609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 608

```text
28 sese.005.001.10
TransferInInstructionV10
28.1 MessageDefinition Functionality
The TransferInInstruction message is sent by an instructing party, for example, an investment manager
or its authorised representative, to the executing party, for example, a transfer agent, to instruct the
receipt of a financial instrument, free of payment, on a given date from a specified party.
This message may also be used to instruct the receipt of a financial instrument, free of payment, from
another of the instructing parties own accounts or from a third party.
Usage
The TransferInInstruction message is used to instruct the receipt of a financial instrument from another
account, either owned by the instructing party or by a third party.
Outline
The TransferInInstructionV10 MessageDefinition is composed of 12 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. Function
Function of the transfer in, that is, whether the transfer in message is used as an instruction or an
advice and request for information. The absence of Function indicates the message is an
instruction.
F. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
G. TransferDetails
General information related to the transfer of the financial instrument.
H. AccountDetails
Information related to the account into which the financial instrument is to be received.
I. SettlementDetails
Information related to the delivering side of the transfer.
J. MarketPracticeVersion
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 608 May 2026
```

## File page 609

```text
Identifies the market practice to which the message conforms.
K. CopyDetails
Information provided when the message is a copy of a previous message.
L. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 609 May 2026
```

