---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.19 PartialFillDetails <PrtlFillDtls>"]
file_pages: [345]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.19 PartialFillDetails <PrtlFillDtls>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 345 to 345.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 345

```text
NAVDate <NAVDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 263 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 263
Or}   DateTime <DtTm> [1..1] DateTime 263
7.1.19.43.19  PartialFillDetails <PrtlFillDtls>
Presence: [0..*]
Definition: Quantity of financial instrument bought or sold which is less than the quantity of financial
instrument ordered.
Impacted by: C27 "PartialFillsRule"
PartialFillDetails <PrtlFillDtls> contains the following elements (see "PartialFill4" on page 379 for
details)
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
7.1.19.43.20  ConfirmationQuantity <ConfQty>
Presence: [1..1]
Definition: Quantity of financial instrument that is being confirmed for the account.The quantity of the
security to be settled.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 345 February 2025
```

