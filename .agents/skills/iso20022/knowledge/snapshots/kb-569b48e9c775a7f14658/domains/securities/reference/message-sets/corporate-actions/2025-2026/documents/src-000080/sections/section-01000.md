---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.2 Message Datatypes", "16.2.5 IdentifierSet", "16.2.5.7 LEIIdentifier"]
file_pages: [1246]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.2.5.7 LEIIdentifier

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 1246 to 1246.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1246

```text
Format
pattern [A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}
16.2.5.7  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
16.2.5.8  MICIdentifier
Definition: Market Identifier Code. The identification of a financial market, as stipulated in the norm ISO
10383 'Codes for exchanges and market identifications'.
Type: IdentifierSet
Identification scheme: SWIFT; MICIdentifier
Format
pattern [A-Z0-9]{4,4}
16.2.6 Indicator
16.2.6.1  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
16.2.7 Quantity
16.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 1246 February 2026
```

