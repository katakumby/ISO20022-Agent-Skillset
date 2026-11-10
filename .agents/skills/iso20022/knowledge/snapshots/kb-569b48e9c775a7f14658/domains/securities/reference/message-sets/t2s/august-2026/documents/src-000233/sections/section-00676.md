---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.1 UpdateType <UpdTp>", "28.4.2.1.1 Add <Add>", "28.4.2.1.1.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.1.1.1.2 Warrant <Warrt>", "28.4.2.1.1.1.2.4 WarrantAgent <WarrtAgt>", "28.4.2.1.1.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [1033, 1034, 1035, 1036]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.1.1.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1033 to 1036.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1033

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
28.4.2.1.1.1.2.4.11  SecondaryCommunicationAddress <ScndryComAdr>
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
28.4.2.1.1.1.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1033 August 2026
```

## File page 1034

```text
Debt <Debt> contains the following Debt5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1037
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 1037
   PaymentFrequency <PmtFrqcy> [0..1] ± 1038
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1038
   DatedDate <DtdDt> [0..1] DateTime 1038
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1038
   MaturityDate <MtrtyDt> [0..1] DateTime 1038
   NextCouponDate <NxtCpnDt> [0..1] DateTime 1038
   PutableDate <PutblDt> [0..1] DateTime 1039
   NextCallableDate <NxtCllblDt> [0..1] DateTime 1039
   NextFactorDate <NxtFctrDt> [0..1] DateTime 1039
   ExpirationDate <XprtnDt> [0..1] DateTime 1039
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1039
   InterestRate <IntrstRate> [0..1] Rate 1039
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1039
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 1039
   CallableIndicator <CllblInd> [0..1] Indicator 1040
   CPProgram <CPPrgm> [0..1] Quantity 1040
   CPRegistrationType <CPRegnTp> [0..1] Text 1040
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1040
   PutableIndicator <PutblInd> [0..1] Indicator 1040
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 1041
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 1041
   PerpetualIndicator <PerptlInd> [0..1] Indicator 1041
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1041
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 1041
   ExtendiblePeriod <XtndblPrd> [0..1]  1042
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1042
Or     ToDateTime <ToDtTm> [1..1] DateTime 1042
Or}     DateTimeRange <DtTmRg> [1..1] ± 1042
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1042
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1034 August 2026
```

## File page 1035

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1043
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1043
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 1043
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1043
   CapitalisedInterest <CptlsdIntrst> [0..1]  1043
{Or     Code <Cd> [1..1] CodeSet 1044
Or}     Proprietary <Prtry> [1..1] ± 1044
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1044
   CurrentFactor <CurFctr> [0..1] Rate 1045
   NextFactor <NxtFctr> [0..1] Rate 1045
   PreviousFactor <PrvsFctr> [0..1] Rate 1045
   Pieces <Pcs> [0..1] Quantity 1045
   PoolsMaximum <PlsMax> [0..1] Quantity 1045
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 1045
   PoolsPerLot <PlsPerLot> [0..1] Quantity 1045
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1046
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1046
   LotIdentification <LotId> [0..1] Text 1046
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1046
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1046
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1046
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1046
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1047
   InsuredIndicator <InsrdInd> [0..1] Indicator 1047
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1047
   YieldCalculation <YldClctn> [0..*]  1047
     Value <Val> [1..1] Rate 1048
     CalculationType <ClctnTp> [0..1]  1048
{Or       Code <Cd> [1..1] CodeSet 1048
Or}       Proprietary <Prtry> [1..1] ± 1051
     RedemptionPrice <RedPric> [0..1]  1051
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1035 August 2026
```

## File page 1036

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 1051
       Value <Val> [1..1] ± 1052
       PriceType <PricTp> [0..1] CodeSet 1052
     ValueDate <ValDt> [1..1] Date 1053
     ValuePeriod <ValPrd> [1..1]  1053
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1053
Or       ToDateTime <ToDtTm> [1..1] DateTime 1054
Or}       DateTimeRange <DtTmRg> [1..1] ± 1054
     CalculationDate <ClctnDt> [1..1] DateTime 1054
   InterestType <IntrstTp> [0..1] CodeSet 1054
   InstrumentStructureType <InstrmStrTp> [0..1]  1054
{Or     Code <Cd> [1..1] CodeSet 1055
Or}     Proprietary <Prtry> [1..1] ± 1056
   GlobalType <GblTp> [0..1]  1056
{Or     Code <Cd> [1..1] CodeSet 1056
Or}     Proprietary <Prtry> [1..1] ± 1057
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 1057
   Geographics <Geogcs> [0..1] Text 1057
   YieldRange <YldRg> [0..1] ± 1057
   CouponRange <CpnRg> [0..1] ± 1058
   Purpose <Purp> [0..1] Text 1058
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1058
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 1059
   Haircut <Hrcut> [0..1] Rate 1059
   TransactionConditions <TxConds> [0..1] ± 1059
   LookBack <LookBck> [0..1] Quantity 1059
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1059
   MinimumIncrement <MinIncrmt> [0..1] ± 1059
   MinimumQuantity <MinQty> [0..1] ± 1060
   Production <Pdctn> [0..1] Text 1060
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 1060
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1036 August 2026
```

