---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.2 Delete <Del>", "28.4.2.1.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.2.1.2 Warrant <Warrt>", "28.4.2.1.2.1.2.4 WarrantAgent <WarrtAgt>", "28.4.2.1.2.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [1221, 1222, 1223, 1224]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.2.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1221 to 1224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1221

```text
PrimaryCommunicationAddress <PmryComAdr> contains the following elements (see
"CommunicationAddress3" on page 3100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
28.4.2.1.2.1.2.4.11  SecondaryCommunicationAddress <ScndryComAdr>
Presence: [0..1]
Definition: Communication device number or electronic address used for communication.
SecondaryCommunicationAddress <ScndryComAdr> contains the following elements (see
"CommunicationAddress3" on page 3100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Email <Email> [0..1] Text 3100
   Phone <Phne> [0..1] Text 3100
   Mobile <Mob> [0..1] Text 3101
   FaxNumber <FaxNb> [0..1] Text 3101
   TelexAddress <TlxAdr> [0..1] Text 3101
   URLAddress <URLAdr> [0..1] Text 3101
28.4.2.1.2.1.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1221 August 2026
```

## File page 1222

```text
Debt <Debt> contains the following Debt5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1225
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 1225
   PaymentFrequency <PmtFrqcy> [0..1] ± 1226
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1226
   DatedDate <DtdDt> [0..1] DateTime 1226
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1226
   MaturityDate <MtrtyDt> [0..1] DateTime 1226
   NextCouponDate <NxtCpnDt> [0..1] DateTime 1226
   PutableDate <PutblDt> [0..1] DateTime 1227
   NextCallableDate <NxtCllblDt> [0..1] DateTime 1227
   NextFactorDate <NxtFctrDt> [0..1] DateTime 1227
   ExpirationDate <XprtnDt> [0..1] DateTime 1227
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1227
   InterestRate <IntrstRate> [0..1] Rate 1227
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1227
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 1227
   CallableIndicator <CllblInd> [0..1] Indicator 1228
   CPProgram <CPPrgm> [0..1] Quantity 1228
   CPRegistrationType <CPRegnTp> [0..1] Text 1228
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1228
   PutableIndicator <PutblInd> [0..1] Indicator 1228
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 1229
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 1229
   PerpetualIndicator <PerptlInd> [0..1] Indicator 1229
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1229
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 1229
   ExtendiblePeriod <XtndblPrd> [0..1]  1230
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1230
Or     ToDateTime <ToDtTm> [1..1] DateTime 1230
Or}     DateTimeRange <DtTmRg> [1..1] ± 1230
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1230
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1222 August 2026
```

## File page 1223

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1231
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1231
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 1231
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1231
   CapitalisedInterest <CptlsdIntrst> [0..1]  1231
{Or     Code <Cd> [1..1] CodeSet 1232
Or}     Proprietary <Prtry> [1..1] ± 1232
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1232
   CurrentFactor <CurFctr> [0..1] Rate 1233
   NextFactor <NxtFctr> [0..1] Rate 1233
   PreviousFactor <PrvsFctr> [0..1] Rate 1233
   Pieces <Pcs> [0..1] Quantity 1233
   PoolsMaximum <PlsMax> [0..1] Quantity 1233
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 1233
   PoolsPerLot <PlsPerLot> [0..1] Quantity 1233
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1234
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1234
   LotIdentification <LotId> [0..1] Text 1234
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1234
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1234
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1234
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1234
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1235
   InsuredIndicator <InsrdInd> [0..1] Indicator 1235
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1235
   YieldCalculation <YldClctn> [0..*]  1235
     Value <Val> [1..1] Rate 1236
     CalculationType <ClctnTp> [0..1]  1236
{Or       Code <Cd> [1..1] CodeSet 1236
Or}       Proprietary <Prtry> [1..1] ± 1239
     RedemptionPrice <RedPric> [0..1]  1239
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1223 August 2026
```

## File page 1224

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 1239
       Value <Val> [1..1] ± 1240
       PriceType <PricTp> [0..1] CodeSet 1240
     ValueDate <ValDt> [1..1] Date 1241
     ValuePeriod <ValPrd> [1..1]  1241
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1241
Or       ToDateTime <ToDtTm> [1..1] DateTime 1242
Or}       DateTimeRange <DtTmRg> [1..1] ± 1242
     CalculationDate <ClctnDt> [1..1] DateTime 1242
   InterestType <IntrstTp> [0..1] CodeSet 1242
   InstrumentStructureType <InstrmStrTp> [0..1]  1242
{Or     Code <Cd> [1..1] CodeSet 1243
Or}     Proprietary <Prtry> [1..1] ± 1244
   GlobalType <GblTp> [0..1]  1244
{Or     Code <Cd> [1..1] CodeSet 1244
Or}     Proprietary <Prtry> [1..1] ± 1245
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 1245
   Geographics <Geogcs> [0..1] Text 1245
   YieldRange <YldRg> [0..1] ± 1245
   CouponRange <CpnRg> [0..1] ± 1246
   Purpose <Purp> [0..1] Text 1246
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1246
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 1247
   Haircut <Hrcut> [0..1] Rate 1247
   TransactionConditions <TxConds> [0..1] ± 1247
   LookBack <LookBck> [0..1] Quantity 1247
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1247
   MinimumIncrement <MinIncrmt> [0..1] ± 1247
   MinimumQuantity <MinQty> [0..1] ± 1248
   Production <Pdctn> [0..1] Text 1248
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 1248
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1224 August 2026
```

