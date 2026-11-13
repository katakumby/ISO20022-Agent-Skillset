---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.11 CorporateActionOptionDetails <CorpActnOptnDtls>", "3.4.11.24 SecuritiesMovementDetails <SctiesMvmntDtls>", "3.4.11.24.18 PriceDetails <PricDtls>", "3.4.11.24.18.1 IndicativeOrMarketPrice <IndctvOrMktPric>"]
file_pages: [196]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.11.24.18.1 IndicativeOrMarketPrice <IndctvOrMktPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 196 to 196.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 196

```text
PriceDetails <PricDtls> contains the following CorporateActionPrice82 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  196
{Or     IndicativePrice <IndctvPric> [1..1] ± 196
Or}     MarketPrice <MktPric> [1..1] ± 197
   CashInLieuOfSharePrice <CshInLieuOfShrPric> [0..1] ± 197
   CashValueForTax <CshValForTax> [0..1] ± 197
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 198
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 198
Constraints
• GenericCashPricePerProductGuideline
GenericCashPriceReceivedPerProduct and GenericCashPricePaidPerProduct are prices received or
paid in the course of an event. The specific meaning (redemption price, subscription price,
reinvestment price, etc.) is derived from the event type.
3.4.11.24.18.1  IndicativeOrMarketPrice <IndctvOrMktPric>
Presence: [0..1]
Definition: Indicates whether the price is an indicative price or a market price.
IndicativeOrMarketPrice <IndctvOrMktPric> contains one of the following
IndicativeOrMarketPrice12Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndicativePrice <IndctvPric> [1..1] ± 196
Or}   MarketPrice <MktPric> [1..1] ± 197
3.4.11.24.18.1.1  IndicativePrice <IndctvPric>
Presence: [1..1]
Definition: Estimated price, for example, for valuation purposes.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 196 February 2026
```

