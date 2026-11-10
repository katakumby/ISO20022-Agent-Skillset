---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.11 CashMovementDetails <CshMvmntDtls>", "8.4.12.11.15 PriceDetails <PricDtls>", "8.4.12.11.15.1 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>"]
file_pages: [660]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.11.15.1 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 660 to 660.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 660

```text
PriceDetails <PricDtls> contains the following PriceDetails37 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 660
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 660
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 661
Constraints
• GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices received or
paid in the course of an event. The specific meaning (redemption price, subscription price,
reinvestment price, ETC.) is derived from the event type.
8.4.12.11.15.1  GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>
Presence: [0..1]
Definition: Generic cash price paid per product by the underlying security holder either as a percentage
or an amount or a number of points above an index, for example, reinvestment price, strike price and
exercise price.
GenericCashPricePaidPerProduct <GncCshPricPdPerPdct> contains one of the following elements
(see "PriceFormat75Choice" on page 1068 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1069
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1069
     PriceValue <PricVal> [1..1] Rate 1069
Or   AmountPrice <AmtPric> [1..1] ± 1069
Or}   IndexPoints <IndxPts> [1..1] Quantity 1069
8.4.12.11.15.2  GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>
Presence: [0..1]
Definition: Generic cash price received per product by the underlying security holder either as a
percentage or an amount, for example, redemption price.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 660 February 2026
```

