---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.7 Financial Institution Identification", "10.1.7.2 GenericFinancialIdentification1", "10.1.7.2.2 SchemeName <SchmeNm>"]
file_pages: [1173]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.7.2.2 SchemeName <SchmeNm>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1173 to 1173.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1173

```text
Datatype: "Max35Text" on page 1246
10.1.7.2.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
FinancialIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1173
Or}   Proprietary <Prtry> [1..1] Text 1173
10.1.7.2.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstitutionIdentification1Code" on page 1230
10.1.7.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 1246
10.1.7.2.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 1246
10.1.7.3  BranchAndFinancialInstitutionIdentification8
Definition: Unique and unambiguous identification of a financial institution or a branch of a financial
institution.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1173 March 2026
```

