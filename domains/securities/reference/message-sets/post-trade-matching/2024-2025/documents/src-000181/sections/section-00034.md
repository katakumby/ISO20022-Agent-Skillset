---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.12 OrderBookingDate <OrdrBookgDt>"]
file_pages: [53]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.12 OrderBookingDate <OrdrBookgDt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 53 to 53.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 53

```text
PlaceOfTrade <PlcOfTrad> contains the following elements (see "MarketIdentification93" on page 282
for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 282
   Type <Tp> [0..1] ± 282
Constraints
• IdentificationPresenceRule
If Type/Code is not Various (VARI) OR Over The Counter (OTCO) then Identification must be
present. 
• MarketTypeAndIdentificationRule
If Type/Code is OverTheCounter (OTCO) and if Identification is present, then Identification/
Description must specify a system.
If Type/Code is Exchange (EXCH) and if Identification is present, then Identification/
MarketIdentifierCode must be present.
• PlaceOfTradeRule
If the trade was executed on multiple places of trade and the place of trade field is used, code VARI
must be used.
3.4.4.12  OrderBookingDate <OrdrBookgDt>
Presence: [0..1]
Definition: Date and time when an entry is posted to an account on the account servicer's books.
Datatype: "ISODate" on page 662
3.4.4.13  TradeOriginationDate <TradOrgtnDt>
Presence: [0..1]
Definition: Indicates the date and time of the agreement in principal between counter-parties prior to
actual trade date.
Used with fixed income for municipal new issue markets.
Datatype: "ISODateTime" on page 662
3.4.4.14  TradeDate <TradDt>
Presence: [1..1]
Definition: Specifies the date/time on which the trade was executed.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 53 February 2025
```

