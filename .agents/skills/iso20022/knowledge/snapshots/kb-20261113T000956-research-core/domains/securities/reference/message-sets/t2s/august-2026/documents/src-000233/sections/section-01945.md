---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["76 semt.031.001.01 SecuritiesSettlementConditionsModificationRequestReportV01", "76.4 Message Building Blocks", "76.4.2 ReportGeneralDetails <RptGnlDtls>", "76.4.2.3 ReportIdentification <RptId>"]
file_pages: [2660]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.031.001.01"]
---

# 76.4.2.3 ReportIdentification <RptId>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2660 to 2660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2660

```text
76.4.2.3  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 3328
76.4.2.4  ReportDateTime <RptDtTm>
Presence: [0..1]
Definition: Date and time when the report was created.
ReportDateTime <RptDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 2914 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2914
Or}   DateTime <DtTm> [1..1] DateTime 2914
76.4.2.5  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the statement.
ReportPeriod <RptPrd> contains one of the following elements (see "Period7Choice" on page 2909
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 2909
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2909
76.4.2.6  QueryType <QryTp>
Presence: [0..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 3264
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
76.4.2.7  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.031.001.01
SecuritiesSettlementConditionsModificationRequest
ReportV01
Target2-Securities 2660 August 2026
```

