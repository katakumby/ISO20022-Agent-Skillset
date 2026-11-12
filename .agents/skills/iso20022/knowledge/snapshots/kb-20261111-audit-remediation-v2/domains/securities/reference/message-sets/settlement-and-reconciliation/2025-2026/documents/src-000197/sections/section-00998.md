---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.7 Date Period", "35.1.7.1 Period7Choice", "35.1.7.1.1 FromDateTimeToDateTime <FrDtTmToDtTm>"]
file_pages: [1435]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.7.1.1 FromDateTimeToDateTime <FrDtTmToDtTm>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1435 to 1435.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1435

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 1435
Or}   FromDateToDate <FrDtToDt> [1..1] ± 1435
35.1.7.1.1  FromDateTimeToDateTime <FrDtTmToDtTm>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateTimeToDateTime <FrDtTmToDtTm> contains the following elements (see
"DateTimePeriod1" on page 1443 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 1443
   ToDateTime <ToDtTm> [1..1] DateTime 1443
35.1.7.1.2  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 1442 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 1442
   ToDate <ToDt> [1..1] Date 1442
35.1.8 Date Time
35.1.8.1  TradeDate8Choice
Definition: Choice of format for the trade date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] ± 1435
Or}   DateCode <DtCd> [1..1]  1436
{Or     Code <Cd> [1..1] CodeSet 1436
Or}     Proprietary <Prtry> [1..1] ± 1436
35.1.8.1.1  Date <Dt>
Presence: [1..1]
Definition: Date expressed as an ISO date.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1435 March 2026
```

