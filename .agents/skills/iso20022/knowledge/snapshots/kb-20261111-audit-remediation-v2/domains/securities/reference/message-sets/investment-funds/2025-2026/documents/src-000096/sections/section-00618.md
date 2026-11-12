---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.6 TransferStatus <TrfSts>", "34.4.4.6.5 Rejected <Rjctd>", "34.4.4.6.5.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [848]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.6.5.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 848 to 848.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 848

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
34.4.4.6.5.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the rejected status reason.
Datatype: "Max350Text" on page 5403
34.4.4.6.6  FailedSettlement <FaildSttlm>
Presence: [1..1]
Definition: Status of the transfer is failed settlement, that is, settlement in the International Central
Securities Depository (ICSD) or Central Securities Depository (CSD) failed.
FailedSettlement <FaildSttlm> contains one of the following elements (see
"FailedSettlementStatus2Choice" on page 5258 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5258
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5258
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5258
34.4.4.6.7  Cancelled <Canc>
Presence: [1..1]
Definition: Status of the transfer is cancelled.
Cancelled <Canc> contains one of the following elements (see "CancelledStatus13Choice" on
page 5257 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5257
Or   Reason <Rsn> [1..1] CodeSet 5257
Or   ExtendedReason <XtndedRsn> [1..1] Text 5257
Or}   DataSourceScheme <DataSrcSchme> [1..1] ± 5258
34.4.4.6.8  Reversed <Rvsd>
Presence: [1..1]
Definition: Status of the transfer is reversed.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 848 May 2026
```

