---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["14 auth.044.001.03 FinancialInstrumentReportingEquityTradingActivityResultV03", "14.4 Message Building Blocks"]
file_pages: [219, 220]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.044.001.03"]
---

# 14.4 Message Building Blocks

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 219 to 220.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 219

```text
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C2 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C3 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C4 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C5 ValidISINRule
ISIN code must pass checksum validation.
C6 ValidMICRule
Market Identification code must be an active market at the time of reporting.
C7 ValidMICRule
Where reported, market Identification code must be an active market for that reporting period.
C8 ValidMICRule
Market Identification code must be an active market at the time of reporting.
14.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
14.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header to provide details on when and from whom the message originates.
ReportHeader <RptHdr> contains the following elements (see "SecuritiesMarketReportHeader1" on
page 411 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ReportingEntity <RptgNtty> [1..1] ± C19 411
   ReportingPeriod <RptgPrd> [1..1] ± 411
   SubmissionDateTime <SubmissnDtTm> [0..1] DateTime 411
14.4.2 EquityTransparencyData <EqtyTrnsprncyData>
Presence: [1..*]
Definition: Details the transparency data reported by a trading venue.
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
219 July 2025
```

## File page 220

```text
Impacted by: C5 "ValidISINRule", C7 "ValidMICRule"
EquityTransparencyData <EqtyTrnsprncyData> contains the following TransparencyDataReport22
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   TechnicalRecordIdentification <TechRcrdId> [0..1] Text 221
   Identification <Id> [1..1] IdentifierSet 221
   FinancialInstrumentClassification <FinInstrmClssfctn> [0..1] CodeSet 221
   FullName <FullNm> [0..1] Text 221
   TradingVenue <TradgVn> [0..1] IdentifierSet 221
   ReportingPeriod <RptgPrd> [0..1] ± 221
   ApplicationPeriod <ApplPrd> [0..1] ± 222
   Liquidity <Lqdty> [0..1] Indicator 222
   Methodology <Mthdlgy> [0..1] CodeSet 222
   Statistics <Sttstcs> [0..1]  223
     AverageDailyTurnover <AvrgDalyTrnvr> [0..1] Amount C1, C3 223
     AverageTransactionValue <AvrgTxVal> [0..1] Amount C1, C3 224
     LargeInScale <LrgInScale> [0..1] Quantity 224
     StandardMarketSize <StdMktSz> [0..1] Quantity 224
     AverageDailyNumberOfTransactions
<AvrgDalyNbOfTxs>
[0..1] Quantity 224
     TotalNumberOfTransactionsExecuted
<TtlNbOfTxsExctd>
[0..1] Quantity 224
     TotalVolumeOfTransactionsExecuted
<TtlVolOfTxsExctd>
[0..1] Quantity 225
     TotalNumberOfTradingDays <TtlNbOfTradgDays> [0..1] Quantity 225
   RelevantMarket <RlvntMkt> [0..1]  C8 225
     Identification <Id> [1..1] IdentifierSet 225
     AverageDailyNumberOfTransactions
<AvrgDalyNbOfTxs>
[0..1] Quantity 225
Constraints
• ValidISINRule
ISIN code must pass checksum validation.
• ValidMICRule
Where reported, market Identification code must be an active market for that reporting period.
Approved by the Securities SEG on 17 July 2025 auth.044.001.03
FinancialInstrumentReportingEquityTradingActivityR
esultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
220 July 2025
```

