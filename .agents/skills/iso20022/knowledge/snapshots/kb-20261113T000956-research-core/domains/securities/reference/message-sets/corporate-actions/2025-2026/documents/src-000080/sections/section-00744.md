---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.33 GrossDividendRateFormat38Choice", "16.1.15.33.1 Amount <Amt>"]
file_pages: [937]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.33.1 Amount <Amt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 937 to 937.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 937

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 937
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  937
     Amount <Amt> [1..1] Amount C1 938
     RateStatus <RateSts> [1..1] CodeSet 938
Or   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  938
     RateType <RateTp> [1..1]  938
{Or       Code <Cd> [1..1] CodeSet 939
Or}       Proprietary <Prtry> [1..1] ± 940
     Amount <Amt> [1..1] Amount C1 940
     RateStatus <RateSts> [0..1]  C52 940
{Or       Code <Cd> [1..1] CodeSet 940
Or}       Proprietary <Prtry> [1..1] ± 941
Or}   NotSpecifiedRate <NotSpcfdRate> [1..1] CodeSet 941
16.1.15.33.1  Amount <Amt>
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
16.1.15.33.2  AmountAndRateStatus <AmtAndRateSts>
Presence: [1..1]
Definition: Specifies an amount and a rate status.
AmountAndRateStatus <AmtAndRateSts> contains the following AmountAndRateStatus1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 938
   RateStatus <RateSts> [1..1] CodeSet 938
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 937 February 2026
```

