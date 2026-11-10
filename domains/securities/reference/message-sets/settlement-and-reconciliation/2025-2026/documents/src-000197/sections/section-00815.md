---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["32 sese.038.001.11 SecuritiesSettlementTransactionModificationRequestV11", "32.4 Message Building Blocks", "32.4.2 UpdateType <UpdTp>", "32.4.2.2 Deletion <Deltn>", "32.4.2.2.3 TradeDetails <TradDtls>", "32.4.2.2.3.9 NumberOfDaysAccrued <NbOfDaysAcrd>"]
file_pages: [1223]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.038.001.11"]
---

# 32.4.2.2.3.9 NumberOfDaysAccrued <NbOfDaysAcrd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1223 to 1223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1223

```text
DealPrice <DealPric> contains the following elements (see "Price10" on page 1712 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [1..1]  1712
{Or     Yielded <Yldd> [1..1] Indicator 1712
Or}     ValueType <ValTp> [1..1] CodeSet 1712
   Value <Val> [1..1] ± 1713
32.4.2.2.3.9  NumberOfDaysAccrued <NbOfDaysAcrd>
Presence: [0..1]
Definition: Number of days on which the interest rate accrues (daily accrual note).
Impacted by: C38 "NumberRule"
Datatype: "Max3Number" on page 2189
Constraints
• NumberRule
If Number is negative, then Sign must be present.
32.4.2.2.3.10  OpeningClosing <OpngClsg>
Presence: [0..1]
Definition: Specifies additional information relative to the processing of the trade.
OpeningClosing <OpngClsg> contains one of the following elements (see "OpeningClosing3Choice"
on page 1608 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1608
Or}   Proprietary <Prtry> [1..1] ± 1609
32.4.2.2.3.11  Reporting <Rptg>
Presence: [0..*]
Definition: Specifies that a trade is to be reported to a third party.
Reporting <Rptg> contains one of the following elements (see "Reporting6Choice" on page 1592 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1592
Or}   Proprietary <Prtry> [1..1] ± 1592
32.4.2.2.3.12  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 sese.038.001.11
SecuritiesSettlementTransactionModificationReques
tV11
Settlement And Reconciliation - Maintenance 2025 - 2026 1223 March 2026
```

