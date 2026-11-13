---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.2 Message Datatypes", "12.2.1 Amount", "12.2.1.2 ActiveOrHistoricCurrencyAnd13DecimalAmount"]
file_pages: [471]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.2.1.2 ActiveOrHistoricCurrencyAnd13DecimalAmount

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 471 to 471.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 471

```text
12.2.1.2  ActiveOrHistoricCurrencyAnd13DecimalAmount
Definition: A number of monetary units specified in an active or a historic currency where the unit of
currency is explicit and compliant with ISO 4217. The number of fractional digits (or minor unit of
currency) is not checked as per ISO 4217: It must be lesser than or equal to 13.
Note: The decimal separator is a dot.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy ActiveOrHistoricCurrencyCode on page 473
Format
minInclusive 0
totalDigits 18
fractionDigits 13
Constraints
• ActiveOrHistoricCurrency
(Rule)
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the Currency
is exchanged.
Error handling:
– Error severity: Fatal
– Error Code: D00006
– Error Text: Invalid currency code.
12.2.1.3  ActiveOrHistoricCurrencyAndAmount
Definition: A number of monetary units specified in an active or a historic currency where the unit of
currency is explicit and compliant with ISO 4217.
Type: Amount
This data type contains the following XML attribute:
Name Attribute XML Name Datatype
Currency Ccy ActiveOrHistoricCurrencyCode on page 473
Format
minInclusive 0
totalDigits 18
fractionDigits 5
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 471
```

