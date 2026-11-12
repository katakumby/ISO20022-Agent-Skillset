---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.5 BalanceForSubAccount <BalForSubAcct>", "3.4.9.5.13 AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>"]
file_pages: [122]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.5.13 AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 122 to 122.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 122

```text
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
3.4.9.5.13  AlternateReportingCurrencyAmounts <AltrnRptgCcyAmts>
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
3.4.9.5.14  QuantityBreakdown <QtyBrkdwn>
Presence: [0..*]
Definition: Breakdown of the aggregate quantity reported into significant lots, for example, tax lots.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 122 March 2026
```

