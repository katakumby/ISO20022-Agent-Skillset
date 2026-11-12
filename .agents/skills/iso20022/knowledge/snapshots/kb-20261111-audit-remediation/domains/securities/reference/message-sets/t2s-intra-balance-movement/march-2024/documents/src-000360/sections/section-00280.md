---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["15 camt.084.001.02 IntraBalanceMovementPostingReportV02", "15.4 Message Building Blocks", "15.4.3 ReportGeneralDetails <RptGnlDtls>", "15.4.3.3 ReportIdentification <RptId>"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: ["camt.084.001.02"]
---

# 15.4.3.3 ReportIdentification <RptId>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
Definition: Identification of the query message sent to request this statement.
Datatype: "Max35Text" on page 497
15.4.3.3  ReportIdentification <RptId>
Presence: [0..1]
Definition: Reference common to all pages of a statement.
Datatype: "Max35Text" on page 497
15.4.3.4  ReportDateTime <RptDtTm>
Presence: [0..1]
Definition: Date and time when the report was created.
ReportDateTime <RptDtTm> contains one of the following elements (see "DateAndDateTime2Choice"
on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 398
Or}   DateTime <DtTm> [1..1] DateTime 398
15.4.3.5  ReportPeriod <RptPrd>
Presence: [0..1]
Definition: Period for the statement.
ReportPeriod <RptPrd> contains one of the following elements (see "Period7Choice" on page 396 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 397
Or}   FromDateToDate <FrDtToDt> [1..1] ± 397
15.4.3.6  Frequency <Frqcy>
Presence: [0..1]
Definition: Frequency of the statement.
Frequency <Frqcy> contains one of the following elements (see "Frequency22Choice" on page 407 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 407
Or}   Proprietary <Prtry> [1..1] ± 408
15.4.3.7  UpdateType <UpdTp>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
camt.084.001.02
IntraBalanceMovementPostingReportV02
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
339 March 2024
```

