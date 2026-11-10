---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["25 colr.002.001.02 CollateralValueReportV02", "25.4 Message Building Blocks", "25.4.2 ReportOrError <RptOrErr>", "25.4.2.1 BusinessReport <BizRpt>", "25.4.2.1.6 CollateralValueReport <CollValRpt>"]
file_pages: [601, 602]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 25.4.2.1.6 CollateralValueReport <CollValRpt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 601 to 602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 601

```text
25.4.2.1.6  CollateralValueReport <CollValRpt>
Presence: [0..*]
Definition: Provides information specific to the report on collateral value positions.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 601 August 2026
```

## File page 602

```text
CollateralValueReport <CollValRpt> contains one of the following
CollateralValueReportOrError6Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   BusinessError <BizErr> [1..1]  603
     Error <Err> [1..1]  603
{Or       Code <Cd> [1..1] CodeSet 603
Or}       Proprietary <Prtry> [1..1] Text 603
     Description <Desc> [0..1] Text 603
Or}   CollateralValue <CollVal> [1..1]  603
     DataAccessTime <DataAccsTm> [1..1] DateTime 604
     TotalCollateralValuation <TtlCollValtn> [0..1] Amount C1, C6 604
     SecuritiesAccount <SctiesAcct> [0..1] ± 605
     Securities <Scties> [0..*]  605
       Identification <Id> [0..*] ± C7, C8,
C12,
C13,
C14
606
       Position <Pos> [0..*]  607
         Type <Tp> [1..1] Text 608
         Quantity <Qty> [1..1]  608
{Or           Quantity <Qty> [1..1] ± 609
Or           Proprietary <Prtry> [1..1]  609
             Identification <Id> [1..1] Text 609
             Issuer <Issr> [1..1] Text 609
             SchemeName <SchmeNm> [0..1] Text 609
             Balance <Bal> [1..1] Quantity 609
Or}           QuantityAndAvailability <QtyAndAvlbty> [1..1]  610
             Quantity <Qty> [1..1] ± 610
             AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 610
       ValuationPrice <ValtnPric> [1..1]  610
         AmountPriceType <AmtPricTp> [1..1] ± 611
         PriceValue <PricVal> [1..1] ± 611
         FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 611
         PriceFixingDate <PricFxgDt> [1..1] Date 612
       CollateralValue <CollVal> [1..1] Amount C1, C6 612
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
colr.002.001.02 CollateralValueReportV02
Target2-Securities 602 August 2026
```

