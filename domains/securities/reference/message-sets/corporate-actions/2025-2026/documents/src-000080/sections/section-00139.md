---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.18 PriceDetails <PricDtls>", "3.4.11.24.18.4 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>"]
file_pages: [198]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.18.4 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 198 to 198.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 198

```text
CashValueForTax <CshValForTax> contains one of the following elements (see
"PriceFormat46Choice" on page 1065 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AmountPrice <AmtPric> [1..1] ± 1066
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1066
3.4.11.24.18.4  GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>
Presence: [0..1]
Definition: Generic cash price paid per product by the underlying security holder either as a percentage
or an amount or a number of points above an index, for example, reinvestment price, strike price and
exercise price.
GenericCashPricePaidPerProduct <GncCshPricPdPerPdct> contains one of the following elements
(see "PriceFormat73Choice" on page 1085 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1085
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1085
     PriceValue <PricVal> [1..1] Rate 1085
Or   AmountPrice <AmtPric> [1..1] ± 1086
Or   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1086
Or}   IndexPoints <IndxPts> [1..1] Quantity 1086
3.4.11.24.18.5  GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>
Presence: [0..1]
Definition: Generic cash price received per product by the underlying security holder either as a
percentage or an amount, for example, redemption price.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 198 February 2026
```

