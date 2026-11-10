---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.30 Yield Calculation", "7.1.30.1 YieldCalculation7", "7.1.30.1.4 ValueDate <ValDt>"]
file_pages: [610]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.30.1.4 ValueDate <ValDt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 610 to 610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 610

```text
RedemptionPrice <RedPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.30.1.4  ValueDate <ValDt>
Presence: [0..1]
Definition: Date/time on which the calculation is based, for example, valuation on October 1 (price date)
based on price of September 19 ( value date).
Datatype: "ISODate" on page 662
7.1.30.1.5  ValuePeriod <ValPrd>
Presence: [0..1]
Definition: Period on which the calculation is based.
ValuePeriod <ValPrd> contains one of the following DateTimePeriod1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   FromDateTime <FrDtTm> [1..1] DateTime 610
Or   ToDateTime <ToDtTm> [1..1] DateTime 610
Or}   DateTimeRange <DtTmRg> [1..1] ± 610
7.1.30.1.5.1  FromDateTime <FrDtTm>
Presence: [1..1]
Definition: Date and time at which the range starts.
Datatype: "ISODateTime" on page 662
7.1.30.1.5.2  ToDateTime <ToDtTm>
Presence: [1..1]
Definition: Date and time at which the range ends.
Datatype: "ISODateTime" on page 662
7.1.30.1.5.3  DateTimeRange <DtTmRg>
Presence: [1..1]
Definition: Range of time between a start date and time and an end date and time.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 610 February 2025
```

