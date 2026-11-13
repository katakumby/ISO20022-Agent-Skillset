---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.10 Date Time Period"]
file_pages: [323]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.10 Date Time Period

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 323 to 323.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 323

```text
Datatype: "ISODate" on page 550
7.1.10 Date Time Period
7.1.10.1  DateAndPeriod3Choice
Definition: Choice between a date and period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   StatementDate <StmtDt> [1..1] ± 323
Or}   StatementPeriod <StmtPrd> [1..1] ± 323
7.1.10.1.1  StatementDate <StmtDt>
Presence: [1..1]
Definition: Date of the statement.
StatementDate <StmtDt> contains one of the following elements (see "DateAndDateTime2Choice" on
page 321 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 321
Or}   DateTime <DtTm> [1..1] DateTime 321
7.1.10.1.2  StatementPeriod <StmtPrd>
Presence: [1..1]
Definition: Period for the statement.
StatementPeriod <StmtPrd> contains one of the following elements (see "Period7Choice" on
page 317 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 317
Or}   FromDateToDate <FrDtToDt> [1..1] ± 317
7.1.10.2  DateTimePeriod1
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 323
   ToDateTime <ToDtTm> [1..1] DateTime 324
7.1.10.2.1  FromDateTime <FrDtTm>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 323 March 2026
```

