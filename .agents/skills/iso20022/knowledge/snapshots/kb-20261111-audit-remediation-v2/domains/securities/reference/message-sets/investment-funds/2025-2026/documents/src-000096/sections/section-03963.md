---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.3 CancelledCompleteReason1", "66.1.50.3.2 AdditionalReasonInformation <AddtlRsnInf>"]
file_pages: [5260]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.3.2 AdditionalReasonInformation <AddtlRsnInf>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5260 to 5260.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5260

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification36" on page 4549 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4549
   Issuer <Issr> [1..1] Text 4550
   SchemeName <SchmeNm> [0..1] Text 4550
66.1.50.3.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Additional information about the cancelled complete status reason.
Datatype: "Max350Text" on page 5403
66.1.50.4  CancellationPendingStatus7Choice
Definition: Reason for the cancellation pending status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5260
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5260
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5260
66.1.50.4.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the cancellation pending status.
Datatype: "Max350Text" on page 5403
66.1.50.4.2  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the cancellation pending status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.50.4.3  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5260 May 2026
```

