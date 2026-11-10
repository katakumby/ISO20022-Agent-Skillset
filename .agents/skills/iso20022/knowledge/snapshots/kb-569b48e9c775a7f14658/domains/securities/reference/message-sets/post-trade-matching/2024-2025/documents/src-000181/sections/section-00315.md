---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.55 PartialFill4"]
file_pages: [379]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.55 PartialFill4

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 379 to 379.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 379

```text
7.1.19.55  PartialFill4
Definition: Intention to transfer an ownership of a financial instrument.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ConfirmationQuantity <ConfQty> [1..1] ± 379
   DealPrice <DealPric> [1..1] ± 379
   TradeDate <TradDt> [0..1] ± 380
   PlaceOfTrade <PlcOfTrad> [0..1] ± C17,
C24,
C34
380
   OriginalOrderedQuantity <OrgnlOrdrdQty> [1..1] ± 380
   PreviouslyExecutedQuantity <PrevslyExctdQty> [1..1] ± 381
   RemainingQuantity <RmngQty> [1..1] ± 381
   MatchIncrementQuantity <MtchIncrmtQty> [0..1] ± 381
Constraints
• PartialFillsRule
A SecuritiesTradeConfirmation should not be used as a TradeExecution report. PartialFills aims at
providing a for information summary of the different executions that the confirmation consisted of.
7.1.19.55.1  ConfirmationQuantity <ConfQty>
Presence: [1..1]
Definition: Quantity of financial instrument to be ordered.
ConfirmationQuantity <ConfQty> contains one of the following elements (see "Quantity6Choice" on
page 273 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 273
Or}   OriginalAndCurrentFace <OrgnlAndCurFace> [1..1] ± 273
7.1.19.55.2  DealPrice <DealPric>
Presence: [1..1]
Definition: Amount of money for which goods or services are offered, sold, or bought.
DealPrice <DealPric> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 379 February 2025
```

