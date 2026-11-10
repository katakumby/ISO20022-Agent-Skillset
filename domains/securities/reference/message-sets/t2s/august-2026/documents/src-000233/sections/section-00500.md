---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["27 reda.006.001.01 SecurityCreationRequestV01", "27.4 Message Building Blocks", "27.4.2 Security <Scty>", "27.4.2.2 FinancialInstrumentType <FinInstrmTp>"]
file_pages: [654, 655, 656, 657, 658, 659, 660, 661]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.006.001.01"]
---

# 27.4.2.2 FinancialInstrumentType <FinInstrmTp>

Source: [src-000233](../../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDRPart2_Target2Securities_August_2026_v1.pdf). Locator: one-based file pages 654 to 661.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 654

```text
• DescriptionUsageRule
Description must be used alone as the last resort.
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
27.4.2.2  FinancialInstrumentType <FinInstrmTp>
Presence: [0..*]
Definition: Provides additional details about the financial instrument.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 654 August 2026
```

## File page 655

```text
FinancialInstrumentType <FinInstrmTp> contains the following FinancialInstrument97 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Equity <Eqty> [0..1]  662
     PreferenceToIncome <PrefToIncm> [1..1]  663
{Or       Code <Cd> [1..1] CodeSet 663
Or}       Proprietary <Prtry> [1..1] ± 663
     MaturityDate <MtrtyDt> [0..1] DateTime 664
     NonPaidAmount <NonPdAmt> [0..1] Amount C1, C5 664
     ParValue <ParVal> [0..1] Amount C1, C5 664
     VotingRightsPerShare <VtngRghtsPerShr> [0..1] Quantity 665
   Warrant <Warrt> [0..1]  665
     Multiplier <Mltplr> [0..1] Rate 666
     SubscriptionPrice <SbcptPric> [0..1]  666
       ValueType <ValTp> [0..1] CodeSet 667
       Value <Val> [1..1] ± 667
       PriceType <PricTp> [0..1] CodeSet 668
     Type <Tp> [0..1]  668
{Or       Code <Cd> [1..1] CodeSet 669
Or}       Proprietary <Prtry> [1..1] ± 669
     WarrantAgent <WarrtAgt> [0..*]  669
       Name <Nm> [1..1] Text 670
       Identification <Id> [0..1]  670
{Or         AnyBIC <AnyBIC> [1..1] IdentifierSet C3 670
Or}         ProprietaryIdentification <PrtryId> [1..1] ± 671
       Purpose <Purp> [0..1] Text 671
       TaxationCountry <TaxtnCtry> [0..1] CodeSet C4 671
       RegistrationCountry <RegnCtry> [0..1] CodeSet C4 671
       RegistrationDate <RegnDt> [0..1] Date 672
       TaxIdentificationNumber <TaxIdNb> [0..1] Text 672
       NationalRegistrationNumber <NtlRegnNb> [0..1] Text 672
       PostalAddress <PstlAdr> [1..5] ± C10 672
       PrimaryCommunicationAddress <PmryComAdr> [0..1] ± 672
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 655 August 2026
```

## File page 656

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       SecondaryCommunicationAddress
<ScndryComAdr>
[0..1] ± 673
   Debt <Debt> [0..1]  C11,
C13
673
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
{Or       FromDateTime <FrDtTm> [1..1] DateTime 682
Or       ToDateTime <ToDtTm> [1..1] DateTime 682
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 656 August 2026
```

## File page 657

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}       DateTimeRange <DtTmRg> [1..1] ± 682
     VariableRateIndicator <VarblRateInd> [0..1] Indicator 682
     OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 683
     OverAllotmentRate <OverAlltmtRate> [0..1] Rate 683
     AmortisableIndicator <AmtsblInd> [0..1] Indicator 683
     InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 683
     CapitalisedInterest <CptlsdIntrst> [0..1]  683
{Or       Code <Cd> [1..1] CodeSet 684
Or}       Proprietary <Prtry> [1..1] ± 684
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
{Or         Code <Cd> [1..1] CodeSet 688
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 657 August 2026
```

## File page 658

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}         Proprietary <Prtry> [1..1] ± 691
       RedemptionPrice <RedPric> [0..1]  691
         ValueType <ValTp> [0..1] CodeSet 691
         Value <Val> [1..1] ± 692
         PriceType <PricTp> [0..1] CodeSet 692
       ValueDate <ValDt> [1..1] Date 693
       ValuePeriod <ValPrd> [1..1]  693
{Or         FromDateTime <FrDtTm> [1..1] DateTime 693
Or         ToDateTime <ToDtTm> [1..1] DateTime 694
Or}         DateTimeRange <DtTmRg> [1..1] ± 694
       CalculationDate <ClctnDt> [1..1] DateTime 694
     InterestType <IntrstTp> [0..1] CodeSet 694
     InstrumentStructureType <InstrmStrTp> [0..1]  694
{Or       Code <Cd> [1..1] CodeSet 695
Or}       Proprietary <Prtry> [1..1] ± 696
     GlobalType <GblTp> [0..1]  696
{Or       Code <Cd> [1..1] CodeSet 696
Or}       Proprietary <Prtry> [1..1] ± 697
     PotentialEuroSystemEligibility
