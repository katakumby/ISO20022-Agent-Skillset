---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07"]
file_pages: [809]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.010.001.07"]
---

# 33 sese.010.001.07 TransferCancellationStatusReportV07

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 809 to 809.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 809

```text
33 sese.010.001.07
TransferCancellationStatusReportV07
33.1 MessageDefinition Functionality
Scope
The TransferCancellationStatusReport message is sent by an executing party, for example, a transfer
agent, to the instructing party, for example, an investment manager or one of its authorised
representatives to provide the status of a previously received transfer cancellation instruction.
Usage
The TransferCancellationStatusReport message is used to report on the status of a transfer in or
transfer out cancellation request.
The reference of the transfer instruction for which the cancellation status is reported is identified in
TransferReference. The message identification of the transfer cancellation request message in which
the transfer instruction was conveyed may also be quoted in RelatedReference.
The message identification of the transfer instruction request message in which the transfer instruction
was conveyed may also be quoted in RelatedReference.
One of the following statuses can be reported:
- the transfer cancellation is accepted, or,
- the transfer cancellation has been sent to the next party, or,
- the transfer cancellation is complete and the reason for the status,
- the transfer cancellation pending and the reason for the status,
- the transfer cancellation is rejected and the reason for the status.
Outline
The TransferCancellationStatusReportV07 MessageDefinition is composed of 6
MessageBuildingBlocks:
A. MessageIdentification
Reference that uniquely identifies the message from a business application standpoint.
B. CounterpartyReference
Unambiguous identification of the transfer allocated by the counterparty.
C. Reference
Reference to the message or communication that was previously received.
D. StatusReport
Status of the transfer cancellation instruction.
E. MarketPracticeVersion
Approved by the Securities SEG on 27 January 2026 sese.010.001.07
TransferCancellationStatusReportV07
Investment Funds - Maintenance 2025 - 2026 809 May 2026
```

