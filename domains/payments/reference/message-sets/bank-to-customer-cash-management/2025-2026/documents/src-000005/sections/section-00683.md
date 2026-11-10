---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.9 Text", "6.2.9.18 Max4Text"]
file_pages: [917]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.9.18 Max4Text

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 917 to 917.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 917

```text
6.2.9.18  Max4Text
Definition: Specifies a character string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
6.2.9.19  Max500Text
Definition: Specifies a character string with a maximum length of 500 characters.
Type: Text
Format
minLength 1
maxLength 500
6.2.9.20  Max5NumericText
Definition: Specifies a numeric string with a maximum length of 5 digits.
Type: Text
Format
pattern [0-9]{1,5}
6.2.9.21  Max70Text
Definition: Specifies a character string with a maximum length of 70characters.
Type: Text
Format
minLength 1
maxLength 70
6.2.9.22  Min2Max3NumericText
Definition: Specifies a numeric string with a minimum length of 2 digits, and a maximum length of 3
digits.
Type: Text
Format
pattern [0-9]{2,3}
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
917 March 2026
```

