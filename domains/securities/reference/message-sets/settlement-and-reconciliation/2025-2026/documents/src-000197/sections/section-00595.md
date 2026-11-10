---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["27 sese.033.001.13 SecuritiesFinancingInstructionV13", "27.4 Message Building Blocks", "27.4.5 TradeDetails <TradDtls>", "27.4.5.9 InvestorCapacity <InvstrCpcty>"]
file_pages: [904]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.033.001.13"]
---

# 27.4.5.9 InvestorCapacity <InvstrCpcty>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 904 to 904.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 904

```text
27.4.5.9  InvestorCapacity <InvstrCpcty>
Presence: [0..1]
Definition: Specifies the role of the investor in the transaction.
InvestorCapacity <InvstrCpcty> contains one of the following elements (see
"InvestorCapacity4Choice" on page 1547 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1547
Or}   Proprietary <Prtry> [1..1] ± 1547
27.4.5.10  TradeOriginatorRole <TradOrgtrRole>
Presence: [0..1]
Definition: Specifies the role of the trading party in the transaction.
TradeOriginatorRole <TradOrgtrRole> contains one of the following elements (see
"TradeOriginator3Choice" on page 1587 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1587
Or}   Proprietary <Prtry> [1..1] ± 1588
27.4.5.11  CurrencyToBuyOrSell <CcyToBuyOrSell>
Presence: [0..1]
Definition: Account servicer is instructed to buy the indicated currency after the receipt of cash proceeds
or to sell the indicated currency in order to obtain the necessary currency to fund the transaction.
CurrencyToBuyOrSell <CcyToBuyOrSell> contains one of the following elements (see
"CurrencyToBuyOrSell1Choice" on page 1568 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrencyToBuy <CcyToBuy> [1..1] CodeSet C1 1568
Or}   CurrencyToSell <CcyToSell> [1..1] CodeSet C1 1569
27.4.5.12  AffirmationStatus <AffirmSts>
Presence: [0..1]
Definition: Status of affirmation of a trade.
Approved by the Securities SEG on 27 January 2026 sese.033.001.13 SecuritiesFinancingInstructionV13
Settlement And Reconciliation - Maintenance 2025 - 2026 904 March 2026
```

