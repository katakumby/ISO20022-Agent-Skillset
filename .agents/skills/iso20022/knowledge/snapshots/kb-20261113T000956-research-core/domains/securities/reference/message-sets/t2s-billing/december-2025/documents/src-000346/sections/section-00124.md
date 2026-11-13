---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S Billing"
source_ids: ["src-000346"]
source_editions: ["december-2025"]
message_ids: []
heading_path: ["4 Message Items Types", "4.2 Message Datatypes", "4.2.5 IdentifierSet", "4.2.5.3 LEIIdentifier"]
file_pages: [150]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 4.2.5.3 LEIIdentifier

Source: [src-000346](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Billing_MessageSet/ISO20022_MDRPart1_Target2Securities_Billing_v1.pdf`. Locator: one-based file pages 150 to 150.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 150

```text
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
4.2.5.3  LEIIdentifier
Definition: Legal Entity Identifier is a code allocated to a party as described in ISO 17442 "Financial
Services - Legal Entity Identifier (LEI)".
Type: IdentifierSet
Identification scheme: Global LEI System; LEIIdentifier
Format
pattern [A-Z0-9]{18,18}[0-9]{2,2}
4.2.6 Quantity
4.2.6.1  Number
Definition: Number of objects represented as an integer.
Type: Quantity
Format
totalDigits 18
fractionDigits 0
4.2.7 Rate
4.2.7.1  BaseOneRate
Definition: Rate expressed as a decimal, for example, 0.7 is 7/10 and 70%.
Type: Rate
Format
totalDigits 11
fractionDigits 10
baseValue 1.0
4.2.7.2  PercentageRate
Definition: Rate expressed as a percentage, that is, in hundredths, for example, 0.7 is 7/10 of a percent,
and 7.0 is 7%.
Type: Rate
Approved by the Securities SEG on 20 November 2025 and the Payments
SEG on 01 December 2025, under the lead of the Securities Standards
Evaluation Group (SEG).
Message Items Types
Target2-Securities - Billing 150 December 2025
```

