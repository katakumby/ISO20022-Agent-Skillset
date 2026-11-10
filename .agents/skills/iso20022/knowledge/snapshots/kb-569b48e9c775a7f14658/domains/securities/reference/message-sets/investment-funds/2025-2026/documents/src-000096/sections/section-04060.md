---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.2 CodeSet", "66.2.2.240 TransferStatusType2Code"]
file_pages: [5381]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.2.240 TransferStatusType2Code

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5381 to 5381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5381

```text
CodeName Name Definition
COMP Complete Portfolio transfer is complete.
DELY Delayed Transfer or settlement instruction is
delayed.
MACH Matched Transfer or settlement instruction is
matched.
RECE Received Instruction has been received, that is,
technical validation of the message is ok,
and the message is now at the receiving
side.
STNP SentToNextParty Transfer or settlement instruction has
been sent to the next party, that is, the
next intermediary.
SETT Settled Transfer or settlement instruction is
settled.
66.2.2.240  TransferStatusType2Code
Definition: Specifies a type of transfer status or transfer event.
Type: CodeSet
CodeName Name Definition
S019 AccountHoldingInformationRequest Status report is sent in response to an
account holding information request.
BCEV BenefitCrystallisationEvent Status report advises one or more
Benefit Crystallisation Events (BCE)
have occurred.
SETT CSDorICSDSettlementInformation Status report is sent to provide
information required for a CSD or ICSD
settlement leg.
DRAW Drawdown Status report advises one or more
drawdowns.
PAYA PaymentAdvice Status report advises cash is or has
been instructed.
S012 PortfolioTransferInstruction Status report is sent in response to a
portfolio transfer instruction.
INFO Information Status report is sent to provide
information pertinent to the transfer. May
be sent in response to a request for
transfer status.
STAT Status Status report is sent to provide the status
of a transfer. May be sent in response to
a request for transfer status.
S005 TransferInInstruction Status report is sent in response to a
transfer-in instruction.
S001 TransferOutInstruction Status report is sent in response to a
transfer-out instruction.
CONV ConversionStatus Status report is sent to provide the
number of units following a conversion.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5381 May 2026
```

