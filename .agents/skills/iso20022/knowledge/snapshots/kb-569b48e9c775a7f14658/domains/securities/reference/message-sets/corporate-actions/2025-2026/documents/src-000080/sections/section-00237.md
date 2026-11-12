---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.15 PriceDetails <PricDtls>", "5.4.9.15.1 IndicativeOrMarketPrice <IndctvOrMktPric>"]
file_pages: [314]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.15.1 IndicativeOrMarketPrice <IndctvOrMktPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 314 to 314.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 314

```text
PriceDetails <PricDtls> contains the following CorporateActionPrice88 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IndicativeOrMarketPrice <IndctvOrMktPric> [0..1]  314
{Or     IndicativePrice <IndctvPric> [1..1] ± 314
Or}     MarketPrice <MktPric> [1..1] ± 315
   IssuePrice <IssePric> [0..1] ± 315
   GenericCashPriceReceivedPerProduct
<GncCshPricRcvdPerPdct>
[0..1] ± 315
   GenericCashPricePaidPerProduct
<GncCshPricPdPerPdct>
[0..1] ± 316
Constraints
• GenericCashPricePerProductGuideline
Generic Cash Price Received per Product (OFFR) and Generic Cash Price Paid per Product (PRPP)
are prices received or paid in the course of an event. The specific meaning (redemption price,
subscription price, reinvestment price, etc.) is derived from the event type.
5.4.9.15.1  IndicativeOrMarketPrice <IndctvOrMktPric>
Presence: [0..1]
Definition: Indicates whether the price is an indicative price or a market price.
IndicativeOrMarketPrice <IndctvOrMktPric> contains one of the following
IndicativeOrMarketPrice13Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndicativePrice <IndctvPric> [1..1] ± 314
Or}   MarketPrice <MktPric> [1..1] ± 315
5.4.9.15.1.1  IndicativePrice <IndctvPric>
Presence: [1..1]
Definition: Estimated price, for example, for valuation purposes.
IndicativePrice <IndctvPric> contains one of the following elements (see "PriceFormat77Choice" on
page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 314 February 2026
```

