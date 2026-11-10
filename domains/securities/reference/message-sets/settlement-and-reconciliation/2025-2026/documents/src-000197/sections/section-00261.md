---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["7 semt.016.001.10 IntraPositionMovementPostingReportV10", "10.4 Message Building Blocks", "10.4.6 AllegementDetails <AllgmtDtls>", "10.4.6.25 SecuritiesFinancingDetails <SctiesFincgDtls>", "10.4.6.25.9 VariableRateSupport <VarblRateSpprt>"]
file_pages: [392]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.019.001.12"]
---

# 10.4.6.25.9 VariableRateSupport <VarblRateSpprt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 392 to 392.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 392

```text
Definition: Indicates whether the interest is to be paid to the collateral taker. If set to no, the interest is
paid to the collateral giver.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
10.4.6.25.9  VariableRateSupport <VarblRateSpprt>
Presence: [0..1]
Definition: Index or support rate used together with the spread to calculate the repurchase rate.
VariableRateSupport <VarblRateSpprt> contains the following elements (see "RateName1" on
page 1747 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 1747
   RateName <RateNm> [1..1] Text 1747
10.4.6.25.10  RepurchaseRate <RpRate>
Presence: [0..1]
Definition: Rate to be used to recalculate the repurchase amount.
Impacted by: C45 "SignRule"
RepurchaseRate <RpRate> contains the following elements (see "Rate2" on page 1748 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
10.4.6.25.11  TransactionCallDelay <TxCallDely>
Presence: [0..1]
Definition: Minimum number of days' notice a counterparty needs for terminating the transaction.
Datatype: "Exact3NumericText" on page 2190
10.4.6.25.12  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Definition: Interest amount that has accrued in between coupon payment periods.
Approved by the Securities SEG on 27 January 2026 semt.019.001.12
SecuritiesSettlementTransactionAllegementReportV
12
Settlement And Reconciliation - Maintenance 2025 - 2026 392 March 2026
```

