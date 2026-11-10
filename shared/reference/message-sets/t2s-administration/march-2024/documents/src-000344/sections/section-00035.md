---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "shared"
message_set: "T2S Administration"
source_ids: ["src-000344"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["5 Message Items Types", "5.1 MessageComponents", "5.1.5 Financial Institution Identification", "5.1.5.2 BranchAndFinancialInstitutionIdentification8", "5.1.5.2.1 FinancialInstitutionIdentification <FinInstnId>"]
file_pages: [42]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 5.1.5.2.1 FinancialInstitutionIdentification <FinInstnId>

Source: [src-000344](../../../../../../../../raw-input/target2securities_t2s/ISO20022_MDR_Target2Securities_August_2026_v1.zip) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_Administration_MessageSet/ISO20022_MDRPart2_Target2Securities_Administration_2023_2024_v1.pdf`. Locator: one-based file pages 42 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 42

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   FinancialInstitutionIdentification <FinInstnId> [1..1]  42
     BICFI <BICFI> [0..1] IdentifierSet C2 42
     ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 43
     LEI <LEI> [0..1] IdentifierSet 43
     Name <Nm> [0..1] Text 43
     PostalAddress <PstlAdr> [0..1] ± 43
     Other <Othr> [0..1] ± 44
   BranchIdentification <BrnchId> [0..1]  45
     Identification <Id> [0..1] Text 45
     LEI <LEI> [0..1] IdentifierSet 45
     Name <Nm> [0..1] Text 45
     PostalAddress <PstlAdr> [0..1] ± 45
5.1.5.2.1  FinancialInstitutionIdentification <FinInstnId>
Presence: [1..1]
Definition: Unique and unambiguous identification of a financial institution, as assigned under an
internationally recognised or proprietary identification scheme.
FinancialInstitutionIdentification <FinInstnId> contains the following
FinancialInstitutionIdentification23 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICFI <BICFI> [0..1] IdentifierSet C2 42
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 43
   LEI <LEI> [0..1] IdentifierSet 43
   Name <Nm> [0..1] Text 43
   PostalAddress <PstlAdr> [0..1] ± 43
   Other <Othr> [0..1] ± 44
5.1.5.2.1.1  BICFI <BICFI>
Presence: [0..1]
Definition: Code allocated to a financial institution by the ISO 9362 Registration Authority as described
in ISO 9362 "Banking - Banking telecommunication messages - Business identifier code (BIC)".
Impacted by: C2 "BICFI"
Datatype: "BICFIDec2014Identifier" on page 67
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Administration - Maintenance 2023 -
2024
42 March 2024
```

