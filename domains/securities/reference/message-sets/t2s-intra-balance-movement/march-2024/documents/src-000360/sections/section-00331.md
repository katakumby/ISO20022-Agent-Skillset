---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.5 Date Period", "17.1.5.2 Period7Choice", "17.1.5.2.1 FromDateTimeToDateTime <FrDtTmToDtTm>"]
file_pages: [397]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.5.2.1 FromDateTimeToDateTime <FrDtTmToDtTm>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 397 to 397.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 397

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTimeToDateTime <FrDtTmToDtTm> [1..1] ± 397
Or}   FromDateToDate <FrDtToDt> [1..1] ± 397
17.1.5.2.1  FromDateTimeToDateTime <FrDtTmToDtTm>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateTimeToDateTime <FrDtTmToDtTm> contains the following elements (see
"DateTimePeriod1" on page 398 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 398
   ToDateTime <ToDtTm> [1..1] DateTime 398
17.1.5.2.2  FromDateToDate <FrDtToDt>
Presence: [1..1]
Definition: Time span defined by a start date and time, and an end date and time.
FromDateToDate <FrDtToDt> contains the following elements (see "Period2" on page 397 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 397
   ToDate <ToDt> [1..1] Date 397
17.1.6 Date Time
17.1.6.1  Period2
Definition: Time span defined by a start date and time, and an end date and time.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 397
   ToDate <ToDt> [1..1] Date 397
17.1.6.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODate" on page 493
17.1.6.1.2  ToDate <ToDt>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
397 March 2024
```

