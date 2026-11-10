---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Transactions and Financial Instruments Data Reporting"
source_ids: ["src-000321"]
source_editions: ["July 2025"]
message_ids: []
heading_path: ["22 Message Items Types", "22.1 MessageComponents", "22.1.5 Financial Instrument", "22.1.5.3 DerivativeInterest2"]
file_pages: [326]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 22.1.5.3 DerivativeInterest2

Source: [src-000321](../../../../../../../../../raw-input/transactions_and_financial_instruments_data_reporting_fitrr/ISO20022_MDRPart2_FITRR_TransactionAndFinancialInstrumentsDataReporting_FastTrackMaintenance2025_v1.pdf). Locator: one-based file pages 326 to 326.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 326

```text
Definition: Currency in which the notional is denominated.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.5.3  DerivativeInterest2
Definition: Specifies a multi-leg interest derivative.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherNotionalCurrency <OthrNtnlCcy> [1..1] CodeSet C2 326
22.1.5.3.1  OtherNotionalCurrency <OthrNtnlCcy>
Presence: [1..1]
Definition: Currency in which leg 2 of the contract is denominated, in case of multi-currency or cross-
currency swaps.
Currency in which leg 2 of the swap is denominated, in case of swaptions where the underlying swap is
multi-currency.
Impacted by: C2 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 417
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
22.1.5.4  DerivativeForeignExchange2
Definition: Attributes of non-financial instrument of type foreign exchange as underlying.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherNotionalCurrency <OthrNtnlCcy> [1..1] CodeSet C2 326
22.1.5.4.1  OtherNotionalCurrency <OthrNtnlCcy>
Presence: [1..1]
Approved by the Securities SEG on 17 July 2025 Message Items Types
Financial Instruments and Transactions Regulatory Reporting
(Transactions and Financial Instruments Data Reporting) -
Fast Track Minatnenance 2025
326 July 2025
```

