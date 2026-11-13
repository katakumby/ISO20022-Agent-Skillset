---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.1 Amount", "7.2.1.4 ImpliedCurrencyAndAmount"]
file_pages: [613]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.1.4 ImpliedCurrencyAndAmount

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 613 to 613.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 613

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
7.2.1.4  ImpliedCurrencyAndAmount
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount.
Type: Amount
Format
minInclusive 0
totalDigits 18
fractionDigits 5
7.2.2 CodeSet
7.2.2.1  ActiveCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
7.2.2.2  ActiveOrHistoricCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 613 February 2025
```

