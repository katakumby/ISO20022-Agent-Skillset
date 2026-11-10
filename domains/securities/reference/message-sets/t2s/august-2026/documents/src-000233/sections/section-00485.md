---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.6 CollateralValueReport <CollValRpt>", "25.4.2.1.6.2 CollateralValue <CollVal>", "25.4.2.1.6.2.4 Securities <Scties>", "25.4.2.1.6.2.4.3 ValuationPrice <ValtnPric>", "25.4.2.1.6.2.4.3.1 AmountPriceType <AmtPricTp>"]
file_pages: [611]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.6.2.4.3.1 AmountPriceType <AmtPricTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 611 to 611.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 611

```text
ValuationPrice <ValtnPric> contains the following AmountPricePerFinancialInstrumentQuantity9
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] ± 611
   PriceValue <PricVal> [1..1] ± 611
   FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 611
   PriceFixingDate <PricFxgDt> [1..1] Date 612
25.4.2.1.6.2.4.3.1  AmountPriceType <AmtPricTp>
Presence: [1..1]
Definition: Type of amount price.
AmountPriceType <AmtPricTp> contains one of the following elements (see
"YieldedOrValueType1Choice" on page 3025 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Yielded <Yldd> [1..1] Indicator 3025
Or}   ValueType <ValTp> [1..1] CodeSet 3025
25.4.2.1.6.2.4.3.2  PriceValue <PricVal>
Presence: [1..1]
Definition: Value given to a price.
PriceValue <PricVal> contains one of the following elements (see "PriceRateOrAmount3Choice" on
page 3102 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] Rate 3102
Or}   Amount <Amt> [1..1] Amount C1 3102
25.4.2.1.6.2.4.3.3  FinancialInstrumentQuantity <FinInstrmQty>
Presence: [1..1]
Definition: Quantity of financial instrument.
FinancialInstrumentQuantity <FinInstrmQty> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 611 August 2026
```

