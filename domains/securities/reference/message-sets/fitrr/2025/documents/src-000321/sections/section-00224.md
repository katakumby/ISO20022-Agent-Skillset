---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types"]
file_pages: [274]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22 Message Items Types

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 274 to 274.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 274

```text
22 Message Items Types
22.1 MessageComponents
22.1.1 Amount
22.1.1.1  AmountAndDirection53
Definition: Amount of money expressed with an optional currency code and debit/credit indicator.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Amount <Amt> [1..1] Amount C2, C5 274
   Sign <Sgn> [0..1] Indicator 274
22.1.1.1.1  Amount <Amt>
Presence: [1..1]
Definition: Amount of money that results in an increase (positively signed) or decrease (negatively
signed), with specification of the currency.
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
22.1.1.1.2  Sign <Sgn>
Presence: [0..1]
Definition: Indicates that the amount value is positive or negative.
Usage: When absent, the amount is positive.
Datatype: One of the following values must be used (see "PlusOrMinusIndicator" on page 451):
• Meaning When True: Plus
• Meaning When False: Minus
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
274 July 2025
```

