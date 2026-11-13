---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.15 Foreign Exchange", "82.1.15.2 ForeignExchangeTerms34", "82.1.15.2.1 UnitCurrency <UnitCcy>"]
file_pages: [2957]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.15.2.1 UnitCurrency <UnitCcy>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2957 to 2957.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2957

```text
82.1.15.2.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency in which the rate of exchange is expressed in a currency exchange. In the example
1GBP = xxxCUR, the unit currency is GBP.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.1.15.2.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveOrHistoricCurrency"
Datatype: "ActiveOrHistoricCurrencyCode" on page 3212
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
82.1.15.2.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: The value of one currency expressed in relation to another currency. ExchangeRate
expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate = UnitCurrency/
QuotedCurrency).
Datatype: "BaseOneRate" on page 3324
82.1.15.2.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 3320
82.1.15.2.5  QuotingInstitution <QtgInstn>
Presence: [0..1]
Definition: Party that proposes a foreign exchange rate.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2957 August 2026
```

