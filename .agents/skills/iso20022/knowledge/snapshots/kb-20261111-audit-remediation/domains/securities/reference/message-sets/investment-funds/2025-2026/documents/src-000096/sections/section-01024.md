---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "38.4 Message Building Blocks", "38.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>", "38.4.15.8 FinancialInstrumentAssetForTransfer <FinInstrmAsstForTrf>", "38.4.15.8.4 UnitsDetails <UnitsDtls>", "38.4.15.8.4.8 TransactionOverhead <TxOvrhd>", "38.4.15.8.4.8.7 DigitalNetworkFee <DgtlNtwkFee>", "38.4.15.8.4.8.7.2 Quantity <Qty>"]
file_pages: [1417]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.018.001.10"]
---

# 38.4.15.8.4.8.7.2 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 1417 to 1417.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1417

```text
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 5402
38.4.15.8.4.8.7.2  Quantity <Qty>
Presence: [1..1]
Definition: Choice between different quantities related to the payment in digital asset.
Quantity <Qty> contains one of the following Quantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C20 1417
Or}   ProprietaryQuantity <PrtryQty> [1..1]  1417
     Quantity <Qty> [1..1] Quantity 1418
     QuantityType <QtyTp> [1..1] Text 1418
     Issuer <Issr> [1..1] Text 1418
     SchemeName <SchmeNm> [0..1] Text 1418
38.4.15.8.4.8.7.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of security.
Impacted by: C20 "DigitalTokenUnitUsageRule"
Quantity <Qty> contains one of the following elements (see "FinancialInstrumentQuantity33Choice" on
page 5128 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unit <Unit> [1..1] Quantity 5128
Or   FaceAmount <FaceAmt> [1..1] Amount 5128
Or   AmortisedValue <AmtsdVal> [1..1] Amount 5129
Or}   DigitalTokenUnit <DgtlTknUnit> [1..1] Quantity 5129
Constraints
• DigitalTokenUnitUsageRule
DigitalTokenUnit format may only be used for instruments identified with a digital token identifier.
38.4.15.8.4.8.7.2.2  ProprietaryQuantity <PrtryQty>
Presence: [1..1]
Definition: Proprietary quantity of security format.
Approved by the Securities SEG on 27 January 2026 sese.018.001.10 AccountHoldingInformationV10
Investment Funds - Maintenance 2025 - 2026 1417 May 2026
```

