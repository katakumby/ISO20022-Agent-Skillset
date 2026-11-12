---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["35 sese.012.001.12 PortfolioTransferInstructionV12", "35.4 Message Building Blocks", "35.4.12 NomineeAccount <NmneeAcct>", "35.4.14.10 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "35.4.14.10.3 Quantity <Qty>", "35.4.14.10.3.1 Unit <Unit>"]
file_pages: [1027]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.012.001.12"]
---

# 35.4.14.10.3.1 Unit <Unit>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1027 to 1027.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1027

```text
Quantity <Qty> contains the following Quantity53 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [0..1]  1027
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1027
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1027
   PercentageRate <PctgRate> [0..1] Rate 1027
   FaceAmount <FaceAmt> [0..1] Amount 1027
   AmortisedValue <AmtsdVal> [0..1] Amount 1028
   CashAmount <CshAmt> [0..1] Amount C1 1028
   OtherAsset <OthrAsst> [0..1] Text 1028
35.4.14.10.3.1  Unit <Unit>
Presence: [0..1]
Definition: Quantity of security to be transferred.
Unit <Unit> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 1027
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1027
35.4.14.10.3.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
35.4.14.10.3.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
35.4.14.10.3.2  PercentageRate <PctgRate>
Presence: [0..1]
Definition: Percentage rate of assets to be transferred.
Datatype: "PercentageRate" on page 5401
35.4.14.10.3.3  FaceAmount <FaceAmt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.012.001.12 PortfolioTransferInstructionV12
Investment Funds - Maintenance 2025 - 2026 1027 May 2026
```

