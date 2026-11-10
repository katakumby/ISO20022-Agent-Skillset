---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.55 PartialFill4", "7.1.19.55.6 PreviouslyExecutedQuantity <PrevslyExctdQty>"]
file_pages: [381]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.55.6 PreviouslyExecutedQuantity <PrevslyExctdQty>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 381 to 381.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 381

```text
OriginalOrderedQuantity <OrgnlOrdrdQty> contains one of the following elements (see
"QuantityOrAmount2Choice" on page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 318
Or}   Amount <Amt> [1..1] Amount C1, C9 318
7.1.19.55.6  PreviouslyExecutedQuantity <PrevslyExctdQty>
Presence: [1..1]
Definition: Quantity of financial instrument that has been previously executed.
PreviouslyExecutedQuantity <PrevslyExctdQty> contains one of the following elements (see
"QuantityOrAmount2Choice" on page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 318
Or}   Amount <Amt> [1..1] Amount C1, C9 318
7.1.19.55.7  RemainingQuantity <RmngQty>
Presence: [1..1]
Definition: Quantity of financial instrument that is remaining in order.
RemainingQuantity <RmngQty> contains one of the following elements (see
"QuantityOrAmount2Choice" on page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 318
Or}   Amount <Amt> [1..1] Amount C1, C9 318
7.1.19.55.8  MatchIncrementQuantity <MtchIncrmtQty>
Presence: [0..1]
Definition: Minimum quantity that applies to every execution. The order may still fill against smaller
orders, but the cumulative quantity of the execution must be in multiples of the Match Increment.
MatchIncrementQuantity <MtchIncrmtQty> contains one of the following elements (see
"QuantityOrAmount2Choice" on page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Quantity <Qty> [1..1] ± 318
Or}   Amount <Amt> [1..1] Amount C1, C9 318
7.1.19.56  FormOfSecurity6Choice
Definition: Choice of format for the form of securities.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 381 February 2025
```

