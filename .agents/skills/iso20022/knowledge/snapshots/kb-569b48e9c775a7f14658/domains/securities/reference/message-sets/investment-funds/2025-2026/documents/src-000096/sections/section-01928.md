---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["47 setr.007.001.05 SubscriptionBulkOrderV05", "47.4 Message Building Blocks", "47.4.4 BulkOrderDetails <BlkOrdrDtls>", "47.4.4.8 IndividualOrderDetails <IndvOrdrDtls>", "47.4.4.8.21 DigitalAssetSettlement <DgtlAsstSttlm>", "47.4.4.8.21.2 Quantity <Qty>"]
file_pages: [2695]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.007.001.05"]
---

# 47.4.4.8.21.2 Quantity <Qty>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 2695 to 2695.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2695

```text
Definition: Textual description of a security instrument.
Datatype: "Max140Text" on page 5402
47.4.4.8.21.2  Quantity <Qty>
Presence: [1..1]
Definition: Choice between different quantities related to the payment in digital asset.
Quantity <Qty> contains one of the following Quantity48Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± C15 2695
Or}   ProprietaryQuantity <PrtryQty> [1..1]  2695
     Quantity <Qty> [1..1] Quantity 2696
     QuantityType <QtyTp> [1..1] Text 2696
     Issuer <Issr> [1..1] Text 2696
     SchemeName <SchmeNm> [0..1] Text 2696
47.4.4.8.21.2.1  Quantity <Qty>
Presence: [1..1]
Definition: Quantity of security.
Impacted by: C15 "DigitalTokenUnitUsageRule"
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
47.4.4.8.21.2.2  ProprietaryQuantity <PrtryQty>
Presence: [1..1]
Definition: Proprietary quantity of security format.
Approved by the Securities SEG on 27 January 2026 setr.007.001.05 SubscriptionBulkOrderV05
Investment Funds - Maintenance 2025 - 2026 2695 May 2026
```

