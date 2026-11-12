---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["24 sese.001.001.10 TransferOutInstructionV10"]
file_pages: [433, 434]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.001.001.10"]
---

# 24 sese.001.001.10 TransferOutInstructionV10

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 433 to 434.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 433

```text
24 sese.001.001.10
TransferOutInstructionV10
24.1 MessageDefinition Functionality
Scope
The TransferOutInstruction message is sent by an instructing party, for example, an investment
manager or its authorised representative, to the executing party, for example, a transfer agent, to
instruct the delivery of a financial instrument, free of payment, on a given date from a specified party.
This message may also be used to instruct the delivery of a financial instrument, free of payment, to
another of the instructing parties own accounts or to a third party.
Usage
The TransferOutInstruction message is used to instruct the withdrawal of a financial instrument from
one account and deliver it to either another account or to a third party.
Outline
The TransferOutInstructionV10 MessageDefinition is composed of 11 MessageBuildingBlocks:
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
Information related to the account from which the financial instrument is to be withdrawn.
H. SettlementDetails
Information related to the receiving side of the transfer.
I. MarketPracticeVersion
Identifies the market practice to which the message conforms.
J. CopyDetails
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 433 May 2026
```

## File page 434

```text
Information provided when the message is a copy of a previous message.
K. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.001.001.10 TransferOutInstructionV10
Investment Funds - Maintenance 2025 - 2026 434 May 2026
```

