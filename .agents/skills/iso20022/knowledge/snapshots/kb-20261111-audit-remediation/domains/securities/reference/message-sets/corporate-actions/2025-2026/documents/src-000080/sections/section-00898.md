---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.22 Rate", "16.1.22.11 RateAndAmountFormat61Choice", "16.1.22.11.2 Amount <Amt>"]
file_pages: [1116]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.22.11.2 Amount <Amt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1116 to 1116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1116

```text
Definition: Value expressed as a rate.
Datatype: "Percentage14Rate" on page 1247
16.1.22.11.2  Amount <Amt>
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
16.1.22.11.3  NotSpecifiedRate <NotSpcfdRate>
Presence: [1..1]
Definition: Value of the rate not specified.
Datatype: "RateValueType7Code" on page 1235
CodeName Name Definition
UKWN Unknown Rate is unknown by the sender or has
not been established.
16.1.22.11.4  RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts>
Presence: [1..1]
Definition: Value is expressed as a rate type and an amount.
RateTypeAndAmountAndRateStatus <RateTpAndAmtAndRateSts> contains the following
RateTypeAndAmountAndStatus37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateType <RateTp> [1..1]  1116
{Or     Code <Cd> [1..1] CodeSet 1117
Or}     Proprietary <Prtry> [1..1] ± 1117
   Amount <Amt> [1..1] Amount C1 1117
   RateStatus <RateSts> [0..1]  C52 1118
{Or     Code <Cd> [1..1] CodeSet 1118
Or}     Proprietary <Prtry> [1..1] ± 1118
16.1.22.11.4.1  RateType <RateTp>
Presence: [1..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1116 February 2026
```

