---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["32 reda.012.001.01 SecurityReportV01", "32.4 Message Building Blocks", "32.4.3 SecurityReportOrError <SctyRptOrErr>", "32.4.3.1 SecurityReportOrBusinessError <SctyRptOrBizErr>", "32.4.3.1.1 SecurityReport <SctyRpt>", "32.4.3.1.1.2 FinancialInstrumentType <FinInstrmTp>", "32.4.3.1.1.2.2 Warrant <Warrt>", "32.4.3.1.1.2.2.4 WarrantAgent <WarrtAgt>", "32.4.3.1.1.2.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>"]
file_pages: [1875, 1876, 1877, 1878]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.012.001.01"]
---

# 32.4.3.1.1.2.2.4.11 SecondaryCommunicationAddress <ScndryComAdr>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 1875 to 1878.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1875

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
32.4.3.1.1.2.2.4.11  SecondaryCommunicationAddress <ScndryComAdr>
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
32.4.3.1.1.2.3  Debt <Debt>
Presence: [0..1]
Definition: Financial instruments evidencing moneys owed by the issuer to the holder on terms as
specified.
Impacted by: C11 "NextCallableDateAndCallableIndicatorRule", C13
"PutableDateAndPutableIndicatorRule"
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1875 August 2026
```

## File page 1876

```text
Debt <Debt> contains the following Debt5 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PaymentCurrency <PmtCcy> [0..1] CodeSet C1 1879
   FaceAmount <FaceAmt> [0..1] Amount C1, C5 1879
   PaymentFrequency <PmtFrqcy> [0..1] ± 1880
   InterestFixingDate <IntrstFxgDt> [0..1] DateTime 1880
   DatedDate <DtdDt> [0..1] DateTime 1880
   FirstPaymentDate <FrstPmtDt> [0..1] DateTime 1880
   MaturityDate <MtrtyDt> [0..1] DateTime 1880
   NextCouponDate <NxtCpnDt> [0..1] DateTime 1880
   PutableDate <PutblDt> [0..1] DateTime 1881
   NextCallableDate <NxtCllblDt> [0..1] DateTime 1881
   NextFactorDate <NxtFctrDt> [0..1] DateTime 1881
   ExpirationDate <XprtnDt> [0..1] DateTime 1881
   PaymentDirectionIndicator <PmtDrctnInd> [0..1] Indicator 1881
   InterestRate <IntrstRate> [0..1] Rate 1881
   NextInterestRate <NxtIntrstRate> [0..1] Rate 1881
   OddCouponIndicator <OddCpnInd> [0..1] Indicator 1881
   CallableIndicator <CllblInd> [0..1] Indicator 1882
   CPProgram <CPPrgm> [0..1] Quantity 1882
   CPRegistrationType <CPRegnTp> [0..1] Text 1882
   InterestAccrualDate <IntrstAcrlDt> [0..1] DateTime 1882
   PutableIndicator <PutblInd> [0..1] Indicator 1882
   PreFundedIndicator <PreFnddInd> [0..1] Indicator 1883
   EscrowedIndicator <EscrwdInd> [0..1] Indicator 1883
   PerpetualIndicator <PerptlInd> [0..1] Indicator 1883
   SubordinatedIndicator <SubrdntdInd> [0..1] Indicator 1883
   ExtendibleIndicator <XtndblInd> [0..1] Indicator 1883
   ExtendiblePeriod <XtndblPrd> [0..1]  1884
{Or     FromDateTime <FrDtTm> [1..1] DateTime 1884
Or     ToDateTime <ToDtTm> [1..1] DateTime 1884
Or}     DateTimeRange <DtTmRg> [1..1] ± 1884
   VariableRateIndicator <VarblRateInd> [0..1] Indicator 1884
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1876 August 2026
```

## File page 1877

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OverAllotmentAmount <OverAlltmtAmt> [0..1] Amount C1, C5 1885
   OverAllotmentRate <OverAlltmtRate> [0..1] Rate 1885
   AmortisableIndicator <AmtsblInd> [0..1] Indicator 1885
   InterestCalculationMethod <IntrstClctnMtd> [0..1] Text 1885
   CapitalisedInterest <CptlsdIntrst> [0..1]  1885
{Or     Code <Cd> [1..1] CodeSet 1886
Or}     Proprietary <Prtry> [1..1] ± 1886
   ActualDenominationAmount <ActlDnmtnAmt> [0..*] Amount C1, C5 1886
   CurrentFactor <CurFctr> [0..1] Rate 1887
   NextFactor <NxtFctr> [0..1] Rate 1887
   PreviousFactor <PrvsFctr> [0..1] Rate 1887
   Pieces <Pcs> [0..1] Quantity 1887
   PoolsMaximum <PlsMax> [0..1] Quantity 1887
   PoolsPerMillion <PlsPerMln> [0..1] Quantity 1887
   PoolsPerLot <PlsPerLot> [0..1] Quantity 1887
   PoolsPerTrade <PlsPerTrad> [0..1] Quantity 1888
   ConstantPrePaymentPenaltyIndicator
<CstPrePmtPnltyInd>
[0..1] Indicator 1888
   LotIdentification <LotId> [0..1] Text 1888
   ConstantPrePaymentYield <CstPrePmtYld> [0..1] Rate 1888
   WeightedAverageCoupon <WghtdAvrgCpn> [0..1] Rate 1888
   WeightedAverageLife <WghtdAvrgLife> [0..1] Quantity 1888
   WeightedAverageLoan <WghtdAvrgLn> [0..1] Quantity 1888
   WeightedAverageMaturity <WghtdAvrgMtrty> [0..1] Quantity 1889
   InsuredIndicator <InsrdInd> [0..1] Indicator 1889
   BankQualifiedIndicator <BkQlfdInd> [0..1] Indicator 1889
   YieldCalculation <YldClctn> [0..*]  1889
     Value <Val> [1..1] Rate 1890
     CalculationType <ClctnTp> [0..1]  1890
{Or       Code <Cd> [1..1] CodeSet 1890
Or}       Proprietary <Prtry> [1..1] ± 1893
     RedemptionPrice <RedPric> [0..1]  1893
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1877 August 2026
```

