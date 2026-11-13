---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["12 auth.042.001.02 FinancialInstrumentReportingInvalidReferenceDataReportV02", "12.4 Message Building Blocks", "12.4.3 FinancialInstruments <FinInstrms>", "12.4.3.1 FinancialInstrument <FinInstrm>", "12.4.3.1.5 DebtInstrumentAttributes <DebtInstrmAttrbts>", "12.4.3.1.5.2 MaturityDate <MtrtyDt>"]
file_pages: [197]
content_origin: "source-text-extraction"
mentioned_message_ids: ["auth.042.001.02"]
---

# 12.4.3.1.5.2 MaturityDate <MtrtyDt>

Source: [src-000321](../../../../../../../../../evidence/omitted/8d2c320c3a6fbfe4d503c6ab.md). Locator: one-based file pages 197 to 197.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 197

```text
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
12.4.3.1.5.2  MaturityDate <MtrtyDt>
Presence: [0..1]
Definition: Maturity date of the financial instrument.
Datatype: "ISODate" on page 449
12.4.3.1.5.3  NominalValuePerUnit <NmnlValPerUnit>
Presence: [1..1]
Definition: Nominal value of each instrument. If not available, the minimum traded value should be
populated.
Impacted by: C2 "ActiveOrHistoricCurrency", C5 "CurrencyAmount"
Datatype: "ActiveOrHistoricCurrencyAndAmount" on page 416
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
12.4.3.1.5.4  InterestRate <IntrstRate>
Presence: [1..1]
Definition: Interest rate of the debt instrument.
Approved by the Securities SEG on 17 July 2025 auth.042.001.02
FinancialInstrumentReportingInvalidReferenceData
ReportV02
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
197 July 2025
```

