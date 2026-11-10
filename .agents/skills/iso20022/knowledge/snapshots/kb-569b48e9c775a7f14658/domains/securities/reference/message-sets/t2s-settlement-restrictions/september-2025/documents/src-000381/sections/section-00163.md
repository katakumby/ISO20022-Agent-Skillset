---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.1 MessageComponents", "9.1.5 Date Period", "9.1.5.1 Period7Choice", "9.1.5.1.2 FromDateToDate <FrDtToDt>"]
file_pages: [201]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.1.5.1.2 FromDateToDate <FrDtToDt>

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 201 to 201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 201

```text
FromDateTimeToDateTime <FrDtTmToDtTm> contains the following elements (see
"DateTimePeriod1" on page 205 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 205
   ToDateTime <ToDtTm> [1..1] DateTime 205
9.1.5.1.2  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 205 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 205
   ToDate <ToDt> [1..1] Date 205
9.1.5.2  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 201
   ToDate <ToDt> [1..1] Date 201
9.1.5.2.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 340
9.1.5.2.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 340
9.1.6 Date Time
9.1.6.1  TradeDate8Choice
Definition: Choice of format for the trade date.
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 201 September 2025
```

