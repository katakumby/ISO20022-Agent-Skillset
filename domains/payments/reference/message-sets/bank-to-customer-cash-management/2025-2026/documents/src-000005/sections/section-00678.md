---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.7 Quantity"]
file_pages: [912]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.7 Quantity

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 912 to 912.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 912

```text
6.2.7 Quantity
6.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
6.2.7.2  Max30DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6 with a
maximum of 30 digits and 29 fraction digits.
Type: Quantity
Format
totalDigits 30
fractionDigits 29
6.2.7.3  NonNegativeDecimalNumber
Definition: Number of objects represented as a non negative decimal number, for example, 0.75 or
45.6.
Type: Quantity
Format
minInclusive 0
totalDigits 18
fractionDigits 17
6.2.7.4  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
6.2.7.5  PositiveNumber
Definition: Number of objects represented as a positive integer.
Type: Quantity
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
912 March 2026
```

