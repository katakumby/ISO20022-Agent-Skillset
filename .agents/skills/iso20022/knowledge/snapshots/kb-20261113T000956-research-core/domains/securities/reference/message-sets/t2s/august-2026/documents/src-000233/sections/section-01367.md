---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.19 TradingMarket <TradgMkt>"]
file_pages: [1976]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.19 TradingMarket <TradgMkt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1976 to 1976.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1976

```text
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
32.4.3.1.1.3.19  TradingMarket <TradgMkt>
Presence: [0..*]
Definition: Market(s) on which the security is traded.
TradingMarket <TradgMkt> contains the following TradingParameters2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketIdentification <MktId> [0..1] IdentifierSet 1976
   RoundLot <RndLot> [0..1] ± 1976
   TradeLotSize <TradLotSz> [0..1] ± 1977
   SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1977
   MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  1977
{Or     Unit <Unit> [1..1] Quantity 1977
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1977
   MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1978
{Or     Unit <Unit> [1..1] Quantity 1978
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1978
   MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1979
   PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1979
32.4.3.1.1.3.19.1  MarketIdentification <MktId>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, for example,
Electronic Trading Platforms (ECN), and unregulated markets, for example, Automated Trading
Systems (ATS) (MIC - ISO 3166).
Datatype: "MICIdentifier" on page 3322
32.4.3.1.1.3.19.2  RoundLot <RndLot>
Presence: [0..1]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1976 August 2026
```

