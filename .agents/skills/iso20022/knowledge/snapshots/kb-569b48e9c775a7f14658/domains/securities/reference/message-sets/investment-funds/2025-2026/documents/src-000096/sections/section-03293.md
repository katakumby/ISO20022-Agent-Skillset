---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.21 Foreign Exchange", "66.1.21.1 ForeignExchangeTerms19", "66.1.21.1.2 QuotedCurrency <QtdCcy>"]
file_pages: [4530]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.21.1.2 QuotedCurrency <QtdCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4530 to 4530.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4530

```text
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.21.1.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.1.21.1.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects the
price at which one currency was bought with another currency.
Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate
= UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 5401
66.1.21.2  ForeignExchangeTerms6
Definition: Information needed to process a currency exchange or conversion.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C2 4531
   QuotedCurrency <QtdCcy> [1..1] CodeSet C2 4531
   ExchangeRate <XchgRate> [1..1] Rate 4531
   QuotationDate <QtnDt> [0..1] DateTime 4531
   QuotingInstitution <QtgInstn> [0..1] ± 4531
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4530 May 2026
```

