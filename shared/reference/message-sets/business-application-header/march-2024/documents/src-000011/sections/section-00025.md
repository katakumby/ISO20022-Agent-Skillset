---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "Business Application Header"
source_ids: ["src-000011"]
source_editions: ["Version 4 March 2024"]
message_ids: []
heading_path: ["3 Message Items Types", "3.1 MessageComponents", "3.1.1 Financial Institution Identification", "3.1.1.2 BranchAndFinancialInstitutionIdentification8", "3.1.1.2.1 FinancialInstitutionIdentification <FinInstnId>"]
file_pages: [27]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 3.1.1.2.1 FinancialInstitutionIdentification <FinInstnId>

Source: [src-000011](../../../../../../../../raw-input/business_application_header/ISO20022_MDR_bahV4_v1.pdf). Locator: one-based file pages 27 to 27.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 27

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  27
     BICFI <BICFI> [0..1] IdentifierSet C2 27
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 28
     LEI <LEI> [0..1] IdentifierSet 28
     Name <Nm> [0..1] Text 28
     PostalAddress <PstlAdr> [0..1] ± 28
     Other <Othr> [0..1] ± 29
   BranchIdentification <BrnchId> [0..1]  30
     Identification <Id> [0..1] Text 30
     LEI <LEI> [0..1] IdentifierSet 30
     Name <Nm> [0..1] Text 30
     PostalAddress <PstlAdr> [0..1] ± 30
3.1.1.2.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C2 27
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 28
   LEI <LEI> [0..1] IdentifierSet 28
   Name <Nm> [0..1] Text 28
   PostalAddress <PstlAdr> [0..1] ± 28
   Other <Othr> [0..1] ± 29
3.1.1.2.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 54
Approved by the Cross-SEG Harmonisation SEG on 20 February 2024 Message Items Types
Business Application Header - Version 4 27 March 2024
```

