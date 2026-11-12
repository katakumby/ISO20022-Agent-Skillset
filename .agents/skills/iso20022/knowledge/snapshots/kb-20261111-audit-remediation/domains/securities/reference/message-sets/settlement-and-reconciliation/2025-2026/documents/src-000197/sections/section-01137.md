---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.1 MessageComponents", "35.1.16 Miscellaneous", "35.1.16.45 ForeignExchangeTerms23", "35.1.16.45.2 QuotedCurrency <QtdCcy>"]
file_pages: [1582]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.1.16.45.2 QuotedCurrency <QtdCcy>

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 1582 to 1582.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1582

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.1.16.45.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 2044
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
35.1.16.45.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects the
price at which one currency was bought with another currency.
Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate
= UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 2189
35.1.16.45.4  ResultingAmount <RsltgAmt>
Presence: [1..1]
Definition: Counter value of a foreign exchange conversion.
Impacted by: C1 "ActiveCurrency", C9 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 2040
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 1582 March 2026
```

