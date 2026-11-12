---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["2 semt.023.001.02 SecuritiesEndOfProcessReportV02", "2.4 Message Building Blocks", "2.4.2 ReportGeneralDetails <RptGnlDtls>"]
file_pages: [9]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.023.001.02"]
---

# 2.4.2 ReportGeneralDetails <RptGnlDtls>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 9 to 9.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 9

```text
2.4.2 ReportGeneralDetails <RptGnlDtls>
Presence: [1..1]
Definition: Notifies the type of report transmitted.
ReportGeneralDetails <RptGnlDtls> contains the following Report6 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportNumber <RptNb> [0..1] Text 9
   QueryReference <QryRef> [0..1] ± 9
   ReportIdentification <RptId> [0..1] Text 9
   ReportDateTime <RptDtTm> [1..1] ± 9
   Frequency <Frqcy> [0..1] ± 10
   UpdateType <UpdTp> [0..1] ± 10
   NoticeType <NtceTp> [0..1] ± 10
2.4.2.1  ReportNumber <RptNb>
Presence: [0..1]
Definition: Sequential number of the report.
Datatype: "Max5NumericText" on page 669
2.4.2.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Gives the name and the reference of the query.
QueryReference <QryRef> contains the following elements (see "QueryReference2" on page 377 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   QueryReference <QryRef> [1..1] Text 378
   QueryName <QryNm> [0..1] Text 378
2.4.2.3  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference of the report.
Datatype: "Max35Text" on page 669
2.4.2.4  ReportDateTime <RptDtTm>
Presence: [1..1]
Definition: Date of the statement.
Approved by the Securities SEG on 13 February 2025 semt.023.001.02
SecuritiesEndOfProcessReportV02
Post Trade Matching - Maintenance 2024 - 2025 9 February 2025
```

