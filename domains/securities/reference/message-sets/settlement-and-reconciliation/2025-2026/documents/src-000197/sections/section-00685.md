---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>", "29.4.7.20 Spread <Sprd>"]
file_pages: [1030]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7.20 Spread <Sprd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 1030 to 1030.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1030

```text
PricingRate <PricgRate> contains one of the following elements (see "RateOrName1Choice" on
page 1576 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Rate <Rate> [1..1] ± C53 1576
Or}   RateName <RateNm> [1..1] ± 1577
29.4.7.20  Spread <Sprd>
Presence: [0..1]
Definition: Repurchase spread expressed as a rate; margin over or under an index that determines the
repurchase rate.
Impacted by: C53 "SignRule"
Spread <Sprd> contains the following elements (see "Rate2" on page 1748 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Sign <Sgn> [0..1] Indicator 1748
   Rate <Rate> [1..1] Rate 1749
Constraints
• SignRule
When Sign is present, rate must not be zero.
29.4.7.21  TransactionCallDelay <TxCallDely>
Presence: [0..1]
Definition: Minimum number of days' notice a counterparty needs for terminating the transaction.
Datatype: "Exact3NumericText" on page 2190
29.4.7.22  TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs>
Presence: [0..1]
Definition: Total number of collateral instructions involved in the transaction.
Datatype: "Exact3NumericText" on page 2190
29.4.7.23  DealAmount <DealAmt>
Presence: [0..1]
Definition: Principal amount of a trade (for second leg).
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1030 March 2026
```

