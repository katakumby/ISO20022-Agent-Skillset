---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.2 CommonFinancialInstrumentAttributes12", "13.1.6.2.21 TradingMarket <TradgMkt>", "13.1.6.2.21.3 TradeLotSize <TradLotSz>"]
file_pages: [270]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.2.21.3 TradeLotSize <TradLotSz>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 270 to 270.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 270

```text
RoundLot <RndLot> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.21.3  TradeLotSize <TradLotSz>
Presence: [0..1]
Definition: Minimum number of securities that can be traded.
TradeLotSize <TradLotSz> contains one of the following elements (see
"FinancialInstrumentQuantity1Choice" on page 476 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 476
Or   FaceAmount <FaceAmt> [1..1] Amount 476
Or}   AmortisedValue <AmtsdVal> [1..1] Amount 476
13.1.6.2.21.4  SecondaryPlaceOfListing <ScndryPlcOfListg>
Presence: [0..5]
Definition: Market(s) on which the security is listed.
Datatype: "MICIdentifier" on page 531
13.1.6.2.21.5  MinimumTradedNominalQuantity <MinTraddNmnlQty>
Presence: [0..1]
Definition: Minimum number of securities that can be traded.
MinimumTradedNominalQuantity <MinTraddNmnlQty> contains one of the following
UnitOrFaceAmount1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 270
Or}   FaceAmount <FaceAmt> [1..1] Amount C1, C5 270
13.1.6.2.21.5.1  Unit <Unit>
Presence: [1..1]
Definition: Quantity expressed as a number, eg, a number of shares.
Datatype: "DecimalNumber" on page 532
13.1.6.2.21.5.2  FaceAmount <FaceAmt>
Presence: [1..1]
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 270 March 2024
```

