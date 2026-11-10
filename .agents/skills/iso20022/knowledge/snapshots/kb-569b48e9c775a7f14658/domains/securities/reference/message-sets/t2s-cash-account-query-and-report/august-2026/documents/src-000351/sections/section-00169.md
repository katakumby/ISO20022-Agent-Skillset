---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S CashAccountQueryAndReport"
source_ids: ["src-000351"]
source_editions: ["august-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.2 Message Datatypes", "7.2.8 Text", "7.2.8.11 Max3NumericText"]
file_pages: [184]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.2.8.11 Max3NumericText

Source: [src-000351](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_CashAccountQueryAndReport_MessageSet/ISO20022_MDRPart2_Target2Securities_CashAccountQueryAndReport_v1.pdf`. Locator: one-based file pages 184 to 184.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 184

```text
7.2.8.11  Max3NumericText
Definition: Specifies a numeric string with a maximum length of 3 digits.
Type: Text
Format
pattern [0-9]{1,3}
7.2.8.12  Max4AlphaNumericText
Definition: Specifies an alphanumeric string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
pattern [a-zA-Z0-9]{1,4}
7.2.8.13  Max4Text
Definition: Specifies a character string with a maximum length of 4 characters.
Type: Text
Format
minLength 1
maxLength 4
7.2.8.14  Max5NumericText
Definition: Specifies a numeric string with a maximum length of 5 digits.
Type: Text
Format
pattern [0-9]{1,5}
7.2.8.15  Max6Text
Definition: Specifies a character string with a maximum length of 6 characters.
Type: Text
Format
minLength 1
maxLength 6
Approved by the Securities Standards Evaluation Group (SEG) on 18 June
2026.
Message Items Types
Target2-Securities - Cash Account Query and Report 184 August 2026
```

