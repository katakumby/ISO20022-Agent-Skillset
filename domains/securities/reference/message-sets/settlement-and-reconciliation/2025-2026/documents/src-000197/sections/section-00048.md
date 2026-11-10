---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.10 AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts>", "2.4.10.1 TotalHoldingsValueOfPage <TtlHldgsValOfPg>"]
file_pages: [76]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.10.1 TotalHoldingsValueOfPage <TtlHldgsValOfPg>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 76 to 76.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 76

```text
AccountBaseCurrencyTotalAmounts <AcctBaseCcyTtlAmts> contains the following
TotalValueInPageAndStatement1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TotalHoldingsValueOfPage <TtlHldgsValOfPg> [0..1] ± 76
   TotalHoldingsValueOfStatement <TtlHldgsValOfStmt> [1..1] ± 76
   TotalBookValueOfStatement <TtlBookValOfStmt> [0..1] ± 76
   TotalEligibleCollateralValue <TtlElgblCollVal> [0..1] ± 77
Constraints
• TotalEligibleCollateralValueRule
Total eligible collateral value is only to be used in (I)CSD-participant communication or if bilaterally
agreed between the sender and receiver.
2.4.10.1  TotalHoldingsValueOfPage <TtlHldgsValOfPg>
Presence: [0..1]
Definition: Total value of positions reported in this message.
TotalHoldingsValueOfPage <TtlHldgsValOfPg> contains the following elements (see
"AmountAndDirection6" on page 1361 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C8 1362
   Sign <Sgn> [1..1] Indicator 1362
2.4.10.2  TotalHoldingsValueOfStatement <TtlHldgsValOfStmt>
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
2.4.10.3  TotalBookValueOfStatement <TtlBookValOfStmt>
Presence: [0..1]
Definition: Total book value of positions reported in this statement (a statement may comprise one or
more messages).
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 76 March 2026
```

