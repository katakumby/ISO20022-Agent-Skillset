---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.3 FinancialInstrumentAttributes <FinInstrmAttrbts>", "32.4.3.1.1.3.19 TradingMarket <TradgMkt>", "32.4.3.1.1.3.19.3 TradeLotSize <TradLotSz>"]
file_pages: [1977]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.3.19.3 TradeLotSize <TradLotSz>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1977 to 1977.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1977

```text
RoundLot <RndLot> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 2953 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 2954
Or   FaceAmount <FaceAmt> [1..1] Amount 2954
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 2954
32.4.3.1.1.3.19.3  TradeLotSize <TradLotSz>
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
32.4.3.1.1.3.19.4  SecondaryPlaceOfListing <ScndryPlcOfListg>
Presence: [0..5]
Definition: Market(s) on which the security is listed.
Datatype: "MICIdentifier" on page 3322
32.4.3.1.1.3.19.5  MinimumTradedNominalQuantity <MinTraddNmnlQty>
Presence: [0..1]
Definition: Minimum number of securities that can be traded.
MinimumTradedNominalQuantity <MinTraddNmnlQty> contains one of the following
UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 1977
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 1977
32.4.3.1.1.3.19.5.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 3324
32.4.3.1.1.3.19.5.2  FaceAmount <FaceAmt>
Presence: [1..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1977 August 2026
```

