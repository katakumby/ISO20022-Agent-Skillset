---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["9 auth.039.001.01 FinancialInstrumentReportingNonWorkingDayReportV01", "9.4 Message Building Blocks", "9.4.2 NonWorkingDay <NonWorkgDay>", "9.4.2.2 NonWorkingDay <NonWorkgDay>", "9.4.2.2.3 Reason <Rsn>"]
file_pages: [169]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.039.001.01"]
---

# 9.4.2.2.3 Reason <Rsn>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 169 to 169.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 169

```text
Datatype: "ISODate" on page 449
9.4.2.2.3  Reason <Rsn>
Presence: [0..1]
Definition: Reason code for the non-working day.
Datatype: "NonTradingDayReason1Code" on page 442
CodeName Name Definition
THOL TradingHoliday The date is a full day trading holiday with
no trades performed.
OTHR Other Other reasons a day is a non-trading day
e.g. technical fault, company specific
non-trading day not known in advance.
HALF HalfDay Trading venue was open for an amount
of time, up to half the day.
PHOL PublicHoliday Date is a public holiday.
BHOL BankHoliday Date is a bank holiday.
WKND Weekend Date being reported falls during the
weekend.
9.4.3 SupplementaryData <SplmtryData>
Presence: [0..*]
Definition: Additional information that can not be captured in the structured fields and/or any other
specific block.
Impacted by: C2 "SupplementaryDataRule"
SupplementaryData <SplmtryData> contains the following elements (see "SupplementaryData1" on
page 341 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PlaceAndName <PlcAndNm> [0..1] Text 341
   Envelope <Envlp> [1..1] (External Schema) 341
Constraints
• SupplementaryDataRule
This component may not be used without the explicit approval of a SEG and submission to the RA of
ISO 20022 compliant structure(s) to be used in the Envelope element.
Approved by the Securities SEG on 17 July 2025 auth.039.001.01
FinancialInstrumentReportingNonWorkingDayRepor
tV01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
169 July 2025
```

