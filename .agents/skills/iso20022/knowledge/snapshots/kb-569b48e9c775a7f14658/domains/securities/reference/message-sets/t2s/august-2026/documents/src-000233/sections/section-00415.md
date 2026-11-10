---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["22 camt.084.001.02 IntraBalanceMovementPostingReportV02", "22.4 Message Building Blocks", "22.4.3 ReportGeneralDetails <RptGnlDtls>", "22.4.3.3 ReportIdentification <RptId>"]
file_pages: [530]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 22.4.3.3 ReportIdentification <RptId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 530 to 530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 530

```text
Definition: Identification of the query message sent to request this statement.
Datatype: "Max35Text" on page 3328
22.4.3.3  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 3328
22.4.3.4  ReportDateTime <RptDtTm>
Presence: [0..1]
Definition: Date and time when the report was created.
ReportDateTime <RptDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
22.4.3.5  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the statement.
ReportPeriod <RptPrd> contains one of the following elements (see "Period7Choice" on page 2909
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 2909
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2909
22.4.3.6  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 2958
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2958
Or}   Proprietary <Prtry> [1..1] ± 2959
22.4.3.7  UpdateType <UpdTp>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities 530 August 2026
```

