---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["71 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "71.4 Message Building Blocks", "71.4.1 QueryDefinition <QryDef>", "71.4.1.2 SearchCriteria <SchCrit>", "71.4.1.2.24 SecuritiesTransactionCondition <SctiesTxCond>"]
file_pages: [2469]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 71.4.1.2.24 SecuritiesTransactionCondition <SctiesTxCond>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2469 to 2469.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2469

```text
CodeName Name Definition
CLBR ClosureBeforeRollOver Trade to be executed for closure of a
previous position before the rollover of a
position (Deferred Settlement Service).
MONT Monthly Trade to be executed for month-end
settlement (Deferred Settlement
Service).
NBFR NewTradeFollowingRollover Trade to be executed for a new trade
position on the next month following the
roll-over of a position (Deferred
Settlement Service).
TRFR TradeFollowingRollover Trade to be executed on the next month
following the roll-over of positions.
PUTT Putt Trade to be executed following the
exercise of a put option on the security.
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
71.4.1.2.24  SecuritiesTransactionCondition <SctiesTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
SecuritiesTransactionCondition <SctiesTxCond> contains one of the following elements (see
"SettlementTransactionCondition34Choice" on page 3000 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 3000
Or}   Proprietary <Prtry> [1..1] ± 3002
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities 2469 August 2026
```

