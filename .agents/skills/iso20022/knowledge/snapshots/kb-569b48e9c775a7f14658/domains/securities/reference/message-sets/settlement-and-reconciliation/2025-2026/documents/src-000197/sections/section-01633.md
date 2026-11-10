---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.7 Quantity", "35.2.7.2 Max30DecimalNumber"]
file_pages: [2189]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.7.2 Max30DecimalNumber

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2189 to 2189.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2189

```text
35.2.7.2  Max30DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6 with a
maximum of 30 digits and 29 fraction digits.
Type: Quantity
Format
totalDigits 30
fractionDigits 29
35.2.7.3  Max3Number
Definition: Number (max 999) of objects represented as an integer.
Type: Quantity
Format
totalDigits 3
fractionDigits 0
Constraints
• NumberRule
If Number is negative, then Sign must be present.
35.2.7.4  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
35.2.8 Rate
35.2.8.1  BaseOneRate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 1.0
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2189 March 2026
```

