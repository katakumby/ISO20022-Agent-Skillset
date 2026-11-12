---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.14 GrossDividendRateFormat37Choice"]
file_pages: [909]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.14 GrossDividendRateFormat37Choice

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 909 to 909.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 909

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.14  GrossDividendRateFormat37Choice
Definition: Choice of format to express a gross dividend.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 909
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  910
     Amount <Amt> [1..1] Amount C1 910
     RateStatus <RateSts> [1..1] CodeSet 910
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  910
     RateType <RateTp> [1..1]  911
{Or       Code <Cd> [1..1] CodeSet 911
Or}       Proprietary <Prtry> [1..1] ± 912
     Amount <Amt> [1..1] Amount C1 912
     RateStatus <RateSts> [0..1]  C52 913
{Or       Code <Cd> [1..1] CodeSet 913
Or}       Proprietary <Prtry> [1..1] ± 913
16.1.15.14.1  Amount <Amt>
Presence: [1..1]
Definition: Value expressed as an amount.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 909 February 2026
```

