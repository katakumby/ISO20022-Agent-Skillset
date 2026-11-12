---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.1 MessageComponents", "4.1.4 Foreign Exchange", "4.1.4.1 ForeignExchangeTerms24", "4.1.4.1.2 QuotedCurrency <QtdCcy>"]
file_pages: [116]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.1.4.1.2 QuotedCurrency <QtdCcy>

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 116 to 116.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 116

```text
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
4.1.4.1.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the base currency is converted, in a currency exchange.
Impacted by: C1 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
4.1.4.1.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects the
price at which one currency was bought with another currency.
Usage: ExchangeRate expresses the ratio between UnitCurrency and QuotedCurrency (ExchangeRate
= UnitCurrency/QuotedCurrency).
Datatype: "BaseOneRate" on page 150
4.1.4.1.4  ResultingAmount <RsltgAmt>
Presence: [0..1]
Definition: Counter value of a foreign exchange conversion.
Impacted by: C1 "ActiveCurrency", C4 "CurrencyAmount"
Datatype: "ActiveCurrencyAndAmount" on page 143
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 116 December 2025
```

