---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.3 Amount", "6.1.3.4 AmountAndCurrencyExchangeDetails6", "6.1.3.4.3 CurrencyExchange <CcyXchg>", "6.1.3.4.3.3 UnitCurrency <UnitCcy>"]
file_pages: [811]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.3.4.3.3 UnitCurrency <UnitCcy>

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 811 to 811.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 811

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.1.3.4.3.3  UnitCurrency <UnitCcy>
Presence: [0..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 887
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
6.1.3.4.3.4  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used to convert an amount from one currency into another. This reflects the price at
which one currency was bought with another currency.
Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate
= UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 913
6.1.3.4.3.5  ContractIdentification <CtrctId>
Presence: [0..1]
Definition: Unique identification to unambiguously identify the foreign exchange contract.
Datatype: "Max35Text" on page 916
6.1.3.4.3.6  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 908
6.1.3.4.3.7  ExchangeRateBase <XchgRateBase>
Presence: [0..1]
Definition: Expresses the ratio between the base of the denomination of the Unit Currency to the base
of the denomination of the Quoted Currency.
Datatype: "PositiveNumber" on page 912
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
811 March 2026
```

