---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.8 Rate"]
file_pages: [913]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.8 Rate

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 913 to 913.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 913

```text
Format
minInclusive 1
totalDigits 18
fractionDigits 0
6.2.8 Rate
6.2.8.1  BaseOneRate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 1.0
6.2.8.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 100.0
6.2.9 Text
6.2.9.1  Exact1NumericText
Definition: Specifies a numeric string with an exact length of1digit.
Type: Text
Format
pattern [0-9]
6.2.9.2  Exact3NumericText
Definition: Specifies a numeric string with an exact length of 3 digits.
Type: Text
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
913 March 2026
```

