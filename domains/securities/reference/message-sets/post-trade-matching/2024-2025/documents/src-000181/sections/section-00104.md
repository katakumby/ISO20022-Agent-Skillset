---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["3 setr.027.001.05 SecuritiesTradeConfirmationV05", "3.4 Message Building Blocks", "3.4.20 TwoLegTransactionDetails <TwoLegTxDtls>", "3.4.20.11 TwoLegTransactionType <TwoLegTxTp>", "3.4.20.11.2 SecuritiesFinancingDetails <SctiesFincgDtls>"]
file_pages: [136, 137]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.027.001.05"]
---

# 3.4.20.11.2 SecuritiesFinancingDetails <SctiesFincgDtls>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 136 to 137.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 136

```text
FutureOrOptionDetails <FutrOrOptnDtls> contains the following elements (see
"FutureOrOptionDetails3" on page 323 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FutureAndOptionContractType <FutrAndOptnCtrctTp> [0..1] CodeSet 324
   LastDeliveryDate <LastDlvryDt> [0..1] DateTime 325
   UnitOfMeasure <UnitOfMeasr> [0..1] CodeSet 325
   FutureDate <FutrDt> [0..1] DateTime 326
   MinimumSize <MinSz> [0..1] Amount C1, C9 326
   AnnouncementDate <AnncmntDt> [0..1] DateTime 327
   Appearance <Apprnc> [0..1] CodeSet 327
   StrippableIndicator <StrpblInd> [0..1] Indicator 327
   PositionLimit <PosLmt> [0..1] Quantity 327
   NearTermPositionLimit <NearTermPosLmt> [0..1] Quantity 328
   MinimumTradingPricingIncrement
<MinTradgPricgIncrmt>
[0..1] Quantity 328
   Purpose <Purp> [0..1] Text 328
   ContractSettlementMonth <CtrctSttlmMnth> [0..1] YearMonth 328
   FirstDealingDate <FrstDealgDt> [0..1] ± 328
   Ratio <Ratio> [0..*] ± 328
   Rating <Ratg> [0..*] ± 329
   IssuePrice <IssePric> [0..1] ± 329
   OptionRights <OptnRghts> [0..1] ± 329
   LastTransaction <LastTx> [0..1] Indicator 330
   SpreadTransaction <SprdTx> [0..1] Indicator 330
3.4.20.11.2  SecuritiesFinancingDetails <SctiesFincgDtls>
Presence: [1..1]
Definition: Provides details about the two leg transaction.
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 136 February 2025
```

## File page 137

```text
SecuritiesFinancingDetails <SctiesFincgDtls> contains the following elements (see
"SecuritiesFinancing12" on page 358 for details)
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
Approved by the Securities SEG on 13 February 2025 setr.027.001.05 SecuritiesTradeConfirmationV05
Post Trade Matching - Maintenance 2024 - 2025 137 February 2025
```

