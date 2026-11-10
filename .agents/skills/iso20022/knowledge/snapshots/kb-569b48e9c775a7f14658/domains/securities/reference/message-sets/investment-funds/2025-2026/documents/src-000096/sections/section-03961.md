---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.1 CancelledStatus13Choice", "66.1.50.1.4 DataSourceScheme <DataSrcSchme>"]
file_pages: [5258]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.1.4 DataSourceScheme <DataSrcSchme>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5258 to 5258.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5258

```text
Definition: Reason for the cancelled status.
Datatype: "Extended350Code" on page 5402
66.1.50.1.4  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the cancelled status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.50.2  FailedSettlementStatus2Choice
Definition: Reason for the failed settlement status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5258
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5258
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5258
66.1.50.2.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the failed settlement status.
Datatype: "Max350Text" on page 5403
66.1.50.2.2  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the failed settlement status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.50.2.3  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5258 May 2026
```

