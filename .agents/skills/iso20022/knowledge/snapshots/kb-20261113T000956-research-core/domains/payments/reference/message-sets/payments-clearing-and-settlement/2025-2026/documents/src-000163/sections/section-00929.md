---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.2 Message Datatypes", "10.2.2 Binary"]
file_pages: [1224]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.2.2 Binary

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1224 to 1224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1224

```text
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
10.2.2 Binary
10.2.2.1  Max10KBinary
Definition: Binary data of 10K maximum.
Type: Binary
Format
minLength 1
maxLength 10240
10.2.3 CodeSet
10.2.3.1  ActiveCurrencyCode
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
10.2.3.2  ActiveOrHistoricCurrencyCode
Definition: A code allocated to a currency by a Maintenance Agency under an international identification
scheme, as described in the latest edition of the international standard ISO 4217 "Codes for the
representation of currencies and funds".
Type: CodeSet
Format
pattern [A-Z]{3,3}
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1224 March 2026
```

