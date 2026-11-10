---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.23 CashMovementDetails <CshMvmntDtls>", "7.4.13.23.14 PriceDetails <PricDtls>", "7.4.13.23.14.1 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>"]
file_pages: [524]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.23.14.1 GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 524 to 524.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 524

```text
Constraints
• GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices received or
paid in the course of an event. The specific meaning (redemption price, subscription price,
reinvestment price, ETC.) is derived from the event type.
7.4.13.23.14.1  GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>
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
7.4.13.23.14.2  GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>
Presence: [0..1]
Definition: Generic cash price received per product by the underlying security holder either as a
percentage or an amount, for example, redemption price.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 524 February 2026
```

