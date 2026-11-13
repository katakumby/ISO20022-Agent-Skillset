---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.8 Stipulations <Stiptns>", "3.4.8.8 AutoReinvestment <AutoRinvstmt>"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.8.8 AutoReinvestment <AutoRinvstmt>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
• Meaning When True: Yes
• Meaning When False: No
3.4.8.8  AutoReinvestment <AutoRinvstmt>
Presence: [0..1]
Definition: Indicates an instruction to reinvest dividends in the underlying security (or proceeds at
maturity in a similar instrument) if the current rate is <rate> or better.
Datatype: "PercentageRate" on page 667
3.4.8.9  TransactionConditions <TxConds>
Presence: [0..1]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
Datatype: "TradeTransactionCondition2Code" on page 652
CodeName Name Definition
SPCC SpecialCumCoupon Indicates whether the trade is executed
with a special cum coupon.
SECN SpecialExCoupon Indicates whether the trade is executed
with a special ex coupon.
SEBN SpecialExBonus Indicates whether the trade is executed
special ex bonus.
SCBN SpecialCumBonus Indicates whether the trade is executed
special cum bonus.
SCRT SpecialCumRights Indicates whether the trade is executed
special cum rights.
SERT SpecialExRights Indicates whether the trade is executed
special ex rights.
SCCR SpecialCumCapitalRepayments Indicates whether the trade is executed
special cum capital repayments.
SECR SpecialExCapitalRepayments Indicates whether the trade is executed
special ex capital repayments.
CAST CashSettlement Indicates whether the trade is executed
with a cash settlement.
SPPR SpecialPrice Indicates whether the trade is executed
with a special price.
SPCU SpecialCumDividend Indicates whether the trade is executed
with a special cum
dividend, that is, buying after the ex date
and getting the dividend.
SPEX SpecialExDividend Indicates whether the trade is executed
with a special ex
dividend, that is, selling before the ex
date without the coupon.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 98 February 2025
```

