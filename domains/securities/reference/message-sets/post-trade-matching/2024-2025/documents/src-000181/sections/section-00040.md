---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.4 TradeDetails <TradDtls>", "3.4.4.29 AccruedInterestAmount <AcrdIntrstAmt>"]
file_pages: [59]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.4.29 AccruedInterestAmount <AcrdIntrstAmt>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 59 to 59.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
CodeName Name Definition
CINT CumInterest Indicates deal price including accrued
interest.
XINT ExInterest Indicates deal price excluding accrued
interest.
3.4.4.29  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between two periods, for example, in between interest
payment periods.
AccruedInterestAmount <AcrdIntrstAmt> contains the following elements (see
"AmountAndDirection29" on page 228 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C10 228
   CreditDebitIndicator <CdtDbtInd> [0..1] CodeSet 229
   OriginalCurrencyAndOrderedAmount
<OrgnlCcyAndOrdrdAmt>
[0..1] Amount C2, C10 229
   ForeignExchangeDetails <FXDtls> [0..1] ± 229
3.4.4.30  AccruedInterestPercentage <AcrdIntrstPctg>
Presence: [0..1]
Definition: Interest rate that has been accrued in between coupon payment periods.
Datatype: "PercentageRate" on page 667
3.4.4.31  TradeRegulatoryConditionsType <TradRgltryCondsTp>
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
3.4.4.32  CurrencyToBuyOrSell <CcyToBuyOrSell>
Presence: [0..1]
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds
or to sell the indicated currency in order to obtain the necessary currency to fund the transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 59 February 2025
```

