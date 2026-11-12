---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Payments Clearing and Settlement"
source_ids: ["src-000163"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["10 Message Items Types", "10.1 MessageComponents", "10.1.7 Financial Institution Identification", "10.1.7.3 BranchAndFinancialInstitutionIdentification8", "10.1.7.3.1 FinancialInstitutionIdentification <FinInstnId>"]
file_pages: [1174]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 10.1.7.3.1 FinancialInstitutionIdentification <FinInstnId>

Source: [src-000163](../../../../../../../../../evidence/omitted/0b754f3040fa67a0a084bf38.md). Locator: one-based file pages 1174 to 1174.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1174

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  1174
     BICFI <BICFI> [0..1] IdentifierSet C5 1174
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
     LEI <LEI> [0..1] IdentifierSet 1175
     Name <Nm> [0..1] Text 1175
     PostalAddress <PstlAdr> [0..1] ± 1175
     Other <Othr> [0..1] ± 1176
   BranchIdentification <BrnchId> [0..1]  1177
     Identification <Id> [0..1] Text 1177
     LEI <LEI> [0..1] IdentifierSet 1177
     Name <Nm> [0..1] Text 1177
     PostalAddress <PstlAdr> [0..1] ± 1177
10.1.7.3.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C5 1174
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 1175
   LEI <LEI> [0..1] IdentifierSet 1175
   Name <Nm> [0..1] Text 1175
   PostalAddress <PstlAdr> [0..1] ± 1175
   Other <Othr> [0..1] ± 1176
10.1.7.3.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C5 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 1240
Approved by the Payments SEG on 12 January 2026 Message Items Types
Payments Clearing and Settlement - Maintenance 2025 -
2026
1174 March 2026
```

