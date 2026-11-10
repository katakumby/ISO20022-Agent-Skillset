---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["28 reda.007.001.01 SecurityMaintenanceRequestV01", "28.4 Message Building Blocks", "28.4.2 UpdateType <UpdTp>", "28.4.2.2 Replace <Rplc>", "28.4.2.2.1 FinancialInstrumentType <FinInstrmTp>", "28.4.2.2.1.2 Warrant <Warrt>", "28.4.2.2.1.2.4 WarrantAgent <WarrtAgt>", "28.4.2.2.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [1597, 1598, 1599, 1600]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.007.001.01"]
---

# 28.4.2.2.1.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 1597 to 1600.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1597

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
28.4.2.2.1.2.4.11  SecondaryCommunicationAddress <ScndryComAdr>
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
28.4.2.2.1.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1597 August 2026
```

## File page 1598

```text
Debt <Debt> contains the following Debt5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1601
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 1601
   PaymentFrequency <PmtFrqcy> [0..1] ± 1602
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1602
   DatedDate <DtdDt> [0..1] DateTime 1602
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1602
   MaturityDate <MtrtyDt> [0..1] DateTime 1602
   NextCouponDate <NxtCpnDt> [0..1] DateTime 1602
   PutableDate <PutblDt> [0..1] DateTime 1603
   NextCallableDate <NxtCllblDt> [0..1] DateTime 1603
   NextFactorDate <NxtFctrDt> [0..1] DateTime 1603
   ExpirationDate <XprtnDt> [0..1] DateTime 1603
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1603
   InterestRate <IntrstRate> [0..1] Rate 1603
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1603
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 1603
   CallableIndicator <CllblInd> [0..1] Indicator 1604
   CPProgram <CPPrgm> [0..1] Quantity 1604
   CPRegistrationType <CPRegnTp> [0..1] Text 1604
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1604
   PutableIndicator <PutblInd> [0..1] Indicator 1604
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 1605
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 1605
   PerpetualIndicator <PerptlInd> [0..1] Indicator 1605
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1605
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 1605
   ExtendiblePeriod <XtndblPrd> [0..1]  1606
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1606
Or     ToDateTime <ToDtTm> [1..1] DateTime 1606
Or}     DateTimeRange <DtTmRg> [1..1] ± 1606
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1606
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1598 August 2026
```

## File page 1599

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1607
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1607
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 1607
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1607
   CapitalisedInterest <CptlsdIntrst> [0..1]  1607
{Or     Code <Cd> [1..1] CodeSet 1608
Or}     Proprietary <Prtry> [1..1] ± 1608
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1608
   CurrentFactor <CurFctr> [0..1] Rate 1609
   NextFactor <NxtFctr> [0..1] Rate 1609
   PreviousFactor <PrvsFctr> [0..1] Rate 1609
   Pieces <Pcs> [0..1] Quantity 1609
   PoolsMaximum <PlsMax> [0..1] Quantity 1609
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 1609
   PoolsPerLot <PlsPerLot> [0..1] Quantity 1609
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1610
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1610
   LotIdentification <LotId> [0..1] Text 1610
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1610
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1610
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1610
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1610
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1611
   InsuredIndicator <InsrdInd> [0..1] Indicator 1611
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1611
   YieldCalculation <YldClctn> [0..*]  1611
     Value <Val> [1..1] Rate 1612
     CalculationType <ClctnTp> [0..1]  1612
{Or       Code <Cd> [1..1] CodeSet 1612
Or}       Proprietary <Prtry> [1..1] ± 1615
     RedemptionPrice <RedPric> [0..1]  1615
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1599 August 2026
```

## File page 1600

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 1615
       Value <Val> [1..1] ± 1616
       PriceType <PricTp> [0..1] CodeSet 1616
     ValueDate <ValDt> [1..1] Date 1617
     ValuePeriod <ValPrd> [1..1]  1617
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1617
Or       ToDateTime <ToDtTm> [1..1] DateTime 1618
Or}       DateTimeRange <DtTmRg> [1..1] ± 1618
     CalculationDate <ClctnDt> [1..1] DateTime 1618
   InterestType <IntrstTp> [0..1] CodeSet 1618
   InstrumentStructureType <InstrmStrTp> [0..1]  1618
{Or     Code <Cd> [1..1] CodeSet 1619
Or}     Proprietary <Prtry> [1..1] ± 1620
   GlobalType <GblTp> [0..1]  1620
{Or     Code <Cd> [1..1] CodeSet 1620
Or}     Proprietary <Prtry> [1..1] ± 1621
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 1621
   Geographics <Geogcs> [0..1] Text 1621
   YieldRange <YldRg> [0..1] ± 1621
   CouponRange <CpnRg> [0..1] ± 1622
   Purpose <Purp> [0..1] Text 1622
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1622
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 1623
   Haircut <Hrcut> [0..1] Rate 1623
   TransactionConditions <TxConds> [0..1] ± 1623
   LookBack <LookBck> [0..1] Quantity 1623
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1623
   MinimumIncrement <MinIncrmt> [0..1] ± 1623
   MinimumQuantity <MinQty> [0..1] ± 1624
   Production <Pdctn> [0..1] Text 1624
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 1624
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.007.001.01 SecurityMaintenanceRequestV01
Target2-Securities 1600 August 2026
```

