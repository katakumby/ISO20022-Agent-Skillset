---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.16 PriceDetails <PricDtls>", "8.4.12.10.16.5 GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>"]
file_pages: [610]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.16.5 GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 610 to 610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 610

```text
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
8.4.12.10.16.5  GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>
Presence: [0..1]
Definition: Generic cash price received per product by the underlying security holder either as a
percentage or an amount, for example, redemption price.
GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct> contains one of the following
elements (see "PriceFormat76Choice" on page 1080 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1081
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1081
     PriceValue <PricVal> [1..1] Rate 1082
Or   AmountPrice <AmtPric> [1..1] ± 1082
Or   AmountPricePerFinancialInstrumentQuantity
<AmtPricPerFinInstrmQty>
[1..1]  1082
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1082
     PriceValue <PricVal> [1..1] Amount C1 1083
     FinancialInstrumentQuantity <FinInstrmQty> [1..1] ± C13 1083
Or   AmountPricePerAmount <AmtPricPerAmt> [1..1]  1083
     AmountPriceType <AmtPricTp> [1..1] CodeSet 1084
     PriceValue <PricVal> [1..1] Amount C1 1084
     Amount <Amt> [1..1] Amount C1 1084
Or}   IndexPoints <IndxPts> [1..1] Quantity 1084
8.4.12.10.17  AmountDetails <AmtDtls>
Presence: [0..1]
Definition: Provides information about the amounts related to a securities movement.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 610 February 2026
```

