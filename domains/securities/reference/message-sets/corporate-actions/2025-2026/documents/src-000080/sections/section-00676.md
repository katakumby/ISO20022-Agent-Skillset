---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.3 GenericFinancialIdentification1", "16.1.8.3.2 SchemeName <SchmeNm>"]
file_pages: [867]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.3.2 SchemeName <SchmeNm>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 867 to 867.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 867

```text
Datatype: "Max35Text" on page 1251
16.1.8.3.2  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Name of the identification scheme.
SchemeName <SchmeNm> contains one of the following
FinancialIdentificationSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 867
Or}   Proprietary <Prtry> [1..1] Text 867
16.1.8.3.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalFinancialInstitutionIdentification1Code" on page 1209
16.1.8.3.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 1251
16.1.8.3.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 1251
16.1.8.4  BranchAndFinancialInstitutionIdentification6
Definition: Unique and unambiguous identification of a financial institution or a branch of a financial
institution.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1] ± 867
   BranchIdentification <BrnchId> [0..1] ± 868
16.1.8.4.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 867 February 2026
```

