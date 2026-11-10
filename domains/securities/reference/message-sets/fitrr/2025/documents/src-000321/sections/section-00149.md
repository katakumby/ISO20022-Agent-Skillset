---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
12 auth.042.001.02
FinancialInstrumentReportingInvalidReferenc
eDataReportV02
12.1 MessageDefinition Functionality
The FinancialInstrumentReportingInvalidReferenceDataReport message is sent by the trading venue to
the national competent authority to report on all records that have become invalid based on updates
that have been received or that have passed the termination date original set for the instrument.
Outline
The FinancialInstrumentReportingInvalidReferenceDataReportV02 MessageDefinition is composed of 4
MessageBuildingBlocks:
A. DatePeriod
Date period capturing when instruments in the report have been invalidated
Usage:
Within MiFIR, only the From Date To Date field will be used with the From Date corresponding to
the date the first instrument was added to this report while the To Date is the date the last
instrument was added to the file.
B. NumberOfRecords
Number of invalid records in this message.
C. FinancialInstruments
Provides the details of the financial instruments.
D. SupplementaryData
Additional information that can not be captured in the structured fields and/or any other specific
block.
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
184 July 2025
```

