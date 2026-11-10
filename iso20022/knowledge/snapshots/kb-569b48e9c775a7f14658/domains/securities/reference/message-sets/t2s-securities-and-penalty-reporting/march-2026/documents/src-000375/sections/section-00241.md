---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.8 Date Period", "7.1.8.3 Period7Choice"]
file_pages: [317]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.8.3 Period7Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 317 to 317.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 317

```text
Datatype: "ISODate" on page 550
7.1.8.3  Period7Choice
Definition: Choice between date and date-time for the specification of a period.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 317
Or}   FromDateToDate <FrDtToDt> [1..1] ± 317
7.1.8.3.1  FromDateTimeToDateTime <FrDtTmToDtTm>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateTimeToDateTime <FrDtTmToDtTm> contains the following elements (see
"DateTimePeriod1" on page 323 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 323
   ToDateTime <ToDtTm> [1..1] DateTime 324
7.1.8.3.2  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 322 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 322
   ToDate <ToDt> [1..1] Date 322
7.1.9 Date Time
7.1.9.1  TradeDate8Choice
Definition: Choice of format for the trade date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 318
Or}   DateCode <DtCd> [1..1]  318
{Or     Code <Cd> [1..1] CodeSet 318
Or}     Proprietary <Prtry> [1..1] ± 318
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 317 March 2026
```

