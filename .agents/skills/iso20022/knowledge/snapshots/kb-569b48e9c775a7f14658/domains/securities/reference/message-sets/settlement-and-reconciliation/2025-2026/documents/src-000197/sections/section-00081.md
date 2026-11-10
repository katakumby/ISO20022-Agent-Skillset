---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["3 semt.003.001.12 SecuritiesBalanceAccountingReportV12", "3.4 Message Building Blocks", "3.4.9 SubAccountDetails <SubAcctDtls>", "3.4.9.5 BalanceForSubAccount <BalForSubAcct>", "3.4.9.5.9 ForeignExchangeDetails <FXDtls>"]
file_pages: [121]
content_origin: "source-text-extraction"
mentioned_message_ids: ["semt.003.001.12"]
---

# 3.4.9.5.9 ForeignExchangeDetails <FXDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 121 to 121.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 121

```text
Constraints
• ValueRule
If TypeOfPriceCode is not MRKT, then Value may not be expressed with UnknownIndicator.
3.4.9.5.9  ForeignExchangeDetails <FXDtls>
Presence: [0..*]
Definition: Information needed to process a currency exchange or conversion.
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
3.4.9.5.10  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 2189
3.4.9.5.11  AccountBaseCurrencyAmounts <AcctBaseCcyAmts>
Presence: [1..1]
Definition: Valuation amounts provided in the base currency of the account.
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
3.4.9.5.12  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the currency of the financial instrument.
Approved by the Securities SEG on 27 January 2026 semt.003.001.12
SecuritiesBalanceAccountingReportV12
Settlement And Reconciliation - Maintenance 2025 - 2026 121 March 2026
```

