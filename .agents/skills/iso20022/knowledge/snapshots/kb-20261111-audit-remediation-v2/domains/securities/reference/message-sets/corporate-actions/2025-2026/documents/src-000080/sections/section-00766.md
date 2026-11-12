---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.43 NetDividendRateFormat39Choice"]
file_pages: [959]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.43 NetDividendRateFormat39Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 959 to 959.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 959

```text
16.1.15.43  NetDividendRateFormat39Choice
Definition: Choice between an amount or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 959
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  959
     Amount <Amt> [1..1] Amount C1 960
     RateStatus <RateSts> [1..1] CodeSet 960
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  960
     RateType <RateTp> [1..1]  961
{Or       Code <Cd> [1..1] CodeSet 961
Or}       Proprietary <Prtry> [1..1] ± 962
     Amount <Amt> [1..1] Amount C1 962
     RateStatus <RateSts> [0..1]  C52 962
{Or       Code <Cd> [1..1] CodeSet 963
Or}       Proprietary <Prtry> [1..1] ± 963
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 963
16.1.15.43.1  Amount <Amt>
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
16.1.15.43.2  AmountAndRateStatus <AmtAndRateSts>
Presence: [1..1]
Definition: Specifies an amount and a rate status.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 959 February 2026
```

