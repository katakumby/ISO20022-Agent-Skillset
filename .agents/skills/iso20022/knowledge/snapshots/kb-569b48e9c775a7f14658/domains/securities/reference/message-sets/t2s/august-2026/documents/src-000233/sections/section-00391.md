---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["21 camt.083.001.02 IntraBalanceMovementCancellationReportV02", "21.4 Message Building Blocks", "21.4.3 ReportGeneralDetails <RptGnlDtls>", "21.4.3.5 ReportPeriod <RptPrd>"]
file_pages: [500]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.083.001.02"]
---

# 21.4.3.5 ReportPeriod <RptPrd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 500 to 500.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 500

```text
21.4.3.5  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the statement.
ReportPeriod <RptPrd> contains one of the following elements (see "Period7Choice" on page 2909
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 2909
Or}   FromDateToDate <FrDtToDt> [1..1] ± 2909
21.4.3.6  QueryType <QryTp>
Presence: [0..1]
Definition: Defines the type of query.
Datatype: "MovementResponseType1Code" on page 3264
CodeName Name Definition
FULL Full Response will include full details on the
movements reported.
STTS Status Response will include limited details
including the status on the movements
reported.
21.4.3.7  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 2958
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2958
Or}   Proprietary <Prtry> [1..1] ± 2959
21.4.3.8  UpdateType <UpdTp>
Presence: [1..1]
Definition: Indicates whether the statement is complete or contains changes only.
UpdateType <UpdTp> contains one of the following elements (see "UpdateType15Choice" on
page 3045 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3045
Or}   Proprietary <Prtry> [1..1] ± 3045
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
camt.083.001.02
IntraBalanceMovementCancellationReportV02
Target2-Securities 500 August 2026
```

