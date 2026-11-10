---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["6 auth.033.001.03 FinancialInstrumentReportingNonEquityTransparencyDataReportV03", "6.2 Structure"]
file_pages: [56, 57]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.033.001.03"]
---

# 6.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 56 to 57.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 56

```text
6.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document>
<FinInstrmRptgNonEqtyTrnsprncyDataRpt>
[1..1]  
   ReportHeader <RptHdr> [1..1] ± 59
   NonEquityTransparencyData <NonEqtyTrnsprncyData> [1..*]  C6, C10 59
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 62
     Identification <Id> [1..1] IdentifierSet 62
     FullName <FullNm> [0..1] Text 63
     TradingVenue <TradgVn> [0..1] IdentifierSet 63
     ReportingDate <RptgDt> [0..1] Date 63
     MaturityDate <MtrtyDt> [0..1] Date 63
     FinancialInstrumentClassification <FinInstrmClssfctn> [1..1] CodeSet 63
     UnderlyingInstrumentAssetClass <UndrlygInstrmAsstClss> [0..1] CodeSet 63
     DerivativeContractType <DerivCtrctTp> [0..1] CodeSet 64
     Bond <Bd> [0..1] ± 64
     EmissionAllowanceType <EmssnAllwncTp> [0..1] CodeSet 64
     Derivative <Deriv> [0..1]  65
{Or       Commodity <Cmmdty> [1..1]  68
         ClassSpecific <ClssSpcfc> [0..1]  68
{Or           Freight <Frght> [1..1]  68
             Size <Sz> [1..1] Text 68
             AverageTimeCharter <AvrgTmChrtr> [1..1] Text 69
Or}           Energy <Nrgy> [1..1]  69
             SettlementLocation <SttlmLctn> [1..1] Text 69
         NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 69
Or       InterestRate <IntrstRate> [1..1]  69
         UnderlyingType <UndrlygTp> [1..1]  70
{Or           SwapRelated <SwpRltd> [1..1] CodeSet 70
Or}           Other <Othr> [1..1] CodeSet 71
         UnderlyingBond <UndrlygBd> [0..1]  71
           Issuer <Issr> [1..1] IdentifierSet 71
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
56 July 2025
```

## File page 57

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
           MaturityDate <MtrtyDt> [0..1] Date 71
           IssuanceDate <IssncDt> [0..1] Date 72
         SwaptionNotionalCurrency <SwptnNtnlCcy> [0..1] CodeSet C1 72
         UnderlyingSwapMaturityDate <UndrlygSwpMtrtyDt> [0..1] Date 72
         InflationIndex <InfltnIndx> [0..1]  C7 72
{Or           ISIN <ISIN> [1..1] IdentifierSet 72
Or}           Name <Nm> [1..1] Text 73
         InterestRateReference <IntrstRateRef> [1..1] ± 73
Or       ForeignExchange <FX> [1..1]  73
         ContractSubType <CtrctSubTp> [1..1] CodeSet 73
Or       Equity <Eqty> [1..1]  73
         UnderlyingType <UndrlygTp> [1..1]  74
{Or           Basket <Bskt> [1..1] CodeSet 74
Or           Index <Indx> [1..1] CodeSet 74
Or           SingleName <SnglNm> [1..1] CodeSet 75
Or}           Other <Othr> [1..1] CodeSet 75
         Parameter <Param> [0..1] CodeSet 75
Or       ContractForDifference <CtrctForDiff> [1..1]  76
         UnderlyingType <UndrlygTp> [1..1] CodeSet 76
         NotionalCurrency1 <NtnlCcy1> [0..1] CodeSet C2 76
         NotionalCurrency2 <NtnlCcy2> [0..1] CodeSet C2 77
Or       Credit <Cdt> [1..1]  77
{Or         SingleNameCreditDefaultSwap <SnglNmCdtDfltSwp> [1..1] ± 78
Or         CreditDefaultSwapIndex <CdtDfltSwpIndx> [1..1]  79
           UnderlyingIndexIdentification <UndrlygIndxId> [0..1] IdentifierSet 79
           UnderlyingIndexName <UndrlygIndxNm> [0..1] Text 79
           Series <Srs> [0..1] Quantity 79
           Version <Vrsn> [0..1] Quantity 79
           RollMonth <RollMnth> [0..12] Quantity 80
           NextRollDate <NxtRollDt> [0..1] Date 80
           NotionalCurrency <NtnlCcy> [1..1] CodeSet C2 80
Approved by the Securities SEG on 17 July 2025 auth.033.001.03
FinancialInstrumentReportingNonEquityTransparen
cyDataReportV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
57 July 2025
```

