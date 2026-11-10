---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.15 Miscellaneous", "16.1.15.8 NetDividendRateFormat37Choice"]
file_pages: [895]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.15.8 NetDividendRateFormat37Choice

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 895 to 895.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 895

```text
Definition: Proprietary identification of the type of fraction disposition.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 879 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 879
   Issuer <Issr> [1..1] Text 879
   SchemeName <SchmeNm> [0..1] Text 880
16.1.15.8  NetDividendRateFormat37Choice
Definition: Choice between an amount or an unspecified rate.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount C1 895
Or   AmountAndRateStatus <AmtAndRateSts> [1..1]  896
     Amount <Amt> [1..1] Amount C1 896
     RateStatus <RateSts> [1..1] CodeSet 896
Or}   RateTypeAndAmountAndRateStatus
<RateTpAndAmtAndRateSts>
[1..1]  896
     RateType <RateTp> [1..1]  897
{Or       Code <Cd> [1..1] CodeSet 897
Or}       Proprietary <Prtry> [1..1] ± 898
     Amount <Amt> [1..1] Amount C1 898
     RateStatus <RateSts> [0..1]  C52 898
{Or       Code <Cd> [1..1] CodeSet 899
Or}       Proprietary <Prtry> [1..1] ± 899
16.1.15.8.1  Amount <Amt>
Presence: [1..1]
Definition: Number of monetary units specified in a currency.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyAnd13DecimalAmount" on page 1155
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 895 February 2026
```

