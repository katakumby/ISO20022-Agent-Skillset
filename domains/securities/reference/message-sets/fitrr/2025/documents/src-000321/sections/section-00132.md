---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01"]
file_pages: [166]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.039.001.01"]
---

# 9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 166 to 166.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 166

```text
9 auth.039.001.01
FinancialInstrumentReportingNonWorkingDa
yReportV01
9.1 MessageDefinition Functionality
The FinancialInstrumentReportingNonWorkingDayReport message is sent by the reporting entity to the
competent authority to report on non-working days.
Outline
The FinancialInstrumentReportingNonWorkingDayReportV01 MessageDefinition is composed of 3
MessageBuildingBlocks:
A. ReportHeader
Header information related to the global report.
B. NonWorkingDay
Provides details on the days a venue is not open.
C. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
9.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <FinInstrmRptgNonWorkgDayRpt> [1..1]  
   ReportHeader <RptHdr> [1..1] ± 167
   NonWorkingDay <NonWorkgDay> [1..*]  167
     Identification <Id> [1..1] ± C3 168
     NonWorkingDay <NonWorkgDay> [1..*]  168
       TechnicalRecordIdentification <TechRcrdId> [0..1] Text 168
       Date <Dt> [1..1] Date 168
       Reason <Rsn> [0..1] CodeSet 169
   SupplementaryData <SplmtryData> [0..*] ± C2 169
Approved by the Securities SEG on 17 July 2025 auth.039.001.01
FinancialInstrumentReportingNonWorkingDayRepor
tV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
166 July 2025
```

