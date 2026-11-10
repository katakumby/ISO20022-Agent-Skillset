---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["22 sese.028.001.12 SecuritiesSettlementTransactionAllegementNotificationV12", "22.4 Message Building Blocks", "22.4.7 FinancialInstrumentAttributes <FinInstrmAttrbts>", "22.4.9.8 InterestPayment <IntrstPmt>"]
file_pages: [751]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.028.001.12"]
---

# 22.4.9.8 InterestPayment <IntrstPmt>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 751 to 751.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 751

```text
22.4.9.8  InterestPayment <IntrstPmt>
Presence: [0..1]
Definition: Indicates whether the interest is to be paid to the collateral taker. If set to no, the interest is
paid to the collateral giver.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 2188):
• Meaning When True: Yes
• Meaning When False: No
22.4.9.9  VariableRateSupport <VarblRateSpprt>
Presence: [0..1]
Definition: Index or support rate used together with the spread to calculate the repurchase rate.
VariableRateSupport <VarblRateSpprt> contains the following elements (see "RateName1" on
page 1747 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Issuer <Issr> [0..1] Text 1747
   RateName <RateNm> [1..1] Text 1747
22.4.9.10  RepurchaseRate <RpRate>
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
22.4.9.11  TransactionCallDelay <TxCallDely>
Presence: [0..1]
Definition: Minimum number of days' notice a counterparty needs for terminating the transaction.
Datatype: "Exact3NumericText" on page 2190
22.4.9.12  AccruedInterestAmount <AcrdIntrstAmt>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 sese.028.001.12
SecuritiesSettlementTransactionAllegementNotificat
ionV12
Settlement And Reconciliation - Maintenance 2025 - 2026 751 March 2026
```

