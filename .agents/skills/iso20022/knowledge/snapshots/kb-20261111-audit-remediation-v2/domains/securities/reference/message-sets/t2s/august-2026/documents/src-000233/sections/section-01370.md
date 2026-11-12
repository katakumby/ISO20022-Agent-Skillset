---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.19 TradingMarket <TradgMkt>", "32.4.3.1.1.3.19.7 MinimumTradingPricingIncrement <MinTradgPricgIncrmt>"]
file_pages: [1979]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.19.7 MinimumTradingPricingIncrement <MinTradgPricgIncrmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1979 to 1979.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1979

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
32.4.3.1.1.3.19.7  MinimumTradingPricingIncrement <MinTradgPricgIncrmt>
Presence: [0..1]
Definition: Indicates the minimum or smallest movement (up or down) in the price allowed for the
security.
Datatype: "Number" on page 3324
32.4.3.1.1.3.19.8  PrimaryPlaceOfListingIdentification <PmryPlcOfListgId>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
Datatype: "MICIdentifier" on page 3322
32.4.3.1.1.3.20  SpreadAndBenchmarkCurve <SprdAndBchmkCrv>
Presence: [0..*]
Definition: Indicates the spread to benchmark details of an indication of interest.
SpreadAndBenchmarkCurve <SprdAndBchmkCrv> contains the following BenchmarkCurve6
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Spread <Sprd> [0..1] Quantity 1979
   BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
1980
   BenchmarkPrice <BchmkPric> [0..1]  1981
     ValueType <ValTp> [0..1] CodeSet 1981
     Value <Val> [1..1] ± 1982
     PriceType <PricTp> [0..1] CodeSet 1982
   BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 1983
   BenchmarkCurveName <BchmkCrvNm> [0..1]  1983
{Or     Code <Cd> [1..1] CodeSet 1983
Or}     Proprietary <Prtry> [1..1] ± 1984
   BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 1985
32.4.3.1.1.3.20.1  Spread <Sprd>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1979 August 2026
```

