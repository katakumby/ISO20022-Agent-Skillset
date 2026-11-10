---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01", "9.3 Constraints"]
file_pages: [167]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.039.001.01"]
---

# 9.3 Constraints

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 167 to 167.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 167

```text
9.3 Constraints
C1 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C2 SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the
RA of ISO 20022 compliant structure(s) to be used in the Envelope element.
C3 ValidMICRule
Market Identification code must be an active market at the time of reporting.
9.4 Message Building Blocks
This chapter describes the MessageBuildingBlocks of this MessageDefinition.
9.4.1 ReportHeader <RptHdr>
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
9.4.2 NonWorkingDay <NonWorkgDay>
Presence: [1..*]
Definition: Provides details on the days a venue is not open.
NonWorkingDay <NonWorkgDay> contains the following SecuritiesNonTradingDayReport1
elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± C3 168
   NonWorkingDay <NonWorkgDay> [1..*]  168
     TechnicalRecordIdentification <TechRcrdId> [0..1] Text 168
     Date <Dt> [1..1] Date 168
     Reason <Rsn> [0..1] CodeSet 169
Approved by the Securities SEG on 17 July 2025 auth.039.001.01
FinancialInstrumentReportingNonWorkingDayRepor
tV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
167 July 2025
```

