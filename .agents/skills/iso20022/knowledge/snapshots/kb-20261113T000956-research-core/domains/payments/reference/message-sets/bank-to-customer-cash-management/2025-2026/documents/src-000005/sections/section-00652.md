---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes"]
file_pages: [885]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2 Message Datatypes

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 885 to 885.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 885

```text
Datatype: "Max35Text" on page 916
6.2 Message Datatypes
6.2.1 Amount
6.2.1.1  ActiveCurrencyAndAmount
Definition: A number of monetary units specified in an active currency where the unit of currency is
explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveCurrencyCode" on page 887
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Constraints
• ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the message
containing the currency is exchanged. Valid active currency codes are registered with the ISO 4217
Maintenance Agency, consist of three (3) contiguous letters, and are not yet withdrawn on the day
the message containing the Currency is exchanged.
• CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
6.2.1.2  ActiveOrHistoricCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active or a historic currency where the unit of
currency is explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of
currency) is not checked as per ISO 4217: It must be lesser than or equal to 13.
Note: The decimal separator is a dot.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveOrHistoricCurrencyCode" on page 887
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
885 March 2026
```

