---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.76 InterestRateUsedForPaymentFormat11Choice", "16.1.15.76.1 Rate <Rate>"]
file_pages: [1029]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.76.1 Rate <Rate>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1029 to 1029.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1029

```text
16.1.15.76.1  Rate <Rate>
Presence: [1..1]
Definition: Value is expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.15.76.2  Amount <Amt>
Presence: [1..1]
Definition: Number of monetary units specified in a currency.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.76.3  RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>
Presence: [1..1]
Definition: Specifies different formats for interest rate used for payment.
RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts> contains the following
RateTypeAndAmountAndStatus24 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  1029
{Or     Code <Cd> [1..1] CodeSet 1030
Or}     Proprietary <Prtry> [1..1] ± 1030
   Amount <Amt> [1..1] Amount C1 1030
   RateStatus <RateSts> [0..1]  C52 1030
{Or     Code <Cd> [1..1] CodeSet 1031
Or}     Proprietary <Prtry> [1..1] ± 1031
16.1.15.76.3.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1029 February 2026
```

