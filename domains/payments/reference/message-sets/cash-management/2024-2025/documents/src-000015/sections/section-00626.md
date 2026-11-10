---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.9 Financial Institution Identification", "37.1.9.2 GenericFinancialIdentification1", "37.1.9.2.1 Identification <Id>"]
file_pages: [803]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.9.2.1 Identification <Id>

Source: [src-000015](../../../../../../../../../raw-input/cash_management/ISO20022_MDRPart2_CashManagement_2024_2025_v1.pdf). Locator: one-based file pages 803 to 803.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 803

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 803
   SchemeName <SchmeNm> [0..1]  803
{Or     Code <Cd> [1..1] CodeSet 803
Or}     Proprietary <Prtry> [1..1] Text 803
   Issuer <Issr> [0..1] Text 803
37.1.9.2.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification of a person.
Datatype: "Max35Text" on page 889
37.1.9.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
FinancialIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 803
Or}   Proprietary <Prtry> [1..1] Text 803
37.1.9.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstitutionIdentification1Code" on page 854
37.1.9.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 889
37.1.9.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 889
37.1.9.3  BranchAndFinancialInstitutionIdentification8
Definition: Unique and unambiguous identification of a financial institution or a branch of a financial
institution.
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 803 February 2025
```

