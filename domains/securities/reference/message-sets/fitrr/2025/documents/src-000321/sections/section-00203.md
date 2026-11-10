---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01"]
file_pages: [247]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.048.001.01"]
---

# 17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 247 to 247.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 247

```text
17 auth.048.001.01
FinancialInstrumentReportingCurrencyCode
ReportV01
17.1 MessageDefinition Functionality
The MiFIRCurrencyCodeReport message provides the details the ISO 4217 currency codes and is
created by ESMA for distribution to National Competent Authorities.
Outline
The FinancialInstrumentReportingCurrencyCodeReportV01 MessageDefinition is composed of 2
MessageBuildingBlocks:
A. CurrencyData
Report all currencies and countries which use that currency.
B. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
17.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgCcyCdRpt> [1..1]  
   CurrencyData <CcyData> [1..*]  248
     Currency <Ccy> [1..1]  248
       Code <Cd> [1..1] CodeSet C1 249
       Name <Nm> [1..1] Text 249
     FractionalDigit <FrctnlDgt> [0..1] Quantity 249
     CountryDetails <CtryDtls> [1..1] ± 249
     PreEuro <PreEuro> [1..1] Indicator 249
     Modification <Mod> [0..1] CodeSet 250
     ValidityPeriod <VldtyPrd> [1..1] ± 250
     LastUpdated <LastUpdtd> [0..1] Date 250
   SupplementaryData <SplmtryData> [0..*] ± C3 250
Approved by the Securities SEG on 17 July 2025 auth.048.001.01
FinancialInstrumentReportingCurrencyCodeReportV
01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
247 July 2025
```

