---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.3 Quantity <Qty>"]
file_pages: [1394]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.3 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1394 to 1394.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1394

```text
OtherAsset <OthrAsst> contains the following elements (see "OtherAsset2" on page 4525 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherAssetType <OthrAsstTp> [1..1]  4525
{Or     Code <Cd> [1..1] CodeSet 4525
Or}     Proprietary <Prtry> [1..1] ± 4526
   Identification <Id> [1..1] Text 4526
   Name <Nm> [0..1] Text 4526
   Description <Desc> [0..1] Text 4526
   OtherIdentification <OthrId> [0..5] Text 4526
   AdditionalInformation <AddtlInf> [0..*] ± 4527
38.4.15.8.3  Quantity <Qty>
Presence: [0..1]
Definition: Specifies the quantity of assets to be transferred in units or in a percentage rate.
Quantity <Qty> contains the following Quantity53 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Unit <Unit> [0..1]  1394
{Or     UnitsNumber <UnitsNb> [1..1] Quantity 1395
Or}     DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1395
   PercentageRate <PctgRate> [0..1] Rate 1395
   FaceAmount <FaceAmt> [0..1] Amount 1395
   AmortisedValue <AmtsdVal> [0..1] Amount 1395
   CashAmount <CshAmt> [0..1] Amount C1 1395
   OtherAsset <OthrAsst> [0..1] Text 1395
38.4.15.8.3.1  Unit <Unit>
Presence: [0..1]
Definition: Quantity of security to be transferred.
Unit <Unit> contains one of the following Unit1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   UnitsNumber <UnitsNb> [1..1] Quantity 1395
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 1395
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1394 May 2026
```

