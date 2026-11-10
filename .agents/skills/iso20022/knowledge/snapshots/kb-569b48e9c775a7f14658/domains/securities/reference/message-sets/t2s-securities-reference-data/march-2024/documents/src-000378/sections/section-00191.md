---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.21 TradingMarket <TradgMkt>"]
file_pages: [269]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.21 TradingMarket <TradgMkt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 269 to 269.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 269

```text
Datatype: "CountryCode" on page 513
Constraints
• Country
The code is checked against the list of country names obtained from the United Nations (ISO 3166,
Alpha-2 code).
13.1.6.2.21  TradingMarket <TradgMkt>
Presence: [0..*]
Definition: Market(s) on which the security is traded.
TradingMarket <TradgMkt> contains the following TradingParameters2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MarketIdentification <MktId> [0..1] IdentifierSet 269
   RoundLot <RndLot> [0..1] ± 269
   TradeLotSize <TradLotSz> [0..1] ± 270
   SecondaryPlaceOfListing <ScndryPlcOfListg> [0..5] IdentifierSet 270
   MinimumTradedNominalQuantity <MinTraddNmnlQty> [0..1]  270
{Or     Unit <Unit> [1..1] Quantity 270
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 270
   MaximumTradedNominalQuantity <MaxTraddNmnlQty> [0..1]  271
{Or     Unit <Unit> [1..1] Quantity 271
Or}     FaceAmount <FaceAmt> [1..1] Amount C1, C5 271
   MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 272
   PrimaryPlaceOfListingIdentification <PmryPlcOfListgId> [0..1] IdentifierSet 272
13.1.6.2.21.1  MarketIdentification <MktId>
Presence: [0..1]
Definition: Code allocated to places of trade, ie, stock exchanges, regulated markets, for example,
Electronic Trading Platforms (ECN), and unregulated markets, for example, Automated Trading
Systems (ATS) (MIC - ISO 3166).
Datatype: "MICIdentifier" on page 531
13.1.6.2.21.2  RoundLot <RndLot>
Presence: [0..1]
Definition: Minimum quantity of securities that can be purchased without incurring a larger fee. For
example, if the round lot size is 100 and the trade is for 125 shares, then 100 will be processed without
a fee and the remaining 25 will incur a service fee for being an odd lot size.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 269 March 2024
```

