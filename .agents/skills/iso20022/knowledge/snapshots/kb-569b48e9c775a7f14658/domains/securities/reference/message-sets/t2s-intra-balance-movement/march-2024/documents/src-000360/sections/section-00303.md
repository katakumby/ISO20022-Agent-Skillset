---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["16 camt.085.001.02 IntraBalanceMovementPendingReportV02", "16.4 Message Building Blocks", "16.4.3 ReportGeneralDetails <RptGnlDtls>", "16.4.3.2 QueryReference <QryRef>"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.085.001.02"]
---

# 16.4.3.2 QueryReference <QryRef>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
ReportNumber <RptNb> contains one of the following elements (see "Number3Choice" on page 410
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 410
Or}   Long <Lng> [1..1] Text 410
16.4.3.2  QueryReference <QryRef>
Presence: [0..1]
Definition: Identification of the query message sent to request this statement.
Datatype: "Max35Text" on page 497
16.4.3.3  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 497
16.4.3.4  ReportDateTime <RptDtTm>
Presence: [0..1]
Definition: Date and time when the report was created.
ReportDateTime <RptDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 398
Or}   DateTime <DtTm> [1..1] DateTime 398
16.4.3.5  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the statement.
ReportPeriod <RptPrd> contains one of the following elements (see "Period7Choice" on page 396 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 397
Or}   FromDateToDate <FrDtToDt> [1..1] ± 397
16.4.3.6  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.085.001.02
IntraBalanceMovementPendingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
366 March 2024
```

