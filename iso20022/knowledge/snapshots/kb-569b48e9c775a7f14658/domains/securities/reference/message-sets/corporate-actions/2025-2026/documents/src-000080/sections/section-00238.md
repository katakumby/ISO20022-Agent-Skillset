---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["5 seev.033.001.14 CorporateActionInstructionV14", "5.4 Message Building Blocks", "5.4.9 CorporateActionInstruction <CorpActnInstr>", "5.4.9.15 PriceDetails <PricDtls>", "5.4.9.15.1 IndicativeOrMarketPrice <IndctvOrMktPric>", "5.4.9.15.1.2 MarketPrice <MktPric>"]
file_pages: [315]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.033.001.14"]
---

# 5.4.9.15.1.2 MarketPrice <MktPric>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 315 to 315.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 315

```text
5.4.9.15.1.2  MarketPrice <MktPric>
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
5.4.9.15.2  IssuePrice <IssePric>
Presence: [0..1]
Definition: Initial issue price of a financial instrument.
IssuePrice <IssePric> contains one of the following elements (see "PriceFormat77Choice" on
page 1064 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   PercentagePrice <PctgPric> [1..1]  1064
     PercentagePriceType <PctgPricTp> [1..1] CodeSet 1065
     PriceValue <PricVal> [1..1] Rate 1065
Or}   AmountPrice <AmtPric> [1..1] ± 1065
5.4.9.15.3  GenericCashPriceReceivedPerProduct <GncCshPricRcvdPerPdct>
Presence: [0..1]
Definition: Generic cash price received per product by the underlying security holder either as a
percentage or an amount, for example, redemption price.
Approved by the Securities SEG on 27 January 2026 seev.033.001.14 CorporateActionInstructionV14
Corporate Actions - Maintenance 2025 - 2026 315 February 2026
```

