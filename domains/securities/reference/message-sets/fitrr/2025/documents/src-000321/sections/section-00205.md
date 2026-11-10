---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["17 auth.048.001.01 FinancialInstrumentReportingCurrencyCodeReportV01", "17.4 Message Building Blocks", "17.4.1 CurrencyData <CcyData>", "17.4.1.1 Currency <Ccy>", "17.4.1.1.1 Code <Cd>"]
file_pages: [249]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.048.001.01"]
---

# 17.4.1.1.1 Code <Cd>

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 249 to 249.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 249

```text
Currency <Ccy> contains the following CurrencyCodeAndName1 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet C1 249
   Name <Nm> [1..1] Text 249
17.4.1.1.1  Code <Cd>
Presence: [1..1]
Definition: Currency is specified by its code.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
17.4.1.1.2  Name <Nm>
Presence: [1..1]
Definition: Currency is specified by its name.
Datatype: "Max70Text" on page 456
17.4.1.2  FractionalDigit <FrctnlDgt>
Presence: [0..1]
Definition: Fractional digit for the currency, that is, the number of decimals to use.
Datatype: "Max1Number" on page 452
17.4.1.3  CountryDetails <CtryDtls>
Presence: [1..1]
Definition: Details the country name and ISO 3166 country code.
CountryDetails <CtryDtls> contains the following elements (see "CountryCodeAndName3" on
page 339 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Code <Cd> [1..1] CodeSet C4 339
   Name <Nm> [1..1] Text 340
17.4.1.4  PreEuro <PreEuro>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 auth.048.001.01
FinancialInstrumentReportingCurrencyCodeReportV
01
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
249 July 2025
```

