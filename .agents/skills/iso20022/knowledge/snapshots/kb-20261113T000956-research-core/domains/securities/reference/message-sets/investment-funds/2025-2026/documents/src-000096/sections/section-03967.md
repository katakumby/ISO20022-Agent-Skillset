---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.50 Transfer Status", "66.1.50.8 InRepairStatus4Choice"]
file_pages: [5265]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.50.8 InRepairStatus4Choice

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5265 to 5265.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5265

```text
66.1.50.8  InRepairStatus4Choice
Definition: Reason for the in repair status.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Reason <Rsn> [1..1] Text 5265
Or   DataSourceScheme <DataSrcSchme> [1..1] ± 5265
Or}   NoSpecifiedReason <NoSpcfdRsn> [1..1] CodeSet 5265
66.1.50.8.1  Reason <Rsn>
Presence: [1..1]
Definition: Reason for the in-repair status.
Datatype: "Max350Text" on page 5403
66.1.50.8.2  DataSourceScheme <DataSrcSchme>
Presence: [1..1]
Definition: Proprietary identification of the reason for the in-repair status.
DataSourceScheme <DataSrcSchme> contains the following elements (see "GenericIdentification1"
on page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.50.8.3  NoSpecifiedReason <NoSpcfdRsn>
Presence: [1..1]
Definition: Indicates that there is no reason available or to report.
Datatype: "NoReasonCode" on page 5331
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
66.1.50.9  TransferReason1Choice
Definition: Choice between formats for a transfer reason.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 5266
Or}   Proprietary <Prtry> [1..1] ± 5266
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5265 May 2026
```

