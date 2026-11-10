---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.1 BusinessProcessType <BizPrcTp>"]
file_pages: [338]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.1 BusinessProcessType <BizPrcTp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 338 to 338.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 338

```text
If CurrencyToBuy is used, then it implies the following:
- the instruction is to delivery
- the currency received as proceeds from the sale of securities, eg, the currency to be sold, is the
currency of the settlement amount. The currency to be bought is provided by the currency to buy
message element. If proceeds are repatriated, this is in the base currency of the portfolio.
- the amount of currency to be sold is equal to the settlement amount of the transaction. This implies
a bulk forex deal must be instructed by other means.
- a forex deal to repatriate proceeds after the sale of securities should be executed for the soonest
possible value date after settlement of the securities, as permitted by market convention.
- a bilateral agreement regarding the use of this field has been established.
• PlaceOfTradeRule
If PlaceOfTrade is used and a ISO 10383 MIC exists for the market to be identified, then the ISO
10383 Market Identifier Code (MIC) must be used.
• TradeDateTimeUTCRule
If Trade Date/Time is used with a time or a time + UTC indicator, then it must be the local time of the
place of trade, eg, of the stock exchange, or of the selling broker for OTC.
7.1.19.43.1  BusinessProcessType <BizPrcTp>
Presence: [0..1]
Definition: Specifies the type of business process.
BusinessProcessType <BizPrcTp> contains one of the following elements (see
"BusinessProcessType2Choice" on page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 319
Or}   Proprietary <Prtry> [1..1] ± 319
7.1.19.43.2  OrderIdentification <OrdrId>
Presence: [0..*]
Definition: Unique identifier for Order as assigned by sell-side.
Datatype: "Max35Text" on page 669
7.1.19.43.3  ClientOrderIdentification <ClntOrdrId>
Presence: [0..*]
Definition: Unique identifier for the order as assigned by the buy-side. Uniqueness must be guaranteed
within a single trading day. Firms, particularly those that electronically submit multi-day orders, trade
globally or throughout market close periods, should ensure uniqueness across days, for example by
embedding a date within the ClientOrderIdentification element.
Datatype: "Max35Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 338 February 2025
```

