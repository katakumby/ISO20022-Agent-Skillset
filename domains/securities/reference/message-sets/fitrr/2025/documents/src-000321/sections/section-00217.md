---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["20 auth.053.001.01 FinancialInstrumentReportingTradingVolumeCapResultReportV01", "20.2 Structure"]
file_pages: [263]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.053.001.01"]
---

# 20.2 Structure

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 263 to 263.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 263

```text
20.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgTradgVolCapRsltRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 264
   VolumeCapResult <VolCapRslt> [1..*]  264
     Identification <Id> [1..1] IdentifierSet 264
     ReportingPeriod <RptgPrd> [1..1] ± 265
     LastUpdateDate <LastUpdDt> [0..1] Date 265
     TotalTradingVolume <TtlTradgVol> [1..1] Amount C1, C3 265
     TradingUnderWaiverPercentage <TradgUdrWvrPctg> [1..1] Rate 265
     TradingUnderWaiverBreakdown <TradgUdrWvrBrkdwn> [0..*]  265
       TradingUnderWaiverPercentage <TradgUdrWvrPctg> [1..1] Rate 266
       TradingVenue <TradgVn> [1..1] IdentifierSet 266
       Disclaimer <Dsclmr> [0..1] Text 266
     Disclaimer <Dsclmr> [0..1] Text 266
   SupplementaryData <SplmtryData> [0..*] ± C4 266
20.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
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
C5 ValidMICRule
Market Identification code must be an active market at the time of reporting.
Approved by the Securities SEG on 17 July 2025 auth.053.001.01
FinancialInstrumentReportingTradingVolumeCapRe
sultReportV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
263 July 2025
```

