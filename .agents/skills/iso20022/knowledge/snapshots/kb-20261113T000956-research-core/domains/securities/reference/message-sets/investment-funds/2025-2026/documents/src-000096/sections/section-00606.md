---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.1 MessageDefinition Functionality"]
file_pages: [816]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.1 MessageDefinition Functionality

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 816 to 816.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 816

```text
34 sese.011.001.10
TransferInstructionStatusReportV10
34.1 MessageDefinition Functionality
Scope
The TransferInstructionStatusReport message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or one of its authorised
representatives to provide the status of a previously received request for holdings information, portfolio
transfer or transfer instruction.
It may also be used to report the status of an event related to the asset being transferred or provide
additional information.
The TransferInstructionStatusReport message may also be sent by any party in the transfer transaction
to another party in the transfer transaction chain to provide information relevant for the settlement of a
transfer transaction.
Usage
The TransferInstructionStatusReport message is used to provide the status of a previously received
request for holdings information, portfolio transfer or transfer instruction, or in response to a
RequestForTransferStatus message. It may also be used to report the status of an event related to the
asset being transferred or provide additional information.
Outline
The TransferInstructionStatusReportV10 MessageDefinition is composed of 6 MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. CounterpartyReference
Unambiguous identification of the transfer allocated by the counterparty.
C. Reference
Reference to the message or communication that was previously received.
D. StatusReport
Status of the transfer instruction.
E. MarketPracticeVersion
Identifies the market practice to which the message conforms.
F. Extension
Additional information that cannot be captured in the structured elements and/or any other specific
block.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 816 May 2026
```

