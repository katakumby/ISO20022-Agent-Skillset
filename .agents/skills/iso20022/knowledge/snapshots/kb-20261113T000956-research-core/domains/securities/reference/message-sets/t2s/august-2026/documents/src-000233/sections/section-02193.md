---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.15 Foreign Exchange", "82.1.15.1 ForeignExchangeTerms24", "82.1.15.1.3 ExchangeRate <XchgRate>"]
file_pages: [2956]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.15.1.3 ExchangeRate <XchgRate>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2956 to 2956.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2956

```text
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
82.1.15.1.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects the
price at which one currency was bought with another currency.
Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate
= UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 3324
82.1.15.1.4  ResultingAmount <RsltgAmt>
Presence: [0..1]
Definition: Counter value of a foreign exchange conversion.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 3209
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
82.1.15.2  ForeignExchangeTerms34
Definition: Information needed to process a currency exchange or conversion.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C1 2957
   QuotedCurrency <QtdCcy> [1..1] CodeSet C1 2957
   ExchangeRate <XchgRate> [1..1] Rate 2957
   QuotationDate <QtnDt> [0..1] DateTime 2957
   QuotingInstitution <QtgInstn> [0..1] ± 2957
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2956 August 2026
```

