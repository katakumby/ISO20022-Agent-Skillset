---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "27.4.2.3.21 TradingMarket <TradgMkt>", "27.4.2.3.21.3 TradeLotSize <TradLotSz>"]
file_pages: [774]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.3.21.3 TradeLotSize <TradLotSz>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 774 to 774.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 774

```text
RoundLot <RndLot> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
27.4.2.3.21.3  TradeLotSize <TradLotSz>
Presence: [0..1]
Definition: Minimum number of securities that can be traded.
TradeLotSize <TradLotSz> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
27.4.2.3.21.4  SecondaryPlaceOfListing <ScndryPlcOfListg>
Presence: [0..5]
Definition: Market(s) on which the security is listed.
Datatype: "MICIdentifier" on page 3322
27.4.2.3.21.5  MinimumTradedNominalQuantity <MinTraddNmnlQty>
Presence: [0..1]
Definition: Minimum number of securities that can be traded.
MinimumTradedNominalQuantity <MinTraddNmnlQty> contains one of the following
UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 774
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 774
27.4.2.3.21.5.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 3324
27.4.2.3.21.5.2  FaceAmount <FaceAmt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 774 August 2026
```

