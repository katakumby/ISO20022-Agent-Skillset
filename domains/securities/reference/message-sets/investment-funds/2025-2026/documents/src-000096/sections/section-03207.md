---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.1 Fees2", "66.1.8.1.2 IndividualFee <IndvFee>", "66.1.8.1.2.4 DiscountDetails <DscntDtls>", "66.1.8.1.2.4.1 Amount <Amt>"]
file_pages: [4439]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.1.2.4.1 Amount <Amt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4439 to 4439.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4439

```text
DiscountDetails <DscntDtls> contains the following ChargeOrCommissionDiscount2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [0..1] Amount C1, C13 4439
   Rate <Rate> [0..1] Rate 4439
   Basis <Bsis> [0..1]  4439
{Or     Code <Cd> [1..1] CodeSet 4440
Or}     Proprietary <Prtry> [1..1] ± 4440
Constraints
• DiscountElementRule
Amount Or Rate Or Basis must be present.
Following Must be True
    /Amount Must be present
 Or    /Rate Must be present
 Or    /Basis Must be present
66.1.8.1.2.4.1  Amount <Amt>
Presence: [0..1]
Definition: Amount of discount or waiver.
Impacted by: C1 "ActiveCurrency", C13 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 5268
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.1.8.1.2.4.2  Rate <Rate>
Presence: [0..1]
Definition: Rate of discount or waiver.
Datatype: "PercentageRate" on page 5401
66.1.8.1.2.4.3  Basis <Bsis>
Presence: [0..1]
Definition: Form of the discount or rebate.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4439 May 2026
```

