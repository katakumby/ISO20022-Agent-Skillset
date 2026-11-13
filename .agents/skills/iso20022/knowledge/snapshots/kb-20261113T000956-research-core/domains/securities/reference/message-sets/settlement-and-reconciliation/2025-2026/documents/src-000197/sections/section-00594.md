---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.5 TradeDetails <TradDtls>", "27.4.5.6 NumberOfDaysAccrued <NbOfDaysAcrd>"]
file_pages: [903]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.5.6 NumberOfDaysAccrued <NbOfDaysAcrd>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 903 to 903.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 903

```text
DealPrice <DealPric> contains the following elements (see "Price10" on page 1712 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1712
{Or     Yielded <Yldd> [1..1] Indicator 1712
Or}     ValueType <ValTp> [1..1] CodeSet 1712
   Value <Val> [1..1] ± 1713
27.4.5.6  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C36 "NumberRule"
Datatype: "Max3Number" on page 2189
Constraints
• NumberRule
If Number is negative, then Sign must be present.
27.4.5.7  Reporting <Rptg>
Presence: [0..*]
Definition: Specifies that a trade is to be reported to a third party.
Reporting <Rptg> contains one of the following elements (see "Reporting6Choice" on page 1592 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1592
Or}   Proprietary <Prtry> [1..1] ± 1592
27.4.5.8  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition5Choice" on page 2032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2032
Or}   Proprietary <Prtry> [1..1] ± 2033
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 903 March 2026
```

