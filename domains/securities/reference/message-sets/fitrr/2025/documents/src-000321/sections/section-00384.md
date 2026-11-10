---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.2 Message Datatypes", "22.2.2 CodeSet", "22.2.2.96 NonTradingDayReason1Code"]
file_pages: [442]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.2.2.96 NonTradingDayReason1Code

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 442 to 442.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 442

```text
22.2.2.96  NonTradingDayReason1Code
Definition: Specifies the reason capturing a non trading day.
Type: CodeSet
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
22.2.2.97  NoReasonCode
Definition: Specifies that there is no reason available.
Type: CodeSet
CodeName Name Definition
NORE NoReason No reason to report or no reason
available to report.
22.2.2.98  OptionStyle7Code
Definition: Specifies how an option for a derivative or securities derivative can be exercised.
Type: CodeSet
CodeName Name Definition
AMER American Option can be exercised before or on
expiry date.
ASIA Asian Option where the payoff is not
determined by the underlying price at
maturity but by the average underlying
price over some pre-set period of time.
BERM Bermudan Option that can be exercised on multiple
discrete dates prior to, or on expiry date.
EURO European Option that can be exercised on expiry
date only.
OTHR Other Other type of option style.
22.2.2.99  OptionType2Code
Definition: Specifies whether it is a call option (right to purchase a specific underlying asset) or a put
option (right to sell a specific underlying asset) or any other type of option.
Type: CodeSet
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
442 July 2025
```