## File page 1878

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       ValueType <ValTp> [0..1] CodeSet 1893
       Value <Val> [1..1] ± 1894
       PriceType <PricTp> [0..1] CodeSet 1894
     ValueDate <ValDt> [1..1] Date 1895
     ValuePeriod <ValPrd> [1..1]  1895
{Or       FromDateTime <FrDtTm> [1..1] DateTime 1895
Or       ToDateTime <ToDtTm> [1..1] DateTime 1896
Or}       DateTimeRange <DtTmRg> [1..1] ± 1896
     CalculationDate <ClctnDt> [1..1] DateTime 1896
   InterestType <IntrstTp> [0..1] CodeSet 1896
   InstrumentStructureType <InstrmStrTp> [0..1]  1896
{Or     Code <Cd> [1..1] CodeSet 1897
Or}     Proprietary <Prtry> [1..1] ± 1898
   GlobalType <GblTp> [0..1]  1898
{Or     Code <Cd> [1..1] CodeSet 1898
Or}     Proprietary <Prtry> [1..1] ± 1899
   PotentialEuroSystemEligibility <PotntlEuroSysElgblty> [0..1] Indicator 1899
   Geographics <Geogcs> [0..1] Text 1899
   YieldRange <YldRg> [0..1] ± 1899
   CouponRange <CpnRg> [0..1] ± 1900
   Purpose <Purp> [0..1] Text 1900
   AlternativeMinimumTaxIndicator <AltrntvMinTaxInd> [0..1] Indicator 1900
   AutoReinvestment <AutoRinvstmt> [0..1] Rate 1901
   Haircut <Hrcut> [0..1] Rate 1901
   TransactionConditions <TxConds> [0..1] ± 1901
   LookBack <LookBck> [0..1] Quantity 1901
   MaximumSubstitution <MaxSbstitn> [0..1] Quantity 1901
   MinimumIncrement <MinIncrmt> [0..1] ± 1901
   MinimumQuantity <MinQty> [0..1] ± 1902
   Production <Pdctn> [0..1] Text 1902
   RestrictedIndicator <RstrctdInd> [0..1] Indicator 1902
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.012.001.01 SecurityReportV01
Target2-Securities 1878 August 2026
```

