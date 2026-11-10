---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAccountReferenceData"
source_ids: ["src-000372"]
source_editions: ["december-2019"]
message_ids: []
heading_path: ["11 Message Items Types", "11.2 Message Datatypes", "11.2.4 IdentifierSet"]
file_pages: [98]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 11.2.4 IdentifierSet

Source: [src-000372](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAccountReferenceData_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAccountReferenceData_v1.pdf`. Locator: one-based file pages 98 to 98.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 98

```text
11.2.4 IdentifierSet
11.2.4.1  AnyBICDec2014Identifier
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362: 2014 - "Banking - Banking telecommunication messages -
Business identifier code (BIC)".
Type: IdentifierSet
Identification scheme: SWIFT; AnyBICIdentifier
Format
pattern [A-Z0-9]{4,4}[A-Z]{2,2}[A-Z0-9]{2,2}([A-Z0-9]{3,3}){0,1}
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
11.2.4.2  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
11.2.5 Indicator
11.2.5.1  RequestedIndicator
Definition: Indicates if requested or not.
Type: Indicator
Meaning When True: Requested
Meaning When False: Not Requested
11.2.5.2  TrueFalseIndicator
Definition: A flag indicating a True or False value.
Type: Indicator
Meaning When True: True
Meaning When False: False
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 02 December 2019
Message Items Types
Target2-Securities - Securities Account Reference Data 98 December 2019
```

