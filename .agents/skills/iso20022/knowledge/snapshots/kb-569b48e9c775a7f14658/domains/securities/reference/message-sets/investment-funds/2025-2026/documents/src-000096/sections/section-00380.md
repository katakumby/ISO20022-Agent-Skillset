---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["25 sese.002.001.09 TransferOutCancellationRequestV09", "26.1 MessageDefinition Functionality"]
file_pages: [519, 520]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.003.001.10"]
---

# 26.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 519 to 520.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 519

```text
26 sese.003.001.10
TransferOutConfirmationV10
26.1 MessageDefinition Functionality
The TransferOutConfirmation message is sent by an executing party, for example, a transfer agent, to
the instructing party, for example, an investment manager or its authorised representative, to confirm
the delivery of a financial instrument, free of payment, on a given date, to a specified party.
This message may also be used to confirm the delivery of a financial instrument, free of payment, to
another of the instructing parties own accounts or to a third party.
Usage
The TransferOutConfirmation message is used to confirm the withdrawal of a financial instrument from
the owner's account and its delivery to another own account, or to a third party, has taken place.
The reference of the transfer confirmation is identified in TransferConfirmationReference. The reference
of the original transfer instruction is specified in TransferReference. The message identification of the
TransferOutInstruction message in which the transfer instruction was conveyed may also be quoted in
RelatedReference but this is not recommended.
Outline
The TransferOutConfirmationV10 MessageDefinition is composed of 11 MessageBuildingBlocks:
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
F. TransferDetails
General information related to the transfer of the financial instrument.
G. AccountDetails
Information related to the account from which the financial instrument was withdrawn.
H. SettlementDetails
Information related to the receiving side of the transfer.
I. MarketPracticeVersion
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 519 May 2026
```

## File page 520

```text
Identifies the market practice to which the message conforms.
J. CopyDetails
Information provided when the message is a copy of a previous message.
K. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.003.001.10 TransferOutConfirmationV10
Investment Funds - Maintenance 2025 - 2026 520 May 2026
```

