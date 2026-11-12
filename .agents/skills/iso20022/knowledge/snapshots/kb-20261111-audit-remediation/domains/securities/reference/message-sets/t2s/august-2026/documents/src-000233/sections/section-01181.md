---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.2 FinancialInstrumentAttributes <FinInstrmAttrbts>", "28.4.2.2.2.21 TradingMarket <TradgMkt>"]
file_pages: [1697]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.2.21 TradingMarket <TradgMkt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1697 to 1697.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1697

```text
Datatype: "CountryCode" on page 3234
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
28.4.2.2.2.21  TradingMarket <TradgMkt>
Presence: [0..*]
Definition: Market(s) on which the security is traded.
TradingMarket <TradgMkt> contains the following TradingParameters2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketIdentification <MktId> [0..1] IdentifierSet 1697
   RoundLot <RndLot> [0..1] ± 1697
   TradeLotSize <TradLotSz> [0..1] ± 1698
   SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 1698
   MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  1698
{Or     Unit <Unit> [1..1] Quantity 1698
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1698
   MaximumTradedNominalQuantity
<MaxTraddNmnlQty>
[0..1]  1699
{Or     Unit <Unit> [1..1] Quantity 1699
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 1699
   MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 1700
   PrimaryPlaceOfListingIdentification
<PmryPlcOfListgId>
[0..1] IdentifierSet 1700
28.4.2.2.2.21.1  MarketIdentification <MktId>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, for example,
Electronic Trading Platforms (ECN), and unregulated markets, for example, Automated Trading
Systems (ATS) (MIC - ISO 3166).
Datatype: "MICIdentifier" on page 3322
28.4.2.2.2.21.2  RoundLot <RndLot>
Presence: [0..1]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1697 August 2026
```

