---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.2 Message Datatypes", "3.2.4 IdentifierSet", "3.2.4.3 LEIIdentifier"]
file_pages: [55]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.2.4.3 LEIIdentifier

Source: [src-000011](../../../../../../../../evidence/omitted/b1a725a8c57af20c03e238c2.md). Locator: one-based file pages 55 to 55.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 55

```text
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous characters.
3.2.4.3  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
3.2.5 Indicator
3.2.5.1  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
3.2.6 Text
3.2.6.1  Exact4AlphaNumericText
Definition: Specifies an alphanumeric string with a length of 4 characters.
Type: Text
Format
pattern [a-zA-Z0-9]{4}
3.2.6.2  Max128Text
Definition: Specifies a character string with a maximum length of 128 characters.
Type: Text
Format
minLength 1
maxLength 128
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 55 March 2024
```

