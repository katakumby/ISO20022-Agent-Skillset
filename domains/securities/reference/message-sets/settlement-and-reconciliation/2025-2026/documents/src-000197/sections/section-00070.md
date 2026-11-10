---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.8 BalanceForAccount <BalForAcct>", "3.4.8.17 BalanceAtSafekeepingPlace <BalAtSfkpgPlc>", "3.4.8.17.9 InstrumentCurrencyAmounts <InstrmCcyAmts>"]
file_pages: [106]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.8.17.9 InstrumentCurrencyAmounts <InstrmCcyAmts>

Source: [src-000197](../../../../../../../../../raw-input/settlement_and_reconciliation/ISO20022_MDRPart2_SettlementAndReconciliation_2025_2026_v1.pdf). Locator: one-based file pages 106 to 106.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 106

```text
AccountBaseCurrencyAmounts <AcctBaseCcyAmts> contains the following elements (see
"BalanceAmounts1" on page 1410 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1410
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1410
   BookValue <BookVal> [0..1] ± 1411
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1411
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1411
3.4.8.17.9  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the currency of the financial instrument.
InstrumentCurrencyAmounts <InstrmCcyAmts> contains the following elements (see
"BalanceAmounts1" on page 1410 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1410
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1410
   BookValue <BookVal> [0..1] ± 1411
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1411
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1411
3.4.8.17.10  AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in a currency other than the base currency of the account.
AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts> contains the following elements (see
"BalanceAmounts1" on page 1410 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [1..1] ± 1410
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 1410
   BookValue <BookVal> [0..1] ± 1411
   UnrealisedGainLoss <UrlsdGnLoss> [0..1] ± 1411
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1411
3.4.8.17.11  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 106 March 2026
```

