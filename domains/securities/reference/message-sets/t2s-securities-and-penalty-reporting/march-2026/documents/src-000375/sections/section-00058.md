---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["3 semt.026.001.01 SecuritiesSettlementTransactionQueryV01", "3.4 Message Building Blocks", "3.4.1 QueryDefinition <QryDef>", "3.4.1.2 SearchCriteria <SchCrit>", "3.4.1.2.24 SecuritiesTransactionCondition <SctiesTxCond>"]
file_pages: [73]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.026.001.01"]
---

# 3.4.1.2.24 SecuritiesTransactionCondition <SctiesTxCond>

Source: [src-000375](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 73 to 73.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 73

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
3.4.1.2.24  SecuritiesTransactionCondition <SctiesTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
SecuritiesTransactionCondition <SctiesTxCond> contains one of the following elements (see
"SettlementTransactionCondition34Choice" on page 370 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 370
Or}   Proprietary <Prtry> [1..1] ± 371
Approved by the Securities SEG 19 February 2026. semt.026.001.01
SecuritiesSettlementTransactionQueryV01
Target2-Securities - Securities and Penalty Reporting 73 March 2026
```

