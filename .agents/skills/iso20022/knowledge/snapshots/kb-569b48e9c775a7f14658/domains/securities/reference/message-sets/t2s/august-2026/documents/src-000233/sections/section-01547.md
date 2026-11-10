---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["44 reda.024.001.01 CollateralValueCreationRequestV01", "44.4 Message Building Blocks", "44.4.2 CollateralValue <CollVal>", "44.4.2.5 ValuationCloseLinkPrice <ValtnClsLkPric>", "44.4.2.5.3 Coefficient <Coeff>"]
file_pages: [2170]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.024.001.01"]
---

# 44.4.2.5.3 Coefficient <Coeff>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2170 to 2170.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2170

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
44.4.2.5.3  Coefficient <Coeff>
Presence: [1..1]
Definition: Provides details of the price when expressed with a coefficient.
Datatype: "DecimalNumber" on page 3324
44.4.2.6  CleanPrice <CleanPric>
Presence: [0..1]
Definition: Price excluding the accrued interest.
CleanPrice <CleanPric> contains one of the following elements (see "PriceRateOrAmount6Choice" on
page 3106 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3106
Or   Amount <Amt> [1..1] Amount 3106
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C5 3106
44.4.2.7  AccruedInterest <AcrdIntrst>
Presence: [0..1]
Definition: Amount of money or rate accrued interest computed in the case of interest bearing financial
instruments.
AccruedInterest <AcrdIntrst> contains one of the following elements (see
"PriceRateOrAmount6Choice" on page 3106 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3106
Or   Amount <Amt> [1..1] Amount 3106
Or}   AmountWithCurrency <AmtWthCcy> [1..1] Amount C1, C5 3106
44.4.2.8  Haircut <Hrcut>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.024.001.01
CollateralValueCreationRequestV01
Target2-Securities 2170 August 2026
```

