---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.10 NetDividendRateFormat40Choice", "16.1.15.10.1 Amount <Amt>"]
file_pages: [901]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.10.1 Amount <Amt>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 901 to 901.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 901

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 901
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  901
     Amount <Amt> [1..1] Amount C1 902
     RateStatus <RateSts> [1..1] CodeSet 902
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  902
     RateType <RateTp> [1..1]  902
{Or       Code <Cd> [1..1] CodeSet 903
Or}       Proprietary <Prtry> [1..1] ± 903
     Amount <Amt> [1..1] Amount C1 904
     RateStatus <RateSts> [0..1]  C52 904
{Or       Code <Cd> [1..1] CodeSet 904
Or}       Proprietary <Prtry> [1..1] ± 905
16.1.15.10.1  Amount <Amt>
Presence: [1..1]
Definition: Value expressed as an amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
16.1.15.10.2  AmountAndRateStatus <AmtAndRateSts>
Presence: [1..1]
Definition: Specifies an amount and a rate status.
AmountAndRateStatus <AmtAndRateSts> contains the following AmountAndRateStatus1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C1 902
   RateStatus <RateSts> [1..1] CodeSet 902
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 901 February 2026
```

