---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.2 Message Datatypes", "17.2.6 Indicator"]
file_pages: [495]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.2.6 Indicator

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 495 to 495.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 495

```text
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
17.2.6 Indicator
17.2.6.1  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
17.2.7 Quantity
17.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
17.2.8 Text
17.2.8.1  Exact3NumericText
Definition: Specifies a numeric string with an exact length of 3 digits.
Type: Text
Format
pattern [0-9]{3}
17.2.8.2  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
17.2.8.3  Exact4NumericText
Definition: Specifies a numeric string with an exact length of 4 digits.
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
495 March 2024
```

