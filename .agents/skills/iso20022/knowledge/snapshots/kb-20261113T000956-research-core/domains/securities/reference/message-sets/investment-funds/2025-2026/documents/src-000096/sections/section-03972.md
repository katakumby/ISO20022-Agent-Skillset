---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes", "66.2.1 Amount", "66.2.1.5 ImpliedCurrencyAndAmount"]
file_pages: [5270]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2.1.5 ImpliedCurrencyAndAmount

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5270 to 5270.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5270

```text
Name Attribute XML Name Datatype
Currency Ccy "ActiveOrHistoricCurrencyCode" on page 5276
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
66.2.1.5  ImpliedCurrencyAndAmount
Definition: Number of monetary units specified in a currency where the unit of currency is implied by the
context and compliant with ISO 4217. The decimal separator is a dot.
Note: a zero amount is considered a positive amount.
Type: Amount
Format
minInclusive 0
totalDigits 18
fractionDigits 5
66.2.2 CodeSet
66.2.2.1  AcceptedStatusReason1Code
Definition: Specifies the reason for an accepted status.
Type: CodeSet
CodeName Name Definition
PLAC PlaceNotAllowed Status of the account modification
instruction is accepted but modification
of the account data will not be carried
out for the place.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5270 May 2026
```

