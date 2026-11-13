---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["53 setr.013.001.05 SwitchOrderV05", "53.4 Message Building Blocks", "53.4.5 SwitchOrderDetails <SwtchOrdrDtls>", "53.4.5.19 ForeignExchangeDetails <FXDtls>", "53.4.5.19.2 QuotedCurrency <QtdCcy>"]
file_pages: [3793]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.013.001.05"]
---

# 53.4.5.19.2 QuotedCurrency <QtdCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3793 to 3793.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3793

```text
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
53.4.5.19.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the unit currency is converted in an exchange rate calculation.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Impacted by: C2 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
53.4.5.19.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects
that amount of the quoted currency that can be purchased with one unit of the unit currency, as follows:
1 x CUR1 = nnn x CUR2,
where:
CUR1 is the unit currency
CUR2 is the quoted currency
nnn is the exchange rate.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Datatype: "BaseOneRate" on page 5401
53.4.5.19.4  QuotationDate <QtnDt>
Presence: [0..1]
Definition: Date and time at which an exchange rate is quoted.
Datatype: "ISODateTime" on page 5388
Approved by the Securities SEG on 27 January 2026 setr.013.001.05 SwitchOrderV05
Investment Funds - Maintenance 2025 - 2026 3793 May 2026
```

