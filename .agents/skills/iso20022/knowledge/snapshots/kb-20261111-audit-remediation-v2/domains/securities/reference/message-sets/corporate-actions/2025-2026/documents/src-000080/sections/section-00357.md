---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.22 SecuritiesMovementDetails <SctiesMvmntDtls>", "7.4.13.22.18 PriceDetails <PricDtls>", "7.4.13.22.18.1 IndicativeOrMarketPrice <IndctvOrMktPric>", "7.4.13.22.18.1.2 MarketPrice <MktPric>"]
file_pages: [480]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.22.18.1.2 MarketPrice <MktPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 480 to 480.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 480

```text
IndicativePrice <IndctvPric> contains one of the following elements (see "PriceFormat74Choice" on
page 1074 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
7.4.13.22.18.1.2  MarketPrice <MktPric>
Presence: [1..1]
Definition: Last reported/known price of a financial instrument in a market.
MarketPrice <MktPric> contains one of the following elements (see "PriceFormat74Choice" on
page 1074 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
7.4.13.22.18.2  CashInLieuOfSharePrice <CshInLieuOfShrPric>
Presence: [0..1]
Definition: Cash disbursement in lieu of equities; usually in lieu of fractional quantity.
CashInLieuOfSharePrice <CshInLieuOfShrPric> contains one of the following elements (see
"PriceFormat74Choice" on page 1074 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1074
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1075
     PriceValue <PricVal> [1..1] Rate 1075
Or   AmountPrice <AmtPric> [1..1] ± 1075
Or}   NotSpecifiedPrice <NotSpcfdPric> [1..1] CodeSet 1075
7.4.13.22.18.3  CashValueForTax <CshValForTax>
Presence: [0..1]
Definition: Cash value of resulting securities proceeds for tax calculation and/or reporting.
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 480 February 2026
```

