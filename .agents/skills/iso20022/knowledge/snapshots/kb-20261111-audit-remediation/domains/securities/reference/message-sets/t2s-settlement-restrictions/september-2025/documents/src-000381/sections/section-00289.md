---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SettlementRestrictions"
source_ids: ["src-000381"]
source_editions: ["september-2025"]
message_ids: []
heading_path: ["9 Message Items Types", "9.2 Message Datatypes", "9.2.5 IdentifierSet", "9.2.5.4 LEIIdentifier"]
file_pages: [342]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 9.2.5.4 LEIIdentifier

Source: [src-000381](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SettlementRestrictions_MessageSet/ISO20022_MDRPart2_Target2Securities_SettlementRestrictions_v1.pdf`. Locator: one-based file pages 342 to 342.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 342

```text
Format
pattern [A-Z]{2,2}[A-Z0-9]{9,9}[0-9]{1,1}
9.2.5.4  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
9.2.5.5  MICIdentifier
Definition: Market Identifier Code. The identification of a financial market, as stipulated in the norm ISO
10383 'Codes for exchanges and market identifications'.
Type: IdentifierSet
Identification scheme: SWIFT; MICIdentifier
Format
pattern [A-Z0-9]{4,4}
9.2.6 Indicator
9.2.6.1  YesNoIndicator
Definition: Indicates a "Yes" or "No" type of answer for an element.
Type: Indicator
Meaning When True: Yes
Meaning When False: No
9.2.7 Quantity
9.2.7.1  DecimalNumber
Definition: Number of objects represented as a decimal number, for example 0.75 or 45.6.
Type: Quantity
Format
totalDigits 18
fractionDigits 17
Approved by the Securities SEG on 21 August 2025 Message Items Types
Target2-Securities - Settlement Restrictions 342 September 2025
```

