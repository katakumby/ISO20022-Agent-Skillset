---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.29 InterestType <IntrstTp>"]
file_pages: [349]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.29 InterestType <IntrstTp>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 349 to 349.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 349

```text
Definition: Specifies the number of days from trade date that the counterparty on the other side of the
trade should be "given up" or divulged.
Impacted by: C25 "NumberRule"
Datatype: "Max3Number" on page 666
Constraints
• NumberRule
If Number is negative, then Sign must be present.
7.1.19.43.29  InterestType <IntrstTp>
Presence: [0..1]
Definition: Indicates whether the trade is cum interest or ex interest.
Datatype: "InterestType2Code" on page 634
CodeName Name Definition
CINT CumInterest Indicates deal price including accrued
interest.
XINT ExInterest Indicates deal price excluding accrued
interest.
7.1.19.43.30  AccruedInterestPercentage <AcrdIntrstPctg>
Presence: [0..1]
Definition: Interest rate that has been accrued in between coupon payment periods.
Datatype: "PercentageRate" on page 667
7.1.19.43.31  TradeRegulatoryConditionsType <TradRgltryCondsTp>
Presence: [0..1]
Definition: Specifies the regulatory conditions type of the trade.
Datatype: "TradeRegulatoryConditions1Code" on page 652
CodeName Name Definition
SOLI Solicited Trade was solicited by the executing
broker. The broker has suggested to his
client to buy/sell financial instruments.
USOL Unsolicited Trade was unsolicited. The client acts on
its own without advice from the
executing broker.
7.1.19.43.32  CurrencyToBuyOrSell <CcyToBuyOrSell>
Presence: [0..1]
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds
or to sell the indicated currency in order to obtain the necessary currency to fund the transaction.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 349 February 2025
```

