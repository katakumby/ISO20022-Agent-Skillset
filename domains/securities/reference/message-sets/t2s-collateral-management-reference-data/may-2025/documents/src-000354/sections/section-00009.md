---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 CollateralValue <CollVal>", "2.4.2.2 ValuationDate <ValtnDt>"]
file_pages: [11]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.4.2.2 ValuationDate <ValtnDt>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 11 to 11.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 11

```text
    /ISIN Must be present
 Or    /Description Must be present
2.4.2.2  ValuationDate <ValtnDt>
Presence: [1..1]
Definition: Valuation date for the price.
Datatype: "ISODate" on page 80
2.4.2.3  ValuationCurrency <ValtnCcy>
Presence: [0..1]
Definition: Provides details of the currency of the valuation.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 77
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
2.4.2.4  ValuationPrice <ValtnPric>
Presence: [1..1]
Definition: Provides details of the price provided for the security.
ValuationPrice <ValtnPric> contains one of the following AmountOrCoefficientPrice2Choice
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount 11
Or   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 11
Or}   Coefficient <Coeff> [1..1] Quantity 12
2.4.2.4.1  Amount <Amt>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and implied currency.
Datatype: "ImpliedCurrencyAndAmount" on page 77
2.4.2.4.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and explicit currency.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 76
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 11 May 2025
```

