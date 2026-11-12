---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.6 PendingSettlementStatus3Choice", "66.1.50.6.2 ExtendedReason <XtndedRsn>"]
file_pages: [5264]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.6.2 ExtendedReason <XtndedRsn>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5264 to 5264.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5264

```text
CodeName Name Definition
NRCP TransferAgentNonReceipt Transfer agent claims non-receipt of
physical shares.
FVER FinalVerification Confirmed but finality is to be verified.
66.1.50.6.2  ExtendedReason <XtndedRsn>
Presence: [1..1]
Definition: Reason for the settlement pending status.
Datatype: "Extended350Code" on page 5402
66.1.50.6.3  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the pending settlement status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.50.6.4  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.50.7  TransferCancellationPendingStatus1
Definition: Transfer cancellation status is in pending.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Reason <Rsn> [0..1] Text 5264
66.1.50.7.1  Reason <Rsn>
Presence: [0..1]
Definition: Reason for the cancellation pending status.
Datatype: "Max350Text" on page 5403
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5264 May 2026
```

