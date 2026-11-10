---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Settlement and Reconciliation"
source_ids: ["src-000197"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["35 Message Items Types", "35.2 Message Datatypes", "35.2.5 IdentifierSet", "35.2.5.9 UTIIdentifier"]
file_pages: [2188]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 35.2.5.9 UTIIdentifier

Source: [src-000197](../../../../../../../../../evidence/omitted/e96bb98c659322ed5684b325.md). Locator: one-based file pages 2188 to 2188.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2188

```text
Type: IdentifierSet
Identification scheme: SWIFT; MICIdentifier
Format
pattern [A-Z0-9]{4,4}
35.2.5.9  UTIIdentifier
Definition: Unique Transaction Identifier (UTI). Unique number allocated to a financial transaction as
agreed among the parties and/or within the regulatory system under which it is formed. The UTI is
described in the latest edition of the international standard ISO 23897:2020.
Type: IdentifierSet
Identification scheme: Parties to a trade; UTIIdentier
Format
pattern [A-Z0-9]{18}[0-9]{2}[A-Z0-9]{0,32}
35.2.6 Indicator
35.2.6.1  PlusOrMinusIndicator
Definition: Indicates a positive or negative value.
Type: Indicator
Meaning When True: Plus
Meaning When False: Minus
35.2.6.2  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
35.2.7 Quantity
35.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
Approved by the Securities SEG on 27 January 2026 Message Items Types
Settlement And Reconciliation - Maintenance 2025 - 2026 2188 March 2026
```

