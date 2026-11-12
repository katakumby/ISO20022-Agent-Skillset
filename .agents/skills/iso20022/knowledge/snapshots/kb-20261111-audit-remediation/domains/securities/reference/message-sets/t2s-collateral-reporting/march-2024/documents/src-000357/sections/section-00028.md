---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CollateralReporting"
source_ids: ["src-000357"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["3 colr.002.001.02 CollateralValueReportV02", "3.4 Message Building Blocks", "3.4.2 ReportOrError <RptOrErr>", "3.4.2.1 BusinessReport <BizRpt>", "3.4.2.1.6 CollateralValueReport <CollValRpt>", "3.4.2.1.6.2 CollateralValue <CollVal>", "3.4.2.1.6.2.4 Securities <Scties>", "3.4.2.1.6.2.4.1 Identification <Id>"]
file_pages: [32]
content_origin: "source-text-extraction"
mentioned_message_ids: ["colr.002.001.02"]
---

# 3.4.2.1.6.2.4.1 Identification <Id>

Source: [src-000357](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CollateralReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_CollateralReporting_2023_2024_v1.pdf`. Locator: one-based file pages 32 to 32.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 32

```text
Securities <Scties> contains the following SecurityCharacteristics3 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..*] ± C7, C8,
C12,
C13,
C14
32
   Position <Pos> [0..*]  33
     Type <Tp> [1..1] Text 34
     Quantity <Qty> [1..1]  34
{Or       Quantity <Qty> [1..1] ± 35
Or       Proprietary <Prtry> [1..1]  35
         Identification <Id> [1..1] Text 35
         Issuer <Issr> [1..1] Text 35
         SchemeName <SchmeNm> [0..1] Text 35
         Balance <Bal> [1..1] Quantity 35
Or}       QuantityAndAvailability <QtyAndAvlbty> [1..1]  36
         Quantity <Qty> [1..1] ± 36
         AvailabilityIndicator <AvlbtyInd> [1..1] Indicator 36
   ValuationPrice <ValtnPric> [1..1]  36
     AmountPriceType <AmtPricTp> [1..1] ± 37
     PriceValue <PricVal> [1..1] ± 37
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± 37
     PriceFixingDate <PricFxgDt> [1..1] Date 38
   CollateralValue <CollVal> [1..1] Amount C1, C6 38
3.4.2.1.6.2.4.1  Identification <Id>
Presence: [0..*]
Definition: Unique identification, as known by the account owner, to unambiguously identify the security.
Impacted by: C7 "DescriptionPresenceRule", C8 "DescriptionUsageRule", C12 "ISINGuideline", C13
"ISINPresenceRule", C14 "OtherIdentificationPresenceRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
colr.002.001.02 CollateralValueReportV02
Target2-Securities - Collateral Reporting - Maintenance 2023
- 2024
32 March 2024
```

