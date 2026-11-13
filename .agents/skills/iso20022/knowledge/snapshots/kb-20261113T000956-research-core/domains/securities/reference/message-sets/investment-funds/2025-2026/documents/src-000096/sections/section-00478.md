---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["27 sese.004.001.09 ReversalOfTransferOutConfirmationV09", "28.4 Message Building Blocks", "28.4.6 MasterReference <MstrRef>", "28.4.7.12 UnitsDetails <UnitsDtls>", "28.4.7.12.8 TransactionOverhead <TxOvrhd>", "28.4.7.12.8.7 DigitalNetworkFee <DgtlNtwkFee>", "28.4.7.12.8.7.2 Quantity <Qty>"]
file_pages: [655]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.005.001.10"]
---

# 28.4.7.12.8.7.2 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 655 to 655.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 655

```text
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 5402
28.4.7.12.8.7.2  Quantity <Qty>
Presence: [1..1]
Definition: Choice between different quantities related to the payment in digital asset.
Quantity <Qty> contains one of the following Quantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C14 655
Or}   ProprietaryQuantity <PrtryQty> [1..1]  655
     Quantity <Qty> [1..1] Quantity 656
     QuantityType <QtyTp> [1..1] Text 656
     Issuer <Issr> [1..1] Text 656
     SchemeName <SchmeNm> [0..1] Text 656
28.4.7.12.8.7.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of security.
Impacted by: C14 "DigitalTokenUnitUsageRule"
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
28.4.7.12.8.7.2.2  ProprietaryQuantity <PrtryQty>
Presence: [1..1]
Definition: Proprietary quantity of security format.
Approved by the Securities SEG on 27 January 2026 sese.005.001.10 TransferInInstructionV10
Investment Funds - Maintenance 2025 - 2026 655 May 2026
```

