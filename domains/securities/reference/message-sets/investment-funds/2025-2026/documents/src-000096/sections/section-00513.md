---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10"]
file_pages: [695, 696]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30 sese.007.001.10 TransferInConfirmationV10

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 695 to 696.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 695

```text
30 sese.007.001.10
TransferInConfirmationV10
30.1 MessageDefinition Functionality
Scope
The TransferInConfirmation message is sent by an executing party, for example, a transfer agent, to the
instructing party, for example, an investment manager or its authorised representative, to confirm the
receipt of a financial instrument, free of payment, on a given date, from a specified party.
This message may also be used to confirm the receipt of a financial instrument, free of payment, from
another of the instructing parties own accounts or from a third party.
This message may also be used as an advice, that is, the message is used to provide account
information.
Usage
The TransferInConfirmation message is used to confirm receipt of a financial instrument, either from
another account owned by the instructing party or from a third party. The reference of the transfer
confirmation is identified in TransferConfirmationReference.
The reference of the original transfer instruction is specified in TransferReference. The message
identification of the TransferInInstruction message in which the transfer instruction was conveyed may
also be quoted in RelatedReference.
Outline
The TransferInConfirmationV10 MessageDefinition is composed of 12 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. PoolReference
Collective reference identifying a set of messages.
C. PreviousReference
Reference to a linked message that was previously sent.
D. RelatedReference
Reference to a linked message that was previously received.
E. Function
Function of the transfer in, that is, whether the transfer in message is used as a confirmation or as
or an advice. The absence of Function indicates the message is a confirmation.
F. MasterReference
Unique and unambiguous identifier for a group of individual transfers as assigned by the instructing
party. This identifier links the individual transfers together.
G. TransferDetails
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 695 May 2026
```

## File page 696

```text
General information related to the transfer of the financial instrument.
H. AccountDetails
Information related to the account into which the financial instrument was received.
I. SettlementDetails
Information related to the delivering side of the transfer.
J. MarketPracticeVersion
Identifies the market practice to which the message conforms.
K. CopyDetails
Information provided when the message is a copy of a previous message.
L. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 696 May 2026
```

