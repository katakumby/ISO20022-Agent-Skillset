---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.4 Message Building Blocks", "2.4.2 ReportGeneralDetails <RptGnlDtls>", "2.4.2.5 Frequency <Frqcy>"]
file_pages: [10]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.4.2.5 Frequency <Frqcy>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 10 to 10.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 10

```text
ReportDateTime <RptDtTm> contains one of the following elements (see "DateAndDateTime1Choice"
on page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
2.4.2.5  Frequency <Frqcy>
Presence: [0..1]
Definition: Specifies the regularity of an event.
Frequency <Frqcy> contains one of the following elements (see "Frequency25Choice" on page 274 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 274
Or}   Proprietary <Prtry> [1..1] ± 274
2.4.2.6  UpdateType <UpdTp>
Presence: [0..1]
Definition: Indicates whether the report is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see
"StatementUpdateTypeCodeAndDSSCode1Choice" on page 311 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementUpdateTypeAsCode <StmtUpdTpAsCd> [1..1] CodeSet 311
Or}   StatementUpdateTypeAsDSS <StmtUpdTpAsDSS> [1..1] ± 311
2.4.2.7  NoticeType <NtceTp>
Presence: [0..1]
Definition: Notifies the type of report transmitted.
NoticeType <NtceTp> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 10 February 2025
```

