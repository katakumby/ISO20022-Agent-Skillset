---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.9 Text", "6.2.9.8 Max15NumericText"]
file_pages: [915]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.9.8 Max15NumericText

Source: [src-000005](../../../../../../../../../raw-input/banktocustomer_cash_management/ISO20022_MDRPart2_BanktoCustomerCashManagement_2025_2026_v1.pdf). Locator: one-based file pages 915 to 915.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 915

```text
maxLength 140
6.2.9.8  Max15NumericText
Definition: Specifies a numeric string with a maximum length of 15 digits.
Type: Text
Format
pattern [0-9]{1,15}
6.2.9.9  Max15PlusSignedNumericText
Definition: Specifies a numeric string with a maximum length of 15 digits and may be prefixed with a
plus sign.
Type: Text
Format
pattern [\+]{0,1}[0-9]{1,15}
6.2.9.10  Max16Text
Definition: Specifies a character string with a maximum length of 16 characters.
Type: Text
Format
minLength 1
maxLength 16
6.2.9.11  Max20000Text
Definition: Specifies a character string with a maximum length of 20, 000 characters.
Type: Text
Format
minLength 1
maxLength 20000
6.2.9.12  Max2048Text
Definition: Specifies a character string with a maximum length of 2048 characters.
Type: Text
Format
minLength 1
maxLength 2048
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
915 March 2026
```

