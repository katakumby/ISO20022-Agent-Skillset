---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.30 Yield Calculation", "7.1.30.1 YieldCalculation7", "7.1.30.1.6 CalculationDate <ClctnDt>"]
file_pages: [611]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.30.1.6 CalculationDate <ClctnDt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 611 to 611.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 611

```text
DateTimeRange <DtTmRg> contains the following elements (see "DateTimePeriod1" on page 268 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FromDateTime <FrDtTm> [1..1] DateTime 268
   ToDateTime <ToDtTm> [1..1] DateTime 268
7.1.30.1.6  CalculationDate <ClctnDt>
Presence: [0..1]
Definition: Included as needed to clarify yield irregularities associated with date, e.g. when it falls on a
non-business day.
Datatype: "ISODate" on page 662
7.2 Message Datatypes
7.2.1 Amount
7.2.1.1  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 613
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 611 February 2025
```

