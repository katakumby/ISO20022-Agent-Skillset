---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.4 Amount Range", "17.1.4.2 AmountRangeBoundary1", "17.1.4.2.1 BoundaryAmount <BdryAmt>"]
file_pages: [396]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.4.2.1 BoundaryAmount <BdryAmt>

Source: [src-000360](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 396 to 396.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 396

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BoundaryAmount <BdryAmt> [1..1] Amount 396
   Included <Incl> [1..1] Indicator 396
17.1.4.2.1  BoundaryAmount <BdryAmt>
Presence: [1..1]
Definition: Amount value of the range limit.
Datatype: "ImpliedCurrencyAndAmount" on page 474
17.1.4.2.2  Included <Incl>
Presence: [1..1]
Definition: Indicates whether the boundary amount is included in the range of amount values.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 495):
• Meaning When True: Yes
• Meaning When False: No
17.1.5 Date Period
17.1.5.1  DatePeriod2
Definition: Range of time defined by a start date and an end date.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDate <FrDt> [1..1] Date 396
   ToDate <ToDt> [1..1] Date 396
17.1.5.1.1  FromDate <FrDt>
Presence: [1..1]
Definition: Start date of the range.
Datatype: "ISODate" on page 493
17.1.5.1.2  ToDate <ToDt>
Presence: [1..1]
Definition: End date of the range.
Datatype: "ISODate" on page 493
17.1.5.2  Period7Choice
Definition: Choice between date and date-time for the specification of a period.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
396 March 2024
```

