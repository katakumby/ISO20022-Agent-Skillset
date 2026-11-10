---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.10 RateAndAmountFormat62Choice", "16.1.22.10.1 Rate <Rate>"]
file_pages: [1111]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.10.1 Rate <Rate>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 1111 to 1111.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1111

```text
16.1.22.10.1  Rate <Rate>
Presence: [1..1]
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.10.2  Amount <Amt>
Presence: [1..1]
Definition: Value is expressed as a currency and amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.22.10.3  RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>
Presence: [1..1]
Definition: Value is expressed as a rate type and an amount.
RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts> contains the following
RateTypeAndAmountAndStatus37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  1111
{Or     Code <Cd> [1..1] CodeSet 1112
Or}     Proprietary <Prtry> [1..1] ± 1112
   Amount <Amt> [1..1] Amount C1 1112
   RateStatus <RateSts> [0..1]  C52 1113
{Or     Code <Cd> [1..1] CodeSet 1113
Or}     Proprietary <Prtry> [1..1] ± 1113
16.1.22.10.3.1  RateType <RateTp>
Presence: [1..1]
Definition: Value expressed as a rate type.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1111 February 2026
```

