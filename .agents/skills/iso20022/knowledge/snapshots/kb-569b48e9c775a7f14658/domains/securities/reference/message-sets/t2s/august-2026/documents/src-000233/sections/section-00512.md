---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>", "27.4.2.2.2 Warrant <Warrt>", "27.4.2.2.2.4 WarrantAgent <WarrtAgt>", "27.4.2.2.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [673, 674, 675, 676]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 673 to 676.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 673

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
27.4.2.2.2.4.11  SecondaryCommunicationAddress <ScndryComAdr>
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
27.4.2.2.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 673 August 2026
```

## File page 674

```text
Debt <Debt> contains the following Debt5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 677
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 677
   PaymentFrequency <PmtFrqcy> [0..1] ± 678
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 678
   DatedDate <DtdDt> [0..1] DateTime 678
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 678
   MaturityDate <MtrtyDt> [0..1] DateTime 678
   NextCouponDate <NxtCpnDt> [0..1] DateTime 678
   PutableDate <PutblDt> [0..1] DateTime 679
   NextCallableDate <NxtCllblDt> [0..1] DateTime 679
   NextFactorDate <NxtFctrDt> [0..1] DateTime 679
   ExpirationDate <XprtnDt> [0..1] DateTime 679
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 679
   InterestRate <IntrstRate> [0..1] Rate 679
   NextInterestRate <NxtIntrstRate> [0..1] Rate 679
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 679
   CallableIndicator <CllblInd> [0..1] Indicator 680
   CPProgram <CPPrgm> [0..1] Quantity 680
   CPRegistrationType <CPRegnTp> [0..1] Text 680
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 680
   PutableIndicator <PutblInd> [0..1] Indicator 680
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 681
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 681
   PerpetualIndicator <PerptlInd> [0..1] Indicator 681
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 681
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 681
   ExtendiblePeriod <XtndblPrd> [0..1]  682
{Or     FromDateTime <FrDtTm> [1..1] DateTime 682
Or     ToDateTime <ToDtTm> [1..1] DateTime 682
Or}     DateTimeRange <DtTmRg> [1..1] ± 682
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 682
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 674 August 2026
```

## File page 675

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 683
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 683
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 683
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 683
   CapitalisedInterest <CptlsdIntrst> [0..1]  683
{Or     Code <Cd> [1..1] CodeSet 684
Or}     Proprietary <Prtry> [1..1] ± 684
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 684
   CurrentFactor <CurFctr> [0..1] Rate 685
   NextFactor <NxtFctr> [0..1] Rate 685
   PreviousFactor <PrvsFctr> [0..1] Rate 685
   Pieces <Pcs> [0..1] Quantity 685
   PoolsMaximum <PlsMax> [0..1] Quantity 685
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 685
   PoolsPerLot <PlsPerLot> [0..1] Quantity 685
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 686
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 686
   LotIdentification <LotId> [0..1] Text 686
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 686
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 686
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 686
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 686
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 687
   InsuredIndicator <InsrdInd> [0..1] Indicator 687
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 687
   YieldCalculation <YldClctn> [0..*]  687
     Value <Val> [1..1] Rate 688
     CalculationType <ClctnTp> [0..1]  688
{Or       Code <Cd> [1..1] CodeSet 688
Or}       Proprietary <Prtry> [1..1] ± 691
     RedemptionPrice <RedPric> [0..1]  691
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 675 August 2026
```

## File page 676

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 691
       Value <Val> [1..1] ± 692
       PriceType <PricTp> [0..1] CodeSet 692
     ValueDate <ValDt> [1..1] Date 693
     ValuePeriod <ValPrd> [1..1]  693
{Or       FromDateTime <FrDtTm> [1..1] DateTime 693
Or       ToDateTime <ToDtTm> [1..1] DateTime 694
Or}       DateTimeRange <DtTmRg> [1..1] ± 694
     CalculationDate <ClctnDt> [1..1] DateTime 694
   InterestType <IntrstTp> [0..1] CodeSet 694
   InstrumentStructureType <InstrmStrTp> [0..1]  694
{Or     Code <Cd> [1..1] CodeSet 695
Or}     Proprietary <Prtry> [1..1] ± 696
   GlobalType <GblTp> [0..1]  696
{Or     Code <Cd> [1..1] CodeSet 696
Or}     Proprietary <Prtry> [1..1] ± 697
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 697
   Geographics <Geogcs> [0..1] Text 697
   YieldRange <YldRg> [0..1] ± 697
   CouponRange <CpnRg> [0..1] ± 698
   Purpose <Purp> [0..1] Text 698
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 698
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 699
   Haircut <Hrcut> [0..1] Rate 699
   TransactionConditions <TxConds> [0..1] ± 699
   LookBack <LookBck> [0..1] Quantity 699
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 699
   MinimumIncrement <MinIncrmt> [0..1] ± 699
   MinimumQuantity <MinQty> [0..1] ± 700
   Production <Pdctn> [0..1] Text 700
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 700
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 676 August 2026
```

