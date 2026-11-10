---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.16 PriceDetails <PricDtls>", "8.4.12.10.16.1 CashInLieuOfSharePrice <CshInLieuOfShrPric>"]
file_pages: [608]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.16.1 CashInLieuOfSharePrice <CshInLieuOfShrPric>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 608 to 608.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 608

```text
PriceDetails <PricDtls> contains the following CorporateActionPrice83 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 608
   IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  608
{Or     IndicativePrice <IndctvPric> [1..1] ± 609
Or}     MarketPrice <MktPric> [1..1] ± 609
   CashValueForTax <CshValForTax> [0..1] ± 609
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 609
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 610
Constraints
• GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices received or
paid in the course of an event. The specific meaning (redemption price, subscription price,
reinvestment price, etc.) is derived from the event type.
8.4.12.10.16.1  CashInLieuOfSharePrice <CshInLieuOfShrPric>
Presence: [0..1]
Definition: Cash disbursement in lieu of equities; usually in lieu of fractional quantity.
CashInLieuOfSharePrice <CshInLieuOfShrPric> contains one of the following elements (see
"PriceFormat77Choice" on page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
8.4.12.10.16.2  IndicativeOrMarketPrice <IndctvOrMktPric>
Presence: [0..1]
Definition: Indicates whether the price is an indicative price or a market price.
IndicativeOrMarketPrice <IndctvOrMktPric> contains one of the following
IndicativeOrMarketPrice13Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndicativePrice <IndctvPric> [1..1] ± 609
Or}   MarketPrice <MktPric> [1..1] ± 609
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 608 February 2026
```

