---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.1 BusinessProcessType <BizPrcTp>"]
file_pages: [49]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.1 BusinessProcessType <BizPrcTp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 49 to 49.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 49

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
3.4.4.1  BusinessProcessType <BizPrcTp>
Presence: [0..1]
Definition: Specifies the type of business process.
BusinessProcessType <BizPrcTp> contains one of the following elements (see
"BusinessProcessType2Choice" on page 318 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 319
Or}   Proprietary <Prtry> [1..1] ± 319
3.4.4.2  OrderIdentification <OrdrId>
Presence: [0..*]
Definition: Unique identifier for Order as assigned by sell-side.
Datatype: "Max35Text" on page 669
3.4.4.3  ClientOrderIdentification <ClntOrdrId>
Presence: [0..*]
Definition: Unique identifier for the order as assigned by the buy-side. Uniqueness must be guaranteed
within a single trading day. Firms, particularly those that electronically submit multi-day orders, trade
globally or throughout market close periods, should ensure uniqueness across days, for example by
embedding a date within the ClientOrderIdentification element.
Datatype: "Max35Text" on page 669
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 49 February 2025
```

