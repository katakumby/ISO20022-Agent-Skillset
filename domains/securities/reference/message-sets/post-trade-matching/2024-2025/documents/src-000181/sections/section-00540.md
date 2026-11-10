---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.2 CodeSet", "7.2.2.17 ChargeTaxBasis1Code"]
file_pages: [620]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.2.17 ChargeTaxBasis1Code

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 620 to 620.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 620

```text
Type: CodeSet
CodeName Name Definition
GROS GrossSettlementSystem Settle money through gross settlement
system.
NETS NetSettlementSystem Settle money through net settlement
system.
7.2.2.17  ChargeTaxBasis1Code
Definition: Define the Charges/tax basis for the trade being allocated.
Type: CodeSet
CodeName Name Definition
FLAT FlatOrAbsolute Charges/tax basis is flat or absolute for
the trade being allocated.
PERU PerUnit Charge/tax basis is per unit of financial
instrument.
7.2.2.18  ClearingAccountType1Code
Definition: Specifies the clearing account type.
Type: CodeSet
CodeName Name Definition
HOUS House Specifies that the account is used to
register trades executed for either the
clearing member or its subsidiaries.
CLIE Client Specifies that the account is used to
register trades executed for the clearing
member's customers.
LIPR LiquidityProvider Specifies that the account is used to
register trades executed for liquidity
providers (also known as market maker)
activities.
7.2.2.19  ClearingSide1Code
Definition: Side taken by a party on an order.
Type: CodeSet
CodeName Name Definition
BUYI Buy Clearing member is on the buying side.
SELL Sell Clearing member is on the selling side.
LEND Lend Clearing member is on the lending side.
BORW Borrow Clearing member is on the borrowing
side.
7.2.2.20  ClosingType1Code
Definition: Specifies the timing or method for terminating the agreement - for repos.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 620 February 2025
```

