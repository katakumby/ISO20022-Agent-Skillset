---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["8 seev.036.001.17 CorporateActionMovementConfirmationV17", "8.4 Message Building Blocks", "8.4.12 CorporateActionConfirmationDetails <CorpActnConfDtls>", "8.4.12.10 SecuritiesMovementDetails <SctiesMvmntDtls>", "8.4.12.10.16 PriceDetails <PricDtls>", "8.4.12.10.16.2 IndicativeOrMarketPrice <IndctvOrMktPric>", "8.4.12.10.16.2.1 IndicativePrice <IndctvPric>"]
file_pages: [609]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.036.001.17"]
---

# 8.4.12.10.16.2.1 IndicativePrice <IndctvPric>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 609 to 609.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 609

```text
8.4.12.10.16.2.1  IndicativePrice <IndctvPric>
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
8.4.12.10.16.2.2  MarketPrice <MktPric>
Presence: [1..1]
Definition: Last reported/known price of a financial instrument in a market.
MarketPrice <MktPric> contains one of the following elements (see "PriceFormat77Choice" on
page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
8.4.12.10.16.3  CashValueForTax <CshValForTax>
Presence: [0..1]
Definition: Cash value of resulting securities proceeds for tax calculation and/or reporting.
CashValueForTax <CshValForTax> contains the following elements (see "AmountPrice2" on
page 831 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AmountPriceType <AmtPricTp> [1..1] CodeSet 831
   PriceValue <PricVal> [1..1] Amount C1 831
8.4.12.10.16.4  GenericCashPricePaidPerProduct <GncCshPricPdPerPdct>
Presence: [0..1]
Definition: Generic cash price paid per product by the underlying security holder either as a percentage
or an amount or a number of points above an index, for example, reinvestment price, strike price and
exercise price.
Approved by the Securities SEG on 27 January 2026 seev.036.001.17
CorporateActionMovementConfirmationV17
Corporate Actions - Maintenance 2025 - 2026 609 February 2026
```

