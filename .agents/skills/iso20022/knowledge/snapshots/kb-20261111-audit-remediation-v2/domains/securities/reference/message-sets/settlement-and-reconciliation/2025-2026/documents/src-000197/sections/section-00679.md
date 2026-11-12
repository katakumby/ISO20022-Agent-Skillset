---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["29 sese.035.001.13 SecuritiesFinancingConfirmationV13", "29.4 Message Building Blocks", "29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>"]
file_pages: [1023, 1024]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.035.001.13"]
---

# 29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1023 to 1024.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1023

```text
SafekeepingPlace <SfkpgPlc> contains the following elements (see "SafeKeepingPlace5" on
page 1749 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SafekeepingPlaceFormat <SfkpgPlcFrmt> [0..1] ± 1749
   LEI <LEI> [0..1] IdentifierSet 1750
Constraints
• SafekeepingPlaceFormatOrLEIRule
SafekeepingPlaceFormat must be present or LEI must be present.
Following Must be True
    /SafekeepingPlaceFormat Must be present
 Or    /LEI Must be present
29.4.7 SecuritiesFinancingDetails <SctiesFincgDtls>
Presence: [0..1]
Definition: Details of the closing of the securities financing transaction.
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1023 March 2026
```

## File page 1024

```text
SecuritiesFinancingDetails <SctiesFincgDtls> contains the following
SecuritiesFinancingTransactionDetails56 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   SecuritiesFinancingTradeIdentification
<SctiesFincgTradId>
[0..1] Text 1025
   SecuritiesFinancingUniqueTransactionIdentifier
<SctiesFincgUnqTxIdr>
[0..1] IdentifierSet 1025
   ClosingLegIdentification <ClsgLegId> [0..1] Text 1025
   TerminationDate <TermntnDt> [0..1] ± 1025
   RateChangeDate <RateChngDt> [0..1] ± 1025
   EarliestCallBackDate <EarlstCallBckDt> [0..1] ± 1026
   CommissionCalculationDate <ComssnClctnDt> [0..1] ± 1026
   RateType <RateTp> [0..1] ± 1026
   Revaluation <Rvaltn> [0..1] ± 1026
   LegalFramework <LglFrmwk> [0..1] ± 1027
   InterestComputationMethod <IntrstCmptnMtd> [0..1] ± 1027
   MaturityDateModification <MtrtyDtMod> [0..1] Indicator 1027
   InterestPayment <IntrstPmt> [0..1] Indicator 1027
   VariableRateSupport <VarblRateSpprt> [0..1] ± 1028
   RepurchaseRate <RpRate> [0..1] ± C53 1028
   StockLoanMargin <StockLnMrgn> [0..1] ± C53 1028
   SecuritiesHaircut <SctiesHrcut> [0..1] ± C53 1029
   ChargesRate <ChrgsRate> [0..1] ± C53 1029
   PricingRate <PricgRate> [0..1] ± 1029
   Spread <Sprd> [0..1] ± C53 1030
   TransactionCallDelay <TxCallDely> [0..1] Text 1030
   TotalNumberOfCollateralInstructions
<TtlNbOfCollInstrs>
[0..1] Text 1030
   DealAmount <DealAmt> [0..1] ± 1030
   AccruedInterestAmount <AcrdIntrstAmt> [0..1] ± 1031
   ForfeitAmount <FrftAmt> [0..1] ± 1031
   PremiumAmount <PrmAmt> [0..1] ± 1031
   TerminationAmountPerPieceOfCollateral
<TermntnAmtPerPcOfColl>
[0..1] ± 1032
   TerminationTransactionAmount <TermntnTxAmt> [0..1] ± 1032
Approved by the Securities SEG on 27 January 2026 sese.035.001.13
SecuritiesFinancingConfirmationV13
Settlement And Reconciliation - Maintenance 2025 - 2026 1024 March 2026
```

