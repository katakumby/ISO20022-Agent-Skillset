---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "40.4 Message Building Blocks", "40.4.14 Transferee <Trfee>", "40.4.15.11 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "40.4.15.11.3 Quantity <Qty>", "40.4.15.11.3.1 Unit <Unit>"]
file_pages: [1605]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.043.001.02"]
---

# 40.4.15.11.3.1 Unit <Unit>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1605 to 1605.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1605

```text
Quantity <Qty> contains the following Quantity54 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [0..1]  1605
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1605
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1605
   PercentageRate <PctgRate> [0..1] Rate 1605
   FaceAmount <FaceAmt> [0..1] Amount 1605
   AmortisedValue <AmtsdVal> [0..1] Amount 1606
   CashAmount <CshAmt> [0..1] Amount C1 1606
   OtherAsset <OthrAsst> [0..1] Text 1606
40.4.15.11.3.1  Unit <Unit>
Presence: [0..1]
Definition: Quantity of security transferred.
Unit <Unit> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 1605
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1605
40.4.15.11.3.1.1  UnitsNumber <UnitsNb>
Presence: [1..1]
Definition: Quantity of units.
Datatype: "DecimalNumber" on page 5400
40.4.15.11.3.1.2  DigitalTokenUnit <DgtlTknUnit>
Presence: [1..1]
Definition: Quantity of digital tokens expressed as a number, for example, a number of blockchain
tokens.
Datatype: "Max30DecimalNumber" on page 5400
40.4.15.11.3.2  PercentageRate <PctgRate>
Presence: [0..1]
Definition: Percentage rate of assets transferred.
Datatype: "PercentageRate" on page 5401
40.4.15.11.3.3  FaceAmount <FaceAmt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.043.001.02 PortfolioTransferCompletionV02
Investment Funds - Maintenance 2025 - 2026 1605 May 2026
```

