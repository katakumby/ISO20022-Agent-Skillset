---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.10 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>", "3.4.10.2 TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>"]
file_pages: [133]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.10.2 TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 133 to 133.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 133

```text
3.4.10.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
Presence: [1..1]
Definition: Total value of positions reported in this statement (a statement may comprise one or more
messages).
TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
3.4.10.3  TotalBookValueOfStatement <TtlBookValOfStmt>
Presence: [0..1]
Definition: Total book value of positions reported in this statement (a statement may comprise one or
more messages).
TotalBookValueOfStatement <TtlBookValOfStmt> contains the following elements (see
"AmountAndDirection6" on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
3.4.11 AlternateReportingCurrencyTotalAmounts
<AltrnRptgCcyTtlAmts>
Presence: [0..1]
Definition: Total valuation amounts provided in a currency other than the base currency of the account.
AlternateReportingCurrencyTotalAmounts <AltrnRptgCcyTtlAmts> contains the following
TotalValueInPageAndStatement2 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 133
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 134
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 134
3.4.11.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 133 March 2026
```

