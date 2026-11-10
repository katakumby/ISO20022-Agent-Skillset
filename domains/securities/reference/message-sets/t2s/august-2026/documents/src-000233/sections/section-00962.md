---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.3 Modify <Modfy>", "28.4.2.1.3.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.3.1.2 Warrant <Warrt>", "28.4.2.1.3.1.2.4 WarrantAgent <WarrtAgt>", "28.4.2.1.3.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [1409, 1410, 1411, 1412]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.3.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1409 to 1412.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1409

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
28.4.2.1.3.1.2.4.11  SecondaryCommunicationAddress <ScndryComAdr>
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
28.4.2.1.3.1.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1409 August 2026
```

## File page 1410

```text
Debt <Debt> contains the following Debt5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1413
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 1413
   PaymentFrequency <PmtFrqcy> [0..1] ± 1414
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1414
   DatedDate <DtdDt> [0..1] DateTime 1414
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1414
   MaturityDate <MtrtyDt> [0..1] DateTime 1414
   NextCouponDate <NxtCpnDt> [0..1] DateTime 1414
   PutableDate <PutblDt> [0..1] DateTime 1415
   NextCallableDate <NxtCllblDt> [0..1] DateTime 1415
   NextFactorDate <NxtFctrDt> [0..1] DateTime 1415
   ExpirationDate <XprtnDt> [0..1] DateTime 1415
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1415
   InterestRate <IntrstRate> [0..1] Rate 1415
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1415
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 1415
   CallableIndicator <CllblInd> [0..1] Indicator 1416
   CPProgram <CPPrgm> [0..1] Quantity 1416
   CPRegistrationType <CPRegnTp> [0..1] Text 1416
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1416
   PutableIndicator <PutblInd> [0..1] Indicator 1416
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 1417
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 1417
   PerpetualIndicator <PerptlInd> [0..1] Indicator 1417
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1417
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 1417
   ExtendiblePeriod <XtndblPrd> [0..1]  1418
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1418
Or     ToDateTime <ToDtTm> [1..1] DateTime 1418
Or}     DateTimeRange <DtTmRg> [1..1] ± 1418
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1418
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1410 August 2026
```

## File page 1411

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1419
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1419
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 1419
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1419
   CapitalisedInterest <CptlsdIntrst> [0..1]  1419
{Or     Code <Cd> [1..1] CodeSet 1420
Or}     Proprietary <Prtry> [1..1] ± 1420
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1420
   CurrentFactor <CurFctr> [0..1] Rate 1421
   NextFactor <NxtFctr> [0..1] Rate 1421
   PreviousFactor <PrvsFctr> [0..1] Rate 1421
   Pieces <Pcs> [0..1] Quantity 1421
   PoolsMaximum <PlsMax> [0..1] Quantity 1421
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 1421
   PoolsPerLot <PlsPerLot> [0..1] Quantity 1421
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1422
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1422
   LotIdentification <LotId> [0..1] Text 1422
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1422
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1422
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1422
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1422
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1423
   InsuredIndicator <InsrdInd> [0..1] Indicator 1423
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1423
   YieldCalculation <YldClctn> [0..*]  1423
     Value <Val> [1..1] Rate 1424
     CalculationType <ClctnTp> [0..1]  1424
{Or       Code <Cd> [1..1] CodeSet 1424
Or}       Proprietary <Prtry> [1..1] ± 1427
     RedemptionPrice <RedPric> [0..1]  1427
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1411 August 2026
```

## File page 1412

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 1427
       Value <Val> [1..1] ± 1428
       PriceType <PricTp> [0..1] CodeSet 1428
     ValueDate <ValDt> [1..1] Date 1429
     ValuePeriod <ValPrd> [1..1]  1429
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1429
Or       ToDateTime <ToDtTm> [1..1] DateTime 1430
Or}       DateTimeRange <DtTmRg> [1..1] ± 1430
     CalculationDate <ClctnDt> [1..1] DateTime 1430
   InterestType <IntrstTp> [0..1] CodeSet 1430
   InstrumentStructureType <InstrmStrTp> [0..1]  1430
{Or     Code <Cd> [1..1] CodeSet 1431
Or}     Proprietary <Prtry> [1..1] ± 1432
   GlobalType <GblTp> [0..1]  1432
{Or     Code <Cd> [1..1] CodeSet 1432
Or}     Proprietary <Prtry> [1..1] ± 1433
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 1433
   Geographics <Geogcs> [0..1] Text 1433
   YieldRange <YldRg> [0..1] ± 1433
   CouponRange <CpnRg> [0..1] ± 1434
   Purpose <Purp> [0..1] Text 1434
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1434
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 1435
   Haircut <Hrcut> [0..1] Rate 1435
   TransactionConditions <TxConds> [0..1] ± 1435
   LookBack <LookBck> [0..1] Quantity 1435
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1435
   MinimumIncrement <MinIncrmt> [0..1] ± 1435
   MinimumQuantity <MinQty> [0..1] ± 1436
   Production <Pdctn> [0..1] Text 1436
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 1436
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1412 August 2026
```

