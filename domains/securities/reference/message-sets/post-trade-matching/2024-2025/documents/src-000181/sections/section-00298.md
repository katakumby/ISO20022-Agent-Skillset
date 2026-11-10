---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.48 AutomaticBorrowing6Choice", "7.1.19.48.2 Proprietary <Prtry>"]
file_pages: [358, 359]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.48.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 358 to 359.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 358

```text
CodeName Name Definition
YBOR Automatic Automatic borrowing should take place.
7.1.19.48.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Condition for automatic borrowing expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.49  SecuritiesFinancing12
Definition: Details of the closing of the securities financing transaction.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 358 February 2025
```

## File page 359

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   RateChangeDate <RateChngDt> [0..1] DateTime 360
   RateType <RateTp> [0..1] ± 360
   Revaluation <Rvaltn> [0..1] ± 360
   LegalFramework <LglFrmwk> [0..1] CodeSet 361
   InterestComputationMethod <IntrstCmptnMtd> [0..1] ± 361
   VariableRateSupport <VarblRateSpprt> [0..1] ± 361
   RepurchaseRate <RpRate> [0..1] ± C48 361
   StockLoanMargin <StockLnMrgn> [0..1] ± C48 362
   SecuritiesHaircut <SctiesHrcut> [0..1] ± C48 362
   PricingRate <PricgRate> [0..1] ± 362
   SpreadRate <SprdRate> [0..1] ± 363
   CallableTradeIndicator <CllblTradInd> [0..1] Indicator 363
   TransactionCallDelay <TxCallDely> [0..1] Text 363
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 363
   AccruedInterestPercentage <AcrdIntrstPctg> [0..1] Rate 364
   ForfeitAmount <FrftAmt> [0..1] ± 364
   PremiumAmount <PrmAmt> [0..1] ± 364
   ClosingAmountPerPiecesOfCollateral
<ClsgAmtPerPcsOfColl>
[0..1] ± 364
   TotalNumberOfCollateralInstructions <TtlNbOfCollInstrs> [0..1] Text 365
   FinancingAgreement <FincgAgrmt> [0..1] ± 365
   LendingTransactionMethod <LndgTxMtd> [0..1] ± 365
   LendingWithCollateral <LndgWthColl> [0..1] Indicator 365
   BorrowingReason <BrrwgRsn> [0..1] ± 366
   CollateralType <CollTp> [0..1] ± 366
   ContractTermsModificationChanged
<CtrctTermsModChngd>
[0..1] Indicator 366
   InterestRate <IntrstRate> [0..1] ± C48 366
   BorrowingRate <BrrwgRate> [0..1] ± C48 367
   StandardCollateralRatio <StdCollRatio> [0..1] ± C48 367
   DividendRatio <DvddRatio> [0..1] ± C48 368
   NumberOfDaysLendingBorrowing
<NbOfDaysLndgBrrwg>
[0..1] ± 368
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 359 February 2025
```

