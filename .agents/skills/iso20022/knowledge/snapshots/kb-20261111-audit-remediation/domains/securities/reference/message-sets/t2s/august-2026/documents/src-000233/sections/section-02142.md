---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.17 AggregateBalancePerSafekeepingPlace44", "82.1.5.17.9 DaysAccrued <DaysAcrd>"]
file_pages: [2903]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.17.9 DaysAccrued <DaysAcrd>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2903 to 2903.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2903

```text
ForeignExchangeDetails <FXDtls> contains the following elements (see "ForeignExchangeTerms34"
on page 2956 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 2957
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 2957
   ExchangeRate <XchgRate> [1..1] Rate 2957
   QuotationDate <QtnDt> [0..1] DateTime 2957
   QuotingInstitution <QtgInstn> [0..1] ± 2957
82.1.5.17.9  DaysAccrued <DaysAcrd>
Presence: [0..1]
Definition: Specifies the number of days used for calculating the accrued interest amount.
Datatype: "Number" on page 3324
82.1.5.17.10  AccountBaseCurrencyAmounts <AcctBaseCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the base currency of the account.
Impacted by: C19 "EligibleCollateralValueRule"
AccountBaseCurrencyAmounts <AcctBaseCcyAmts> contains the following elements (see
"BalanceAmounts3" on page 2855 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   HoldingValue <HldgVal> [0..1] ± 2855
   PreviousHoldingValue <PrvsHldgVal> [0..1] ± 2855
   BookValue <BookVal> [0..1] ± 2856
   EligibleCollateralValue <ElgblCollVal> [0..1] ± 2856
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 2856
Constraints
• EligibleCollateralValueRule
EligibleCollateralValue is only to be used in (I)CSD-participant communication or if bilaterally agreed
between the sender and receiver.
82.1.5.17.11  InstrumentCurrencyAmounts <InstrmCcyAmts>
Presence: [0..1]
Definition: Valuation amounts provided in the currency of the financial instrument.
Impacted by: C19 "EligibleCollateralValueRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2903 August 2026
```

