---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.18 PriceDetails <PricDtls>", "7.4.13.22.18.1 IndicativeOrMarketPrice <IndctvOrMktPric>"]
file_pages: [479]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.18.1 IndicativeOrMarketPrice <IndctvOrMktPric>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 479 to 479.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 479

```text
PriceDetails <PricDtls> contains the following CorporateActionPrice82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  479
{Or     IndicativePrice <IndctvPric> [1..1] ± 479
Or}     MarketPrice <MktPric> [1..1] ± 480
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 480
   CashValueForTax <CshValForTax> [0..1] ± 480
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 481
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 481
Constraints
• GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices received or
paid in the course of an event. The specific meaning (redemption price, subscription price,
reinvestment price, etc.) is derived from the event type.
7.4.13.22.18.1  IndicativeOrMarketPrice <IndctvOrMktPric>
Presence: [0..1]
Definition: Indicates whether the price is an indicative price or a market price.
IndicativeOrMarketPrice <IndctvOrMktPric> contains one of the following
IndicativeOrMarketPrice12Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndicativePrice <IndctvPric> [1..1] ± 479
Or}   MarketPrice <MktPric> [1..1] ± 480
7.4.13.22.18.1.1  IndicativePrice <IndctvPric>
Presence: [1..1]
Definition: Estimated price, for example, for valuation purposes.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 479 February 2026
```

