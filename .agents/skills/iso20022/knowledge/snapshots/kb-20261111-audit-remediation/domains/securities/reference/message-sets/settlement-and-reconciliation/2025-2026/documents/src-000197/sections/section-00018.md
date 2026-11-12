---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.13 AccountBaseCurrencyAmounts <AcctBaseCcyAmts>"]
file_pages: [41]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.13 AccountBaseCurrencyAmounts <AcctBaseCcyAmts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 41 to 41.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 41

```text
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 2189
2.4.8.13  AccountBaseCurrencyAmounts <AcctBaseCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the base currency of the account.
Impacted by: C18 "EligibleCollateralValueRule"
AccountBaseCurrencyAmounts <AcctBaseCcyAmts> contains the following elements (see
"BalanceAmounts3" on page 1419 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 1419
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1420
   BookValue <BookVal> [0..1] ± 1420
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 1420
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1420
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
2.4.8.14  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the currency of the financial instrument.
Impacted by: C18 "EligibleCollateralValueRule"
InstrumentCurrencyAmounts <InstrmCcyAmts> contains the following elements (see
"BalanceAmounts3" on page 1419 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 1419
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1420
   BookValue <BookVal> [0..1] ± 1420
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 1420
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1420
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 41 March 2026
```

