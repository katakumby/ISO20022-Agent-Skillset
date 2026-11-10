---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["50 setr.010.001.05 SubscriptionOrderV05", "50.4 Message Building Blocks", "50.4.4 MultipleOrderDetails <MltplOrdrDtls>", "50.4.4.9 IndividualOrderDetails <IndvOrdrDtls>", "50.4.4.9.12 ForeignExchangeDetails <FXDtls>", "50.4.4.9.12.1 UnitCurrency <UnitCcy>"]
file_pages: [3068]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.010.001.05"]
---

# 50.4.4.9.12.1 UnitCurrency <UnitCcy>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 3068 to 3068.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 3068

```text
ForeignExchangeDetails <FXDtls> contains the following ForeignExchangeTerms44 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   UnitCurrency <UnitCcy> [1..1] CodeSet C3 3068
   QuotedCurrency <QtdCcy> [1..1] CodeSet C3 3068
   ExchangeRate <XchgRate> [1..1] Rate 3068
   QuotationDate <QtnDt> [0..1] DateTime 3069
   QuotingInstitution <QtgInstn> [0..1] ± 3069
50.4.4.9.12.1  UnitCurrency <UnitCcy>
Presence: [1..1]
Definition: Currency from which the quoted currency is converted in an exchange rate calculation.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Impacted by: C3 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
50.4.4.9.12.2  QuotedCurrency <QtdCcy>
Presence: [1..1]
Definition: Currency into which the unit currency is converted in an exchange rate calculation.
1 x <UnitCcy> = <XchgRate> x <QtdCcy>.
Impacted by: C3 "ActiveCurrency"
Datatype: "ActiveCurrencyCode" on page 5275
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
50.4.4.9.12.3  ExchangeRate <XchgRate>
Presence: [1..1]
Definition: Factor used for the conversion of an amount from one currency into another. This reflects
that amount of the quoted currency that can be purchased with one unit of the unit currency, as follows:
Approved by the Securities SEG on 27 January 2026 setr.010.001.05 SubscriptionOrderV05
Investment Funds - Maintenance 2025 - 2026 3068 May 2026
```

