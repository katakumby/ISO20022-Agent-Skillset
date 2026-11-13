---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.4 Message Building Blocks"]
file_pages: [59, 60, 61]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
preceding_topic_continuations: [{"constraint_ids": ["C5", "C6", "C7", "C8", "C9", "C10"], "until_heading": "6.4 Message Building Blocks", "scope": "Text before the named heading on this one-based file page.", "file_page": 59, "topic": "6.3 Constraints", "reference_path": "domains/securities/reference/message-sets/fitrr/2025/documents/src-000321/sections/section-00046.md"}]
---

# 6.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 59 to 61.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

<!-- PDF-TOPIC-NAV-START -->
## Topic continuation

On file page 59, C5–C10 before **6.4 Message Building Blocks** continue [6.3 Constraints](section-00046.md). They belong to the preceding Constraints topic; the full source page is retained below without rearranging its text.
<!-- PDF-TOPIC-NAV-END -->

## File page 59

```text
C5 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C6 ValidISINRule
ISIN code must pass checksum validation.
C7 ValidISINRule
ISIN code must pass checksum validation.
C8 ValidISINRule
ISIN code must pass checksum validation.
C9 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C10 ValidMICRule
Where reported, Market Identification code must be an active market for that reporting period.
6.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
6.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header information related to the global report.
ReportHeader <RptHdr> contains the following elements (see "SecuritiesMarketReportHeader1" on
page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
6.4.2 NonEquityTransparencyData
<NonEqtyTrnsprncyData>
Presence: [1..*]
Definition: Details the non-equity transparency qualitative data reported by a trading venue.
Impacted by: C6 "ValidISINRule", C10 "ValidMICRule"
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
59 July 2025
```

## File page 60

```text
NonEquityTransparencyData <NonEqtyTrnsprncyData> contains the following
TransparencyDataReport21 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 62
   Identification <Id> [1..1] IdentifierSet 62
   FullName <FullNm> [0..1] Text 63
   TradingVenue <TradgVn> [0..1] IdentifierSet 63
   ReportingDate <RptgDt> [0..1] Date 63
   MaturityDate <MtrtyDt> [0..1] Date 63
   FinancialInstrumentClassification <FinInstrmClssfctn> [1..1] CodeSet 63
   UnderlyingInstrumentAssetClass
<UndrlygInstrmAsstClss>
[0..1] CodeSet 63
   DerivativeContractType <DerivCtrctTp> [0..1] CodeSet 64
   Bond <Bd> [0..1] ± 64
   EmissionAllowanceType <EmssnAllwncTp> [0..1] CodeSet 64
   Derivative <Deriv> [0..1]  65
{Or     Commodity <Cmmdty> [1..1]  68
       ClassSpecific <ClssSpcfc> [0..1]  68
{Or         Freight <Frght> [1..1]  68
           Size <Sz> [1..1] Text 68
           AverageTimeCharter <AvrgTmChrtr> [1..1] Text 69
Or}         Energy <Nrgy> [1..1]  69
           SettlementLocation <SttlmLctn> [1..1] Text 69
       NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 69
Or     InterestRate <IntrstRate> [1..1]  69
       UnderlyingType <UndrlygTp> [1..1]  70
{Or         SwapRelated <SwpRltd> [1..1] CodeSet 70
Or}         Other <Othr> [1..1] CodeSet 71
       UnderlyingBond <UndrlygBd> [0..1]  71
         Issuer <Issr> [1..1] IdentifierSet 71
         MaturityDate <MtrtyDt> [0..1] Date 71
         IssuanceDate <IssncDt> [0..1] Date 72
       SwaptionNotionalCurrency <SwptnNtnlCcy> [0..1] CodeSet C1 72
       UnderlyingSwapMaturityDate <UndrlygSwpMtrtyDt> [0..1] Date 72
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
60 July 2025
```

## File page 61

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
       InflationIndex <InfltnIndx> [0..1]  C7 72
{Or         ISIN <ISIN> [1..1] IdentifierSet 72
Or}         Name <Nm> [1..1] Text 73
       InterestRateReference <IntrstRateRef> [1..1] ± 73
Or     ForeignExchange <FX> [1..1]  73
       ContractSubType <CtrctSubTp> [1..1] CodeSet 73
Or     Equity <Eqty> [1..1]  73
       UnderlyingType <UndrlygTp> [1..1]  74
{Or         Basket <Bskt> [1..1] CodeSet 74
Or         Index <Indx> [1..1] CodeSet 74
Or         SingleName <SnglNm> [1..1] CodeSet 75
Or}         Other <Othr> [1..1] CodeSet 75
       Parameter <Param> [0..1] CodeSet 75
Or     ContractForDifference <CtrctForDiff> [1..1]  76
       UnderlyingType <UndrlygTp> [1..1] CodeSet 76
       NotionalCurrency1 <NtnlCcy1> [0..1] CodeSet C2 76
       NotionalCurrency2 <NtnlCcy2> [0..1] CodeSet C2 77
Or     Credit <Cdt> [1..1]  77
{Or       SingleNameCreditDefaultSwap
<SnglNmCdtDfltSwp>
[1..1] ± 78
Or       CreditDefaultSwapIndex <CdtDfltSwpIndx> [1..1]  79
         UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 79
         UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 79
         Series <Srs> [0..1] Quantity 79
         Version <Vrsn> [0..1] Quantity 79
         RollMonth <RollMnth> [0..12] Quantity 80
         NextRollDate <NxtRollDt> [0..1] Date 80
         NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 80
Or       SingleNameCreditDefaultSwapDerivative
<SnglNmCdtDfltSwpDeriv>
[1..1]  C8 80
         UnderlyingCreditDefaultSwapIdentification
<UndrlygCdtDfltSwpId>
[0..1] IdentifierSet 81
         ObligationIdentification <OblgtnId> [1..1] IdentifierSet 81
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
61 July 2025
```

