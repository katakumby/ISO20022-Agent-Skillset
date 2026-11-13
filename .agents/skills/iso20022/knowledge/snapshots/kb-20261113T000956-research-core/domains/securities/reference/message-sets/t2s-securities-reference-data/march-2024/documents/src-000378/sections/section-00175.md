---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesReferenceData"
source_ids: ["src-000378"]
source_editions: ["March 2024"]
message_ids: []
heading_path: ["13 Message Items Types", "13.1 MessageComponents", "13.1.6 Financial Instrument", "13.1.6.1 FinancialInstrument97", "13.1.6.1.3 Debt <Debt>"]
file_pages: [239, 240, 241, 242]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 13.1.6.1.3 Debt <Debt>

Source: [src-000378](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesReferenceData_v1.pdf`. Locator: one-based file pages 239 to 242.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 239

```text
Warrant <Warrt> contains the following elements (see "Warrant4" on page 227 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Multiplier <Mltplr> [0..1] Rate 228
   SubscriptionPrice <SbcptPric> [0..1]  228
     ValueType <ValTp> [0..1] CodeSet 229
     Value <Val> [1..1] ± 229
     PriceType <PricTp> [0..1] CodeSet 230
   Type <Tp> [0..1]  230
{Or     Code <Cd> [1..1] CodeSet 231
Or}     Proprietary <Prtry> [1..1] ± 231
   WarrantAgent <WarrtAgt> [0..*]  231
     Name <Nm> [1..1] Text 232
     Identification <Id> [0..1]  232
{Or       AnyBIC <AnyBIC> [1..1] IdentifierSet C3 232
Or}       ProprietaryIdentification <PrtryId> [1..1] ± 233
     Purpose <Purp> [0..1] Text 233
     TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 233
     RegistrationCountry <RegnCtry> [0..1] CodeSet C4 233
     RegistrationDate <RegnDt> [0..1] Date 234
     TaxIdentificationNumber <TaxIdNb> [0..1] Text 234
     NationalRegistrationNumber <NtlRegnNb> [0..1] Text 234
     PostalAddress <PstlAdr> [1..5] ± C10 234
     PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 234
     SecondaryCommunicationAddress <ScndryComAdr> [0..1] ± 235
13.1.6.1.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 239 March 2024
```

## File page 240

```text
Debt <Debt> contains the following elements (see "Debt5" on page 198 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 202
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 202
   PaymentFrequency <PmtFrqcy> [0..1] ± 203
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 203
   DatedDate <DtdDt> [0..1] DateTime 203
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 203
   MaturityDate <MtrtyDt> [0..1] DateTime 203
   NextCouponDate <NxtCpnDt> [0..1] DateTime 203
   PutableDate <PutblDt> [0..1] DateTime 204
   NextCallableDate <NxtCllblDt> [0..1] DateTime 204
   NextFactorDate <NxtFctrDt> [0..1] DateTime 204
   ExpirationDate <XprtnDt> [0..1] DateTime 204
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 204
   InterestRate <IntrstRate> [0..1] Rate 204
   NextInterestRate <NxtIntrstRate> [0..1] Rate 204
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 204
   CallableIndicator <CllblInd> [0..1] Indicator 205
   CPProgram <CPPrgm> [0..1] Quantity 205
   CPRegistrationType <CPRegnTp> [0..1] Text 205
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 205
   PutableIndicator <PutblInd> [0..1] Indicator 206
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 206
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 206
   PerpetualIndicator <PerptlInd> [0..1] Indicator 206
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 206
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 207
   ExtendiblePeriod <XtndblPrd> [0..1]  207
{Or     FromDateTime <FrDtTm> [1..1] DateTime 207
Or     ToDateTime <ToDtTm> [1..1] DateTime 207
Or}     DateTimeRange <DtTmRg> [1..1] ± 207
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 207
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 240 March 2024
```

## File page 241

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 208
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 208
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 208
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 208
   CapitalisedInterest <CptlsdIntrst> [0..1]  208
{Or     Code <Cd> [1..1] CodeSet 209
Or}     Proprietary <Prtry> [1..1] ± 209
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 209
   CurrentFactor <CurFctr> [0..1] Rate 210
   NextFactor <NxtFctr> [0..1] Rate 210
   PreviousFactor <PrvsFctr> [0..1] Rate 210
   Pieces <Pcs> [0..1] Quantity 210
   PoolsMaximum <PlsMax> [0..1] Quantity 210
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 210
   PoolsPerLot <PlsPerLot> [0..1] Quantity 210
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 211
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 211
   LotIdentification <LotId> [0..1] Text 211
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 211
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 211
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 211
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 211
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 212
   InsuredIndicator <InsrdInd> [0..1] Indicator 212
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 212
   YieldCalculation <YldClctn> [0..*]  212
     Value <Val> [1..1] Rate 213
     CalculationType <ClctnTp> [0..1]  213
{Or       Code <Cd> [1..1] CodeSet 213
Or}       Proprietary <Prtry> [1..1] ± 216
     RedemptionPrice <RedPric> [0..1]  216
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 241 March 2024
```

## File page 242

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 216
       Value <Val> [1..1] ± 217
       PriceType <PricTp> [0..1] CodeSet 217
     ValueDate <ValDt> [1..1] Date 218
     ValuePeriod <ValPrd> [1..1]  218
{Or       FromDateTime <FrDtTm> [1..1] DateTime 218
Or       ToDateTime <ToDtTm> [1..1] DateTime 219
Or}       DateTimeRange <DtTmRg> [1..1] ± 219
     CalculationDate <ClctnDt> [1..1] DateTime 219
   InterestType <IntrstTp> [0..1] CodeSet 219
   InstrumentStructureType <InstrmStrTp> [0..1]  219
{Or     Code <Cd> [1..1] CodeSet 220
Or}     Proprietary <Prtry> [1..1] ± 221
   GlobalType <GblTp> [0..1]  221
{Or     Code <Cd> [1..1] CodeSet 221
Or}     Proprietary <Prtry> [1..1] ± 222
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 222
   Geographics <Geogcs> [0..1] Text 222
   YieldRange <YldRg> [0..1] ± 222
   CouponRange <CpnRg> [0..1] ± 223
   Purpose <Purp> [0..1] Text 223
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 223
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 224
   Haircut <Hrcut> [0..1] Rate 224
   TransactionConditions <TxConds> [0..1] ± 224
   LookBack <LookBck> [0..1] Quantity 224
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 224
   MinimumIncrement <MinIncrmt> [0..1] ± 224
   MinimumQuantity <MinQty> [0..1] ± 225
   Production <Pdctn> [0..1] Text 225
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 225
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 28 June 2021
Message Items Types
Target2-Securities - Securities Reference Data 242 March 2024
```

