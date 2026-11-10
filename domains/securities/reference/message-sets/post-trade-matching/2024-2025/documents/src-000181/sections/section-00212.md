---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.11 Date Time", "7.1.11.6 SettlementDateCode12Choice"]
file_pages: [266]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.11.6 SettlementDateCode12Choice

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 266 to 266.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 266

```text
Datatype: "ISODateTime" on page 662
7.1.11.6  SettlementDateCode12Choice
Definition: Choice of format for the settlement date code.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 266
Or}   Proprietary <Prtry> [1..1] ± 266
7.1.11.6.1  Code <Cd>
Presence: [1..1]
Definition: Settlement date expressed as an ISO 20022 code.
Datatype: "SettlementDate5Code" on page 645
CodeName Name Definition
REGU Regular Settlement takes place under the
standard rules applicable to the market
and instrument.
CASH Cash Settlement takes place on the trade
date.
NXTD NextDay Settlement takes place on the day after
trade date.
TONE TPlusOne Settlement takes place on the trade date
plus one business day.
TTWO TPlusTwo Settlement takes place on the trade date
plus two business days.
TTRE TPlusThree Settlement takes place on the trade date
plus three business days.
TFOR TPlusFour Settlement takes place on the trade date
plus four business days.
TFIV TPlusFive Settlement takes place on the trade date
plus five business days.
SELL SellersOption Settlement takes place at the choice/
option of the seller.
WDIS WhenDistributed Settlement takes place when the
financial instrument is distributed.
WHID WhenIssuedOrDistributed Settlement takes place when the
financial instrument is issued or
distributed.
TBAT ToBeAnnouncedTrade Settlement takes place as a result of a
"to be announced" trade.
WISS WhenIssued Settlement is to be done when the
security is issued.
7.1.11.6.2  Proprietary <Prtry>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 266 February 2025
```

