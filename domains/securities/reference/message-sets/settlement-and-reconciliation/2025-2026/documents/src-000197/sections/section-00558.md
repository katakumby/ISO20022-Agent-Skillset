---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["25 sese.031.001.11 SecuritiesSettlementConditionModificationStatusAdviceV11", "26.4 Message Building Blocks", "26.4.3 Linkages <Lnkgs>", "26.4.4.14 Reporting <Rptg>"]
file_pages: [842]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.032.001.13"]
---

# 26.4.4.14 Reporting <Rptg>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 842 to 842.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 842

```text
OpeningClosing <OpngClsg> contains one of the following elements (see "OpeningClosing3Choice"
on page 1608 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1608
Or}   Proprietary <Prtry> [1..1] ± 1609
26.4.4.14  Reporting <Rptg>
Presence: [0..*]
Definition: Specifies that a trade is to be reported to a third party.
Reporting <Rptg> contains one of the following elements (see "Reporting6Choice" on page 1592 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1592
Or}   Proprietary <Prtry> [1..1] ± 1592
26.4.4.15  TradeTransactionCondition <TradTxCond>
Presence: [0..*]
Definition: Indicates the conditions under which the order/trade is to be/was executed.
TradeTransactionCondition <TradTxCond> contains one of the following elements (see
"TradeTransactionCondition5Choice" on page 2032 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2032
Or}   Proprietary <Prtry> [1..1] ± 2033
26.4.4.16  InvestorCapacity <InvstrCpcty>
Presence: [0..1]
Definition: Specifies the role of the investor in the transaction.
InvestorCapacity <InvstrCpcty> contains one of the following elements (see
"InvestorCapacity4Choice" on page 1547 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1547
Or}   Proprietary <Prtry> [1..1] ± 1547
26.4.4.17  TradeOriginatorRole <TradOrgtrRole>
Presence: [0..1]
Definition: Specifies the role of the trading party in the transaction.
Approved by the Securities SEG on 27 January 2026 sese.032.001.13
SecuritiesSettlementTransactionGenerationNotificati
onV13
Settlement And Reconciliation - Maintenance 2025 - 2026 842 March 2026
```

