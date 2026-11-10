---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.6 CollateralValueReport <CollValRpt>", "3.4.2.1.6.2 CollateralValue <CollVal>", "3.4.2.1.6.2.4 Securities <Scties>", "3.4.2.1.6.2.4.3 ValuationPrice <ValtnPric>", "3.4.2.1.6.2.4.3.1 AmountPriceType <AmtPricTp>"]
file_pages: [37]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.6.2.4.3.1 AmountPriceType <AmtPricTp>

Source: [src-000357](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 37 to 37.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 37

```text
ValuationPrice <ValtnPric> contains the following AmountPricePerFinancialInstrumentQuantity9
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] ± 37
   PriceValue <PricVal> [1..1] ± 37
   FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 37
   PriceFixingDate <PricFxgDt> [1..1] Date 38
3.4.2.1.6.2.4.3.1  AmountPriceType <AmtPricTp>
Presence: [1..1]
Definition: Type of amount price.
AmountPriceType <AmtPricTp> contains one of the following elements (see
"YieldedOrValueType1Choice" on page 60 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 61
Or}   ValueType <ValTp> [1..1] CodeSet 61
3.4.2.1.6.2.4.3.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Value given to a price.
PriceValue <PricVal> contains one of the following elements (see "PriceRateOrAmount3Choice" on
page 71 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 71
Or}   Amount <Amt> [1..1] Amount C2 72
3.4.2.1.6.2.4.3.3  FinancialInstrumentQuantity <FinInstrmQty>
Presence: [1..1]
Definition: Quantity of financial instrument.
FinancialInstrumentQuantity <FinInstrmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 54 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 55
Or   FaceAmount <FaceAmt> [1..1] Amount 55
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 55
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
37 March 2024
```

