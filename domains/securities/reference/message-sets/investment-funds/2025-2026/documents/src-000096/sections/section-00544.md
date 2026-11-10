---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["30 sese.007.001.10 TransferInConfirmationV10", "30.4 Message Building Blocks", "30.4.4 RelatedReference <RltdRef>", "30.4.7.16 UnitsDetails <UnitsDtls>", "30.4.7.16.8 TransactionOverhead <TxOvrhd>", "30.4.7.16.8.7 DigitalNetworkFee <DgtlNtwkFee>", "30.4.7.16.8.7.2 Quantity <Qty>"]
file_pages: [743]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.007.001.10"]
---

# 30.4.7.16.8.7.2 Quantity <Qty>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 743 to 743.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 743

```text
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 5402
30.4.7.16.8.7.2  Quantity <Qty>
Presence: [1..1]
Definition: Choice between different quantities related to the payment in digital asset.
Quantity <Qty> contains one of the following Quantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C14 743
Or}   ProprietaryQuantity <PrtryQty> [1..1]  743
     Quantity <Qty> [1..1] Quantity 744
     QuantityType <QtyTp> [1..1] Text 744
     Issuer <Issr> [1..1] Text 744
     SchemeName <SchmeNm> [0..1] Text 744
30.4.7.16.8.7.2.1  Quantity <Qty>
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
30.4.7.16.8.7.2.2  ProprietaryQuantity <PrtryQty>
Presence: [1..1]
Definition: Proprietary quantity of security format.
Approved by the Securities SEG on 27 January 2026 sese.007.001.10 TransferInConfirmationV10
Investment Funds - Maintenance 2025 - 2026 743 May 2026
```

