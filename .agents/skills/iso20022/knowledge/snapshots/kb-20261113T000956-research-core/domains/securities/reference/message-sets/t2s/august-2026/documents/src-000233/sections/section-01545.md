---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.4 Message Building Blocks", "44.4.2 CollateralValue <CollVal>", "44.4.2.2 ValuationDate <ValtnDt>"]
file_pages: [2168]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.4.2.2 ValuationDate <ValtnDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2168 to 2168.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2168

```text
    /ISIN Must be present
 Or    /Description Must be present
44.4.2.2  ValuationDate <ValtnDt>
Presence: [1..1]
Definition: Valuation date for the price.
Datatype: "ISODate" on page 3319
44.4.2.3  ValuationCurrency <ValtnCcy>
Presence: [0..1]
Definition: Provides details of the currency of the valuation.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 3212
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
44.4.2.4  ValuationPrice <ValtnPric>
Presence: [1..1]
Definition: Provides details of the price provided for the security.
ValuationPrice <ValtnPric> contains one of the following AmountOrCoefficientPrice2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount 2168
Or   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 2168
Or}   Coefficient <Coeff> [1..1] Quantity 2169
44.4.2.4.1  Amount <Amt>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and implied currency.
Datatype: "ImpliedCurrencyAndAmount" on page 3210
44.4.2.4.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and explicit currency.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 3210
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2168 August 2026
```

