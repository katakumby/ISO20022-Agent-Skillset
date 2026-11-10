---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Initiation"
source_ids: ["src-000174"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.2 Message Datatypes", "6.2.10 Text", "6.2.10.16 Max70Text"]
file_pages: [610]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.2.10.16 Max70Text

Source: [src-000174](../../../../../../../../../raw-input/payments_initiation/ISO20022_MDRPart2_PaymentsInitiation_2025_2026_v1.pdf). Locator: one-based file pages 610 to 610.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 610

```text
6.2.10.16  Max70Text
Definition: Specifies a character string with a maximum length of 70characters.
Type: Text
Format
minLength 1
maxLength 70
6.2.10.17  PhoneNumber
Definition: The collection of information which identifies a specific phone or FAX number as defined by
telecom services.
It consists of a "+" followed by the country code (from 1 to 3 characters) then a "-" and finally, any
combination of numbers, "(", ")", "+" and "-" (up to 30 characters).
Type: Text
Format
pattern \+[0-9]{1,3}-[0-9()+\-]{1,30}
6.2.11 Year
6.2.11.1  ISOYear
Definition: Year represented by YYYY (ISO 8601).
Type: Year
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Initiation - Maintenance 2025 - 2026 610 March 2026
```

