---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.4 CommonFinancialInstrumentAttributes10", "13.1.6.4.21 TradingMarket <TradgMkt>", "13.1.6.4.21.7 MinimumTradingPricingIncrement <MinTradgPricgIncrmt>"]
file_pages: [426]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.4.21.7 MinimumTradingPricingIncrement <MinTradgPricgIncrmt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 426 to 426.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 426

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
13.1.6.4.21.7  MinimumTradingPricingIncrement <MinTradgPricgIncrmt>
Presence: [0..1]
Definition: Indicates the minimum or smallest movement (up or down) in the price allowed for the
security.
Datatype: "Number" on page 532
13.1.6.4.21.8  PrimaryPlaceOfListingIdentification <PmryPlcOfListgId>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
Datatype: "MICIdentifier" on page 531
13.1.6.4.22  SpreadAndBenchmarkCurve <SprdAndBchmkCrv>
Presence: [0..*]
Definition: Indicates the spread to benchmark details of an indication of interest.
SpreadAndBenchmarkCurve <SprdAndBchmkCrv> contains the following BenchmarkCurve6
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Spread <Sprd> [0..1] Quantity 426
   BenchmarkIdentification <BchmkId> [0..1] ± C1, C2,
C3, C4,
C5
427
   BenchmarkPrice <BchmkPric> [0..1]  428
     ValueType <ValTp> [0..1] CodeSet 428
     Value <Val> [1..1] ± 429
     PriceType <PricTp> [0..1] CodeSet 429
   BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 430
   BenchmarkCurveName <BchmkCrvNm> [0..1]  430
{Or     Code <Cd> [1..1] CodeSet 430
Or}     Proprietary <Prtry> [1..1] ± 431
   BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 432
13.1.6.4.22.1  Spread <Sprd>
Presence: [0..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 426 March 2024
```

