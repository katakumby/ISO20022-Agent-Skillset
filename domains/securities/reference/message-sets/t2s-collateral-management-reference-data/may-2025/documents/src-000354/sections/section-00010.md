---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 CollateralValue <CollVal>", "2.4.2.4 ValuationPrice <ValtnPric>", "2.4.2.4.3 Coefficient <Coeff>"]
file_pages: [12]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.4.2.4.3 Coefficient <Coeff>

Source: [src-000354](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 12 to 12.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 12

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
2.4.2.4.3  Coefficient <Coeff>
Presence: [1..1]
Definition: Provides details of the price when expressed with a coefficient.
Datatype: "DecimalNumber" on page 82
2.4.2.5  ValuationCloseLinkPrice <ValtnClsLkPric>
Presence: [0..1]
Definition: Price of the security as of the valuation date in the collateral valuation currency where there
is a close link between the credit consumer and the security provided as collateral.
ValuationCloseLinkPrice <ValtnClsLkPric> contains one of the following
AmountOrCoefficientPrice2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Amount <Amt> [1..1] Amount 12
Or   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 12
Or}   Coefficient <Coeff> [1..1] Quantity 13
2.4.2.5.1  Amount <Amt>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and implied currency.
Datatype: "ImpliedCurrencyAndAmount" on page 77
2.4.2.5.2  AmountWithCurrency <AmtWthCcy>
Presence: [1..1]
Definition: Provides details of the price when expressed with an amount and explicit currency.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 76
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 12 May 2025
```

