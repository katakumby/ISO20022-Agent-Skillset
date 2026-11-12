---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralManagementReferenceData"
source_ids: ["src-000354"]
source_editions: ["may-2025"]
message_ids: []
heading_path: ["2 reda.024.001.01 CollateralValueCreationRequestV01", "2.4 Message Building Blocks", "2.4.2 CollateralValue <CollVal>", "2.4.2.5 ValuationCloseLinkPrice <ValtnClsLkPric>", "2.4.2.5.3 Coefficient <Coeff>"]
file_pages: [13]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 2.4.2.5.3 Coefficient <Coeff>

Source: [src-000354](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralManagementReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralManagementReferenceData_v1.pdf`. Locator: one-based file pages 13 to 13.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 13

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
2.4.2.5.3  Coefficient <Coeff>
Presence: [1..1]
Definition: Provides details of the price when expressed with a coefficient.
Datatype: "DecimalNumber" on page 82
2.4.2.6  CleanPrice <CleanPric>
Presence: [0..1]
Definition: Price excluding the accrued interest.
CleanPrice <CleanPric> contains one of the following elements (see "PriceRateOrAmount6Choice" on
page 75 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 75
Or   Amount <Amt> [1..1] Amount 75
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 75
2.4.2.7  AccruedInterest <AcrdIntrst>
Presence: [0..1]
Definition: Amount of money or rate accrued interest computed in the case of interest bearing financial
instruments.
AccruedInterest <AcrdIntrst> contains one of the following elements (see
"PriceRateOrAmount6Choice" on page 75 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 75
Or   Amount <Amt> [1..1] Amount 75
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C2, C5 75
2.4.2.8  Haircut <Hrcut>
Presence: [0..1]
Approved by the Securities SEG on 17 April 2025. reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities - Collateral Management Reference Data 13 May 2025
```

