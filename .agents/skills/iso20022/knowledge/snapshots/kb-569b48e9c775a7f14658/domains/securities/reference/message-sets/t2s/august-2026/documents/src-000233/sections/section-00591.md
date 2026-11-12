---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.21 TradingMarket <TradgMkt>", "27.4.2.3.21.7 MinimumTradingPricingIncrement <MinTradgPricgIncrmt>"]
file_pages: [776]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.21.7 MinimumTradingPricingIncrement <MinTradgPricgIncrmt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 776 to 776.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 776

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
27.4.2.3.21.7  MinimumTradingPricingIncrement <MinTradgPricgIncrmt>
Presence: [0..1]
Definition: Indicates the minimum or smallest movement (up or down) in the price allowed for the
security.
Datatype: "Number" on page 3324
27.4.2.3.21.8  PrimaryPlaceOfListingIdentification <PmryPlcOfListgId>
Presence: [0..1]
Definition: Market(s) on which the security is listed.
Datatype: "MICIdentifier" on page 3322
27.4.2.3.22  SpreadAndBenchmarkCurve <SprdAndBchmkCrv>
Presence: [0..*]
Definition: Indicates the spread to benchmark details of an indication of interest.
SpreadAndBenchmarkCurve <SprdAndBchmkCrv> contains the following BenchmarkCurve6
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Spread <Sprd> [0..1] Quantity 776
   BenchmarkIdentification <BchmkId> [0..1] ± C6, C7,
C8, C9,
C12
777
   BenchmarkPrice <BchmkPric> [0..1]  778
     ValueType <ValTp> [0..1] CodeSet 778
     Value <Val> [1..1] ± 779
     PriceType <PricTp> [0..1] CodeSet 779
   BenchmarkCurveCurrency <BchmkCrvCcy> [0..1] CodeSet C2 780
   BenchmarkCurveName <BchmkCrvNm> [0..1]  780
{Or     Code <Cd> [1..1] CodeSet 780
Or}     Proprietary <Prtry> [1..1] ± 781
   BenchmarkCurvePoint <BchmkCrvPt> [0..1] Text 782
27.4.2.3.22.1  Spread <Sprd>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 776 August 2026
```

