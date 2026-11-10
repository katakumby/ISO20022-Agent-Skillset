---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.1 Amount", "7.2.1.2 ActiveOrHistoricCurrencyAnd13DecimalAmount"]
file_pages: [612]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.1.2 ActiveOrHistoricCurrencyAnd13DecimalAmount

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 612 to 612.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 612

```text
7.2.1.2  ActiveOrHistoricCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active or a historic currency where the unit of
currency is explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of
currency) is not checked as per ISO 4217: It must be lesser than or equal to 13.
Note: The decimal separator is a dot.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveOrHistoricCurrencyCode" on page 613
Format
minInclusive 0
totalDigits 18
fractionDigits 13
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
7.2.1.3  ActiveOrHistoricCurrencyAndAmount
Definition: A number of monetary units specified in an active or a historic currency where the unit of
currency is explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy "ActiveOrHistoricCurrencyCode" on page 613
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Constraints
• ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 612 February 2025
```

