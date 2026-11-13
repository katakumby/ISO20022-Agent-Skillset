---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.5 TransferEventType <TrfEvtTp>", "34.4.4.5.2 Proprietary <Prtry>"]
file_pages: [842]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.5.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 842 to 842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 842

```text
Definition: Type of event expressed as a code.
Datatype: "TransferStatusType2Code" on page 5381
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
34.4.4.5.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of event expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification1" on page 4552 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
34.4.4.6  TransferStatus <TrfSts>
Presence: [1..1]
Definition: Status of the transfer instruction.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 842 May 2026
```

