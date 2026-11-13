---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.4 Message Building Blocks", "44.4.2 CollateralValue <CollVal>", "44.4.2.4 ValuationPrice <ValtnPric>", "44.4.2.4.3 Coefficient <Coeff>"]
file_pages: [2169]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.4.2.4.3 Coefficient <Coeff>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2169 to 2169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2169

```text
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
44.4.2.4.3  Coefficient <Coeff>
Presence: [1..1]
Definition: Provides details of the price when expressed with a coefficient.
Datatype: "DecimalNumber" on page 3324
44.4.2.5  ValuationCloseLinkPrice <ValtnClsLkPric>
Presence: [0..1]
Definition: Price of the security as of the valuation date in the collateral valuation currency where there
is a close link between the credit consumer and the security provided as collateral.
ValuationCloseLinkPrice <ValtnClsLkPric> contains one of the following
AmountOrCoefficientPrice2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount 2169
Or   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 2169
Or}   Coefficient <Coeff> [1..1] Quantity 2170
44.4.2.5.1  Amount <Amt>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and implied currency.
Datatype: "ImpliedCurrencyAndAmount" on page 3210
44.4.2.5.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and explicit currency.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 3210
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2169 August 2026
```