<PotntlEuroSysElgblty>
[0..1] Indicator 697
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 658 August 2026
```

## File page 659

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
     Production <Pdctn> [0..1] Text 700
     RestrictedIndicator <RstrctdInd> [0..1] Indicator 700
     PriceFrequency <PricFrqcy> [0..1] ± 700
     Sector <Sctr> [0..1] Text 701
     SubstitutionFrequency <SbstitnFrqcy> [0..1] ± 701
     SubstitutionLeft <SbstitnLft> [0..1] Quantity 701
     WholePoolIndicator <WhlPoolInd> [0..1] Indicator 701
     PriceSource <PricSrc> [0..1] Text 701
     PriceRange <PricRg> [0..1] ± 702
   Derivative <Deriv> [0..1]  702
     Future <Futr> [0..1]  706
       ContractSize <CtrctSz> [0..1] Rate 708
       ExercisePrice <ExrcPric> [0..1]  708
         ValueType <ValTp> [0..1] CodeSet 708
         Value <Val> [1..1] ± 709
         PriceType <PricTp> [0..1] CodeSet 709
       FutureDate <FutrDt> [0..1] DateTime 710
       MinimumSize <MinSz> [0..1] Amount C1, C5 710
       UnitOfMeasure <UnitOfMeasr> [0..1]  711
{Or         Code <Cd> [1..1] CodeSet 711
Or}         Proprietary <Prtry> [1..1] ± 713
       TimeUnit <TmUnit> [0..1]  713
{Or         Code <Cd> [1..1] CodeSet 714
Or}         Proprietary <Prtry> [1..1] ± 714
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  714
         AllocationPercentage <AllcnPctg> [0..1] Rate 716
         Quantity <Qty> [0..1]  716
{Or           Unit <Unit> [1..1] Quantity 716
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 716
         SettlementType <SttlmTp> [0..1]  716
{Or           Code <Cd> [1..1] CodeSet 717
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 659 August 2026
```

## File page 660

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or}           Proprietary <Prtry> [1..1] ± 717
         CashAmount <CshAmt> [0..1] Amount C1, C5 717
         CashType <CshTp> [0..1] Text 718
         Price <Pric> [0..1]  718
           ValueType <ValTp> [0..1] CodeSet 718
           Value <Val> [1..1] ± 719
           PriceType <PricTp> [0..1] CodeSet 719
         DirtyPrice <DrtyPric> [0..1]  720
           ValueType <ValTp> [0..1] CodeSet 720
           Value <Val> [1..1] ± 721
           PriceType <PricTp> [0..1] CodeSet 721
         EndPrice <EndPric> [0..1]  722
           ValueType <ValTp> [0..1] CodeSet 722
           Value <Val> [1..1] ± 723
           PriceType <PricTp> [0..1] CodeSet 723
         StartValue <StartVal> [0..1] Amount C1, C5 724
         CurrentValue <CurVal> [0..1] Amount C1, C5 724
         EndValue <EndVal> [0..1] Amount C1, C5 725
         AdjustedQuantity <AdjstdQty> [0..1]  725
{Or           Unit <Unit> [1..1] Quantity 725
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 726
         ExchangeRate <XchgRate> [0..1] Rate 726
         CapValue <CapVal> [0..1] Amount C1, C5 726
     Option <Optn> [0..1]  726
       OptionSettlementStyle <OptnSttlmStyle> [0..1]  730
{Or         Code <Cd> [0..*] CodeSet 730
Or}         Proprietary <Prtry> [1..1] ± 730
       ConversionDate <ConvsDt> [0..1] DateTime 730
       StrikePrice <StrkPric> [0..1]  730
         ValueType <ValTp> [0..1] CodeSet 731
         Value <Val> [1..1] ± 731
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 660 August 2026
```

## File page 661

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
         PriceType <PricTp> [0..1] CodeSet 732
       MinimumExercisableQuantity <MinExrcblQty> [0..1] ± 732
       ConversionPeriod <ConvsPrd> [0..1]  733
{Or         FromDateTime <FrDtTm> [1..1] DateTime 733
Or         ToDateTime <ToDtTm> [1..1] DateTime 733
Or}         DateTimeRange <DtTmRg> [1..1] ± 733
       OptionStyle <OptnStyle> [0..1]  734
{Or         Code <Cd> [1..1] CodeSet 734
Or}         Proprietary <Prtry> [1..1] ± 734
       OptionType <OptnTp> [0..1] ± 734
       StrikeValue <StrkVal> [0..1] Quantity 735
       StrikeMultiplier <StrkMltplr> [0..1] Quantity 735
       InstrumentAssignmentMethod <InstrmAssgnmtMtd> [0..1]  735
{Or         Code <Cd> [1..1] CodeSet 735
Or}         Proprietary <Prtry> [1..1] ± 735
       VersionNumber <VrsnNb> [0..1] Quantity 736
       ExpiryLocation <XpryLctn> [0..1] Text 736
       Standardisation <Stdstn> [0..1]  736
{Or         Code <Cd> [1..*] CodeSet 736
Or}         Proprietary <Prtry> [1..1] ± 737
       TradingPartyRole <TradgPtyRole> [0..1]  737
{Or         Code <Cd> [1..*] CodeSet 737
Or}         Proprietary <Prtry> [1..1] ± 737
       ContractSize <CtrctSz> [0..1] Rate 738
       AdditionalUnderlyingAttributes
<AddtlUndrlygAttrbts>
[0..*]  738
         AllocationPercentage <AllcnPctg> [0..1] Rate 740
         Quantity <Qty> [0..1]  740
{Or           Unit <Unit> [1..1] Quantity 740
Or}           FaceAmount <FaceAmt> [1..1] Amount C1, C5 740
         SettlementType <SttlmTp> [0..1]  740
{Or           Code <Cd> [1..1] CodeSet 741
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.006.001.01 SecurityCreationRequestV01
Target2-Securities 661 August 2026
```

