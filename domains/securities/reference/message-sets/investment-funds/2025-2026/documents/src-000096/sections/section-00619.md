---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["33 sese.010.001.07 TransferCancellationStatusReportV07", "34.4 Message Building Blocks", "34.4.4 StatusReport <StsRpt>", "34.4.4.6 TransferStatus <TrfSts>", "34.4.4.6.9 CancellationPending <CxlPdg>"]
file_pages: [849]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.011.001.10"]
---

# 34.4.4.6.9 CancellationPending <CxlPdg>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 849 to 849.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 849

```text
Reversed <Rvsd> contains one of the following elements (see "ReversedStatus2Choice" on
page 5261 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5261
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5261
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5261
34.4.4.6.9  CancellationPending <CxlPdg>
Presence: [1..1]
Definition: Status of the transfer is cancellation pending.
CancellationPending <CxlPdg> contains one of the following elements (see
"CancellationPendingStatus7Choice" on page 5260 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5260
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5260
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5260
34.4.4.7  Instrument <Instrm>
Presence: [0..1]
Definition: Identification of the asset.
Approved by the Securities SEG on 27 January 2026 sese.011.001.10
TransferInstructionStatusReportV10
Investment Funds - Maintenance 2025 - 2026 849 May 2026
```

