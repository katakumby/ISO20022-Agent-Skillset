---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.6 TransferStatus <TrfSts>", "34.4.4.6.3 Unmatched <Umtchd>"]
file_pages: [844]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.6.3 Unmatched <Umtchd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 844 to 844.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 844

```text
PendingSettlement <PdgSttlm> contains one of the following elements (see
"PendingSettlementStatus3Choice" on page 5261 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] CodeSet 5262
Or   ExtendedReason <XtndedRsn> [1..1] Text 5264
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5264
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5264
34.4.4.6.3  Unmatched <Umtchd>
Presence: [1..1]
Definition: Status of the transfer is unmatched.
Unmatched <Umtchd> contains one of the following elements (see
"TransferUnmatchedStatus4Choice" on page 5196 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5197
Or   Reason <Rsn> [1..1] CodeSet 5197
Or   ExtendedReason <XtndedRsn> [1..1] Text 5197
Or}   DataSourceScheme <DataSrcSchme> [1..1] ± 5198
34.4.4.6.4  InRepair <InRpr>
Presence: [1..1]
Definition: Status of the transfer is in repair.
InRepair <InRpr> contains one of the following elements (see "InRepairStatus4Choice" on page 5265
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5265
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5265
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5265
34.4.4.6.5  Rejected <Rjctd>
Presence: [1..10]
Definition: Status of the transfer is rejected.
Impacted by: C25 "OtherRule"
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 844 May 2026
```

