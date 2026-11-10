---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["15 auth.045.001.03 FinancialInstrumentReportingNonEquityTradingActivityResultV03", "15.3 Constraints"]
file_pages: [229]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.045.001.03"]
---

# 15.3 Constraints

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 229 to 229.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 229

```text
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
     PostTradeInstrumentSizeSpecificThreshold
<PstTradInstrmSzSpcfcThrshld>
[0..1] ± 242
     Statistics <Sttstcs> [0..1]  242
       TotalNumberOfTransactionsExecuted <TtlNbOfTxsExctd> [1..1] Quantity 242
       TotalVolumeOfTransactionsExecuted <TtlVolOfTxsExctd> [1..1] Quantity 242
   SupplementaryData <SplmtryData> [0..*] ± C4 243
15.3 Constraints
C1 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
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
15.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
15.4.1 ReportHeader <RptHdr>
Presence: [1..1]
Definition: Header information related to the global report.
Approved by the Securities SEG on 17 July 2025 auth.045.001.03
FinancialInstrumentReportingNonEquityTradingActi
vityResultV03
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
229 July 2025
```

