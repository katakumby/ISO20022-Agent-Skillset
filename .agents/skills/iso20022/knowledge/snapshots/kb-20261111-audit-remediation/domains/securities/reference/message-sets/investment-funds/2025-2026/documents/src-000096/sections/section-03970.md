---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.2 Message Datatypes"]
file_pages: [5268]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.2 Message Datatypes

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5268 to 5268.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5268

```text
Definition: Additional information about the rejected status reason.
Datatype: "Max350Text" on page 5403
66.2 Message Datatypes
66.2.1 Amount
66.2.1.1  ActiveCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of currency) is not
checked as per ISO 4217: It must be lesser than or equal to 13.
Note: The decimal separator is a dot.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 5275
Format
minInclusive 0
totalDigits 18
fractionDigits 13
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
66.2.1.2  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 5275
Format
minInclusive 0
totalDigits 18
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5268 May 2026
```

