---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["2 semt.002.001.12 SecuritiesBalanceCustodyReportV12", "2.4 Message Building Blocks", "2.4.8 BalanceForAccount <BalForAcct>", "2.4.8.18 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "2.4.8.18.9 DaysAccrued <DaysAcrd>"]
file_pages: [48]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.002.001.12"]
---

# 2.4.8.18.9 DaysAccrued <DaysAcrd>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 48 to 48.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 48

```text
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms34"
on page 1477 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C2 1477
   QuotedCurrency <QtdCcy> [1..1] CodeSet C2 1477
   ExchangeRate <XchgRate> [1..1] Rate 1477
   QuotationDate <QtnDt> [0..1] DateTime 1478
   QuotingInstitution <QtgInstn> [0..1] ± 1478
2.4.8.18.9  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 2189
2.4.8.18.10  AccountBaseCurrencyAmounts <AcctBaseCcyAmts>
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
2.4.8.18.11  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the currency of the financial instrument.
Impacted by: C18 "EligibleCollateralValueRule"
Approved by the Securities SEG on 27 January 2026 semt.002.001.12
SecuritiesBalanceCustodyReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 48 March 2026
```

