---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types"]
file_pages: [222]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7 Message Items Types

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 222 to 222.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 222

```text
7 Message Items Types
7.1 MessageComponents
7.1.1 Account Identification
7.1.1.1  SecuritiesAccount20
Definition: Number assigned by a government agency to identify foreign nationals.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 222
   Type <Tp> [1..1] CodeSet 222
   Name <Nm> [0..1] Text 222
7.1.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 669
7.1.1.1.2  Type <Tp>
Presence: [1..1]
Definition: Choice between a code and a data source scheme to identify the type of account.
Datatype: "ClearingAccountType1Code" on page 620
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
7.1.1.1.3  Name <Nm>
Presence: [0..1]
Definition: .
Datatype: "Max70Text" on page 670
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 222 February 2025
```

