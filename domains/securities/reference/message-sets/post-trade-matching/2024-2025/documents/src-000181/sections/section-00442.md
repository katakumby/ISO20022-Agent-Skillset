---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.22 Price", "7.1.22.2 OtherPrices5", "7.1.22.2.2 Transaction <Tx>"]
file_pages: [508]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.22.2.2 Transaction <Tx>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 508 to 508.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 508

```text
7.1.22.2.2  Transaction <Tx>
Presence: [0..1]
Definition: Specifies the transaction price.
Transaction <Tx> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.3  MarketBrokerCommission <MktBrkrComssn>
Presence: [0..1]
Definition: Market price including or excluding the broker's commission.
MarketBrokerCommission <MktBrkrComssn> contains the following elements (see "Price14" on
page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.4  MarkedUp <MrkdUp>
Presence: [0..1]
Definition: In case of an order to buy, the price that the broker paid on the market plus the broker's
commission.
MarkedUp <MrkdUp> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
7.1.22.2.5  MarkedDown <MrkdDwn>
Presence: [0..1]
Definition: In case of an order to sell, the price the broker receives in the market minus the broker's
commission.
MarkedDown <MrkdDwn> contains the following elements (see "Price14" on page 512 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Value <Val> [1..1] ± 512
   Type <Tp> [0..1] CodeSet 512
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 508 February 2025
```

